"""Offline geometry preview — see the model before AEDT ever launches.

**Why this exists.** The Review gate (ADR 0003) is a human looking at the built
Math model in the AEDT UI, and the 2026-08-17/18 campaign proved it is carrying
the correctness of this whole tool almost single-handedly: four defects found by
eye on a model that had passed `validate_spec`, `precheck`,
`compile_spec --dry-run`, snapshot verification and `validate_simple`. Four for
four caught by a person; four for four missed by every machine check.

The problem is not that the gate is human. The problem is **what it costs to
reach it**. Today the shortest path from a spec to something a person can look
at runs through a licence check, an AEDT launch, a full compile and a desktop
window — minutes at best, and every correction round pays it again. The 2x2 run
spent four Review-gate repair cycles that way. That is the dominant wall-clock
term between "the parameters are locked" and "there is geometry in front of me",
and none of it is EM.

So: render the same spec to a picture in about a second, with no licence, no
desktop and no pyAEDT. Three orthographic views straight off the bounding boxes
`model_checks` already computes.

What it is for, in order:

1. **The agent looks at its own model before showing anyone.** It can read the
   PNG back. A build defect found here costs one edit instead of one rebuild.
2. **A first Review gate that happens in the conversation**, in seconds, so the
   AEDT gate is confirmation rather than discovery.
3. **Correction rounds get cheap.** Edit, re-render, look. No relaunch.

Of the four defects the maintainer caught by eye, three are visible here:
notches missing from three of four patches (count the cut marks), ports drawn
in the wrong plane (they are labelled with their plane and their integration
direction), and an airbox flush against the model (the clearance is annotated
per face). The fourth — sheets left without a material — is not geometric at
all, so it is reported in the footer instead.

**It never pretends.** An op whose bounds cannot be resolved is not drawn and is
listed by name under "not drawn". A preview that silently omits geometry would
be the exact confident-but-wrong failure this repo keeps paying for; a preview
that says "3 ops not drawn: FeedArc, Horn, LoftBody" is honest and still useful.

Matplotlib is the only non-stdlib import, and it is imported lazily so that
`hfss_spec` still loads without it.
"""

from __future__ import annotations

from typing import Optional

from .expressions import ExpressionError, Value, evaluate, resolve_all
from .model_checks import (C0, CLEARANCE_FRACTION, _num, _selector_object,
                           _target_frequency, bounding_box, port_sheets)
from .units import UnitError

# Views, as (name, horizontal axis, vertical axis, axis viewed along).
VIEWS = (("plan  (xy)", 0, 1, 2),
         ("front (xz)", 0, 2, 1),
         ("side  (yz)", 1, 2, 0))

AXES = "xyz"

# Anything whose name or library says "metal". Kept broad on purpose: the point
# is to make an *unassigned* conductor stand out, so a false conductor reading
# is cheaper than a false "no material".
CONDUCTORS = ("pec", "copper", "gold", "silver", "aluminum", "aluminium",
              "brass", "tin", "nickel", "perfect conductor")

TRANSPARENT = ("vacuum", "air")

STYLE = {
    "conductor":  {"fc": "#c9821f", "ec": "#7a4d0b", "alpha": 0.85, "z": 3},
    "dielectric": {"fc": "#7fb2d9", "ec": "#31688e", "alpha": 0.30, "z": 2},
    "air":        {"fc": "none",    "ec": "#9aa0a6", "alpha": 1.00, "z": 1},
    "port":       {"fc": "#d43fa0", "ec": "#7a1a5c", "alpha": 0.75, "z": 5},
    "unassigned": {"fc": "#e05252", "ec": "#8a1f1f", "alpha": 0.35, "z": 4},
    # A boolean tool: shown as a dashed ghost so an inset notch or a via cut is
    # visible as an *absence* rather than as a solid block on top of the patch.
    "tool":       {"fc": "none",    "ec": "#444444", "alpha": 1.00, "z": 6},
}


def resolve_scope(spec) -> dict[str, Value]:
    """`spec.variable_scope()` resolved to `Value`s, tolerantly.

    `variable_scope()` hands back raw expressions; every consumer has to
    resolve them, and the geometry helpers assume `Value`s. Passing the raw
    table through instead surfaces as an `AttributeError` deep inside
    `evaluate` rather than as a finding — which is what happened the first time
    this module was pointed at a real spec.

    Tolerant on purpose, mirroring `validate._check_variables`: a preview of a
    spec with one bad variable should draw the other twelve objects and list
    the casualty, not refuse to draw anything. Looking at a partly-broken model
    is exactly when a picture helps most.
    """
    table = spec.variable_scope()
    try:
        return resolve_all(table)
    except ExpressionError:
        partial: dict[str, Value] = {}
        for name, raw in table.items():
            try:
                partial[name] = evaluate(raw, partial)
            except (ExpressionError, UnitError, AttributeError, TypeError):
                continue
        return partial


