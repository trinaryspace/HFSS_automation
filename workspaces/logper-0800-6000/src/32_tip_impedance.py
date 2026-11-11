"""Where does the antenna sit on the Smith chart, seen at the tip?

|S11| alone says how big the mismatch is, not which way to move. This stage
reads complex S11 at the port (coax base), removes the coax's electrical
length so the reference plane is at the feed point on the tip, and reports
the average reflection coefficient and the impedance it corresponds to, per
GHz. A locus centred left of the chart centre (Re Gamma < 0) means the
antenna looks LOWER than 50 ohm - narrow the feed strips; right means higher.

The coax delay is taken from the model's own variables: length coax_L (read
from the Shield's bounding box) and the dielectric's permittivity.

Usage (workspace root):
    set HFSS_WS_DESIGN=LogPer_RO4350B_v2
    python src/32_tip_impedance.py --tag v2_it1
Prints one Verification line:  PASS: tip_impedance ...
"""

import argparse
import cmath
import math
import os
import sys

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

C0 = 299792458.0
SWEEP = "Setup1 : Sweep1"
BANDS = ((0.8, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tag", required=True)
    args = parser.parse_args(argv)
    hfss = ws_common.attach()
    out_dir = os.path.join(ws_common.RESULTS, args.tag)
    os.makedirs(out_dir, exist_ok=True)

    shield = [float(v) for v in hfss.modeler["Shield"].bounding_box]
    length_m = (shield[3] - shield[0]) * 1e-3
    diel = hfss.modeler["CoaxDiel"].material_name
    eps = float(hfss.materials[diel].permittivity.value)

    fx, re, note_r = read_results.read_via_report(hfss, "re(S(1,1))", sweep=SWEEP,
                                                  export_dir=out_dir)
    fy, im, note_i = read_results.read_via_report(hfss, "im(S(1,1))", sweep=SWEEP,
                                                  export_dir=out_dir)
    if not re or not im or len(re) != len(im):
        raise RuntimeError("complex S11 unreadable: %s | %s" % (note_r[:150], note_i[:150]))
    freqs = [f / 1e9 if f > 1e6 else f for f in fx]

    gammas = []
    for f, a, b in zip(freqs, re, im):
        beta = 2 * math.pi * f * 1e9 * math.sqrt(eps) / C0
        gammas.append((f, complex(a, b) * cmath.exp(2j * beta * length_m)))

    print("coax: length %.2f mm, dielectric %s eps %.3f" % (length_m * 1e3, diel, eps),
          flush=True)
    rows = []
    for lo, hi in BANDS:
        g = [v for f, v in gammas if lo <= f <= hi]
        mean = sum(g) / len(g)
        radius = sum(abs(v - mean) for v in g) / len(g)
        z = 50.0 * (1 + mean) / (1 - mean)
        rows.append((lo, hi, mean, radius, z))
        print("  %.1f-%.0f GHz: locus centre Gamma = %+.3f %+.3fj (|.|=%.3f), mean "
              "radius %.3f -> centre impedance %.1f %+.1fj ohm"
              % (lo, hi, mean.real, mean.imag, abs(mean), radius, z.real, z.imag),
              flush=True)
    allg = [v for f, v in gammas if 1.0 <= f <= 6.0]
    centre = sum(allg) / len(allg)
    z = 50.0 * (1 + centre) / (1 - centre)
    print("PASS: tip_impedance tag=%s points=%d centre_1to6GHz=%+.3f%+.3fj "
          "Z_centre=%.1f%+.1fj ohm" % (args.tag, len(gammas), centre.real,
                                      centre.imag, z.real, z.imag), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
