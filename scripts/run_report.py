"""The run report: where a run's tokens, wall, retries and escalations went
(run logging, ticket 06).

    python scripts/run_report.py --workspace workspaces/<name>

writes `workspaces/<name>/run-report.md` (for people) and `run-report.json`
(for the runs index, ticket 07, and the `runcard` subagent), next to
`summary.md`, and prints one line:

    PASS: run_report workspace=<name> sessions=<resolved>/<found> steps=N findings=N high=N

It exits 1 only when the workspace directory does not exist. Everything
else degrades: a missing store, a missing trace, a missing machine-state
file each become a labelled line in the report, never a guess and never a
crash.

Three inputs, one report (`.scratch/hfss-agent-run-logging/spec.md`):

1. **Steps** — `results/state/trace/<session-id>.steps.jsonl`, written by
   `scripts/run_trace.py` from the harness stores. The report re-runs the
   trace when it is missing or stale (a session's store newer than its
   trace file, or `sessions.jsonl` newer than the newest trace file) and
   otherwise reads what is there, so a workspace whose stores are gone
   still reports from its last trace. It never opens a transcript for
   content itself.
2. **Events** — `results/state/events.jsonl` (`hfss_spec.events`), the
   stage boundaries and verdicts the repo's own scripts wrote. The report's
   own `report.written` line is left out of the analysis.
3. **Machine state** — the `results/state/*.txt` files the watchdog and the
   runners wrote, read as text (`hfss_spec.painpoints.STATE_FILES`).

Which sessions are the run's, in order of trust (each is named in the
headline with how it was found):

- `sessions.jsonl` / `session.json` with a host and session id (ticket 01):
  `declared`.
- a declaration with a name but no id (the last run's `session.json` was
  overwritten by a readout experiment that recorded neither): the Claude
  Code transcript whose own `session.py --phase ... --name <name>` command
  made it: `transcript scan`.
- a slug the ledger or the summary names (`slug: hidden-falcon`): resolved
  in the opencode database and walked up `parent_id` to the root session,
  so a subagent's slug finds its run: `ledger slug`.
- `--session HOST:ID` on the command line: `cli`.

Sections, in this order (ticket 06): headline; top pain points; stage
timeline; waiting; retries and rebuilds; context; backend; solve;
discipline; versus previous runs (`docs/runs/index.jsonl`, ticket 07, or
`no index yet`); the run card (`scripts/run_card.py`'s own section: the
run's carded sessions when the workspace has a history, else a card built
from the trace with the store-only fields marked unmeasurable).

Every number is machine-derived or reads `unmeasurable: <reason>` in
`run_card`'s wording. The classifiers and the stage table come from
`hfss_spec.painpoints`; nothing in the markdown is computed a second time
— both files render one dict. Running twice yields byte-identical files.
Stdlib only, Python 3.10 compatible.
"""

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
import claude_transcript  # noqa: E402
import run_card  # noqa: E402
import run_trace  # noqa: E402
from hfss_spec import events  # noqa: E402
from hfss_spec import painpoints  # noqa: E402
from hfss_spec import session as phase_session  # noqa: E402

REPORT_MD = "run-report.md"
REPORT_JSON = "run-report.json"
INDEX_PATH = REPO / "docs" / "runs" / "index.jsonl"
TOP_N = 10
CONTEXT_N = 10
PREVIOUS_N = 5

HOST_CLAUDE = claude_transcript.HOST
HOST_OPENCODE = run_card.HOST_OPENCODE
UNMEASURABLE = run_card.UNMEASURABLE
UNRECORDED = run_card.UNKNOWN_OUTCOME
REASON_NO_TRACE = "no step trace (results/state/trace/ holds no steps)"
REASON_NO_STORE = "no store access (trace only)"
REASON_NO_STATE = "no machine state (results/state/ holds no state file)"
REPORT_EVENT = "report.written"

# The eleven sections, in the ticket's order: (key, title).
SECTIONS = (
    ("headline", "Headline"),
    ("top", "Top pain points"),
    ("stages", "Stage timeline"),
    ("waiting", "Waiting"),
    ("retries", "Retries and rebuilds"),
    ("context", "Context"),
    ("backend", "Backend"),
    ("solve", "Solve"),
    ("discipline", "Discipline"),
    ("previous", "Versus previous runs"),
    ("run_card", "The run card"),
)
RETRY_KINDS = ("retry_same_command", "rebuild_chain", "identical_error_twice")
BACKEND_KINDS = ("backend_error", "desktop_recycle")
DISCIPLINE_KINDS = ("late_declaration", "undeclared_session", "probe_script", "foreground_poll",
                    "whole_file_read", "recursive_listing", "design_misroute", "escalation")
GAP_CLASSES = ("user_wait", "solver_wait", "unexplained")
# The machine-state files read, beyond the ones the classifiers take.
EXTRA_STATE_FILES = ("completions.txt", "solve_started.txt", "aedt_port.txt")

SLUG_RE = re.compile(r"\bslug[:\s]+`?([a-z]+-[a-z]+)\b")
RECIPE_RE = re.compile(r"(?m)^-\s*Recipe:\s*`?([A-Za-z0-9][A-Za-z0-9_-]*)")
DECLARE_CMD_RE = re.compile(r"session\.py\b[^\n]*--phase\s+(clarify|build|solve)\b")
GAP_CLASS_RE = re.compile(r"\((user_wait|solver_wait|unexplained)\)")
STAGE_LEDGER_RE = re.compile(r"stage_ledger=(\S+)")
LEDGER_ENTRY_RE = re.compile(r"([A-Za-z_]+):(\d\d):(\d\d):(\d\d)(?::(\d+)p)?")
PROFILE_STATUS_RE = re.compile(r"profile_status=(\S+)")
ROUTE_LINE_RE = re.compile(r"(?m)^(\w+):\s*route=([\w\-]+)")

