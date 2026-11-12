"""Beam check from two principal-plane cuts - the light replacement for the
full-sphere read in `11_pattern_check.py`.

The full 2-degree sphere at six frequencies is ~99,000 directions; on the
Rogers design AEDT spent over an hour on it and had to be killed. Whether
the beam is a single forward lobe needs far less:

  E-plane cut  theta = 90 deg, phi 0..360   (the plane of the board)
  H-plane cut  phi = 0 and 180 deg, theta 0..180   (normal to the board,
               through the board axis)

Frame: +x runs base -> tip (the wanted beam direction), board in xy, z normal.

Per frequency it reports, for each cut: the peak and where it points, the
value straight off the tip, the -3 dB beamwidth around the peak, the highest
lobe outside the main beam, and front-to-back ratio. It also compares the cut
peak with the design's peak directivity (from the antenna-parameter table,
if `results/<tag>/AgentReadout_AntennaParams.csv` exists) to show whether the
true maximum lies in these planes at all.

Reports are created with a restricted family so AEDT evaluates only the cut,
and are deleted afterwards so they cannot slow the project down later.

Usage (workspace root):
    set HFSS_WS_DESIGN=LogPer_RO4350B_v3
    python src/33_pattern_cuts.py --tag v3_it2v
Prints one Verification line:  PASS: pattern_cuts ...
"""

import argparse
import csv
import math
import os

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

SWEEP = "Setup1 : FieldPts"
SPHERE = "FF_Sphere"
EXPR = "dB(DirTotal)"
CUTS = {
    "E": ("AgentReadout_cutE", ["Freq:=", ["All"], "Theta:=", ["90deg"], "Phi:=", ["All"]], "Phi"),
    "H": ("AgentReadout_cutH", ["Freq:=", ["All"], "Phi:=", ["0deg", "180deg"], "Theta:=", ["All"]], "Theta"),
}


def export_cut(hfss, name, families, primary, out_dir):
    module = hfss.odesign.GetModule("ReportSetup")
    if name in [str(n) for n in (module.GetAllReportNames() or [])]:
        module.DeleteReports([name])
    module.CreateReport(name, "Far Fields", "Data Table", SWEEP,
                        ["Context:=", SPHERE], families,
                        ["X Component:=", primary, "Y Component:=", [EXPR]], [])
    print("   created %s" % name, flush=True)
    # Export through the report module itself. pyAEDT's
    # `post.export_report_to_file` first reads the report's properties
    # (`GetPropValue`), which failed over gRPC on this report (measured
    # 2026-11-11); `ExportToFile` needs nothing but the name and a path.
    path = os.path.join(out_dir, name + ".csv")
    if os.path.isfile(path):
        os.remove(path)
    module.ExportToFile(name, path)
    print("   exported %s" % os.path.basename(path), flush=True)
    module.DeleteReports([name])
    with open(path, encoding="utf-8-sig", newline="") as handle:
        rows = [r for r in csv.reader(handle) if any(c.strip() for c in r)]
    # Layout measured 2026-11-11: ONE ROW PER FREQUENCY, and one value column
    # per direction whose header names it, e.g.
    #   "dB(DirTotal) [] - Phi='266deg' Theta='90deg'"
    # (each preceded by a column repeating the primary sweep value). So the
    # direction is read from the header, never inferred from column position.
    import re
    header = [h.strip() for h in rows[0]]
    named = []
    for i, text in enumerate(header):
        phi = re.search(r"Phi='([-\d.]+)deg'", text)
        theta = re.search(r"Theta='([-\d.]+)deg'", text)
        if phi and theta:
            named.append((i, float(theta.group(1)), float(phi.group(1))))
    if not named:
        raise RuntimeError("no direction-named columns in %s: %r" % (path, header[:4]))
    data = {}
    for r in rows[1:]:
        f = float(r[0])
        data[f] = [(theta, phi, float(r[i])) for i, theta, phi in named]
    return data