def _material_class(spec, op, is_port: bool) -> str:
    """Which drawing style an op gets, and the material question it answers."""
    if is_port:
        return "port"
    name = (op.material or "").strip()
    if not name:
        return "unassigned"
    lowered = name.lower()
    defined = getattr(spec, "materials", {}) or {}
    entry = defined.get(name)
    library = getattr(entry, "library", None)
    if library:
        lowered = library.lower()
    if any(metal in lowered for metal in CONDUCTORS):
        return "conductor"
    if any(clear in lowered for clear in TRANSPARENT):
        return "air"
    return "dielectric"


def _integration_arrow(exc, scope) -> Optional[tuple[list[float], list[float]]]:
    """`(from, to)` of the integration line in metres, or None."""
    line = getattr(exc, "integration_line", None)
    if line is None:
        return None
    a = getattr(getattr(line, "from_", None) or getattr(line, "start", None),
                "point", None)
    b = getattr(getattr(line, "to", None) or getattr(line, "end", None),
                "point", None)
    if not a or not b or len(a) != 3 or len(b) != 3:
        return None
    start = [_num(v, scope) for v in a]
    end = [_num(v, scope) for v in b]
    if any(v is None for v in start + end):
        return None
    return start, end                              # type: ignore[return-value]


def collect(spec, scope: dict[str, Value]) -> dict:
    """Everything the drawing needs, as plain data. Testable without matplotlib.

    Returns `{"bodies", "undrawn", "ports", "boundary", "clearance", "notes"}`.
    `bodies` entries are `{"name", "bbox", "style", "material", "cuts"}` where
    `cuts` counts the boolean subtractions that consumed this object — the
    number that goes wrong when an array's elements are not all built alike.
    """
    port_objects = port_sheets(spec)

    # Two very different kinds of "consumed", and conflating them draws the
    # wrong picture both ways.
    #
    # `ghost` — a subtract/intersect tool. Its volume is REMOVED. Drawing it
    # solid would show an inset notch as a block sitting on top of the patch it
    # cut, which is the opposite of what happened, so it is drawn as a dashed
    # outline: the absence, marked.
    #
    # `merged` — a unite member. Its volume STAYS; it just stops being its own
    # object and inherits the first operand's material. So it is drawn normally
    # and excused from the missing-material note, because blank is correct for
    # it. Ghosting these instead made patch-2400's feed line vanish from the
    # drawing, which is exactly the silent omission this module must not do.
    cuts: dict[str, int] = {}
    ghost: set[str] = set()
    merged: set[str] = set()
    for op in getattr(spec, "geometry", []) or []:
        if op.op in ("subtract", "intersect"):
            cuts[op.name] = cuts.get(op.name, 0) + len(op.tools or [])
            if not op.keep_tools:
                ghost.update(op.tools or [])
        if op.op == "unite":
            merged.update(op.with_ or [])

    bodies, undrawn = [], []
    for op in getattr(spec, "geometry", []) or []:
        if op.op in ("subtract", "intersect", "unite"):
            continue                     # booleans mutate a body already listed
        bbox = bounding_box(op, scope)
        if bbox is None:
            undrawn.append(f"{op.name} ({op.op})")
            continue
        bodies.append({
            "name": op.name,
            "bbox": bbox,
            "style": ("tool" if op.name in ghost
                      else _material_class(spec, op, op.name in port_objects)),
            "material": op.material or "(none)",
            "cuts": cuts.get(op.name, 0),
            "consumed": op.name in ghost or op.name in merged,
        })

    ports = []
    for exc in getattr(spec, "excitations", []) or []:
        arrow = _integration_arrow(exc, scope)
        ports.append({
            "name": getattr(exc, "name", "?"),
            "type": getattr(exc, "type", "?"),
            "on": _selector_object(getattr(exc, "on", None)),
            "arrow": arrow,
        })

    host = None
    for boundary in getattr(spec, "boundaries", []) or []:
        if boundary.type == "radiation":
            host = _selector_object(getattr(boundary, "on", None))
            break

    return {
        "bodies": bodies,
        "undrawn": undrawn,
        "ports": ports,
        "boundary": host,
        "clearance": clearance_report(spec, scope, bodies, host, port_objects),
        "notes": _notes(spec, bodies, undrawn),
    }