_iso = run_card._iso
_duration = run_card._duration


# -- sessions: which ones are the run's --------------------------------------

def _entry(host, session_id, how, slug=None, note=None):
    return {"host": host, "session_id": session_id, "how": how, "slug": slug,
            "note": note, "resolved": False, "steps": 0, "tokens": 0, "subagents": 0,
            "first_ts": None, "last_ts": None}


def _add(found, entry):
    key = (entry["host"], entry["session_id"])
    if entry["session_id"] and any((e["host"], e["session_id"]) == key for e in found):
        return
    found.append(entry)


def ledger_slugs(workspace):
    """Every `slug: x` / `slug x` the ledger and the summary name, in order."""
    slugs = []
    for name in ("state.md", "summary.md"):
        try:
            text = (Path(workspace) / name).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in SLUG_RE.finditer(text):
            if m.group(1) not in slugs:
                slugs.append(m.group(1))
    return slugs


def recipe_of(workspace):
    """The recipe the ledger's Session 1 block names, or None."""
    try:
        text = (Path(workspace) / "state.md").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = RECIPE_RE.search(text)
    return m.group(1) if m else None


def unnamed_declarations(state_dir):
    """Declaration names recorded without a session id: the history's
    lines and the current `session.json`."""
    names = []
    for record in phase_session.history(state_dir):
        if not record.get("host_session_id") and record.get("name"):
            names.append(str(record["name"]))
    current = phase_session.Session.load(state_dir)
    if current is not None and current.name and not current.host_session_id:
        names.append(current.name)
    return list(dict.fromkeys(names))


def transcript_declaring(name, root=None):
    """(transcript path, session id) of the Claude Code session whose own
    `session.py --phase ... --name <name>` command made the declaration, or
    None. A subagent's declaration counts for its parent (the records carry
    the parent's sessionId). Quoting the name in a prompt or reading it
    back from a file is not a declaration; only a tool_use command is."""
    needle = f"--name {name}"
    for path in claude_transcript.project_transcripts(root):
        for file in [path] + claude_transcript.subagent_transcripts(path):
            try:
                with open(file, encoding="utf-8", errors="replace") as handle:
                    for line in handle:
                        if needle not in line or "session.py" not in line:
                            continue
                        try:
                            record = json.loads(line)
                        except ValueError:
                            continue
                        if record.get("type") != "assistant":
                            continue
                        content = (record.get("message") or {}).get("content")
                        for block in content if isinstance(content, list) else ():
                            if not isinstance(block, dict) or block.get("type") != "tool_use":
                                continue
                            command = (block.get("input") or {}).get("command") or ""
                            if needle in command and DECLARE_CMD_RE.search(command):
                                return path, record.get("sessionId") or path.stem
            except OSError:
                continue
    return None


def _open_db(args):
    """(DbStore, None) or (None, reason)."""
    try:
        return run_trace.open_db(getattr(args, "db", None)), None
    except (OSError, sqlite3.Error) as exc:
        return None, str(exc)


def _root_of(store, session_id):
    """Walk `parent_id` up to the root session; (root id, hops)."""
    hops = 0
    seen = {session_id}
    while True:
        row = store.session(session_id)
        parent = row.get("parent_id") if row else None
        if not parent or parent in seen:
            return session_id, hops
        seen.add(parent)
        session_id, hops = parent, hops + 1


def discover_sessions(workspace, args):
    """The run's sessions, each with how it was found (module docstring)."""
    workspace = Path(workspace)
    state_dir = workspace / "results" / "state"
    found = []
    for host, sid in run_trace.workspace_sessions(workspace):
        _add(found, _entry(host, sid, "declared"))
    projects = getattr(args, "projects_dir", None)
    for name in unnamed_declarations(state_dir):
        hit = transcript_declaring(name, projects)
        if hit is None:
            _add(found, _entry("", None, f"transcript scan: declaration --name {name}",
                               note="unresolved: no Claude Code transcript declares it"))
        else:
            _add(found, _entry(HOST_CLAUDE, hit[1], f"transcript scan: declaration --name {name}"))
    slugs = ledger_slugs(workspace)
    store = reason = None
    if slugs:
        store, reason = _open_db(args)
    for slug in slugs:
        how = f"ledger slug {slug}"
        if store is None:
            _add(found, _entry(HOST_OPENCODE, None, how, slug=slug,
                               note=f"unresolved: {reason}"))
            continue
        sid = store.find_slug(slug)
        if sid is None:
            _add(found, _entry(HOST_OPENCODE, None, how, slug=slug,
                               note="unresolved: no session with that slug in the "
                                    f"{run_card.PROJECT_MARKER} project"))
            continue
        root, hops = _root_of(store, sid)
        if hops:
            how += f" (subagent {sid}, {hops} level(s) below its root)"
        _add(found, _entry(HOST_OPENCODE, root, how, slug=slug))
    for spec in getattr(args, "session", None) or ():
        host, _, sid = spec.rpartition(":")
        host = host or run_trace.host_of(sid)
        _add(found, _entry(host, sid, "cli"))
    return found


# -- the trace: refresh when stale, else read what is there ------------------

