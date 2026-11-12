"""Export the RO4350B candidate for fabrication and for the mechanical team.

Reads the candidate's values from `design_ro4350b_final.yaml` (the same
numbers the solved HFSS design holds) and writes, under `fab/`:

    logper_ro4350b.kicad_pcb     both copper layers, board outline, notes
    drawing_mechanical.pdf/.png  dimensioned sheet for the mechanical team
    geometry_check.txt           extents of what was written, for comparison
                                 with the HFSS model's bounding boxes

Gerbers, DXF, a copper PDF and a STEP body are then produced from the
.kicad_pcb by KiCad's own `kicad-cli`, which also proves the file loads.

    python tools/export_fab.py

Frame: x runs from the wide base edge (x = 0) to the tip, y is across the
board, the coax lies on the FRONT copper (F.Cu). In the KiCad file the board
origin is placed at (ORIGIN_X, ORIGIN_Y) and y is flipped, as KiCad's y axis
points down.
"""
import math
import re
import textwrap
import uuid
from pathlib import Path

from shapely.geometry import Point, Polygon, box
from shapely.ops import unary_union

HERE = Path(__file__).resolve().parent.parent
SPEC = HERE / "design_ro4350b_final.yaml"
FAB = HERE / "fab"
ORIGIN_X, ORIGIN_Y = 40.0, 150.0
N = 15
NOTCH_R = 0.25          # half-hole at the tip for the 0.31 mm centre conductor


def read_vars():
    """Literal design variables from the spec (numbers in mm, or plain)."""
    text = SPEC.read_text(encoding="utf-8")
    block = text.split("\nvariables:\n", 1)[1].split("\nmaterials:", 1)[0]
    out = {}
    for line in block.splitlines():
        m = re.match(r"\s+(\w+):\s*\"?([-\d.]+)(mm)?\"?\s*(#.*)?$", line)
        if m:
            out[m.group(1)] = float(m.group(2))
    need = ("k_el", "tau", "feed_Wt", "feed_Wb", "pad_L", "pad_W", "bend_R",
            "tip_len", "pcb_Wtip", "h")
    missing = [n for n in need if n not in out]
    if missing:
        raise SystemExit(f"spec is missing literal variables: {missing}")
    return out


def geometry(v):
    k, tau = v["k_el"], v["tau"]
    arm1, we1, wr1, x1, sp1 = 60 * k, 30 * k, 5 * k, 18 * k, 30 * k
    centres, s = [x1], [1.0]
    for n in range(1, N):
        centres.append(centres[-1] + sp1 * s[-1])
        s.append(s[-1] * tau)
    length = centres[-1] + v["tip_len"]
    w_base = 2 * arm1 + 40.0
    coax_l = length - v["bend_R"]           # feed_cut = bend_R
    elements = [dict(n=i + 1, x=centres[i], arm=arm1 * s[i], end_w=we1 * s[i],
                     root_w=wr1 * s[i], front_side=(+1 if i % 2 == 0 else -1))
                for i in range(N)]

    def layer(front):
        feed_w = v["feed_Wt"] if front else v["feed_Wb"]
        feed_len = coax_l if front else length
        parts = [box(0, -feed_w / 2, feed_len, feed_w / 2),
                 box(coax_l - v["pad_L"], -v["pad_W"] / 2,
                     coax_l if front else length, v["pad_W"] / 2)]
        for e in elements:
            sign = e["front_side"] if front else -e["front_side"]
            parts.append(Polygon([(e["x"] - e["root_w"] / 2, 0),
                                  (e["x"] + e["root_w"] / 2, 0),
                                  (e["x"] + e["end_w"] / 2, sign * e["arm"]),
                                  (e["x"] - e["end_w"] / 2, sign * e["arm"])]))
        merged = unary_union(parts)
        if merged.geom_type != "Polygon" or merged.interiors:
            raise SystemExit(f"copper did not merge into one simple polygon: {merged.geom_type}")
        return merged

    notch = Point(length, 0).buffer(NOTCH_R, 32)
    outline = Polygon([(0, -w_base / 2), (length, -v["pcb_Wtip"] / 2),
                       (length, v["pcb_Wtip"] / 2), (0, w_base / 2)])
    front = layer(True)
    back = layer(False).difference(notch)
    if back.geom_type != "Polygon":
        raise SystemExit("back copper split after the notch cut")
    return dict(v=v, length=length, w_base=w_base, coax_l=coax_l, elements=elements,
                front=front, back=back, outline=outline)


