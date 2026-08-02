"""Diagnostic: find the report context shape that returns S11 from a solved project."""

import os
import sys
import time

import psutil
from ansys.aedt.core import Hfss

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
    try:
        with Hfss(
            version="2024.1",
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design="solve_design2",
            solution_type="Modal",
            remove_lock=True,
        ) as hfss:
            print("sweeps:", hfss.existing_analysis_sweeps, flush=True)
            variants = [
                ("no ctx", {}),
                ("LastAdaptive", {"setup_sweep_name": "Setup1 : LastAdaptive"}),
                ("Sweep", {"setup_sweep_name": "Setup1 : Sweep"}),
                ("Sweep+domain", {"setup_sweep_name": "Setup1 : Sweep", "domain": "Sweep"}),
            ]
            for label, kwargs in variants:
                try:
                    data = hfss.post.get_solution_data(expressions="dB(S(1,1))", **kwargs)
                    ok = data is not None and not isinstance(data, bool)
                    print(f"{label}: got={type(data).__name__} valid={ok}", flush=True)
                    if ok and hasattr(data, "data_real"):
                        print("   S11 min =", round(min(data.data_real()), 2), "dB", flush=True)
                except Exception as e:
                    print(f"{label}: EXC {type(e).__name__}: {str(e)[:150]}", flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
