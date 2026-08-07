"""Stage 1: solution type + design (EC#1 launch preamble, EC#11 explicit Modal).

Launches the workspace desktop (first stage), creates the project + design
with an explicit solution type, saves, records the pinned port/pid machine
state, and reports the Verification line.
"""

import os
import sys
import time

from ws_common import AEDT_VERSION, DESIGN, PROJECT, SOLUTION_TYPE, attach, write_state


def main() -> int:
    t0 = time.time()
    hfss = attach(launch=True)
    print("launch seconds = %.1f" % (time.time() - t0), flush=True)
    print("solution_type =", hfss.solution_type, flush=True)
    assert str(hfss.solution_type).lower() == SOLUTION_TYPE.lower(), (
        "solution type mismatch: got %s" % hfss.solution_type
    )
    hfss.save_project()
    print("project saved, exists =", os.path.exists(PROJECT), flush=True)
    assert os.path.exists(PROJECT), "project file missing on disk"
    write_state("validated", "False")
    print("PASS: solution_type %s design %s project saved" % (SOLUTION_TYPE, DESIGN), flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    sys.stdout.flush()
    os._exit(0)
