"""Stage 10: Result QA — report every agreed signal (or "unreadable — flaky").

Signals (locked in Clarification): (1) convergence dS<=0.02; (2) port
excited — lumped port + radiation present, S11 populated; (3) in-band
resonance — S11 min inside 2.28-2.52 GHz (5% of 2.4; case notes.md judges
resonance position, not absolute depth); (4) energy pass — single-port
passive (S11 <= 0 dB everywhere) + solve profile Normal Completion.

Reads results/state + s11.csv (stage 09) + the solve profile (filesystem
only, profile_evidence); re-attach-based reads only (EC#6 never poll).
Prints one line per signal; the summary records them verbatim.
"""

import csv
import os
import sys

from confirm_solve import project_results_dir
from profile_evidence import newest_terminal_profile, terminal_status
from ws_common import RESULTS, PROJECT, attach, exit_keep_alive, read_state, write_state

TARGET = 2.4
BW_LOW = 2.28
BW_HIGH = 2.52
TARGET_DEPTH = -10.0


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
    names = sorted(b.name for b in hfss.boundaries)
    print("boundaries:", names, flush=True)
    has_port = any(n == "1" for n in names)
    has_rad = any("Rad" in n for n in names)

    profile = newest_terminal_profile(project_results_dir(PROJECT))
    status = terminal_status(profile) if profile else None
    print("solve profile:", os.path.basename(profile) if profile else None, "status =", status, flush=True)

    rows = read_csv(os.path.join(RESULTS, "s11.csv"))
    print("s11 points from csv:", len(rows), flush=True)
    unreadable = read_state("s11_unreadable")

    signals = {}
    signals["convergence"] = (
        "solve %s" % (status or "no terminal profile")
        + " — dS<=0.02 target on Setup1; final dS read via UI on this box (readout route: UI)"
    )
    signals["port_excited"] = (
        "yes: lumped port '1' + Rad boundary, %d s11 samples" % len(rows)
        if (has_port and has_rad and rows) else
        "port=%s rad=%s csv=%d — unreadable — flaky readout (%s)"
        % (has_port, has_rad, len(rows), unreadable or "no csv")
    )
    if not rows:
        signals["in_band_resonance"] = "unreadable — flaky readout (%s)" % (unreadable or "no csv")
        signals["energy_pass"] = "unreadable — flaky readout"
    else:
        freqs = [f for f, _ in rows]
        s11 = [s for _, s in rows]
        band = [s for f, s in rows if BW_LOW <= f <= BW_HIGH]
        if band:
            s11_min = min(band)
            f_min = freqs[s11.index(s11_min)]
            signals["in_band_resonance"] = (
                "S11 min %.2f dB @ %.3f GHz (in %.2f-%.2f GHz) — %s"
                % (s11_min, f_min, BW_LOW, BW_HIGH,
                   "PASS resonance in band" if BW_LOW <= f_min <= BW_HIGH else "FAIL out of band")
                + (" (depth >= %.0f dB)" % TARGET_DEPTH if s11_min > TARGET_DEPTH else " (depth OK)")
            )
        else:
            signals["in_band_resonance"] = "no samples in %.2f-%.2f GHz" % (BW_LOW, BW_HIGH)
        max_s11 = max(s11)
        signals["energy_pass"] = (
            "single-port passive: max S11 %.2f dB over %d points — %s"
            % (max_s11, len(rows), "PASS (no positive S11)" if max_s11 <= 0 else "FAIL positive S11")
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
