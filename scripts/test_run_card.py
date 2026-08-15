"""Unit tests for scripts/run_card.py (feature hfss-agent-perf-refactor,
tickets 01 + 11).

Seam under test (spec Seam 1): the run-card harness emits the baseline
numbers from the opencode session database, plus the ticket-11 wall axis:
raw wall and active wall (ledger session-1 start -> solve_submitted_at
gate) side by side, unmeasurable-marking when a boundary is absent, and
the verdict-table gate (active wall compared only when the baseline's
build-to-solve window is derivable, informational otherwise). Tests use
fixture databases (small SQLite files with the session/project/part shape)
and fixture workspaces (state.md + results/state/), never the live opencode
DB. Expected values are independent hand-written literals (analysis doc
section 1 figures).

Usage: python scripts/test_run_card.py
"""

import contextlib
import io
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_card  # noqa: E402

SCHEMA = """
CREATE TABLE project (
    id TEXT, worktree TEXT, name TEXT
);
CREATE TABLE session (
    id TEXT PRIMARY KEY, project_id TEXT, workspace_id TEXT, parent_id TEXT,
    slug TEXT, directory TEXT, path TEXT, title TEXT, version TEXT,
    share_url TEXT, summary_additions TEXT, summary_deletions TEXT,
    summary_files TEXT, summary_diffs TEXT, metadata TEXT, cost REAL,
    tokens_input INTEGER, tokens_output INTEGER, tokens_reasoning INTEGER,
    tokens_cache_read INTEGER, tokens_cache_write INTEGER, revert TEXT,
    permission TEXT, agent TEXT, model TEXT,
    time_created INTEGER, time_updated INTEGER,
    time_compacting INTEGER, time_archived INTEGER
);
CREATE TABLE part (
    id TEXT PRIMARY KEY, message_id TEXT, session_id TEXT,
    time_created INTEGER, time_updated INTEGER, data BLOB
);
"""

HFSS_PROJECT_ID = "pid-hfss"

# Baseline literals from docs/hfss-agent-performance-analysis.md section 1.
BASELINE = dict(
    slug="silent-engine",
    created_ms=1785732194154,
    updated_ms=1785737232452,
    tokens_input=329760,
    tokens_output=68370,
    tokens_reasoning=0,
    tokens_cache_read=9186701,
    tokens_cache_write=0,
    billed=398130,
    parts=424,
    store_bytes=1082759,
)

_SESSION_INSERT = (
    "INSERT INTO session (id, project_id, slug, tokens_input,"
    " tokens_output, tokens_reasoning, tokens_cache_read,"
    " tokens_cache_write, time_created, time_updated)"
    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
)


def _insert_session(con, sid, project_id, s):
    con.execute(
        _SESSION_INSERT,
        (
            sid, project_id, s["slug"], s.get("tokens_input", 0),
            s.get("tokens_output", 0), s.get("tokens_reasoning", 0),
            s.get("tokens_cache_read", 0), s.get("tokens_cache_write", 0),
            s["created_ms"], s["updated_ms"],
        ),
    )
    parts = s.get("parts", 0)
    base, extra = divmod(s.get("store_bytes", 0), parts) if parts else (0, 0)
    for j in range(parts):
        data = b"x" * (base + (extra if j == parts - 1 else 0))
        con.execute(
            "INSERT INTO part (id, message_id, session_id, data)"
            " VALUES (?, ?, ?, ?)",
            (f"{sid}-{j}", f"m-{sid}-{j}", sid, data),
        )


LEDGER_STARTED = "2026-08-05T14:00:00Z"
LEDGER_GATE = "2026-08-05T15:40:00Z"  # started + 1 h 40 min


def _gate_epoch():
    return datetime(2026, 8, 5, 15, 40, tzinfo=timezone.utc).timestamp()


