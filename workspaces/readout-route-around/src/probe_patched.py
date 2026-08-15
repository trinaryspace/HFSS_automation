"""Ticket 16 probe, phase 2 (PATCHED): route-around validation on a copy.

Monkeypatch = the route-around under test: alias the missing
`HfssConstants.default_solution` to the existing `solution_default`
(the AttributeError trap in HFSSDesignSolution.*, .solution_type
getter/setter fallbacks and the base-class setter).

Then exercise the readout/export shape matrix on the throwaway copy of an
already-solved project (fresh attach per EC#6 guidance), recording exactly
which shapes return data and which still fail.

Evidence protocol (EC items 9/10): kill any ansysedt.exe started by this
process before exit; never rely on release_desktop to reap the server.
"""

import os
import sys
import time

import psutil

from ansys.aedt.core.generic.aedt_constants import HfssConstants

print(f"pre-patch: hasattr HfssConstants.default_solution = {hasattr(HfssConstants, 'default_solution')}", flush=True)
print(f"pre-patch: HfssConstants.solution_default = {HfssConstants.solution_default!r}", flush=True)
HfssConstants.default_solution = "HFSS Terminal Network"
print(f"post-patch: hasattr HfssConstants.default_solution = {hasattr(HfssConstants, 'default_solution')}", flush=True)

print("--- offline annex: HFSSDesignSolution(None, DesignType.HFSS).solution_type ---", flush=True)
try:
    from ansys.aedt.core.application.design_solutions import HFSSDesignSolution  # noqa: E402

    off = HFSSDesignSolution(None, HfssConstants, "2024.1")
    print("offline annex: solution_type =", repr(off.solution_type), flush=True)
except Exception as e:  # noqa: BLE001
    print(f"offline annex: EXC {type(e).__name__}: {str(e)[:200]}", flush=True)

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


def dump(data, label):
    if data is None or isinstance(data, bool):
        print(f"{label}: got={type(data).__name__} valid=False", flush=True)
        return data
    print(f"{label}: got={type(data).__name__} valid=True", flush=True)
    try:
        psv = list(data.primary_sweep_values)
        print(f"{label}: primary_sweep n={len(psv)} first={psv[0] if psv else None} last={psv[-1] if psv else None}", flush=True)
    except Exception as e:  # noqa: BLE001
        print(f"{label}: primary_sweep FAILED {type(e).__name__}: {str(e)[:120]}", flush=True)
        psv = []
    try:
        real, _ = data.full_matrix_real_imag
        vals = [float(v) for v in real[data.active_expression]]
        print(f"{label}: full_matrix_real n={len(vals)} min={round(min(vals), 3)}", flush=True)
        if psv:
            freqs = [float(f) for f in psv]
            i24 = min(range(len(freqs)), key=lambda i: abs(freqs[i] - 2.4))
            if i24 < len(vals):
                print(f"{label}: S11@2.4GHz = {round(vals[i24], 3)} dB", flush=True)
    except Exception as e:  # noqa: BLE001
        print(f"{label}: full_matrix REAL FAILED {type(e).__name__}: {str(e)[:160]} (unfilled shape)", flush=True)
    print(f"{label}: hasattr data_real = {hasattr(data, 'data_real')}", flush=True)
    return data


def main() -> int:
    start_time = time.time()
    print(f"PROJECT={PROJECT}", flush=True)
    try:
        expect_unfilled = 0
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

            print("--- shape A: design_solutions.solution_type ---", flush=True)
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
            sweeps = list(hfss.existing_analysis_sweeps)
            print("C:", sweeps, flush=True)

            print("--- shape D: get_solution_data, no context ---", flush=True)
            try:
                dump(hfss.post.get_solution_data(expressions="dB(S(1,1))"), "D")
            except Exception as e:  # noqa: BLE001
                print(f"D: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape E: get_solution_data, actual sweep name ---", flush=True)
            for name in sweeps:
                try:
                    dump(hfss.post.get_solution_data(expressions="dB(S(1,1))", setup_sweep_name=name), f"E[{name}]")
                except Exception as e:  # noqa: BLE001
                    print(f"E[{name}]: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape F: get_solution_data, LastAdaptive ---", flush=True)
            for name in sweeps:
                base = name.split(":")[0].strip()
                try:
                    dump(hfss.post.get_solution_data("dB(S(1,1))", setup_sweep_name=f"{base} : LastAdaptive"), "F")
                except Exception as e:  # noqa: BLE001
                    print(f"F: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)
                break

            print("--- shape G: results proxy get_solution_data ---", flush=True)
            try:
                tiny = [s for s in sweeps if "Sweep" in s] or sweeps
                dump(hfss.results.get_solution_data("S(1,1)", setup_sweep_name=tiny[0] if tiny else None), "G")
            except Exception as e:  # noqa: BLE001
                print(f"G: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape H: post.create_report (actual sweep) ---", flush=True)
            try:
                base = sweeps[0].split(":")[0].strip()
                report = hfss.post.create_report(
                    expressions="dB(S(1,1))", setup_sweep_name=sweeps[0], plot_name="rubar_probe"
                )
                print("H:", type(report).__name__, "plot_name:", getattr(report, "plot_name", None), flush=True)
                if report and not isinstance(report, bool):
                    rdata = report.get_solution_data()
                    dump(rdata, "H.rpt")
            except Exception as e:  # noqa: BLE001
                print(f"H: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape I: export_report_to_file (csv) ---", flush=True)
            try:
                outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence")
                path = hfss.post.export_report_to_file(output_dir=outdir, plot_name="rubar_probe", extension="csv")
                print("I:", path, "exists:", os.path.exists(path) if path else None, flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"I: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)

            print("--- shape J: SolutionData.export_data_to_csv ---", flush=True)
            try:
                base = [s for s in sweeps if "Sweep" in s] or sweeps
                rdata = hfss.post.get_solution_data(expressions="dB(S(1,1))", setup_sweep_name=base[0])
                if rdata and not isinstance(rdata, bool):
                    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "rubar_s11.csv")
                    print("J: export_data_to_csv ->", rdata.export_data_to_csv(out), flush=True)
                else:
                    print("J: skipped (source readout unfilled/failed)", flush=True)
            except Exception as e:  # noqa: BLE001
                print(f"J: EXC {type(e).__name__}: {str(e)[:250]}", flush=True)
    finally:
        kill_new_aedt(start_time)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
