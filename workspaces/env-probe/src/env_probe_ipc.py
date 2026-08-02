"""Probe: full trivial flow over the non-gRPC (IPC/COM) transport.

Replicates env_probe.py but with settings.use_grpc_api=False, to test
whether the GetActiveDesign freeze is gRPC-specific on this backend.
"""

import os
import sys

from ansys.aedt.core import settings

settings.use_grpc_api = False

from ansys.aedt.core import Hfss


def main() -> int:
    print("step 1: use_grpc_api = False set", flush=True)
    print("step 2: launching new graphical desktop (2024.1) via IPC...", flush=True)
    with Hfss(
        version="2024.1",
        new_desktop=True,
        non_graphical=False,
        design="probe_design",
    ) as hfss:
        print("step 3: desktop version:", hfss.aedt_version, flush=True)
        print("step 4: product:", hfss.product_name, flush=True)
        print("step 5: design:", hfss.design_name, flush=True)
        print("step 6: throwaway design created OK", flush=True)
    print("step 7: releasing desktop...", flush=True)
    hfss.release_desktop(close_projects=True, close_desktop=True)
    print("PROBE PASS", flush=True)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
