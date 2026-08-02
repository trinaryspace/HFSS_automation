"""Micro-probe: find a working excitation-assignment form for 2024 R1 via gRPC."""

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
            hfss.modeler.create_box([0, 0, 0], [60, 50, 1.6], "substrate", "FR4_epoxy")
            hfss.modeler.create_box([-15, -15, -1], [90, 80, 1], "ground", "pec")
            hfss.modeler.create_box([10, 10, 1.6], [40, 30, 0.05], "patch", "pec")
            sheet = hfss.modeler.create_rectangle("YZ", [50, 10, 0], [30, 1.6], "port_sheet", "vacuum")
            face = sheet.faces[0]
            print("via id:", hfss.modeler.convert_to_selections(face.id, False), flush=True)
            print("via face obj:", hfss.modeler.convert_to_selections(face, False), flush=True)
            try:
                rv = hfss.wave_port(face, name="Port1", renormalize=True)
                print("wave_port(face obj) ->", rv.name if rv else None, flush=True)
            except Exception as e:
                print("wave_port(face obj) FAILED:", type(e).__name__, str(e)[:200], flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
