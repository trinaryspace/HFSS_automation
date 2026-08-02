"""Diagnostic v2: bisect validation failure; retry port with explicit integration line."""

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
            print("v0 (current):", bool(hfss.validate_simple()), flush=True)
            for b in list(hfss.boundaries):
                b.delete()
            print("after del boundaries:", bool(hfss.validate_simple()), flush=True)
            sheet = hfss.modeler.objects_by_name["port_sheet"]
            vertical = [e for e in sheet.edges if abs(e.vertices[0].position[2] - e.vertices[1].position[2]) > 0.1][0]
            hfss.wave_port(sheet.faces[0], integration_line=vertical, impedance=50, name="Port1", renormalize=True)
            print("after port w/ explicit int line:", bool(hfss.validate_simple()), flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