def kxy(x, y):
    return "(xy %.4f %.4f)" % (ORIGIN_X + x, ORIGIN_Y - y)


def uid():
    return str(uuid.uuid4())


def poly_block(poly, layer):
    pts = list(poly.exterior.coords)[:-1]
    rows = ["\t\t\t" + " ".join(kxy(x, y) for x, y in pts[i:i + 4]) for i in range(0, len(pts), 4)]
    return ("\t(gr_poly\n\t\t(pts\n" + "\n".join(rows) + "\n\t\t)\n"
            "\t\t(stroke (width 0) (type solid))\n\t\t(fill solid)\n"
            f"\t\t(layer \"{layer}\")\n\t\t(uuid \"{uid()}\")\n\t)\n")


def line_block(a, b, layer, width=0.1):
    return ("\t(gr_line\n\t\t(start %.4f %.4f)\n\t\t(end %.4f %.4f)\n"
            "\t\t(stroke (width %.3f) (type default))\n\t\t(layer \"%s\")\n\t\t(uuid \"%s\")\n\t)\n"
            % (ORIGIN_X + a[0], ORIGIN_Y - a[1], ORIGIN_X + b[0], ORIGIN_Y - b[1],
               width, layer, uid()))


def arc_block(start, mid, end, layer, width=0.1):
    return ("\t(gr_arc\n\t\t(start %.4f %.4f)\n\t\t(mid %.4f %.4f)\n\t\t(end %.4f %.4f)\n"
            "\t\t(stroke (width %.3f) (type default))\n\t\t(layer \"%s\")\n\t\t(uuid \"%s\")\n\t)\n"
            % (ORIGIN_X + start[0], ORIGIN_Y - start[1], ORIGIN_X + mid[0], ORIGIN_Y - mid[1],
               ORIGIN_X + end[0], ORIGIN_Y - end[1], width, layer, uid()))


def text_block(text, x, y, layer, size=2.0):
    return ("\t(gr_text \"%s\"\n\t\t(at %.4f %.4f 0)\n\t\t(layer \"%s\")\n\t\t(uuid \"%s\")\n"
            "\t\t(effects\n\t\t\t(font\n\t\t\t\t(size %.2f %.2f)\n\t\t\t\t(thickness %.2f)\n\t\t\t)\n"
            "\t\t\t(justify left bottom)\n\t\t)\n\t)\n"
            % (text.replace('"', "'"), ORIGIN_X + x, ORIGIN_Y - y, layer, uid(),
               size, size, size * 0.15))


HEADER = '''(kicad_pcb
	(version 20240108)
	(generator "logper_export_fab")
	(generator_version "8.0")
	(general
		(thickness %(thick).3f)
		(legacy_teardrops no)
	)
	(paper "A3")
	(title_block
		(title "Log-periodic bow-tie array, 0.7-6 GHz, RO4350B 20 mil")
		(rev "candidate 2026-11-12")
		(comment 1 "Generated from design_ro4350b_final.yaml by tools/export_fab.py")
		(comment 2 "Coax side = F.Cu. No solder mask. Not yet reviewed for fabrication.")
	)
	(layers
		(0 "F.Cu" signal)
		(31 "B.Cu" signal)
		(32 "B.Adhes" user "B.Adhesive")
		(33 "F.Adhes" user "F.Adhesive")
		(34 "B.Paste" user)
		(35 "F.Paste" user)
		(36 "B.SilkS" user "B.Silkscreen")
		(37 "F.SilkS" user "F.Silkscreen")
		(38 "B.Mask" user)
		(39 "F.Mask" user)
		(40 "Dwgs.User" user "User.Drawings")
		(41 "Cmts.User" user "User.Comments")
		(42 "Eco1.User" user "User.Eco1")
		(43 "Eco2.User" user "User.Eco2")
		(44 "Edge.Cuts" user)
		(45 "Margin" user)
		(46 "B.CrtYd" user "B.Courtyard")
		(47 "F.CrtYd" user "F.Courtyard")
		(48 "B.Fab" user)
		(49 "F.Fab" user)
	)
	(setup
		(stackup
			(layer "F.Cu"
				(type "copper")
				(thickness 0.035)
			)
			(layer "dielectric 1"
				(type "core")
				(thickness %(h).3f)
				(material "RO4350B")
				(epsilon_r 3.66)
				(loss_tangent 0.0037)
			)
			(layer "B.Cu"
				(type "copper")
				(thickness 0.035)
			)
			(copper_finish "None")
			(dielectric_constraints no)
		)
		(pad_to_mask_clearance 0)
		(allow_soldermask_bridges_in_footprints no)
	)
	(net 0 "")
'''


