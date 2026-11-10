"""Read S11 and the radiation numbers, compare with CST and the measurement,
plot, and report the Result QA signals locked in Clarification.

Route policy (SKILL.md, EC#6): `read_results.apply_route_arounds()` BEFORE
constructing Hfss, then one `ReadoutSession` for the whole stage. The route
token for each signal lands in `results/state/readouts.txt`.

References are read from the source repo (not copied here):
  CST   .../CST_SIM/2_WITH_FEED_COAX_FR4_V1/RESULTS/SIM_LOG_PERIODIC_COAX_FEED_WITHOUT_CASE.s1p
  MEAS  .../MEASUREMENTS/2_WITH_FEED_COAX_FR4_V1/MEAS_LOG_PERIODIC_WITHOUT_CASE.s1p
Set LOGPER_REF to the repo's PROJECT_FILES directory if it has moved.

The radiation block is indicative in phase A: CST's exported far-field data
belongs to the WITH-CASE model. It is read best-effort and never fails the
stage; an unreadable number is reported as unreadable.

Usage (workspace root):  python src/09_plots_qa.py
Prints one Verification line:  PASS: plots_qa <counts>
"""

import csv
import math
import os
import sys

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

RESULTS = ws_common.RESULTS
STATE = ws_common.STATE
S11_SWEEP = "Setup1 : Sweep1"
FIELD_SWEEP = "Setup1 : FieldPts"
SPHERE = "FF_Sphere"

REF_ROOT = os.environ.get("LOGPER_REF") or os.path.join(
    os.path.expanduser("~"), "Repos", "LogPer_Antenna",
    "RF---PCB-Log-Periodic-Antenna--0.8-6-GHz-", "PROJECT_FILES")
CST_S1P = os.path.join(REF_ROOT, "CST_SIM", "2_WITH_FEED_COAX_FR4_V1", "RESULTS",
                       "SIM_LOG_PERIODIC_COAX_FEED_WITHOUT_CASE.s1p")
MEAS_S1P = os.path.join(REF_ROOT, "MEASUREMENTS", "2_WITH_FEED_COAX_FR4_V1",
                        "MEAS_LOG_PERIODIC_WITHOUT_CASE.s1p")

# QA thresholds locked in Clarification (state.md, signals 3-6).
EDGE_TOL_PCT = 5.0
SEGMENTS = ((1, 2), (2, 3), (3, 4), (4, 5), (5, 6))
SEGMENT_TOL_DB = 3.0
WORST_IN_BAND_DB = -5.0
DIRECTIVITY_RANGE = (6.0, 7.0)
EFFICIENCY_RANGE = (0.6, 0.8)
# CST with-case values at 1..6 GHz, for the indicative radiation table.
CST_CASE = {"directivity_dbi": [6.93, 6.55, 6.13, 6.73, 6.82, 6.91],
            "rad_eff": [0.767, 0.740, 0.629, 0.705, 0.668, 0.693]}

COLORS = {"hfss": "#2a78d6", "cst": "#eb6834", "meas": "#1baf7a"}
SURFACE, INK, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#dddcd6"


def load_s1p(path):
    """(freq_GHz, s11_dB) from a one-port Touchstone file, MA or DB format."""
    freqs, db, fmt, scale = [], [], "MA", 1.0
    with open(path, encoding="cp1252") as handle:
        for line in handle:
            s = line.strip()
            if not s or s.startswith("!"):
                continue
            if s.startswith("#"):
                parts = s.upper().split()
                scale = {"HZ": 1e-9, "KHZ": 1e-6, "MHZ": 1e-3, "GHZ": 1.0}[parts[1]]
                fmt = parts[3]
                continue
            a = s.split()
            freqs.append(float(a[0]) * scale)
            value = float(a[1])
            db.append(value if fmt == "DB" else 20 * math.log10(max(value, 1e-12)))
    return freqs, db


def interp(xs, ys, x):
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return ys[-1]
    lo, hi = 0, len(xs) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if xs[mid] <= x:
            lo = mid
        else:
            hi = mid
    t = (x - xs[lo]) / (xs[hi] - xs[lo])
    return ys[lo] + t * (ys[hi] - ys[lo])


def first_crossing(freqs, db, threshold=-10.0):
    """First frequency where the curve falls to `threshold`, interpolated."""
    for i in range(1, len(db)):
        if db[i] <= threshold < db[i - 1]:
            f0, v0 = freqs[i - 1], db[i - 1]
            return f0 + (threshold - v0) * (freqs[i] - f0) / (db[i] - v0)
    return None


def segment_mean(freqs, db, lo, hi):
    values = [v for f, v in zip(freqs, db) if lo <= f <= hi]
    return sum(values) / len(values) if values else None


