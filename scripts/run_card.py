"""Print the run card for a session, from the harness's own session store.

Two harnesses run the skill, and each keeps sessions differently:

- **opencode** — the session database (`~/.local/share/opencode/opencode.db`,
  `session` / `part` / `project` tables). The reference backend; the card's
  metrics were defined against it.
- **Claude Code** — one JSONL transcript per session under
  `~/.claude/projects/`; read through `scripts/claude_transcript.py`, which
  states how every metric maps. Selected by `--host claude-code`, by
  `--session-id` / `--transcript`, by a workspace whose declared session
  (`results/state/session.json`, written by `scripts/session.py`) says it
  ran under Claude Code, or by the `CLAUDE_CODE_SESSION_ID` variable that
  Claude Code exports to every shell command. An explicit `--db` (or the
  `OPENCODE_DB` variable) always means opencode. Otherwise opencode is
  assumed, exactly as before.

The card always names its `host`, so a number from one harness is never
mistaken for the other's.

A run is three phase sessions plus their subagents (run logging, ticket 01).
When a workspace's `results/state/sessions.jsonl` — appended by every
`scripts/session.py --phase` declaration — lists the sessions, `--workspace`
(or `--summary`) with no explicit session selection cards **every** declared
session, one card each, folds in the subagent transcripts of each Claude Code
session (`scripts/claude_subagents.py`), and closes with a `## Run total`
block carrying the run's identity (`run.json`), the wall axis, the outcome
and the summed cost. A workspace that only has the older single
`session.json` cards that one session exactly as before.

Part of the hfss-agent-perf-refactor measurement harness (ticket 01): every
optimization is judged against the numbers this card emits, so the card is
derived from the reference SQL in
docs/hfss-agent-performance-analysis.md section 10.

Wall-time acceptance axis (ticket 11): active wall = Clarification session
start -> the user-gated solver submission instant (solver physics, idle
gaps and post-solve time are out). The start boundary is the ledger's
session-1 "- Started:" line (state.md header block, written once by the
Clarification session); the gate boundary is the machine-state file
results/state/solve_submitted_at.txt (written when the user approves the
solve submission). The card reports raw wall (duration) and active wall
side by side; a missing boundary is reported as "unmeasurable: ...", never
guessed. The verdict-table helper compares active wall only when the
baseline's build-to-solve window is derivable the same way; otherwise the
wall row is marked informational.

The database is opened read-only (WAL-safe while opencode is running) with
a generous busy timeout. Stdlib only, Python 3.10 compatible.

Usage:
    python scripts/run_card.py --slug <slug> [--db PATH] [--workspace DIR]
    python scripts/run_card.py --latest [--db PATH] [--verdict]
    python scripts/run_card.py --slug <slug> --summary <path>/summary.md
    python scripts/run_card.py --latest --summary <path>/summary.md --verdict
    python scripts/run_card.py --summary <path>/summary.md      # Claude Code:
        # the workspace's declared session id, recorded by scripts/session.py
    python scripts/run_card.py --host claude-code --session-id <id> ...
    python scripts/run_card.py --transcript <path>.jsonl ...

--workspace DIR points at a workspace directory (state.md + results/state/);
when --summary is given and --workspace is not, the summary's parent
directory is used. The database path resolves in order: --db flag,
OPENCODE_DB env var, default ~/.local/share/opencode/opencode.db. The
Claude Code projects dir resolves: --projects-dir, CLAUDE_PROJECTS_DIR,
default ~/.claude/projects.
"""

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
import claude_subagents  # noqa: E402
import claude_transcript  # noqa: E402
from hfss_spec import session as phase_session  # noqa: E402

DEFAULT_DB = Path.home() / ".local" / "share" / "opencode" / "opencode.db"
ENV_DB = "OPENCODE_DB"
PROJECT_MARKER = "HFSS_automation"

HOST_OPENCODE = "opencode"
HOST_CLAUDE_CODE = claude_transcript.HOST
HOSTS = (HOST_OPENCODE, HOST_CLAUDE_CODE)
SESSION_STATE_FILE = phase_session.STATE_FILE        # session.json
SESSIONS_HISTORY_FILE = phase_session.HISTORY_FILE   # sessions.jsonl
RUN_FILE = phase_session.RUN_FILE                    # run.json
TOKEN_KEYS = ("tokens_input", "tokens_output", "tokens_reasoning",
              "tokens_cache_read", "tokens_cache_write")
SUM_KEYS = TOKEN_KEYS + ("billed", "parts", "storesize")

SOLVE_SUBMITTED_FILE = "solve_submitted_at.txt"
UNMEASURABLE = "unmeasurable"
REASON_NO_WORKSPACE = "no workspace state (no --workspace/--summary)"
REASON_NO_START = "no session-1 start in state.md"
# Where the session-1 start came from: the machine record first (the clarify
# declaration in sessions.jsonl, ticket 01), the hand-written ledger second.
START_SOURCE_HISTORY = SESSIONS_HISTORY_FILE
START_SOURCE_LEDGER = "state.md"
REASON_NO_GATE = "no solve_gate timestamp"
REASON_GATE_BEFORE_START = "solve gate precedes session start"

