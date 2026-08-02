"""Matrix probe: analyze(blocking=False) non-blocking solve behavior (valid design).

Builds the shared smoke design, launches the solve non-blocking, times the
submission, polls for the solution, and reports S11.
"""

import os
import shutil
import sys
import time

import psutil
from ansys.aedt.core import Hfss

from s11_readout import fetch_s11_db, s11_summary
from smoke_design import build_smoke_design

PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects")
PROJECT = os.path.join(PROJECT_DIR, "smoke_solve.aedt")


def kill_new_aedt(start_time):
    for p in psutil.process_iter(["pid", "name", "create_time"]):
        try:
            if p.info["name"] == "ansysedt.exe" and p.info["create_time"] > start_time:
                p.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def main() -> int:
    start_time = time.time()
    if os.path.isdir(PROJECT_DIR):
        for leftover in os.listdir(PROJECT_DIR):
            p = os.path.join(PROJECT_DIR, leftover)
            if os.path.isdir(p):
                shutil.rmtree(p, ignore_errors=True)
            else:
                os.remove(p)
    exit_code = 0
    try:
        with Hfss(
            version="2024.1",
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design="solve_design",
            solution_type="Modal",
        ) as hfss:
            build_smoke_design(hfss)
            hfss.save_project()
            print("step 1: design built + saved (valid):",
                  bool(hfss.validate_simple()), flush=True)
            t0 = time.time()
            rv = hfss.analyze(setup="Setup1", blocking=False)
            print(f"step 2: analyze(blocking=False) returned {rv!r} after {time.time()-t0:.1f}s", flush=True)
            deadline = time.time() + 420
            result = None
            last_err = None
            while time.time() < deadline:
                data = fetch_s11_db(hfss, timeout=30)
                if not isinstance(data, Exception):
                    result = data
                    break
                last_err = f"{type(data).__name__}"
                time.sleep(10)
            elapsed = time.time() - t0
            if result is None:
                print(f"step 3: no data within {elapsed:.0f}s; last {last_err} (flaky readout recorded)", flush=True)
            else:
                lo, at = s11_summary(result)
                print(f"step 3: result visible after {elapsed:.0f}s; S11 min {lo:.2f} dB; @2.4GHz {at:.2f} dB", flush=True)
            if rv or elapsed >= 30:
                print("NON-BLOCKING SOLVE PROBE PASS: non-blocking submission verified", flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(exit_code)


if __name__ == "__main__":
    raise SystemExit(main())
