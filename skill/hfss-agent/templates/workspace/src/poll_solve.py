"""Detached solve watchdog (ADR 0006) — no LLM babysits the solve.

`08_solve.py` submits `analyze(..., blocking=False)` and launches THIS
script detached (`Start-Process python src/poll_solve.py <project>.aedt`),
then exits. The watchdog scans `<project>.aedtresults/` recursively every
~20 s, appends one line to `results/state/solve_progress.txt` per tick,
and exits when the solve completes or stalls. The agent does nothing but
read `solve_progress.txt`; it never foreground-polls.

Exit semantics (mirrored in the last progress line):
  status: complete  -> exit 0   (completion criteria met)
  status: stalled   -> exit 2   (growth stopped before completion)

Completion/stall rules (see `watchdog_tick`):
  - with EXPECTED_SD set (08_solve passes the sweep point count):
    complete when sd count >= expected and unchanged for SETTLE_TICKS;
  - without: complete when the results tree has grown at all and then
    stayed unchanged for SETTLE_TICKS;
  - stalled: grown at least once, then unchanged for STALL_TICKS
    (a sweep plateau is a stall signal — escalate, never claim done);
  - never grew at all within START_TICKS: stalled (submit never picked up).

This module imports nothing from pyAEDT and no other workspace module, so
it runs in any Python and can never attach to or kill a desktop. On
startup it guarantees the `aedt_port.txt` / `aedt_process_id.txt` files
exist (filling "0" only if the launching session left none — it never
overwrites live values) and records its own pid in
`solve_watchdog_pid.txt` (the pid `08_solve`'s detach step records).
"""

import os
import sys
import time

SLEEP_SECONDS = 20
SETTLE_TICKS = 3          # unchanged ticks after growth => complete
STALL_TICKS = 30          # unchanged ticks after growth => stalled (10 min)
START_TICKS = 30          # no growth from the start within this => stalled

STATUS_RUNNING = "running"
STATUS_SETTLING = "settling"
STATUS_COMPLETE = "complete"
STATUS_STALLED = "stalled"


def project_results_dir(project_path):
    """AEDT results folder for a project: `<project>.aedtresults`."""
    return project_path + "results"


def scan_results(root):
    """Count recursive `.asol`/`.sd` growth under an `.aedtresults` tree.

    Returns (n_asol, n_sd, n_files, bytes_total): entries whose name ends
    in `.asol` or `.sd` (both directories and files), the total number of
    regular files, and their summed size. A single os.walk — no recursive
    listings land in the agent's context.
    """
    if not os.path.isdir(root):
        return (0, 0, 0, 0)
    n_asol = n_sd = n_files = 0
    bytes_total = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for name in dirnames:
            if name.endswith(".asol"):
                n_asol += 1
            elif name.endswith(".sd"):
                n_sd += 1
        for name in filenames:
            n_files += 1
            try:
                bytes_total += os.path.getsize(os.path.join(dirpath, name))
            except OSError:
                pass
    return (n_asol, n_sd, n_files, bytes_total)


def watchdog_tick(prev, cur, state, cfg):
    """One 20 s decision step; pure.

    `state` is the mutable dict carried between ticks. `cfg` may override
    SETTLE_TICKS/STALL_TICKS/START_TICKS and hold `expected_sd`.
    Returns (status, state). Statuses: running | settling | complete |
    stalled. 'settling' means it has grown and is on the completion count;
    a plateau re-grow flips it back to running.
    """
    settle = cfg.get("settle_ticks", SETTLE_TICKS)
    stall = cfg.get("stall_ticks", STALL_TICKS)
    start = cfg.get("start_ticks", START_TICKS)
    expected_sd = cfg.get("expected_sd")
    changed = (prev is None or cur[0] != prev[0] or cur[1] != prev[1]
               or cur[2] != prev[2] or cur[3] != prev[3])
    if changed:
        state["unchanged"] = 0
        if prev is not None or cur[0] + cur[1] + cur[3] > 0:
            state["grown"] = True
    else:
        state["unchanged"] += 1
    if not state.get("grown") and state["unchanged"] >= start:
        return STATUS_STALLED, state
    if expected_sd is not None:
        done = cur[1] >= expected_sd and state.get("grown")
    else:
        done = state.get("grown")
    if done and state["unchanged"] >= settle:
        return STATUS_COMPLETE, state
    if state.get("grown") and state["unchanged"] >= stall:
        return STATUS_STALLED, state
    if done:
        return STATUS_SETTLING, state
    return STATUS_RUNNING, state


