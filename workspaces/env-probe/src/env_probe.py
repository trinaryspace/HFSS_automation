"""Ticket 01 probe: trivial graphical desktop launch against AEDT 2024 R1.

Launches a new graphical AEDT desktop, creates a throwaway HFSS design,
reports the backend version, and releases the desktop so no process is
left behind.
"""

import os
import sys
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
        print("step 3: desktop version:", hfss.aedt_version)
        print("step 4: product:", hfss.product_name)
        print("step 5: design:", hfss.design_name)
        print("step 6: throwaway design created OK")
    print("step 7: releasing desktop...")
    hfss.release_desktop(close_projects=True, close_desktop=True)
    print("PROBE PASS")
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
