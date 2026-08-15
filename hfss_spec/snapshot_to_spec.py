"""`model_snapshot.json` -> `design.yaml`. Ticket 12a.

Sequenced before the schema (Q7) so that the non-geometry sections are shaped
by five real captured models instead of by guesswork, and so that Re-entry
(Q8) gets a spec by reduction rather than by archaeology: copy the project
(ADR 0001) -> `capture_state` -> `snapshot_to_spec` -> the spec *is* the model
card for a project we did not build.

The scope boundary is the whole point, and it is **descriptive, not
constructive**:

- **Exact** — variables (AEDT expressions verbatim), project-scoped `$vars`,
  materials, boundaries, ports, terminals, setup, sweep, solution type.
- **Approximate, and marked as such** — geometry. A bounding box is a
  *consequence* of a construction op, not a restatement of it: the parabolic
  reflector explains 2 of 18 bbox dimensions from its variables because a
  paraboloid's extent is a nonlinear function of focal length, and a horn's
  flare is byte-identical to a rectangular box of the same extent. So an
  object whose construction cannot be established emits `op: unknown`
  carrying its bbox — a first-class value, never a silent wrong guess.

Everything here is Tier 0: stdlib plus the schema module, no pyAEDT.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
_CAPTURE_STATE = REPO / "skill" / "hfss-agent" / "templates" / "workspace" / "src" / "capture_state.py"


def _load_split_ports():
    """Import `split_ports` from capture_state rather than re-deriving it.

    One rule, one implementation: ticket 01's two profile parsers are why the
    banking bug survived a green suite, and ports/terminals share exactly that
    hazard — both are typed `Wave Port`, and a second copy of the `_T\\d+$`
    rule would drift the moment one of them learned about lumped ports.
    """
    spec = importlib.util.spec_from_file_location("_capture_state", _CAPTURE_STATE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.split_ports


split_ports = _load_split_ports()


# AEDT boundary type strings -> schema types. Anything unmapped is reported
# rather than guessed.
BOUNDARY_TYPES = {
    "radiation": "radiation",
    "perfect e": "perfect_e",
    "perfect h": "perfect_h",
    "finite conductivity": "finite_conductivity",
    "symmetry": "symmetry",
    "impedance": "impedance",
    "fe-bi": "fe_bi",
    "febi": "fe_bi",
}

PORT_TYPES = {
    "wave port": "wave_port",
    "lumped port": "lumped_port",
}

# A parametric variation string masquerading as a sweep:
#   "Setup1 - AirGap='25mm' CuT='0.1mm' ... : Table"
# Both the patch and the pilot carry one. It is a parametric table, not a
# sweep, and a reducer that treats it as one invents a frequency range.
_VARIATION_RE = re.compile(r"=\s*'")

# Setup property names, as AEDT actually spells them.
_FREQUENCY_KEYS = ("Frequency", "SolveFrequency", "AdaptiveFrequency")
_PASSES_KEYS = ("MaximumPasses", "MaxPasses", "NumPasses")
_DELTAS_KEYS = ("MaxDeltaS", "DeltaS", "MaximumDeltaS")


@dataclass
class Reduction:
    """The reducer's output plus an honest account of what it could not do."""

    spec: dict[str, Any]
    exact: list[str] = field(default_factory=list)
    approximate: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def unknown_geometry(self) -> int:
        return sum(1 for op in self.spec.get("geometry", []) if op.get("op") == "unknown")

    @property
    def summary(self) -> str:
        return (
            f"objects={len(self.spec.get('geometry', []))} "
            f"unknown={self.unknown_geometry} "
            f"variables={len(self.spec.get('variables', {}))} "
            f"ports={len(self.spec.get('excitations', []))} "
            f"boundaries={len(self.spec.get('boundaries', []))} "
            f"missing={len(self.missing)}"
        )


def reduce_snapshot(snapshot: dict, name: str = "", recipe: str = "") -> Reduction:
    """Reduce a captured snapshot to spec shape."""
    capture = snapshot.get("_capture", {}) or {}
    design = capture.get("design") or ""
    out: dict[str, Any] = {
        "spec_version": 1,
        "name": name or design or "reduced-design",
        "recipe": recipe or "unknown-recipe",
        "solution_type": _solution_type(snapshot, capture),
        "provenance": {
            "source": f"reduced from a captured model snapshot "
                      f"(v{snapshot.get('snapshot_version', 1)})"
                      + (f", design {design!r}" if design else ""),
            "canonical_reading": "measured",
            "notes": "geometry is descriptive, not constructive — see `unknown` ops",
        },
    }
    reduction = Reduction(spec=out)

    _reduce_variables(snapshot, out, reduction)
    _reduce_materials(snapshot, out, reduction)
    _reduce_geometry(snapshot, out, reduction)
    _reduce_ports(snapshot, out, reduction)
    _reduce_boundaries(snapshot, out, reduction)
    _reduce_setup(snapshot, out, reduction)

    out["mesh"] = [{"type": "adaptive_only"}]
    out["qa_signals"] = ["convergence", "ports_excited"]
    return reduction


