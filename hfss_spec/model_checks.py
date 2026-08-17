"""Relational checks: properties of the model as a whole, not of one field.

Every other check in `validate.py` asks whether a field is well-formed — is this
a length, does that name resolve, is the sweep bracketing the target. The
2026-08-17 review found that **all three real defects in six machine-clean specs
were relational**, and none of those checks could see them:

- a radiation boundary too close to what it is bounding (4 of 6 specs);
- a lumped port whose sheet bears no relation to the conductor it bridges (S4);
- a feed network terminating into an impedance its elements were not matched to
  (S7 — not implemented here; see the module note at the bottom).

The false-green rate was 50%: six specs passed `validate_spec`, `precheck` and
`compile_spec --dry-run` with zero errors and zero escape hatches, and three of
them were wrong. These checks close the two cheapest of those holes.

**Why these two and not more prompting.** Both encode a geometric relation the
author cannot satisfy by adjusting a number it already controls — you cannot tune
your way to a lambda0/3 clearance without actually moving the boundary. That
property matters: cell S11 showed that a limit written as prose (the
`precheck-tolerances.json` note on coupled-line synthesis) gets read, quoted, and
ignored. A check that computes is not a check that advises.
"""

from __future__ import annotations

import math
from typing import Optional

from .expressions import ExpressionError, Value, evaluate
from .units import DIMENSIONLESS, FREQUENCY, LENGTH, UnitError

C0 = 299792458.0

# Radiation-boundary clearance, as a fraction of the free-space wavelength.
# lambda0/3 is the maintainer's stated rule of thumb (2026-08-17 review). It is
# not arbitrary: of six authored specs only the horn met it, while four chose
# lambda0/4 and one chose lambda0/10 — independently, without coordinating. That
# is a missing default rather than five mistakes.
CLEARANCE_FRACTION = 1.0 / 3.0

# A lumped port sheet should be about as wide as the conductor it bridges. S4
# drew a 4 mm ribbon across a 2 mm gap on a 1 mm wire: the port then presents a
# cross-section unrelated to the antenna's, so the impedance it reports is not
# the antenna's. 1.5x leaves room for legitimate flare without admitting 4x.
PORT_WIDTH_RATIO = 1.5

# Ops that produce a solid or sheet we can bound. Boolean results take the name
# of their first operand, which is already in the table by the time they run.
_BOUNDED_OPS = {"box", "sheet", "cylinder"}


def _num(raw, scope, dimension=LENGTH) -> Optional[float]:
    """Evaluate `raw` to an SI float of the expected dimension, or None."""
    if raw is None:
        return None
    try:
        value = evaluate(raw, scope)
    except (ExpressionError, UnitError):
        return None
    if not isinstance(value, Value) or value.dimension != dimension:
        return None
    return value.si


def _span(origin, size, axis: int, scope) -> Optional[tuple[float, float]]:
    """`(lo, hi)` for one axis of a box-like op, in metres."""
    o = _num(origin[axis] if origin and len(origin) > axis else None, scope)
    if o is None:
        return None
    s = _num(size[axis] if size and len(size) > axis else None, scope)
    if s is None:
        return None
    return (o, o + s) if s >= 0 else (o + s, o)


def bounding_box(op, scope) -> Optional[list[tuple[float, float]]]:
    """Axis-aligned bounds for one geometry op, or None when not computable.

    Deliberately conservative: an op whose bounds cannot be resolved returns
    None and is skipped rather than guessed at. A check that invents a bound
    would produce exactly the confident-but-wrong verdict this module exists to
    prevent.
    """
    if op.op == "box":
        spans = [_span(op.origin, op.size, i, scope) for i in range(3)]
        return spans if all(s is not None for s in spans) else None

    if op.op == "sheet":
        plane = (op.plane or "xy").lower()
        axes = {"xy": (0, 1, 2), "xz": (0, 2, 1), "yz": (1, 2, 0)}.get(plane)
        if axes is None or not op.origin:
            return None
        a, b, flat = axes
        # A sheet's `size` is stated in axis order and carries two entries.
        first = _span([op.origin[a]], [op.size[0]] if op.size else None, 0, scope)
        second = _span([op.origin[b]],
                       [op.size[1]] if op.size and len(op.size) > 1 else None,
                       0, scope)
        at = _num(op.origin[flat] if len(op.origin) > flat else None, scope)
        if first is None or second is None or at is None:
            return None
        out: list[Optional[tuple[float, float]]] = [None, None, None]
        out[a], out[b], out[flat] = first, second, (at, at)
        return out                                    # type: ignore[return-value]

    if op.op == "cylinder":
        centre = [_num(c, scope) for c in (op.origin or [])]
        radius = _num(getattr(op, "radius", None), scope)
        height = _num(getattr(op, "height", None), scope)
        if len(centre) != 3 or any(c is None for c in centre) or radius is None:
            return None
        axis = {"x": 0, "y": 1, "z": 2}.get((getattr(op, "axis", "z") or "z").lower(), 2)
        if height is None:
            return None
        out = []
        for i in range(3):
            if i == axis:
                lo, hi = centre[i], centre[i] + height
                out.append((min(lo, hi), max(lo, hi)))
            else:
                out.append((centre[i] - radius, centre[i] + radius))
        return out

    return None


