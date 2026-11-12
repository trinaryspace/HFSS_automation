"""Draw the report figures for one solved variant. Offline: reads saved CSVs.

    python tools/report_plots.py <tag> [<baseline tag>]

Inputs under results/<tag>/ (written by src/30_variant_qa.py and
src/33_pattern_cuts.py):
    s11.csv, AgentReadout_cutE.csv, AgentReadout_cutH.csv,
    AgentReadout_AntennaParams.csv
Outputs under results/<tag>/:
    report_s11.png        S11 with the bands of interest marked
    report_patterns.png   E- and H-plane cuts at each field frequency

The baseline curve defaults to the FR-4 replica (results/s11_comparison.csv).
"""
import csv
import math
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RESULTS = Path(__file__).resolve().parent.parent / "results"
BLUE, ORANGE = "#2a78d6", "#eb6834"
SURFACE, INK, MUTED, GRID, BAND = "#fcfcfb", "#0b0b0b", "#52514e", "#dddcd6", "#ecebe6"
BANDS = [("ISM 900", 0.902, 0.928), ("cell 1.7-2.0", 1.71, 1.99),
         ("ISM 2.4", 2.40, 2.4835), ("Wi-Fi 5.15-5.9", 5.15, 5.895)]


def load_s11(path, col=1):
    rows = list(csv.reader(open(path, encoding="utf-8")))[1:]
    return [float(r[0]) for r in rows], [float(r[col]) for r in rows]


def style(ax):
    ax.set_facecolor(SURFACE)
    ax.grid(color=GRID, lw=0.6)
    ax.tick_params(colors=MUTED, labelsize=8.5)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)


