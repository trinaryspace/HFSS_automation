"""Pain-point classifiers over one run (run logging, ticket 05).

Pure functions. They take the three inputs the spec names and return
findings; nothing here opens a file, a database or a desktop:

- `steps`: every step of every session of the run, in the `steps.jsonl`
  shape `scripts/run_trace.py` writes (one flat list; a session is told
  apart by `session_id`, a subagent by `parent_session_id`).
- `events`: `results/state/events.jsonl` as `hfss_spec.events.read()`
  returns it.
- `history`: `results/state/sessions.jsonl` as `hfss_spec.session.history()`
  returns it.
- `machine_state`: `{file name: text}` for the files of `results/state/`
  (`STATE_FILES` lists the ones read here; a missing file is simply absent).

A finding is one dict:

    {kind, severity, phase, stage, cost_tokens, cost_wall_ms,
     steps: [seq, ...], evidence: one line, fix_hint,
     session: the session the steps belong to (None for a machine-state
     finding), source: "trace" | "events" | "state"}

Attribution first (`attribute`): every step gets a `phase` — the latest
declaration at or before it that names its session (or its parent's), read
from the history, from `phase.declared` events and, for a run that predates
both (patch-array-5800 did), from the `scripts/session.py --phase X`
commands in the trace itself — and a `stage`: the stage window an event
opened that contains the step's tool call (`compile.start` .. `compile.end`,
`solve.submitted` .. `solve.terminal`, `stage.start` .. `stage.end`, the point
events for snapshot / gate / sync-verify / readout / summary), else
`between-stages`. A run with no stage events at all falls back to a stage
read off the command (`stage_hint`); the attributed step says which
(`stage_source`), so the report never presents a guess as a boundary.

Cost: a finding's `cost_tokens` is the billed tokens (input + output) of the
API requests its steps belong to. `analyze` counts a request at most once
per kind, so the findings of one kind never sum to more than the run.
`cost_wall_ms` is what the classifier can measure: a call's duration, a
gap, or the span of a chain. Severity by cost (`severity_of`): `high` above
`HIGH_TOKEN_SHARE` of the run or `HIGH_WALL_MS`; `low` for a discipline
finding that cost nothing this time; `medium` otherwise.

What the trace does not carry, and how that is handled: `run_trace` keeps
the first 200 characters of a command and the byte size of a tool's
output, never the output text. `backend_error` and `design_misroute` are
defined on output text (`Active Design set to X`, `GrpcApiError ...
command: X`); `step_text` reads it from an `output_head` key when a future
trace carries one, and until then the two classifiers work from what is
recorded: the machine-state files that quote the errors (`readouts.txt`,
`z_act.txt`) and, for the misroute, the command-level signature that both
patch-array-5800 misroutes left — a spec compiled, `ws_common.py` (the file
that holds the `DESIGN` constant) edited, the same spec compiled again, all
inside one build phase. The evidence line says which source it came from.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone

# -- thresholds, one named constant per rule --------------------------------

HEAVY_OUTPUT_BYTES = 8 * 1024        # a tool result above this stays in context
LONG_REASONING_BYTES = 4 * 1024      # a reasoning block above this
BYTES_PER_TOKEN = 4                  # Claude Code stores thinking without text;
                                     # tokens_reasoning * this estimates bytes
RETRY_MIN = 2                        # same normalised command this often in a stage
REBUILD_MIN = 2                      # compiles in one build phase
FOREGROUND_POLL_MIN = 3              # state-file reads ...
FOREGROUND_POLL_WINDOW_MS = 60_000   # ... within this window
IDLE_GAP_MS = 5 * 60_000             # a gap between steps at least this long
HIGH_TOKEN_SHARE = 0.05              # severity high above this share of the run
HIGH_WALL_MS = 15 * 60_000           # or above this wall
LOW_TOKEN_SHARE = 0.005              # a discipline finding below both of these
LOW_WALL_MS = 60_000                 # "cost nothing this time" -> low
ROUTING_FILE = "ws_common.py"        # holds the DESIGN constant that routes a compile
COMMAND_CHARS = 200                  # run_trace keeps this much of a command; a
                                     # command this long may be cut mid-flag
UNKNOWN_SPEC = "?"                   # a compile whose --spec the cut command lost

PHASES = ("clarify", "build", "solve")
UNDECLARED = "undeclared"
BETWEEN = "between-stages"
STAGES = ("compile", "snapshot", "gate", "sync-verify", "solve", "readout", "summary")

KINDS = ("heavy_output", "long_reasoning", "whole_file_read", "recursive_listing",
         "retry_same_command", "identical_error_twice", "rebuild_chain",
         "foreground_poll", "probe_script", "idle_gap", "escalation",
         "late_declaration", "undeclared_session", "backend_error",
         "desktop_recycle", "design_misroute", "solve_anomaly", "unbanked")
DISCIPLINE_KINDS = frozenset(("whole_file_read", "recursive_listing", "foreground_poll",
                              "probe_script", "late_declaration", "undeclared_session",
                              "design_misroute"))
WALL_ONLY_KINDS = frozenset(("idle_gap",))     # waiting spends no tokens
SEVERITIES = ("high", "medium", "low")

STATE_FILES = ("solve_progress.txt", "readouts.txt", "aedt_port.txt",
               "aedt_process_id.txt", "session.json", "solved.txt", "outcome.txt",
               "solve_submitted_at.txt", "z_act.txt", "review_gate.txt")
ERROR_STATE_FILES = ("readouts.txt", "z_act.txt")   # quote readout errors verbatim

FIX_HINTS = {
    "heavy_output": "filter the output (tail / Select-Object -Last N) or read it in a subagent",
    "long_reasoning": "a trivial step does not need a reasoning dump; state the decision in one line",
    "whole_file_read": "read state files with tail / -Tail; the last line is the signal",
    "recursive_listing": "use the KB index or a glob with a narrow pattern; never list a tree into context",
    "retry_same_command": "a command run twice in a stage is a loop; change something or escalate",
    "identical_error_twice": "the same error twice means the fix did not land; read the error before retrying",
    "rebuild_chain": "stage scripts are idempotent (ADR 0008); fix the failing stage, do not rebuild the chain",
    "foreground_poll": "the watchdog owns the solve (ADR 0006); read solve_progress.txt once, later",
    "probe_script": "put the probe in a named workspace script so it is replayable and verifiable",
    "idle_gap": "user_wait is the gate; solver_wait is physics; unexplained is a lost session",
    "escalation": "an escalation is right when the phase cannot decide; count them, do not hide them",
    "late_declaration": "declare the phase before the first launch or submit (scripts/session.py --phase)",
    "undeclared_session": "every session declares its phase; an undeclared one is unguarded and uncarded",
    "backend_error": "a GrpcApiError names the call that died, not the cause; check the session is alive first",
    "desktop_recycle": "a recycled desktop costs a licence seat and a cold start; record why in the event",
    "design_misroute": "read 'Active Design set to' at every compile; the DESIGN constant routes the build",
    "solve_anomaly": "a stalled or aborted terminal line needs a decision, not a resubmission",
    "unbanked": "run confirm_solve.py before teardown; unbanked results are purged",
}

# -- what the trace carries: tools and command patterns ---------------------

BASH_TOOLS = frozenset(("bash", "Bash", "PowerShell", "powershell", "shell"))
READ_TOOLS = frozenset(("read", "Read"))
WRITE_TOOLS = frozenset(("write", "Write", "edit", "Edit", "multiedit", "MultiEdit"))
QUESTION_TOOLS = frozenset(("question", "AskUserQuestion", "ask_user", "ask"))
TEXT_KEYS = ("output_head", "output", "error", "text")   # a future trace may carry these

DECLARE_RE = re.compile(r"session\.py\b[^;&|\n]*?--phase\s+(clarify|build|solve)\b")
COMPILE_RE = re.compile(r"compile_spec(?:\.py)?\b")
SPEC_RE = re.compile(r"--spec\s+(\S+)")
DRY_RUN = "--dry-run"
LAUNCH_RE = re.compile(r"--launch\b|launch=True|new_desktop=True")
SOLVE_SUBMIT_RE = re.compile(r"\b08_solve(?:\.py)?\b")
WHOLE_FILE_CMD_RE = re.compile(r"(?:^|[\s;&|(])(?:cat|type|Get-Content|gc)\s")
WHOLE_FILE_TARGET_RE = re.compile(r"solve_progress\.txt|\.log\b|verify[\\/]", re.IGNORECASE)
PARTIAL_READ_RE = re.compile(r"\btail\b|\bhead\b|-Tail\b|-TotalCount\b|-Last\b|-First\b|\bsed\s+-n\b")
RECURSIVE_RE = re.compile(r"\bls\s+-[a-zA-Z]*R|\bls\s+--recursive|Get-ChildItem\b[^;|&]*-Recurse"
                          r"|\bgci\b[^;|&]*-Recurse|\bfind\s+(?:\"[^\"]+\"|\S+)(?![^;|&]*-maxdepth\s+[01]\b)")
SLEEP_RE = re.compile(r"\bStart-Sleep\b|\bsleep\s+\d")
SLEEP_SECONDS_RE = re.compile(r"Start-Sleep\s+(?:-Seconds\s+)?(\d+)|\bsleep\s+(\d+)")
STATE_FILE_RE = re.compile(r"\b(solve_progress|readouts|solved|aedt_port|aedt_process_id|"
                           r"session|z_act|outcome|solve_started|solve_watchdog_pid)\.(?:txt|json)\b")
PROBE_RE = re.compile(r"\bpython3?(?:\.exe)?\s+-c\b")
PROBE_NAME_RE = re.compile(r"probe|tmp", re.IGNORECASE)
REDIRECT_WRITE_RE = re.compile(r">\s*\"?([^\s\"<>|;&]+)")
KILL_RE = re.compile(r"Stop-Process\b|taskkill\b|\bkill\s+-?\d|\bpkill\b")
ANSYSEDT_RE = re.compile(r"ansysedt", re.IGNORECASE)
GRPC_RE = re.compile(r"\b(GrpcApiError|AEDTRuntimeError)\b")
# An AEDT command is a CamelCase name (GetVariables, Subtract, OpenProject);
# the readout experiment's notes write the placeholder `command: X`, which is
# prose, not an error.
GRPC_CMD_RE = re.compile(r"Failed to execute gRPC AEDT command:\s*([A-Z][A-Za-z]{2,})")
ERROR_NAME_RE = re.compile(r"\b([A-Z]\w*(?:Error|Exception))\b")
ROUTE_RE = re.compile(r"route=([\w\-]+)")
ACTIVE_DESIGN_RE = re.compile(r"Active Design set to\s+([^\s,;]+)")
PIN_MOVE_RE = re.compile(r"released the pinned desktop on port (\d+).*?pinned at port (\d+) \(pid (\d+)\)",
                         re.DOTALL)
PIN_ARROW_RE = re.compile(r"[Pp]in moved (\d+)/(\d+) -> (\d+)/(\d+)")
PORT_PID_RE = re.compile(r"port=(\d+)\s+pid=(\d+)")
SESSION_ID_RE = re.compile(r"session_id=(\S+)")
TICK_RE = re.compile(r"^tick=(\d+) status=(\w+) stage=(\w+) elapsed_s=(\d+) .*?watchdog_started=(\d+)"
                     r"(?: evidence=(.*))?$")
KEY_VALUE_RE = re.compile(r"^\s*(\w+)\s*=\s*(.*?)\s*$")
PYTHON_SCRIPT_RE = re.compile(r"\bpython3?(?:\.exe)?\s+(?:-m\s+)?\S+\.py\b|\bpython3?\s+-m\s+\S+")

# The stage a command belongs to when no event says so (fallback only).
STAGE_HINTS = (
    ("solve", re.compile(r"\b08_solve\b|confirm_solve|poll_solve|solve_progress\.txt")),
    ("sync-verify", re.compile(r"12_verify_sync|verify_spec_replay")),
    ("snapshot", re.compile(r"capture_state")),
    ("readout", re.compile(r"11_plots|read_results|extract_active_z|readouts\.txt|z_act")),
    ("summary", re.compile(r"run_card\.py|summary\.md|record_outcome")),
    ("gate", re.compile(r"tier0\.py|tier1\.py|validate_spec|precheck\.py|00_static_gate|record_gate"
                        r"|compile_spec\b[^;&]*--dry-run")),
)

STAGE_START_EVENTS = {"compile.start": "compile", "solve.submitted": "solve"}
STAGE_END_EVENTS = {"compile.end": "compile", "solve.terminal": "solve",
                    "solve.banked": "solve", "solve.unbanked": "solve"}
POINT_EVENTS = {"snapshot.captured": "snapshot", "sync.verify": "sync-verify",
                "readout.attempt": "readout", "card.written": "summary",
                "outcome.recorded": "summary", "gate.recorded": "gate"}


# -- small helpers ----------------------------------------------------------

def _iso(ms):
    if ms is None:
        return "n/a"
    return datetime.fromtimestamp(ms / 1000.0, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _duration(ms):
    ms = int(ms or 0)
    s = ms // 1000
    if s < 60:
        return f"{s} s"
    if s < 3600:
        return f"{s // 60} min {s % 60} s"
    return f"{s // 3600} h {(s % 3600) // 60} min"


def _cmd(step, limit=100):
    return (step.get("command") or "").replace("\n", " ").replace("\r", " ").strip()[:limit]


def normalise_command(command):
    """One spelling for a command: whitespace collapsed, trailing separators cut."""
    return re.sub(r"\s+", " ", (command or "").strip()).rstrip("; ")


def step_text(step):
    """Whatever output text a step carries (`TEXT_KEYS`); "" on today's trace."""
    parts = []
    for key in TEXT_KEYS:
        value = step.get(key)
        if value:
            parts.append(value if isinstance(value, str) else json.dumps(value))
    return "\n".join(parts)