def write_kicad(g):
    v = g["v"]
    length, w_base, w_tip = g["length"], g["w_base"], v["pcb_Wtip"]
    out = [HEADER % dict(thick=v["h"] + 0.07, h=v["h"])]
    out.append(poly_block(g["front"], "F.Cu"))
    out.append(poly_block(g["back"], "B.Cu"))
    # outline: trapezoid with a half-hole at the tip centre for the wire
    out.append(line_block((0, -w_base / 2), (length, -w_tip / 2), "Edge.Cuts"))
    out.append(line_block((length, -w_tip / 2), (length, -NOTCH_R), "Edge.Cuts"))
    out.append(arc_block((length, -NOTCH_R), (length - NOTCH_R, 0), (length, NOTCH_R), "Edge.Cuts"))
    out.append(line_block((length, NOTCH_R), (length, w_tip / 2), "Edge.Cuts"))
    out.append(line_block((length, w_tip / 2), (0, w_base / 2), "Edge.Cuts"))
    out.append(line_block((0, w_base / 2), (0, -w_base / 2), "Edge.Cuts"))
    # notes for whoever opens the board
    out.append(line_block((0, 0), (g["coax_l"], 0), "Dwgs.User", width=0.15))
    notes = [
        "COAX: Taoglas CAB.01061 (1.37 mm), jacket stripped, braid soldered to the F.Cu",
        "feed strip along this line from the base edge to x = %.2f mm." % g["coax_l"],
        "Centre conductor wraps the tip edge through the half-hole to the B.Cu strip.",
        "Board: RO4350B 0.508 mm, 1 oz copper, no solder mask. %.2f x %.2f mm." % (length, w_base),
        "No mounting holes or stiffener are in the simulated design.",
    ]
    for i, line in enumerate(notes):
        out.append(text_block(line, 0, -w_base / 2 - 10 - 4.2 * i, "Cmts.User", size=2.4))
    out.append(")\n")
    target = FAB / "logper_ro4350b.kicad_pcb"
    target.write_text("".join(out), encoding="utf-8", newline="\n")
    return target


def dim(ax, a, b, text, offset, color, horizontal=True):
    """A dimension line between two points with witness lines."""
    if horizontal:
        y = a[1] + offset
        ax.plot([a[0], a[0]], [a[1], y], color=color, lw=0.5)
        ax.plot([b[0], b[0]], [b[1], y], color=color, lw=0.5)
        ax.annotate("", (a[0], y), (b[0], y), arrowprops=dict(arrowstyle="<->", color=color, lw=0.8))
        ax.text((a[0] + b[0]) / 2, y + (1.6 if offset > 0 else -1.6), text, ha="center",
                va="bottom" if offset > 0 else "top", fontsize=8, color=color)
    else:
        x = a[0] + offset
        ax.plot([a[0], x], [a[1], a[1]], color=color, lw=0.5)
        ax.plot([b[0], x], [b[1], b[1]], color=color, lw=0.5)
        ax.annotate("", (x, a[1]), (x, b[1]), arrowprops=dict(arrowstyle="<->", color=color, lw=0.8))
        ax.text(x + (1.6 if offset > 0 else -1.6), (a[1] + b[1]) / 2, text, rotation=90,
                ha="left" if offset > 0 else "right", va="center", fontsize=8, color=color)


