"""Matrix probe: launch a desktop and keep the server alive for attach.

Creates a project + design in a workspace location, releases the client
session WITHOUT closing AEDT, and prints the info an attaching session
would need. Pair with attach_reuse.py.
"""

import os
import sys

from ansys.aedt.core import Hfss

PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects")


def main() -> int:
    os.makedirs(PROJECT_DIR, exist_ok=True)
    print("step 1: launching new graphical desktop (2024.1)...", flush=True)
    with Hfss(
        version="2024.1",
        new_desktop=True,
        non_graphical=False,
        project=os.path.join(PROJECT_DIR, "smoke_attach.aedt"),
        design="attach_design",
        solution_type="Modal",
    ) as hfss:
        print("step 2: project:", hfss.project_name, flush=True)
        print("step 3: design:", hfss.design_name, flush=True)
        print("step 4: solution type:", hfss.solution_type, flush=True)
        hfss["probe_var"] = "1.5mm"
        print("step 5: variable probe_var=1.5mm set", flush=True)
        hfss.save_project()
        print("step 6: project saved to workspace", flush=True)
        pid = hfss.desktop_class.aedt_process_id
    print("step 7: releasing client WITHOUT closing AEDT (pid", pid, ")", flush=True)
    hfss.desktop_class.release_desktop(close_projects=False, close_on_exit=False)
    print("LAUNCH-KEEP DONE: aedt pid left alive:", pid, flush=True)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
