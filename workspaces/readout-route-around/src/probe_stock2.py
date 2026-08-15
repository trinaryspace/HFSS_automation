"""Ticket 16 probe, phase 4 (STOCK): does the missing default_solution trap fire?

The trap is in HFSSDesignSolution.solution_type fallbacks (no odesign, or
GetSolutionType() raising). The smoke-matrix always passed solution_type
explicitly, which dodges the None-value branches. This phase opens the copy
WITHOUT solution_type (None) and without a design name, then touches
design_solutions/report paths — the shape a recipe hits when it reads
results after solve (EC#6 flake route: fresh attach).

Also: stock attach + readout, then the SAME readout again after releasing
odesign (simulating the grpc-design drop): design_solutions._odesign = None
then solution_type read -> falls into the missing-attr branch if the code
path is reached.

No monkeypatch. Record the exact exception.
"""

import os
import sys
import time

import psutil
from ansys.aedt.core import Hfss

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
    print(f"PROJECT={PROJECT}", flush=True)
    try:
        print("--- phase 4a: open WITHOUT solution_type (None path) ---", flush=True)
        try:
            with Hfss(
                version="2024.1",
                new_desktop=True,
                non_graphical=False,
                project=PROJECT,
                design=DESIGN,
                remove_lock=True,
            ) as hfss:
                print("4a: open ok", flush=True)
                print("4a: solution_type =", repr(hfss.solution_type), flush=True)
                print("4a: report read:", flush=True)
                data = hfss.post.get_solution_data(expressions="dB(S(1,1))", setup_sweep_name="Setup1 : Sweep_MM13NY")
                print("4a: readout got", type(data).__name__, "real rows:",
                      getattr(data, "_solutions_real", {}).get("dB(S(1,1))", []).shape, flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"4a: EXC {type(e).__name__}: {str(e)[:300]}", flush=True)
            trace = sys.exc_info()[2]
            while trace and trace.tb_next:
                trace = trace.tb_next
            if trace:
                print(f"4a: raised at {os.path.basename(trace.tb_frame.f_code.co_filename)}:{trace.tb_lineno} in {trace.tb_frame.f_code.co_name}", flush=True)

        print("--- phase 4b: open, then detach odesign (forced fallback path) ---", flush=True)
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
                print("4b: open ok", flush=True)
                hfss.design_solutions._odesign = None
                try:
                    print("4b: after detach, design_solutions.solution_type =", repr(hfss.design_solutions.solution_type), flush=True)
                except Exception as e:  # noqa: BLE001
                    print(f"4b: EXC {type(e).__name__}: {str(e)[:200]}", flush=True)
                hfss.solution_type = None
                print("4b: setter(None) ok, solution_type =", repr(hfss.solution_type), flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"4b: EXC {type(e).__name__}: {str(e)[:300]}", flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