def _is_tool_use(step):
    return step.get("kind") == "tool_use"


def _is_result(step):
    return step.get("kind") == "tool_result"


def _is_bash(step):
    return (step.get("tool") or "") in BASH_TOOLS


def _basename(path):
    return re.split(r"[\\/]", (path or "").strip().strip("\"'"))[-1]


def _segments(command):
    """A shell command split at `;`, `&&`, `||` — one invocation per segment."""
    return [s.strip() for s in re.split(r";|&&|\|\|", command or "") if s.strip()]


def compile_calls(command):
    """`[(spec, dry_run)]` for every compile_spec invocation in a command.

    `spec` is the spec file's basename, or `UNKNOWN_SPEC` when the trace's
    200-character cut lost it: the `--spec` value is the last thing on a cut
    command (its extension may be gone), or `--spec` was cut off entirely.
    A cut command whose compile segment ends in a dangling `-` lost a flag
    that may have been `--dry-run`; such a compile is unknown too, rather
    than counted as a real one.
    """
    command = command or ""
    cut = len(command) >= COMMAND_CHARS
    segments = _segments(command)
    calls = []
    for i, segment in enumerate(segments):
        if not COMPILE_RE.search(segment):
            continue
        last = cut and i == len(segments) - 1
        spec = SPEC_RE.search(segment)
        name = _basename(spec.group(1)) if spec else UNKNOWN_SPEC
        if spec and last and (segment.endswith(spec.group(1)) or not name.endswith((".yaml", ".yml"))):
            name = UNKNOWN_SPEC
        if last and re.search(r"\s-{1,2}[\w-]*$", segment) and DRY_RUN not in segment:
            name = UNKNOWN_SPEC
        calls.append((name, DRY_RUN in segment))
    return calls


