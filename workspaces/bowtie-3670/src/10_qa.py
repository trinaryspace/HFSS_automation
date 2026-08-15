"""Stage 13: Result QA — report each agreed signal with numbers.

Signals (as approved in Clarification, adjusted for the plain-bowtie choice):
  1. convergence        (solve completed; delta-S from profile if readable)
  2. port excited       (P1WavePort present, S11 data populated)
  3. in-band resonance  (S11 min within 3.4-3.6 GHz band, paper baseline)
  4. bandwidth          (VSWR<=2 span >= 2.6% of center, paper baseline)
  5. plausibility       (S11 sane magnitude, single-port passive device)
Flaky readouts are reported verbatim, never invented (EC#6).
"""

import csv
import os
import sys

from ws_common import PROJECT, RESULTS, read_state

S11_CSV = os.path.join(RESULTS, "s11.csv")
VSWR_CSV = os.path.join(RESULTS, "vswr.csv")


def load(csvp):
    rows = []
    if not os.path.exists(csvp):
        return None
    with open(csvp) as f:
        for r in csv.reader(f):
            if len(r) == 2:
                rows.append((float(r[0]), float(r[1])))
    return rows


def in_band_min(rows, lo=3.4, hi=3.6):
    band = [(f, v) for f, v in rows if lo <= f <= hi]
    if not band:
        return None
    return min(band, key=lambda t: t[1])


def main() -> int:
    print("=== Result QA ===", flush=True)
    s11 = load(S11_CSV)
    vswr = load(VSWR_CSV)

    s = []
    # 1. convergence
    solved = read_state("solve_done") is not None
    asol_present = os.path.exists(os.path.join(PROJECT + "results"))
    s.append(("1 convergence", f"solve_done={solved}; asol folder present={asol_present}"))

    # 2. ports
    bnds = (read_state("boundaries") or "").split(",")
    s.append(("2 port excited", f"P1WavePort in boundaries={any('P1WavePort' in b for b in bnds)}; s11 rows={len(s11) if s11 else 'none'}"))

    # 3. resonance
    if s11:
        imin = in_band_min(s11, 3.4, 3.6)
        global_min = min(s11, key=lambda t: t[1])
        if imin:
            ok = imin[1] <= -10
            s.append(("3 in-band resonance", f"min in 3.4-3.6 GHz = {imin[1]:.2f} dB @ {imin[0]:.3f} GHz (OK={ok})"))
        else:
            s.append(("3 in-band resonance", f"no S11 sample in 3.4-3.6 GHz; global min {global_min[1]:.2f} dB @ {global_min[0]:.3f}"))
    else:
        s.append(("3 in-band resonance", "unreadable — no s11.csv"))

    # 4. bandwidth
    if vswr:
        low, high = None, None
        below2 = [(f, v) for f, v in vswr if v <= 2]
        if below2:
            low = min(f for f, _ in below2)
            high = max(f for f, _ in below2)
        if low is not None and high is not None and high > low:
            fc = (low + high) / 2
            fbw = (high - low) / fc * 100
            ok = (high - low) / fc >= 0.026
            s.append(("4 bandwidth VSWR<=2", f"{low:.3f}-{high:.3f} GHz (FBW {fbw:.2f}%, OK={ok} vs paper 2.6%)"))
        else:
            s.append(("4 bandwidth VSWR<=2", "no VSWR<=2 span found"))
    else:
        s.append(("4 bandwidth VSWR<=2", "unreadable — no vswr.csv"))

    # 5. plausibility
    if s11:
        vals = [v for _, v in s11]
        sane = max(vals) <= 1.0 and min(vals) >= -40
        s.append(("5 plausibility |S11|", f"max={max(vals):.2f} dB, min={min(vals):.2f} dB (sane={sane})"))
    else:
        s.append(("5 plausibility |S11|", "unreadable"))

    for name, msg in s:
        print(f"  {name}: {msg}", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