def write_workspace(root, started=True, gate=True):
    """Fixture workspace: state.md (optional session-1 Started) + solve gate."""
    ws = Path(root) / "ws"
    (ws / "results" / "state").mkdir(parents=True, exist_ok=True)
    ledger = (
        "# State ledger - fixture\n\n"
        "## Session 1 - Clarification (locked in the UI, never changed after)\n\n"
    )
    if started:
        ledger += f"- Started: {LEDGER_STARTED}\n"
    ledger += (
        "- Recipe: bowtie-5g-baseline\n"
        "- Assumptions: none\n"
        "- Approved Result QA signals: convergence; in-band resonance\n\n"
        "## Session 2 - Build\n"
    )
    (ws / "state.md").write_text(ledger, encoding="utf-8")
    if gate:
        (ws / "results" / "state" / run_card.SOLVE_SUBMITTED_FILE).write_text(
            f"{_gate_epoch()}\n", encoding="utf-8")
    return ws


def make_db(path, sessions, foreign_sessions=()):
    """Build a fixture DB: HFSS project sessions + optional other-project ones."""
    con = sqlite3.connect(path)
    con.executescript(SCHEMA)
    con.execute(
        "INSERT INTO project (id, worktree, name) VALUES (?, ?, ?)",
        (HFSS_PROJECT_ID, "C:/Users/afpim/Repos/HFSS_automation", "HFSS_automation"),
    )
    con.execute(
        "INSERT INTO project (id, worktree, name) VALUES (?, ?, ?)",
        ("pid-other", "C:/Users/afpim/Repos/Other", "Other"),
    )
    for i, s in enumerate(sessions):
        _insert_session(con, f"sid-{i}", HFSS_PROJECT_ID, s)
    for i, s in enumerate(foreign_sessions):
        _insert_session(con, f"fid-{i}", "pid-other", s)
    con.commit()
    con.close()


