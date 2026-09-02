"""The session boundary, enforced — ticket 14's first checklist item.

A run is three phase sessions (ADR 0007): clarify, build, solve. Until now that
was advisory: the phases lived in prose in SKILL.md and in the State ledger, and
nothing stopped a session from doing another phase's work. Cell S11 (2026-08-17)
showed what that costs. Asked for a coupled-line filter and finding the repo has
no even/odd-mode synthesis, it began writing a 2D finite-difference field solver
and spent 51 minutes, 151,526 tokens and 250 parts debugging it **inside a
Clarification block**, delivering nothing. That is `shiny-canyon`'s 25-hour
failure reproduced in under an hour.

The lesson from that cell is specifically about *form*: the gap was documented,
correctly, in `precheck-tolerances.json`, and the agent read it, quoted it, and
proceeded anyway. Prose that informs does not bind. So this module does not
advise — it refuses, and the refusal is a non-zero exit from the tool the action
would have gone through.

## What it does and does not cover

Covered: every expensive, irreversible action that goes through this repo's own
tooling. Launching an AEDT desktop, compiling onto one, solving. Those are the
actions worth a hard boundary and they all funnel through `compile_spec`,
`tier1`, and the staged solve scripts.

**Not covered: an arbitrary `python -c` in a bash call.** S11's solver was
written that way and this module could not have stopped it. Closing that needs
per-phase tool gating in the harness, which is ticket 14's remaining work and is
recorded as such. What this does close is the far more expensive class: nothing
reaches a licence or a solver outside the phase that owns it.

## The budget

A phase also carries a call budget; the default matches SKILL.md's ~60-call
escalation. The count it is judged against is the **actual** tool-call count
from the step trace — `results/state/trace/<session-id>.steps.jsonl`, one JSON
object per line, a tool call being `"kind": "tool_use"` (run logging, ticket
04) — read by `trace_calls()`. Nobody ever called `note_call` during a run (the
last run's card read `calls: 0` against a budget of 60), so a verdict without a
trace says `calls unaccounted (no trace)` rather than pretending zero calls were
made. `note_call` remains for a driver that does count by hand; it is used only
when it was actually advanced.

## The record (run logging, ticket 01)

`session.json` is the *current* session, and it is overwritten on every
declaration because the phase gate wants exactly one answer. That made it a
poor record: the last run's file was overwritten by a later readout experiment
and the run's own three sessions were no longer findable from the workspace.
So `start()` also appends one line to `sessions.jsonl` — append-only, one
record per declaration, re-declaring a phase appends rather than replaces —
and writes `run.json` once, on the first declaration, naming the run. The
JSONL is the history; `session.json` keeps its role and format unchanged.

Declarations, refusals and budget escalations are also events
(`hfss_spec.events`, ticket 03): `phase.declared`, `phase.refused` (with the
action) and `budget.escalate` land in `events.jsonl` beside the history.
"""

from __future__ import annotations

import json
import os
import subprocess
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Optional

from . import events

CLARIFY, BUILD, SOLVE = "clarify", "build", "solve"
PHASES = (CLARIFY, BUILD, SOLVE)

# Which phase may perform which action. The names are the actions worth
# guarding: each is expensive, irreversible, or both.
ACTIONS = {
    # offline: writing and gating a spec. Legal everywhere - a build session
    # re-gating its own spec is normal, and cheap.
    "author_spec":   (CLARIFY, BUILD, SOLVE),
    "gate_spec":     (CLARIFY, BUILD, SOLVE),
    # a desktop launch costs a licence seat and 6-25 s of cold start
    "launch_desktop": (BUILD, SOLVE),
    # building geometry onto a live desktop
    "compile_model":  (BUILD,),
    # the solve itself, and anything that consumes solver time
    "solve":          (SOLVE,),
}

DEFAULT_CALL_BUDGET = 60

# Filename kept next to the other machine state, so a later session or a human
# reads the phase the same way they read everything else (execution.md).
STATE_FILE = "session.json"
# The append-only declaration history and the run's identity, beside it.
HISTORY_FILE = "sessions.jsonl"
RUN_FILE = "run.json"

# The checkout this module lives in is the one whose skill text runs: the
# installed skill is a link back into it (scripts/install_skill.py).
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class PhaseViolation(RuntimeError):
    """Raised when a phase attempts an action another phase owns."""


