"""Ticket 16 probe, phase 5: stock before-state of the trap + clean single-launch detach test.

5a (OFFLINE, no AEDT): HFSSDesignSolution(None, DesignType.HFSS) under STOCK
    1.3.0 and under the patched alias -> exact before/after of the
    missing HfssConstants.default_solution trap.
5b (LIVE, one launch): open the copy, detach odesign, touch the
    solution_type getter/setter fallback paths -> does the trap fire
    under a real (non-offline) recipe path when GetSolutionType is
    unavailable.
"""

import os
import sys
import time

print("--- 5a OFFLINE before-state ---", flush=True)
from ansys.aedt.core.generic.aedt_constants import HfssConstants  # noqa: E402
from ansys.aedt.core.application.design_solutions import HFSSDesignSolution  # noqa: E402

print("5a: hasattr default_solution (stock) =", hasattr(HfssConstants, "default_solution"), flush=True)
try:
    off = HFSSDesignSolution(None, HfssConstants, "2024.1")
    off = off.solution_type
    print("5a: STOCK solution_type =", repr(off), flush=True)
except Exception as e:  # noqa: BLE001
    print(f"5a: STOCK EXC {type(e).__name__}: {str(e)[:150]}", flush=True)
print("5a: patching alias...", flush=True)
HfssConstants.default_solution = HfssConstants.solution_default
off = HFSSDesignSolution(None, HfssConstants, "2024.1")
print("5a: PATCHED solution_type =", repr(off.solution_type), flush=True)
off.solution_type = None
print("5a: PATCHED setter(None) ok, value =", repr(off.solution_type), flush=True)

import psutil  # noqa: E402
from ansys.aedt.core import Hfss  # noqa: E402

PROJECT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects", "readout_probe.aedt")
)
DESIGN = "solve_design"


def kill_new_aedt(start_time):
    for p in psutil.process_iter(["pid", "name", "create_time"]):
        try:
            if p.info["name"] == "ansysedt.exe" and p.info["create_time"] > start_time:
                p.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def main() -> int:
    start_time = time.time()
    print("--- 5b LIVE detach test ---", flush=True)
    try:
        with Hfss(
            version="2024.1",
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design=DESIGN,
            solution_type="Modal",
            remove_lock=True,
        ) as hfss:
            print("5b: open ok", flush=True)
            try:
                print("5b: stock getter (odesign attached) =", repr(hfss.design_solutions.solution_type), flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"5b: getter EXC {type(e).__name__}: {str(e)[:200]}", flush=True)
            try:
                hfss.solution_type = None
                print("5b: setter(None) ok, value =", repr(hfss.solution_type), flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"5b: setter(None) EXC {type(e).__name__}: {str(e)[:200]}", flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