def _solution_type(snapshot: dict, capture: dict) -> str:
    raw = str(capture.get("solution_type") or snapshot.get("solution_type") or "")
    return "Terminal" if "terminal" in raw.lower() else "Modal"


def _reduce_variables(snapshot: dict, out: dict, r: Reduction) -> None:
    """Exact. AEDT expressions are preserved verbatim, scopes kept separate."""
    variables = snapshot.get("variables") or {}
    design_vars, project_vars = {}, {}
    for key, value in variables.items():
        # `$losstan` is AEDT's project scope — a different namespace, and a
        # reducer that flattens the two writes back to the wrong place.
        (project_vars if str(key).startswith("$") else design_vars)[str(key)] = str(value)
    out["variables"] = dict(sorted(design_vars.items()))
    if project_vars:
        out["project_variables"] = dict(sorted(project_vars.items()))
        r.exact.append(f"project_variables ({len(project_vars)})")
    r.exact.append(f"variables ({len(design_vars)}, expressions verbatim)")
    if not variables:
        r.missing.append("variables (snapshot carried none)")


def _reduce_materials(snapshot: dict, out: dict, r: Reduction) -> None:
    """Exact as *references*; an inline definition needs data no snapshot holds."""
    materials = snapshot.get("materials") or {}
    named = sorted({str(v) for v in materials.values() if str(v).strip()})
    out["materials"] = {m: {"library": m} for m in named}
    r.exact.append(f"materials ({len(named)} referenced)")
    for material in named:
        if material.lower() not in _KNOWN_LIBRARY_MATERIALS:
            r.notes.append(
                f"material {material!r} is not a known library name — it is probably "
                f"user-defined, and its properties are NOT in the snapshot"
            )


_KNOWN_LIBRARY_MATERIALS = {
    "air", "vacuum", "pec", "copper", "gold", "silver", "aluminum", "aluminium",
    "fr4_epoxy", "rogers rt/duroid 5880 (tm)", "teflon_based", "polyimide",
    "silicon", "alumina_96pct", "iron", "nickel", "steel_stainless",
}


def _reduce_geometry(snapshot: dict, out: dict, r: Reduction) -> None:
    """Approximate, and marked. See the module docstring for why."""
    objects = list(snapshot.get("objects") or [])
    bboxes = snapshot.get("bboxes") or {}
    materials = snapshot.get("materials") or {}
    kinds = snapshot.get("object_kinds") or {}
    units = snapshot.get("model_units") or ""
    geometry = []
    guessed = 0
    for name in objects:
        bbox = bboxes.get(name)
        material = str(materials.get(name) or "") or None
        kind = str(kinds.get(name) or "").lower()
        op = _guess_op(kind, bbox)
        if op == "sheet":
            entry = _sheet_from_bbox(name, bbox, units, material)
            guessed += 1
        elif op == "box":
            entry = _box_from_bbox(name, bbox, units, material)
            guessed += 1
        else:
            entry = {
                "op": "unknown",
                "name": name,
                "bbox": bbox,
                "bbox_units": units or None,
                "reason": _unknown_reason(kind, bbox),
            }
            if material:
                entry["material"] = material
        geometry.append(entry)
    out["geometry"] = geometry
    unknown = sum(1 for g in geometry if g["op"] == "unknown")
    r.approximate.append(
        f"geometry ({len(geometry)} objects: {guessed} derived from kind+bbox, "
        f"{unknown} unknown)"
    )
    if not units:
        r.missing.append(
            "model_units (bbox numbers have no scale — snapshot_version 1)"
        )
    if not kinds:
        r.missing.append(
            "object_kinds (solid/sheet/line not captured — every object "
            "falls back to `op: unknown`)"
        )


def _guess_op(kind: str, bbox) -> str:
    """A construction op only where kind and bbox agree; otherwise `unknown`.

    A planar bbox plus a `sheet` kind still only pins the *plane*, not the
    outline — a bow-tie and a rectangle share a bounding box. So `sheet` here
    means "a planar object whose extent is this", and ticket 11's diff is what
    proves whether that was good enough.
    """
    if not bbox or len(bbox) != 6:
        return "unknown"
    extents = [round(bbox[i + 3] - bbox[i], 9) for i in range(3)]
    degenerate = sum(1 for e in extents if e == 0)
    if kind == "sheet" and degenerate == 1:
        return "sheet"
    if kind == "solid" and degenerate == 0:
        return "box"
    return "unknown"