def read_antenna_table(hfss):
    """{'freq': [...], '<quantity>': [...]} from an Antenna Parameters table.

    Its own CreateReport, because `read_results.report_spec` knows the modal
    and far-field forms only. Returns ({}, note) when anything fails.
    """
    name = "AgentReadout_AntennaParams"
    quantities = ["PeakDirectivity", "RadiationEfficiency", "PeakRealizedGain",
                  "PeakGain"]
    try:
        module = hfss.odesign.GetModule("ReportSetup")
        if name not in [str(n) for n in (module.GetAllReportNames() or [])]:
            module.CreateReport(
                name, "Antenna Parameters", "Data Table", FIELD_SWEEP,
                ["Context:=", SPHERE], ["Freq:=", ["All"]],
                ["X Component:=", "Freq", "Y Component:=", quantities], [])
        path = hfss.post.export_report_to_file(RESULTS, name, ".csv")
        if not (isinstance(path, str) and os.path.isfile(path)):
            path = os.path.join(RESULTS, name + ".csv")
        with open(path, encoding="utf-8-sig", newline="") as handle:
            rows = [r for r in csv.reader(handle) if any(c.strip() for c in r)]
        header = [c.strip() for c in rows[0]]
        table = {"freq": [float(r[0]) for r in rows[1:]]}
        for quantity in quantities:
            col = next((i for i, h in enumerate(header) if h.startswith(quantity)), None)
            if col is not None:
                table[quantity] = [float(r[col]) for r in rows[1:]]
        return table, "report-export %s" % os.path.basename(path)
    except Exception as exc:                 # noqa: BLE001 - reported, not raised
        return {}, "%s: %s" % (type(exc).__name__, str(exc)[:200])


def plot_s11(hfss_curve, refs, edge, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 5.2), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    series = [("meas", "Measured", refs.get("meas")),
              ("cst", "CST", refs.get("cst")),
              ("hfss", "HFSS", hfss_curve)]
    for key, label, curve in series:
        if not curve:
            continue
        f, v = curve
        keep = [(x, y) for x, y in zip(f, v) if 0.4 <= x <= 6.5]
        ax.plot([p[0] for p in keep], [p[1] for p in keep], lw=2.0,
                color=COLORS[key], label=label, zorder=3 if key == "hfss" else 2)
        ax.annotate(label, (keep[-1][0], keep[-1][1]), xytext=(6, 0),
                    textcoords="offset points", va="center", fontsize=9, color=INK)
    ax.axhline(-10.0, lw=1, color=MUTED, ls=(0, (4, 3)), zorder=1)
    ax.annotate("-10 dB", (0.42, -10.0), xytext=(0, 4), textcoords="offset points",
                fontsize=8.5, color=MUTED)
    ax.set_xlim(0.4, 6.5)
    ax.set_ylim(-30, 1)
    ax.set_xlabel("Frequency (GHz)", color=MUTED)
    ax.set_ylabel("|S11| (dB)", color=MUTED)
    title = "Log-periodic bow-tie array, coax feed, no case: S11"
    if edge:
        title += "  (HFSS -10 dB edge %.3f GHz)" % edge
    ax.set_title(title, loc="left", fontsize=11, color=INK)
    ax.grid(color=GRID, lw=0.6)
    ax.tick_params(colors=MUTED, labelsize=9)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.legend(loc="lower left", fontsize=9, frameon=False)
    fig.subplots_adjust(left=0.08, right=0.92, top=0.92, bottom=0.11)
    fig.savefig(out, dpi=150, facecolor=SURFACE)
    plt.close(fig)


