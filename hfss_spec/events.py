"""The event log: every stage boundary and verdict, machine-written (ticket 03).

`results/state/events.jsonl` is the second of the run report's three inputs
(`.scratch/hfss-agent-run-logging/spec.md`). The harness stores already hold
every step; what they cannot know is where a Spine stage started and ended,
which `PASS:` line closed it, which desktop a script attached to, and when
the solve went to the solver. Those facts are known in exactly one place —
the repo's own scripts, at the instant they happen — so those scripts append
them here. One JSON object per line:

    {ts, ts_ms, run_id, phase, stage, event, verdict, detail, duration_ms,
     pid, argv0}

- `verdict` is the exact `PASS:` / `FAIL:` line the runner already prints,
  so nothing is worded twice and the ledger, the Verification line and the
  event never disagree.
- `detail` is ONE line, never a dump. The watchdog's tick log stays in
  `solve_progress.txt`; only its terminal line becomes an event.
- `run_id` comes from `run.json` (ticket 01); `null` before the first phase
  declaration. `phase` defaults to the current `session.json` phase.

Three rules `emit()` keeps, because a logger that can fail a stage is worse
than no logger:

1. **It never raises.** Any failure — an unwritable file, a value that will
   not serialise, a torn `run.json` — returns False and costs the caller
   nothing. A stage's outcome is decided by the stage, never by its log line.
2. **It is a no-op when the state dir does not exist.** The tooling runs
   against throwaway trees, template copies and offline gates that have no
   workspace; none of those should grow a `results/state/`.
3. **It is cheap.** Two small JSON reads and one append; no imports beyond
   the stdlib. This module deliberately imports nothing else from
   `hfss_spec` so the workspace template's `run_events.py` can load it by
   file path without dragging the package (and Pydantic) into a watchdog.
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from typing import Optional

EVENTS_FILE = "events.jsonl"
RUN_FILE = "run.json"           # hfss_spec.session.RUN_FILE, restated (rule 3)
SESSION_FILE = "session.json"   # hfss_spec.session.STATE_FILE, restated

# The record's keys, in the order they are written.
FIELDS = ("ts", "ts_ms", "run_id", "phase", "stage", "event", "verdict",
          "detail", "duration_ms", "pid", "argv0")

# A detail or verdict is one line; anything longer is a dump by definition.
MAX_LINE = 1000


def events_path(state_dir) -> str:
    return os.path.join(str(state_dir), EVENTS_FILE)


def one_line(text, limit: int = MAX_LINE) -> str:
    """The first line of `text`, stripped and capped — never a dump."""
    if text is None:
        return ""
    text = str(text)
    first = text.strip().splitlines()[0].strip() if text.strip() else ""
    if len(first) > limit:
        first = first[: limit - 1] + "…"
    return first


def _iso_utc(epoch_ms: int) -> str:
    stamp = datetime.fromtimestamp(epoch_ms / 1000.0, timezone.utc)
    return stamp.strftime("%Y-%m-%dT%H:%M:%S.") + "%03dZ" % (epoch_ms % 1000)


def _json_file(path) -> Optional[dict]:
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def run_id_of(state_dir) -> Optional[str]:
    """`run.json`'s `run_id`, or None when the run has not been declared."""
    data = _json_file(os.path.join(str(state_dir), RUN_FILE))
    if not data:
        return None
    value = data.get("run_id")
    return str(value) if value else None


def phase_of(state_dir) -> Optional[str]:
    """The current `session.json` phase, or None when nothing is declared."""
    data = _json_file(os.path.join(str(state_dir), SESSION_FILE))
    if not data:
        return None
    value = data.get("phase")
    return str(value) if value else None


def record(state_dir, event, *, phase=None, stage=None, verdict=None,
           detail="", duration_ms=None, now_ms=None) -> dict:
    """The record `emit()` would append, as a dict. May raise; `emit` may not."""
    now_ms = int(time.time() * 1000) if now_ms is None else int(now_ms)
    argv0 = os.path.basename(sys.argv[0]) if sys.argv and sys.argv[0] else ""
    return {
        "ts": _iso_utc(now_ms),
        "ts_ms": now_ms,
        "run_id": run_id_of(state_dir),
        "phase": phase if phase is not None else phase_of(state_dir),
        "stage": None if stage is None else str(stage),
        "event": str(event),
        "verdict": None if verdict is None else one_line(verdict),
        "detail": one_line(detail),
        "duration_ms": None if duration_ms is None else int(duration_ms),
        "pid": os.getpid(),
        "argv0": argv0,
    }


def emit(state_dir, event, *, phase=None, stage=None, verdict=None,
         detail="", duration_ms=None) -> bool:
    """Append one event line. True when a line landed; never raises.

    No-op (False) when `state_dir` is not an existing directory — nothing
    here ever creates a workspace's state dir.
    """
    try:
        if not state_dir or not os.path.isdir(str(state_dir)):
            return False
        line = json.dumps(record(state_dir, event, phase=phase, stage=stage,
                                 verdict=verdict, detail=detail,
                                 duration_ms=duration_ms),
                          sort_keys=False, default=str)
        with open(events_path(state_dir), "a", encoding="utf-8") as handle:
            handle.write(line + "\n")
        return True
    except Exception:       # noqa: BLE001 - rule 1: a log line never fails a stage
        return False


def read(state_dir) -> list:
    """Every event recorded, oldest first; a torn or foreign line is skipped."""
    records = []
    try:
        with open(events_path(state_dir), encoding="utf-8") as handle:
            lines = handle.read().splitlines()
    except OSError:
        return records
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except ValueError:
            continue
        if isinstance(data, dict) and data.get("event"):
            records.append(data)
    return records


def names(state_dir) -> list:
    """Just the event names, in order — the shape most assertions want."""
    return [r["event"] for r in read(state_dir)]