def _unknown_reason(kind: str, bbox) -> str:
    if not bbox or len(bbox) != 6:
        return "no bounding box captured"
    if not kind:
        return "object kind not captured; a bbox alone cannot name the op"
    extents = [round(bbox[i + 3] - bbox[i], 9) for i in range(3)]
    degenerate = sum(1 for e in extents if e == 0)
    if kind == "sheet" and degenerate != 1:
        return f"sheet with {degenerate} degenerate axes — not planar-rectangular"
    if kind == "solid" and degenerate:
        return "solid with a zero extent — a degenerate or swept body"
    return f"kind {kind!r} has no v1 op"


def _dim(value: float, units: str) -> str:
    text = repr(round(float(value), 9))
    if text.endswith(".0"):
        text = text[:-2]
    return f"{text}{units}" if units else text


def _sheet_from_bbox(name, bbox, units, material) -> dict:
    extents = [round(bbox[i + 3] - bbox[i], 9) for i in range(3)]
    flat = extents.index(0)
    plane = {0: "yz", 1: "xz", 2: "xy"}[flat]
    keep = [i for i in range(3) if i != flat]
    entry = {
        "op": "sheet",
        "name": name,
        "plane": plane,
        "origin": [_dim(bbox[i], units) for i in range(3)],
        "size": [_dim(extents[i], units) for i in keep],
        "derived_from": "bbox",
    }
    if material:
        entry["material"] = material
    return entry


def _box_from_bbox(name, bbox, units, material) -> dict:
    entry = {
        "op": "box",
        "name": name,
        "origin": [_dim(bbox[i], units) for i in range(3)],
        "size": [_dim(bbox[i + 3] - bbox[i], units) for i in range(3)],
        "derived_from": "bbox",
    }
    if material:
        entry["material"] = material
    return entry


def _ports_and_terminals(snapshot: dict, r: Reduction, quiet: bool = False):
    """Always recompute from raw `boundaries` — never trust a stored section.

    The stored `ports` section is only as good as the splitter that wrote it,
    and every snapshot captured before the terminal fix recorded terminals as
    ports: the coplanar waveguide's section lists all six of
    `1, 1_T1, 1_T2, 2, 2_T1, 2_T2` for a two-port line. Raw `boundaries` are
    preserved on every snapshot, so recomputing costs nothing and means one
    rule with one implementation (the same `split_ports` capture_state uses).
    """
    boundaries = snapshot.get("boundaries") or {}
    ports, terminals = split_ports(boundaries)
    stored = snapshot.get("ports")
    if stored is not None and set(stored) != set(ports) and not quiet:
        r.notes.append(
            f"stored `ports` section listed {len(stored)} entries; recomputed "
            f"{len(ports)} port(s) + {len(terminals)} terminal(s) from raw "
            f"boundaries (the snapshot predates the terminal-suffix rule)"
        )
    return ports, terminals


def _reduce_ports(snapshot: dict, out: dict, r: Reduction) -> None:
    """Exact for names and types; the *face* is not in a snapshot."""
    ports, terminals = _ports_and_terminals(snapshot, r)
    objects = set(snapshot.get("objects") or [])
    excitations = []
    for name, kind in ports.items():
        mapped = PORT_TYPES.get(str(kind).lower())
        if mapped is None:
            r.missing.append(f"port {name!r}: unmapped AEDT type {kind!r}")
            continue
        entry = {"name": name, "type": mapped}
        if name in objects:
            # Real models name the port sheet after the port ("p1"), which is
            # the only object association a snapshot actually supports.
            entry["on"] = {"object": name}
        else:
            entry["on"] = {"object": name}
            r.missing.append(
                f"port {name!r}: no object of that name — the face selector "
                f"must be written by hand before this spec can compile"
            )
        if mapped == "lumped_port":
            r.missing.append(
                f"port {name!r}: a lumped port needs an integration_line, which "
                f"is not recoverable from a snapshot"
            )
        excitations.append(entry)
    out["excitations"] = excitations
    r.exact.append(f"ports ({len(excitations)}), terminals ({len(terminals)}) excluded")
    if terminals:
        r.notes.append(
            f"{len(terminals)} terminal(s) ignored: terminal-solution designs add "
            f"one `<port>_T<n>` per conductor and they are not ports"
        )


