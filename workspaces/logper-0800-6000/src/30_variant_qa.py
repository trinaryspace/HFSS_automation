"""Read one substrate variant's results and compare the variants.

A variant is the design selected by HFSS_WS_DESIGN at its current nominal
variable values, labelled by --tag (for example `ro4350b_A`). The stage reads
S11 and the antenna parameters into `results/<tag>/`, prints the same summary
numbers the FR-4 QA uses, and redraws `results/s11_variants.png` from every
variant read so far plus the FR-4 design's HFSS curve.

There is no CST or measured reference for the Rogers variants; the FR-4 HFSS
result is the comparison.

Usage (workspace root):
    set HFSS_WS_DESIGN=LogPer_RO4350B_20mil
    python src/30_variant_qa.py --tag ro4350b_A --label "RO4350B, feed 4 mm"
Prints one Verification line:  PASS: variant_qa tag=<tag> ...
"""

import argparse
import csv
import json
import math
import os
import sys

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

RESULTS = ws_common.RESULTS
S11_SWEEP = "Setup1 : Sweep1"
FIELD_SWEEP = "Setup1 : FieldPts"
SPHERE = "FF_Sphere"
SEGMENTS = ((1, 2), (2, 3), (3, 4), (4, 5), (5, 6))
QUANTITIES = ["PeakDirectivity", "RadiationEfficiency", "PeakRealizedGain", "PeakGain"]
# Fixed colour per variant (validated categorical order: blue, orange, aqua).
STYLE = {"fr4": ("#2a78d6", "FR-4 1.5 mm (replica)"),
         "ro4350b_A": ("#eb6834", None), "ro4350b_B": ("#1baf7a", None)}