def _source_mtime(entry, args):
    """(mtime, None) of the store a session lives in, or (None, reason)."""
    if entry["host"] == HOST_OPENCODE:
        db = Path(getattr(args, "db", None) or os.environ.get(run_card.ENV_DB) or run_card.DEFAULT_DB)
        if not db.is_file():
            return None, f"database not found: {db}"
        return db.stat().st_mtime, None
    path = claude_transcript.find_transcript(entry["session_id"], getattr(args, "projects_dir", None))
    if path is None:
        return None, (f"no Claude Code transcript for session {entry['session_id']} under "
                      f"{claude_transcript.projects_dir(getattr(args, 'projects_dir', None))}")
    latest = path.stat().st_mtime
    for agent in claude_transcript.subagent_transcripts(path):
        latest = max(latest, agent.stat().st_mtime)
    return latest, None


def _trace_family(entry, args):
    if entry["host"] == HOST_OPENCODE:
        store, reason = _open_db(args)
        if store is None:
            raise OSError(reason)
        if store.session(entry["session_id"]) is None:
            raise ValueError(f"no opencode session {entry['session_id']}")
        return run_trace.trace_opencode_family(store, entry["session_id"])
    path = claude_transcript.find_transcript(entry["session_id"], getattr(args, "projects_dir", None))
    if path is None:
        raise OSError(f"no Claude Code transcript for session {entry['session_id']}")
    return run_trace.trace_claude(path)


def refresh_trace(workspace, sessions, args):
    """Run the trace for every session whose file is missing or older than
    its store; `{status, detail}` says what happened. Never raises."""
    workspace = Path(workspace)
    trace_dir = workspace / run_trace.TRACE_DIR
    existing = {}
    if trace_dir.is_dir():
        for path in trace_dir.glob("*" + run_trace.STEPS_SUFFIX):
            existing[path.name[: -len(run_trace.STEPS_SUFFIX)]] = path.stat().st_mtime
    roots = [s for s in sessions if s["session_id"]]
    if getattr(args, "no_trace", False):
        return {"status": "kept", "detail": f"{len(existing)} file(s); --no-trace"}
    if not roots:
        if existing:
            return {"status": "kept", "detail": f"{len(existing)} file(s); no session to refresh from"}
        return {"status": "unavailable",
                "detail": "no session found: no sessions.jsonl, no session id in session.json, "
                          "no declaration in a transcript, no slug in the ledger"}
    history = workspace / "results" / "state" / phase_session.HISTORY_FILE
    history_mtime = history.stat().st_mtime if history.is_file() else 0
    newest = max(existing.values()) if existing else 0
    stale, missing_store = [], []
    for entry in roots:
        mine = existing.get(entry["session_id"])
        source, reason = _source_mtime(entry, args)
        if source is None:
            if mine is None:
                missing_store.append(f"{entry['session_id']}: {reason}")
            continue
        if mine is None or source > mine or history_mtime > newest:
            stale.append(entry)
    if not stale:
        if missing_store and not existing:
            return {"status": "unavailable", "detail": "; ".join(missing_store)}
        detail = f"{len(existing)} file(s) up to date"
        if missing_store:
            detail += "; not traceable: " + "; ".join(missing_store)
        return {"status": "fresh", "detail": detail}
    written = steps = 0
    failures = list(missing_store)
    for entry in stale:
        try:
            family = _trace_family(entry, args)
        except (ValueError, OSError, sqlite3.Error) as exc:
            failures.append(f"{entry['session_id']}: {exc}")
            continue
        for sid, family_steps in family.items():
            run_trace.write_steps(family_steps, trace_dir, sid)
            written += 1
            steps += len(family_steps)
    if not written and not existing:
        return {"status": "unavailable", "detail": "; ".join(failures) or "nothing traced"}
    detail = f"sessions={written} steps={steps}"
    if failures:
        detail += "; failed: " + "; ".join(failures)
    return {"status": "refreshed", "detail": detail}


def load_trace(workspace):
    """`{session_id: steps}` for every trace file, by file name."""
    trace_dir = Path(workspace) / run_trace.TRACE_DIR
    families = {}
    if not trace_dir.is_dir():
        return families
    for path in sorted(trace_dir.glob("*" + run_trace.STEPS_SUFFIX)):
        try:
            families[path.name[: -len(run_trace.STEPS_SUFFIX)]] = run_trace.read_steps(path)
        except (OSError, ValueError):
            continue
    return families


def load_machine_state(state_dir):
    state = {}
    for name in painpoints.STATE_FILES + EXTRA_STATE_FILES:
        path = Path(state_dir) / name
        try:
            state[name] = path.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
    return state


# -- the machine state's own numbers -----------------------------------------

def stage_ledger(line):
    """`{stage: {seconds, passes}}` from a tick line's `stage_ledger=`."""
    m = STAGE_LEDGER_RE.search(line or "")
    out = {}
    if not m or m.group(1) == "-":
        return out
    for stage, h, mi, s, passes in LEDGER_ENTRY_RE.findall(m.group(1)):
        out[stage] = {"seconds": int(h) * 3600 + int(mi) * 60 + int(s),
                      "passes": int(passes) if passes else None}
    return out


