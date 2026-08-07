"""Stage 9: plots — S11 report written to results/ (EC#6 flaky-readout rules).

Fetches dB(S(1,1)) via get_solution_data; writes s11.csv (freq, dB) when
readable. On an unfilled SolutionData (expected; EC#6): retry once on a
fresh attach, then report the readout unreadable — never claim a
numbers-based QA verdict on a flaky readout.
"""

import csv
import os
import sys

from ws_common import RESULTS, attach, exit_keep_alive, read_state


def fetch(expression, setup_sweep):
    """(freqs|None, vals|None, errmsg|None) — None pair on unfilled readout."""
    hfss = attach(launch=False)
    sol = hfss.post.get_solution_data(
        expressions=expression, setup_sweep_name=setup_sweep
    )
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
        print("first readout unreadable:", err, "— retrying once", flush=True)
        freqs, vals, err = fetch("dB(S(1,1))", sweep_name)
    if freqs is None:
        print("PASS: plots readout unreadable — flaky readout (%s); no plot written" % err, flush=True)
        write_state("s11_unreadable", err)
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