def _reduce_boundaries(snapshot: dict, out: dict, r: Reduction) -> None:
    """Exact for names and types; the assignment target is not in a snapshot."""
    boundaries = snapshot.get("boundaries") or {}
    ports, terminals = _ports_and_terminals(snapshot, r, quiet=True)
    skip = set(ports) | set(terminals)
    reduced = []
    for name, kind in sorted(boundaries.items()):
        if name in skip:
            continue
        mapped = BOUNDARY_TYPES.get(str(kind).lower())
        if mapped is None:
            r.missing.append(f"boundary {name!r}: unmapped AEDT type {kind!r}")
            continue
        reduced.append({
            "name": name,
            "type": mapped,
            # The snapshot records a boundary's name and type but not what it
            # is assigned to, so the selector is a placeholder the spec author
            # (or the sync diff) has to complete.
            "on": {"object": "UNRESOLVED"},
        })
    out["boundaries"] = reduced
    r.exact.append(f"boundaries ({len(reduced)} names and types)")
    if reduced:
        r.approximate.append(
            "boundary assignments (`on:` is UNRESOLVED — a snapshot records "
            "the boundary, not its faces)"
        )


def _reduce_setup(snapshot: dict, out: dict, r: Reduction) -> None:
    """Exact where the properties were captured; the pilot's were not."""
    setups = snapshot.get("setups") or {}
    sweeps_raw = list(snapshot.get("sweeps") or [])
    real_sweeps, variations = _split_sweeps(sweeps_raw)
    if variations:
        r.notes.append(
            f"{len(variations)} parametric variation string(s) in `sweeps` were "
            f"NOT read as sweeps (they are parametric tables)"
        )
    if not setups:
        out["setup"] = {
            "name": "Setup1",
            "solution_frequency": "UNRESOLVED",
            "max_passes": 6,
            "delta_s": 0.02,
        }
        r.missing.append(
            "setup properties (snapshot recorded none — capture_state's "
            "`get_properties` probe never fired before snapshot_version 2)"
        )
        return
    name, props = sorted(setups.items())[0]
    props = props or {}
    setup: dict[str, Any] = {"name": name}
    if not props:
        # The v1 defect: capture_state probed for `get_properties`, which
        # pyAEDT 1.3.0's Setup does not have, so every snapshot taken before
        # snapshot_version 2 recorded `{}` — including the pilot's, which is
        # ticket 11's acceptance target.
        r.missing.append(
            f"setup properties for {name!r} (the snapshot recorded none — "
            f"capture_state's `get_properties` probe never fired before "
            f"snapshot_version 2)"
        )
    frequency = _first(props, _FREQUENCY_KEYS)
    setup["solution_frequency"] = str(frequency) if frequency else "UNRESOLVED"
    if props and not frequency:
        r.missing.append(f"setup {name!r}: no solution frequency in properties")
    passes = _first(props, _PASSES_KEYS)
    if passes is not None:
        setup["max_passes"] = int(passes)
    delta = _first(props, _DELTAS_KEYS)
    if delta is not None:
        setup["delta_s"] = float(delta)
    sweep = _sweep_for(name, real_sweeps)
    if sweep:
        setup["sweep"] = sweep
        r.approximate.append(
            "setup.sweep (name only — a snapshot lists sweep names, not their "
            "frequency ranges)"
        )
    out["setup"] = setup
    r.exact.append(f"setup {name!r} ({len(props)} properties read)")
    if len(setups) > 1:
        r.notes.append(
            f"{len(setups)} setups captured; the spec holds one, so "
            f"{sorted(setups)[1:]} were dropped"
        )


def _split_sweeps(sweeps: list) -> tuple[list[str], list[str]]:
    real, variations = [], []
    for entry in sweeps:
        (variations if _VARIATION_RE.search(str(entry)) else real).append(str(entry))
    return real, variations


def _sweep_for(setup_name: str, sweeps: list[str]) -> dict | None:
    for entry in sweeps:
        if " : " not in entry:
            continue
        owner, sweep_name = entry.split(" : ", 1)
        if owner.strip() != setup_name or sweep_name.strip() == "LastAdaptive":
            continue
        return {
            "name": sweep_name.strip(),
            "type": "interpolating",
            "start": "UNRESOLVED",
            "stop": "UNRESOLVED",
            "count": 2,
        }
    return None


def _first(props: dict, keys) -> Any:
    for key in keys:
        if key in props and props[key] not in (None, ""):
            return props[key]
    return None


def load_snapshot(path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def to_yaml(spec: dict) -> str:
    """Spec dict as YAML. Falls back to JSON when PyYAML is absent."""
    try:
        import yaml
    except ImportError:
        return json.dumps(spec, indent=2, sort_keys=False) + "\n"
    return yaml.safe_dump(spec, sort_keys=False, allow_unicode=True, width=100)
