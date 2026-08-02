"""Matrix probe: RCS/SBR+ surface availability on AEDT 2024 R1.

Records whether the client surface exists and what calling it on a plain
Modal design does (expected per ADR 0004: unavailable on this backend).
"""

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


def main() -> int:
    start_time = time.time()
    print("Hfss.get_rcs_data present:", hasattr(Hfss, "get_rcs_data"), flush=True)
    try:
        from ansys.aedt.core.visualization.post.rcs_exporter import MonostaticRCSExporter

        print("MonostaticRCSExporter import: OK", flush=True)
    except Exception as e:
        print("MonostaticRCSExporter import: FAIL", type(e).__name__, str(e)[:120], flush=True)
        sys.stdout.flush()
        os._exit(0)
    try:
        with Hfss(
            version="2024.1",
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design="solve_design",
            solution_type="Modal",
            remove_lock=True,
            close_on_exit=True,
        ) as hfss:
            try:
                rv = hfss.get_rcs_data(frequencies=[2.4], setup="Setup1")
                print("get_rcs_data on Modal design ->", rv, flush=True)
            except Exception as e:
                print("get_rcs_data on Modal design:", type(e).__name__, str(e)[:160], flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
