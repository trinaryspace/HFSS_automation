"""The workspace's one hook into the repo's event log (run logging, ticket 03).

Every template runner that prints a `PASS:` / `FAIL:` line, attaches to a
desktop, submits the solve, sees the watchdog's terminal line, banks or tears
down also appends that fact to `results/state/events.jsonl` through this
module. The log itself lives in `hfss_spec/events.py`, in the checkout whose
skill text runs; this file only finds it and forwards.

Finding it follows the pattern the other runners already use for the repo
(`test_poll_solve_stages` walks up to `workspaces/bowtie-3500-pilot`;
`verify_spec_replay` reaches `../../scripts` from the workspace): walk up
from this file's directory until a `hfss_spec/events.py` appears. That works
from `<repo>/workspaces/<name>/src/` and from a sync-verify copy nested under
`results/state/verify/<stamp>/copy/src/` alike. The module is loaded by file
path, not by package import, so nothing here imports `hfss_spec` — and so a
watchdog that must import nothing from pyAEDT still imports nothing that
could. Stdlib only.

Everything degrades to a silent no-op: no repo above this workspace, an
unreadable module, a state dir that does not exist yet. A runner's verdict
is never decided by its log line, and `emit()` never raises.

    import run_events
    run_events.emit("solve.submitted", stage="solve", verdict=line)
"""

import importlib.util
import os
import sys

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(WORKSPACE, "results", "state")

EVENTS_RELPATH = os.path.join("hfss_spec", "events.py")
MAX_UP = 12         # levels to climb before giving up — a copy nests ~6 deep

_module = None      # the loaded events module, or False once lookup failed


def repo_root(start=None):
    """The nearest ancestor of `start` holding `hfss_spec/events.py`, or None."""
    here = os.path.abspath(start or os.path.dirname(os.path.abspath(__file__)))
    for _ in range(MAX_UP):
        if os.path.isfile(os.path.join(here, EVENTS_RELPATH)):
            return here
        parent = os.path.dirname(here)
        if parent == here:
            break
        here = parent
    return None


def events_module(start=None):
    """`hfss_spec.events`, loaded by file from the checkout above us; None if absent."""
    global _module
    if _module is not None:
        return _module or None
    try:
        root = repo_root(start)
        if root is None:
            _module = False
            return None
        path = os.path.join(root, EVENTS_RELPATH)
        spec = importlib.util.spec_from_file_location("_hfss_run_events", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _module = module
        return module
    except Exception:       # noqa: BLE001 - a missing logger is not a failure
        _module = False
        return None


def reset():
    """Forget the resolved module (tests that move the repo root call this)."""
    global _module
    _module = None


def emit(event, *, stage=None, verdict=None, detail="", duration_ms=None,
         phase=None, state_dir=None):
    """Append one event to `<state_dir>/events.jsonl`; True when it landed.

    `state_dir` defaults to this workspace's `results/state`; runners that
    redirect their state (ws_common.STATE) pass it explicitly. Never raises.
    """
    try:
        module = events_module()
        if module is None:
            return False
        return bool(module.emit(state_dir or STATE, event, phase=phase,
                                stage=stage, verdict=verdict, detail=detail,
                                duration_ms=duration_ms))
    except Exception:       # noqa: BLE001 - never fail a stage for its log line
        return False


def read(state_dir=None):
    """The recorded events, oldest first (empty when none or no logger)."""
    try:
        module = events_module()
        if module is None:
            return []
        return module.read(state_dir or STATE)
    except Exception:       # noqa: BLE001
        return []


def names(state_dir=None):
    return [record.get("event") for record in read(state_dir)]


if __name__ == "__main__":
    root = repo_root()
    print("PASS: run_events repo_root=%s state=%s logger=%s"
          % (root or "-", STATE, "found" if events_module() else "absent"))
