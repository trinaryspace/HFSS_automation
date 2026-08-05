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
    out = {}
    for setup in getattr(model, "setups", []) or []:
        try:
            props = setup.get_properties() if hasattr(setup, "get_properties") else {}
            out[str(setup.name)] = _rounded(dict(props))
        except Exception:  # noqa: BLE001 - unreadable setup
            out[str(setup.name)] = "<unreadable>"
    return dict(sorted(out.items()))


def shape_from_model(model):
    """The model shape as a plain, JSON-ready dict (the snapshot)."""
    objects = _object_names(model)
    bboxes = {}
    materials = {}
    for name in objects:
        bboxes[name] = _bbox(model, name)
        materials[name] = _material(model, name)
    variables = dict(getattr(model, "variables", {}) or {})
    sweeps = sorted(getattr(model, "existing_analysis_sweeps", []) or [])
    return {
        "objects": objects,
        "bboxes": bboxes,
        "materials": materials,
        "boundaries": _entity_map(getattr(model, "boundaries", []) or []),
        "excitations": _entity_map(getattr(model, "excitations", []) or []),
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
    print("PASS: capture_state " + detail, flush=True)
    print("snapshot written:", out, flush=True)
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    import ws_common

    ws_common.exit_keep_alive()