class UnknownAction(KeyError):
    """Raised for an action name not in ACTIONS - a typo must not pass silently."""


# The harness a session runs under, and its id there, so the run card can
# find the session afterwards without a slug. Claude Code exports its id to
# every shell command; opencode does not export one this module knows of, so
# a session there records nothing and the card falls back to its slug lookup.
HOST_CLAUDE_CODE = "claude-code"
HOST_OPENCODE = "opencode"
ENV_CLAUDE_SESSION_ID = "CLAUDE_CODE_SESSION_ID"


def detect_host(environ=None) -> tuple:
    """(host, session_id) from the environment; ("", "") when unrecognised."""
    env = os.environ if environ is None else environ
    claude_id = env.get(ENV_CLAUDE_SESSION_ID, "").strip()
    if claude_id:
        return HOST_CLAUDE_CODE, claude_id
    return "", ""


@dataclass
class Session:
    phase: str
    name: str = ""
    started_ms: int = 0
    calls: int = 0
    call_budget: int = DEFAULT_CALL_BUDGET
    escalations: list = field(default_factory=list)
    host: str = ""
    host_session_id: str = ""

    # -- persistence -------------------------------------------------------
    @staticmethod
    def path_for(state_dir) -> str:
        return os.path.join(str(state_dir), STATE_FILE)

    def save(self, state_dir) -> str:
        os.makedirs(str(state_dir), exist_ok=True)
        target = self.path_for(state_dir)
        with open(target, "w", encoding="utf-8") as handle:
            json.dump(asdict(self), handle, indent=2, sort_keys=True)
        return target

    @classmethod
    def load(cls, state_dir) -> Optional["Session"]:
        try:
            with open(cls.path_for(state_dir), encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, ValueError):
            return None
        if data.get("phase") not in PHASES:
            return None
        allowed = {f for f in cls.__dataclass_fields__}      # ignore unknown keys
        return cls(**{k: v for k, v in data.items() if k in allowed})

    # -- the boundary ------------------------------------------------------
    def may(self, action: str) -> bool:
        try:
            return self.phase in ACTIONS[action]
        except KeyError:
            raise UnknownAction(action) from None

    def require(self, action: str) -> None:
        """Permit the action, or raise with the phase that owns it."""
        if self.may(action):
            return
        owners = ", ".join(ACTIONS[action])
        raise PhaseViolation(
            f"a '{self.phase}' session may not {action!r}; that belongs to the "
            f"'{owners}' phase. Report what is done and what is blocking, and "
            f"let the user open the right session - do not work around this."
        )

    # -- the budget --------------------------------------------------------
    def note_call(self, count: int = 1) -> int:
        self.calls += count
        return self.calls

    def exceeds(self, calls: Optional[int]) -> bool:
        """True when `calls` has reached the budget; an unknown count never does."""
        return self.call_budget > 0 and calls is not None and calls >= self.call_budget

    @property
    def over_budget(self) -> bool:
        return self.exceeds(self.calls)

    def budget_verdict(self, trace_calls: Optional[int] = None,
                       state_dir=None) -> str:
        """The verdict against the actual call count.

        `trace_calls` is the tool-call count from the step trace (see
        `trace_calls()`), or None when no trace has been extracted. With no
        trace and no hand-advanced count the verdict says the calls are
        unaccounted — it never reports 0 calls as a fact. With a `state_dir`,
        an ESCALATE verdict is also recorded as a `budget.escalate` event.
        """
        if trace_calls is not None:
            calls, source = trace_calls, "trace"
        elif self.calls:
            calls, source = self.calls, "note_call"
        else:
            return (f"ok: session phase={self.phase} calls unaccounted (no trace) "
                    f"budget={self.call_budget}")
        if not self.exceeds(calls):
            return (f"ok: session phase={self.phase} calls={calls}/"
                    f"{self.call_budget} ({source})")
        verdict = (f"ESCALATE: session phase={self.phase} calls={calls} ({source}) has "
                   f"reached its budget of {self.call_budget} without finishing. "
                   f"A session this long is looping, not converging - report state "
                   f"and hand the decision to the user.")
        if state_dir is not None:
            events.emit(state_dir, "budget.escalate", phase=self.phase,
                        verdict=verdict,
                        detail=f"calls={calls} budget={self.call_budget} source={source}")
        return verdict