def stage_hint(command):
    """The stage a command's script belongs to, or None (fallback attribution)."""
    if SOLVE_SUBMIT_RE.search(command or "") or STAGE_HINTS[0][1].search(command or ""):
        return "solve"
    if any(not dry for _, dry in compile_calls(command)):
        return "compile"
    for stage, rx in STAGE_HINTS:
        if rx.search(command or ""):
            return stage
    return None


def _by_session(steps):
    groups = defaultdict(list)
    for step in steps:
        groups[step.get("session_id")].append(step)
    for group in groups.values():
        group.sort(key=lambda s: (s.get("seq") if s.get("seq") is not None else -1))
    return groups


def _call_index(steps):
    """`{(session, tool_use_id): (tool_use, tool_result)}` for every call."""
    index = {}
    for step in steps:
        if step.get("tool_use_id") is None or step.get("kind") not in ("tool_use", "tool_result"):
            continue
        key = (step.get("session_id"), step["tool_use_id"])
        use, result = index.get(key, (None, None))
        if _is_tool_use(step):
            use = step
        else:
            result = step
        index[key] = (use, result)
    return index


def _call_wall(step, calls):
    """A tool call's duration (use -> result), else the step's latency."""
    pair = calls.get((step.get("session_id"), step.get("tool_use_id")))
    if pair and pair[0] and pair[1] and pair[0].get("ts") is not None and pair[1].get("ts") is not None:
        return max(0, pair[1]["ts"] - pair[0]["ts"])
    return int(step.get("latency_ms") or 0)


def _span_wall(steps):
    stamped = [s for s in steps if s.get("ts") is not None]
    if not stamped:
        return 0
    start = min(s["ts"] for s in stamped)
    end = max(s["ts"] + int(s.get("latency_ms") or 0) for s in stamped)
    return max(0, end - start)


def _seqs(steps):
    return sorted({int(s["seq"]) for s in steps if s.get("seq") is not None})


def _finding(kind, steps=(), session=None, phase=UNDECLARED, stage=BETWEEN, wall=0,
             evidence="", source="trace", requests=None):
    if steps:
        session = session if session is not None else steps[0].get("session_id")
        phase = phase if phase != UNDECLARED else steps[0].get("phase", UNDECLARED)
        stage = stage if stage != BETWEEN else steps[0].get("stage", BETWEEN)
    return {"kind": kind, "severity": "medium", "phase": phase, "stage": stage,
            "cost_tokens": 0, "cost_wall_ms": int(wall or 0), "steps": _seqs(steps),
            "evidence": evidence, "fix_hint": FIX_HINTS[kind], "session": session,
            "source": source, "_steps": list(steps),
            "_requests": set(requests) if requests else None}


# -- machine state ----------------------------------------------------------

def watchdog_runs(text):
    """The watchdog runs `solve_progress.txt` records, one per `watchdog_started`.

    Each: `{started_ms, ticks, status, stage, elapsed_s, end_ms, line}` —
    `status` is the run's last line (a terminal `complete` / `stalled` /
    `aborted`, or `running` when the log ends mid-solve), `end_ms` its ts.
    """
    runs = {}
    order = []
    for line in (text or "").splitlines():
        m = TICK_RE.match(line.strip())
        if not m:
            continue
        tick, status, stage, elapsed, started, evidence = m.groups()
        key = int(started)
        if key not in runs:
            runs[key] = {"started_ms": key * 1000, "ticks": 0, "status": "running",
                         "stage": stage, "elapsed_s": 0, "end_ms": key * 1000, "line": line.strip(),
                         "evidence": None}
            order.append(key)
        run = runs[key]
        run["ticks"] = int(tick) + 1
        run["status"] = status
        run["stage"] = stage
        run["elapsed_s"] = int(elapsed)
        run["end_ms"] = (key + int(elapsed)) * 1000
        run["line"] = line.strip()
        run["evidence"] = evidence
    return [runs[k] for k in order]


