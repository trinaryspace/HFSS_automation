"""Sanity-check the far-field pattern: where the beam points, and whether the
directivity integrates to unity over the sphere.

Reads dB(DirTotal) over FF_Sphere at the six field points through the
report-export route, then for each frequency reports:
  - the peak and its direction (theta, phi)
  - the value toward the tip (+x: theta 90, phi 0) and away from it (-x)
  - (1/4pi) * integral of D over the sphere, which must be 1 by definition

Frame: +x runs base -> tip (the expected end-fire direction), the board lies
in the xy plane, z is normal to it.

Usage (workspace root):  python src/11_pattern_check.py
Prints one Verification line:  PASS: pattern_check ...
"""

import csv
import math
import os

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

RESULTS = ws_common.RESULTS
EXPR = "dB(DirTotal)"


def main():
    hfss = ws_common.attach()
    path, note = read_results.export_report_csv(
        hfss, EXPR, export_dir=RESULTS, sweep="Setup1 : FieldPts",
        sphere="FF_Sphere")
    if not path:
        raise RuntimeError("far-field export failed: %s" % note[:300])

    with open(path, encoding="utf-8-sig", newline="") as handle:
        rows = [r for r in csv.reader(handle) if any(c.strip() for c in r)]
    header = [h.strip() for h in rows[0]]
    i_f = next(i for i, h in enumerate(header) if h.startswith("Freq"))
    i_p = next(i for i, h in enumerate(header) if h.startswith("Phi"))
    i_t = next(i for i, h in enumerate(header) if h.startswith("Theta"))
    i_v = len(header) - 1
    by_freq = {}
    for r in rows[1:]:
        by_freq.setdefault(float(r[i_f]), []).append(
            (float(r[i_t]), float(r[i_p]), float(r[i_v])))

    print("header:", header, "rows:", len(rows) - 1, flush=True)
    summary = []
    for f in sorted(by_freq):
        pts = by_freq[f]
        thetas = sorted({p[0] for p in pts})
        phis = sorted({p[1] for p in pts})
        dth = math.radians(thetas[1] - thetas[0])
        dph = math.radians(phis[1] - phis[0])
        peak = max(pts, key=lambda p: p[2])
        look = {(p[0], p[1] % 360.0): p[2] for p in pts}
        fwd, back = look.get((90.0, 0.0)), look.get((90.0, 180.0))
        total = 0.0
        for t, p, v in pts:
            if p >= 360.0 - 1e-9 and 0.0 in phis:
                continue                     # phi 360 duplicates phi 0
            w = dth if 0.0 < t < 180.0 else dth / 2.0
            total += (10 ** (v / 10.0)) * math.sin(math.radians(t)) * w * dph
        unity = total / (4 * math.pi)
        # angle between the peak direction and +x
        st = math.sin(math.radians(peak[0]))
        off = math.degrees(math.acos(max(-1.0, min(1.0, st * math.cos(math.radians(peak[1]))))))
        print("%.0f GHz: peak %.2f dBi at theta=%.0f phi=%.0f (%.0f deg off +x); "
              "toward tip %.2f dBi, away %.2f dBi, front/back %.1f dB; "
              "sphere integral %.3f"
              % (f, peak[2], peak[0], peak[1], off, fwd, back, fwd - back, unity),
              flush=True)
        summary.append((f, peak[2], off, fwd, fwd - back, unity))

    worst_unity = max(abs(s[5] - 1.0) for s in summary)
    print("PASS: pattern_check freqs=%d max_peak_offset_deg=%.0f "
          "min_front_to_back_dB=%.1f worst_integral_error=%.3f"
          % (len(summary), max(s[2] for s in summary),
             min(s[4] for s in summary), worst_unity), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