class CardPrintTest(unittest.TestCase):
    def run_cli(self, db_path, args):
        """Drive main([--db db_path] + args); return (code, stdout, stderr)."""
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = run_card.main(["--db", str(db_path)] + args)
        return code, out.getvalue(), err.getvalue()

    def test_slug_invocation_prints_full_card(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            code, text, _ = self.run_cli(db, ["--slug", "silent-engine"])
        self.assertEqual(code, 0)
        self.assertIn("slug: silent-engine", text)
        self.assertIn("created: 2026-08-03T04:43:14Z", text)
        self.assertIn("updated: 2026-08-03T06:07:12Z", text)
        self.assertIn("tokens_input: 329760", text)
        self.assertIn("tokens_output: 68370", text)
        self.assertIn("tokens_reasoning: 0", text)
        self.assertIn("tokens_cache_read: 9186701", text)
        self.assertIn("tokens_cache_write: 0", text)
        self.assertIn("billed: 398130", text)
        self.assertIn("parts: 424", text)
        self.assertIn("store_bytes: 1082759", text)
        self.assertIn("duration", text)

    def test_unknown_slug_fails_cleanly(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            code, _, err = self.run_cli(db, ["--slug", "nope"])
        self.assertEqual(code, 1)
        self.assertIn("no session", err)

    def test_latest_picks_newest_hfss_session(self):
        older = dict(BASELINE, slug="quiet-forest", created_ms=1785814248403,
                     updated_ms=1785819574679, tokens_input=326291,
                     tokens_output=79181, tokens_cache_read=11835770,
                     billed=405472, parts=565, store_bytes=1038263)
        newest = dict(BASELINE, slug="shiny-star", created_ms=1785819586728,
                      updated_ms=1785819595911, tokens_input=11477,
                      tokens_output=187, billed=11664, parts=13,
                      store_bytes=10849)
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [older, newest])
            code, text, _ = self.run_cli(db, ["--latest"])
        self.assertEqual(code, 0)
        self.assertIn("slug: shiny-star", text)
        self.assertNotIn("slug: quiet-forest", text)

    def test_latest_ignores_newer_sessions_outside_hfss_project(self):
        foreign_newest = dict(BASELINE, slug="zulu", created_ms=9999999999999,
                              updated_ms=9999999999999, billed=1, parts=1,
                              store_bytes=16)
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE], foreign_sessions=[foreign_newest])
            code, text, _ = self.run_cli(db, ["--latest"])
        self.assertEqual(code, 0)
        self.assertIn("slug: silent-engine", text)

    def test_db_flag_beats_env_var_and_env_var_beats_default(self):
        other = dict(BASELINE, slug="from-flag", billed=1, parts=1, store_bytes=16)
        env = dict(BASELINE, slug="from-env", billed=2, parts=1, store_bytes=16)
        with tempfile.TemporaryDirectory() as td:
            flag_db = Path(td) / "flag.db"
            env_db = Path(td) / "env.db"
            make_db(flag_db, [other])
            make_db(env_db, [env])
            saved = os.environ.get(run_card.ENV_DB)
            try:
                os.environ[run_card.ENV_DB] = str(env_db)
                code, text, _ = self.run_cli(flag_db, ["--latest"])
                self.assertEqual(code, 0)
                self.assertIn("slug: from-flag", text)
                out, err = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    code = run_card.main(["--latest"])
                self.assertEqual(code, 0)
                self.assertIn("slug: from-env", out.getvalue())
            finally:
                if saved is None:
                    os.environ.pop(run_card.ENV_DB, None)
                else:
                    os.environ[run_card.ENV_DB] = saved

    def test_read_only_even_while_a_writer_holds_the_db(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            writer = sqlite3.connect(str(db))
            writer.execute("PRAGMA journal_mode=WAL")
            writer.execute("BEGIN IMMEDIATE")
            writer.execute(
                "UPDATE session SET tokens_input = 1 WHERE slug = 'silent-engine'"
            )
            before = db.stat()
            try:
                try:
                    code, text, _ = self.run_cli(db, ["--slug", "silent-engine"])
                finally:
                    writer.rollback()
                    writer.close()
            finally:
                after = db.stat()
            self.assertEqual(code, 0)
            self.assertIn("tokens_input: 329760", text)
            self.assertEqual((before.st_size, before.st_mtime_ns),
                             (after.st_size, after.st_mtime_ns))

    BODY = (
        "# Summary — bowtie-3500\n\n"
        "## What the Model is\n\n"
        "- Design: Bowtie3500\n\n"
        "## Results\n\n<not solved yet>\n\n"
    )

    def test_summary_appends_section_and_keeps_rest(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            summary = Path(td) / "summary.md"
            summary.write_text(self.BODY, encoding="utf-8")
            code, _, _ = self.run_cli(db, ["--slug", "silent-engine",
                                           "--summary", str(summary)])
            after = summary.read_text(encoding="utf-8")
        self.assertEqual(code, 0)
        self.assertIn("## Run card", after)
        self.assertIn("- slug: silent-engine", after)
        self.assertIn("- billed: 398130", after)
        self.assertIn("## What the Model is", after)
        self.assertIn("## Results", after)

    def test_summary_is_idempotent_across_two_runs(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            summary = Path(td) / "summary.md"
            summary.write_text(self.BODY, encoding="utf-8")
            first, _, _ = self.run_cli(db, ["--slug", "silent-engine",
                                            "--summary", str(summary)])
            after_first = summary.read_text(encoding="utf-8")
            _, second, _ = self.run_cli(db, ["--slug", "silent-engine",
                                             "--summary", str(summary)])
            after_second = summary.read_text(encoding="utf-8")
        self.assertEqual(after_first, after_second)
        self.assertEqual(after_first.count("## Run card"), 1)

    def test_summary_replaces_mid_file_run_card_section(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            summary = Path(td) / "summary.md"
            summary.write_text(
                self.BODY.replace("## Results",
                                  "## Run card\n\n-stale: x\n\n## Results"),
                encoding="utf-8")
            self.run_cli(db, ["--slug", "silent-engine", "--summary", str(summary)])
            after = summary.read_text(encoding="utf-8")
        self.assertIn("- slug: silent-engine", after)
        self.assertNotIn("-stale: x", after)
        self.assertIn("## Results", after)

    def test_summary_creates_section_in_empty_file(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            summary = Path(td) / "summary.md"
            summary.write_text("", encoding="utf-8")
            self.run_cli(db, ["--slug", "silent-engine", "--summary", str(summary)])
            after = summary.read_text(encoding="utf-8")
        self.assertIn("## Run card", after)
        self.assertIn("- slug: silent-engine", after)
        self.assertTrue(after.startswith("## Run card"))

    def test_active_wall_printed_raw_and_active_side_by_side(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            ws = write_workspace(td)
            code, text, _ = self.run_cli(
                db, ["--slug", "silent-engine", "--workspace", str(ws)])
        self.assertEqual(code, 0)
        self.assertIn("duration: 1 h 23 min 58 s", text)
        self.assertIn(f"active_wall_start: {LEDGER_STARTED}", text)
        self.assertIn(f"solve_gate: {LEDGER_GATE}", text)
        self.assertIn("active_wall: 1 h 40 min 0 s", text)
        self.assertNotIn("unmeasurable", text)

    def test_active_wall_unmeasurable_without_solve_gate(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            ws = write_workspace(td, gate=False)
            code, text, _ = self.run_cli(
                db, ["--slug", "silent-engine", "--workspace", str(ws)])
        self.assertEqual(code, 0)
        self.assertIn(f"active_wall_start: {LEDGER_STARTED}", text)
        self.assertIn("solve_gate: n/a", text)
        self.assertIn("active_wall: unmeasurable: no solve_gate timestamp", text)

    def test_active_wall_unmeasurable_without_workspace(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            code, text, _ = self.run_cli(db, ["--slug", "silent-engine"])
        self.assertEqual(code, 0)
        self.assertIn("active_wall: unmeasurable: no workspace state", text)

    def test_active_wall_unmeasurable_without_ledger_start(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            ws = write_workspace(td, started=False)
            code, text, _ = self.run_cli(
                db, ["--slug", "silent-engine", "--workspace", str(ws)])
        self.assertEqual(code, 0)
        self.assertIn("active_wall_start: n/a", text)
        self.assertIn("active_wall: unmeasurable: no session-1 start in state.md",
                      text)

    def test_workspace_derived_from_summary_parent(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            ws = write_workspace(td)
            summary = ws / "summary.md"
            summary.write_text(self.BODY, encoding="utf-8")
            code, _, _ = self.run_cli(
                db, ["--slug", "silent-engine", "--summary", str(summary)])
            text = summary.read_text(encoding="utf-8")
        self.assertEqual(code, 0)
        self.assertIn(f"- active_wall_start: {LEDGER_STARTED}", text)
        self.assertIn("- active_wall: 1 h 40 min 0 s", text)

    def test_verdict_wall_informational_when_baseline_window_not_derivable(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            ws = write_workspace(td)
            code, text, _ = self.run_cli(
                db, ["--slug", "silent-engine", "--workspace", str(ws),
                     "--verdict"])
        self.assertEqual(code, 0)
        self.assertIn("| Metric", text)
        self.assertIn("| billed tokens", text)
        self.assertIn("| parts", text)
        self.assertIn("| wall (active: start -> solve gate)", text)
        self.assertIn("informational - baseline build-to-solve window not "
                      "derivable", text)
        wall_row = [ln for ln in text.splitlines()
                    if ln.startswith("| wall (active")][0]
        cells = [c.strip() for c in wall_row.strip().strip("|").split("|")]
        self.assertIn("informational", cells[3])
        self.assertEqual(cells[5], "-")  # not gated

    def test_verdict_wall_compared_when_baseline_window_derivable(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            ws = write_workspace(td)
            con = run_card.connect(db)
            try:
                card = run_card.load_card(con, slug="silent-engine")
            finally:
                con.close()
            wall = run_card.Wall(ws)
            faster = dict(run_card.BASELINE, active_wall_ms=4 * 60 * 60 * 1000)
            table = run_card.verdict_table(card, wall, baseline=faster)
        self.assertIn("**-58%**", table)
        self.assertEqual(table.count("PASS"), 1)   # only the wall row passes
        self.assertEqual(table.count("FAIL"), 2)   # billed + parts rows
        self.assertNotIn("informational", table)

    def test_verdict_wall_informational_when_ours_unmeasurable(self):
        with tempfile.TemporaryDirectory() as td:
            db = Path(td) / "opencode.db"
            make_db(db, [BASELINE])
            con = run_card.connect(db)
            try:
                card = run_card.load_card(con, slug="silent-engine")
            finally:
                con.close()
            wall = run_card.Wall(None)
            faster = dict(run_card.BASELINE, active_wall_ms=4 * 60 * 60 * 1000)
            table = run_card.verdict_table(card, wall, baseline=faster)
        wall_row = [ln for ln in table.splitlines()
                    if ln.startswith("| wall (active")][0]
        self.assertIn("informational - active wall unmeasurable", table)
        cells = [c.strip() for c in wall_row.strip().strip("|").split("|")]
        self.assertIn("informational", cells[3])
        self.assertEqual(cells[5], "-")  # not gated


class TestOutcome(unittest.TestCase):
    """Cost per completed simulation (ticket 04).

    Tokens per run scores the pilot as 4x worse than baseline. It delivered
    nothing, so the honest score is infinitely worse; these tests pin that.
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _workspace(self, body=None):
        state = Path(self.tmp) / "results" / "state"
        state.mkdir(parents=True, exist_ok=True)
        if body is not None:
            (state / run_card.OUTCOME_FILE).write_text(body, encoding="utf-8")
        return self.tmp

    def test_unrecorded_outcome_is_never_guessed(self):
        outcome = run_card.Outcome(self._workspace())
        self.assertEqual(outcome.label, run_card.UNKNOWN_OUTCOME)
        self.assertEqual(outcome.cost_label(398130), run_card.UNKNOWN_OUTCOME)

    def test_completed_run_costs_its_billed_tokens(self):
        outcome = run_card.Outcome(
            self._workspace("outcome=completed\ncompletions=1\n"))
        self.assertEqual(outcome.label, "completed")
        self.assertEqual(outcome.cost_label(398130), "398,130")

    def test_abandoned_run_costs_infinity_not_four_times_baseline(self):
        outcome = run_card.Outcome(self._workspace("outcome=abandoned\n"))
        self.assertEqual(outcome.completions, 0)
        self.assertIn("infinite", outcome.cost_label(1579333))
        self.assertIn("0 completed", outcome.cost_label(1579333))

    def test_escalated_run_also_has_no_completions(self):
        outcome = run_card.Outcome(self._workspace("outcome=escalated\n"))
        self.assertEqual(outcome.completions, 0)
        self.assertIn("infinite", outcome.cost_label(100))

    def test_sweep_divides_across_completions(self):
        outcome = run_card.Outcome(
            self._workspace("outcome=completed\ncompletions=8\n"))
        label = outcome.cost_label(240000)
        self.assertTrue(label.startswith("30,000"))
        self.assertIn("8 completed", label)

    def test_cli_overrides_the_workspace_file(self):
        workspace = self._workspace("outcome=completed\ncompletions=1\n")
        outcome = run_card.Outcome(workspace, outcome="abandoned", completions=0)
        self.assertIn("infinite", outcome.cost_label(500))

    def test_escape_hatch_and_note_are_carried(self):
        outcome = run_card.Outcome(self._workspace(
            "outcome=completed\nescape_hatch_scripts=2\nnote=horn flare\n"))
        self.assertEqual(outcome.escape_hatch_label, "2")
        self.assertIn("horn flare", outcome.label)

    def test_garbage_values_do_not_crash_or_invent_numbers(self):
        outcome = run_card.Outcome(self._workspace(
            "outcome=nonsense\ncompletions=many\nescape_hatch_scripts=\n"))
        self.assertIsNone(outcome.outcome)
        self.assertIsNone(outcome.completions)
        self.assertEqual(outcome.escape_hatch_label, run_card.UNKNOWN_OUTCOME)

    def test_metrics_appear_on_the_card(self):
        card = {"slug": "s", "time_created": None, "time_updated": None,
                "duration_ms": None, "tokens_input": 0, "tokens_output": 0,
                "tokens_reasoning": 0, "tokens_cache_read": 0,
                "tokens_cache_write": 0, "billed": 1579333, "parts": 1392,
                "storesize": 0}
        text = run_card.render_card(card, None,
                                    run_card.Outcome(None, outcome="abandoned"))
        self.assertIn("outcome: abandoned", text)
        self.assertIn("billed_per_completed_sim: infinite", text)


if __name__ == "__main__":
    raise SystemExit(unittest.main())
