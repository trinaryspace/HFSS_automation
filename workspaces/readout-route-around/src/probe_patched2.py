"""Ticket 16 probe, phase 3 (PATCHED): export-path correctness for the full auto-sweep.

Follow-up to run2: shape H mistakenly targeted `Setup1 : LastAdaptive` (sweeps[0]),
so the exported report had a single 2.4 GHz row. Re-run the report+export shapes
against the actual auto-sweep `Setup1 : Sweep_MM13NY`, and introspect the raw
client-side tables of the returned SolutionData to pin the "unfilled" shape.

Same route-around (HfssConstants.default_solution alias) kept applied.
"""

import os
import sys
import time

import psutil

from ansys.aedt.core.generic.aedt_constants import HfssConstants

HfssConstants.default_solution = "HFSS Terminal Network"

from ansys.aedt.core import Hfss  # noqa: E402

PROJECT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects", "readout_probe.aedt")
)
DESIGN = "solve_design"
SWEEP = "Setup1 : Sweep_MM13NY"
EVIDENCE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence"))


def kill_new_aedt(start_time):
    for p in psutil.process_iter(["pid", "name", "create_time"]):
        try:
            if p.info["name"] == "ansysedt.exe" and p.info["create_time"] > start_time:
                p.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def main() -> int:
    start_time = time.time()
    print(f"PROJECT={PROJECT} SWEEP={SWEEP}", flush=True)
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
            print("[open] ok (patched)", flush=True)

            print("--- shape K: raw internals of get_solution_data(auto sweep) ---", flush=True)
            try:
                data = hfss.post.get_solution_data(expressions="dB(S(1,1))", setup_sweep_name=SWEEP)
                print("K: expressions =", data.expressions, flush=True)
                print("K: primary_sweep_values n =", len(data.primary_sweep_values), flush=True)
                print("K: _solutions_real keys =", list(getattr(data, "_solutions_real", {}).keys()), flush=True)
                for k, v in getattr(data, "_solutions_real", {}).items():
                    print(f"K:   _solutions_real[{k}].shape = {getattr(v, 'shape', 'n/a')}", flush=True)
                    print(f"K:   _solutions_real[{k}] dtype = {getattr(v, 'dtype', 'n/a')}", flush=True)
                print("K: raw server table size check via variations:", len(data.variations), flush=True)
                print("K: nominal_variation data len:", len(list(data.nominal_variation.GetRealDataValues("dB(S(1,1))", False))), flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"K: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape L: create_report on the actual sweep ---", flush=True)
            try:
                report = hfss.post.create_report(
                    expressions="dB(S(1,1))", setup_sweep_name=SWEEP, plot_name="rubar_full"
                )
                print("L: report ok", type(report).__name__, flush=True)
                rd = report.get_solution_data()
                print("L: report data primary_sweep n =", len(rd.primary_sweep_values), flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"L: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape M: export_report_to_file of the full-sweep report ---", flush=True)
            for ext in ("csv", "tab"):
                try:
                    path = hfss.post.export_report_to_file(
                        output_dir=EVIDENCE, plot_name="rubar_full", extension=ext
                    )
                    nrows = 0
                    if path and os.path.exists(path):
                        with open(path, "r", errors="replace") as fh:
                            nrows = sum(1 for _ in fh)
                    print(f"M[{ext}]: {path} exists={bool(path and os.path.exists(path))} rows={nrows}", flush=True)
                except Exception as e:  # noqa: BLE001
                    print(f"M[{ext}]: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape N: export_report_to_jpg ---", flush=True)
            try:
                ok = hfss.post.export_report_to_jpg(project_path=EVIDENCE, plot_name="rubar_full")
                jpg = os.path.join(EVIDENCE, "rubar_full.jpg")
                print("N: export_report_to_jpg ->", ok, "file exists:", os.path.exists(jpg), flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"N: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
