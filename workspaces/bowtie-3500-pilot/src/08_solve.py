"""Stage 8: solve submission + detached watchdog launch (ADR 0006).

1. Cleanup: stale solve results removed (cleanup_solution only when real
   results exist — asol skeletons are not solve results; the raw
   DeleteFullVariation surface errors on a first-ever solve, benign).
2. In-flight-solve probe: if a solver run looks live (results-dir age +
   ansysedt.exe processes), print a WARNING line — the 08_solve flow asks
   the user before submitting (the asking happens in the solve session when
   the probe fires; this stage is a no-op guard).
3. Submit: analyze(setup="Setup1", blocking=False) — True is submission
   only, not completion (EC#5).
4. Detach: launch poll_solve.py via subprocess.Popen(DETACHED_PROCESS |
   CREATE_NEW_PROCESS_GROUP) — the deterministic detached launch
   (Perf-refactor pilot fix; the PowerShell Start-Process quoting broke
   twice). poll_solve writes results/state/solve_watchdog_pid.txt itself.
5. End with the Verification line; the solve session then READS
   results/state/solve_progress.txt only.
"""

import glob
import os
import subprocess
import sys
import time

from ws_common import PROJECT, attach, exit_keep_alive, write_state

SOLVE_SETUP = "Setup1"


def results_dir():
    return PROJECT + "results"


def in_flight_evidence():
    """(age_seconds | None, live_ansysedt_count) — None age when no results."""
    d = results_dir()
    if not os.path.isdir(d):
        return None, 0
    asols = glob.glob(os.path.join(d, "*.asol"))
    sds = glob.glob(os.path.join(d, "*.sd"))
    if not asols and not sds:
        return None, 0
    import psutil

    procs = [p for p in psutil.process_iter(["name"]) if p.info["name"] == "ansysedt.exe"]
    newest = max(os.path.getmtime(p) for p in asols + sds)
    return int(time.time() - newest), len(procs)


def main() -> int:
    age, procs = in_flight_evidence()
    print("pre-solve in-flight probe: results_age_s = %s, live ansysedt = %d" % (age, procs), flush=True)
    if age is not None and age < 300:
        print(
            "WARNING: results younger than 5 min and %d solver process(es) live — "
            "a solve may be in flight; the session must ask the user before submitting" % procs,
            flush=True,
        )

    hfss = attach(launch=False)

    # Cleanup: only meaningful when stale SOLVE results exist. The asol
    # skeletons AEDT writes at build time (few KB) are NOT solve results —
    # delete-then-create never mistakes them for one (the real signal:
    # per-frequency .sd sweep files, or a solved .asol in MBs). With no
    # real results the raw DeleteFullVariation surface errors (benign).
    d = results_dir()
    sds = glob.glob(os.path.join(d, "**", "*.sd"), recursive=True)
    big_asols = [p for p in glob.glob(os.path.join(d, "*.asol"))
                 if os.path.getsize(p) > 100 * 1024]
    stale = sds or big_asols
    if stale:
        print("stale solve results found (%d .sd, %d big .asol) — cleaning" %
              (len(sds), len(big_asols)), flush=True)
        print("cleanup_solution:", hfss.cleanup_solution(entire_solution=True, field=True, mesh=True), flush=True)
    else:
        print("no stale solve results (asol skeletons only) — cleanup skipped", flush=True)

    t0 = time.time()
    rv = hfss.analyze(setup=SOLVE_SETUP, blocking=False)
    print("analyze(blocking=False) -> %s submission in %.1f s" % (rv, time.time() - t0), flush=True)
    assert rv, "analyze submission returned False"
    write_state("solve_started", str(time.time()))

    # Detach the watchdog (ADR 0006): a hidden, fully detached python
    # process — no PowerShell quoting to break. It writes its own state
    # files (solve_watchdog_pid.txt) and exits on completion/stall.
    poll = os.path.join(os.path.dirname(os.path.abspath(__file__)), "poll_solve.py")
    flags = getattr(subprocess, "DETACHED_PROCESS", 0x00000008) | \
        getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
    proc = subprocess.Popen(
        ["python", poll, PROJECT],
        creationflags=flags,
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        cwd=os.path.dirname(poll),
    )
    print("watchdog launched detached pid:", proc.pid, flush=True)
    print("PASS: solve submitted blocking=False, watchdog detached (poll_solve.py)", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