def solve_section(machine_state, evs):
    """The watchdog's runs, submissions, terminal line and bank status."""
    state = machine_state or {}
    runs = []
    for run in painpoints.watchdog_runs(state.get("solve_progress.txt")):
        status_m = PROFILE_STATUS_RE.search(run["line"])
        runs.append({
            "started": _iso(run["started_ms"]), "started_ms": run["started_ms"],
            "status": run["status"], "stage": run["stage"], "ticks": run["ticks"],
            "elapsed_s": run["elapsed_s"], "stages": stage_ledger(run["line"]),
            "profile_status": status_m.group(1) if status_m else None,
            "evidence": run["evidence"], "terminal_line": run["line"],
        })
    gates = painpoints.epoch_lines(state.get("solve_submitted_at.txt"))
    if gates:
        submissions = {"count": len(gates), "source": run_card.SOLVE_SUBMITTED_FILE,
                       "instants": [_iso(g) for g in gates]}
    elif runs:
        submissions = {"count": len(runs), "source": "watchdog runs in solve_progress.txt",
                       "instants": [r["started"] for r in runs]}
    else:
        submissions = {"count": None, "source": f"{UNMEASURABLE}: no {run_card.SOLVE_SUBMITTED_FILE} "
                                                "and no watchdog run", "instants": []}
    solved = painpoints.key_values(state.get("solved.txt"))
    bank = {"status": solved.get("status"), "sweep_points": solved.get("sweep_points"),
            "banked_at": None}
    try:
        bank["banked_at"] = _iso(int(float(solved["banked_at"])) * 1000)
    except (KeyError, ValueError):
        pass
    if "solved.txt" not in state:
        bank["note"] = "solved.txt absent: nothing banked"
    terminals = [e for e in evs if e.get("event") == "solve.terminal"]
    return {"runs": runs, "submissions": submissions, "bank": bank,
            "terminal_events": [e.get("detail") for e in terminals],
            "terminal_line": runs[-1]["terminal_line"] if runs else None}


def backend_section(findings, machine_state, evs):
    routes = []
    text = (machine_state or {}).get("readouts.txt") or ""
    for m in ROUTE_LINE_RE.finditer(text):
        routes.append({"expression": m.group(1), "route": m.group(2), "source": "readouts.txt"})
    for e in evs:
        if e.get("event") == "readout.attempt":
            routes.append({"expression": None, "route": e.get("detail"), "source": "events"})
    return {"errors": [f for f in findings if f["kind"] == "backend_error"],
            "recycles": [f for f in findings if f["kind"] == "desktop_recycle"],
            "readout_routes": routes}


def waiting_section(findings):
    gaps = []
    totals = {cls: 0 for cls in GAP_CLASSES}
    for f in findings:
        if f["kind"] != "idle_gap":
            continue
        m = GAP_CLASS_RE.search(f["evidence"])
        cls = m.group(1) if m else "unexplained"
        totals[cls] += f["cost_wall_ms"]
        gaps.append({"class": cls, "wall_ms": f["cost_wall_ms"], "phase": f["phase"],
                     "stage": f["stage"], "session": f["session"], "evidence": f["evidence"]})
    return {"gaps": gaps, "totals_ms": totals}


def context_section(attributed, n=CONTEXT_N):
    """The heaviest tool outputs and longest reasoning blocks, from the steps."""
    by_session = painpoints._by_session(attributed)
    firsts = {}
    for s in attributed:
        if s.get("tokens_input") is not None:
            firsts.setdefault((s["session_id"], s.get("request_id")), s)
    outputs = []
    for s in attributed:
        if s.get("kind") != "tool_result" or not s.get("out_bytes"):
            continue
        later = sum(1 for t in by_session[s["session_id"]] if (t.get("seq") or 0) > (s.get("seq") or 0))
        outputs.append({"bytes": s["out_bytes"], "tool": s.get("tool"), "command": painpoints._cmd(s, 100),
                        "later_steps": later, "phase": s.get("phase"), "stage": s.get("stage"),
                        "session": s["session_id"], "seq": s["seq"], "is_error": bool(s.get("is_error"))})
    outputs.sort(key=lambda r: (-r["bytes"], r["session"], r["seq"]))
    reasoning = []
    for s in attributed:
        if s.get("kind") != "reasoning":
            continue
        size = int(s.get("out_bytes") or 0)
        estimated = False
        if size == 0:
            first = firsts.get((s["session_id"], s.get("request_id")))
            size = int((first or {}).get("tokens_reasoning") or 0) * painpoints.BYTES_PER_TOKEN
            estimated = True
        following = next((t for t in by_session[s["session_id"]]
                          if (t.get("seq") or 0) > (s.get("seq") or 0) and t.get("kind") == "tool_use"), None)
        reasoning.append({"bytes": size, "estimated": estimated, "phase": s.get("phase"),
                          "stage": s.get("stage"), "session": s["session_id"], "seq": s["seq"],
                          "before": (f"{following.get('tool')} {painpoints._cmd(following, 60)}"
                                     if following else "no tool call")})
    reasoning.sort(key=lambda r: (-r["bytes"], r["session"], r["seq"]))
    return {"outputs": outputs[:n], "reasoning": reasoning[:n]}


# -- the headline and the run card -------------------------------------------

def _phase_label(phase, index):
    return phase if index is None or index < 0 else f"{phase} #{index}"