# Baseline literals from docs/hfss-agent-performance-analysis.md section 1
# (silent-engine, 2026-08-03), captured by ticket 01. Its build-to-solve
# window was never recorded (no ledger/machine state existed then), so
# active_wall_ms stays None: the wall axis is informational until a
# baseline measured the same way exists.
BASELINE = {
    "label": "silent-engine",
    "billed": 398130,
    "parts": 424,
    "active_wall_ms": None,
    # Re-scored under the ticket-04 metric: this run delivered one solved,
    # readable simulation, so its cost per completed simulation IS its
    # billed total.
    "outcome": "completed",
    "completions": 1,
}

# The pilot, re-scored the same way. Kept as a named constant because it is
# the case the metric exists for: per-run it looks 4x worse than baseline;
# per completed simulation it is infinitely worse, because it delivered no
# readable result (the user terminated at the results readout, which never
# worked). Judging optimizations on tokens-per-run would have scored this
# run as a mere regression rather than a failure.
PILOT = {
    "label": "shiny-canyon",
    "billed": 1579333,
    "parts": 1392,
    "active_wall_ms": None,
    "outcome": "abandoned",
    "completions": 0,
}

REFERENCE_SQL = """
SELECT s.slug, s.time_created, s.time_updated,
       s.tokens_input, s.tokens_output, s.tokens_reasoning,
       s.tokens_cache_read, s.tokens_cache_write,
       s.tokens_input + s.tokens_output AS billed,
       (SELECT count(*) FROM part p WHERE p.session_id = s.id) AS parts,
       (SELECT sum(length(data)) FROM part p2 WHERE p2.session_id = s.id) AS storesize
FROM session s
"""


class Wall:
    """The active-wall window: ledger session-1 start -> solve gate.

    measurable is False (and ``reason`` tells why) whenever either boundary
    is missing or the window would be negative -- the card never guesses.
    """

    def __init__(self, workspace=None):
        self.start_ms = None
        self.start_source = None
        self.gate_ms = None
        self.submissions = 0
        self.active_ms = None
        self.reason = None
        if workspace is None:
            self.reason = REASON_NO_WORKSPACE
            return
        state = Path(workspace) / "results" / "state"
        self.start_ms = history_start_ms(state)
        if self.start_ms is not None:
            self.start_source = START_SOURCE_HISTORY
        else:
            self.start_ms = ledger_start_ms(Path(workspace) / "state.md")
            if self.start_ms is not None:
                self.start_source = START_SOURCE_LEDGER
        # The gate file is append-only (ticket 02): the first line is the
        # user-gated submission the wall axis ends at; every line is one
        # submission, so a re-submitted solve is visible as a count.
        gates = epoch_ms_lines(state / SOLVE_SUBMITTED_FILE)
        self.submissions = len(gates)
        self.gate_ms = gates[0] if gates else None
        if self.start_ms is None:
            self.reason = REASON_NO_START
        elif self.gate_ms is None:
            self.reason = REASON_NO_GATE
        elif self.gate_ms < self.start_ms:
            self.reason = REASON_GATE_BEFORE_START
        else:
            self.active_ms = self.gate_ms - self.start_ms

    @property
    def measurable(self):
        return self.reason is None

    @property
    def label(self):
        """The card-line value: a duration, or an explicit unmeasurable."""
        if self.measurable:
            return _duration(self.active_ms)
        return f"{UNMEASURABLE}: {self.reason}"


OUTCOME_FILE = "outcome.txt"
OUTCOME_COMPLETED = "completed"
OUTCOME_ESCALATED = "escalated"
OUTCOME_ABANDONED = "abandoned"
OUTCOMES = (OUTCOME_COMPLETED, OUTCOME_ESCALATED, OUTCOME_ABANDONED)
UNKNOWN_OUTCOME = "unrecorded"