def _selector_object(selector) -> Optional[str]:
    """The object a selector names, whichever shape it uses.

    A radiation boundary is normally written `{outer_faces: AirBox}`, not
    `{object: AirBox}` — reading only `object` made the clearance check silently
    inert on every real spec, which is precisely the false-negative this module
    was written to stop. Check every naming field the schema offers.
    """
    if selector is None:
        return None
    if isinstance(selector, str):
        return selector
    for field in ("object", "outer_faces", "face_of"):
        name = getattr(selector, field, None)
        if name:
            return name
    return None


def _integration_axis(excitation, scope) -> Optional[int]:
    """Which axis the integration line runs along (0/1/2), or None.

    This is the current direction, so the port's extent along it is the gap it
    bridges and must not be judged as a width.
    """
    line = getattr(excitation, "integration_line", None)
    if line is None:
        return None
    a = getattr(getattr(line, "from_", None) or getattr(line, "start", None),
                "point", None)
    b = getattr(getattr(line, "to", None) or getattr(line, "end", None),
                "point", None)
    if not a or not b or len(a) != 3 or len(b) != 3:
        return None
    deltas = []
    for i in range(3):
        lo, hi = _num(a[i], scope), _num(b[i], scope)
        deltas.append(abs(hi - lo) if lo is not None and hi is not None else 0.0)
    widest = max(deltas)
    return deltas.index(widest) if widest > 0 else None


def _target_frequency(spec) -> Optional[float]:
    """The frequency the clearance is judged at, in Hz."""
    target = getattr(spec, "target", None)
    if target is not None and getattr(target, "quantity", "") in (
            "resonant_frequency", "center_frequency", "cutoff_frequency"):
        hz = _num(getattr(target, "value", None), {}, FREQUENCY)
        if hz:
            return hz
    setup = getattr(spec, "setup", None)
    if setup is not None:
        hz = _num(getattr(setup, "frequency", None), {}, FREQUENCY)
        if hz:
            return hz
    return None


