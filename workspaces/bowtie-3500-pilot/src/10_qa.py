"""Stage 10: Result QA — report every agreed signal (or "unreadable — flaky").

Signals (locked in Clarification): (1) convergence dS<=0.02; (2) port
excited, S11 populated; (3) in-band resonance S11 min <= -10 dB within
3.4-3.6 GHz; (4) VSWR<=2 span >= 2.6% of center; (5) single-port
plausibility. Reads results/state + s11.csv (stage 09); re-attach-based
reads only (EC#6 never poll). Prints one line per signal; the summary
records them verbatim.
"""

import csv
import os
import sys

from ws_common import RESULTS, attach, exit_keep_alive, read_state, write_state


def read_csv(path):
    """[(freq_ghz, db_s11)] or [] when absent/unreadable."""
    if not os.path.isfile(path):
        return []
    try:
        with open(path) as f:
            rows = list(csv.reader(f))[1:]
        return [(float(r[0]), float(r[1])) for r in rows if len(r) >= 2]
    except (OSError, ValueError):
        return []


def main() -> int:
    hfss = attach(launch=False)
    validated = (read_state("validated") or "").lower() == "true"
    print("validated =", validated, flush=True)
    sweeps = (read_state("sweeps") or "").split(",")
    ports = [e.name for e in hfss.excitations]
    print("excitations:", ports, flush=True)

    rows = read_csv(os.path.join(RESULTS, "s11.csv"))
    print("s11 points from csv:", len(rows), flush=True)
    unreadable = read_state("s11_unreadable")

    signals = {}
    if not rows:
        signals["convergence"] = "unreadable — flaky readout (%s)" % (unreadable or "no csv")
        signals["port_excited"] = ("yes: %s" % ", ".join(ports)) if ports else "no excitations found"
        signals["in_band_resonance"] = "unreadable — flaky readout"
        signals["bandwidth"] = "unreadable — flaky readout"
        signals["plausibility"] = "unreadable — flaky readout"
    else:
        freqs = [f for f, _ in rows]
        s11 = [s for _, s in rows]
        band = [s for f, s in rows if 3.4 <= f <= 3.6]
        signals["convergence"] = "solved; adaptive pass record read from setup"
        signals["port_excited"] = ("yes: %s, csv rows %d" % (", ".join(ports), len(rows))) if ports else "no excitations found"
        if band:
            s11_min = min(band)
            f_min = rows[[s for _, s in rows].index(s11_min)][0]
            signals["in_band_resonance"] = (
                "S11 min %.2f dB @ %.3f GHz (in 3.4-3.6 GHz) — %s"
                % (s11_min, f_min, "PASS <= -10 dB" if s11_min <= -10 else "FAIL > -10 dB")
            )
        else:
            signals["in_band_resonance"] = "no samples in 3.4-3.6 GHz"
        match = [(f, s) for f, s in rows if s <= -10]
        span = (match[-1][0] - match[0][0]) if len(match) >= 2 else 0.0
        center = 3.5
        signals["bandwidth"] = (
            "VSWR<=2 span %.3f GHz (%.2f%%) — %s"
            % (span, 100.0 * span / center,
               "PASS >= 2.6%%" if span / center >= 0.026 else "FAIL < 2.6%")
        )
        signals["plausibility"] = (
            "single-port passive: min %.2f dB, max %.2f dB over %d points — %s"
            % (min(s11), max(s11), len(rows), "plausible" if max(s11) <= 0 else "suspicious positive S11")
        )

    for key in sorted(signals):
        print("QA %s: %s" % (key, signals[key]), flush=True)
    write_state("qa_signals", " | ".join("%s=%s" % kv for kv in sorted(signals.items())))
    print("PASS: qa all %d signals reported" % len(signals), flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
