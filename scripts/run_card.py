"""Print the opencode run card for a session, from the session database.

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

--workspace DIR points at a workspace directory (state.md + results/state/);
when --summary is given and --workspace is not, the summary's parent
directory is used. The database path resolves in order: --db flag,
OPENCODE_DB env var, default ~/.local/share/opencode/opencode.db.
"""

import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = Path.home() / ".local" / "share" / "opencode" / "opencode.db"
ENV_DB = "OPENCODE_DB"
PROJECT_MARKER = "HFSS_automation"

SOLVE_SUBMITTED_FILE = "solve_submitted_at.txt"
UNMEASURABLE = "unmeasurable"
REASON_NO_WORKSPACE = "no workspace state (no --workspace/--summary)"
REASON_NO_START = "no session-1 start in state.md"
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
        self.gate_ms = None
        self.active_ms = None
        self.reason = None
        if workspace is None:
            self.reason = REASON_NO_WORKSPACE
            return
        self.start_ms = ledger_start_ms(Path(workspace) / "state.md")
        self.gate_ms = epoch_ms_file(
            Path(workspace) / "results" / "state" / SOLVE_SUBMITTED_FILE
        )
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
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            return
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


def ledger_start_ms(path):
    """Session-1 start (epoch ms) from a workspace state.md, or None.

    Only the Session 1 header block is consulted -- the timestamp lives in
    the header area only, written there once by the Clarification session.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    section = _session1_section(text)
    if section is None:
        return None
    m = re.search(r"(?m)^-\s*Started:\s*(\S+)\s*$", section)
    if m is None:
        return None
    return _parse_iso_ms(m.group(1))


def epoch_ms_file(path):
    """Epoch-seconds float state file as epoch ms; None if absent/garbage."""
    try:
        text = path.read_text(encoding="utf-8").strip()
    except OSError:
        return None
    try:
        return int(float(text) * 1000)
    except ValueError:
        return None


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


def load_card(con, slug=None, latest=False):
    """Return the card dict for one session, or None if not found.

    Sessions are constrained to the HFSS project (worktree contains
    PROJECT_MARKER), mirroring the reference SQL of analysis section 10;
    slug ties (duplicate slugs across projects) are broken by recency.
    """
    where = ["s.project_id = (SELECT id FROM project WHERE worktree LIKE '%' || ? || '%')"]
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
        ("created", _iso(card["time_created"])),
        ("updated", _iso(card["time_updated"])),
        ("duration", _duration(card["duration_ms"])),
        ("active_wall_start", _iso(wall.start_ms)),
        ("solve_gate", _iso(wall.gate_ms)),
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
    """Insert the Run card section into summary.md; replace any old one.

    The section is the block under a `## Run card` heading (a whole line)
    up to the next `## ` heading (or end of file). Idempotent: writing
    twice yields the same file.
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
    path.write_text(head + summary_section(card, wall, outcome) + tail,
                    encoding="utf-8")


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


def main(argv=None):
    parser = argparse.ArgumentParser(description="Print the opencode run card.")
    parser.add_argument("--db", help="path to opencode.db (default: %r)" % DEFAULT_DB)
    parser.add_argument("--slug", help="session slug to card")
    parser.add_argument("--latest", action="store_true",
                        help="card the latest HFSS-project session")
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
    args = parser.parse_args(argv)

    if args.latest == (args.slug is not None):
        parser.error("give exactly one of --slug <slug> or --latest")
    db_path = args.db or os.environ.get(ENV_DB) or DEFAULT_DB
    if not Path(db_path).is_file():
        print(f"error: database not found: {db_path}", file=sys.stderr)
        return 1
    try:
        con = connect(db_path)
    except sqlite3.Error as exc:
        print(f"error: cannot open database {db_path}: {exc}", file=sys.stderr)
        return 1
    try:
        card = load_card(con, slug=args.slug or None, latest=args.latest)
    except sqlite3.Error as exc:
        print(f"error: query failed: {exc}", file=sys.stderr)
        return 1
    finally:
        con.close()
    if card is None:
        subject = f"whose slug is '{args.slug}' " if args.slug else ""
        print(f"error: no session {subject}in the HFSS_automation project",
              file=sys.stderr)
        return 1
    summary_path = Path(args.summary) if args.summary else None
    workspace = args.workspace or (str(summary_path.parent) if summary_path else None)
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
