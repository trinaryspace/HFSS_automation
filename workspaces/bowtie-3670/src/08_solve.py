"""Stage 11 (ver.2): solve — background analyze + poll on results-on-disk growth.

Run #1 failed: my poll globbed *.sd non-recursively (sweep files live in the
<design>.results/ subfolder), and a stray second desktop had opened the same
project, so two sessions collided writing one results dir (stall at 11/201).
Fix: cleanup_solution() first, recursive glob, single port-pinned desktop.
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
    asols = glob.glob(os.path.join(d, "**", "*.asol"), recursive=True)
    sds = glob.glob(os.path.join(d, "**", "*.sd"), recursive=True)
    total = sum(os.path.getsize(p) for p in asols + sds)
    return len(asols), len(sds), total


def main() -> int:
    sweeps = (read_state("sweeps") or "").split(",")
    assert sweeps, "no sweep recorded; run 06 first"
    hfss = attach(launch=False)
    print("pre-solve disk: asol/sd/total =", snapshot(), flush=True)
    hfss.cleanup_solution(entire_solution=True)
    print("after cleanup: asol/sd/total =", snapshot(), flush=True)
    t0 = time.time()
    rv = hfss.analyze(setup="Setup1", blocking=False)
    print("analyze(blocking=False) ->", rv, "submission", round(time.time() - t0, 1), "s", flush=True)
    if not rv:
        print("STAGE_FAILED analyze submission returned False", flush=True)
        return 1
    write_state("solve_started", str(time.time()))
    deadline = time.time() + 45 * 60
    last = snapshot()
    while time.time() < deadline:
        time.sleep(20)
        cur = snapshot()
        if cur != last:
            print("  disk:", cur, flush=True)
            last = cur
        a, s, _ = cur
        if a >= 1 and s >= 200:  # 1 adaptive asol + >=200 of 201 sweep freq files
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
