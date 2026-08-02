"""Ticket 01 probe: trivial graphical desktop launch against AEDT 2024 R1.

Launches a new graphical AEDT desktop, creates a throwaway HFSS design,
reports the backend version, and releases the desktop so no process is
left behind.
"""

import os
import sys
import time

import psutil
from ansys.aedt.core import Hfss


def main() -> int:
    print("step 1: import ansys.aedt.core OK")
    print("step 2: launching new graphical desktop (2024.1)...")
    with Hfss(
        version="2024.1",
        new_desktop=True,
        non_graphical=False,
        design="probe_design",
    ) as hfss:
        print("step 3: desktop version:", hfss.desktop_class.aedt_version)
        print("step 4: project:", hfss.project_name)
        print("step 5: design:", hfss.design_name)
        print("step 5b: solution type:", hfss.solution_type)
        print("step 6: throwaway design created OK")
    pid = hfss.desktop_class.aedt_process_id
    print("step 7: releasing desktop, closing AEDT (pid", pid, ")...")
    hfss.desktop_class.release_desktop(close_projects=True, close_on_exit=True)
    deadline = time.time() + 30
    while time.time() < deadline:
        if not psutil.pid_exists(pid):
            break
        try:
            proc = psutil.Process(pid)
            for child in proc.children(recursive=True):
                try:
                    child.kill()
                except psutil.NoSuchProcess:
                    pass
            proc.kill()
        except psutil.NoSuchProcess:
            break
        time.sleep(1)
    gone = not psutil.pid_exists(pid)
    print("step 8: AEDT process gone ->", gone)
    assert gone, "AEDT process did not exit after release + kill"
    print("PROBE PASS")
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
