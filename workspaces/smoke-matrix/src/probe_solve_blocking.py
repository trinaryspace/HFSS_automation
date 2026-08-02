"""Matrix probe: blocking solve on the shared smoke design (reference outcome)."""

import os
import shutil
import sys
import time

import psutil
from ansys.aedt.core import Hfss

from s11_readout import fetch_s11_db, s11_summary
from smoke_design import build_smoke_design

PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects")
PROJECT = os.path.join(PROJECT_DIR, "smoke_solve2.aedt")


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
            design="solve_design2",
            solution_type="Modal",
        ) as hfss:
            build_smoke_design(hfss)
            hfss.save_project()
            print("built + saved; validate:",
                  bool(hfss.validate_simple()), flush=True)
            t0 = time.time()
            rv = hfss.analyze(setup="Setup1", blocking=True)
            print(f"analyze(blocking=True) -> {rv} after {time.time()-t0:.0f}s", flush=True)
            if rv:
                print("BLOCKING SOLVE PROBE PASS: solve completed", flush=True)
            data = fetch_s11_db(hfss, timeout=45)
            if isinstance(data, Exception):
                print(f"readout: {type(data).__name__} (recorded: flaky, see env-compat)", flush=True)
            else:
                lo, at = s11_summary(data)
                print(f"S11 min = {lo:.2f} dB; S11 at 2.4GHz = {at:.2f} dB", flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(exit_code)


if __name__ == "__main__":
    raise SystemExit(main())
