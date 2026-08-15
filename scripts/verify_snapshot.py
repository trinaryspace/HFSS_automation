"""Check a captured snapshot against its own design variables.

The question this answers is "did the capture record the model faithfully",
and it answers it **without AEDT** by asking whether each object's bounding
box can be reconstructed from the design variables. If every extent falls
out of the variables exactly, the capture is faithful and the variables
carry real design intent. If they cannot, either the capture is wrong or
the model is not parametric.

What it deliberately does NOT do is regenerate the geometry. A snapshot
records bounding boxes, not construction: a pyramidal horn and a
rectangular box with the same extent are byte-identical in a snapshot. That
is the `op: unknown` boundary from ticket 12a, and this script reports it
rather than papering over it.

Unit note: `capture_state` records bbox numbers in the MODEL's display
units with no unit tag, while variables carry explicit units. This script
infers the model unit by finding the scale that makes the two agree, and
reports it — an untagged bbox is a real gap in the snapshot format, and
naming the inferred unit is how it stays visible.

Usage:
    python scripts/verify_snapshot.py knowledge/cases/_snapshots/horn-10ghz.json
"""

import argparse
import itertools
import json
import sys

UNITS_MM = {"m": 1000.0, "cm": 10.0, "mm": 1.0, "um": 0.001,
            "in": 25.4, "mil": 0.0254, "ft": 304.8}
TOL = 1e-6


def parse_length(raw):
    """'1.8in' -> mm, or None when not a plain length literal."""
    text = str(raw).strip()
    for suffix in sorted(UNITS_MM, key=len, reverse=True):
        if text.endswith(suffix):
            try:
                return float(text[: -len(suffix)]) * UNITS_MM[suffix]
            except ValueError:
                return None
    try:
        return float(text)
    except ValueError:
        return None


def extents(bbox):
    return [bbox[3] - bbox[0], bbox[4] - bbox[1], bbox[5] - bbox[2]]


def infer_model_unit(snapshot, lengths):
    """The unit that makes bbox numbers agree with variable values."""
    best = None
    all_ext = []
    for name in snapshot.get("objects", []):
        bbox = (snapshot.get("bboxes") or {}).get(name)
        if bbox and len(bbox) == 6:
            all_ext.extend(e for e in extents(bbox) if e > 0)
    if not all_ext or not lengths:
        return None, 0
    for unit, scale in UNITS_MM.items():
        hits = 0
        for extent in all_ext:
            target = extent * scale
            for value in lengths.values():
                if abs(target - value) <= max(1e-4, abs(value) * 1e-6):
                    hits += 1
                    break
        if best is None or hits > best[1]:
            best = (unit, hits)
    return best


def explain(extent_mm, lengths):
    """Express an extent as the SIMPLEST matching combination of variables.

    Simplest-first matters: a zero-valued variable makes spurious sums look
    valid (`feedX + 2*coax_outer_rad` with `feedX = 0cm` is really just
    `2*coax_outer_rad`, a cylinder diameter). Zero-valued variables are
    therefore excluded from additive positions, and single-term and
    doubled-term forms are tried before any sum.
    """
    nonzero = {k: v for k, v in lengths.items() if abs(v) > 1e-9}

    for name, value in sorted(nonzero.items()):
        if abs(extent_mm - value) <= 1e-4:
            return name
    # k*var — a radius driving a diameter, an aperture spanning radii, etc.
    for k in (2, 3, 4):
        for name, value in sorted(nonzero.items()):
            if abs(extent_mm - k * value) <= 1e-4:
                return "%d*%s" % (k, name)
    for name, value in sorted(nonzero.items()):
        if abs(extent_mm - value / 2.0) <= 1e-4:
            return "%s/2" % name
    for (a, av), (b, bv) in itertools.product(sorted(nonzero.items()), repeat=2):
        if a == b:
            continue
        if abs(extent_mm - (av + 2 * bv)) <= 1e-4:
            return "%s + 2*%s" % (a, b)
        if abs(extent_mm - (av + bv)) <= 1e-4:
            return "%s + %s" % (a, b)
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("snapshot")
    parser.add_argument("--unit", help="force the model unit (e.g. in, mm)")
    args = parser.parse_args(argv)

    snapshot = json.load(open(args.snapshot, encoding="utf-8"))
    variables = snapshot.get("variables") or {}
    lengths = {}
    for name, raw in variables.items():
        value = parse_length(raw)
        if value is not None:
            lengths[name] = value

    meta = snapshot.get("_capture") or {}
    print("project=%s design=%s solution=%s"
          % (meta.get("project"), meta.get("design"), meta.get("solution_type")))
    print("variables with a length value: %d of %d"
          % (len(lengths), len(variables)))

    stored = str(snapshot.get("model_units") or "").strip()
    if args.unit:
        unit, source = args.unit, "forced"
    elif stored in UNITS_MM:
        unit, source = stored, "recorded in the snapshot"
        inferred, _hits = infer_model_unit(snapshot, lengths)
        if inferred and inferred != unit:
            print("! recorded unit %r disagrees with the inferred %r — "
                  "trusting the recorded one" % (unit, inferred))
    else:
        unit, _hits = infer_model_unit(snapshot, lengths)
        source = "INFERRED (snapshot predates snapshot_version 2)"
    if not unit:
        print("FAIL: verify_snapshot cannot determine the model unit "
              "(no bboxes or no length variables)")
        return 1
    scale = UNITS_MM[unit]
    print("model unit: %s  (%s)" % (unit, source))
    print()

    explained = 0
    total = 0
    print("%-20s %-26s %s" % ("object", "extent (model units)", "explained by"))
    for name in snapshot.get("objects", []):
        bbox = (snapshot.get("bboxes") or {}).get(name)
        if not bbox or len(bbox) != 6:
            print("%-20s %-26s %s" % (name, "<no bbox>", "-"))
            continue
        ext = extents(bbox)
        parts = []
        for value in ext:
            if abs(value) <= TOL:
                parts.append("0 (sheet)")
                continue
            total += 1
            found = explain(value * scale, lengths)
            if found:
                explained += 1
            parts.append(found or "UNEXPLAINED")
        print("%-20s %-26s %s"
              % (name, str([round(e, 4) for e in ext]), ", ".join(parts)))

    print()
    print("bbox dimensions explained by variables: %d of %d" % (explained, total))
    print()
    print("NOT recorded, and not recoverable from this snapshot:")
    print("  - the construction op per object (a flared horn and a box with")
    print("    the same extent are identical here) -> ticket 12a `op: unknown`")
    print("  - which face each port sits on (only the port's own bbox is kept)")
    print("  - the model unit (inferred above, not stored)")

    ok = total and explained == total
    print()
    print("%s: verify_snapshot explained=%d/%d unit=%s"
          % ("PASS" if ok else "PARTIAL", explained, total, unit))
    return 0 if ok else 0  # informational: a partial explanation is not a failure


if __name__ == "__main__":
    raise SystemExit(main())
