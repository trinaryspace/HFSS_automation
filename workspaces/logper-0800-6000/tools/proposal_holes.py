"""Draw the PROPOSED mounting-hole layout on the candidate board. Draws only:
it changes neither the KiCad board nor the HFSS design.

    python tools/proposal_holes.py     ->  fab/proposal_mounting_holes.png

Four M3 clearance holes on copper-free ears outside the slanted edges, one
pair beside element 3 and one beside element 6, the two pairs the same
distance behind and ahead of the turntable axis at the board centre.
"""
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon as MplPoly
from shapely.geometry import LineString, Point

import export_fab

HOLE_D = 3.2        # M3 clearance
EAR_R = 5.0         # substrate around the hole centre
OUTSET = 5.0        # hole centre outside the present edge, measured in y
DX = 36.5           # each pair's distance from the axis along the board


def main():
    g = export_fab.geometry(export_fab.read_vars())
    L, WB, WT = g["length"], g["w_base"], g["v"]["pcb_Wtip"]
    slope = (WB - WT) / 2 / L
    cx = L / 2
    half = lambda x: WB / 2 - slope * x
    holes = [(cx + sx * DX, sy * (half(cx + sx * DX) + OUTSET))
             for sx in (-1, 1) for sy in (1, -1)]
    outline = g["outline"]
    for x, y in holes:
        inward = (x, y - math.copysign(OUTSET + EAR_R, y))
        outline = outline.union(LineString([(x, y), inward]).buffer(EAR_R, 48))
    copper = g["front"].union(g["back"])

    INK, MUTED, FRONT, BACK, NEW = "#0b0b0b", "#52514e", "#2a78d6", "#eb6834", "#008300"
    fig, ax = plt.subplots(figsize=(15, 11), facecolor="white")
    ax.set_aspect("equal")
    ax.add_patch(MplPoly(list(outline.exterior.coords), closed=True, fc="#d9f0d9", ec=NEW, lw=1.4))
    ax.add_patch(MplPoly(list(g["outline"].exterior.coords), closed=True, fc="#f4f3ef", ec=INK, lw=1.0))
    ax.add_patch(MplPoly(list(g["back"].exterior.coords), closed=True, fc=BACK, ec="none", alpha=0.45))
    ax.add_patch(MplPoly(list(g["front"].exterior.coords), closed=True, fc=FRONT, ec="none", alpha=0.75))
    for e in g["elements"][:8]:
        ax.text(e["x"], -e["front_side"] * 4.5, str(e["n"]), ha="center", va="center",
                fontsize=8, color=INK)
    # the hole trapezoid and the axis
    order = [holes[0], holes[2], holes[3], holes[1]]
    ax.add_patch(MplPoly(order, closed=True, fc="none", ec=NEW, lw=0.9, ls=(0, (5, 4))))
    ax.plot([cx], [0], marker="+", ms=22, mew=1.8, color=INK)
    ax.add_patch(Circle((cx, 0), 4, fc="none", ec=INK, lw=1.2))
    ax.annotate("turntable axis\nx = %.1f, on the centreline" % cx, (cx, 0), (cx - 14, -22),
                fontsize=9.5, color=INK, ha="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
    for x, y in holes:
        ax.add_patch(Circle((x, y), HOLE_D / 2, fc="white", ec=INK, lw=1.2))
        clear = copper.distance(Point(x, y)) - HOLE_D / 2
        r = math.hypot(x - cx, y)
        ax.text(x + 8, y + (7 if y > 0 else -7),
                "x = %.1f, y = %+.1f\n%.0f mm from axis\n%.1f mm hole edge to copper"
                % (x, y, r, clear), fontsize=8.5, color=INK, va="center")
    # dimensions
    top = WB / 2 + 12
    for x in (cx - DX, cx, cx + DX):
        ax.plot([x, x], [half(x) + 12 if x != cx else 4, top + 3], color=MUTED, lw=0.5, ls=(0, (3, 3)))
    for a, b in ((cx - DX, cx), (cx, cx + DX)):
        ax.annotate("", (a, top), (b, top), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.8))
        ax.text((a + b) / 2, top + 1.5, "%.1f" % DX, ha="center", fontsize=9, color=INK)
    for x, side in ((holes[0][0], -1), (holes[2][0], 1)):
        y = half(x) + OUTSET
        xo = x + side * 0  # dimension drawn at the hole's own x, offset for legibility
        xd = x - 22 if side < 0 else x + 62
        ax.plot([x, xd], [y, y], color=MUTED, lw=0.5)
        ax.plot([x, xd], [-y, -y], color=MUTED, lw=0.5)
        ax.annotate("", (xd, y), (xd, -y), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.8))
        ax.text(xd - 1.5, 30 if side < 0 else -30, "%.1f" % (2 * y), rotation=90, ha="right",
                va="center", fontsize=9, color=INK)
    ax.text(0, -WB / 2 - 12,
            "Green = added substrate (ears, no copper): a tab %.0f mm wide with a rounded end, hole centre "
            "%.0f mm outside the present edge.\nHoles Ø%.1f (M3 clearance). Numbers 1-8 count the elements "
            "from the wide base. Blue = front copper, orange = back copper.\nPROPOSAL ONLY - not simulated, "
            "not in the KiCad board." % (2 * EAR_R, OUTSET, HOLE_D), fontsize=9.5, color=INK, va="top")
    ax.set_title("Proposed mounting holes: pairs beside elements 3 and 6, equal distance either side "
                 "of the axis (dimensions in mm)", loc="left", fontsize=12, color=INK)
    ax.set_xlim(-30, L + 30)
    ax.set_ylim(-WB / 2 - 32, WB / 2 + 22)
    ax.axis("off")
    out = export_fab.FAB / "proposal_mounting_holes.png"
    fig.savefig(out, dpi=120, bbox_inches="tight")
    for x, y in holes:
        print("hole x=%.2f y=%+.2f  r_axis=%.1f  edge_to_copper=%.2f"
              % (x, y, math.hypot(x - cx, y), copper.distance(Point(x, y)) - HOLE_D / 2))
    print("overall width with ears %.1f mm (was %.2f)" % (outline.bounds[3] - outline.bounds[1], WB))
    print("wrote", out)


if __name__ == "__main__":
    main()