def write_drawing(g):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon as MplPoly

    v = g["v"]
    L, WB, WT = g["length"], g["w_base"], v["pcb_Wtip"]
    INK, MUTED, FRONT, BACK, COAX = "#0b0b0b", "#52514e", "#2a78d6", "#eb6834", "#008300"
    fig = plt.figure(figsize=(16.5, 11.7), facecolor="white")          # A3 landscape
    ax = fig.add_axes([0.03, 0.29, 0.66, 0.62])
    ax.set_aspect("equal")
    ax.add_patch(MplPoly(list(g["outline"].exterior.coords), closed=True, fc="#f4f3ef",
                         ec=INK, lw=1.2, zorder=1))
    ax.add_patch(MplPoly(list(g["back"].exterior.coords), closed=True, fc=BACK, ec="none",
                         alpha=0.45, zorder=2))
    ax.add_patch(MplPoly(list(g["front"].exterior.coords), closed=True, fc=FRONT, ec="none",
                         alpha=0.75, zorder=3))
    ax.plot([-14, g["coax_l"]], [0, 0], color=COAX, lw=2.0, zorder=4)
    ax.add_patch(plt.Rectangle((-26, -3.2), 12, 6.4, fc="#c9c8c2", ec=INK, lw=0.8, zorder=4))
    ax.text(-20, 5.5, "SMA(F)\nbulkhead", ha="center", va="bottom", fontsize=7.5, color=MUTED)
    ax.text(L * 0.45, 3.0, "coax on front (F.Cu) feed strip, braid soldered full length",
            fontsize=8, color=COAX, ha="center")
    ax.text(L + 3, WT / 2 + 7, "tip (beam direction →)", fontsize=8.5, color=INK, va="bottom")
    dim(ax, (0, -WB / 2), (L, -WB / 2), "%.2f" % L, -14, INK)
    dim(ax, (0, -WB / 2), (0, WB / 2), "%.2f" % WB, -34, INK, horizontal=False)
    dim(ax, (L, -WT / 2), (L, WT / 2), "%.2f" % WT, 24, INK, horizontal=False)
    e1 = g["elements"][0]
    dim(ax, (0, WB / 2), (e1["x"], WB / 2), "%.2f" % e1["x"], 9, MUTED)
    ax.plot([e1["x"], e1["x"]], [0, WB / 2], color=MUTED, lw=0.4, ls=(0, (3, 3)))
    ax.text(e1["x"] + 2, e1["arm"] * 0.55, "element 1", fontsize=7.5, color=MUTED)
    ax.set_xlim(-45, L + 45)
    ax.set_ylim(-WB / 2 - 28, WB / 2 + 22)
    ax.axis("off")
    ax.set_title("Front view (coax side). Blue = front copper, orange = back copper. "
                 "Dimensions in mm.", loc="left", fontsize=10, color=INK)

    # tip detail
    ad = fig.add_axes([0.03, 0.04, 0.30, 0.22])
    ad.set_aspect("equal")
    ad.add_patch(MplPoly(list(g["outline"].exterior.coords), closed=True, fc="#f4f3ef", ec=INK, lw=1.0))
    ad.add_patch(MplPoly(list(g["back"].exterior.coords), closed=True, fc=BACK, ec="none", alpha=0.45))
    ad.add_patch(MplPoly(list(g["front"].exterior.coords), closed=True, fc=FRONT, ec="none", alpha=0.75))
    ad.plot([L - 9, g["coax_l"]], [0, 0], color=COAX, lw=2.2)
    ad.set_xlim(L - 9, L + 2.2)
    ad.set_ylim(-4.2, 4.2)
    ad.set_xticks([])
    ad.set_yticks([])
    for s in ad.spines.values():
        s.set_color(MUTED)
    pad0 = g["coax_l"] - v["pad_L"]
    ad.annotate("pad %.1f wide" % v["pad_W"], (pad0 + 1.2, v["pad_W"] / 2), (L - 8.6, 3.5),
                fontsize=7.5, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
    ad.annotate("front strip ends %.2f before tip" % v["bend_R"], (g["coax_l"], -0.8),
                (L - 8.6, -3.7), fontsize=7.5, color=INK,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
    ad.annotate("half-hole Ø%.1f" % (2 * NOTCH_R), (L - NOTCH_R, 0), (L - 3.4, 2.3),
                fontsize=7.5, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
    ad.set_title("Detail: tip (about 12:1)", loc="left", fontsize=9, color=INK)

    # element table
    at = fig.add_axes([0.70, 0.29, 0.29, 0.60])
    at.axis("off")
    rows = [["#", "centre x", "arm", "end w", "root w", "front side"]]
    for e in g["elements"]:
        rows.append(["%d" % e["n"], "%.2f" % e["x"], "%.2f" % e["arm"], "%.2f" % e["end_w"],
                     "%.2f" % e["root_w"], "+y" if e["front_side"] > 0 else "-y"])
    table = at.table(cellText=rows[1:], colLabels=rows[0], loc="upper center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.0, 1.45)
    at.set_title("Bow-tie elements (mm). Arm length is measured from the\n"
                 "centreline; the back layer is the mirror image.", loc="left",
                 fontsize=9, color=INK)

    # notes
    an = fig.add_axes([0.36, 0.04, 0.63, 0.22])
    an.axis("off")
    notes = [
        "MATERIAL  Rogers RO4350B, 20 mil (0.508 mm) core, 1 oz (35 µm) copper both sides, no solder mask. "
        "Total thickness about 0.58 mm.",
        "FEED  Strips 1.60 mm wide on the centreline of both faces. Front strip %.2f mm long; back strip "
        "runs to the tip. Matching pad at the tip: %.2f mm wide." % (g["coax_l"], v["pad_W"]),
        "COAX  Taoglas CAB.01061: SMA(F) bulkhead + 300 mm of 1.37 mm micro-coax. Cut off the U.FL end, strip "
        "the jacket over the board length (braid 1.15 mm), solder the braid to the front strip. The SMA "
        "hangs off the base edge on the cable; it is not board-mounted.",
        "TIP  The 0.31 mm centre conductor leaves the coax %.2f mm before the tip, wraps the tip edge "
        "through the Ø%.1f half-hole and is soldered to the back strip. Keep it as short as possible."
        % (v["bend_R"], 2 * NOTCH_R),
        "NOT IN THE SIMULATED DESIGN  mounting holes, stiffener, enclosure, SMA body. The board is "
        "flexible at this size and needs support.",
        "SUPPORT GUIDANCE (not simulated)  Keep all metal and solid plastic away from the feed strips and "
        "the element arms. Preferred: low-permittivity foam bonded to the back face, or a frame touching "
        "only the outline. Any mounting holes or a tab behind the base edge should be re-simulated.",
        "HEIGHT  The soldered coax stands about 1.2 mm proud of the front face along the whole centreline "
        "(plus solder); the wire wrap adds about 0.3 mm beyond the tip edge and on the back face at the tip.",
        "RF (simulated)  First -10 dB crossing 0.685 GHz; S11 at or below -13 dB across the 902-928 MHz, "
        "1.71-1.99 GHz, 2.4 GHz and 5.15-5.9 GHz bands; beam along +x (toward the tip).",
    ]
    y = 1.0
    for line in notes:
        wrapped = textwrap.wrap(line, 150)
        an.text(0.0, y, "\n".join(wrapped), fontsize=7.6, color=INK, va="top")
        y -= 0.062 * len(wrapped) + 0.03
    fig.text(0.03, 0.965, "Log-periodic bow-tie array on RO4350B 20 mil — mechanical sheet "
             "(candidate, 2026-11-12, from the HFSS model; not a released drawing)",
             fontsize=12, color=INK)
    pdf, png = FAB / "drawing_mechanical.pdf", FAB / "drawing_mechanical.png"
    fig.savefig(pdf)
    fig.savefig(png, dpi=130)
    plt.close(fig)
    return pdf, png


def main():
    FAB.mkdir(exist_ok=True)
    g = geometry(read_vars())
    board = write_kicad(g)
    pdf, png = write_drawing(g)
    fb, bb = g["front"].bounds, g["back"].bounds
    check = [
        "board  length %.4f  base width %.4f  tip width %.4f  thickness %.3f"
        % (g["length"], g["w_base"], g["v"]["pcb_Wtip"], g["v"]["h"]),
        "front copper bbox x %.4f..%.4f  y %.4f..%.4f  vertices %d  area %.2f mm2"
        % (fb[0], fb[2], fb[1], fb[3], len(g["front"].exterior.coords) - 1, g["front"].area),
        "back  copper bbox x %.4f..%.4f  y %.4f..%.4f  vertices %d  area %.2f mm2"
        % (bb[0], bb[2], bb[1], bb[3], len(g["back"].exterior.coords) - 1, g["back"].area),
        "narrowest copper: element %d root %.3f mm" % (N, g["elements"][-1]["root_w"]),
        "front strip ends %.3f mm before the tip (gap to the tip edge)" % g["v"]["bend_R"],
    ]
    (FAB / "geometry_check.txt").write_text("\n".join(check) + "\n", encoding="utf-8")
    print("\n".join(check))
    print("wrote", board.name, pdf.name, png.name)


if __name__ == "__main__":
    main()