# Later variants take the palette's next slots in order (yellow, magenta,
# green, violet, red) - never a generated hue.
EXTRA = ["#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
SURFACE, INK, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#dddcd6"


def first_crossing(freqs, db, threshold=-10.0):
    for i in range(1, len(db)):
        if db[i] <= threshold < db[i - 1]:
            f0, v0 = freqs[i - 1], db[i - 1]
            return f0 + (threshold - v0) * (freqs[i] - f0) / (db[i] - v0)
    return None


def segment_mean(freqs, db, lo, hi):
    values = [v for f, v in zip(freqs, db) if lo <= f <= hi]
    return sum(values) / len(values)


def read_antenna_table(hfss, out_dir):
    name = "AgentReadout_AntennaParams"
    try:
        module = hfss.odesign.GetModule("ReportSetup")
        if name not in [str(n) for n in (module.GetAllReportNames() or [])]:
            module.CreateReport(
                name, "Antenna Parameters", "Data Table", FIELD_SWEEP,
                ["Context:=", SPHERE], ["Freq:=", ["All"]],
                ["X Component:=", "Freq", "Y Component:=", QUANTITIES], [])
        path = hfss.post.export_report_to_file(out_dir, name, ".csv")
        if not (isinstance(path, str) and os.path.isfile(path)):
            path = os.path.join(out_dir, name + ".csv")
        with open(path, encoding="utf-8-sig", newline="") as handle:
            rows = [r for r in csv.reader(handle) if any(c.strip() for c in r)]
        header = [c.strip() for c in rows[0]]
        table = {"freq": [float(r[0]) for r in rows[1:]]}
        for quantity in QUANTITIES:
            col = next(i for i, h in enumerate(header) if h.startswith(quantity))
            table[quantity] = [float(r[col]) for r in rows[1:]]
        return table, "report-export"
    except Exception as exc:                 # noqa: BLE001 - reported, not raised
        return {}, "%s: %s" % (type(exc).__name__, str(exc)[:200])


def load_curves():
    """{tag: (label, freqs, s11)} for the FR-4 design and every variant read."""
    curves = {}
    fr4 = os.path.join(RESULTS, "s11_comparison.csv")
    if os.path.isfile(fr4):
        rows = list(csv.reader(open(fr4, encoding="utf-8")))[1:]
        curves["fr4"] = (STYLE["fr4"][1], [float(r[0]) for r in rows],
                         [float(r[1]) for r in rows])
    for tag in sorted(os.listdir(RESULTS)):
        meta = os.path.join(RESULTS, tag, "variant.json")
        if not os.path.isfile(meta):
            continue
        info = json.load(open(meta, encoding="utf-8"))
        rows = list(csv.reader(open(os.path.join(RESULTS, tag, "s11.csv"),
                                    encoding="utf-8")))[1:]
        curves[tag] = (info["label"], [float(r[0]) for r in rows],
                       [float(r[1]) for r in rows])
    return curves


def plot(curves, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 5.2), facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    # Colour follows the variant, in the palette's fixed order: a variant keeps
    # its slot however many are added after it. The baseline and the newest
    # variant are drawn heavier so the eye finds "before" and "now" first.
    order = [t for t in curves if t != "fr4"]
    newest = order[-1] if order else None
    for tag, (label, freqs, s11) in curves.items():
        if tag in STYLE:
            color = STYLE[tag][0]
        else:
            color = EXTRA[(order.index(tag)) % len(EXTRA)]
        heavy = tag in ("fr4", newest)
        ax.plot(freqs, s11, lw=2.2 if heavy else 1.2, color=color, label=label,
                alpha=1.0 if heavy else 0.75, zorder=3 if heavy else 2)
    ax.axhline(-10.0, lw=1, color=MUTED, ls=(0, (4, 3)), zorder=1)
    ax.annotate("-10 dB", (0.42, -10.0), xytext=(0, 4), textcoords="offset points",
                fontsize=8.5, color=MUTED)
    ax.set_xlim(0.4, 6.5)
    ax.set_ylim(-30, 1)
    ax.set_xlabel("Frequency (GHz)", color=MUTED)
    ax.set_ylabel("|S11| (dB)", color=MUTED)
    ax.set_title("Log-periodic bow-tie array: S11 by substrate (HFSS)",
                 loc="left", fontsize=11, color=INK)
    ax.grid(color=GRID, lw=0.6)
    ax.tick_params(colors=MUTED, labelsize=9)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.legend(loc="lower left", fontsize=9, frameon=False)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.92, bottom=0.11)
    fig.savefig(out, dpi=150, facecolor=SURFACE)
    plt.close(fig)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--tag", required=True)
    parser.add_argument("--label", required=True)
    args = parser.parse_args(argv)

    hfss = ws_common.attach()
    out_dir = os.path.join(RESULTS, args.tag)
    os.makedirs(out_dir, exist_ok=True)
    session = read_results.ReadoutSession(
        hfss, recycle=ws_common.recycle_desktop, export_dir=out_dir,
        state_dir=ws_common.STATE)
    readout = session.read("dB(S(1,1))", sweep=S11_SWEEP)
    if not readout.y:
        print("FAIL: variant_qa tag=%s s11 unreadable route=%s"
              % (args.tag, readout.route), flush=True)
        return 1
    freqs = [float(x) for x in readout.x]
    if max(freqs) > 1e6:
        freqs = [f / 1e9 for f in freqs]
    s11 = [float(v) for v in readout.y]

    with open(os.path.join(out_dir, "s11.csv"), "w", encoding="utf-8", newline="") as h:
        writer = csv.writer(h)
        writer.writerow(["freq_GHz", "s11_dB"])
        writer.writerows(["%.5f" % f, "%.4f" % v] for f, v in zip(freqs, s11))
    json.dump({"tag": args.tag, "label": args.label, "design": ws_common.DESIGN},
              open(os.path.join(out_dir, "variant.json"), "w", encoding="utf-8"))

    edge = first_crossing(freqs, s11)
    band = [(f, v) for f, v in zip(freqs, s11) if 1.0 <= f <= 6.0]
    worst_f, worst = max(band, key=lambda p: p[1])
    frac10 = sum(1 for _, v in band if v <= -10.0) / len(band)
    print("%s [%s] design=%s" % (args.tag, args.label, ws_common.DESIGN), flush=True)
    print("  first -10 dB crossing: %s; max S11 %.2f dB; worst 1-6 GHz %.2f dB at "
          "%.3f GHz; fraction of 1-6 GHz at or below -10 dB: %.2f"
          % ("%.3f GHz" % edge if edge else "none", max(s11), worst, worst_f, frac10),
          flush=True)
    print("  per-GHz mean S11 (dB): " + ", ".join(
        "%d-%d: %.2f" % (lo, hi, segment_mean(freqs, s11, lo, hi))
        for lo, hi in SEGMENTS), flush=True)
    # dips below -10 dB under 1.2 GHz, to see where the low band edge sits
    lows = [(f, v) for f, v in zip(freqs, s11) if f <= 1.3]
    f_min, v_min = min(lows, key=lambda p: p[1])
    print("  deepest S11 below 1.3 GHz: %.2f dB at %.3f GHz" % (v_min, f_min), flush=True)

    antenna, note = read_antenna_table(hfss, out_dir)
    if antenna:
        for i, f in enumerate(antenna["freq"]):
            d = 10 * math.log10(antenna["PeakDirectivity"][i])
            g = 10 * math.log10(antenna["PeakGain"][i])
            rg = 10 * math.log10(antenna["PeakRealizedGain"][i])
            print("  %.0f GHz: directivity %.2f dBi, rad. efficiency %.3f, gain %.2f dBi, "
                  "realized gain %.2f dBi"
                  % (f, d, antenna["RadiationEfficiency"][i], g, rg), flush=True)
    else:
        print("  antenna parameters unreadable: %s" % note, flush=True)

    curves = load_curves()
    out = os.path.join(RESULTS, "s11_variants.png")
    plot(curves, out)
    print("PASS: variant_qa tag=%s route=%s points=%d edge=%s worst_in_band=%.2fdB "
          "antenna=%s curves=%s plot=%s"
          % (args.tag, readout.route, len(s11), "%.3fGHz" % edge if edge else "none",
             worst, "read" if antenna else "unreadable", sorted(curves),
             os.path.basename(out)), flush=True)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
        sys.exit(1)