def headline(workspace, sessions, families, attributed, rows, findings, trace, machine_state,
             history, wall, outcome, evs):
    steps = [s for steps in families.values() for s in steps]
    usage = run_trace.totals(steps) if steps else None
    billed = usage["billed"] if usage else None
    stamped = [s for s in steps if s.get("ts") is not None]
    raw_ms = None
    if stamped:
        raw_ms = max(s["ts"] + int(s.get("latency_ms") or 0) for s in stamped) - min(s["ts"] for s in stamped)
    tokens_by_phase, steps_by_phase = {}, {}
    for r in rows:
        label = _phase_label(r["phase"], r["phase_index"])
        tokens_by_phase[label] = tokens_by_phase.get(label, 0) + r["tokens"]
        steps_by_phase[label] = steps_by_phase.get(label, 0) + r["steps"]
    tokens_by_session, tokens_by_subagent = {}, {}
    for sid, fam in families.items():
        parent = next((s.get("parent_session_id") for s in fam if s.get("parent_session_id")), None)
        total = run_trace.totals(fam)["billed"]
        if parent:
            tokens_by_subagent[sid] = {"parent": parent, "billed": total, "steps": len(fam)}
        else:
            tokens_by_session[sid] = {"billed": total, "steps": len(fam)}
    sources = {r["stage_source"] for r in rows}
    if not rows:
        attribution = f"{UNMEASURABLE}: {REASON_NO_TRACE}"
    elif sources == {"events"}:
        attribution = "stages from events.jsonl"
    elif "events" in sources:
        attribution = "stages from events.jsonl where an event covered the call, else read off the command"
    else:
        attribution = ("between-stages / stage read off the command: no stage events recorded "
                       "(the run predates the event log, ticket 03)")
    state_files = sorted(machine_state)
    # What the report reads, not what this run of it did: the refresh
    # outcome varies between two runs and goes to stdout and the event.
    if families:
        trace_line = (f"{len(families)} session file(s), {len(steps)} steps"
                      + (f"; not traceable: {trace['detail'].split('not traceable: ', 1)[1]}"
                         if "not traceable: " in trace["detail"] else ""))
    else:
        trace_line = f"unavailable ({trace['detail']})"
    run = phase_session.run_info(workspace / "results" / "state") or {}
    run_id = run.get("run_id")
    derived = False
    if not run_id and stamped:
        run_id = f"{workspace.name}-{_iso(min(s['ts'] for s in stamped))[:10]}"
        derived = True
    commits = [r.get("skill_commit") for r in history if r.get("skill_commit")]
    return {
        "run_id": run_id or f"{UNRECORDED} (no run.json)",
        "run_id_source": "run.json" if run.get("run_id") else ("derived from the trace's first step; "
                                                                "run.json absent" if derived else "absent"),
        "workspace": workspace.name,
        "recipe": recipe_of(workspace) or UNRECORDED,
        "skill_commit": " -> ".join(dict.fromkeys(commits)) if commits else UNRECORDED,
        "hosts": sorted({s["host"] for s in sessions if s["host"]}) or [],
        "outcome": outcome.label,
        "completions": outcome.completions if outcome.completions is not None else UNRECORDED,
        "billed": billed if billed is not None else f"{UNMEASURABLE}: {REASON_NO_TRACE}",
        "billed_per_completion": outcome.cost_label(billed) if billed is not None
        else f"{UNMEASURABLE}: {REASON_NO_TRACE}",
        "raw_wall": _duration(raw_ms) if raw_ms is not None else f"{UNMEASURABLE}: {REASON_NO_TRACE}",
        "raw_wall_ms": raw_ms,
        "active_wall": wall.label,
        "active_wall_ms": wall.active_ms,
        "active_wall_start": _iso(wall.start_ms),
        "active_wall_start_source": wall.start_source or "n/a",
        "solve_gate": _iso(wall.gate_ms),
        "solve_submissions": wall.submissions,
        "tokens": {k: usage[k] for k in run_trace.TOKEN_KEYS} if usage else None,
        "requests": usage["requests"] if usage else None,
        "steps": len(steps),
        "tokens_by_phase": tokens_by_phase,
        "steps_by_phase": steps_by_phase,
        "tokens_by_session": tokens_by_session,
        "tokens_by_subagent": tokens_by_subagent,
        "attribution": attribution,
        "trace": trace_line,
        "sessions": sessions,
        "machine_state": state_files if state_files else f"absent ({REASON_NO_STATE})",
        "events": len(evs),
        "findings": len(findings),
        "findings_high": sum(1 for f in findings if f["severity"] == "high"),
        "top_finding_kind": findings[0]["kind"] if findings else None,
    }


def trace_card(workspace, families, hosts):
    """A run card in `run_card`'s shape from the trace alone; the fields
    only a store holds are marked unmeasurable, never estimated."""
    steps = [s for steps in families.values() for s in steps]
    usage = run_trace.totals(steps)
    stamped = [s["ts"] for s in steps if s.get("ts") is not None]
    ends = [s["ts"] + int(s.get("latency_ms") or 0) for s in steps if s.get("ts") is not None]
    first = min(stamped) if stamped else None
    last = max(ends) if ends else None
    card = {k: usage[k] for k in run_trace.TOKEN_KEYS}
    card.update({
        "slug": f"{Path(workspace).name} (trace: {len(families)} session(s))",
        "host": "+".join(hosts) if hosts else "trace",
        "time_created": first, "time_updated": last,
        "duration_ms": None if first is None or last is None else last - first,
        "billed": usage["billed"],
        "parts": f"{UNMEASURABLE}: {REASON_NO_STORE}; steps={usage['steps']}",
        "storesize": f"{UNMEASURABLE}: {REASON_NO_STORE}",
    })
    return card