def clearance_report(spec, scope, bodies, host, port_objects) -> list[dict]:
    """Per-face gap between the radiation boundary and what it encloses.

    The same measurement `model_checks.radiation_clearance` warns on, but
    reported for **every** face rather than only the tightest, and in
    wavelengths as well as millimetres. A person reading a picture wants to see
    which face is tight, not just that one is.
    """
    if host is None:
        return []
    outer = next((b["bbox"] for b in bodies if b["name"] == host), None)
    inner = [b["bbox"] for b in bodies
             if b["name"] != host and b["name"] not in port_objects]
    if outer is None or not inner:
        return []
    f0 = _target_frequency(spec)
    lam = C0 / f0 if f0 else None
    # A flush face is legitimate exactly when a wave port sits on it — a wave
    # port is a 2D port on the outer surface of the solution domain, so the
    # boundary has to be flush there. A lumped port is internal and buys no
    # such exemption. Same rule as `model_checks.radiation_clearance`; stated
    # again here because a picture that flags a correct wave-port design as
    # TIGHT on every render is a picture people stop reading.
    has_wave_port = any(getattr(e, "type", None) == "wave_port"
                        for e in (getattr(spec, "excitations", []) or []))
    lo = [min(b[i][0] for b in inner) for i in range(3)]
    hi = [max(b[i][1] for b in inner) for i in range(3)]
    out = []
    for i in range(3):
        for face, gap in (("-" + AXES[i], lo[i] - outer[i][0]),
                          ("+" + AXES[i], outer[i][1] - hi[i])):
            flush = abs(gap) <= 1e-12
            if lam is None:
                verdict = None
            elif flush and has_wave_port:
                verdict = "wave-port face"
            elif gap >= CLEARANCE_FRACTION * lam * 0.99:
                verdict = True
            else:
                verdict = False
            out.append({
                "face": face,
                "gap_mm": gap * 1e3,
                "gap_lambda": (gap / lam) if lam else None,
                "ok": verdict,
            })
    return out


def _notes(spec, bodies, undrawn) -> list[str]:
    """Short lines under the drawing: the things a picture cannot show."""
    notes: list[str] = []

    unassigned = [b["name"] for b in bodies
                  if b["style"] == "unassigned" and not b.get("consumed")]
    if unassigned:
        notes.append(
            "NO MATERIAL on %d object(s): %s — a sheet with no material is "
            "legal and solves as nothing. Caught by eye at a 2026-08-18 gate."
            % (len(unassigned), ", ".join(unassigned[:6])))

    cut_counts = sorted({b["cuts"] for b in bodies if b["cuts"]})
    if len(cut_counts) > 1:
        by_count: dict[int, list[str]] = {}
        for b in bodies:
            if b["cuts"]:
                by_count.setdefault(b["cuts"], []).append(b["name"])
        detail = "; ".join(
            "%d cut(s): %s" % (n, ", ".join(sorted(by_count[n])[:4]))
            for n in cut_counts)
        notes.append(
            "UNEVEN CUTS — %s. In a repeated array every element should carry "
            "the same boolean count." % detail)

    planes = {}
    for exc in getattr(spec, "excitations", []) or []:
        on = _selector_object(getattr(exc, "on", None))
        for op in getattr(spec, "geometry", []) or []:
            if op.name == on and op.op == "sheet":
                planes.setdefault(op.plane or "?", []).append(op.name)
    if len(planes) > 1:
        notes.append(
            "MIXED PORT PLANES: %s — ports feeding the same way should share a "
            "plane; a port normal to the wrong axis still solves and still "
            "reports an impedance, just not the antenna's."
            % ", ".join("%s=%s" % (k, ",".join(v)) for k, v in planes.items()))

    if undrawn:
        notes.append("NOT DRAWN (%d): %s — bounds not resolvable offline; this "
                     "preview is incomplete for them."
                     % (len(undrawn), ", ".join(undrawn[:8])))
    return notes