class Outcome:
    """What the run actually delivered, and what that cost (ticket 04).

    Tokens per run is the wrong headline: the `shiny-canyon` pilot burned
    1,579,333 tokens and delivered no readable result, while the
    `silent-engine` baseline burned 398,130 and delivered one. Per-run
    cost scores the first as merely 4x worse; per *completed simulation*
    scores it as infinitely worse, which is the truth.

    `completions` is the number of simulations the run actually delivered
    (0 for an escalated or abandoned run, 1 for a normal greenfield build,
    N for a parametric sweep). Cost per completion is billed / completions,
    or explicitly infinite when nothing completed. Read from the
    workspace's `results/state/outcome.txt`, overridable from the CLI, and
    never inferred: an unrecorded outcome is reported as unrecorded.
    """

    def __init__(self, workspace=None, outcome=None, completions=None,
                 escape_hatch=None):
        self.outcome = None
        self.completions = None
        self.escape_hatch = None
        self.note = None
        self.warning = None
        if workspace is not None:
            self._read(Path(workspace) / "results" / "state" / OUTCOME_FILE)
        if outcome is not None:
            self.outcome = outcome
        if completions is not None:
            self.completions = completions
        if escape_hatch is not None:
            self.escape_hatch = escape_hatch
        if self.completions is None and self.outcome is not None:
            self.completions = 1 if self.outcome == OUTCOME_COMPLETED else 0

    def _read(self, path):
        """Parse `outcome.txt`; loud when it is not the key=value form.

        The last run wrote `completed - user verdict: ...` by hand (a UTF-8
        BOM in front of it, too) and the parser read it as nothing: the card
        said `unrecorded` and nobody noticed. A file that exists but does not
        start with `<key>=` is now reported on stderr and on the card, and
        `scripts/record_outcome.py` is the writer that cannot get it wrong.
        """
        try:
            text = path.read_text(encoding="utf-8-sig")
        except OSError:
            return
        first = next((ln for ln in text.splitlines() if ln.strip()), "")
        if not re.match(r"^\s*\w+\s*=", first):
            self.warning = f"{OUTCOME_FILE} is not key=value: {first.strip()}"
            print(f"warning: {self.warning}", file=sys.stderr)
        for line in text.splitlines():
            key, _, value = line.partition("=")
            key, value = key.strip(), value.strip()
            if key == "outcome" and value in OUTCOMES:
                self.outcome = value
            elif key == "completions":
                self.completions = _int_or_none(value)
            elif key == "escape_hatch_scripts":
                self.escape_hatch = _int_or_none(value)
            elif key == "note":
                self.note = value

    @property
    def label(self):
        if self.outcome is None:
            if self.warning:
                return f"{UNKNOWN_OUTCOME} ({self.warning})"
            return UNKNOWN_OUTCOME
        if self.note:
            return f"{self.outcome} ({self.note})"
        return self.outcome

    @property
    def escape_hatch_label(self):
        if self.escape_hatch is None:
            return UNKNOWN_OUTCOME
        return str(self.escape_hatch)

    def cost_label(self, billed):
        """`billed / completions`, or an explicit infinity / unrecorded."""
        if self.completions is None or billed is None:
            return UNKNOWN_OUTCOME
        if self.completions <= 0:
            return f"infinite ({billed:,} billed, 0 completed)"
        per = billed / self.completions
        if self.completions == 1:
            return f"{int(round(per)):,}"
        return f"{int(round(per)):,} ({billed:,} / {self.completions} completed)"


def _int_or_none(raw):
    try:
        return int(raw)
    except (TypeError, ValueError):
        return None


def history_start_ms(state_dir):
    """Session-1 start (epoch ms) from `sessions.jsonl`, or None.

    The earliest `clarify` declaration is the Clarification session's start,
    written by `scripts/session.py --phase clarify` at the instant it
    happened (ticket 01). Machine-written, so it is consulted before the
    hand-written ledger. A history with no clarify declaration gives None
    rather than the start of some other phase.
    """
    starts = [r["ts_ms"] for r in phase_session.history(state_dir)
              if r.get("phase") == phase_session.CLARIFY
              and isinstance(r.get("ts_ms"), int) and r["ts_ms"] > 0]
    return min(starts) if starts else None


def ledger_start_ms(path):
    """Session-1 start (epoch ms) from a workspace state.md, or None.

    Only the Session 1 header block is consulted -- the timestamp lives in
    the header area only, written there once by the Clarification session.
    The line is hand-written, so only the timestamp token is required: the
    real patch-array-5800 ledger reads `- Started: 2026-08-18T09:27:37Z
    (\\`session.json\\`); task: ...` and the strict end-of-line match that
    used to live here rejected it, which is why that run's active wall read
    unmeasurable.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    section = _session1_section(text)
    if section is None:
        return None
    m = re.search(r"(?m)^-\s*Started:\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\b",
                  section)
    if m is None:
        return None
    return _parse_iso_ms(m.group(1))


def epoch_ms_lines(path):
    """Every parseable epoch-seconds line of a state file, as epoch ms.

    The solve gate is append-only: one line per submission. A blank or
    garbage line is skipped, never guessed; an absent file is [].
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return []
    stamps = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            stamps.append(int(float(line) * 1000))
        except ValueError:
            continue
    return stamps


def epoch_ms_file(path):
    """The first epoch-seconds line of a state file as epoch ms; None if none."""
    stamps = epoch_ms_lines(path)
    return stamps[0] if stamps else None


def _session1_section(text):
    head = re.search(r"(?m)^## Session 1\b[^\n]*\n", text)
    if head is None:
        return None
    tail = text[head.end():]
    nxt = re.search(r"(?m)^##\s", tail)
    return tail[: nxt.start()] if nxt else tail