# -- the trace: the actual call count (run logging, tickets 02 / 04) ---------

TRACE_DIR = "trace"
TRACE_SUFFIX = ".steps.jsonl"
STEP_KIND_TOOL_USE = "tool_use"


def trace_dir(state_dir) -> str:
    return os.path.join(str(state_dir), TRACE_DIR)


def trace_calls(state_dir) -> Optional[int]:
    """Tool calls recorded under `results/state/trace/*.steps.jsonl`, or None.

    One JSON object per line; a tool call is `"kind": "tool_use"`. Every
    trace file in the directory counts (a run is three sessions plus
    subagents, each its own file). None — not 0 — when no trace file exists:
    that is the difference between "no calls" and "nobody looked". A torn
    or foreign line is skipped.
    """
    try:
        names = sorted(os.listdir(trace_dir(state_dir)))
    except OSError:
        return None
    files = [n for n in names if n.endswith(TRACE_SUFFIX)]
    if not files:
        return None
    count = 0
    for name in files:
        try:
            with open(os.path.join(trace_dir(state_dir), name), encoding="utf-8") as handle:
                lines = handle.read().splitlines()
        except OSError:
            continue
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                step = json.loads(line)
            except ValueError:
                continue
            if isinstance(step, dict) and step.get("kind") == STEP_KIND_TOOL_USE:
                count += 1
    return count


def start(phase: str, name: str = "", state_dir=None,
          call_budget: int = DEFAULT_CALL_BUDGET,
          host: Optional[str] = None,
          host_session_id: Optional[str] = None,
          task_doc: str = "") -> Session:
    """Begin a phase session, persisting it when a state dir is given.

    `host` / `host_session_id` default to what `detect_host()` sees in the
    environment; pass them explicitly to override or to record an opencode
    slug by hand. With a state dir the declaration is recorded three ways:
    `session.json` (the current session, overwritten), one appended line in
    `sessions.jsonl` (the history), and `run.json` if this is the run's first
    declaration (`task_doc` names the request document it answers).
    """
    if phase not in PHASES:
        raise ValueError(f"phase must be one of {PHASES}, got {phase!r}")
    detected_host, detected_id = detect_host()
    session = Session(phase=phase, name=name,
                      started_ms=int(time.time() * 1000),
                      call_budget=call_budget,
                      host=detected_host if host is None else host,
                      host_session_id=(detected_id if host_session_id is None
                                       else host_session_id))
    if state_dir is not None:
        session.save(state_dir)
        ensure_run(state_dir, task_doc=task_doc, now_ms=session.started_ms)
        append_history(state_dir, session)
        events.emit(state_dir, "phase.declared", phase=phase,
                    detail=f"name={name or '-'} host={session.host or '-'} "
                           f"session_id={session.host_session_id or '-'} "
                           f"budget={call_budget} declared={len(history(state_dir))}")
    return session


# -- the record: sessions.jsonl and run.json ---------------------------------

def _git(args, cwd) -> str:
    """stdout of a git query, or "" when git is absent, fails, or hangs."""
    try:
        proc = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True,
                              text=True, timeout=15)
    except (OSError, subprocess.SubprocessError):
        return ""
    if proc.returncode != 0:
        return ""
    return (proc.stdout or "").strip()


def skill_commit(repo_root=None) -> str:
    """`git rev-parse --short HEAD` of the checkout whose skill text runs.

    "" when git is not installed or the checkout is not a repository; a later
    report then says the commit is unrecorded rather than guessing one.
    """
    return _git(["rev-parse", "--short", "HEAD"], repo_root or REPO_ROOT)


def worktree_of(cwd=None) -> str:
    """The git toplevel of `cwd` (a worktree runs its own checkout), or ""."""
    return _git(["rev-parse", "--show-toplevel"], cwd or os.getcwd())


