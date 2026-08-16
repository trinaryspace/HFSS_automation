"""Is the S11 readout actually broken, or is the reader broken?

Ticket 16 (2026-08-07) proved `get_solution_data` works on this box against a
solved project on a FRESH attach, and recorded one thing it could not test:
"the in-session-after-analyze / reopen empty state ... cannot be exercised
without a solve, which this ticket forbids."

The 2026-08-16 pilot hit exactly that untested state and failed with
`GrpcApiError ... GetPropValue`. This probe closes the gap: same project,
solved, opened from a clean process on a copy (ADR 0001), trying the shapes
ticket 16 validated plus the accessors the pilot's reader used.

Read-only. No solve. Never touches the original.
"""

import json
import os
import sys
import traceback

WS = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.join(WS, "probe.aedt")
DESIGN = "Patch2400"
RESULT = {}


def record(name, ok, detail=""):
    RESULT[name] = {"ok": bool(ok), "detail": str(detail)[:300]}
    print(f"  {'OK  ' if ok else 'FAIL'} {name}: {str(detail)[:160]}", flush=True)


def main():
    # Ticket 16's one-line route-around, applied before the app is built.
    try:
        from ansys.aedt.core.application import design_solutions as ds
        klass = getattr(ds, "HfssConstants", None)
        if klass is not None and not hasattr(klass, "default_solution"):
            klass.default_solution = klass.solution_default
            record("route_around_applied", True, "HfssConstants aliased")
        else:
            record("route_around_applied", True, f"HfssConstants={klass!r} (no alias needed)")
    except Exception as exc:
        record("route_around_applied", False, f"{type(exc).__name__}: {exc}")

    from ansys.aedt.core import Hfss

    graphical = "--graphical" in sys.argv
    hfss = Hfss(project=PROJECT, design=DESIGN, version="2024.1",
                new_desktop=True, non_graphical=not graphical, remove_lock=True)
    record("mode", True, "graphical" if graphical else "non_graphical")
    try:
        sweeps = list(getattr(hfss, "existing_analysis_sweeps", []) or [])
        record("existing_analysis_sweeps", bool(sweeps), sweeps)
        sweep = next((s for s in sweeps if "Sweep" in s), None)

        for label, kwargs in (
            ("get_solution_data(no ctx)", {"expressions": "dB(S(1,1))"}),
            ("get_solution_data(sweep)", {"expressions": "dB(S(1,1))",
                                          "setup_sweep_name": sweep}),
            ("get_solution_data(LastAdaptive)", {"expressions": "dB(S(1,1))",
                                                 "setup_sweep_name": "Setup1 : LastAdaptive"}),
        ):
            if kwargs.get("setup_sweep_name") is None and "sweep" in label:
                record(label, False, "no sweep name found")
                continue
            try:
                sol = hfss.post.get_solution_data(**kwargs)
            except Exception as exc:
                record(label, False, f"{type(exc).__name__}: {exc}")
                continue
            if not sol:
                record(label, False, "returned falsy")
                continue
            # The pilot's reader judged fill-state with `data_real`, which does
            # not exist in 1.3.0 -- so it reads "unfilled" even when filled.
            has_data_real = hasattr(sol, "data_real")
            freqs = list(getattr(sol, "primary_sweep_values", []) or [])
            try:
                vals = sol.get_expression_data("dB(S(1,1))", formula="real")
                vals = list(vals or [])
            except Exception as exc:
                vals = []
                record(label + " :: get_expression_data", False,
                       f"{type(exc).__name__}: {exc}")
            record(label, bool(freqs and vals),
                   f"points={len(freqs)} values={len(vals)} "
                   f"data_real_attr={has_data_real} "
                   f"first={vals[0] if vals else None} min={min(vals) if vals else None}")
            if freqs and vals:
                low = min(range(len(vals)), key=lambda i: vals[i])
                record(label + " :: S11 minimum", True,
                       f"{vals[low]:.4f} dB at {freqs[low]:.5f} GHz")
        for label, fn in (
            ("create_report", lambda: hfss.post.create_report(
                expressions="dB(S(1,1))", setup_sweep_name=sweep,
                plot_type="Rectangular Plot", plot_name="S11probe")),
            ("export_report_to_file", lambda: hfss.post.export_report_to_file(
                output_dir=WS, plot_name="S11probe", extension=".csv")),
        ):
            try:
                out = fn()
                record(label, bool(out), out)
            except Exception as exc:
                record(label, False, f"{type(exc).__name__}: {exc}")
    finally:
        try:
            hfss.release_desktop(close_projects=False, close_desktop=True)
        except Exception:
            pass
    print("\nRESULT_JSON " + json.dumps(RESULT))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
    sys.stdout.flush()
    os._exit(0)