def plot_s11(tag, label, baseline):
    f, v = load_s11(RESULTS / tag / "s11.csv")
    fig, ax = plt.subplots(figsize=(10.5, 5.2), facecolor=SURFACE)
    style(ax)
    for name, lo, hi in BANDS:
        ax.axvspan(lo, hi, color=BAND, zorder=0)
        ax.text((lo + hi) / 2, 0.4, name, ha="center", va="bottom", fontsize=8, color=MUTED)
    if baseline:
        bf, bv, blabel = baseline
        ax.plot(bf, bv, lw=1.3, color=ORANGE, label=blabel, zorder=2)
    ax.plot(f, v, lw=2.2, color=BLUE, label=label, zorder=3)
    ax.axhline(-10, lw=1, color=MUTED, ls=(0, (4, 3)), zorder=1)
    ax.text(0.42, -9.6, "-10 dB", fontsize=8.5, color=MUTED)
    ax.set_xlim(0.4, 6.5)
    ax.set_ylim(-35, 3)
    ax.set_xlabel("Frequency (GHz)", color=MUTED)
    ax.set_ylabel("|S11| (dB)", color=MUTED)
    ax.set_title("S11 with the bands of interest shaded", loc="left", fontsize=11, color=INK)
    ax.legend(loc="lower left", fontsize=9, frameon=False)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.92, bottom=0.11)
    out = RESULTS / tag / "report_s11.png"
    fig.savefig(out, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    return out


def load_cut(path):
    rows = [r for r in csv.reader(open(path, encoding="utf-8-sig")) if any(c.strip() for c in r)]
    named = []
    for i, text in enumerate(rows[0]):
        phi = re.search(r"Phi='([-\d.]+)deg'", text)
        theta = re.search(r"Theta='([-\d.]+)deg'", text)
        if phi and theta:
            named.append((i, float(theta.group(1)), float(phi.group(1))))
    return {float(r[0]): [(th, ph, float(r[i])) for i, th, ph in named] for r in rows[1:]}


def plot_patterns(tag):
    e_path = RESULTS / tag / "AgentReadout_cutE.csv"
    h_path = RESULTS / tag / "AgentReadout_cutH.csv"
    if not (e_path.exists() and h_path.exists()):
        return None
    e, h = load_cut(e_path), load_cut(h_path)
    freqs = sorted(e)
    fig, axes = plt.subplots(2, len(freqs), figsize=(2.55 * len(freqs), 5.4),
                             facecolor=SURFACE, sharex=True, sharey=True)
    for j, f in enumerate(freqs):
        e_pts = sorted({(p if p <= 180 else p - 360): v for t, p, v in e[f] if p < 359.9}.items())
        h_map = {}
        for t, p, v in h[f]:
            a = (90.0 - t) if p < 90.0 else (90.0 + t)
            h_map[round(((a + 180.0) % 360.0) - 180.0, 3)] = v
        h_pts = sorted(h_map.items())
        for i, (pts, plane) in enumerate(((e_pts, "E-plane (board plane)"),
                                          (h_pts, "H-plane (normal to board)"))):
            ax = axes[i][j]
            style(ax)
            ax.plot([a for a, _ in pts], [v for _, v in pts], lw=1.8, color=BLUE)
            ax.axvline(0, lw=0.8, color=MUTED, ls=(0, (2, 3)))
            ax.set_xlim(-180, 180)
            ax.set_ylim(-30, 10)
            ax.set_xticks([-90, 0, 90])     # +/-180 labels collide between panels
            if i == 0:
                ax.set_title("%.0f GHz" % f, fontsize=10, color=INK)
            if j == 0:
                ax.set_ylabel("%s\ndirectivity (dBi)" % plane, fontsize=8.5, color=MUTED)
            if i == 1:
                ax.set_xlabel("angle from tip (deg)", fontsize=8.5, color=MUTED)
    fig.suptitle("Far-field cuts; the dotted line is straight off the tip",
                 x=0.01, ha="left", fontsize=11, color=INK)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.88, bottom=0.10, wspace=0.08, hspace=0.12)
    out = RESULTS / tag / "report_patterns.png"
    fig.savefig(out, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    return out


def cut_points(e, h, f):
    """Both cuts as [(angle from the tip in degrees, dBi)], -180..180."""
    e_pts = sorted({(p if p <= 180 else p - 360): v for t, p, v in e[f] if p < 359.9}.items())
    h_map = {}
    for t, p, v in h[f]:
        a = (90.0 - t) if p < 90.0 else (90.0 + t)
        h_map[round(((a + 180.0) % 360.0) - 180.0, 3)] = v
    return e_pts, sorted(h_map.items())


def plot_polar(tag):
    """The same two cuts as polar plots: the tip direction is at the top."""
    e_path = RESULTS / tag / "AgentReadout_cutE.csv"
    h_path = RESULTS / tag / "AgentReadout_cutH.csv"
    if not (e_path.exists() and h_path.exists()):
        return None
    e, h = load_cut(e_path), load_cut(h_path)
    freqs = sorted(e)
    floor = -25.0
    fig, axes = plt.subplots(2, len(freqs), figsize=(2.6 * len(freqs), 6.0),
                             facecolor=SURFACE, subplot_kw={"projection": "polar"})
    for j, f in enumerate(freqs):
        for i, pts in enumerate(cut_points(e, h, f)):
            ax = axes[i][j]
            ax.set_facecolor(SURFACE)
            ang = [math.radians(a) for a, _ in pts] + [math.radians(pts[0][0])]
            val = [max(v, floor) for _, v in pts] + [max(pts[0][1], floor)]
            ax.plot(ang, val, lw=1.8, color=BLUE)
            ax.set_theta_zero_location("N")       # tip direction at the top
            ax.set_theta_direction(-1)
            ax.set_ylim(floor, 10)
            ax.set_yticks([-20, -10, 0, 10])
            ax.set_yticklabels(["-20", "-10", "0", "10"], fontsize=6.5, color=MUTED)
            ax.set_xticks([math.radians(a) for a in (0, 90, 180, 270)])
            ax.set_xticklabels(["tip", "90", "back", "-90"], fontsize=7.5, color=MUTED)
            ax.grid(color=GRID, lw=0.6)
            ax.spines["polar"].set_color(GRID)
            if i == 0:
                ax.set_title("%.0f GHz" % f, fontsize=10, color=INK, pad=12)
    fig.text(0.012, 0.70, "E-plane\n(board plane)", fontsize=9, color=MUTED, va="center")
    fig.text(0.012, 0.27, "H-plane\n(normal to board)", fontsize=9, color=MUTED, va="center")
    fig.suptitle("Radiation pattern, total directivity in dBi (rings every 10 dB)",
                 x=0.012, ha="left", fontsize=11, color=INK)
    fig.subplots_adjust(left=0.10, right=0.965, top=0.86, bottom=0.04, wspace=0.35, hspace=0.25)
    out = RESULTS / tag / "report_patterns_polar.png"
    fig.savefig(out, dpi=150, facecolor=SURFACE)
    plt.close(fig)
    return out


def main(argv):
    tag = argv[0]
    label = argv[2] if len(argv) > 2 else tag
    baseline = None
    if len(argv) > 1 and argv[1] != "fr4":
        bf, bv = load_s11(RESULTS / argv[1] / "s11.csv")
        baseline = (bf, bv, argv[1])
    elif (RESULTS / "s11_comparison.csv").exists():
        bf, bv = load_s11(RESULTS / "s11_comparison.csv")
        baseline = (bf, bv, "FR-4 original (HFSS replica)")
    print("wrote", plot_s11(tag, label, baseline))
    print("wrote", plot_patterns(tag))
    print("wrote", plot_polar(tag))
    table = RESULTS / tag / "AgentReadout_AntennaParams.csv"
    if table.exists():
        rows = list(csv.reader(open(table, encoding="utf-8-sig")))
        hdr = [h.strip() for h in rows[0]]
        col = lambda name: next(i for i, h in enumerate(hdr) if h.startswith(name))
        print("freq_GHz  directivity_dBi  rad_eff  gain_dBi  realized_gain_dBi")
        for r in rows[1:]:
            db = lambda name: 10 * math.log10(float(r[col(name)]))
            print("%7.0f  %14.2f  %7.3f  %8.2f  %16.2f" % (
                float(r[0]), db("PeakDirectivity"), float(r[col("RadiationEfficiency")]),
                db("PeakGain"), db("PeakRealizedGain")))


if __name__ == "__main__":
    main(sys.argv[1:])
