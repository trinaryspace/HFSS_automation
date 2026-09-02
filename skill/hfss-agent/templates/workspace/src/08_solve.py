"""Stage 8: solve submission + detached watchdog launch (ADR 0006).

The solve launcher, shipped with the template since run logging ticket 02.
Every earlier workspace carried its own copy ("the template does not ship
it; the shape is patch-2400's delivered 08_solve.py"), and none of those
copies wrote the one boundary the run card and the run report need: the
instant the user-approved submission went to the solver. This file is that
shape — patch-array-5800's `src/08_solve.py`, behavior kept — plus the
boundary, and it is the single submission path for both Build routes (the
compiler never solves; `scripts/compile_spec.py` says so in its first line).

1. In-flight-solve probe: results-dir age + live solver processes. When a
   solve looks live the stage REFUSES to submit — the session asks the user
   and re-runs with `--approved` after their explicit go. It never submits
   over a live solve silently (double-solves cost an hour).
2. Attach to the pinned desktop (never a launch: a solve session attaches to
   the desktop the build left alive; a stale pin re-pins through `attach`).
3. Cleanup: stale solve results removed (skip-if-no-stale: with no real
   results the raw DeleteFullVariation surface errors — benign).
4. Submit: `analyze(setup=..., blocking=False)` — True is submission only,
   not completion (EC#5); never foreground-poll; never estimate. In the
   SAME call, `submit()` appends the epoch-seconds instant to
   `results/state/solve_submitted_at.txt` — the solve gate. A re-submission
   appends a second line: the run card uses the first line as the gate, the
   run report counts the lines as submissions. Nothing is appended when the
   submission is refused, or when `analyze` returns False.
5. Detach: launch poll_solve.py via subprocess.Popen(DETACHED_PROCESS |
   CREATE_NEW_PROCESS_GROUP). poll_solve writes
   results/state/solve_watchdog_pid.txt and solve_progress.txt itself.
6. End with the Verification line; the solve session then READS
   results/state/solve_progress.txt only.

The design solved is the one ws_common.DESIGN names — switch the constant
and re-run for a second design. Run:  python src/08_solve.py [--approved]
"""

import glob
import os
import subprocess
import sys
import time

import ws_common

SOLVE_SETUP = "Setup1"
# The solve gate: `results/state/solve_submitted_at.txt`, one epoch-seconds
# float per line, first line = the gate, line count = submissions.
SOLVE_GATE_STATE = "solve_submitted_at"
IN_FLIGHT_WINDOW_S = 300


def results_dir():
    return ws_common.PROJECT + "results"


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


def looks_live(age, procs):
    """The probe's verdict: results younger than the window is a live solve."""
    return age is not None and age < IN_FLIGHT_WINDOW_S


def cleanup_stale(hfss):
    """Remove stale solve results; skip when only asol skeletons exist."""
    d = results_dir()
    sds = glob.glob(os.path.join(d, "**", "*.sd"), recursive=True)
    big_asols = [p for p in glob.glob(os.path.join(d, "*.asol"))
                 if os.path.getsize(p) > 100 * 1024]
    if not (sds or big_asols):
        print("no stale solve results (asol skeletons only) — cleanup skipped", flush=True)
        return
    print("stale solve results found (%d .sd, %d big .asol) — cleaning" %
          (len(sds), len(big_asols)), flush=True)
    try:
        print("cleanup_solution:",
              hfss.cleanup_solution(entire_solution=True, field=True, mesh=True), flush=True)
    except Exception as exc:  # noqa: BLE001 - first-solve DeleteFullVariation is benign
        print("cleanup_solution raised (benign on first solve): %s: %s"
              % (type(exc).__name__, str(exc)[:200]), flush=True)


def submit(hfss, setup=SOLVE_SETUP, now=None):
    """Submit the solve and write the solve gate, in this one call.

    Returns the epoch-seconds instant that was appended to the gate file.
    Raises when `analyze` reports the submission failed — and then nothing
    is appended, so the gate never names a submission that did not happen.
    """
    t0 = time.time()
    rv = hfss.analyze(setup=setup, blocking=False)
    print("analyze(blocking=False) -> %s submission in %.1f s" % (rv, time.time() - t0),
          flush=True)
    if not rv:
        raise RuntimeError("analyze submission returned False")
    submitted = float(time.time() if now is None else now)
    ws_common.write_state("solve_started", str(submitted))
    ws_common.append_state(SOLVE_GATE_STATE, repr(submitted))
    return submitted


def launch_watchdog(popen=None):
    """Detach poll_solve.py on the pinned project; returns its pid."""
    popen = popen or subprocess.Popen
    poll = os.path.join(os.path.dirname(os.path.abspath(__file__)), "poll_solve.py")
    flags = getattr(subprocess, "DETACHED_PROCESS", 0x00000008) | \
        getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
    proc = popen(
        ["python", poll, ws_common.PROJECT],
        creationflags=flags,
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        cwd=os.path.dirname(poll),
    )
    return proc.pid


def main(argv=None, attach=None, probe=None, popen=None, now=None) -> int:
    """The stage; `attach` / `probe` / `popen` are injectable for tier-0 tests."""
    argv = sys.argv[1:] if argv is None else list(argv)
    approved = "--approved" in argv
    attach = attach or ws_common.attach
    probe = probe or in_flight_evidence

    age, procs = probe()
    print("pre-solve in-flight probe: results_age_s = %s, live ansysedt = %d" % (age, procs),
          flush=True)
    if looks_live(age, procs) and not approved:
        print(
            "FAIL: solve not submitted — results younger than %d s and %d solver "
            "process(es) live: a solve may be in flight. Ask the user; re-run "
            "`python src/08_solve.py --approved` after their explicit go."
            % (IN_FLIGHT_WINDOW_S, procs),
            flush=True,
        )
        return 2
    if approved:
        print("user approval recorded (--approved): submitting over the in-flight evidence",
              flush=True)

    hfss = attach(launch=False)
    cleanup_stale(hfss)
    submitted = submit(hfss, SOLVE_SETUP, now=now)
    pid = launch_watchdog(popen)
    print("watchdog launched detached pid:", pid, flush=True)
    print("PASS: solve submitted blocking=False setup=%s submitted_at=%r, "
          "watchdog detached (poll_solve.py)" % (SOLVE_SETUP, submitted), flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
