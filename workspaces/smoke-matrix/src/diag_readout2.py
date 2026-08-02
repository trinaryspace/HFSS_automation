"""Diagnostic: verbose per-attempt shape of post.get_solution_data after solve."""

import os
import sys
import time

import psutil
from ansys.aedt.core import Hfss

PROJECT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "projects", "smoke_solve2.aedt"
)


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
            for i in range(6):
                try:
                    data = hfss.post.get_solution_data(expressions="dB(S(1,1))")
                    print(f"t={i}: type={type(data).__name__} str={str(data)[:80]!r}", flush=True)
                    if data is not None and not isinstance(data, bool):
                        print(f"   attrs: data_real={hasattr(data,'data_real')} "
                              f"primary_sweep={hasattr(data,'primary_sweep_values')} "
                              f"real={data.data_real() if hasattr(data,'data_real') else None}", flush=True)
                except Exception as e:
                    print(f"t={i}: EXC {type(e).__name__}: {str(e)[:120]}", flush=True)
                time.sleep(8)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