def render(spec, scope: dict[str, Value], out_path, dpi: int = 130) -> dict:
    """Draw the three views to `out_path`. Returns the `collect()` data."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    data = collect(spec, scope)
    bodies = data["bodies"]

    fig, axes = plt.subplots(1, 3, figsize=(16.5, 5.6))
    fig.suptitle(
        "%s  —  recipe %s  —  offline preview, no AEDT"
        % (getattr(spec, "name", "?"), getattr(spec, "recipe", "?")),
        fontsize=12, y=0.985)

    for ax, (title, hi_ax, vi_ax, _flat) in zip(axes, VIEWS):
        for body in sorted(bodies, key=lambda b: STYLE[b["style"]]["z"]):
            bbox = body["bbox"]
            x0, x1 = bbox[hi_ax]
            y0, y1 = bbox[vi_ax]
            st = STYLE[body["style"]]
            w, h = (x1 - x0) * 1e3, (y1 - y0) * 1e3
            # A body seen edge-on has zero extent; draw it as a line so a sheet
            # in the wrong plane is visible rather than invisible.
            ax.add_patch(Rectangle(
                (x0 * 1e3, y0 * 1e3), w or 1e-9, h or 1e-9,
                facecolor=st["fc"], edgecolor=st["ec"], alpha=st["alpha"],
                linewidth=1.6 if (w == 0 or h == 0) else 0.9,
                linestyle="--" if body["style"] == "tool" else "-",
                zorder=st["z"],
                hatch="//" if body["style"] == "unassigned" else None))
            if body["cuts"]:
                ax.plot([(x0 + x1) / 2 * 1e3], [(y0 + y1) / 2 * 1e3],
                        marker="x", color="#2b2b2b", markersize=6,
                        zorder=st["z"] + 1)

        for port in data["ports"]:
            if port["arrow"]:
                start, end = port["arrow"]
                ax.annotate(
                    "", xy=(end[hi_ax] * 1e3, end[vi_ax] * 1e3),
                    xytext=(start[hi_ax] * 1e3, start[vi_ax] * 1e3),
                    arrowprops=dict(arrowstyle="->", color="#7a1a5c", lw=1.4),
                    zorder=9)

        ax.set_title(title, fontsize=10, loc="left")
        ax.set_xlabel("%s (mm)" % AXES[hi_ax], fontsize=8)
        ax.set_ylabel("%s (mm)" % AXES[vi_ax], fontsize=8)
        ax.set_aspect("equal", adjustable="datalim")
        ax.tick_params(labelsize=7)
        ax.grid(True, linewidth=0.3, alpha=0.4)
        ax.autoscale_view()

    # A legend, because a picture nobody can decode is a picture nobody uses.
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch as LegendPatch
    present = {b["style"] for b in data["bodies"]}
    labels = [("conductor", "conductor"), ("dielectric", "dielectric"),
              ("air", "air / boundary"), ("port", "port sheet"),
              ("unassigned", "NO MATERIAL"), ("tool", "cut tool (removed)")]
    handles = [LegendPatch(facecolor=STYLE[k]["fc"], edgecolor=STYLE[k]["ec"],
                           alpha=STYLE[k]["alpha"], label=text,
                           linestyle="--" if k == "tool" else "-")
               for k, text in labels if k in present]
    if any(b["cuts"] for b in data["bodies"]):
        handles.append(Line2D([], [], marker="x", color="#2b2b2b", lw=0,
                              label="carries boolean cuts"))
    if handles:
        fig.legend(handles=handles, loc="upper right", ncol=len(handles),
                   fontsize=7.5, frameon=False, bbox_to_anchor=(0.995, 0.945))

    footer = []
    if data["clearance"]:
        tight = [c for c in data["clearance"] if c["ok"] is False]
        flush = [c for c in data["clearance"] if c["ok"] == "wave-port face"]
        if tight:
            footer.append("radiation clearance TIGHT on " + ", ".join(
                "%s %.1f mm (%.2f lambda)" % (c["face"], c["gap_mm"],
                                              c["gap_lambda"] or 0)
                for c in tight))
        else:
            footer.append("radiation clearance OK on all six faces "
                          "(>= lambda0/3)")
        if flush:
            footer.append("flush on " + ", ".join(c["face"] for c in flush)
                          + " — legitimate: a wave port terminates there")
    footer += data["notes"]

    if footer:
        fig.text(0.012, 0.015, "\n".join("• " + line for line in footer),
                 fontsize=7.4, va="bottom", family="monospace", color="#333333")
        fig.subplots_adjust(bottom=0.10 + 0.035 * len(footer), top=0.86)
    else:
        fig.subplots_adjust(bottom=0.12, top=0.86)

    fig.savefig(str(out_path), dpi=dpi)
    plt.close(fig)
    return data


def text_report(data: dict) -> str:
    """The same findings as prose, for a terminal or a log."""
    lines = ["objects drawn: %d" % len(data["bodies"])]
    for body in data["bodies"]:
        bbox = body["bbox"]
        extent = " x ".join("%.3f" % ((hi - lo) * 1e3) for lo, hi in bbox)
        lines.append("  %-22s %-11s %s mm  cuts=%d"
                     % (body["name"], body["style"], extent, body["cuts"]))
    for port in data["ports"]:
        lines.append("  port %-16s %-11s on %s"
                     % (port["name"], port["type"], port["on"]))
    for c in data["clearance"]:
        mark = ("wave-port face" if c["ok"] == "wave-port face"
                else "ok " if c["ok"] else "TIGHT")
        lines.append("  clearance %-3s %8.2f mm  %s"
                     % (c["face"], c["gap_mm"], mark))
    for note in data["notes"]:
        lines.append("  ! " + note)
    return "\n".join(lines)
