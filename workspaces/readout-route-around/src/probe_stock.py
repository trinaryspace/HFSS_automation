"""Ticket 16 probe, phase 1 (STOCK): reproduce the missing HfssConstants.default_solution bug on a copy.

Strictly a reproduction pass on a throwaway copy of an already-solved project:
no monkeypatch, no route-around. Every shape below runs exactly as the
smoke-matrix diag scripts ran them (prior art), plus the app-level
solution_type getter that hits the client bug surface.

Evidence protocol (EC items 9/10): kill any ansysedt.exe started by this
process before exit; never rely on release_desktop to reap the server.
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
        with Hfss(
            version="2024.1",
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design=DESIGN,
            solution_type="Modal",
            remove_lock=True,
        ) as hfss:
            print("[open] ok", flush=True)

            print("--- shape A: design_solutions.solution_type (client bug surface) ---", flush=True)
            try:
                print("A:", repr(hfss.design_solutions.solution_type), flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"A: EXC {type(e).__name__}: {str(e)[:200]}", flush=True)

            print("--- shape B: app-level solution_type ---", flush=True)
            try:
                print("B:", repr(hfss.solution_type), flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"B: EXC {type(e).__name__}: {str(e)[:200]}", flush=True)

            print("--- shape C: existing_analysis_sweeps ---", flush=True)
            try:
                sweeps = list(hfss.existing_analysis_sweeps)
                print("C:", sweeps, flush=True)
            except Exception as e:  # noqa: BLE001
                sweeps = []
                print(f"C: EXC {type(e).__name__}: {str(e)[:200]}", flush=True)

            print("--- shape D: get_solution_data, no context ---", flush=True)
            try:
                data = hfss.post.get_solution_data(expressions="dB(S(1,1))")
                ok = data is not None and not isinstance(data, bool)
                print(f"D: got={type(data).__name__} valid={ok}", flush=True)
                if ok and hasattr(data, "data_real"):
                    try:
                        print("D: data_real len =", len(data.data_real()), flush=True)
                    except Exception:  # noqa: BLE001
                        print("D: data_real empty/failed", flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"D: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape E: get_solution_data, actual sweep name ---", flush=True)
            for name in sweeps:
                try:
                    data = hfss.post.get_solution_data(expressions="dB(S(1,1))", setup_sweep_name=name)
                    ok = data is not None and not isinstance(data, bool)
                    print(f"E[{name}]: got={type(data).__name__} valid={ok}", flush=True)
                    if ok and hasattr(data, "data_real"):
                        try:
                            print(f"E[{name}]: data_real len =", len(data.data_real()), flush=True)
                        except Exception:  # noqa: BLE001
                            print(f"E[{name}]: data_real empty/failed", flush=True)
                except Exception as e:  # noqa: BLE001
                    print(f"E[{name}]: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
