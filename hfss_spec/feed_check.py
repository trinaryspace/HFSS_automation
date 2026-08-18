"""The feed-network impedance walk - the third gate, aimed at S7's defect.

Cell S7 (2026-08-17) authored a 2x2 corporate-fed patch array in which every line
width was individually correct: 1.7427 mm really is 50 ohm on that stack, 0.4403
mm really is 100 ohm, and 70.71 is sqrt(50*100), the right transformer impedance
for that pair. The network was even internally self-consistent. And it was wrong:
those four 100 ohm lines terminated at patches inset-matched to 50 ohm, so every
element was mismatched 2:1. validate_spec, precheck and compile_spec --dry-run
all passed, because each examines fields and this defect lives in the
relationship between them.

Declarative on purpose. The one quantity this cannot derive is the element's
input impedance - inset depth or probe position sets it, and deriving it is
synthesis rather than arithmetic. So the spec states it and everything downstream
is checked against the geometry's own widths. That is not a concession: S7's
failure was never a miscalculation, it was the absence of a statement about what
the network demanded at its elements. element_impedance is that statement, and
once it exists the rest is algebra.

Topology-agnostic on purpose too, because more than one feed is correct. Measured
on RO4350B 0.762 mm at 5.8 GHz:

  50 ohm elements  : 50 -> par -> lam/4 @ 35.36 -> 50 -> par -> lam/4 -> 50
                     3 sections, narrowest line 1.743 mm
  200 ohm elements : 200 -> par -> 100 -> par -> 50
                     0 sections, but a 200 ohm line is 0.038 mm wide
  200 stepped down : 200 -> lam/4 @ 141.4 -> 100 -> par -> 50 -> par -> lam/4
                     5 sections, narrowest 0.158 mm

The halving design is elegant precisely because 200 is 4x a 50 ohm input: two
parallel combinations land on it with no matching sections at all. Its cost is
that the 200 ohm line is unmakeable and outside Hammerstad's validity, so it
works only where the pair junction sits at the element edge with no such line to
route. All three close, and a checker enforcing any one shape would reject the
other two. What they share, and what is enforced here:

    at every junction the parallel combination of the branches must equal the
    characteristic impedance of the line feeding it, with a quarter-wave section
    transforming a load as Z^2 / Z_load.
"""

from __future__ import annotations

import difflib
from typing import Optional

from .expressions import ExpressionError, Value, evaluate
from .units import DIMENSIONLESS, LENGTH, RESISTANCE, UnitError

# Hammerstad-Jensen is quoted for W/h in roughly 0.1..10. Outside that its number
# is not so much wrong as meaningless, and a gate that reports a meaningless
# number confidently is the defect this module exists to catch.
WH_MIN, WH_MAX = 0.05, 20.0


def _num(raw, scope, dimension) -> Optional[float]:
    if raw is None:
        return None
    try:
        value = evaluate(raw, scope)
    except (ExpressionError, UnitError):
        return None
    if not isinstance(value, Value) or value.dimension != dimension:
        return None
    return value.si


def _strip_extents(op, scope) -> Optional[tuple[float, float]]:
    """(width, length) of a strip: the narrower and wider in-plane extents."""
    from .model_checks import bounding_box
    bbox = bounding_box(op, scope)
    if bbox is None:
        return None
    extents = sorted(hi - lo for lo, hi in bbox if hi - lo > 0)
    if len(extents) < 2:
        return None
    return extents[0], extents[-1]


def _impedance_of(width, h, er):
    """(Z0, eeff) for this strip, or None when outside Hammerstad's range."""
    if width <= 0 or h <= 0 or er <= 0:
        return None
    if not WH_MIN <= width / h <= WH_MAX:
        return None
    try:
        from .physics import microstrip_impedance
        return microstrip_impedance(width, h, er)
    except Exception:                          # noqa: BLE001 - never blocks
        return None


def _substrate_stack(spec, scope):
    """(h, er) for the board the feed sits on."""
    h = None
    for name in ("h", "sub_h", "SubH", "subst_h"):
        value = scope.get(name)
        if value is not None and getattr(value, "dimension", None) == LENGTH:
            h = value.si
            break
    er = None
    for material in (getattr(spec, "materials", {}) or {}).values():
        raw = getattr(material, "permittivity", None)
        if raw is not None:
            er = _num(raw, scope, DIMENSIONLESS)
            if er:
                break
    if not er:
        for name in ("er", "eps_r", "epsilon_r"):
            value = scope.get(name)
            if value is not None and getattr(value, "dimension", None) == DIMENSIONLESS:
                er = value.si
                break
    return h, er


def _port_impedance(spec, scope, declared):
    if declared is not None:
        return declared
    for excitation in (getattr(spec, "excitations", []) or []):
        z = _num(getattr(excitation, "impedance", None), scope, RESISTANCE)
        if z:
            return z
    return 50.0


