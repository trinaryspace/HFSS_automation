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

A phase also carries a call budget. The count is advanced by whoever is driving
(`note_call`), and `over_budget` reports the breach; the default matches
SKILL.md's ~60-call escalation. Accounting here is honest about its limits: an
agent that never calls `note_call` is not accounted for, so the budget binds a
driver, not a conversation. It exists so that a driver — today the operator,
later ticket 14's runner — has one place to ask "is this session looping?"
rather than having to notice.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import asdict, dataclass, field
from typing import Optional

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

    @property
    def over_budget(self) -> bool:
        return self.call_budget > 0 and self.calls >= self.call_budget

    def budget_verdict(self) -> str:
        if not self.over_budget:
            return (f"ok: session phase={self.phase} calls={self.calls}/"
                    f"{self.call_budget}")
        return (f"ESCALATE: session phase={self.phase} calls={self.calls} has "
                f"reached its budget of {self.call_budget} without finishing. "
                f"A session this long is looping, not converging - report state "
                f"and hand the decision to the user.")


def start(phase: str, name: str = "", state_dir=None,
          call_budget: int = DEFAULT_CALL_BUDGET,
          host: Optional[str] = None,
          host_session_id: Optional[str] = None) -> Session:
    """Begin a phase session, persisting it when a state dir is given.

    `host` / `host_session_id` default to what `detect_host()` sees in the
    environment; pass them explicitly to override or to record an opencode
    slug by hand.
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
    return session


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
    session.require(action)
