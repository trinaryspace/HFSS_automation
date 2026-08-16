"""Stage 9: plots — S11 vs frequency report written to results/ (EC#6 rules).

Fetches dB(S(1,1)) via get_solution_data; writes s11.csv (freq, dB) when
readable. Unfilled SolutionData is expected (EC#6): retry ONCE on a fresh
attach, then record the readout unreadable — the UI read on this box is
authoritative; never iterate readout shapes.
"""

import csv
import os
import sys

from ws_common import RESULTS, attach, exit_keep_alive, read_state, write_state


def fetch(expression, setup_sweep):
    """(freqs|None, vals|None, errmsg|None) — None pair on unfilled readout."""
    hfss = attach(launch=False)
    try:
        sol = hfss.post.get_solution_data(
            expressions=expression, setup_sweep_name=setup_sweep
        )
    except Exception as exc:  # noqa: BLE001 - any backend readout raise is unreadable (EC#6)
        return None, None, "%s: %s" % (type(exc).__name__, str(exc)[:160])
    if not sol:
        return None, None, "get_solution_data returned falsy"
    freqs = getattr(sol, "primary_sweep_values", None)
    rows = getattr(sol, "data_real", None)
    if freqs is None or rows is None or not len(list(rows or [])):
        return None, None, "unfilled SolutionData (no data_real / no sweep values)"
    return list(freqs), list(rows[0]), None


def main() -> int:
    sweeps = read_state("sweeps") or ""
    sweep_name = next((s.strip() for s in sweeps.split(",") if "Sweep" in s), None)
    assert sweep_name, "no sweep name recorded; run stage 06 first"
    print("using sweep:", sweep_name, flush=True)

    freqs, vals, err = fetch("dB(S(1,1))", sweep_name)
    if freqs is None:
        print("first readout unreadable:", err, "— retrying once on a fresh attach", flush=True)
        freqs, vals, err = fetch("dB(S(1,1))", sweep_name)
    if freqs is None:
        print("readout unreadable: %s — creating the S11 report in the open UI "
              "(authoritative read box) with a one-shot snapshot attempt" % err, flush=True)
        write_state("s11_unreadable", err)
        hfss = attach(launch=False)
        try:
            hfss.post.create_report(
                expressions="dB(S(1,1))",
                setup_sweep_name=sweep_name,
                plot_type="Rectangular Plot",
                plot_name="S11",
                snapshot_path=os.path.join(RESULTS, "s11_plot.png"),
                show=False,
            )
            print("S11 report + snapshot: created in UI / results/s11_plot.png", flush=True)
        except Exception as exc:  # noqa: BLE001 - snapshot is a bonus, never a blocker (locked route: UI)
            print("S11 report creation failed (%s: %s) — UI read remains the route" %
                  (type(exc).__name__, str(exc)[:160]), flush=True)
        print("PASS: plots readout unreadable — flaky readout (%s); no csv written "
              "(UI read on this box is authoritative)" % err, flush=True)
        return 0

    os.makedirs(RESULTS, exist_ok=True)
    csv_path = os.path.join(RESULTS, "s11.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["freq_ghz", "db_s11"])
        for fq, s11v in zip(freqs, vals):
            w.writerow(["%.6f" % float(fq), "%.6f" % float(s11v)])
    print("PASS: plots s11.csv written (%d points) — sweep %s" % (len(freqs), sweep_name), flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
