"""Snapshot the live model into `results/state/model_snapshot.json`.

Run in the Build session after the Review gate tweaks (read-back sync,
ADR 0005) and again in the Solve+QA session: the shape is the contract
between sessions and the input to the verify runner.

Sections captured (all pure-introspection, sorted for deterministic
bytes): objects (names), bboxes (per object, from the modeler),
materials (per object), boundaries (name -> type), excitations (name ->
type), setups (name -> properties), sweeps (existing_analysis_sweeps),
variables (name -> expression). Floats are rounded to 9 decimals so
identical geometry reads byte-identically; anything not JSON-native is
stringified.

Usage (workspace root):  python src/capture_state.py
Prints one Verification line:  PASS: capture_state <counts>
Keeps the desktop alive.
"""

import json
import os
import re
import sys


def _rounded(value):
    """Normalize a value into JSON-native form; floats rounded to 9 dp."""
    import math

    if isinstance(value, float) or isinstance(value, int):
        if isinstance(value, int):
            return value
        rounded = round(value, 9)
        return rounded if rounded == rounded else None  # NaN -> None
    if isinstance(value, (tuple, list)):
        return [_rounded(v) for v in value]
    if isinstance(value, dict):
        return {k: _rounded(v) for k, v in value.items()}
    if hasattr(value, "tolist"):  # numpy arrays / scalar-like objects
        try:
            return _rounded(value.tolist())
        except Exception:  # noqa: BLE001 - object not convertible
            return str(value)
    if isinstance(value, (bool, type(None), str)):
        return value
    return str(value)


def _object_names(model):
    try:
        return sorted(model.modeler.object_names or [])
    except Exception:  # noqa: BLE001 - modeler unavailable
        return []


def _bbox(model, name):
    for probe in (
        lambda: model.modeler.get_object_bounding_box(name),
        lambda: model.modeler[name].bounding_box,
    ):
        try:
            value = probe()
            if value is not None:
                return _rounded(value)
        except Exception:  # noqa: BLE001 - not a solid / API missing
            continue
    return None


def _material(model, name):
    try:
        obj = model.modeler[name]
        return str(getattr(obj, "material_name", "")) or ""
    except Exception:  # noqa: BLE001 - non-material objects
        return ""


def _object_kinds(model):
    """`name -> solid | sheet | line`, the one thing a bbox cannot tell you.

    Added for the spec reducer (ticket 12a): a bounding box alone cannot name
    a construction op, so every object reduced to `op: unknown`. Knowing that
    an object is a SHEET with one degenerate axis at least pins the plane, and
    a SOLID with no degenerate axis is a plausible box. It does not pin the
    outline — a bow-tie and a rectangle share a bounding box — but it turns a
    blind guess into a checkable one.
    """
    kinds = {}
    for attribute, kind in (("solid_names", "solid"),
                            ("sheet_names", "sheet"),
                            ("line_names", "line"),
                            ("point_names", "point")):
        try:
            for name in getattr(model.modeler, attribute, None) or []:
                kinds[str(name)] = kind
        except Exception:  # noqa: BLE001 - attribute missing on this pyAEDT
            continue
    return dict(sorted(kinds.items()))


def _entity_map(entities):
    """`{name: type}` from a pyAEDT boundary/excitation collection."""
    out = {}
    for entity in entities:
        try:
            name = str(getattr(entity, "name", ""))
            if not name:
                continue
            kind = str(getattr(entity, "type", "") or type(entity).__name__)
            out[name] = kind
        except Exception:  # noqa: BLE001 - unreadable entity
            continue
    return dict(sorted(out.items()))


def _setup_map(model):
    """`{setup name: properties}` — passes, delta-S, frequency, and so on.

    pyAEDT 1.3.0's `Setup` has NO `get_properties()`; it exposes `props`
    and `properties`. The original `hasattr(setup, "get_properties")` probe
    was therefore always False and every snapshot recorded `{}` for every
    setup — silently, on both sides of any comparison, so a changed
    max-pass or delta-S looked identical to an unchanged one. Verified
    empty in all three captured models, the pilot included.
    """
    out = {}
    for setup in getattr(model, "setups", []) or []:
        name = str(getattr(setup, "name", "") or "<unnamed>")
        props = None
        for probe in (
            lambda: getattr(setup, "props", None),
            lambda: getattr(setup, "properties", None),
            lambda: setup.get_properties(),
        ):
            try:
                candidate = probe()
            except Exception:  # noqa: BLE001 - API absent on this version
                continue
            if candidate:
                props = candidate
                break
        if props is None:
            out[name] = "<unreadable>"
            continue
        try:
            out[name] = _rounded(dict(props))
        except Exception:  # noqa: BLE001 - not mapping-like
            out[name] = _rounded(props)
    return dict(sorted(out.items()))