def walk(spec, scope):
    """(path, severity, message, hint) for each finding.

    Chain arithmetic is an ERROR: the designer declared what the elements
    present, so either it closes or the array is mismatched. The provenance of
    that declaration is a WARNING - it is methodology rather than algebra, and
    making it fatal would block every array spec until someone runs a multi-port
    extraction, which is the right order of work but not a reason to refuse to
    validate a document.
    """
    out = []
    net = getattr(spec, "feed_network", None)
    if net is None or not getattr(net, "chain", None):
        return out

    h, er = _substrate_stack(spec, scope)
    if not h or not er:
        return [("feed_network", "error",
                 "cannot read the substrate stack, so no line impedance is computable",
                 "declare h as a length variable and a permittivity on the substrate material")]

    z_elem = _num(net.element_impedance, scope, RESISTANCE)
    if not z_elem or z_elem <= 0:
        return [("feed_network.element_impedance", "error",
                 "element_impedance must be a positive impedance",
                 "read as " + repr(net.element_impedance))]

    z_port = _port_impedance(spec, scope, _num(net.port_impedance, scope, RESISTANCE))
    ops = {op.name: op for op in (getattr(spec, "geometry", []) or [])}
    tol = net.tolerance_pct / 100.0

    from .model_checks import _target_frequency
    f0 = _target_frequency(spec)

    # A chain with a junction is a multi-element array, and in an array the
    # figure that matters is the ACTIVE impedance - what an element presents
    # while its neighbours are driven - not its isolated value. At lambda/2 the
    # difference is not small: a perfectly matched isolated element can present
    # about 41 ohm active, a 17% error that reads as roughly -20 dB at the input.
    # "Mostly matches" is exactly what a feed solved against the wrong load looks
    # like, which is why this is surfaced rather than assumed away.
    if any(stage.junction for stage in net.chain) and             net.element_impedance_source != "active_measured":
        out.append((
            "feed_network.element_impedance_source", "warning",
            "this feed drives multiple elements, but element_impedance is marked "
            "%r rather than measured" % net.element_impedance_source,
            "simulate the elements with individual ports and no feed network, "
            "take the active impedance from the S-matrix "
            "(gamma_act,i = sum_j S_ij a_j/a_i), and match to that; matching to "
            "the isolated value leaves a mismatch no feed arithmetic can remove",
        ))

    z = z_elem
    steps = ["element %.2f" % z_elem]

    for index, stage in enumerate(net.chain):
        path = "feed_network.chain[%d]" % index

        if stage.junction:
            z = z / stage.junction
            steps.append("%d in parallel -> %.2f" % (stage.junction, z))
            continue

        name = stage.line or stage.quarter_wave
        if not name:
            out.append((path, "error", "a stage must set one of line, quarter_wave or junction", ""))
            return out
        op = ops.get(name)
        if op is None:
            close = difflib.get_close_matches(str(name), list(ops), n=1)
            out.append((path, "error", "%r is not a geometry object" % name,
                        ("did you mean %r?" % close[0]) if close else "check the object name"))
            return out

        extents = _strip_extents(op, scope)
        if extents is None:
            out.append((path, "error", "cannot measure %r as a strip" % name,
                        "the walk needs a resolvable width and length"))
            return out
        width, length = extents
        pair = _impedance_of(width, h, er)
        if pair is None:
            out.append((path, "error",
                        "no trustworthy impedance for %r: W/h = %.3f, outside "
                        "Hammerstad's usable range" % (name, width / h),
                        "a 200 ohm line on this stack is about 0.04 mm wide, both "
                        "unmakeable and past the closed form; put the junction at the "
                        "element edge rather than routing a line that thin"))
            return out
        z_line, eeff = pair

        if stage.quarter_wave:
            if f0:
                from .physics import guide_wavelength
                quarter = guide_wavelength(f0, eeff) / 4.0
                if abs(length - quarter) / quarter > 0.05:
                    # ERROR, not a warning: the walk computes Z^2/Z_load,
                    # which holds only at exactly a quarter wavelength. A
                    # section off that length does not perform the transform the
                    # chain declares, so the closure reported downstream is
                    # fiction rather than an approximation.
                    out.append((path, "error",
                                "%r acts as a quarter-wave section but is %.3f mm long "
                                "against lambda_g/4 = %.3f mm at %.4g GHz"
                                % (name, length * 1e3, quarter * 1e3, f0 / 1e9),
                                "a section that is not a quarter wavelength does not "
                                "transform to the impedance the algebra assumes"))
            z = z_line * z_line / z
            steps.append("lam/4 %s @ %.2f -> %.2f" % (name, z_line, z))
            continue

        if abs(z_line - z) / z > tol:
            ratio = max(z_line, z) / min(z_line, z)
            out.append((path, "error",
                        "%r is a %.2f ohm line (%.3f mm) into a %.2f ohm load - "
                        "%.2f:1 mismatch" % (name, z_line, width * 1e3, z, ratio),
                        "match the line, add a quarter-wave section, or declare a "
                        "different element_impedance; all are valid feeds, but the "
                        "chain has to close"))
            return out
        steps.append("line %s %.2f" % (name, z_line))

    if abs(z - z_port) / z_port > tol:
        out.append(("feed_network", "error",
                    "the chain does not close: a %.2f ohm element presents %.2f ohm "
                    "at the port, which wants %.2f ohm" % (z_elem, z, z_port),
                    "walk: " + " | ".join(steps)))
    return out
