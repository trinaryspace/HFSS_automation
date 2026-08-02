"""Matrix probe: attach onto the running desktop (cross-process).

Must run AFTER launch_keep.py (which left an AEDT server alive).
Discovers the running session, opens the saved project, verifies the
design and the variable written by the launching session, then closes.
"""

import os
import sys
import time

from ansys.aedt.core import Desktop

PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects")


def main() -> int:
    print("step A: attaching (new_desktop=False)...", flush=True)
    d = Desktop(version="2024.1", new_desktop=False, non_graphical=False)
    print("step B: attached; version", d.aedt_version, flush=True)
    proj = os.path.join(PROJECT_DIR, "smoke_attach.aedt")
    print("step C: opening saved project...", flush=True)
    d.load_project(proj)
    print("step D: project loaded:", d.active_project_name, flush=True)
    d = None
    from ansys.aedt.core import Hfss

    hfss = Hfss(project=proj, design="attach_design", solution_type="Modal", new_desktop=False)
    print("step E: attached design:", hfss.design_name, flush=True)
    print("step F: solution type:", hfss.solution_type, flush=True)
    print("step G: probe_var value:", hfss["probe_var"], flush=True)
    assert hfss["probe_var"] == "1.5mm", "variable written by launcher not visible on attach"
    print("ATTACH REUSE PASS", flush=True)
    hfss.desktop_class.release_desktop(close_projects=True, close_on_exit=True)
    sys.stdout.flush()
    time.sleep(1)
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