_TERMINAL_SUFFIX = re.compile(r"_T\d+$")


def split_ports(boundaries):
    """`(ports, terminals)` from a boundary map.

    Ports and their terminals are BOTH typed `Wave Port` in the boundary
    list, so counting everything port-typed over-reports: a 2-port coplanar
    waveguide lists `1, 1_T1, 1_T2, 2, 2_T1, 2_T2` — six entries, two
    ports. Terminal-solution designs create one terminal per conductor per
    port, named `<port or object>_T<n>`.

    Verified against every model captured here: coplanar 6 -> 2 ports +
    4 terminals, bandpass 4 -> 2 + 2, probe-fed patch 2 -> 1 port + 1
    terminal, horn and parabolic 1 -> 1 + 0.
    """
    port_typed = {name: kind for name, kind in boundaries.items()
                  if "port" in str(kind).lower()}
    terminals = {n: k for n, k in port_typed.items() if _TERMINAL_SUFFIX.search(n)}
    ports = {n: k for n, k in port_typed.items() if n not in terminals}
    return dict(sorted(ports.items())), dict(sorted(terminals.items()))


def _model_units(model):
    """The modeler's display units — bbox numbers are in THESE, not mm.

    Snapshots recorded bare bbox numbers with no unit, while variables
    carry explicit units, so the two could only be compared by guessing the
    scale. Observed in the wild: inches for one model, centimetres for
    another, millimetres for the pilot.
    """
    for probe in (
        lambda: model.modeler.model_units,
        lambda: model.modeler.oeditor.GetModelUnits(),
    ):
        try:
            value = probe()
            if value:
                return str(value)
        except Exception:  # noqa: BLE001 - modeler/API unavailable
            continue
    return ""


def shape_from_model(model):
    """The model shape as a plain, JSON-ready dict (the snapshot)."""
    objects = _object_names(model)
    bboxes = {}
    materials = {}
    for name in objects:
        bboxes[name] = _bbox(model, name)
        materials[name] = _material(model, name)
    # `model.variables` is None on fresh attach (observed; pilot calibration) —
    # fall back to the variable manager so the variables section always carries.
    variables = dict(getattr(model, "variables", None) or {})
    if not variables:
        try:
            raw = dict(getattr(model, "variable_manager", None).variables or {})
            variables = {
                str(k): str(getattr(v, "expression", "") or v) for k, v in raw.items()
            }
        except Exception:  # noqa: BLE001 - variable manager unavailable
            variables = {}
    sweeps = sorted(getattr(model, "existing_analysis_sweeps", []) or [])
    boundaries = _entity_map(getattr(model, "boundaries", []) or [])
    # Ports land in `boundaries`, not `excitations` — observed on every model
    # captured here (Modal and Terminal): `excitations` came back empty each
    # time. Terminals are port-typed too, so they are split out rather than
    # counted as ports. Both raw sections stay untouched.
    ports, terminals = split_ports(boundaries)
    return {
        "snapshot_version": 3,
        "model_units": _model_units(model),
        "objects": objects,
        "object_kinds": _object_kinds(model),
        "bboxes": bboxes,
        "materials": materials,
        "boundaries": boundaries,
        "excitations": _entity_map(getattr(model, "excitations", []) or []),
        "ports": ports,
        "terminals": terminals,
        "setups": _setup_map(model),
        "sweeps": sweeps,
        "variables": dict(sorted(variables.items())),
    }


def main():
    from ws_common import STATE, attach, exit_keep_alive  # pyaedt-scoped import

    model = attach(launch=False)
    shape = shape_from_model(model)
    os.makedirs(STATE, exist_ok=True)
    out = os.path.join(STATE, "model_snapshot.json")
    with open(out, "w") as f:
        json.dump(shape, f, indent=1, sort_keys=True)
    counts = {
        "objects": len(shape["objects"]),
        "bboxes": len(shape["bboxes"]),
        "materials": len([m for m in shape["materials"].values() if m]),
        "boundaries": len(shape["boundaries"]),
        "excitations": len(shape["excitations"]),
        "setups": len(shape["setups"]),
        "sweeps": len(shape["sweeps"]),
        "variables": len(shape["variables"]),
    }
    detail = " ".join("%s=%d" % kv for kv in sorted(counts.items()))
    print("snapshot written:", out, flush=True)
    line = "PASS: capture_state " + detail
    print(line, flush=True)
    import run_events

    run_events.emit("snapshot.captured", stage="snapshot", verdict=line,
                    detail="snapshot=%s" % out, state_dir=STATE)
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    import ws_common

    ws_common.exit_keep_alive()
