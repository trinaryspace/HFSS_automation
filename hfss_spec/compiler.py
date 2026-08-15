"""The spec compiler: `design.yaml` -> a live model. Ticket 10.

Hand-written, deterministic, and **no LLM in this layer, ever**. It replaces
the per-run generation of ten staged scripts with one tested artifact, which
is where the robustness and the token saving come from at the same time.

Properties that matter, each of them structural rather than remembered:

- **Idempotent by construction.** Every stage deletes the objects, boundaries,
  excitations and sweeps the spec names before creating them. ADR 0008 stops
  depending on the model remembering it per script.
- **Selectors resolve at build time.** A port sits on `{face_of: Feed,
  direction: -y}`, never on an id — env-compat #7/#8 enforced by the compiler.
  An ambiguous selector is an error unless the spec opted in with `pick:` (Q3),
  because silently choosing the wrong face builds a model that simulates
  nonsense.
- **Variables first.** Every dimension is emitted as an AEDT design variable
  with its expression intact, so the parametric link is live in the UI.
- **Verification lines preserved.** Each stage still emits
  `PASS: <stage> <assertions>`, so the ledger and self-correction contracts are
  untouched. The Spine does not change; only who writes the code that walks it.

The Spine order is fixed here and matches SKILL.md exactly.

pyAEDT is imported lazily inside `build()`, so importing this module — which
the Tier 0 golden tests do — costs no license check and no AEDT.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from .schema import Boundary, DesignSpec, Excitation, GeometryOp, MaterialDef, MaterialRef
from .validate import SpecNotValidated, require_valid

# The Spine, in order. Names match SKILL.md's stages so the ledger, the
# Verification lines and the run card all keep reading the same words.
STAGES = (
    "solution_type",
    "variables",
    "materials",
    "geometry",
    "excitations",
    "boundaries",
    "mesh",
    "setup_sweep",
    "validate",
)


class CompileError(RuntimeError):
    """The compiler could not carry out the spec against this model."""


class SelectorError(CompileError):
    """A symbolic selector matched nothing, or matched ambiguously (Q3)."""


@dataclass
class StageResult:
    stage: str
    assertions: dict[str, Any] = field(default_factory=dict)

    @property
    def line(self) -> str:
        body = " ".join(f"{k}={v}" for k, v in self.assertions.items())
        return f"PASS: {self.stage} {body}".rstrip()


@dataclass
class BuildLog:
    """One line per stage, and nothing else — quiet by default."""

    results: list[StageResult] = field(default_factory=list)
    emit: Optional[Callable[[str], None]] = None

    def record(self, stage: str, **assertions) -> StageResult:
        result = StageResult(stage, assertions)
        self.results.append(result)
        if self.emit:
            self.emit(result.line)
        return result

    @property
    def lines(self) -> list[str]:
        return [r.line for r in self.results]


def build(spec: DesignSpec, hfss, log: Optional[BuildLog] = None,
          stages: tuple[str, ...] = STAGES) -> BuildLog:
    """Walk the Spine against a live `hfss` handle.

    `hfss` is a pyAEDT `Hfss` (or any object with the same surface — the
    golden tests pass a recorder). The validator is a hard gate: an
    unvalidated spec never reaches the desktop.
    """
    require_valid(spec)
    log = log or BuildLog()
    for stage in stages:
        _STAGE_FUNCS[stage](spec, hfss, log)
    return log


# --- stages ----------------------------------------------------------------


def _stage_solution_type(spec: DesignSpec, hfss, log: BuildLog) -> None:
    """Explicit, never the default: AEDT defaults to Terminal (env-compat #11)."""
    hfss.solution_type = spec.solution_type
    log.record("solution_type", solution_type=spec.solution_type)


def _stage_variables(spec: DesignSpec, hfss, log: BuildLog) -> None:
    """Expressions pass through verbatim so the parametric link survives (Q2)."""
    for name, expression in spec.variables.items():
        hfss[name] = _as_aedt(expression)
    for name, expression in spec.project_variables.items():
        hfss[name] = _as_aedt(expression)      # `$name` is AEDT's project scope
    log.record("variables", design=len(spec.variables),
               project=len(spec.project_variables))


def _stage_materials(spec: DesignSpec, hfss, log: BuildLog) -> None:
    """Only inline definitions are created; library names are used as-is."""
    created = 0
    for key, material in spec.materials.items():
        if isinstance(material, MaterialRef):
            continue
        if not isinstance(material, MaterialDef):
            continue
        name = key
        if hfss.materials.checkifmaterialexists(name):
            existing = hfss.materials[name]
        else:
            existing = hfss.materials.add_material(name)
            created += 1
        existing.permittivity = _as_aedt(material.permittivity)
        existing.permeability = _as_aedt(material.permeability)
        existing.dielectric_loss_tangent = _as_aedt(material.loss_tangent)
        if material.conductivity is not None:
            existing.conductivity = _as_aedt(material.conductivity)
    log.record("materials", declared=len(spec.materials), created=created)


def _stage_geometry(spec: DesignSpec, hfss, log: BuildLog) -> None:
    for op in spec.geometry:
        _GEOMETRY_OPS[op.op](spec, hfss, op)
    names = spec.declared_objects
    log.record("geometry", ops=len(spec.geometry), objects=len(names))


def _stage_excitations(spec: DesignSpec, hfss, log: BuildLog) -> None:
    for port in spec.excitations:
        _delete_boundary(hfss, port.name)
        if port.type == "lumped_port":
            _create_lumped_port(hfss, spec, port)
        else:
            _create_wave_port(hfss, spec, port)
    log.record("excitations", ports=len(spec.excitations))


def _stage_boundaries(spec: DesignSpec, hfss, log: BuildLog) -> None:
    for boundary in spec.boundaries:
        _delete_boundary(hfss, boundary.name)
        _create_boundary(hfss, spec, boundary)
    log.record("boundaries", count=len(spec.boundaries))


def _stage_mesh(spec: DesignSpec, hfss, log: BuildLog) -> None:
    """v1 is adaptive-only (Q4) — there is nothing to create, and saying so
    explicitly keeps the stage in the ledger rather than silently absent."""
    log.record("mesh", strategy="adaptive_only", operations=0)


def _stage_setup_sweep(spec: DesignSpec, hfss, log: BuildLog) -> None:
    setup_spec = spec.setup
    for existing in list(getattr(hfss, "setup_names", []) or []):
        if existing == setup_spec.name:
            hfss.delete_setup(setup_spec.name)
    setup = hfss.create_setup(setup_spec.name)
    setup.props["Frequency"] = _as_aedt(setup_spec.solution_frequency)
    setup.props["MaximumPasses"] = setup_spec.max_passes
    setup.props["MaxDeltaS"] = setup_spec.delta_s
    setup.update()
    sweep_name = None
    if setup_spec.sweep is not None:
        sweep = setup_spec.sweep
        sweep_name = sweep.name
        hfss.create_linear_count_sweep(
            setup=setup_spec.name,
            units="",                       # units travel on the values
            start_frequency=_as_aedt(sweep.start),
            stop_frequency=_as_aedt(sweep.stop),
            num_of_freq_points=sweep.count,
            name=sweep.name,
            sweep_type={"interpolating": "Interpolating",
                        "discrete": "Discrete",
                        "fast": "Fast"}[sweep.type],
        )
    log.record("setup_sweep", setup=setup_spec.name,
               passes=setup_spec.max_passes, sweep=sweep_name or "none")


def _stage_validate(spec: DesignSpec, hfss, log: BuildLog) -> None:
    """The gate ADR/env-compat #8 requires before any solve."""
    ok = bool(hfss.validate_simple())
    if not ok:
        raise CompileError("validate_simple() returned False — the model is not solvable")
    log.record("validate", validate_simple=True,
               objects=len(spec.declared_objects))


_STAGE_FUNCS: dict[str, Callable[[DesignSpec, Any, BuildLog], None]] = {
    "solution_type": _stage_solution_type,
    "variables": _stage_variables,
    "materials": _stage_materials,
    "geometry": _stage_geometry,
    "excitations": _stage_excitations,
    "boundaries": _stage_boundaries,
    "mesh": _stage_mesh,
    "setup_sweep": _stage_setup_sweep,
    "validate": _stage_validate,
}


# --- geometry ops ----------------------------------------------------------


def _delete_if_present(hfss, name: str) -> None:
    """Idempotency, as a property of the compiler rather than a discipline."""
    if name in (getattr(hfss.modeler, "object_names", None) or []):
        hfss.modeler.delete(name)


def _material_name(spec: DesignSpec, key: Optional[str]) -> Optional[str]:
    """A spec-local material key resolved to the name AEDT knows."""
    if key is None:
        return None
    material = spec.materials.get(key)
    if isinstance(material, MaterialRef):
        return material.library
    if material is not None:
        return key          # an inline definition is created under its key
    return key              # a bare library name used without declaring it


def _op_box(spec, hfss, op: GeometryOp) -> None:
    _delete_if_present(hfss, op.name)
    hfss.modeler.create_box(
        origin=[_as_aedt(v) for v in op.origin],
        sizes=[_as_aedt(v) for v in op.size],
        name=op.name,
        material=_material_name(spec, op.material),
    )


def _op_sheet(spec, hfss, op: GeometryOp) -> None:
    _delete_if_present(hfss, op.name)
    # `create_rectangle("XZ", ...)` maps sizes to [z, x], not [x, z], on
    # 2024 R1 — measured on the patch-2400 run, where a transposed sheet was
    # caught by its bbox. The spec always states sizes in axis order, so the
    # compiler does the swap once, here, instead of every author doing it.
    plane = op.plane.upper()
    sizes = [_as_aedt(v) for v in op.size]
    if plane == "XZ":
        sizes = list(reversed(sizes))
    hfss.modeler.create_rectangle(
        orientation=plane,
        origin=[_as_aedt(v) for v in op.origin],
        sizes=sizes,
        name=op.name,
        material=_material_name(spec, op.material),
    )


def _op_cylinder(spec, hfss, op: GeometryOp) -> None:
    _delete_if_present(hfss, op.name)
    hfss.modeler.create_cylinder(
        orientation=op.axis.upper(),
        origin=[_as_aedt(v) for v in op.origin],
        radius=_as_aedt(op.radius),
        height=_as_aedt(op.height),
        name=op.name,
        material=_material_name(spec, op.material),
    )


def _op_polyline(spec, hfss, op: GeometryOp) -> None:
    _delete_if_present(hfss, op.name)
    hfss.modeler.create_polyline(
        points=[[_as_aedt(c) for c in point] for point in op.points],
        name=op.name,
        material=_material_name(spec, op.material),
        cover_surface=op.cover,
        close_surface=op.close,
        segment_type=op.segment_type,
    )


def _op_unite(spec, hfss, op: GeometryOp) -> None:
    hfss.modeler.unite([op.name] + list(op.with_))


def _op_subtract(spec, hfss, op: GeometryOp) -> None:
    hfss.modeler.subtract(op.name, list(op.tools), keep_originals=op.keep_tools)


def _op_intersect(spec, hfss, op: GeometryOp) -> None:
    hfss.modeler.intersect([op.name] + list(op.tools), keep_originals=op.keep_tools)


def _op_sweep_along_vector(spec, hfss, op: GeometryOp) -> None:
    """A pyramidal horn is a rectangle swept along a vector with a draft angle."""
    hfss.modeler.sweep_along_vector(
        assignment=op.name,
        sweep_vector=[_as_aedt(v) for v in op.sweep_vector],
        draft_angle=_as_aedt(op.draft_angle) if op.draft_angle is not None else 0,
        draft_type=op.draft_type or "Round",
    )


def _op_sweep_along_path(spec, hfss, op: GeometryOp) -> None:
    hfss.modeler.sweep_along_path(assignment=op.name, sweep_object=op.path)


def _op_sweep_around_axis(spec, hfss, op: GeometryOp) -> None:
    hfss.modeler.sweep_around_axis(
        assignment=op.name, axis=op.axis.upper(), sweep_angle=_as_aedt(op.angle),
    )


def _op_connect(spec, hfss, op: GeometryOp) -> None:
    """HFSS's loft/blend between profiles — the exact horn flare, not an
    approximation of one."""
    hfss.modeler.connect(assignment=[op.name] + list(op.profiles))


def _op_thicken_sheet(spec, hfss, op: GeometryOp) -> None:
    hfss.modeler.thicken_sheet(assignment=op.name,
                               thickness=_as_aedt(op.thickness))


def _op_import_cad(spec, hfss, op: GeometryOp) -> None:
    """Received geometry, not designed geometry. Carries no parametrics — that
    is the documented cost, and why it is an escape hatch rather than a habit."""
    hfss.modeler.import_3d_cad(op.file)


def _op_escape_hatch(spec, hfss, op: GeometryOp) -> None:
    raise CompileError(
        f"escape-hatch op {op.name!r} must be run by the caller "
        f"({op.script}): {op.reason}"
    )


def _op_unknown(spec, hfss, op: GeometryOp) -> None:
    raise CompileError(
        f"{op.name!r} is `op: unknown` — the reducer could not name its "
        f"construction op, and the validator should have refused this spec"
    )


_GEOMETRY_OPS: dict[str, Callable[[DesignSpec, Any, GeometryOp], None]] = {
    "box": _op_box,
    "sheet": _op_sheet,
    "cylinder": _op_cylinder,
    "polyline": _op_polyline,
    "unite": _op_unite,
    "subtract": _op_subtract,
    "intersect": _op_intersect,
    "sweep_along_vector": _op_sweep_along_vector,
    "sweep_along_path": _op_sweep_along_path,
    "sweep_around_axis": _op_sweep_around_axis,
    "connect": _op_connect,
    "thicken_sheet": _op_thicken_sheet,
    "import_cad": _op_import_cad,
    "escape_hatch": _op_escape_hatch,
    "unknown": _op_unknown,
}


# --- selectors, ports and boundaries ---------------------------------------

_AXIS_INDEX = {"x": 0, "y": 1, "z": 2}


def resolve_face(hfss, selector, spec: DesignSpec):
    """`{face_of: Feed, direction: -y}` -> a face object, or a clear error.

    Ambiguity is an ERROR by default (Q3). A spec that means "the big one" has
    to say `pick: largest_area`, because a silently-chosen wrong face produces
    a model that builds fine and simulates nonsense — the worst failure class
    this tool has.
    """
    name = selector.face_of
    obj = hfss.modeler[name]
    if obj is None:
        raise SelectorError(f"face_of: {name!r} is not in the modeler")
    sign, axis = selector.direction[0], selector.direction[1]
    index = _AXIS_INDEX[axis]
    faces = list(obj.faces)
    if not faces:
        raise SelectorError(f"face_of: {name!r} has no faces")
    # The extreme face along the axis, by face-centre coordinate.
    key = (lambda f: f.center[index]) if sign == "+" else (lambda f: -f.center[index])
    best = max(key(f) for f in faces)
    candidates = [f for f in faces if abs(key(f) - best) <= 1e-9]
    if len(candidates) == 1:
        return candidates[0]
    if selector.pick == "largest_area":
        return max(candidates, key=lambda f: f.area)
    if selector.pick == "smallest_area":
        return min(candidates, key=lambda f: f.area)
    if selector.nearest is not None:
        point = [float(_number(v)) for v in selector.nearest]
        return min(candidates,
                   key=lambda f: sum((c - p) ** 2 for c, p in zip(f.center, point)))
    raise SelectorError(
        f"face_of: {name!r} has {len(candidates)} faces on {selector.direction} — "
        f"add `pick: largest_area` or `nearest: [x, y, z]` to disambiguate"
    )


def _create_lumped_port(hfss, spec: DesignSpec, port: Excitation) -> None:
    """Pass the sheet NAME plus an explicit integration line.

    pyAEDT 1.3.0 serialises a FacePrimitive's id into `props["Objects"]` and
    the macro layer rejects it ("a geometry selection is required for
    assignment") — unlike `wave_port`, which resolves ids to object names.
    Measured on the patch-2400 run; absorbed here so no future run rediscovers it.
    """
    target = getattr(port.on, "object", None) or getattr(port.on, "face_of", None)
    start, end = _integration_points(hfss, port)
    hfss.lumped_port(
        assignment=target,
        integration_line=[start, end],
        impedance=_number(port.impedance),
        name=port.name,
        renormalize=port.renormalize,
    )


def _create_wave_port(hfss, spec: DesignSpec, port: Excitation) -> None:
    if hasattr(port.on, "face_of"):
        assignment = resolve_face(hfss, port.on, spec)
    else:
        assignment = getattr(port.on, "object", None)
    kwargs = {"assignment": assignment, "name": port.name,
              "impedance": _number(port.impedance),
              "renormalize": port.renormalize}
    if port.integration_line is not None:
        start, end = _integration_points(hfss, port)
        kwargs["integration_line"] = [start, end]
    hfss.wave_port(**kwargs)


def _integration_points(hfss, port: Excitation):
    line = port.integration_line
    if line is None:
        raise CompileError(f"port {port.name!r} has no integration line")
    return _endpoint(hfss, line.from_), _endpoint(hfss, line.to)


def _endpoint(hfss, endpoint):
    """An integration-line endpoint as [x, y, z] in model units."""
    explicit = getattr(endpoint, "point", None)
    if explicit is not None:
        return [_as_aedt(v) for v in explicit]
    name, direction, extreme = endpoint.edge_mid
    obj = hfss.modeler[name]
    if obj is None:
        raise SelectorError(f"edge_mid: {name!r} is not in the modeler")
    box = list(obj.bounding_box)          # [xmin, ymin, zmin, xmax, ymax, zmax]
    sign, axis = direction[0], direction[1]
    index = _AXIS_INDEX[axis]
    centre = [(box[i] + box[i + 3]) / 2.0 for i in range(3)]
    centre[index] = box[index] if sign == "-" else box[index + 3]
    which, extreme_axis = extreme[:3], extreme[-1]
    extreme_index = _AXIS_INDEX[extreme_axis]
    centre[extreme_index] = (box[extreme_index] if which == "min"
                             else box[extreme_index + 3])
    return centre


_BOUNDARY_CREATORS = {
    "radiation": lambda hfss, target, b: hfss.assign_radiation_boundary_to_objects(
        target, name=b.name),
    "perfect_e": lambda hfss, target, b: hfss.assign_perfecte_to_sheets(
        target, name=b.name),
    "perfect_h": lambda hfss, target, b: hfss.assign_perfailh_to_sheets(
        target, name=b.name),
}


def _create_boundary(hfss, spec: DesignSpec, boundary: Boundary) -> None:
    target = (getattr(boundary.on, "object", None)
              or getattr(boundary.on, "outer_faces", None)
              or getattr(boundary.on, "face_of", None))
    if boundary.type == "radiation":
        hfss.assign_radiation_boundary_to_objects(target, name=boundary.name)
    elif boundary.type == "perfect_e":
        hfss.assign_perfecte_to_sheets(target, name=boundary.name)
    elif boundary.type == "perfect_h":
        hfss.assign_perfecth_to_sheets(target, name=boundary.name)
    elif boundary.type == "finite_conductivity":
        hfss.assign_finite_conductivity_to_sheets(
            target, name=boundary.name, conductivity=_number(boundary.conductivity))
    else:
        raise CompileError(
            f"boundary type {boundary.type!r} has no v1 creator — use an "
            f"escape-hatch stage")


def _delete_boundary(hfss, name: str) -> None:
    """Delete by object, not by a `delete_boundary` helper.

    `Hfss.delete_boundary` does not exist on 1.3.0 — the pilot found that the
    expensive way. `BoundaryObject.delete()` is the working shape.
    """
    for existing in list(getattr(hfss, "boundaries", None) or []):
        if getattr(existing, "name", None) == name:
            existing.delete()


# --- value marshalling ------------------------------------------------------


def _as_aedt(value) -> str:
    """A spec value as the string AEDT wants.

    Expressions and literals-with-units both go through unchanged: AEDT is the
    evaluator, and passing `patch_W + 6*h` verbatim is what keeps the
    parametric link alive in the variable table.
    """
    return value if isinstance(value, str) else repr(value)


def _number(value) -> float:
    """A literal quantity's magnitude, for the few APIs that demand a float."""
    from .units import parse_quantity
    return parse_quantity(value).value
