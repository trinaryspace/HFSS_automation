"""Diagnostic v2: filesystem-level tracking of a non-blocking solve + message manager."""

import glob
import os
import sys
import time

import psutil
from ansys.aedt.core import Hfss

PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects")
PROJECT = os.path.join(PROJECT_DIR, "smoke_solve.aedt")


def kill_new_aedt(start_time):
    for p in psutil.process_iter(["pid", "name", "create_time"]):
        try:
            if p.info["name"] == "ansysedt.exe" and p.info["create_time"] > start_time:
                p.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def sol_files():
    found = []
    for pat in ("*.asol", "*.mxwl", "*.ess"):
        found += glob.glob(os.path.join(PROJECT_DIR, "**", pat), recursive=True)
    return len(found)


def main() -> int:
    start_time = time.time()
    try:
        with Hfss(
            version="2024.1",
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design="solve_design",
            solution_type="Modal",
            remove_lock=True,
        ) as hfss:
            t0 = time.time()
            rv = hfss.analyze(setup="Setup1", blocking=False)
            print(f"analyze(blocking=False) -> {rv} after {time.time()-t0:.1f}s; sol_files={sol_files()}", flush=True)
            deadline = time.time() + 360
            data = None
            while time.time() < deadline:
                time.sleep(15)
                files = sol_files()
                try:
                    data = hfss.results.get_solution_data("S(1,1)")
                    break
                except Exception as e:
                    err = f"{type(e).__name__}: {str(e)[:120]}"
                print(f"t={time.time()-t0:.0f}s sol_files={files} data={data is not None} err={err}", flush=True)
            print("FINAL: sol_files =", sol_files(), "data =", data is not None, flush=True)
            msgs = hfss.desktop_class.odesktop.GetMessages(hfss.project_name, hfss.design_name, 2, False)
            print("GetMessages(level=2):", msgs, flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