def run_card_section(workspace, families, sessions, args, wall, outcome):
    """`run_card`'s own `## Run card` section: the carded run when the
    workspace has a declaration history, else the trace-derived card."""
    run = None
    try:
        run = run_card.load_run(str(workspace), args)
    except (OSError, ValueError, sqlite3.Error):
        run = None
    if run is not None and run["cards"]:
        return run_card.run_summary_section(run["entries"], run["total"], run["run"], wall, outcome)
    hosts = sorted({s["host"] for s in sessions if s["host"]})
    if not families:
        card = trace_card(workspace, {}, hosts)
        card["slug"] = f"{Path(workspace).name} ({UNMEASURABLE}: {REASON_NO_TRACE})"
    else:
        card = trace_card(workspace, families, hosts)
    return run_card.summary_section(card, wall, outcome)


# -- previous runs (ticket 07's index) ---------------------------------------

def read_index(path):
    rows = []
    try:
        lines = Path(path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def previous_runs(index_path, head, n=PREVIOUS_N):
    rows = read_index(index_path)
    if rows is None:
        return {"note": f"no index yet ({_relative(index_path)} not found; ticket 07)", "rows": []}
    recipe = head.get("recipe")
    mine = [r for r in rows if r.get("run_id") != head.get("run_id")
            and (recipe in (None, UNRECORDED) or r.get("recipe") == recipe)]
    if not mine:
        return {"note": f"no previous run of recipe {recipe} in the index", "rows": []}
    return {"note": None, "rows": mine[-n:]}


def index_row(head, report_path):
    """This run's line for `docs/runs/index.jsonl` (ticket 07's columns)."""
    return {
        "run_id": head["run_id"], "workspace": head["workspace"], "recipe": head["recipe"],
        "skill_commit": head["skill_commit"], "host": "+".join(head["hosts"]) or None,
        "outcome": head["outcome"], "completions": head["completions"],
        "billed": head["billed"] if isinstance(head["billed"], int) else None,
        "billed_per_completion": head["billed_per_completion"],
        "parts": None, "raw_wall_ms": head["raw_wall_ms"], "active_wall_ms": head["active_wall_ms"],
        "tokens_by_phase": head["tokens_by_phase"], "findings_high": head["findings_high"],
        "top_finding_kind": head["top_finding_kind"], "report_path": report_path,
    }


# -- rendering ---------------------------------------------------------------

def _cell(value):
    text = "" if value is None else str(value)
    return text.replace("\r", " ").replace("\n", " ").replace("|", "\\|")


def _table(header, rows):
    if not rows:
        return "_none_\n"
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(_cell(c) for c in row) + " |")
    return "\n".join(lines) + "\n"


def _finding_row(i, f):
    return [i, f"{f['cost_tokens']:,}", _duration(f["cost_wall_ms"]), f["kind"], f["severity"],
            f"{_phase_label(f['phase'], None)}/{f['stage']}", f["evidence"], f["fix_hint"]]


FINDING_HEADER = ["#", "tokens", "wall", "kind", "sev", "phase/stage", "evidence", "fix"]


def _findings_table(findings, limit=None):
    """The findings as a table; past `limit` rows, one line counts the rest
    by kind so the section stays short and nothing is hidden silently."""
    shown = findings if limit is None else findings[:limit]
    out = _table(FINDING_HEADER, [_finding_row(1 + i, f) for i, f in enumerate(shown)])
    rest = findings[len(shown):]
    if rest:
        kinds = defaultdict(int)
        for f in rest:
            kinds[f["kind"]] += 1
        out += (f"\n{len(rest)} more not shown (all in run-report.json): "
                + ", ".join(f"{k} x{v}" for k, v in sorted(kinds.items())) + "\n")
    return out