def _iso_utc(epoch_ms: int) -> str:
    return datetime.fromtimestamp(epoch_ms / 1000.0, timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


def workspace_of(state_dir) -> str:
    """The workspace a state dir belongs to: `<workspace>/results/state`.

    A state dir that is not laid out that way (a bare temp dir in a test) is
    its own workspace, so the run id is still derivable.
    """
    state = os.path.abspath(str(state_dir))
    parent = os.path.dirname(state)
    if (os.path.basename(state) == "state"
            and os.path.basename(parent) == "results"):
        return os.path.dirname(parent)
    return state


def history_path(state_dir) -> str:
    return os.path.join(str(state_dir), HISTORY_FILE)


def run_path(state_dir) -> str:
    return os.path.join(str(state_dir), RUN_FILE)


def history_record(session: Session, cwd=None, commit=None) -> dict:
    """The `sessions.jsonl` line for one declaration."""
    cwd = os.getcwd() if cwd is None else str(cwd)
    return {
        "ts": _iso_utc(session.started_ms),
        "ts_ms": session.started_ms,
        "phase": session.phase,
        "name": session.name,
        "host": session.host,
        "host_session_id": session.host_session_id,
        "cwd": cwd,
        "worktree": worktree_of(cwd),
        "skill_commit": skill_commit() if commit is None else commit,
        "pid": os.getpid(),
    }


def append_history(state_dir, session: Session, cwd=None) -> dict:
    """Append one declaration to `sessions.jsonl`; never rewrites a line."""
    os.makedirs(str(state_dir), exist_ok=True)
    record = history_record(session, cwd=cwd)
    with open(history_path(state_dir), "a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")
    return record


def history(state_dir) -> list:
    """Every declaration recorded for this workspace, oldest first.

    A torn or foreign line is skipped, not fatal: the file is appended by
    whichever session is running and may be read while one is.
    """
    records = []
    try:
        with open(history_path(state_dir), encoding="utf-8") as handle:
            lines = handle.read().splitlines()
    except OSError:
        return records
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except ValueError:
            continue
        if isinstance(record, dict) and record.get("phase") in PHASES:
            records.append(record)
    return records


def run_info(state_dir) -> Optional[dict]:
    """`run.json` as a dict, or None when this workspace has no run yet."""
    try:
        with open(run_path(state_dir), encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict) or not data.get("run_id"):
        return None
    return data


def ensure_run(state_dir, task_doc: str = "", now_ms: Optional[int] = None,
               workspace=None) -> dict:
    """Write `run.json` on the first declaration; return it unchanged after.

    `run_id` is `<workspace-name>-<created date>`, so a workspace copied for
    a second run — which starts with no `run.json`, `results/` being
    gitignored — gets a new one. Nothing here rewrites an existing file:
    the identity is fixed the moment the run starts.
    """
    existing = run_info(state_dir)
    if existing is not None:
        return existing
    now_ms = int(time.time() * 1000) if now_ms is None else now_ms
    workspace = workspace_of(state_dir) if workspace is None else os.path.abspath(str(workspace))
    created = _iso_utc(now_ms)
    info = {
        "run_id": f"{os.path.basename(workspace)}-{created[:10]}",
        "workspace": workspace,
        "created_ts": created,
        "created_ms": now_ms,
        "task_doc": task_doc or "",
    }
    os.makedirs(str(state_dir), exist_ok=True)
    with open(run_path(state_dir), "w", encoding="utf-8") as handle:
        json.dump(info, handle, indent=2, sort_keys=True)
    return info


def require(action: str, state_dir, default_phase: Optional[str] = None) -> None:
    """Gate `action` against the persisted session, for use by CLI entry points.

    When no session has been declared the action is **permitted** and the caller
    carries on. That is deliberate: the guard is being introduced into a repo
    whose existing scripts and workspaces predate it, and a guard that broke
    every current path on day one would be turned off rather than adopted. An
    undeclared session is unguarded, which is exactly the status quo; a declared
    one is enforced.
    """
    session = Session.load(state_dir) if state_dir else None
    if session is None:
        if default_phase is None:
            return
        session = Session(phase=default_phase)
    try:
        session.require(action)
    except PhaseViolation as exc:
        # A refusal is a pain point the report must see (spec, class 6): it
        # is recorded with the action, so a misrouted session is countable.
        events.emit(state_dir, "phase.refused", phase=session.phase,
                    verdict=f"FAIL: phase-boundary {action!r} refused in "
                            f"a {session.phase!r} session",
                    detail=f"action={action}: {exc}")
        raise
