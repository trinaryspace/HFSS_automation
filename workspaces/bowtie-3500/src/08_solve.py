"""Stage 11: solve — background analyze + poll on results-on-disk growth.

analyze(blocking=False) returns submission-only (EC#5); completion is
signalled by .asol / per-frequency .sd files appearing in the
project results folder. Never estimate time — poll only.
"""

import glob
import os
import sys
import time

from ws_common import PROJECT, attach, exit_keep_alive, read_state, write_state


def results_dir():
    return PROJECT + "results"


def snapshot():
    d = results_dir()
    if not os.path.isdir(d):
        return 0, 0, []
    asols = glob.glob(os.path.join(d, "*.asol"))
    sds = glob.glob(os.path.join(d, "*.sd"))
    total = sum(os.path.getsize(p) for p in asols + sds)
    return len(asols), len(sds), total


def main() -> int:
    sweeps = (read_state("sweeps") or "").split(",")
    assert sweeps, "no sweep recorded; run 06 first"
    hfss = attach(launch=False)
    print("pre-solve disk: asol/sd/total =", snapshot(), flush=True)
    t0 = time.time()
    rv = hfss.analyze(setup="Setup1", blocking=False)
    print("analyze(blocking=False) ->", rv, "submission", time.time() - t0, "s", flush=True)
    if not rv:
        print("STAGE_FAILED analyze submission returned False", flush=True)
        return 1
    write_state("solve_started", str(time.time()))
    # poll: results-on-disk growth; cap total wait at 45 min
    deadline = time.time() + 45 * 60
    last = snapshot()
    while time.time() < deadline:
        time.sleep(20)
        cur = snapshot()
        changed = cur != last
        if changed:
            print("  disk:", cur, "delta vs", last, flush=True)
            last = cur
        a, s, _ = cur
        if a >= 1 and s >= 195:  # 1 adaptive asol + >=195 of 201 sweep freq files
            print("SOLVE_COMPLETE asol={} sd={} after {:.0f}s".format(a, s, time.time() - t0), flush=True)
            write_state("solve_done", str(time.time()))
            print("STAGE_OK solve complete (disk signal)", flush=True)
            return 0
    print("STAGE_FAILED solve timeout; last disk:", last, flush=True)
    return 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