def format_progress(tick_no, status, metrics, state, cfg, elapsed_s, started_at):
    """One `solve_progress.txt` line — the agent's only solve signal."""
    expected = cfg.get("expected_sd") if cfg.get("expected_sd") is not None else "-"
    parts = [
        "tick=%d" % tick_no,
        "status=%s" % status,
        "elapsed_s=%d" % int(elapsed_s),
        "asol=%d" % metrics[0],
        "sd=%d" % metrics[1],
        "files=%d" % metrics[2],
        "bytes=%d" % metrics[3],
        "unchanged_ticks=%d" % state.get("unchanged", 0),
        "expected_sd=%s" % expected,
        "watchdog_started=%d" % int(started_at),
    ]
    return " ".join(parts)


def resolve_project(argv=None):
    """The `.aedt` project path: argv[1] > SOLVE_PROJECT env > one in parent dir."""
    argv = argv or sys.argv
    if len(argv) > 1:
        return os.path.abspath(argv[1])
    env = os.environ.get("SOLVE_PROJECT")
    if env:
        return os.path.abspath(env)
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    matches = [os.path.join(parent, f) for f in os.listdir(parent)
               if f.endswith(".aedt") and not f.endswith(".aedt.lock")]
    if len(matches) == 1:
        return matches[0]
    return None


def main(argv=None):
    argv = argv if argv is not None else sys.argv
    project = resolve_project(argv)
    if not project:
        print("watchdog aborted: no project path (pass <project>.aedt or set SOLVE_PROJECT)", flush=True)
        return 3
    workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    state_dir = os.path.join(workspace, "results", "state")
    os.makedirs(state_dir, exist_ok=True)
    progress = os.path.join(state_dir, "solve_progress.txt")

    # State-file writebacks (ADR 0006): the watchdog's startup guarantees
    # the pinned-port/pid records EXIST for the solve session's attach and
    # teardown (08_solve wrote their live values before launching it; the
    # watchdog only fills in "0" if they are missing) and records its own
    # pid in solve_watchdog_pid.txt for whoever launched it.
    with open(os.path.join(state_dir, "solve_watchdog_pid.txt"), "w") as f:
        f.write(str(os.getpid()))
    for key in ("aedt_port", "aedt_process_id"):
        path = os.path.join(state_dir, key + ".txt")
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("0")

    expected_sd = None
    try:
        expected_sd = int(os.environ.get("EXPECTED_SD", "") or 0) or None
    except ValueError:
        expected_sd = None
    cfg = {"expected_sd": expected_sd}

    started = time.time()
    prev = None
    state = {"grown": False, "unchanged": 0}
    tick_no = 0
    status = STATUS_RUNNING
    while True:
        cur = scan_results(project_results_dir(project))
        status, state = watchdog_tick(prev, cur, state, cfg)
        line = format_progress(tick_no, status, cur, state, cfg, time.time() - started, started)
        with open(progress, "a") as f:
            f.write(line + "\n")
        print(line, flush=True)
        if status in (STATUS_COMPLETE, STATUS_STALLED):
            print("watchdog exit:", status, flush=True)
            return 0 if status == STATUS_COMPLETE else 2
        prev = cur
        tick_no += 1
        time.sleep(SLEEP_SECONDS)


if __name__ == "__main__":
    raise SystemExit(main())