def _relative(path):
    """A path relative to the checkout, forward slashes; absolute only when
    it lies outside it, so a committed report reads the same everywhere."""
    path = Path(path)
    try:
        return path.resolve().relative_to(REPO.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def render_headline(h):
    lines = [f"- run_id: {h['run_id']} ({h['run_id_source']})",
             f"- workspace: {h['workspace']}",
             f"- recipe: {h['recipe']}",
             f"- skill_commit: {h['skill_commit']}",
             f"- outcome: {h['outcome']}",
             f"- completions: {h['completions']}",
             f"- billed: {h['billed']:,}" if isinstance(h["billed"], int) else f"- billed: {h['billed']}",
             f"- billed_per_completed_sim: {h['billed_per_completion']}",
             f"- raw_wall: {h['raw_wall']}",
             f"- active_wall: {h['active_wall']}",
             f"- active_wall_start: {h['active_wall_start']} ({h['active_wall_start_source']})",
             f"- solve_gate: {h['solve_gate']} (submissions recorded: {h['solve_submissions']})",
             f"- steps: {h['steps']}" + (f" in {h['requests']} requests" if h["requests"] else ""),
             f"- stage attribution: {h['attribution']}",
             f"- trace: {h['trace']}",
             f"- machine state: {', '.join(h['machine_state']) if isinstance(h['machine_state'], list) else h['machine_state']}",
             f"- events: {h['events']}",
             f"- findings: {h['findings']} ({h['findings_high']} high)"]
    lines.append("- tokens by phase session: " + (", ".join(
        f"{k} {v:,}" for k, v in h["tokens_by_phase"].items()) if h["tokens_by_phase"]
        else f"{UNMEASURABLE}: {REASON_NO_TRACE}"))
    lines.append("- steps by phase: " + (", ".join(
        f"{k} {v}" for k, v in h["steps_by_phase"].items()) if h["steps_by_phase"]
        else f"{UNMEASURABLE}: {REASON_NO_TRACE}"))
    lines.append("- tokens by session: " + (", ".join(
        f"{k} {v['billed']:,} ({v['steps']} steps)" for k, v in h["tokens_by_session"].items())
        if h["tokens_by_session"] else f"{UNMEASURABLE}: {REASON_NO_TRACE}"))
    lines.append("- tokens by subagent: " + (", ".join(
        f"{k} {v['billed']:,} ({v['steps']} steps, under {v['parent']})"
        for k, v in h["tokens_by_subagent"].items()) if h["tokens_by_subagent"] else "none"))
    lines.append("- sessions:")
    if not h["sessions"]:
        lines.append("  - none found")
    for s in h["sessions"]:
        span = ""
        if s.get("first_ts") is not None and s.get("last_ts") is not None:
            span = f", {_iso(s['first_ts'])} -> {_iso(s['last_ts'])} ({_duration(s['last_ts'] - s['first_ts'])})"
        status = (f"resolved: {s['steps']} steps, {s['tokens']:,} tokens, {s['subagents']} subagent(s){span}"
                  if s["resolved"] else (s["note"] or "unresolved: no trace file"))
        lines.append(f"  - {s['host'] or '?'} {s['session_id'] or '-'}"
                     + (f" ({s['slug']})" if s.get("slug") else "") + f" — {s['how']} — {status}")
    return "\n".join(lines) + "\n"


def render_stages(rows):
    table = []
    for r in rows:
        stage = r["stage"] + ("" if r["stage_source"] == "events" else " *")
        table.append([_phase_label(r["phase"], r["phase_index"]), stage, _iso(r["start"]),
                      _duration(r["wall_ms"]), r["steps"], f"{r['tokens']:,}", r["script_runs"],
                      r["fails"], r["retries"]])
    out = _table(["phase", "stage", "start", "wall", "steps", "tokens", "script runs", "fails", "retries"], table)
    if any(r["stage_source"] != "events" for r in rows):
        out += "\n`*` stage read off the command (no event covered the call); `between-stages` is its own row.\n"
    return out


def render_waiting(w, limit):
    lines = [f"- {cls}: {_duration(w['totals_ms'][cls])}" for cls in GAP_CLASSES]
    lines.append(f"- total: {_duration(sum(w['totals_ms'].values()))} in {len(w['gaps'])} gap(s)")
    shown = w["gaps"][:limit]
    table = [[g["class"], _duration(g["wall_ms"]), g["phase"], g["stage"], g["evidence"]] for g in shown]
    out = "\n".join(lines) + "\n\n" + _table(["class", "wall", "phase", "stage", "evidence"], table)
    if len(w["gaps"]) > len(shown):
        out += f"\n{len(w['gaps']) - len(shown)} more gap(s) not shown (all in run-report.json)\n"
    return out


def render_context(c):
    out = "Heaviest tool outputs:\n\n" + _table(
        ["bytes", "tool", "command", "in context for", "phase/stage"],
        [[f"{r['bytes']:,}", r["tool"], r["command"], f"{r['later_steps']} later steps",
          f"{r['phase']}/{r['stage']}"] for r in c["outputs"]])
    out += "\nLongest reasoning blocks:\n\n" + _table(
        ["bytes", "before", "phase/stage"],
        [[f"{r['bytes']:,}" + (" (est.)" if r["estimated"] else ""), r["before"],
          f"{r['phase']}/{r['stage']}"] for r in c["reasoning"]])
    return out


def render_backend(b, limit):
    out = "Errors by AEDT command:\n\n" + _findings_table(b["errors"], limit)
    out += "\nDesktop recycles:\n\n" + _findings_table(b["recycles"], limit)
    out += "\nReadout routes:\n\n" + _table(
        ["expression", "route", "source"],
        [[r["expression"] or "-", r["route"], r["source"]] for r in b["readout_routes"]])
    return out


def render_solve(s):
    if not s["runs"] and s["submissions"]["count"] is None:
        return f"- {s['submissions']['source']}\n"
    lines = [f"- submissions: {s['submissions']['count']} ({s['submissions']['source']}): "
             + ", ".join(s["submissions"]["instants"])]
    table = []
    for r in s["runs"]:
        stages = ", ".join(f"{k} {_duration(v['seconds'] * 1000)}" + (f" ({v['passes']} passes)" if v["passes"] else "")
                           for k, v in r["stages"].items()) or "-"
        table.append([r["started"], r["status"], r["stage"], _duration(r["elapsed_s"] * 1000), r["ticks"],
                      stages, r["profile_status"] or "-"])
    out = "\n".join(lines) + "\n\n" + _table(
        ["watchdog started", "status", "stage", "elapsed", "ticks", "stage durations", "profile"], table)
    out += f"\n- terminal line: `{s['terminal_line']}`\n" if s["terminal_line"] else "\n- terminal line: none\n"
    bank = s["bank"]
    out += (f"- bank: status={bank['status'] or '-'} sweep_points={bank['sweep_points'] or '-'} "
            f"banked_at={bank['banked_at'] or '-'}" + (f" ({bank['note']})" if bank.get("note") else "") + "\n")
    return out


def render_previous(p):
    if p["note"]:
        return f"{p['note']}\n"
    header = ["run_id", "outcome", "completions", "billed", "billed_per_completion", "raw_wall", "active_wall",
              "findings_high", "top_finding_kind"]
    rows = [[r.get("run_id"), r.get("outcome"), r.get("completions"), r.get("billed"),
             r.get("billed_per_completion"), _duration(r.get("raw_wall_ms")), _duration(r.get("active_wall_ms")),
             r.get("findings_high"), r.get("top_finding_kind")] for r in p["rows"]]
    return _table(header, rows)


def render(report):
    h = report["headline"]
    limit = report["top_n"]
    out = [f"# Run report — {h['workspace']}\n"]
    renderers = {
        "headline": lambda: render_headline(h),
        "top": lambda: _findings_table(report["top"]),
        "stages": lambda: render_stages(report["stages"]),
        "waiting": lambda: render_waiting(report["waiting"], limit),
        "retries": lambda: _findings_table(report["retries"], limit),
        "context": lambda: render_context(report["context"]),
        "backend": lambda: render_backend(report["backend"], limit),
        "solve": lambda: render_solve(report["solve"]),
        "discipline": lambda: _findings_table(report["discipline"], limit),
        "previous": lambda: render_previous(report["previous"]),
        "run_card": lambda: report["run_card"].split("\n", 1)[1].lstrip("\n"),
    }
    for number, (key, title) in enumerate(SECTIONS, start=1):
        out.append(f"## {number}. {title}\n")
        out.append(renderers[key]())
    return "\n".join(out)


# -- the report --------------------------------------------------------------

def build(workspace, args):
    """Everything the two files hold, as one dict."""
    workspace = Path(workspace)
    state_dir = workspace / "results" / "state"
    sessions = discover_sessions(workspace, args)
    trace = refresh_trace(workspace, sessions, args)
    families = load_trace(workspace)
    for entry in sessions:
        fam = families.get(entry["session_id"]) if entry["session_id"] else None
        if fam is not None:
            children = [sid for sid, steps in families.items()
                        if any(s.get("parent_session_id") == entry["session_id"] for s in steps)]
            mine = fam + [s for c in children for s in families[c]]
            stamped = [s for s in mine if s.get("ts") is not None]
            entry["resolved"] = True
            entry["steps"] = len(mine)
            entry["tokens"] = run_trace.totals(mine)["billed"]
            entry["subagents"] = len(children)
            entry["first_ts"] = min(s["ts"] for s in stamped) if stamped else None
            entry["last_ts"] = (max(s["ts"] + int(s.get("latency_ms") or 0) for s in stamped)
                                if stamped else None)
    steps = [s for sid in sorted(families) for s in families[sid]]
    evs = [e for e in events.read(state_dir) if e.get("event") != REPORT_EVENT]
    history = phase_session.history(state_dir)
    machine_state = load_machine_state(state_dir)
    findings = painpoints.analyze(steps, evs, history, machine_state)
    rows = painpoints.stage_table(steps, evs, history)
    attributed = painpoints.attribute(steps, evs, history)
    wall = run_card.Wall(str(workspace))
    outcome = run_card.Outcome(str(workspace))
    head = headline(workspace, sessions, families, attributed, rows, findings, trace, machine_state,
                    history, wall, outcome, evs)
    report_path = _relative(workspace / REPORT_MD)
    report = {
        "_trace_refresh": trace,          # this run's action; not rendered
        "headline": head,
        "top_n": args.top,
        "top": findings[: args.top],
        "findings": findings,
        "stages": rows,
        "waiting": waiting_section(findings),
        "retries": [f for f in findings if f["kind"] in RETRY_KINDS],
        "context": context_section(attributed),
        "backend": backend_section(findings, machine_state, evs),
        "solve": solve_section(machine_state, evs),
        "discipline": [f for f in findings if f["kind"] in DISCIPLINE_KINDS],
        "previous": previous_runs(getattr(args, "index", None) or INDEX_PATH, head),
        "run_card": run_card_section(workspace, families, sessions, args, wall, outcome),
        "sections": [key for key, _ in SECTIONS],
    }
    report["index_row"] = index_row(head, report_path)
    return report


def write_report(workspace, report):
    workspace = Path(workspace)
    md = workspace / REPORT_MD
    js = workspace / REPORT_JSON
    data = {k: v for k, v in report.items() if not k.startswith("_")}
    with open(md, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(render(report))
    with open(js, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    return md, js


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspace", required=True, help="workspace dir (state.md + results/state/)")
    parser.add_argument("--db", help="opencode.db path (default: $OPENCODE_DB or ~/.local/share/opencode/opencode.db)")
    parser.add_argument("--projects-dir", help="Claude Code projects dir (default: ~/.claude/projects)")
    parser.add_argument("--session", action="append", metavar="HOST:ID",
                        help="a session to include besides the discovered ones (repeatable)")
    parser.add_argument("--top", type=int, default=TOP_N, help="findings in the top section (default %d)" % TOP_N)
    parser.add_argument("--no-trace", action="store_true", dest="no_trace",
                        help="never touch a store; report from the trace on disk")
    parser.add_argument("--index", help="runs index to compare against (default docs/runs/index.jsonl)")
    parser.add_argument("--worktree", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    workspace = Path(args.workspace)
    if not workspace.is_dir():
        print(f"error: workspace not found: {workspace}", file=sys.stderr)
        return 1
    report = build(workspace, args)
    md, js = write_report(workspace, report)
    head = report["headline"]
    resolved = sum(1 for s in head["sessions"] if s["resolved"])
    refresh = report["_trace_refresh"]
    line = (f"PASS: run_report workspace={workspace.name} sessions={resolved}/{len(head['sessions'])} "
            f"steps={head['steps']} findings={head['findings']} high={head['findings_high']} "
            f"trace={refresh['status']}")
    events.emit(workspace / "results" / "state", REPORT_EVENT, stage="summary", verdict=line,
                detail=f"md={md.name} json={js.name} trace={refresh['status']}: {refresh['detail']}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
