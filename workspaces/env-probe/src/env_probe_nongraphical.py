"""Probe variant: same trivial flow with non_graphical=True.

Tests whether the design-open freeze is a GUI-message-pump deadlock.
"""

import os
import sys

from ansys.aedt.core import Hfss


def main() -> int:
    print("step 1: launching NON-GRAPHICAL desktop (2024.1)...", flush=True)
    with Hfss(
        version="2024.1",
        new_desktop=True,
        non_graphical=True,
        design="probe_design",
    ) as hfss:
        print("step 2: desktop version:", hfss.aedt_version, flush=True)
        print("step 3: design:", hfss.design_name, flush=True)
        print("step 4: throwaway design created OK (non-graphical)", flush=True)
    print("step 5: releasing desktop...", flush=True)
    hfss.release_desktop(close_projects=True)
    print("PROBE PASS (non-graphical)", flush=True)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
