"""Tier 0 tests for scripts/run_report.py (run logging, ticket 06).

The report is rendered on the shipped fixtures, with no store access
(`--no-trace`): a workspace materialized from the real patch-array-5800
ledger slice (`scripts/fixtures/patch-array-5800/state.session1.md`), the
run's real machine state (`.../state/*`, byte for byte) and a trace written
from the real `neon-eagle` opencode slice by `run_trace`. Nothing here is
typed from memory (docs/agents/fixture-fidelity.md).

What is asserted: the one `PASS:` line and exit 1 only on a missing
workspace; the eleven sections in the ticket's order; byte-idempotency of
both files; every `unmeasurable` in the headline carrying a reason in
`run_card`'s wording; the findings the ledger records by hand present in
the JSON (both DESIGN misroutes, the late solve declaration, the readout
errors, the three watchdog runs); session discovery from a declared history,
from a declaration's `--name` in a transcript, and from a ledger slug; and
the degraded renderings (no trace, no store, no index).

Run: `python scripts/test_run_report.py`
"""

import contextlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
import run_card  # noqa: E402
import run_report  # noqa: E402
import run_trace  # noqa: E402
from hfss_spec import events, painpoints  # noqa: E402

FIXTURES = REPO / "scripts" / "fixtures"
STATE_DIR = FIXTURES / "patch-array-5800" / "state"
LEDGER_SLICE = FIXTURES / "patch-array-5800" / "state.session1.md"
OC_SLICE = FIXTURES / "opencode" / "ses_fe9ae6dd3ffe2a8knbeE1b4yrr.jsonl"
NEON = "ses_fe9ae6dd3ffe2a8knbeE1b4yrr"
READOUT = "e5cdcdf5-e3fe-4a62-9402-0e4010171c51"
HISTORY_FILE = "sessions.jsonl"
HOOK_PAYLOAD = FIXTURES / "hooks" / "PostToolUseFailure.toolu_01Wq4yd3xcssNi3976krgrPL.json"
NO_DB = "Z:/nonexistent/opencode.db"
# An empty Claude Code projects dir, so the declaration scan never reads
# this box's real transcripts (which do hold the 09-01 readout session).
NO_PROJECTS = tempfile.mkdtemp(prefix="no-projects-")
PASS_RE = re.compile(r"^PASS: run_report workspace=(\S+) sessions=(\d+)/(\d+) steps=(\d+) "
                     r"findings=(\d+) high=(\d+) trace=(\w+) index=(\d+)$")
REINDEX_RE = re.compile(r"^PASS: run_report reindex reports=(\d+) rows=(\d+) index=(\S+) changed=(yes|no)$")
REASONS = {run_card.REASON_NO_WORKSPACE, run_card.REASON_NO_START, run_card.REASON_NO_GATE,
           run_card.REASON_GATE_BEFORE_START, run_report.REASON_NO_TRACE,
           run_report.REASON_NO_STORE, run_report.REASON_NO_STATE}


def materialize(root, trace=True, state=True, ledger=True, history=False):
    """A workspace from the fixtures: real ledger slice, real state, a
    trace written from the real opencode slice. `history` adds ticket 10's
    backfilled `sessions.jsonl` (the run itself wrote none)."""
    ws = Path(root) / "patch-array-5800"
    state_dir = ws / "results" / "state"
    state_dir.mkdir(parents=True)
    if ledger:
        shutil.copy(LEDGER_SLICE, ws / "state.md")
    if state:
        for name in os.listdir(STATE_DIR):
            if name == HISTORY_FILE and not history:
                continue
            shutil.copy(STATE_DIR / name, state_dir / name)
    if trace:
        family = run_trace.trace_opencode_family(run_trace.SliceStore(OC_SLICE), NEON)
        for sid, steps in family.items():
            run_trace.write_steps(steps, ws / run_trace.TRACE_DIR, sid)
    return ws


def run_main(argv):
    """Drive main with an empty projects dir and, unless the test gives one,
    a throwaway index: a test must never append to docs/runs/index.jsonl."""
    argv = list(argv)
    if "--projects-dir" not in argv:
        argv += ["--projects-dir", NO_PROJECTS]
    if "--index" not in argv:
        argv += ["--index", os.path.join(tempfile.mkdtemp(prefix="no-index-"), "index.jsonl")]
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = run_report.main(argv)
    return code, out.getvalue(), err.getvalue()


def sections_of(text):
    return re.findall(r"(?m)^## \d+\. (.+)$", text)


class TestFixturesArePresent(unittest.TestCase):
    def test_corpus(self):
        for path in (STATE_DIR / "solve_progress.txt", STATE_DIR / "readouts.txt", LEDGER_SLICE, OC_SLICE):
            self.assertTrue(path.is_file(), path)


class TestReportOnTheFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.ws = materialize(cls.tmp)
        cls.code, cls.out, cls.err = run_main(["--workspace", str(cls.ws), "--no-trace", "--db", NO_DB])
        cls.md = (cls.ws / run_report.REPORT_MD).read_text(encoding="utf-8")
        cls.js = json.loads((cls.ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_one_pass_line_and_exit_zero(self):
        self.assertEqual(self.code, 0, self.err)
        lines = [ln for ln in self.out.splitlines() if ln.strip()]
        self.assertEqual(len(lines), 1)
        m = PASS_RE.match(lines[0])
        self.assertIsNotNone(m, lines[0])
        self.assertEqual(m.group(1), "patch-array-5800")
        self.assertEqual(int(m.group(4)), 954)                 # neon-eagle + its two subagents
        self.assertEqual(int(m.group(5)), len(self.js["findings"]))
        self.assertEqual(m.group(7), "kept")                   # --no-trace

    def test_both_files_next_to_summary_with_the_sections_in_order(self):
        self.assertEqual(sections_of(self.md), [title for _, title in run_report.SECTIONS])
        self.assertEqual(self.js["sections"], [key for key, _ in run_report.SECTIONS])
        self.assertTrue(self.md.startswith("# Run report — patch-array-5800\n"))
        self.assertTrue(self.md.endswith("\n"))

    def test_byte_idempotent(self):
        before = ((self.ws / run_report.REPORT_MD).read_bytes(), (self.ws / run_report.REPORT_JSON).read_bytes())
        code, out, _ = run_main(["--workspace", str(self.ws), "--no-trace", "--db", NO_DB])
        self.assertEqual(code, 0)
        after = ((self.ws / run_report.REPORT_MD).read_bytes(), (self.ws / run_report.REPORT_JSON).read_bytes())
        self.assertEqual(before, after)
        # The report's own event landed twice and is left out of the analysis.
        names = events.names(self.ws / "results" / "state")
        self.assertGreaterEqual(names.count(run_report.REPORT_EVENT), 2)
        self.assertEqual(self.js["headline"]["events"], 0)

    def test_every_unmeasurable_names_a_reason_in_run_card_wording(self):
        head = self.md.split("## 2.")[0]
        found = re.findall(r"unmeasurable: ([^\n|)]+)", head)
        self.assertTrue(found)
        for reason in found:
            self.assertIn(reason.strip(), REASONS, reason)
        wall = run_card.Wall(str(self.ws))
        self.assertFalse(wall.measurable)
        self.assertIn(f"- active_wall: {wall.label}\n", head)
        self.assertEqual(wall.label, f"{run_card.UNMEASURABLE}: {run_card.REASON_NO_GATE}")
        # The real ledger slice's Started line parses, so the start is measured.
        self.assertIn("- active_wall_start: 2026-08-18T09:27:37Z (state.md)", head)

    def test_headline_numbers_are_machine_derived(self):
        h = self.js["headline"]
        self.assertEqual(h["billed"], 2094310 + 76083 + 27888 + 1531 + 19966 + 1085)
        self.assertEqual(h["steps"], 954)
        self.assertEqual(h["recipe"], "corporate-patch-array")
        self.assertEqual(h["completions"], run_card.UNKNOWN_OUTCOME)
        self.assertTrue(h["outcome"].startswith(run_card.UNKNOWN_OUTCOME + " (outcome.txt is not key=value"))
        self.assertEqual(h["run_id"], "patch-array-5800-2026-08-18")
        self.assertIn("run.json absent", h["run_id_source"])
        self.assertEqual(sum(h["tokens_by_phase"].values()), h["billed"])
        self.assertEqual(sum(h["steps_by_phase"].values()), h["steps"])
        self.assertIn("no stage events recorded", h["attribution"])
        self.assertEqual(h["trace"], "3 session file(s), 954 steps")
        self.assertIn("solve_progress.txt", h["machine_state"])

    def test_the_ledgers_pain_points_are_in_the_findings(self):
        kinds = {}
        for f in self.js["findings"]:
            kinds.setdefault(f["kind"], []).append(f)
        misroutes = kinds["design_misroute"]
        self.assertEqual(sorted(f["steps"][0] for f in misroutes), [568, 743])
        self.assertFalse(any(f["evidence"].startswith("POSSIBLE") for f in misroutes))
        late = kinds["late_declaration"]
        self.assertTrue(any("watchdog_started=1787092156" in f["evidence"] for f in late))
        errors = kinds["backend_error"]
        self.assertTrue(any(f["source"] == "state" and "GetVariables x3" in f["evidence"] for f in errors))
        recycles = kinds["desktop_recycle"]
        self.assertTrue(any("Stop-Process -Id 29756" in f["evidence"] for f in recycles))
        self.assertTrue(any("port 55583 -> port 64077" in f["evidence"] for f in recycles))
        self.assertEqual(len(kinds["rebuild_chain"]), 3)
        # Section 2 is one row per kind (ticket 10), severity first, then
        # cost, so the state-sourced findings (0 tokens) are in it.
        top = self.js["top"]
        self.assertEqual(top, painpoints.kind_rows(self.js["findings"]))
        self.assertEqual([r["kind"] for r in top], [r["kind"] for r in painpoints.kind_rows(self.js["findings"])])
        self.assertEqual({r["kind"] for r in top}, set(kinds))
        section = self.md.split("## 2. Top pain points\n", 1)[1].split("\n## 3.", 1)[0]
        for needle in ("design.yaml compiled at seq 568", "design.yaml compiled at seq 743",
                       "GrpcApiError GetVariables x3 quoted by readouts.txt x2, z_act.txt x1",
                       "Stop-Process -Id 29756", "8 s before the solve declaration",
                       "session.json names readout-experiment-2026-09-01"):
            self.assertIn(needle, section, needle)
        highs = [r for r in top if r["severity"] == "high"]
        self.assertEqual(highs, top[:len(highs)])

    def test_solve_section_reads_the_watchdog(self):
        s = self.js["solve"]
        self.assertEqual([r["status"] for r in s["runs"]], ["complete"] * 3)
        self.assertEqual(s["submissions"]["count"], 3)
        self.assertEqual(s["submissions"]["source"], "watchdog runs in solve_progress.txt")
        self.assertEqual(s["runs"][0]["stages"]["Frequency_Sweep"], {"seconds": 173, "passes": None})
        self.assertEqual(s["runs"][2]["stages"]["Adaptive_Meshing"], {"seconds": 52, "passes": 14})
        self.assertEqual(s["runs"][0]["profile_status"], "normal_completion")
        self.assertEqual(s["bank"]["status"], "Normal Completion")
        self.assertEqual(s["bank"]["banked_at"], "2026-08-18T23:38:24Z")
        self.assertIn("| 2026-08-18T22:29:16Z | complete | done | 0 h 9 min 51 s | 30 |", self.md)

    def test_backend_and_waiting_and_context(self):
        routes = self.js["backend"]["readout_routes"]
        self.assertEqual(routes, [{"expression": "s11", "route": "both-failed", "source": "readouts.txt"}])
        w = self.js["waiting"]
        self.assertEqual(w["totals_ms"]["solver_wait"], 0)
        self.assertGreater(w["totals_ms"]["user_wait"], 60 * 60_000)
        self.assertEqual(sum(w["totals_ms"].values()), sum(g["wall_ms"] for g in w["gaps"]))
        c = self.js["context"]
        self.assertEqual(c["outputs"][0]["bytes"], 27707)
        self.assertTrue(c["outputs"][0]["command"].endswith("physics.py"))
        self.assertEqual(c["reasoning"][0]["bytes"], 60572)
        self.assertEqual(len(c["outputs"]), run_report.CONTEXT_N)

    def test_stage_rows_add_up(self):
        rows = self.js["stages"]
        self.assertEqual(sum(r["steps"] for r in rows), 954)
        self.assertTrue(all(r["stage_source"] == "commands" for r in rows))
        self.assertIn("`*` stage read off the command", self.md)

    def test_section_10_holds_this_run_last_and_only_its_recipe(self):
        rows = self.js["previous"]["rows"]
        self.assertIsNone(self.js["previous"]["note"])
        self.assertEqual([r["run_id"] for r in rows], ["patch-array-5800-2026-08-18"])   # the seeds are bowtie
        self.assertEqual(rows[-1]["delta"], {k: {"abs": None, "pct": None} for k in run_report.DELTA_KEYS})
        self.assertIn("\n## 10. Versus previous runs\n\n| " + " | ".join(run_report.COMPARE_HEADER) + " |\n", self.md)
        self.assertIn("| patch-array-5800-2026-08-18 | 2026-08-18T", self.md)
        self.assertIn("first of its recipe in the index", self.md)

    def test_run_card_is_the_last_section_in_run_card_wording(self):
        card = self.js["run_card"]
        self.assertTrue(card.startswith("## Run card\n\n- slug: "))
        tail = self.md.split("## 11. The run card\n\n", 1)[1]
        self.assertEqual(tail, card.split("\n", 1)[1].lstrip("\n"))
        self.assertIn(f"- parts: {run_card.UNMEASURABLE}: {run_report.REASON_NO_STORE}; steps=954\n", card)
        self.assertIn("- billed: 2220863\n", card)
        self.assertIn(f"- active_wall: {run_card.UNMEASURABLE}: {run_card.REASON_NO_GATE}\n", card)

    def test_index_row_has_ticket_07_columns(self):
        row = self.js["index_row"]
        self.assertEqual(set(row), {"run_id", "workspace", "recipe", "skill_commit", "host", "outcome",
                                    "completions", "billed", "billed_per_completion", "parts", "raw_wall_ms",
                                    "active_wall_ms", "started", "tokens_by_phase", "findings_high",
                                    "top_finding_kind", "report_path"})
        self.assertEqual(set(row), set(run_card.INDEX_COLUMNS))
        self.assertEqual(row["billed"], self.js["headline"]["billed"])
        self.assertIsNone(row["active_wall_ms"])
        self.assertIsNone(row["parts"])                        # trace only: the store's count is unknown
        self.assertTrue(row["started"].startswith("2026-08-18T"))
        self.assertEqual(row["started"], self.js["headline"]["started"])
        self.assertIn(f"- started: {row['started']} (first traced step)\n", self.md)
        self.assertTrue(row["report_path"].endswith("patch-array-5800/run-report.md"))

    def test_sessions_line_names_how_each_was_found(self):
        sessions = self.js["headline"]["sessions"]
        self.assertEqual(len(sessions), 1)
        self.assertEqual(sessions[0]["how"], "transcript scan: declaration --name readout-experiment-2026-09-01")
        self.assertFalse(sessions[0]["resolved"])
        self.assertTrue(sessions[0]["note"].startswith("unresolved: no Claude Code transcript declares it"))


class TestDegradedInputs(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_missing_workspace_is_the_only_exit_one(self):
        code, out, err = run_main(["--workspace", os.path.join(self.tmp, "nope")])
        self.assertEqual(code, 1)
        self.assertIn("workspace not found", err)
        self.assertEqual(out, "")

    def test_no_trace_no_store_still_renders_from_state(self):
        ws = materialize(self.tmp, trace=False)
        code, out, _ = run_main(["--workspace", str(ws), "--no-trace", "--db", NO_DB])
        self.assertEqual(code, 0)
        self.assertRegex(out.strip(), PASS_RE)
        self.assertIn("steps=0", out)
        js = json.loads((ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))
        h = js["headline"]
        self.assertEqual(h["trace"], "unavailable (0 file(s); --no-trace)")
        self.assertEqual(h["billed"], f"{run_card.UNMEASURABLE}: {run_report.REASON_NO_TRACE}")
        self.assertEqual(h["raw_wall"], f"{run_card.UNMEASURABLE}: {run_report.REASON_NO_TRACE}")
        self.assertEqual(sections_of((ws / run_report.REPORT_MD).read_text(encoding="utf-8")),
                         [title for _, title in run_report.SECTIONS])
        kinds = {f["kind"] for f in js["findings"]}
        self.assertTrue({"solve_anomaly", "backend_error", "desktop_recycle"} <= kinds)
        self.assertEqual(js["solve"]["submissions"]["count"], 3)
        self.assertIn(f"- parts: {run_card.UNMEASURABLE}", js["run_card"])

    def test_store_unavailable_is_reported_not_raised(self):
        ws = materialize(self.tmp)
        (ws / "state.md").write_text((ws / "state.md").read_text(encoding="utf-8")
                                     + "\n- run card (slug hidden-falcon)\n", encoding="utf-8")
        code, out, _ = run_main(["--workspace", str(ws), "--db", NO_DB,
                                 "--projects-dir", os.path.join(self.tmp, "no-projects")])
        self.assertEqual(code, 0)
        # Neither session resolves to an id, so nothing can be refreshed and
        # the trace on disk is kept and reported from.
        self.assertIn("sessions=0/2", out)
        self.assertIn("trace=kept", out)
        js = json.loads((ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))
        slug = next(s for s in js["headline"]["sessions"] if s["slug"] == "hidden-falcon")
        self.assertEqual(slug["how"], "ledger slug hidden-falcon")
        self.assertTrue(slug["note"].startswith("unresolved: database not found"))
        self.assertEqual(js["headline"]["steps"], 954)

    def test_no_machine_state_is_named_in_the_headline(self):
        ws = materialize(self.tmp, state=False, ledger=False)
        code, out, _ = run_main(["--workspace", str(ws), "--no-trace", "--db", NO_DB])
        self.assertEqual(code, 0)
        js = json.loads((ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))
        h = js["headline"]
        self.assertEqual(h["machine_state"], f"absent ({run_report.REASON_NO_STATE})")
        self.assertEqual(h["active_wall"], f"{run_card.UNMEASURABLE}: {run_card.REASON_NO_START}")
        self.assertEqual(h["outcome"], run_card.UNKNOWN_OUTCOME)
        self.assertEqual(h["recipe"], run_card.UNKNOWN_OUTCOME)
        self.assertEqual(js["solve"]["runs"], [])
        self.assertIn("- unmeasurable: no solve_submitted_at.txt and no watchdog run",
                      (ws / run_report.REPORT_MD).read_text(encoding="utf-8"))

    def test_previous_runs_from_an_index(self):
        ws = materialize(self.tmp)
        index = Path(self.tmp) / "index.jsonl"
        rows = [{"run_id": f"patch-array-5800-2026-07-0{i}", "workspace": f"pa-{i}", "recipe": "corporate-patch-array",
                 "outcome": "completed", "completions": 1, "billed": 1000 * i, "parts": 10 * i,
                 "billed_per_completion": str(1000 * i), "raw_wall_ms": 60_000 * i, "started": f"2026-07-0{i}T00:00:00Z",
                 "active_wall_ms": None, "findings_high": i, "top_finding_kind": "idle_gap"} for i in range(1, 8)]
        rows.append({"run_id": "bowtie-1", "recipe": "bowtie-5g-baseline", "outcome": "abandoned"})
        rows.append({"run_id": "patch-array-5800-2026-08-18", "workspace": "patch-array-5800",
                     "recipe": "corporate-patch-array", "billed": 1})                      # this run, stale
        rows.append({"run_id": "patch-array-5800-2026-09-09", "workspace": "pa-later",
                     "recipe": "corporate-patch-array", "started": "2026-09-09T00:00:00Z"})  # newer: not "previous"
        index.write_text("".join(json.dumps(r) + "\n" for r in rows) + "not json\n", encoding="utf-8")
        code, _, _ = run_main(["--workspace", str(ws), "--no-trace", "--db", NO_DB, "--index", str(index)])
        self.assertEqual(code, 0)
        js = json.loads((ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))
        shown = [r["run_id"] for r in js["previous"]["rows"]]
        self.assertEqual(shown, [f"patch-array-5800-2026-07-0{i}" for i in range(3, 8)]
                         + ["patch-array-5800-2026-08-18"])                         # last five before it, then itself
        self.assertIsNone(js["previous"]["note"])
        mine = js["previous"]["rows"][-1]
        self.assertEqual(mine["billed"], js["headline"]["billed"])                  # the fresh row, not the stale line
        self.assertEqual(mine["delta"]["billed"]["abs"], js["headline"]["billed"] - 7000)
        self.assertAlmostEqual(mine["delta"]["billed"]["pct"], (js["headline"]["billed"] - 7000) / 70.0)
        self.assertEqual(mine["delta"]["parts"], {"abs": None, "pct": None})
        md = (ws / run_report.REPORT_MD).read_text(encoding="utf-8")
        self.assertIn("| patch-array-5800-2026-07-07 | 2026-07-07T00:00:00Z | completed | 1 | 7,000 | +1,000 (+17%) "
                      "| 70 | +10 (+17%) | n/a | n/a | 7 | idle_gap |", md)
        self.assertIn("Deltas are against the row above; the last row is this run.", md)
        # The index now holds the fresh row in place of the stale one, plus the seeds.
        after = run_card.read_index(index)
        self.assertEqual(sum(1 for r in after if r["run_id"] == "patch-array-5800-2026-08-18"), 1)
        self.assertEqual(next(r for r in after if r["run_id"] == "patch-array-5800-2026-08-18")["billed"],
                         js["headline"]["billed"])
        ids = [r["run_id"] for r in after]
        self.assertEqual(ids[0], "bowtie-1")                                       # undated sorts first
        self.assertEqual(ids[-1], "patch-array-5800-2026-09-09")                   # oldest first, newest last
        self.assertLess(ids.index("silent-engine"), ids.index("shiny-canyon"))
        self.assertLess(ids.index("patch-array-5800-2026-07-07"), ids.index("silent-engine"))
        self.assertEqual(len(ids), 12)                                             # 7 + bowtie-1 + this + later + 2 seeds

    def test_top_limits_the_findings_shown_in_the_later_sections(self):
        ws = materialize(self.tmp)
        code, _, _ = run_main(["--workspace", str(ws), "--no-trace", "--db", NO_DB, "--top", "3"])
        self.assertEqual(code, 0)
        js = json.loads((ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))
        self.assertEqual(js["top_n"], 3)
        self.assertEqual(len(js["top"]), len({f["kind"] for f in js["findings"]}))   # section 2: every kind
        md = (ws / run_report.REPORT_MD).read_text(encoding="utf-8")
        self.assertIn("more not shown (all in run-report.json)", md)
        title = dict(run_report.SECTIONS)["retries"]
        section = md.split(f"## 5. {title}\n", 1)[1].split("\n## 6.", 1)[0]
        self.assertEqual(section.count("\n| ") - 1, 3)                        # header, separator, three rows


class TestRunsIndex(unittest.TestCase):
    """`docs/runs/index.jsonl` (ticket 07): appended idempotently by every
    report, rebuilt byte-identically by `--reindex`, read by `--compare`."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.index = Path(self.tmp) / "runs" / "index.jsonl"

    def _render(self, ws, index=None):
        return run_main(["--workspace", str(ws), "--no-trace", "--db", NO_DB, "--index", str(index or self.index)])

    def test_report_appends_its_row_once_after_the_seeds(self):
        ws = materialize(self.tmp)
        code, out, _ = self._render(ws)
        self.assertEqual(code, 0)
        self.assertEqual(PASS_RE.match(out.strip()).group(8), "3")
        first = self.index.read_bytes()
        rows = [json.loads(ln) for ln in first.decode("utf-8").splitlines()]
        self.assertEqual([r["run_id"] for r in rows], ["silent-engine", "shiny-canyon", "patch-array-5800-2026-08-18"])
        self.assertEqual([list(r) for r in rows[:2]], [list(run_card.SEED_COLUMNS)] * 2)
        self.assertEqual(list(rows[2]), list(run_card.INDEX_COLUMNS))
        self.assertEqual(rows[2], json.loads((ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))["index_row"])
        self.assertTrue(first.endswith(b"\n"))
        self.assertNotIn(b"\r", first)
        code, out, _ = self._render(ws)
        self.assertEqual(code, 0)
        self.assertEqual(self.index.read_bytes(), first)                      # replaced, not appended
        self.assertEqual(PASS_RE.match(out.strip()).group(8), "3")

    def test_reindex_rebuilds_the_index_byte_identically(self):
        root = Path(self.tmp) / "workspaces"
        root.mkdir()
        ws = materialize(root)
        (root / "no-report").mkdir()
        (root / "broken").mkdir()
        (root / "broken" / run_report.REPORT_JSON).write_text("{not json", encoding="utf-8")
        self.assertEqual(self._render(ws)[0], 0)
        appended = self.index.read_bytes()
        self.index.unlink()
        code, out, err = run_main(["--reindex", "--index", str(self.index), "--workspaces", str(root)])
        self.assertEqual(code, 0, err)
        m = REINDEX_RE.match(out.strip())
        self.assertIsNotNone(m, out)
        self.assertEqual((m.group(1), m.group(2), m.group(4)), ("1", "3", "yes"))
        self.assertIn("warning: skipped", err)
        self.assertIn("broken", err)
        self.assertEqual(self.index.read_bytes(), appended)
        code, out, _ = run_main(["--reindex", "--index", str(self.index), "--workspaces", str(root)])
        self.assertEqual(code, 0)
        self.assertEqual(REINDEX_RE.match(out.strip()).group(4), "no")
        self.assertEqual(self.index.read_bytes(), appended)
        # A hand-edited seed line does not survive either path.
        text = self.index.read_text(encoding="utf-8").replace('"billed": 398130', '"billed": 1')
        self.index.write_text(text, encoding="utf-8")
        self.assertEqual(self._render(ws)[0], 0)
        self.assertEqual(self.index.read_bytes(), appended)

    def test_compare_prints_the_recipe_rows_newest_last_with_deltas(self):
        ws = materialize(self.tmp)
        rows = [{"run_id": "pa-b", "workspace": "pa-b", "recipe": "corporate-patch-array", "outcome": "completed",
                 "completions": 1, "billed": 2000, "parts": 300, "active_wall_ms": 1_800_000,
                 "started": "2026-07-02T00:00:00Z", "findings_high": 2, "top_finding_kind": "retry_same_command"},
                {"run_id": "pa-a", "workspace": "pa-a", "recipe": "corporate-patch-array", "outcome": "completed",
                 "completions": 1, "billed": 1000, "parts": 200, "active_wall_ms": 1_200_000,
                 "started": "2026-07-01T00:00:00Z", "findings_high": 1, "top_finding_kind": "idle_gap"}]
        self.index.parent.mkdir(parents=True)
        self.index.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
        code, out, err = run_main(["--workspace", str(ws), "--compare", "--index", str(self.index)])
        self.assertEqual(code, 0, err)
        lines = out.splitlines()
        self.assertEqual(lines[0], "| " + " | ".join(run_report.COMPARE_HEADER) + " |")
        self.assertEqual(lines[2], "| pa-a | 2026-07-01T00:00:00Z | completed | 1 | 1,000 | - | 200 | - "
                                   "| 0 h 20 min 0 s | - | 1 | idle_gap |")
        self.assertEqual(lines[3], "| pa-b | 2026-07-02T00:00:00Z | completed | 1 | 2,000 | +1,000 (+100%) | 300 "
                                   "| +100 (+50%) | 0 h 30 min 0 s | +0 h 10 min 0 s (+50%) | 2 | retry_same_command |")
        self.assertEqual(len(lines), 4)                                          # the seeds are another recipe
        # Named runs, any recipe: the two seeds, newest last, the pilot's deltas vs the baseline.
        code, out, _ = run_main(["--compare", "shiny-canyon", "silent-engine", "--index", str(self.index)])
        self.assertEqual(code, 0)
        lines = out.splitlines()
        self.assertTrue(lines[2].startswith("| silent-engine (seed) | 2026-08-03T04:43:14Z | completed | 1 | 398,130 | - | 424 | - | n/a | - |"))
        self.assertTrue(lines[3].startswith("| shiny-canyon (seed) | 2026-08-06T03:56:43Z | abandoned | 0 | 1,579,333 "
                                            "| +1,181,203 (+297%) | 1,392 | +968 (+228%) | n/a | n/a |"))
        code, _, err = run_main(["--compare", "nope", "--index", str(self.index)])
        self.assertEqual(code, 1)
        self.assertIn("no run nope in", err)
        (ws / "state.md").write_text("# no recipe here\n", encoding="utf-8")
        code, _, err = run_main(["--workspace", str(ws), "--compare", "--index", str(self.index)])
        self.assertEqual(code, 1)
        self.assertIn("no `- Recipe:` line", err)

    def test_section_10_and_the_index_agree_after_the_report(self):
        ws = materialize(self.tmp)
        self.assertEqual(self._render(ws)[0], 0)
        js = json.loads((ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))
        indexed = next(r for r in run_card.read_index(self.index) if r["run_id"] == js["index_row"]["run_id"])
        shown = dict(js["previous"]["rows"][-1])
        shown.pop("delta")
        self.assertEqual(shown, indexed)
        code, out, _ = run_main(["--workspace", str(ws), "--compare", "--index", str(self.index)])
        self.assertEqual(code, 0)
        self.assertEqual(out, run_report.render_compare(js["previous"]["rows"]))


class TestSessionDiscovery(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_ledger_slugs_and_recipe(self):
        ws = Path(self.tmp) / "ws"
        ws.mkdir()
        (ws / "state.md").write_text("- Recipe: `corporate-patch-array` (Modal)\n- run card (slug hidden-falcon, runs 2)\n",
                                     encoding="utf-8")
        (ws / "summary.md").write_text("## Run card\n\n- slug: shiny-canyon\n- slug: hidden-falcon\n", encoding="utf-8")
        self.assertEqual(run_report.ledger_slugs(ws), ["hidden-falcon", "shiny-canyon"])
        self.assertEqual(run_report.recipe_of(ws), "corporate-patch-array")
        self.assertEqual(run_report.recipe_of(LEDGER_SLICE.parent), None)
        self.assertEqual(run_report.ledger_slugs(Path(self.tmp) / "none"), [])

    def test_declared_history_is_trusted_first(self):
        ws = materialize(self.tmp, trace=False)
        history = ws / "results" / "state" / "sessions.jsonl"
        history.write_text(json.dumps({"ts": "x", "ts_ms": 1, "phase": "clarify", "name": "p-clarify",
                                       "host": "opencode", "host_session_id": "ses_abc"}) + "\n", encoding="utf-8")
        args = run_report.main.__globals__["argparse"].Namespace(db=NO_DB, projects_dir=os.path.join(self.tmp, "p"),
                                                                  session=["claude-code:cc-1", "ses_zzz"])
        found = run_report.discover_sessions(ws, args)
        hows = [(s["host"], s["session_id"], s["how"]) for s in found]
        self.assertEqual(hows[0], ("opencode", "ses_abc", "declared"))
        self.assertIn(("claude-code", "cc-1", "cli"), hows)
        self.assertIn(("opencode", "ses_zzz", "cli"), hows)
        # the unnamed readout declaration in the real session.json is searched too
        self.assertTrue(any("readout-experiment-2026-09-01" in s["how"] for s in found))

    def test_transcript_declaring_matches_the_command_not_a_mention(self):
        projects = Path(self.tmp) / "projects" / "C--Users-me-Repos-HFSS-automation"
        projects.mkdir(parents=True)

        def record(sid, block, rtype="assistant"):
            return json.dumps({"type": rtype, "sessionId": sid, "timestamp": "2026-09-01T00:00:00.000Z",
                               "message": {"role": rtype, "content": [block]}})
        name = "readout-experiment-2026-09-01"
        decoy = record("decoy", {"type": "text", "text": f"session.json says --name {name}"}, "user") + "\n" \
            + record("decoy", {"type": "tool_use", "id": "t1", "name": "Bash",
                               "input": {"command": f"grep -l '--name {name}' *.jsonl"}}) + "\n"
        real = record("real", {"type": "tool_use", "id": "t2", "name": "Bash",
                               "input": {"command": "cd ws && cp a b; python scripts/session.py --workspace . "
                                                    f"--phase solve --name {name}"}}) + "\n"
        (projects / "decoy.jsonl").write_text(decoy, encoding="utf-8")
        (projects / "real.jsonl").write_text(real, encoding="utf-8")
        hit = run_report.transcript_declaring(name, projects.parent)
        self.assertIsNotNone(hit)
        self.assertEqual((hit[0].name, hit[1]), ("real.jsonl", "real"))
        self.assertIsNone(run_report.transcript_declaring("no-such-name", projects.parent))

    def test_refresh_trace_states(self):
        ws = materialize(self.tmp, trace=False)
        ns = run_report.main.__globals__["argparse"].Namespace
        self.assertEqual(run_report.refresh_trace(ws, [], ns(no_trace=False, db=NO_DB, projects_dir=None))["status"],
                         "unavailable")
        entry = run_report._entry("opencode", "ses_x", "cli")
        out = run_report.refresh_trace(ws, [entry], ns(no_trace=False, db=NO_DB, projects_dir=None))
        self.assertEqual(out["status"], "unavailable")
        self.assertIn("database not found", out["detail"])
        ws2 = materialize(Path(self.tmp) / "two")
        out = run_report.refresh_trace(ws2, [entry], ns(no_trace=False, db=NO_DB, projects_dir=None))
        self.assertEqual(out["status"], "fresh")
        self.assertIn("not traceable", out["detail"])
        self.assertEqual(run_report.refresh_trace(ws2, [entry], ns(no_trace=True))["status"], "kept")


class TestBackfilledWorkspace(unittest.TestCase):
    """Ticket 10: the workspace as it is committed — the run's real state
    plus the backfilled `sessions.jsonl` (eight lines, all `backfilled`)."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.ws = materialize(cls.tmp, history=True)
        cls.code, cls.out, cls.err = run_main(["--workspace", str(cls.ws), "--no-trace", "--db", NO_DB])
        cls.md = (cls.ws / run_report.REPORT_MD).read_text(encoding="utf-8")
        cls.js = json.loads((cls.ws / run_report.REPORT_JSON).read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_headline_says_the_history_is_backfilled_and_attribution_command_derived(self):
        self.assertEqual(self.code, 0, self.err)
        head = self.md.split("## 2.")[0]
        self.assertIn("- sessions.jsonl: 8 declaration(s), 8 backfilled by hand after the run "
                      "(scripts/fixtures/backfill.py): 8 record(s) of declarations the run made, "
                      "0 phase(s) the run never declared\n", head)
        self.assertIn("- stage attribution: command-derived: no stage events recorded (the run predates the "
                      "event log, ticket 03, and events cannot be backfilled) — stage read off each command, "
                      "else between-stages\n", head)
        self.assertIn("- active_wall_start: 2026-08-18T19:27:36Z (sessions.jsonl)\n", head)
        self.assertEqual(self.js["headline"]["history"],
                         {"declarations": 8, "backfilled": 8, "backfilled_by_run": 8,
                          "phases": ["clarify", "build", "solve"]})
        self.assertEqual(self.js["headline"]["skill_commit"], "2d47289")

    def test_sessions_are_the_histories_and_nothing_is_scanned_for_twice(self):
        sessions = self.js["headline"]["sessions"]
        self.assertEqual([(s["host"], s["session_id"], s["how"], s["resolved"]) for s in sessions],
                         [("opencode", NEON, "declared (backfilled history)", True),
                          ("claude-code", READOUT, "declared (backfilled history)", False)])
        self.assertIn(f"  - claude-code {READOUT} — declared (backfilled history) — unresolved: no trace file\n",
                      self.md)
        self.assertFalse(any("transcript scan" in s["how"] for s in sessions))
        self.assertEqual(run_report.unnamed_declarations(self.ws / "results" / "state"), [])
        self.assertIn("sessions=1/2", self.out)

    def test_the_five_ledger_items_are_in_section_2(self):
        section = self.md.split("## 2. Top pain points\n", 1)[1].split("\n## 3.", 1)[0]
        rows = [ln for ln in section.splitlines() if ln.startswith("| ") and not ln.startswith("| #")]
        for needle in ("design.yaml compiled at seq 568 under the DESIGN ws_common.py named before its edit at seq 596",
                       "design.yaml compiled at seq 743 under the DESIGN ws_common.py named before its edit at seq 791",
                       "GrpcApiError GetVariables x3 quoted by readouts.txt x2, z_act.txt x1 (readouts.txt: route=both-failed)",
                       "Stop-Process -Id 29756 -Force -ErrorAction SilentlyContinue; Start-Sleep -Second; "
                       "pin before the first kill: port 64554",
                       "solve submitted 2026-08-18T22:29:16Z (watchdog_started=1787092156) in phase build, "
                       "8 s before the solve declaration at 2026-08-18T22:29:24Z",
                       "session.json names readout-experiment-2026-09-01 (phase solve, 2026-09-01T19:01:49Z, "
                       "host -, session -) 331 h 23 min after the run's last recorded instant"):
            self.assertTrue(any(needle in row for row in rows), needle)
        self.assertNotIn("undeclared_session", section)          # the history declares the run

    def test_byte_idempotent(self):
        before = ((self.ws / run_report.REPORT_MD).read_bytes(), (self.ws / run_report.REPORT_JSON).read_bytes())
        code, _, _ = run_main(["--workspace", str(self.ws), "--no-trace", "--db", NO_DB])
        self.assertEqual(code, 0)
        self.assertEqual(before, ((self.ws / run_report.REPORT_MD).read_bytes(),
                                  (self.ws / run_report.REPORT_JSON).read_bytes()))


class TestHookedRefresh(unittest.TestCase):
    """The report's own trace refresh merges a hooked run's `tools.jsonl`
    (ticket 08's leftover): a database inflated from the real neon-eagle
    slice, a history naming it, one hook line shaped by `hook_log.line_for`
    from the real captured PostToolUseFailure payload."""

    def test_refresh_merges_the_tool_log(self):
        from test_run_trace import materialize_db
        import hook_log
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        ws = materialize(tmp, trace=False, history=True)
        db = materialize_db(OC_SLICE, os.path.join(tmp, "opencode.db"))
        family = run_trace.trace_opencode_family(run_trace.SliceStore(OC_SLICE), NEON)
        results = {s["tool_use_id"]: s for s in family[NEON] if s["kind"] == "tool_result"}
        use = next(s for s in family[NEON] if s["kind"] == "tool_use" and s["tool"] in painpoints.BASH_TOOLS
                   and s.get("command") and not results[s["tool_use_id"]]["is_error"])
        payload = json.loads(HOOK_PAYLOAD.read_text(encoding="utf-8"))
        line = hook_log.line_for(payload, "solve", use["ts"], use["ts"] + 4321)
        self.assertEqual((line["exit_code"], line["is_error"], line["duration_ms"]), (3, True, 4321))
        # The real line's shape, re-addressed to the traced call (the hook
        # never ran on 2026-08-18): no tool_use_id, so it joins by shape.
        line.update(session_id=NEON, tool=use["tool"], command=use["command"], tool_use_id=None)
        tools = ws / "results" / "state" / run_trace.TOOLS_FILE
        tools.write_text(json.dumps(line) + "\n", encoding="utf-8")
        code, out, err = run_main(["--workspace", str(ws), "--db", db])
        self.assertEqual(code, 0, err)
        self.assertIn("trace=refreshed", out)
        steps = run_trace.read_steps(ws / run_trace.TRACE_DIR / f"{NEON}{run_trace.STEPS_SUFFIX}")
        traced = {(s["kind"], s["tool_use_id"]): s for s in steps}
        self.assertEqual(traced[("tool_use", use["tool_use_id"])]["latency_ms"], 4321)
        self.assertTrue(traced[("tool_result", use["tool_use_id"])]["is_error"])
        detail = next(e["detail"] for e in events.read(ws / "results" / "state")
                      if e["event"] == run_report.REPORT_EVENT)
        self.assertIn("hooked=1", detail)
        # Without the log the same refresh merges nothing.
        tools.unlink()
        shutil.rmtree(ws / run_trace.TRACE_DIR)
        code, out, _ = run_main(["--workspace", str(ws), "--db", db])
        self.assertEqual(code, 0)
        steps = run_trace.read_steps(ws / run_trace.TRACE_DIR / f"{NEON}{run_trace.STEPS_SUFFIX}")
        traced = {(s["kind"], s["tool_use_id"]): s for s in steps}
        self.assertNotEqual(traced[("tool_use", use["tool_use_id"])]["latency_ms"], 4321)
        self.assertFalse(traced[("tool_result", use["tool_use_id"])]["is_error"])


class TestStageLedger(unittest.TestCase):
    def test_real_terminal_lines(self):
        text = (STATE_DIR / "solve_progress.txt").read_text(encoding="utf-8")
        runs = painpoints.watchdog_runs(text)
        self.assertEqual(run_report.stage_ledger(runs[0]["line"]),
                         {"Initial_Meshing": {"seconds": 4, "passes": None},
                          "Adaptive_Meshing": {"seconds": 5, "passes": 2},
                          "Frequency_Sweep": {"seconds": 173, "passes": None}})
        self.assertEqual(run_report.stage_ledger(text.splitlines()[0]), {})    # stage_ledger=-
        self.assertEqual(run_report.stage_ledger(None), {})


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: run_report tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
