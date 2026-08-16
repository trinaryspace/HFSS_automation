"""Stage 1: solution type (explicit Modal — never the default, EC#11) + design.

Launches the desktop (new_desktop=True, EC#1) through the port-pinned
ws_common preamble, creates the project + design with the Recipe's explicit
solution type, saves, and ends with its Verification line. The desktop stays
alive for the next stage (exit_keep_alive).
"""

import os
import sys
import time

from ws_common import AEDT_VERSION, DESIGN, PROJECT, SOLUTION_TYPE, attach, exit_keep_alive, write_state


def main() -> int:
    t0 = time.time()
    hfss = attach(launch=True)
    print("launched; port =", hfss.desktop_class.port,
          "aedt_process_id =", getattr(hfss.desktop_class, "aedt_process_id", None), flush=True)
    write_state("aedt_port", str(getattr(hfss.desktop_class, "port", 0)))
    write_state("aedt_process_id", str(getattr(hfss.desktop_class, "aedt_process_id", 0)))
    print("solution_type =", hfss.solution_type, flush=True)
    assert str(hfss.solution_type).lower() == SOLUTION_TYPE.lower(), "solution type mismatch"
    hfss.save_project()
    print("project saved:", PROJECT, "exists =", os.path.exists(PROJECT), flush=True)
    assert os.path.exists(PROJECT), "project file missing on disk"
    print("PASS: solution_type Modal, design Patch2400, project saved (launch %.1f s, port %s)"
          % (time.time() - t0, hfss.desktop_class.port), flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
