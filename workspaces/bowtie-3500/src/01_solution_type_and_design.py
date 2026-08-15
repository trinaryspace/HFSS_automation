"""Stage 2+3: solution type (explicit Modal — never the default, EC#11) and design.

Launches the desktop (new_desktop=True — EC#1), creates the project + design
with an explicit solution type, saves, and reports both completion signals.
"""

import os
import sys
import time

from ws_common import AEDT_VERSION, DESIGN, PROJECT, SOLUTION_TYPE, write_state

PDIR = os.path.dirname(PROJECT)
os.makedirs(PDIR, exist_ok=True)

start_time = time.time()
try:
    from ansys.aedt.core import Hfss

    hfss = Hfss(
        version=AEDT_VERSION,
        new_desktop=True,
        non_graphical=False,
        project=PROJECT,
        design=DESIGN,
        solution_type=SOLUTION_TYPE,
        remove_lock=True,
    )
    print("launched; aedt_process_id =", getattr(hfss.desktop_class, "aedt_process_id", None), flush=True)
    write_state("aedt_port", str(getattr(hfss.desktop_class, "port", 0)))
    write_state("aedt_process_id", str(getattr(hfss.desktop_class, "aedt_process_id", 0)))
    print("solution_type =", hfss.solution_type, flush=True)
    assert str(hfss.solution_type).lower() == SOLUTION_TYPE.lower(), "solution type mismatch"
    hfss.save_project()
    print("project saved:", PROJECT, "exists =", os.path.exists(PROJECT), flush=True)
    assert os.path.exists(PROJECT), "project file missing on disk"
    print("STAGE_OK solution_type=Modal design_created", flush=True)
except Exception as e:
    print("STAGE_FAILED", type(e).__name__, str(e)[:500], flush=True)
sys.stdout.flush()
os._exit(0)