def key_values(text):
    """`key=value` lines of a state file (BOM tolerated); other lines skipped."""
    out = {}
    for line in (text or "").lstrip("﻿").splitlines():
        m = KEY_VALUE_RE.match(line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def epoch_lines(text):
    """Epoch-second lines as epoch ms (the append-only solve gate, ticket 02)."""
    stamps = []
    for line in (text or "").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            stamps.append(int(float(line) * 1000))
        except ValueError:
            continue
    return stamps


def solve_windows(events, machine_state):
    """`[(start_ms, end_ms)]` the solver was running: `solve.submitted` ..
    `solve.terminal` from the events, else the watchdog runs."""
    windows = []
    start = None
    for event in sorted(events or (), key=lambda e: e.get("ts_ms") or 0):
        name = event.get("event")
        if name == "solve.submitted":
            start = event.get("ts_ms")
        elif name in STAGE_END_EVENTS and STAGE_END_EVENTS[name] == "solve" and start is not None:
            windows.append((start, event.get("ts_ms") or start))
            start = None
    if start is not None:
        windows.append((start, None))
    if windows:
        return windows
    for run in watchdog_runs((machine_state or {}).get("solve_progress.txt")):
        windows.append((run["started_ms"], run["end_ms"] if run["status"] != "running" else None))
    return windows


# -- attribution ------------------------------------------------------------

def declarations(steps, events, history):
    """Every phase declaration the run recorded, `[(ts_ms, phase, session, source)]`
    oldest first — from the history, the `phase.declared` events and the
    `session.py --phase` commands in the trace. `session` is None when the
    declaration names no session the trace knows (an opencode slug, say), in
    which case it governs every session from its instant on."""
    known = set()
    for step in steps:
        known.add(step.get("session_id"))
        if step.get("parent_session_id"):
            known.add(step["parent_session_id"])
    found = []
    for record in history or ():
        phase = record.get("phase")
        ts = record.get("ts_ms")
        if phase in PHASES and isinstance(ts, int):
            sid = record.get("host_session_id") or None
            found.append((ts, phase, sid if sid in known else None, "history"))
    for event in events or ():
        if event.get("event") != "phase.declared" or event.get("phase") not in PHASES:
            continue
        ts = event.get("ts_ms")
        if not isinstance(ts, int):
            continue
        m = SESSION_ID_RE.search(event.get("detail") or "")
        sid = m.group(1) if m and m.group(1) != "-" else None
        found.append((ts, event["phase"], sid if sid in known else None, "events"))
    for step in steps:
        if not _is_tool_use(step) or not _is_bash(step) or step.get("ts") is None:
            continue
        m = DECLARE_RE.search(step.get("command") or "")
        if m:
            # A declaration a subagent makes is the run's: it governs the
            # parent session and every subagent of it.
            owner = step.get("parent_session_id") or step.get("session_id")
            found.append((int(step["ts"]), m.group(1), owner, "trace"))
    found.sort(key=lambda d: (d[0], d[3]))
    # The same declaration recorded three ways lands within seconds; a phase
    # re-declared within seconds is one whose first attempt did not land
    # (patch-array-5800's solve-1b: declared at 22:29:16 in a command whose
    # cwd broke it, again at 22:29:25). Either way the LATEST instant is the
    # one that governs, so a cluster keeps its last member.
    deduped = []
    for decl in found:
        if deduped and deduped[-1][1] == decl[1] and abs(decl[0] - deduped[-1][0]) <= 10_000 \
                and (deduped[-1][2] in (None, decl[2]) or decl[2] is None):
            deduped[-1] = (decl[0], decl[1], deduped[-1][2] or decl[2], decl[3])
            continue
        deduped.append(decl)
    return deduped


def _phase_of(decls, step):
    """(phase, declaration index, source) governing a step."""
    ts = step.get("ts")
    mine = (step.get("session_id"), step.get("parent_session_id"))
    best = None
    for index, (dts, phase, sid, source) in enumerate(decls):
        if ts is None or dts > ts:
            break
        if sid is None or sid in mine:
            best = (phase, index, source)
    return best or (UNDECLARED, -1, "none")


def stage_windows(events):
    """`[(start_ms, end_ms | None, stage)]` from the events; point events are
    zero-length windows. A `stage.start` inside a compile window is the
    compiler's own sub-stage and stays `compile`."""
    windows = []
    open_by_stage = {}
    for event in sorted(events or (), key=lambda e: e.get("ts_ms") or 0):
        name = event.get("event") or ""
        ts = event.get("ts_ms")
        if not isinstance(ts, int):
            continue
        if name in STAGE_START_EVENTS:
            stage = STAGE_START_EVENTS[name]
            open_by_stage[stage] = len(windows)
            windows.append([ts, None, stage])
        elif name == "stage.start":
            if "compile" in open_by_stage:
                continue
            stage = event.get("stage") or BETWEEN
            open_by_stage[stage] = len(windows)
            windows.append([ts, None, stage])
        elif name in STAGE_END_EVENTS:
            stage = STAGE_END_EVENTS[name]
            if stage in open_by_stage:
                windows[open_by_stage.pop(stage)][1] = ts
        elif name == "stage.end":
            stage = event.get("stage")
            if stage in open_by_stage and "compile" not in open_by_stage:
                windows[open_by_stage.pop(stage)][1] = ts
        elif name in POINT_EVENTS:
            windows.append([ts, ts, POINT_EVENTS[name]])
        elif name.startswith("gate."):
            windows.append([ts, ts, "gate"])
    return [tuple(w) for w in windows]


def _stage_of(windows, start, end):
    """The stage whose window a call [start, end] touches, else None."""
    if start is None:
        return None
    end = end if end is not None else start
    inside = None
    for wstart, wend, stage in windows:
        if start <= wstart <= end:
            return stage                         # an event fired inside the call
        if wstart <= start and (wend is None or start <= wend):
            inside = stage                       # the call ran inside the window
    return inside


def attribute(steps, events=None, history=None):
    """The steps with `phase`, `phase_index`, `phase_source`, `stage` and
    `stage_source` filled in (copies; the input is not touched)."""
    decls = declarations(steps, events, history)
    windows = stage_windows(events)
    calls = _call_index(steps)
    out = []
    for step in steps:
        copy = dict(step)
        phase, index, source = _phase_of(decls, step)
        copy["phase"], copy["phase_index"], copy["phase_source"] = phase, index, source
        stage, stage_source = None, "events"
        pair = calls.get((step.get("session_id"), step.get("tool_use_id")))
        if pair and pair[0] is not None:
            start = pair[0].get("ts")
            end = pair[1].get("ts") if pair[1] else None
        else:
            start, end = step.get("ts"), step.get("ts")
        if windows:
            stage = _stage_of(windows, start, end)
        elif pair and pair[0] is not None and _is_bash(pair[0]):
            stage, stage_source = stage_hint(pair[0].get("command")), "commands"
        else:
            stage_source = "commands"
        copy["stage"] = stage or BETWEEN
        copy["stage_source"] = stage_source
        out.append(copy)
    # A session's steps before its own first declaration belong to that
    # session: the reading a clarify session does before it declares is the
    # clarify session's cost, not nobody's. Only a declaration that names the
    # session (or governs every session) backfills; a session none reaches
    # stays undeclared, which is `undeclared_session`'s signal.
    for session_steps in _by_session(out).values():
        pending = [s for s in session_steps if s["phase"] == UNDECLARED]
        if not pending or len(pending) == len(session_steps):
            continue
        first = min((s for s in session_steps if s["phase"] != UNDECLARED),
                    key=lambda s: s.get("ts") or 0)
        for step in pending:
            step["phase"], step["phase_index"] = first["phase"], first["phase_index"]
            step["phase_source"] = "backfill"
    return out


# -- the classifiers (each takes attributed steps) --------------------------

def find_heavy_output(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    sessions = _by_session(steps)
    out = []
    for step in steps:
        if not _is_result(step) or (step.get("out_bytes") or 0) <= HEAVY_OUTPUT_BYTES:
            continue
        later = sum(1 for s in sessions[step.get("session_id")]
                    if (s.get("seq") or 0) > (step.get("seq") or 0))
        pair = calls.get((step.get("session_id"), step.get("tool_use_id")), (None, None))
        mine = [s for s in pair if s is not None] or [step]
        out.append(_finding(
            "heavy_output", mine, wall=_call_wall(step, calls),
            evidence=f"{step.get('tool') or '?'} returned {step['out_bytes']:,} B: {_cmd(step, 80)}"
                     f" -- stayed in context for {later} later steps"))
    return out


def find_long_reasoning(steps, events=None, machine_state=None):
    firsts = {}
    for step in steps:
        if step.get("tokens_input") is not None:
            firsts.setdefault((step.get("session_id"), step.get("request_id")), step)
    sessions = _by_session(steps)
    out = []
    for step in steps:
        if step.get("kind") != "reasoning":
            continue
        size = int(step.get("out_bytes") or 0)
        estimated = False
        if size == 0:
            first = firsts.get((step.get("session_id"), step.get("request_id")))
            size = int((first or {}).get("tokens_reasoning") or 0) * BYTES_PER_TOKEN
            estimated = True
        if size <= LONG_REASONING_BYTES:
            continue
        following = next((s for s in sessions[step.get("session_id")]
                          if (s.get("seq") or 0) > (step.get("seq") or 0) and _is_tool_use(s)), None)
        tool = f"{following.get('tool')} {_cmd(following, 50)}" if following else "no tool call"
        out.append(_finding(
            "long_reasoning", [step], wall=int(step.get("latency_ms") or 0),
            evidence=f"{size:,} B reasoning{' (estimated from tokens_reasoning)' if estimated else ''}"
                     f" before: {tool}"))
    return out


def _whole_file_read(step):
    command = step.get("command") or ""
    if step.get("tool") in READ_TOOLS:
        return bool(WHOLE_FILE_TARGET_RE.search(command))
    if not _is_bash(step):
        return False
    for segment in _segments(command):
        if WHOLE_FILE_CMD_RE.search(" " + segment) and WHOLE_FILE_TARGET_RE.search(segment) \
                and not PARTIAL_READ_RE.search(segment):
            return True
    return False


def find_whole_file_read(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    out = []
    for step in steps:
        if _is_tool_use(step) and _whole_file_read(step):
            pair = calls.get((step.get("session_id"), step.get("tool_use_id")), (step, None))
            result = pair[1]
            size = f", {result['out_bytes']:,} B" if result and result.get("out_bytes") else ""
            out.append(_finding("whole_file_read", [s for s in pair if s], wall=_call_wall(step, calls),
                                evidence=f"{step.get('tool')} whole-file read{size}: {_cmd(step, 110)}"))
    return out


def find_recursive_listing(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    out = []
    for step in steps:
        if not (_is_tool_use(step) and _is_bash(step) and RECURSIVE_RE.search(step.get("command") or "")):
            continue
        pair = calls.get((step.get("session_id"), step.get("tool_use_id")), (step, None))
        result = pair[1]
        size = result.get("out_bytes") if result else None
        out.append(_finding("recursive_listing", [s for s in pair if s], wall=_call_wall(step, calls),
                            evidence=f"{_cmd(step, 90)} -> {size if size is not None else '?'} B"))
    return out


def find_retry_same_command(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    groups = defaultdict(list)
    for step in steps:
        if _is_tool_use(step) and _is_bash(step) and step.get("command"):
            key = (step.get("session_id"), step.get("phase"), step.get("phase_index"),
                   step.get("stage"), normalise_command(step["command"]))
            groups[key].append(step)
    out = []
    for key, uses in groups.items():
        if len(uses) < RETRY_MIN:
            continue
        mine = []
        for use in uses:
            mine.extend(s for s in calls.get((use.get("session_id"), use.get("tool_use_id")), (use,)) if s)
        out.append(_finding(
            "retry_same_command", mine, phase=key[1], stage=key[3],
            wall=sum(_call_wall(u, calls) for u in uses),
            evidence=f"x{len(uses)} in {key[3]}: {_cmd(uses[0], 90)} (seq {uses[0]['seq']}..{uses[-1]['seq']})"))
    return out


def error_signature(step):
    """What makes two failed results 'the same': the first error class the
    result's text names (when the trace carries text), else the command."""
    text = step_text(step)
    m = GRPC_CMD_RE.search(text)
    if m:
        return f"GrpcApiError {m.group(1)}"
    m = ERROR_NAME_RE.search(text)
    if m:
        return m.group(1)
    return f"{step.get('tool') or '?'}: {normalise_command(step.get('command'))[:100]}"


def find_identical_error_twice(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    out = []
    for session_steps in _by_session(steps).values():
        results = [s for s in session_steps if _is_result(s)]
        for prev, cur in zip(results, results[1:]):
            if not (prev.get("is_error") and cur.get("is_error")):
                continue
            signature = error_signature(prev)
            if signature != error_signature(cur):
                continue
            mine = []
            for r in (prev, cur):
                mine.extend(s for s in calls.get((r.get("session_id"), r.get("tool_use_id")), (r,)) if s)
            out.append(_finding("identical_error_twice", mine,
                                wall=_call_wall(prev, calls) + _call_wall(cur, calls),
                                evidence=f"{signature[:110]} at seq {prev['seq']} and {cur['seq']}"))
    return out


def find_rebuild_chain(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    out = []
    compile_events = [e for e in events or () if e.get("event") == "compile.start"]
    if compile_events:
        by_phase = defaultdict(list)
        decls = declarations(steps, events, None)
        for event in compile_events:
            phase, index, _ = _phase_of(decls, {"ts": event.get("ts_ms"), "session_id": None,
                                                "parent_session_id": None})
            by_phase[(phase, index)].append(event)
        for (phase, index), evs in by_phase.items():
            if len(evs) < REBUILD_MIN:
                continue
            fails = [e.get("verdict") for e in events
                     if e.get("event") == "stage.end" and (e.get("verdict") or "").startswith("FAIL")
                     and evs[0].get("ts_ms", 0) <= (e.get("ts_ms") or 0) <= evs[-1].get("ts_ms", 0)]
            between = "; ".join(f[:60] for f in fails[:3]) or "no FAIL verdict between them"
            out.append(_finding("rebuild_chain", phase=phase, stage="compile", source="events",
                                wall=(evs[-1].get("ts_ms") or 0) - (evs[0].get("ts_ms") or 0),
                                evidence=f"{len(evs)} compile.start in {phase} #{index}: {between}"))
        return out
    by_phase = defaultdict(list)
    for step in steps:
        if _is_tool_use(step) and _is_bash(step) and step.get("phase") == "build":
            real = [spec for spec, dry in compile_calls(step.get("command")) if not dry]
            if real:
                by_phase[(step["phase"], step.get("phase_index"))].append((step, real))
    for (phase, index), compiles in by_phase.items():
        if len(compiles) < REBUILD_MIN:
            continue
        uses = [c[0] for c in compiles]
        first, last = uses[0], uses[-1]
        session = _by_session(steps)[first.get("session_id")]
        edited = []
        for s in session:
            if first["seq"] < s.get("seq", 0) < last["seq"] and s.get("tool") in WRITE_TOOLS and _is_tool_use(s):
                name = _basename(s.get("command"))
                if name and name not in edited:
                    edited.append(name)
        specs = ", ".join(dict.fromkeys(spec for _, real in compiles for spec in real))
        mine = []
        for use in uses:
            mine.extend(s for s in calls.get((use.get("session_id"), use.get("tool_use_id")), (use,)) if s)
        out.append(_finding(
            "rebuild_chain", mine, phase=phase, stage="compile", wall=_span_wall(mine),
            evidence=f"{len(compiles)} compiles in {phase} #{index} ({specs}); edited between: "
                     f"{', '.join(edited[:6]) or 'nothing recorded'}"))
    return out


def find_foreground_poll(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    out = []
    sleeps = defaultdict(list)
    reads = defaultdict(list)
    for step in steps:
        if not (_is_tool_use(step) and _is_bash(step)):
            continue
        command = step.get("command") or ""
        if SLEEP_RE.search(command):
            sleeps[(step.get("session_id"), step.get("phase"), step.get("phase_index"))].append(step)
        m = STATE_FILE_RE.search(command)
        if m and (PARTIAL_READ_RE.search(command) or WHOLE_FILE_CMD_RE.search(" " + command)):
            reads[(step.get("session_id"), m.group(0))].append(step)
    for (session, phase, index), uses in sleeps.items():
        mine = []
        for use in uses:
            mine.extend(s for s in calls.get((use.get("session_id"), use.get("tool_use_id")), (use,)) if s)
        slept = sum(declared_sleep_ms(u.get("command")) for u in uses)
        out.append(_finding(
            "foreground_poll", mine, phase=phase,
            wall=max(slept, sum(_call_wall(u, calls) for u in uses)),
            evidence=f"{len(uses)} sleeping shell call(s) in {phase}, {_duration(slept)} declared: "
                     f"{_cmd(uses[0], 80)}"))
    for (session, name), uses in reads.items():
        uses.sort(key=lambda s: s.get("ts") or 0)
        i = 0
        while i < len(uses):
            j = i
            while j + 1 < len(uses) and (uses[j + 1].get("ts") or 0) - (uses[i].get("ts") or 0) \
                    <= FOREGROUND_POLL_WINDOW_MS:
                j += 1
            if j - i + 1 >= FOREGROUND_POLL_MIN:
                window = uses[i:j + 1]
                mine = []
                for use in window:
                    mine.extend(s for s in calls.get((use.get("session_id"), use.get("tool_use_id")), (use,)) if s)
                span = (window[-1].get("ts") or 0) - (window[0].get("ts") or 0)
                out.append(_finding(
                    "foreground_poll", mine, wall=span,
                    evidence=f"{len(window)} reads of {name} within {_duration(span)} "
                             f"(seq {window[0]['seq']}..{window[-1]['seq']})"))
                i = j + 1
            else:
                i += 1
    return out


def declared_sleep_ms(command):
    """The seconds a shell command says it sleeps, as ms (opencode's trace
    stamps a call at its completion, so the call itself measures ~0)."""
    total = 0
    for m in SLEEP_SECONDS_RE.finditer(command or ""):
        total += int(m.group(1) or m.group(2) or 0)
    return total * 1000


def _is_probe(step):
    command = step.get("command") or ""
    if _is_bash(step):
        if PROBE_RE.search(command):
            return "python -c"
        m = REDIRECT_WRITE_RE.search(command)
        if m and PROBE_NAME_RE.search(_basename(m.group(1))):
            return "probe file"
        return None
    if step.get("tool") in WRITE_TOOLS and PROBE_NAME_RE.search(_basename(command)):
        return "probe file"
    return None


def find_probe_script(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    groups = defaultdict(list)
    for step in steps:
        if _is_tool_use(step):
            how = _is_probe(step)
            if how:
                groups[(step.get("session_id"), step.get("phase"), step.get("phase_index"))].append((step, how))
    out = []
    for (session, phase, index), found in groups.items():
        uses = [f[0] for f in found]
        inline = sum(1 for _, how in found if how == "python -c")
        mine = []
        for use in uses:
            mine.extend(s for s in calls.get((use.get("session_id"), use.get("tool_use_id")), (use,)) if s)
        out.append(_finding(
            "probe_script", mine, phase=phase, wall=sum(_call_wall(u, calls) for u in uses),
            evidence=f"{len(uses)} probe(s) in {phase} #{index}: {inline} python -c, "
                     f"{len(uses) - inline} probe/tmp file(s); first: {_cmd(uses[0], 70)}"))
    return out


def find_idle_gap(steps, events=None, machine_state=None):
    windows = solve_windows(events, machine_state)
    out = []
    for session_steps in _by_session(steps).values():
        for step, nxt in zip(session_steps, session_steps[1:]):
            gap = int(step.get("latency_ms") or 0)
            if gap < IDLE_GAP_MS or step.get("ts") is None:
                continue
            start, end = step["ts"], step["ts"] + gap
            if nxt.get("role") == "user":
                cls = "user_wait"
            elif any(ws <= end and (we is None or start <= we) for ws, we in windows):
                cls = "solver_wait"
            else:
                cls = "unexplained"
            out.append(_finding(
                "idle_gap", [step], wall=gap,
                evidence=f"{_duration(gap)} idle ({cls}) from {_iso(start)} before seq {nxt.get('seq')} "
                         f"{nxt.get('kind')}/{nxt.get('role')}"))
    return out


def find_escalation(steps, events=None, machine_state=None):
    out = []
    seen_phases = set()
    for event in sorted(events or (), key=lambda e: e.get("ts_ms") or 0):
        name = event.get("event")
        line = (event.get("verdict") or event.get("detail") or "")[:120]
        if name in ("phase.refused", "budget.escalate"):
            out.append(_finding("escalation", phase=event.get("phase") or UNDECLARED,
                                source="events", evidence=f"{name}: {line}"))
        elif name == "gate.recorded" and "verdict=fixes" in (event.get("detail") or ""):
            out.append(_finding("escalation", phase=event.get("phase") or UNDECLARED, stage="gate",
                                source="events", evidence=f"gate fixes requested: {line}"))
        elif name == "phase.declared":
            phase = event.get("phase")
            if phase in seen_phases:
                out.append(_finding("escalation", phase=phase, source="events",
                                    evidence=f"phase re-declared: {line}"))
            seen_phases.add(phase)
    calls = _call_index(steps)
    for session_steps in _by_session(steps).values():
        for i, step in enumerate(session_steps):
            if _is_tool_use(step) and step.get("tool") in QUESTION_TOOLS:
                pair = calls.get((step.get("session_id"), step.get("tool_use_id")), (step, None))
                out.append(_finding("escalation", [s for s in pair if s], wall=_call_wall(step, calls),
                                    evidence=f"question asked: {_cmd(step, 100)}"))
            elif i and step.get("role") == "user" and step.get("kind") == "text":
                prev = session_steps[i - 1]
                if prev.get("role") == "assistant" and prev.get("kind") == "text":
                    waited = int(prev.get("latency_ms") or 0)
                    out.append(_finding(
                        "escalation", [prev, step], wall=waited,
                        evidence=f"user reply after the agent stopped: waited {_duration(waited)}, "
                                 f"{step.get('in_bytes') or 0} B reply at seq {step.get('seq')}"))
    return out


def find_late_declaration(steps, events=None, machine_state=None):
    out = []
    decls = declarations(steps, events, None)
    declared = [e for e in events or () if e.get("event") == "phase.declared"]
    if declared:
        for event in sorted(events, key=lambda e: e.get("ts_ms") or 0):
            name = event.get("event")
            if name not in ("desktop.launch", "solve.submitted"):
                continue
            owners = ("solve",) if name == "solve.submitted" else ("build", "solve")
            before = [d for d in declared if (d.get("ts_ms") or 0) <= (event.get("ts_ms") or 0)]
            current = before[-1].get("phase") if before else None
            if current not in owners:
                out.append(_finding("late_declaration", phase=current or UNDECLARED, source="events",
                                    stage="solve" if name == "solve.submitted" else BETWEEN,
                                    evidence=f"{name} at {_iso(event.get('ts_ms'))} with phase "
                                             f"{current or 'undeclared'} (owner: {'/'.join(owners)})"))
        return out
    # Fallback: the solve instants the machine state recorded against the
    # declarations the trace (or history) knows.
    state = machine_state or {}
    submits = [(ms, "solve_submitted_at.txt") for ms in epoch_lines(state.get("solve_submitted_at.txt"))]
    if not submits:
        submits = [(run["started_ms"], f"watchdog_started={run['started_ms'] // 1000}")
                   for run in watchdog_runs(state.get("solve_progress.txt"))]
    for ms, origin in submits:
        before = [d for d in decls if d[0] <= ms]
        current = before[-1][1] if before else None
        if current == "solve":
            continue
        after = next((d for d in decls if d[0] > ms and d[1] == "solve"), None)
        late = f"{_duration(after[0] - ms)} before the solve declaration at {_iso(after[0])}" \
            if after else "with no solve declaration at all"
        out.append(_finding("late_declaration", phase=current or UNDECLARED, stage="solve", source="state",
                            evidence=f"solve submitted {_iso(ms)} ({origin}) in phase "
                                     f"{current or 'undeclared'}, {late}"))
    for step in steps:
        if _is_tool_use(step) and _is_bash(step) and LAUNCH_RE.search(step.get("command") or "") \
                and step.get("phase") not in ("build", "solve"):
            out.append(_finding("late_declaration", [step], stage=BETWEEN,
                                evidence=f"desktop launch in phase {step.get('phase')}: {_cmd(step, 90)}"))
    return out


def find_undeclared_session(steps, events=None, machine_state=None):
    out = []
    for session, session_steps in _by_session(steps).items():
        if any(s.get("parent_session_id") for s in session_steps):
            continue                                  # a subagent inherits its parent's phase
        if any(s.get("phase", UNDECLARED) != UNDECLARED for s in session_steps):
            continue
        requests = {(session, s.get("request_id")) for s in session_steps if s.get("tokens_input") is not None}
        out.append(_finding("undeclared_session", session=session, requests=requests,
                            wall=_span_wall(session_steps),
                            evidence=f"session {session}: {len(session_steps)} steps, no phase declaration "
                                     f"in history, events or trace"))
    return out


def find_backend_error(steps, events=None, machine_state=None):
    calls = _call_index(steps)
    groups = defaultdict(list)
    for step in steps:
        if not _is_result(step):
            continue
        text = step_text(step)
        if not GRPC_RE.search(text):
            continue
        commands = GRPC_CMD_RE.findall(text) or [GRPC_RE.search(text).group(1)]
        for command in commands:
            groups[(step.get("session_id"), step.get("phase"), step.get("stage"), command)].append(step)
    out = []
    for (session, phase, stage, command), results in groups.items():
        mine = []
        for r in results:
            mine.extend(s for s in calls.get((r.get("session_id"), r.get("tool_use_id")), (r,)) if s)
        out.append(_finding("backend_error", mine, phase=phase, stage=stage,
                            wall=sum(_call_wall(r, calls) for r in results),
                            evidence=f"GrpcApiError {command} x{len(results)} in {stage}: {_cmd(results[0], 60)}"))
    counts = defaultdict(lambda: defaultdict(int))
    routes = {}
    for name in ERROR_STATE_FILES:
        text = (machine_state or {}).get(name) or ""
        for command in GRPC_CMD_RE.findall(text):
            counts[command][name] += 1
        for other in GRPC_RE.findall(text):
            if other != "GrpcApiError" and not GRPC_CMD_RE.search(text):
                counts[other][name] += 1
        m = ROUTE_RE.search(text)
        if m:
            routes[name] = m.group(1)
    for command, files in counts.items():
        total = sum(files.values())
        where = ", ".join(f"{n} x{c}" for n, c in files.items())
        route = "; ".join(f"{n}: route={r}" for n, r in routes.items() if n in files)
        out.append(_finding("backend_error", phase="solve", stage="readout", source="state",
                            evidence=f"GrpcApiError {command} x{total} quoted by {where}"
                                     + (f" ({route})" if route else "")))
    return out


def find_desktop_recycle(steps, events=None, machine_state=None):
    out = []
    last = {}
    for event in sorted(events or (), key=lambda e: e.get("ts_ms") or 0):
        name = event.get("event")
        phase = event.get("phase") or UNDECLARED
        if name == "desktop.recycle":
            out.append(_finding("desktop_recycle", phase=phase, stage="desktop", source="events",
                                evidence=f"desktop.recycle: {(event.get('detail') or '')[:110]}"))
        elif name in ("desktop.attach", "desktop.launch"):
            m = PORT_PID_RE.search(event.get("detail") or "")
            if not m:
                continue
            pin = (m.group(1), m.group(2))
            if phase in last and last[phase] != pin:
                out.append(_finding("desktop_recycle", phase=phase, stage="desktop", source="events",
                                    evidence=f"{name}: port {last[phase][0]}/pid {last[phase][1]} -> "
                                             f"port {pin[0]}/pid {pin[1]} within {phase}"))
            last[phase] = pin
    calls = _call_index(steps)
    for step in steps:
        if _is_tool_use(step) and _is_bash(step):
            command = step.get("command") or ""
            if KILL_RE.search(command) and ANSYSEDT_RE.search(command):
                pair = calls.get((step.get("session_id"), step.get("tool_use_id")), (step, None))
                out.append(_finding("desktop_recycle", [s for s in pair if s], wall=_call_wall(step, calls),
                                    evidence=f"desktop killed from the shell: {_cmd(step, 90)}"))
    text = (machine_state or {}).get("readouts.txt") or ""
    moves = []
    for m in PIN_MOVE_RE.finditer(text):
        moves.append((m.group(1), None, m.group(2), m.group(3)))
    for m in PIN_ARROW_RE.finditer(text):
        moves.append(m.groups())
    seen = set()
    port_now = ((machine_state or {}).get("aedt_port.txt") or "").strip()
    for old_port, old_pid, new_port, new_pid in moves:
        if (old_port, new_port) in seen:
            continue
        seen.add((old_port, new_port))
        out.append(_finding("desktop_recycle", phase="solve", stage="readout", source="state",
                            evidence=f"pin moved port {old_port}{'/pid ' + old_pid if old_pid else ''} -> "
                                     f"port {new_port}/pid {new_pid} (readouts.txt); aedt_port.txt now "
                                     f"{port_now or 'absent'}"))
    return out


def _routing_edit(step):
    command = step.get("command") or ""
    if step.get("tool") in WRITE_TOOLS:
        return _basename(command) == ROUTING_FILE
    return _is_bash(step) and ROUTING_FILE in command and bool(
        re.search(r"sed\s+-i|Set-Content|>\s*\S*" + re.escape(ROUTING_FILE), command))


def find_design_misroute(steps, events=None, machine_state=None):
    """A spec compiled on both sides of a `ws_common.py` edit inside one build
    phase: the first compile was routed by the DESIGN constant as it stood
    before the edit. When the trace carries output text the two `Active
    Design set to` names are quoted; when the cut command lost every spec
    before the edit, the finding says so instead of guessing the spec."""
    calls = _call_index(steps)
    out = []
    for session_steps in _by_session(steps).values():
        by_phase = defaultdict(list)
        for step in session_steps:
            if _is_tool_use(step) and step.get("phase") == "build":
                by_phase[(step.get("phase"), step.get("phase_index"))].append(step)
        for (phase, index), uses in by_phase.items():
            groups = [[]]                      # compiles between routing edits
            edits = []
            for use in uses:
                if _routing_edit(use):
                    edits.append(use)
                    groups.append([])
                    continue
                if not _is_bash(use):
                    continue
                result = calls.get((use.get("session_id"), use.get("tool_use_id")), (None, None))[1]
                m = ACTIVE_DESIGN_RE.search(step_text(result) if result else "")
                design = m.group(1) if m else None
                for spec, dry in compile_calls(use.get("command")):
                    if not dry:
                        groups[-1].append((use, spec, design))
            for k, edit in enumerate(edits):
                before, after = groups[k], groups[k + 1]
                if not before or not after:
                    continue
                known = {spec for _, spec, _ in before if spec != UNKNOWN_SPEC}
                unknown = [c for c in before if c[1] == UNKNOWN_SPEC]
                after_specs = {spec for _, spec, _ in after}
                shared = known & after_specs
                if shared:
                    spec = sorted(shared)[0]
                    firsts = [c for c in before if c[1] == spec]
                    seconds = [c for c in after if c[1] == spec]
                    what = spec
                elif unknown and after_specs - known:
                    # The compiles before the edit whose spec the cut command
                    # lost may have been the spec compiled after it. Reported
                    # as possible, never as confirmed: only the full command
                    # (or the output) can settle it.
                    candidates = sorted(after_specs - known)
                    firsts = unknown
                    seconds = [c for c in after if c[1] in candidates]
                    what = (f"POSSIBLE misroute: {len(unknown)} compile(s) whose --spec the "
                            f"{COMMAND_CHARS}-char command cut lost, then {', '.join(candidates)},")
                else:
                    continue
                first_design = next((d for _, _, d in firsts if d), None)
                second_design = next((d for _, _, d in seconds if d), None)
                designs = (f" (Active Design {first_design} -> {second_design})"
                           if first_design and second_design and first_design != second_design else "")
                mine = []
                for u in [c[0] for c in firsts] + [edit] + [c[0] for c in seconds]:
                    mine.extend(s for s in calls.get((u.get("session_id"), u.get("tool_use_id")), (u,)) if s)
                out.append(_finding(
                    "design_misroute", mine, phase=phase, stage="compile", wall=_span_wall(mine),
                    evidence=f"{what} compiled at seq {firsts[0][0]['seq']} under the DESIGN {ROUTING_FILE} "
                             f"named before its edit at seq {edit['seq']}, then again at seq "
                             f"{seconds[0][0]['seq']}{designs}"))
    return out


def find_solve_anomaly(steps, events=None, machine_state=None):
    out = []
    terminals = [e for e in events or () if e.get("event") == "solve.terminal"]
    submitted = [e for e in events or () if e.get("event") == "solve.submitted"]
    if terminals or submitted:
        for event in terminals:
            detail = event.get("detail") or ""
            m = re.search(r"status=(\w+)", detail)
            if m and m.group(1) in ("stalled", "aborted"):
                out.append(_finding("solve_anomaly", phase=event.get("phase") or "solve", stage="solve",
                                    source="events", evidence=f"watchdog terminal: {detail[:140]}"))
        if len(submitted) > 1:
            out.append(_finding("solve_anomaly", phase="solve", stage="solve", source="events",
                                evidence=f"{len(submitted)} solve.submitted events: "
                                         + ", ".join(_iso(e.get("ts_ms")) for e in submitted)))
        return out
    state = machine_state or {}
    runs = watchdog_runs(state.get("solve_progress.txt"))
    for run in runs:
        if run["status"] in ("stalled", "aborted"):
            out.append(_finding("solve_anomaly", phase="solve", stage="solve", source="state",
                                wall=run["elapsed_s"] * 1000,
                                evidence=f"watchdog terminal: {run['line'][:140]}"))
    gates = epoch_lines(state.get("solve_submitted_at.txt"))
    submissions = len(gates) if gates else len(runs)
    if submissions > 1:
        origin = "solve_submitted_at.txt" if gates else "watchdog runs in solve_progress.txt"
        statuses = ", ".join(f"{_iso(r['started_ms'])} {r['status']}" for r in runs)
        out.append(_finding("solve_anomaly", phase="solve", stage="solve", source="state",
                            evidence=f"{submissions} solve submissions ({origin}): {statuses}"))
    return out


def find_unbanked(steps, events=None, machine_state=None):
    out = []
    ordered = sorted(events or (), key=lambda e: e.get("ts_ms") or 0)
    terminals = [e for e in ordered if e.get("event") == "solve.terminal"]
    if terminals:
        for event in terminals:
            if "status=complete" not in (event.get("detail") or ""):
                continue
            banked = any(e.get("event") == "solve.banked" and (e.get("ts_ms") or 0) >= (event.get("ts_ms") or 0)
                         for e in ordered)
            if not banked:
                out.append(_finding("unbanked", phase=event.get("phase") or "solve", stage="solve",
                                    source="events",
                                    evidence=f"solve.terminal complete at {_iso(event.get('ts_ms'))} "
                                             f"with no solve.banked after it"))
        return out
    state = machine_state or {}
    solved = key_values(state.get("solved.txt"))
    banked_at = None
    try:
        banked_at = int(float(solved["banked_at"])) * 1000
    except (KeyError, ValueError):
        pass
    for run in watchdog_runs(state.get("solve_progress.txt")):
        if run["status"] != "complete":
            continue
        if banked_at is not None and banked_at >= run["end_ms"]:
            continue
        why = "solved.txt absent or without banked_at" if banked_at is None \
            else f"solved.txt banked_at={_iso(banked_at)} precedes it"
        out.append(_finding("unbanked", phase="solve", stage="solve", source="state",
                            evidence=f"watchdog complete at {_iso(run['end_ms'])} "
                                     f"(watchdog_started={run['started_ms'] // 1000}) not banked: {why}"))
    return out


CLASSIFIERS = (find_heavy_output, find_long_reasoning, find_whole_file_read,
               find_recursive_listing, find_retry_same_command, find_identical_error_twice,
               find_rebuild_chain, find_foreground_poll, find_probe_script, find_idle_gap,
               find_escalation, find_late_declaration, find_undeclared_session,
               find_backend_error, find_desktop_recycle, find_design_misroute,
               find_solve_anomaly, find_unbanked)


# -- cost, severity, the entry point ----------------------------------------

def request_tokens(steps):
    """`{(session, request_id): billed}` — input + output, once per request."""
    out = {}
    for step in steps:
        if step.get("tokens_input") is None:
            continue
        key = (step.get("session_id"), step.get("request_id"))
        out[key] = int(step.get("tokens_input") or 0) + int(step.get("tokens_output") or 0)
    return out


def run_tokens(steps):
    return sum(request_tokens(steps).values())


def _claimed_requests(finding, calls):
    if finding.get("_requests") is not None:
        return set(finding["_requests"])
    claimed = set()
    for step in finding.get("_steps") or ():
        rid = step.get("request_id")
        if rid is None and _is_result(step):
            use = calls.get((step.get("session_id"), step.get("tool_use_id")), (None, None))[0]
            rid = use.get("request_id") if use else None
        if rid is not None:
            claimed.add((step.get("session_id"), rid))
    return claimed


def attach_costs(findings, steps):
    """Fill `cost_tokens`: a request counts once per kind (the heaviest
    finding claims it), so the findings of one kind never exceed the run."""
    tokens = request_tokens(steps)
    calls = _call_index(steps)
    by_kind = defaultdict(list)
    for finding in findings:
        finding["_claim"] = _claimed_requests(finding, calls)
        finding["_raw"] = sum(tokens.get(k, 0) for k in finding["_claim"])
        by_kind[finding["kind"]].append(finding)
    for kind, group in by_kind.items():
        counted = set()
        for finding in sorted(group, key=lambda f: (-f["_raw"], -f["cost_wall_ms"])):
            if kind in WALL_ONLY_KINDS:
                finding["cost_tokens"] = 0
                continue
            fresh = finding["_claim"] - counted
            finding["cost_tokens"] = sum(tokens.get(k, 0) for k in fresh)
            counted |= fresh
    for finding in findings:
        for key in ("_steps", "_requests", "_claim", "_raw"):
            finding.pop(key, None)
    return findings


def severity_of(finding, total_tokens):
    share = finding["cost_tokens"] / total_tokens if total_tokens else 0.0
    if share > HIGH_TOKEN_SHARE or finding["cost_wall_ms"] > HIGH_WALL_MS:
        return "high"
    if finding["kind"] in DISCIPLINE_KINDS and share < LOW_TOKEN_SHARE \
            and finding["cost_wall_ms"] < LOW_WALL_MS:
        return "low"
    return "medium"


def analyze(steps, events=None, history=None, machine_state=None):
    """Every finding of every classifier, costed, graded, heaviest first."""
    attributed = attribute(steps, events, history)
    findings = []
    for classifier in CLASSIFIERS:
        findings.extend(classifier(attributed, events or [], machine_state or {}))
    attach_costs(findings, attributed)
    total = run_tokens(attributed)
    for finding in findings:
        finding["severity"] = severity_of(finding, total)
    findings.sort(key=lambda f: (-f["cost_tokens"], -f["cost_wall_ms"], f["kind"], f["evidence"]))
    return findings


def stage_table(steps, events=None, history=None):
    """One row per (phase, stage): where the wall, the steps and the tokens
    went. Rows: `{phase, stage, stage_source, start, wall_ms, steps, tokens,
    script_runs, fails, retries}`, ordered by start."""
    attributed = attribute(steps, events, history)
    tokens = request_tokens(attributed)
    groups = defaultdict(list)
    for step in attributed:
        groups[(step["phase"], step["phase_index"], step["stage"])].append(step)
    rows = []
    for (phase, index, stage), group in groups.items():
        firsts = {(s.get("session_id"), s.get("request_id")) for s in group
                  if s.get("tokens_input") is not None}
        bash = [s for s in group if _is_tool_use(s) and _is_bash(s)]
        distinct = {normalise_command(s.get("command")) for s in bash}
        stamped = [s["ts"] for s in group if s.get("ts") is not None]
        rows.append({
            "phase": phase, "phase_index": index, "stage": stage,
            "stage_source": group[0].get("stage_source"),
            "start": min(stamped) if stamped else None,
            "wall_ms": _span_wall(group),
            "steps": len(group),
            "tokens": sum(tokens.get(k, 0) for k in firsts),
            "script_runs": sum(1 for s in bash if PYTHON_SCRIPT_RE.search(s.get("command") or "")),
            "fails": sum(1 for s in group if _is_result(s) and s.get("is_error")),
            "retries": max(0, len(bash) - len(distinct)),
        })
    rows.sort(key=lambda r: (r["start"] if r["start"] is not None else -1, r["phase"], r["stage"]))
    return rows