def main():
    hfss = ws_common.attach()
    os.makedirs(RESULTS, exist_ok=True)
    session = read_results.ReadoutSession(
        hfss, recycle=ws_common.recycle_desktop, export_dir=RESULTS,
        state_dir=STATE)
    readout = session.read("dB(S(1,1))", sweep=S11_SWEEP)
    lines = [read_results.verdict_line("s11", readout)]

    if not readout.y:
        read_results.write_readouts(STATE, lines)
        print("FAIL: plots_qa s11 unreadable route=%s" % readout.route, flush=True)
        return 1

    freqs = [float(x) for x in readout.x]
    if max(freqs) > 1e6:                     # x came back in Hz
        freqs = [f / 1e9 for f in freqs]
    s11 = [float(v) for v in readout.y]

    refs, ref_notes = {}, []
    for key, path in (("cst", CST_S1P), ("meas", MEAS_S1P)):
        if os.path.isfile(path):
            refs[key] = load_s1p(path)
        else:
            ref_notes.append("%s reference missing at %s" % (key, path))

    # --- QA 3: passivity -------------------------------------------------
    s11_max = max(s11)
    passive = s11_max <= 0.05
    print("QA3 passivity: max S11 %.3f dB -> %s"
          % (s11_max, "PASS" if passive else "FAIL"), flush=True)

    # --- QA 4: band edge -------------------------------------------------
    edge = first_crossing(freqs, s11)
    edge_ok = None
    if edge and "cst" in refs:
        cst_edge = first_crossing(*refs["cst"])
        meas_edge = first_crossing(*refs["meas"]) if "meas" in refs else None
        delta = 100.0 * (edge - cst_edge) / cst_edge
        edge_ok = abs(delta) <= EDGE_TOL_PCT
        print("QA4 band edge (first -10 dB): HFSS %.3f GHz, CST %.3f GHz "
              "(%+.1f%%), measured %s -> %s"
              % (edge, cst_edge, delta,
                 "%.3f GHz" % meas_edge if meas_edge else "n/a",
                 "PASS" if edge_ok else "FAIL"), flush=True)
    else:
        print("QA4 band edge: HFSS %s, no CST reference" % edge, flush=True)

    # --- QA 5: in-band level --------------------------------------------
    rows, seg_ok = [], True
    for lo, hi in SEGMENTS:
        mine = segment_mean(freqs, s11, lo, hi)
        cst = segment_mean(*refs["cst"], lo, hi) if "cst" in refs else None
        meas = segment_mean(*refs["meas"], lo, hi) if "meas" in refs else None
        ok = None if cst is None else abs(mine - cst) <= SEGMENT_TOL_DB
        seg_ok = seg_ok and (ok is not False)
        rows.append((lo, hi, mine, cst, meas, ok))
        print("QA5 %d-%d GHz mean S11: HFSS %.2f dB, CST %s, measured %s -> %s"
              % (lo, hi, mine,
                 "%.2f dB" % cst if cst is not None else "n/a",
                 "%.2f dB" % meas if meas is not None else "n/a",
                 "n/a" if ok is None else ("PASS" if ok else "FAIL")), flush=True)
    band = [(f, v) for f, v in zip(freqs, s11) if 1.0 <= f <= 6.0]
    worst_f, worst = max(band, key=lambda p: p[1])
    worst_ok = worst <= WORST_IN_BAND_DB
    print("QA5 worst in-band S11 (1-6 GHz): %.2f dB at %.3f GHz -> %s"
          % (worst, worst_f, "PASS" if worst_ok else "FAIL"), flush=True)

    # --- deliverables: table + plot -------------------------------------
    table = os.path.join(RESULTS, "s11_comparison.csv")
    with open(table, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["freq_GHz", "hfss_dB", "cst_dB", "measured_dB"])
        for f, v in zip(freqs, s11):
            writer.writerow(["%.5f" % f, "%.4f" % v,
                             "%.4f" % interp(*refs["cst"], f) if "cst" in refs else "",
                             "%.4f" % interp(*refs["meas"], f) if "meas" in refs else ""])
    plot = os.path.join(RESULTS, "s11_vs_cst_meas.png")
    plot_s11((freqs, s11), refs, edge, plot)

    # --- QA 6: radiation, indicative ------------------------------------
    antenna, note = read_antenna_table(hfss)
    rad_ok = None
    if antenna.get("PeakDirectivity"):
        lines.append("antenna_params verdict=read route=report-export points=%d note=%s"
                     % (len(antenna["freq"]), note))
        rad_ok = True
        for i, f in enumerate(antenna["freq"]):
            d_lin = antenna["PeakDirectivity"][i]
            d_dbi = 10 * math.log10(d_lin) if d_lin > 0 else float("nan")
            eff = antenna.get("RadiationEfficiency", [None] * (i + 1))[i]
            ok = (DIRECTIVITY_RANGE[0] <= d_dbi <= DIRECTIVITY_RANGE[1]
                  and (eff is None or EFFICIENCY_RANGE[0] <= eff <= EFFICIENCY_RANGE[1]))
            rad_ok = rad_ok and ok
            idx = int(round(f)) - 1
            ref = ("CST with case %.2f dBi / %.2f"
                   % (CST_CASE["directivity_dbi"][idx], CST_CASE["rad_eff"][idx])
                   if 0 <= idx < 6 else "")
            print("QA6 %.0f GHz: peak directivity %.2f dBi, rad. efficiency %s (%s) -> %s"
                  % (f, d_dbi, "%.3f" % eff if eff is not None else "n/a", ref,
                     "in range" if ok else "OUT OF RANGE"), flush=True)
    else:
        lines.append("antenna_params verdict=unreadable route=report-export note=%s" % note)
        print("QA6 radiation: unreadable - %s" % note, flush=True)

    read_results.write_readouts(STATE, lines)
    for extra in ref_notes:
        print("note:", extra, flush=True)

    line = ("PASS: plots_qa points=%d route=%s passive=%s edge=%s edge_ok=%s "
            "segments_ok=%s worst_in_band=%.2fdB worst_ok=%s radiation_ok=%s plot=%s table=%s"
            % (len(s11), readout.route, passive,
               "%.3fGHz" % edge if edge else "none", edge_ok, seg_ok, worst,
               worst_ok, rad_ok, os.path.basename(plot), os.path.basename(table)))
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