def radiation_clearance(spec, scope) -> list[tuple[str, str, str]]:
    """`(path, message, hint)` for every radiation boundary that sits too close.

    Measures the gap between the boundary object's bounds and the union of every
    other bounded body, on all six faces, and reports the tightest.
    """
    out: list[tuple[str, str, str]] = []
    f0 = _target_frequency(spec)
    if not f0:
        return out
    required = CLEARANCE_FRACTION * C0 / f0

    boxes: dict[str, list[tuple[float, float]]] = {}
    for op in getattr(spec, "geometry", []) or []:
        if op.op in _BOUNDED_OPS:
            bbox = bounding_box(op, scope)
            if bbox is not None:
                boxes[op.name] = bbox

    for index, boundary in enumerate(getattr(spec, "boundaries", []) or []):
        if boundary.type != "radiation":
            continue
        host = _selector_object(getattr(boundary, "on", None))
        outer = boxes.get(host)
        if outer is None:
            continue
        # Port sheets are excitation surfaces, not radiators, and they are
        # routinely drawn touching the boundary on purpose - a wave port on the
        # airbox face is the standard pattern. Counting them as "the model"
        # made a correctly padded spec look under-padded (X0a's port sheet
        # rises 13.6 mm, which ate 13.6 mm of an otherwise exact lambda0/3).
        excited = {
            _selector_object(getattr(e, "on", None))
            for e in (getattr(spec, "excitations", []) or [])
        }
        inner = [b for name, b in boxes.items()
                 if name != host and name not in excited]
        if not inner:
            continue

        # Union of everything the boundary encloses.
        lo = [min(b[i][0] for b in inner) for i in range(3)]
        hi = [max(b[i][1] for b in inner) for i in range(3)]

        gaps = []
        for i in range(3):
            gaps.append((lo[i] - outer[i][0], "-" + "xyz"[i]))
            gaps.append((outer[i][1] - hi[i], "+" + "xyz"[i]))

        # A face flush with the model is a deliberate pattern - a wave port on
        # the boundary face, or a box sitting on a ground plane - so drop those
        # faces and judge the rest. Dropping the *boundary* on a flush face
        # (an earlier version of this) let a deliberate zero mask a genuinely
        # tight face: X0a is flush in -y and -z and clears by lambda0/8 in x,
        # and went unreported.
        padded = [g for g in gaps if abs(g[0]) > 1e-12]
        if not padded:
            continue
        tightest, face = min(padded, key=lambda g: g[0])
        # 1% slack. A spec that writes the pad as `c0 / (3 * f0)` lands on
        # exactly lambda0/3, and a strict `<` then fires on the floating-point
        # residue - warning that 41.64 mm is less than 41.64 mm. A rule of thumb
        # that cannot be satisfied exactly is a rule nobody will keep.
        if tightest >= required * 0.99:
            continue
        out.append((
            f"boundaries[{index}]",
            f"radiation boundary {host!r} clears the model by "
            f"{tightest * 1e3:.2f} mm on {face}, less than lambda0/3 "
            f"({required * 1e3:.2f} mm at {f0 / 1e9:.4g} GHz)",
            "the near field is still substantial there; lambda0/3 on every side "
            "is the rule of thumb (four of six reviewed specs under-padded)",
        ))
    return out


def port_geometry(spec, scope) -> list[tuple[str, str, str]]:
    """`(path, message, hint)` for lumped ports far wider than their conductor.

    The port sheet bridges a gap between two conductors. Its width should track
    the conductor, not the designer's convenience: a ribbon several times wider
    presents a cross-section the antenna does not have.
    """
    out: list[tuple[str, str, str]] = []
    boxes: dict[str, list[tuple[float, float]]] = {}
    radii: dict[str, float] = {}
    for op in getattr(spec, "geometry", []) or []:
        if op.op in _BOUNDED_OPS:
            bbox = bounding_box(op, scope)
            if bbox is not None:
                boxes[op.name] = bbox
        if op.op == "cylinder":
            r = _num(getattr(op, "radius", None), scope)
            if r:
                radii[op.name] = r

    if not radii:
        return out                       # only wire-like feeds are judged here

    for index, exc in enumerate(getattr(spec, "excitations", []) or []):
        if exc.type != "lumped_port":
            continue
        sheet = getattr(getattr(exc, "on", None), "object", None)
        bbox = boxes.get(sheet)
        if bbox is None:
            continue
        # The dimension that matters is *transverse to the current*, not the
        # largest one. A gap-bridging port must span the gap along the
        # integration line - that extent is the gap and is supposed to be there.
        # Judging the widest extent instead flagged a correctly-sized port whose
        # gap simply exceeded the wire diameter.
        along = _integration_axis(exc, scope)
        transverse = [hi - lo for axis, (lo, hi) in enumerate(bbox)
                      if hi > lo and axis != along]
        if not transverse:
            continue
        width = max(transverse)
        conductor = 2.0 * max(radii.values())
        if width <= conductor * PORT_WIDTH_RATIO:
            continue
        out.append((
            f"excitations[{index}]",
            f"lumped port sheet {sheet!r} is {width * 1e3:.2f} mm wide across "
            f"the current against a {conductor * 1e3:.2f} mm conductor "
            f"({width / conductor:.1f}x)",
            "a port much wider than the conductor it bridges reports an "
            "impedance that is not the antenna's; size it to the conductor",
        ))
    return out


# Not implemented here, deliberately: the feed-network impedance walk that would
# have caught S7, where every line width was individually correct and the
# network terminated into 100 ohm while the elements were matched to 50. That
# needs the conductor graph and the quarter-wave sections read off it, which is
# real topology work rather than a bounding-box comparison. It is the third
# candidate gate in FALSE-GREEN-RATE.md and is scoped as its own ticket.
