"""Read S11, plot it, and report the agreed Result QA signals.

Route policy (SKILL.md, EC#6): `read_results.apply_route_arounds()` BEFORE
constructing Hfss, then one `ReadoutSession` for the whole stage — it tries
`get_solution_data` and then the report-export route on the process in hand,
and spends at most one fresh-process escalation per run. The route token for
each signal lands in `results/state/readouts.txt`.

Usage (workspace root):  python src/09_plots_qa.py
Prints one Verification line:  PASS: plots_qa <counts>
"""

import os
import sys

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

RESULTS = ws_common.RESULTS
STATE = ws_common.STATE
# The requested band and the QA thresholds locked in Clarification.
BAND_LO, BAND_HI = 5.8e9, 6.8e9
S11_TARGET_DB = -10.0


def _bands_below(freqs, s11, threshold):
    """Contiguous [lo, hi] spans where s11 <= threshold, by linear crossing."""
    spans, start = [], None
    for i, (f, v) in enumerate(zip(freqs, s11)):
        below = v <= threshold
        if below and start is None:
            if i == 0:
                start = f
            else:                            # interpolate the crossing
                f0, v0 = freqs[i - 1], s11[i - 1]
                start = f0 + (threshold - v0) * (f - f0) / (v - v0)
        elif not below and start is not None:
            f0, v0 = freqs[i - 1], s11[i - 1]
            spans.append((start, f0 + (threshold - v0) * (f - f0) / (v - v0)))
            start = None
    if start is not None:
        spans.append((start, freqs[-1]))
    return spans


def _local_minima(freqs, s11, threshold):
    return [(freqs[i], s11[i]) for i in range(1, len(s11) - 1)
            if s11[i] < s11[i - 1] and s11[i] <= s11[i + 1] and s11[i] < threshold]


def main():
    hfss = ws_common.attach()
    os.makedirs(RESULTS, exist_ok=True)
    session = read_results.ReadoutSession(
        hfss, recycle=ws_common.recycle_desktop, export_dir=RESULTS,
        state_dir=STATE)
    readout = session.read("dB(S(1,1))")
    lines = [read_results.verdict_line("s11", readout)]
    read_results.write_readouts(STATE, lines)

    if not readout.y:
        print("FAIL: plots_qa s11 unreadable route=%s" % readout.route, flush=True)
        return 1

    freqs = [float(x) for x in readout.x]
    if freqs and max(freqs) < 1e6:           # x came back in GHz, not Hz
        freqs = [f * 1e9 for f in freqs]
    s11 = [float(v) for v in readout.y]

    worst_in_band = max(v for f, v in zip(freqs, s11) if BAND_LO <= f <= BAND_HI)
    covered = worst_in_band <= S11_TARGET_DB
    spans = _bands_below(freqs, s11, S11_TARGET_DB)
    widest = max(spans, key=lambda s: s[1] - s[0]) if spans else None
    dips = _local_minima(freqs, s11, S11_TARGET_DB)
    s11_min = min(s11)
    f_min = freqs[s11.index(s11_min)]
    passive = max(s11) <= 0.05               # numerical tolerance on 0 dB

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot([f / 1e9 for f in freqs], s11, lw=1.8, color="#1f77b4", label="S11")
    ax.axhline(S11_TARGET_DB, ls="--", lw=1, color="#888", label="-10 dB")
    ax.axvspan(BAND_LO / 1e9, BAND_HI / 1e9, color="#2ca02c", alpha=0.12,
               label="required 5.8-6.8 GHz")
    if widest:
        ax.axvspan(widest[0] / 1e9, widest[1] / 1e9, color="#ff7f0e", alpha=0.10,
                   label="achieved -10 dB band")
    ax.set_xlabel("Frequency (GHz)")
    ax.set_ylabel("|S11| (dB)")
    ax.set_title("U-slot patch, probe fed - S11")
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right", fontsize=9)
    fig.tight_layout()
    plot = os.path.join(RESULTS, "s11.png")
    fig.savefig(plot, dpi=150)
    plt.close(fig)

    print("QA  in-band worst S11 (5.8-6.8 GHz): %.2f dB -> %s"
          % (worst_in_band, "PASS" if covered else "FAIL"), flush=True)
    if widest:
        print("QA  widest -10 dB band: %.3f-%.3f GHz (%.0f MHz, %.1f%% frac)"
              % (widest[0] / 1e9, widest[1] / 1e9, (widest[1] - widest[0]) / 1e6,
                 100 * (widest[1] - widest[0]) / ((widest[0] + widest[1]) / 2)),
              flush=True)
    print("QA  resonant dips: %s"
          % ", ".join("%.2f GHz @ %.1f dB" % (f / 1e9, v) for f, v in dips),
          flush=True)
    print("QA  S11 min %.2f dB at %.3f GHz; max %.3f dB (passive=%s)"
          % (s11_min, f_min / 1e9, max(s11), passive), flush=True)

    line = ("PASS: plots_qa points=%d route=%s in_band_worst=%.2fdB covered=%s "
            "dips=%d plot=%s" % (len(s11), readout.route, worst_in_band,
                                 covered, len(dips), os.path.basename(plot)))
    print(line, flush=True)
    import run_events
    run_events.emit("qa.s11", stage="qa", verdict=line,
                    detail="plot=%s" % plot, state_dir=STATE)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
        sys.exit(1)