def analyse(points):
    """points: [(angle_from_tip_deg in -180..180, dBi)] sorted by angle."""
    peak_a, peak_v = max(points, key=lambda p: p[1])
    fwd = min(points, key=lambda p: abs(p[0]))[1]
    back = min(points, key=lambda p: abs(abs(p[0]) - 180.0))[1]
    n = len(points)
    i0 = points.index((peak_a, peak_v))
    # walk outward from the peak to the -3 dB points (cut is periodic)
    lo = hi = 0
    while lo < n and points[(i0 - lo) % n][1] >= peak_v - 3.0:
        lo += 1
    while hi < n and points[(i0 + hi) % n][1] >= peak_v - 3.0:
        hi += 1
    step = 360.0 / n
    width = (lo + hi - 1) * step
    # main beam ends at the first minimum on each side; highest value beyond it
    def first_min(direction):
        k = 1
        while k < n - 1 and points[(i0 + direction * (k + 1)) % n][1] <= points[(i0 + direction * k) % n][1]:
            k += 1
        return k
    kl, kr = first_min(-1), first_min(+1)
    outside = [points[(i0 + k) % n][1] for k in range(kr + 1, n - kl)]
    side = max(outside) if outside else float("-inf")
    return peak_a, peak_v, fwd, back, width, side


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tag", required=True)
    args = parser.parse_args(argv)
    out_dir = os.path.join(ws_common.RESULTS, args.tag)
    os.makedirs(out_dir, exist_ok=True)
    hfss = ws_common.attach()

    peak_d = {}
    table = os.path.join(out_dir, "AgentReadout_AntennaParams.csv")
    if os.path.isfile(table):
        rows = list(csv.reader(open(table, encoding="utf-8-sig")))
        col = next(i for i, h in enumerate(rows[0]) if h.strip().startswith("PeakDirectivity"))
        for r in rows[1:]:
            peak_d[float(r[0])] = 10 * math.log10(float(r[col]))

    e = export_cut(hfss, *CUTS["E"], out_dir)
    h = export_cut(hfss, *CUTS["H"], out_dir)

    worst_side, worst_off, summary = -99.0, 0.0, []
    for f in sorted(e):
        # E-plane: angle from the tip = phi, folded to -180..180
        e_pts = sorted(((p if p <= 180 else p - 360), v) for t, p, v in e[f]
                       if abs(t - 90.0) < 1e-6 and p < 360.0 - 1e-6)
        # H-plane: phi=0 -> angle = 90 - theta ; phi=180 -> angle = 90 + theta (mod 360)
        h_raw = {}
        for t, p, v in h[f]:
            ang = (90.0 - t) if p < 90.0 else (90.0 + t)
            ang = ((ang + 180.0) % 360.0) - 180.0
            h_raw[round(ang, 3)] = v
        h_pts = sorted(h_raw.items())
        ea, ev, efwd, eback, ew, eside = analyse(e_pts)
        ha, hv, hfwd, hback, hw, hside = analyse(h_pts)
        ref = peak_d.get(f)
        print("%.0f GHz  E-plane: peak %.2f dBi at %+.0f deg, toward tip %.2f, -3 dB width "
              "%.0f deg, highest lobe outside main beam %.1f dB below peak, front/back %.1f dB"
              % (f, ev, ea, efwd, ew, ev - eside, efwd - eback), flush=True)
        print("        H-plane: peak %.2f dBi at %+.0f deg, toward tip %.2f, -3 dB width "
              "%.0f deg, highest lobe outside main beam %.1f dB below peak%s"
              % (hv, ha, hfwd, hw, hv - hside,
                 "; design peak directivity %.2f dBi" % ref if ref is not None else ""),
              flush=True)
        worst_side = max(worst_side, eside - ev, hside - hv)
        worst_off = max(worst_off, abs(ea), abs(ha))
        summary.append((f, ev, ea, hv, ha))

    hfss.save_project()
    print("PASS: pattern_cuts tag=%s freqs=%d max_peak_offset_deg=%.0f "
          "highest_secondary_lobe_dB_below_peak=%.1f"
          % (args.tag, len(summary), worst_off, -worst_side), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
