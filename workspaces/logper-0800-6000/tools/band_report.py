"""Score saved S11 curves against the bands the user cares about. Offline.

Reads `results/<tag>/s11.csv` (written by `src/30_variant_qa.py`) and prints,
per tag: the low band edge, every span above -10 dB inside 0.8-6 GHz, and
the worst and mean S11 inside each band of interest.

Bands (user, 2026-11-12): 800/900 MHz ISM, 1.8/1.9 GHz cell, 2.4 GHz ISM,
5.1-5.9 GHz Wi-Fi, "and any other cell signals in there". Band edges below
are the usual US allocations and are my reading of that, not the user's
numbers.

    python tools/band_report.py v3_it2v coarse_k121 ...
"""
import csv
import sys
from pathlib import Path

RESULTS = Path(__file__).resolve().parent.parent / "results"
BANDS = [
    ("cell 700/850 (0.70-0.89)", 0.70, 0.894),
    ("ISM 902-928", 0.902, 0.928),
    ("cell 1.7/1.9 (1.71-1.99)", 1.71, 1.99),
    ("cell 2.1 DL (2.11-2.20)", 2.11, 2.20),
    ("cell 2.3 (2.30-2.40)", 2.30, 2.40),
    ("ISM 2.40-2.4835", 2.40, 2.4835),
    ("cell 2.5-2.69", 2.496, 2.69),
    ("cell 3.3-3.8", 3.3, 3.8),
    ("Wi-Fi 5.15-5.895", 5.15, 5.895),
]


def load(tag):
    rows = list(csv.reader(open(RESULTS / tag / "s11.csv", encoding="utf-8")))[1:]
    return [(float(a), float(b)) for a, b in rows]


def spans(rows, lo=0.8, hi=6.0, limit=-10.0):
    out, start = [], None
    for f, v in rows:
        if not lo <= f <= hi:
            continue
        if v > limit:
            if start is None:
                start, peak = f, (f, v)
            if v > peak[1]:
                peak = (f, v)
            last = f
        elif start is not None:
            out.append((start, last, peak))
            start = None
    if start is not None:
        out.append((start, last, peak))
    return out


def main(tags):
    for tag in tags:
        rows = load(tag)
        edge = next((f for (f0, v0), (f, v) in zip(rows, rows[1:]) if v <= -10 < v0), None)
        print(f"\n== {tag}: first -10 dB crossing {edge} GHz; S11 at 6.00 GHz "
              f"{min(rows, key=lambda r: abs(r[0] - 6.0))[1]:.1f} dB")
        sp = spans(rows)
        print("   above -10 dB inside 0.8-6 GHz: " + (", ".join(
            f"{a:.2f}-{b:.2f} (peak {pv:.1f} at {pf:.2f})" for a, b, (pf, pv) in sp) or "nowhere"))
        for name, lo, hi in BANDS:
            band = [v for f, v in rows if lo <= f <= hi]
            if not band:
                continue
            flag = "" if max(band) <= -10 else "   <-- above -10 dB"
            print(f"   {name:28s} worst {max(band):6.1f} dB  mean {sum(band)/len(band):6.1f} dB{flag}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["v3_it2v"])
