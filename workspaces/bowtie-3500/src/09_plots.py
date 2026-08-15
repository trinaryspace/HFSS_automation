"""Stage 12: post-process + reports/plots -> results/.

Recipe plots: |S11| (dB) vs freq, VSWR vs freq (paper baseline squealed at
~3.5 GHz). Readout is flaky (EC#6): retry with backoff, re-attach if
needed, and write what was observed.
"""

import os
import sys
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ws_common import RESULTS, attach, exit_keep_alive, read_state


def retry_get(hfss, expressions, sweep, tries=6, wait=15):
    for i in range(tries):
        data = hfss.post.get_solution_data(expressions=expressions, setup_sweep_name=sweep)
        if data is not None and data.data_real() is not None and len(data.data_real()) > 0:
            return data
        print(f"  try {i+1}: unfilled SolutionData; waiting {wait}s", flush=True)
        time.sleep(wait)
    return None


def main() -> int:
    sweeps = (read_state("sweeps") or "").split(",")
    sweep = next((s for s in sweeps if "Sweep" in s), None)
    assert sweep, "no sweep name found"
    hfss = attach(launch=False)
    print("using sweep:", sweep, flush=True)

    # ---- S11 ----
    s11 = retry_get(hfss, "dB(S(P1WavePort,P1WavePort))", sweep)
    if s11 is None:
        print("S11 readout failed (flaky) after retries — recorded", flush=True)
    else:
        x = list(s11.primary_sweep_values)
        y = list(s11.data_real())
        print("S11 points:", len(x), "range", min(y), "..", max(y), flush=True)
        with open(os.path.join(RESULTS, "s11.csv"), "w") as f:
            for a, b in zip(x, y):
                f.write(f"{a},{b}\n")
        plt.figure()
        plt.plot(x, y)
        plt.xlabel("freq (GHz)"); plt.ylabel("S11 (dB)")
        plt.title("Bowtie patch |S11|, paper baseline replica (no DGS)")
        plt.grid(True)
        plt.savefig(os.path.join(RESULTS, "s11.png"), dpi=150)
        plt.close()

    # ---- VSWR ----
    vswr = retry_get(hfss, "VSWR(P1WavePort)", sweep)
    if vswr is None:
        print("VSWR readout failed (flaky) — recorded", flush=True)
    else:
        x = list(vswr.primary_sweep_values)
        y = list(vswr.data_real())
        with open(os.path.join(RESULTS, "vswr.csv"), "w") as f:
            for a, b in zip(x, y):
                f.write(f"{a},{b}\n")
        plt.figure()
        plt.plot(x, y)
        plt.axhline(2, color="r", ls="--", lw=0.8)
        plt.xlabel("freq (GHz)"); plt.ylabel("VSWR")
        plt.title("VSWR — bowtie patch, paper baseline replica (no DGS)")
        plt.grid(True)
        plt.savefig(os.path.join(RESULTS, "vswr.png"), dpi=150)
        plt.close()

    done = os.path.exists(os.path.join(RESULTS, "s11.png")) and os.path.exists(os.path.join(RESULTS, "vswr.png"))
    print("results files:", sorted(os.listdir(RESULTS)), flush=True)
    print("STAGE_OK plots" if done else "STAGE_PARTIAL plots (flaky readout)", flush=True)
    return 0 if done else 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