def _parse_iso_ms(raw):
    """Parse 2026-08-05T14:00:00Z into epoch ms; None if malformed."""
    if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", raw):
        return None
    try:
        dt = datetime.strptime(raw, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return int(dt.timestamp() * 1000)


def connect(db_path):
    """Open the opencode DB read-only; tolerant of a live-WAL-open DB."""
    uri = "file:" + str(Path(db_path).resolve()).replace("\\", "/") + "?mode=ro"
    con = sqlite3.connect(uri, uri=True, timeout=30.0)
    con.row_factory = sqlite3.Row
    return con


def load_card(con, slug=None, latest=False, worktree=None):
    """Return the card dict for one session, or None if not found.

    Sessions are constrained to the HFSS project (worktree contains
    PROJECT_MARKER), mirroring the reference SQL of analysis section 10;
    slug ties (duplicate slugs across projects) are broken by recency.

    `IN`, not `=`: opencode registers a `project` row per worktree, so a
    parallel campaign running cells from several worktrees has several rows
    matching PROJECT_MARKER. The scalar form silently bound to whichever row
    SQLite happened to return first, which made every session in every other
    worktree invisible — a run that cost real tokens would card as "no session
    ... in the HFSS_automation project", or worse, card the wrong one.

    `worktree` narrows to one exact project path when a cell needs to be sure
    which checkout it is reading (paths are stored with forward slashes).
    """
    if worktree is not None:
        where = ["s.project_id IN (SELECT id FROM project WHERE worktree = ?)"]
        args = [str(worktree).replace("\\", "/").rstrip("/")]
    else:
        where = ["s.project_id IN "
                 "(SELECT id FROM project WHERE worktree LIKE '%' || ? || '%')"]
        args = [PROJECT_MARKER]
    if slug is not None:
        where.append("s.slug = ?")
        args.append(slug)
        sql_tail = " ORDER BY s.time_created DESC LIMIT 1"
    else:
        sql_tail = " ORDER BY s.time_created DESC LIMIT 1"
    sql = REFERENCE_SQL + " WHERE " + " AND ".join(where) + sql_tail
    row = con.execute(sql, args).fetchone()
    if row is None:
        return None
    card = dict(row)
    card["duration_ms"] = card["time_updated"] - card["time_created"]
    return card


def _iso(epoch_ms):
    if epoch_ms is None:
        return "n/a"
    return datetime.fromtimestamp(epoch_ms / 1000.0, timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _duration(duration_ms):
    if duration_ms is None or duration_ms < 0:
        return "n/a"
    total_s = int(duration_ms / 1000)
    h, rem = divmod(total_s, 3600)
    m, s = divmod(rem, 60)
    return f"{h} h {m} min {s} s"


def _metric_pairs(card, wall=None, outcome=None):
    """The card's metrics as (label, value) pairs; one per card line."""
    if wall is None:
        wall = Wall(None)
    if outcome is None:
        outcome = Outcome(None)
    return [
        ("slug", card["slug"]),
        ("host", card.get("host", HOST_OPENCODE)),
        ("created", _iso(card["time_created"])),
        ("updated", _iso(card["time_updated"])),
        ("duration", _duration(card["duration_ms"])),
        ("active_wall_start", _iso(wall.start_ms)),
        ("active_wall_start_source", wall.start_source or "n/a"),
        ("solve_gate", _iso(wall.gate_ms)),
        ("solve_submissions", wall.submissions),
        ("active_wall", wall.label),
        ("tokens_input", card["tokens_input"]),
        ("tokens_output", card["tokens_output"]),
        ("tokens_reasoning", card["tokens_reasoning"]),
        ("tokens_cache_read", card["tokens_cache_read"]),
        ("tokens_cache_write", card["tokens_cache_write"]),
        ("billed", card["billed"]),
        ("parts", card["parts"]),
        ("store_bytes", card["storesize"]),
        ("outcome", outcome.label),
        ("escape_hatch_scripts", outcome.escape_hatch_label),
        ("billed_per_completed_sim", outcome.cost_label(card["billed"])),
    ]


def summary_section(card, wall=None, outcome=None):
    """The `## Run card` markdown block, one `- key: value` line per metric."""
    body = "\n".join(f"- {k}: {v}" for k, v in _metric_pairs(card, wall, outcome))
    return "## Run card\n\n" + body + "\n"


def upsert_summary(path, card, wall=None, outcome=None):
    """Insert the Run card section into summary.md; replace any old one."""
    upsert_section(path, summary_section(card, wall, outcome))


def upsert_section(path, section):
    """Write `section` (a `## Run card` block) into summary.md in place.

    The section is the block under a `## Run card` heading (a whole line)
    up to the next `## ` heading (or end of file); `### ` sub-headings inside
    the block belong to it. Idempotent: writing twice yields the same file.
    """
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^## Run card\s*$", text)
    start = match.start() if match else None
    if start is not None:
        end = len(text)
        nxt = text.find("\n## ", start + len("## Run card"))
        if nxt != -1:
            end = nxt
        head = text[:start].rstrip()
        head = head + "\n\n" if head else ""
        tail = text[end:]
    else:
        head = text.rstrip()
        head = head + "\n\n" if head else ""
        tail = ""
    path.write_text(head + section + tail, encoding="utf-8")


def render_card(card, wall=None, outcome=None):
    """Format the card as `key: value` lines, one per metric."""
    return "\n".join(f"{k}: {v}" for k, v in _metric_pairs(card, wall, outcome))


def _pct(value, base):
    if not base:
        return None
    return (value - base) / base * 100.0


def _fmt_pct(pct):
    if pct is None:
        return "n/a"
    return f"**{pct:+.0f}%**"


def _verdict(pct, frac):
    """PASS when the run is at least ``frac`` lower than the baseline."""
    if pct is None:
        return "-"
    return "PASS" if pct <= -100.0 * frac else "FAIL"


def _cmp_row(metric, base, value, threshold, frac):
    return [
        metric,
        f"{base:,}",
        f"{value:,}",
        _fmt_pct(_pct(value, base)),
        threshold,
        _verdict(_pct(value, base), frac),
    ]


def _wall_row(wall, base_dict):
    """Acceptance row for the wall axis.

    Compared only when both this run's active wall AND the baseline's
    same-way build-to-solve window are derivable; otherwise the delta cell
    says informational and the verdict cell is "-" (never gated on an
    uncomputable number).
    """
    base_ms = base_dict.get("active_wall_ms")
    metric = "wall (active: start -> solve gate)"
    baseline_cell = _duration(base_ms) if base_ms is not None else "n/a (not derivable)"
    run_cell = wall.label if wall.measurable else "n/a"
    if base_ms is not None and wall.measurable:
        pct = _pct(wall.active_ms, base_ms)
        return [metric, baseline_cell, run_cell, _fmt_pct(pct),
                ">=40% lower", _verdict(pct, 0.40)]
    if base_ms is None:
        delta_cell = "informational - baseline build-to-solve window not derivable"
    else:
        delta_cell = "informational - active wall unmeasurable"
    return [metric, baseline_cell, run_cell, delta_cell, ">=40% lower", "-"]


def _markdown_table(header, rows):
    cells = [header] + [list(r) for r in rows]
    widths = [max(len(cell[i]) for cell in cells) for i in range(len(header))]
    line = lambda r: "| " + " | ".join(r[i].ljust(widths[i])
                                       for i in range(len(r))) + " |"
    sep = "|" + "|".join("-" * (w + 2) for w in widths) + "|"
    return "\n".join([line(header), sep] + [line(r) for r in rows])


def verdict_table(card, wall, baseline=None):
    """Markdown acceptance table vs the baseline (tickets 06/18 gate).

    Billed tokens and parts are compared exactly. Active wall is compared
    only when the baseline build-to-solve window is derivable the same way
    (and this run's window is measurable); otherwise the wall row is
    marked informational.
    """
    b = BASELINE if baseline is None else baseline
    header = ["Metric", "baseline", "run", "delta", "threshold", "verdict"]
    rows = [
        _cmp_row("billed tokens", b["billed"], card["billed"], ">=50% lower", 0.50),
        _cmp_row("parts", b["parts"], card["parts"], ">=40% lower", 0.40),
        _wall_row(wall, b),
    ]
    return _markdown_table(header, rows)


# -- the run: every declared session, plus subagents, plus a total -----------

UNRESOLVED = "unresolved"


def declared_sessions(workspace):
    """The run's sessions from `sessions.jsonl`, one entry per distinct
    (host, session id), oldest first; [] when the workspace has no history.

    A session that declared twice (a solve session re-declaring after a
    desktop recycle) is one entry carrying both phases; a declaration with
    no session id stays its own entry so the report can say it is
    unresolved rather than silently dropping a session that cost tokens.
    """
    if workspace is None:
        return []
    entries = []
    by_key = {}
    for record in phase_session.history(Path(workspace) / "results" / "state"):
        host = str(record.get("host") or "")
        session_id = str(record.get("host_session_id") or "")
        key = (host, session_id) if session_id else None
        if key is not None and key in by_key:
            entry = by_key[key]
            if record["phase"] not in entry["phases"]:
                entry["phases"].append(record["phase"])
            entry["declarations"] += 1
            continue
        entry = {"host": host, "session_id": session_id,
                 "phases": [record["phase"]], "name": str(record.get("name") or ""),
                 "ts": record.get("ts"), "skill_commit": record.get("skill_commit", ""),
                 "declarations": 1}
        entries.append(entry)
        if key is not None:
            by_key[key] = entry
    return entries


def load_session_card(entry, args):
    """(card, error) for one declared session, read from its own host's store.

    A Claude Code card is annotated with `subagents`: the cards of the
    transcripts under `<session-id>/subagents/` beside it.
    """
    host, session_id = entry["host"], entry["session_id"]
    if not session_id:
        return None, "no session id was recorded at declaration"
    if host == HOST_CLAUDE_CODE:
        card = claude_transcript.select(session_id=session_id,
                                        root=getattr(args, "projects_dir", None))
        if card is None:
            return None, (f"no Claude Code transcript for session {session_id} under "
                          f"{claude_transcript.projects_dir(getattr(args, 'projects_dir', None))}")
        card["subagents"] = claude_subagents.discover(Path(card["transcript"]))
        return card, None
    if host == HOST_OPENCODE:
        db_path = getattr(args, "db", None) or os.environ.get(ENV_DB) or DEFAULT_DB
        if not Path(db_path).is_file():
            return None, f"database not found: {db_path}"
        try:
            con = connect(db_path)
        except sqlite3.Error as exc:
            return None, f"cannot open database {db_path}: {exc}"
        try:
            card = load_card(con, slug=session_id, worktree=getattr(args, "worktree", None))
        except sqlite3.Error as exc:
            return None, f"query failed: {exc}"
        finally:
            con.close()
        if card is None:
            return None, f"no opencode session whose slug is '{session_id}'"
        card["host"] = HOST_OPENCODE
        card["subagents"] = []
        return card, None
    return None, f"unknown host {host!r}"


def run_total(cards):
    """One card summing the resolved session cards and their subagents.

    `time_created` / `time_updated` span the earliest and latest session;
    `duration_ms` is that span (idle gaps between sessions included, as it
    is for one session). Per-source sums are kept beside the totals so the
    subagents' share is visible.
    """
    total = {k: 0 for k in SUM_KEYS}
    sessions_billed = subagents_billed = 0
    subagent_count = 0
    first = last = None
    for card in cards:
        for key in SUM_KEYS:
            total[key] += int(card.get(key) or 0)
        sessions_billed += int(card.get("billed") or 0)
        for sub in card.get("subagents") or []:
            subagent_count += 1
            subagents_billed += int(sub.get("billed") or 0)
            for key in SUM_KEYS:
                total[key] += int(sub.get(key) or 0)
        for bound in ("time_created", "time_updated"):
            value = card.get(bound)
            if value is None:
                continue
            first = value if first is None else min(first, value)
            last = value if last is None else max(last, value)
    total.update({
        "slug": "run total", "host": "run",
        "time_created": first, "time_updated": last,
        "duration_ms": None if first is None or last is None else last - first,
        "sessions": len(cards), "subagents": subagent_count,
        "billed_sessions": sessions_billed, "billed_subagents": subagents_billed,
    })
    return total


def _session_pairs(card):
    """A session's own metrics, subagent lines included; no run-level axes."""
    pairs = [
        ("slug", card["slug"]),
        ("host", card.get("host", HOST_OPENCODE)),
        ("created", _iso(card["time_created"])),
        ("updated", _iso(card["time_updated"])),
        ("duration", _duration(card["duration_ms"])),
    ]
    pairs += [(k, card[k]) for k in TOKEN_KEYS]
    pairs += [("billed", card["billed"]), ("parts", card["parts"]),
              ("store_bytes", card["storesize"])]
    subagents = card.get("subagents") or []
    if card.get("host") == HOST_CLAUDE_CODE:
        pairs.append(("subagents", len(subagents)))
    for sub in subagents:
        pairs.append(("subagent", f"{sub.get('agent_type') or '-'} "
                                  f"\"{sub['slug']}\" billed={sub['billed']} "
                                  f"parts={sub['parts']} "
                                  f"duration={_duration(sub['duration_ms'])}"))
    return pairs


def _run_pairs(total, run, wall, outcome, entries):
    """The `Run total` block: identity, span, wall axis, cost, outcome."""
    resolved = [e for e in entries if e.get("card") is not None]
    unresolved = [e for e in entries if e.get("card") is None]
    pairs = [
        ("run_id", (run or {}).get("run_id") or UNKNOWN_OUTCOME),
        ("skill_commit", (run or {}).get("skill_commit") or UNKNOWN_OUTCOME),
        ("sessions", f"{len(resolved)} ("
                     + ", ".join("+".join(e["phases"]) for e in resolved) + ")"
                     if resolved else "0"),
        ("unresolved", f"{len(unresolved)} ("
                       + "; ".join(f"{'+'.join(e['phases'])}: {e['error']}"
                                   for e in unresolved) + ")"
                       if unresolved else "0"),
        ("subagents", total["subagents"]),
        ("created", _iso(total["time_created"])),
        ("updated", _iso(total["time_updated"])),
        ("duration", _duration(total["duration_ms"])),
        ("active_wall_start", _iso(wall.start_ms)),
        ("active_wall_start_source", wall.start_source or "n/a"),
        ("solve_gate", _iso(wall.gate_ms)),
        ("solve_submissions", wall.submissions),
        ("active_wall", wall.label),
    ]
    pairs += [(k, total[k]) for k in TOKEN_KEYS]
    pairs += [
        ("billed", total["billed"]),
        ("billed_sessions", total["billed_sessions"]),
        ("billed_subagents", total["billed_subagents"]),
        ("parts", total["parts"]),
        ("store_bytes", total["storesize"]),
        ("outcome", outcome.label),
        ("escape_hatch_scripts", outcome.escape_hatch_label),
        ("billed_per_completed_sim", outcome.cost_label(total["billed"])),
    ]
    return pairs


def _entry_title(entry):
    slug = entry["card"]["slug"] if entry.get("card") else UNRESOLVED
    return f"{'+'.join(entry['phases'])} — {slug}"


def render_run(entries, total, run, wall, outcome, level="## "):
    """One card per declared session, then the `Run total` block.

    `level` is the heading level: `## ` on stdout, `### ` inside the
    summary's `## Run card` section so the whole run stays one section.
    """
    blocks = []
    for entry in entries:
        head = f"{level}{_entry_title(entry)}"
        if entry.get("card") is None:
            blocks.append(f"{head}\n\n- host: {entry['host'] or '-'}\n"
                          f"- session_id: {entry['session_id'] or '-'}\n"
                          f"- {UNRESOLVED}: {entry['error']}\n")
            continue
        body = "\n".join(f"- {k}: {v}" for k, v in _session_pairs(entry["card"]))
        blocks.append(f"{head}\n\n{body}\n")
    body = "\n".join(f"- {k}: {v}" for k, v in _run_pairs(total, run, wall, outcome, entries))
    blocks.append(f"{level}Run total\n\n{body}\n")
    return "\n".join(blocks)


def run_summary_section(entries, total, run, wall, outcome):
    """The `## Run card` section for a whole run (sub-blocks are `###`)."""
    return "## Run card\n\n" + render_run(entries, total, run, wall, outcome,
                                          level="### ")


def load_run(workspace, args):
    """Every declared session carded, with a total; None without a history."""
    entries = declared_sessions(workspace)
    if not entries:
        return None
    for entry in entries:
        card, error = load_session_card(entry, args)
        entry["card"], entry["error"] = card, error
    cards = [e["card"] for e in entries if e["card"] is not None]
    run = phase_session.run_info(Path(workspace) / "results" / "state") or {}
    commits = [e["skill_commit"] for e in entries if e.get("skill_commit")]
    if commits and "skill_commit" not in run:
        run = dict(run, skill_commit=" -> ".join(dict.fromkeys(commits)))
    return {"entries": entries, "cards": cards, "total": run_total(cards), "run": run}


def declared_session(workspace):
    """(host, session_id) the workspace's declared phase session recorded.

    Written by `scripts/session.py --phase ...` into results/state/session.json;
    ("", "") when absent or unrecorded, so the caller falls back cleanly.
    """
    if workspace is None:
        return "", ""
    path = Path(workspace) / "results" / "state" / SESSION_STATE_FILE
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return "", ""
    if not isinstance(data, dict):
        return "", ""
    return (str(data.get("host") or ""), str(data.get("host_session_id") or ""))


def resolve_host(args, workspace):
    """Which backend to read, and the Claude session id if one is implied."""
    host, declared_id = declared_session(workspace)
    if args.host:
        chosen = args.host
    elif args.transcript or args.session_id:
        chosen = HOST_CLAUDE_CODE
    elif args.db or os.environ.get(ENV_DB):
        chosen = HOST_OPENCODE          # an explicit database is an opencode ask
    elif host in HOSTS:
        chosen = host
    elif os.environ.get(claude_transcript.ENV_SESSION_ID):
        chosen = HOST_CLAUDE_CODE
    else:
        chosen = HOST_OPENCODE
    implied_id = ""
    if chosen == HOST_CLAUDE_CODE:
        implied_id = (args.session_id
                      or (declared_id if host == HOST_CLAUDE_CODE else "")
                      or os.environ.get(claude_transcript.ENV_SESSION_ID, ""))
    return chosen, implied_id


def load_opencode_card(args):
    """The opencode card, or (None, error-message)."""
    db_path = args.db or os.environ.get(ENV_DB) or DEFAULT_DB
    if not Path(db_path).is_file():
        return None, f"database not found: {db_path}"
    try:
        con = connect(db_path)
    except sqlite3.Error as exc:
        return None, f"cannot open database {db_path}: {exc}"
    try:
        card = load_card(con, slug=args.slug or None, latest=args.latest,
                         worktree=args.worktree)
    except sqlite3.Error as exc:
        return None, f"query failed: {exc}"
    finally:
        con.close()
    if card is None:
        subject = f"whose slug is '{args.slug}' " if args.slug else ""
        scope = (f"worktree '{args.worktree}'" if args.worktree
                 else "the HFSS_automation project")
        return None, f"no session {subject}in {scope}"
    card["host"] = HOST_OPENCODE
    return card, None


def load_claude_card(args, session_id):
    """The Claude Code card, or (None, error-message).

    Precedence: --transcript, then --slug / --latest (searched over the
    project's transcripts), then the session id implied by --session-id, the
    workspace's declared session, or the environment.
    """
    if args.transcript:
        path = Path(args.transcript)
        if not path.is_file():
            return None, f"transcript not found: {path}"
        card = claude_transcript.load_card(path)
        return (card, None) if card else (None, f"no session in {path}")
    if args.slug or args.latest:
        card = claude_transcript.select(slug=args.slug or None, latest=args.latest,
                                        root=args.projects_dir,
                                        worktree=args.worktree)
        if card is None:
            subject = f"titled '{args.slug}' " if args.slug else ""
            return None, (f"no Claude Code transcript {subject}for the "
                          f"HFSS_automation project under "
                          f"{claude_transcript.projects_dir(args.projects_dir)}")
        return card, None
    if session_id:
        card = claude_transcript.select(session_id=session_id, root=args.projects_dir)
        if card is None:
            return None, (f"no Claude Code transcript for session {session_id} "
                          f"under {claude_transcript.projects_dir(args.projects_dir)}")
        return card, None
    return None, ("no Claude Code session to card: give --session-id, "
                  "--transcript, --slug or --latest, or declare the phase with "
                  "scripts/session.py so the workspace records its session id")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Print the run card for a session (opencode or Claude Code).")
    parser.add_argument("--host", choices=HOSTS,
                        help="which harness's session store to read (default: "
                             "detected — see the module docstring)")
    parser.add_argument("--db", help="path to opencode.db (default: %r)" % DEFAULT_DB)
    parser.add_argument("--slug", help="session slug (opencode) or title (Claude Code) to card")
    parser.add_argument("--latest", action="store_true",
                        help="card the latest HFSS-project session")
    parser.add_argument("--session-id",
                        help="Claude Code session id to card (implies --host claude-code)")
    parser.add_argument("--transcript",
                        help="Claude Code transcript .jsonl to card directly")
    parser.add_argument("--projects-dir",
                        help="Claude Code projects dir (default: "
                             "$CLAUDE_PROJECTS_DIR or ~/.claude/projects)")
    parser.add_argument("--summary", help="append/replace the Run card section in this summary.md")
    parser.add_argument("--workspace",
                        help="workspace dir (state.md + results/state/); "
                             "defaults to the --summary path's parent")
    parser.add_argument("--verdict", action="store_true",
                        help="also print the acceptance-verdict table vs the baseline")
    parser.add_argument("--outcome", choices=OUTCOMES,
                        help="what the run delivered; overrides "
                             "results/state/outcome.txt")
    parser.add_argument("--completions", type=int,
                        help="simulations actually delivered (default: 1 when "
                             "completed, else 0)")
    parser.add_argument("--escape-hatch", type=int, dest="escape_hatch",
                        help="stage scripts written outside the compiler")
    parser.add_argument("--worktree",
                        help="exact project worktree path; disambiguates cells "
                             "run from separate worktrees (parallel campaigns)")
    args = parser.parse_args(argv)

    if args.latest and args.slug is not None:
        parser.error("give at most one of --slug <slug> or --latest")
    summary_path = Path(args.summary) if args.summary else None
    workspace = args.workspace or (str(summary_path.parent) if summary_path else None)

    # The run: a workspace with a declaration history and no explicit
    # session selection cards every session it declared, plus a total.
    explicit = args.slug is not None or args.latest or args.session_id or args.transcript
    run = None if explicit else load_run(workspace, args)
    if run is not None:
        wall = Wall(workspace)
        outcome = Outcome(workspace, outcome=args.outcome,
                          completions=args.completions,
                          escape_hatch=args.escape_hatch)
        print(render_run(run["entries"], run["total"], run["run"], wall, outcome),
              end="")
        if summary_path:
            try:
                upsert_section(summary_path, run_summary_section(
                    run["entries"], run["total"], run["run"], wall, outcome))
            except (OSError, ValueError, UnicodeError) as exc:
                print(f"error: cannot write '{args.summary}': {exc}", file=sys.stderr)
                return 1
            print(f"run card written to {args.summary}")
        if args.verdict:
            print()
            print(verdict_table(run["total"], wall))
        unresolved = [e for e in run["entries"] if e["card"] is None]
        if unresolved and not run["cards"]:
            print("error: none of the declared sessions could be carded: "
                  + "; ".join(e["error"] for e in unresolved), file=sys.stderr)
            return 1
        return 0

    host, session_id = resolve_host(args, workspace)
    if host == HOST_OPENCODE:
        if args.latest == (args.slug is not None):
            parser.error("give exactly one of --slug <slug> or --latest")
        card, error = load_opencode_card(args)
    else:
        card, error = load_claude_card(args, session_id)
    if card is None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    wall = Wall(workspace)
    outcome = Outcome(workspace, outcome=args.outcome,
                      completions=args.completions,
                      escape_hatch=args.escape_hatch)
    print(render_card(card, wall, outcome))
    if summary_path:
        try:
            upsert_summary(summary_path, card, wall, outcome)
        except (OSError, ValueError, UnicodeError) as exc:
            print(f"error: cannot write '{args.summary}': {exc}", file=sys.stderr)
            return 1
        print(f"run card written to {args.summary}")
    if args.verdict:
        print()
        print(verdict_table(card, wall))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
