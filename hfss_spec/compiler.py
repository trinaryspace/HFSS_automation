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
  with its expression intact, so the parametric link is live in the UI. The
  setup's `Frequency` is the one deliberate exception — AEDT's adaptive
  frequency is a literal field, not an expression slot, and `_solution_frequency`
  records what that cost.
- **A write is not believed until the model repeats it.** The setup stage
  reads its own frequency, pass ceiling and delta-S back out and fails the
  build on a disagreement. patch-array-5800 solved for a month at 5GHz with a
  spec that said 5.8GHz, and no call ever raised; a stage that writes without
  looking cannot tell itself apart from a stage that does nothing.
- **Verification lines preserved.** Each stage still emits
  `PASS: <stage> <assertions>`, so the ledger and self-correction contracts are
  untouched. The Spine does not change; only who writes the code that walks it.

The Spine order is fixed here and matches SKILL.md exactly.

pyAEDT is imported lazily inside `build()`, so importing this module — which
the Tier 0 golden tests do — costs no license check and no AEDT.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from . import events
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
    """One line per stage, and nothing else — quiet by default.

    With a `state_dir`, every stage is also bracketed by a `stage.start` /
    `stage.end` event in `<state_dir>/events.jsonl` (run logging, ticket 03),
    the `stage.end` carrying this stage's own `PASS:` line as its verdict —
    or a `FAIL: <stage> ...` line when the stage raised. Nothing else is
    logged; the ledger, the Verification line and the event are one string.
    """

    results: list[StageResult] = field(default_factory=list)
    emit: Optional[Callable[[str], None]] = None
    state_dir: Optional[str] = None

    def event(self, name: str, **fields) -> None:
        """Record an event, when the log has a state dir; never raises."""
        if self.state_dir is not None:
            events.emit(self.state_dir, name, **fields)

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
        log.event("stage.start", stage=stage)
        started = time.monotonic()
        try:
            _STAGE_FUNCS[stage](spec, hfss, log)
        except Exception as exc:
            log.event("stage.end", stage=stage,
                      verdict=f"FAIL: {stage} {type(exc).__name__}: {exc}",
                      duration_ms=(time.monotonic() - started) * 1000)
            raise
        result = log.results[-1] if log.results and log.results[-1].stage == stage else None
        log.event("stage.end", stage=stage,
                  verdict=result.line if result is not None else None,
                  duration_ms=(time.monotonic() - started) * 1000)
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
        # `checkifmaterialexists` does not exist on pyAEDT 1.3.0 — found by the
        # first live acceptance run. `exists_material` is the real predicate,
        # and indexing is the pilot's shape (`materials[name]` returns None
        # rather than raising when the material is absent), so both are used:
        # the predicate where it exists, the index as the fallback.
        probe = getattr(hfss.materials, "exists_material", None)
        present = bool(probe(name)) if callable(probe) else \
            hfss.materials[name] is not None
        if present:
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
    """Write the setup, then make the model say back what it actually holds.

    The adaptive frequency is resolved to a literal here (`_solution_frequency`)
    and read back afterwards (`_verify_setup`), because a wrong adaptive
    frequency is the quietest way to build a model that solves cleanly and
    means nothing: the mesh converges somewhere the design was never about,
    and every number downstream inherits that.
    """
    setup_spec = spec.setup
    for existing in list(getattr(hfss, "setup_names", []) or []):
        if existing == setup_spec.name:
            hfss.delete_setup(setup_spec.name)
    frequency, frequency_hz = _solution_frequency(spec)
    setup = hfss.create_setup(setup_spec.name)
    # `create_setup` runs the requested name through `generate_unique_setup_name`
    # and silently returns `Setup2` when `Setup1` survived the delete above. The
    # sweep and every downstream report string are addressed by the spec's name,
    # so a rename has to stop the build rather than surface later as "unknown
    # setup". Observed in the same family on this box: patch-array-5800's
    # snapshot carries a sweep pyAEDT renamed to `Sweep1_BZ5US7`.
    written = getattr(setup, "name", setup_spec.name)
    if written != setup_spec.name:
        raise CompileError(
            f"create_setup({setup_spec.name!r}) returned {written!r} — a setup "
            f"by that name was still in the design and AEDT renamed the new one")
    # One `update(properties)` is one `EditSetup` carrying the whole arg.
    # Assigning through `props[...]` instead fires an `EditSetup` per key
    # (`SetupProps.__setitem__` calls `update()` when `auto_update` is on), so
    # the model passes through two states nobody asked for.
    if setup.update({"Frequency": frequency,
                     "MaximumPasses": setup_spec.max_passes,
                     "MaxDeltaS": setup_spec.delta_s}) is False:
        raise CompileError(f"setup {setup_spec.name!r}: update() reported failure")
    read_back = _verify_setup(setup, setup_spec, frequency, frequency_hz)
    sweep_name = None
    if setup_spec.sweep is not None:
        sweep = setup_spec.sweep
        sweep_name = sweep.name
        # `create_linear_count_sweep` takes a single `unit` plus bare float
        # endpoints — not strings carrying their own units, and the parameter
        # is `unit`, singular. Found by the first live acceptance run.
        unit, start, stop = _frequency_pair(spec, sweep)
        hfss.create_linear_count_sweep(
            setup=setup_spec.name,
            unit=unit,
            start_frequency=start,
            stop_frequency=stop,
            num_of_freq_points=sweep.count,
            name=sweep.name,
            sweep_type={"interpolating": "Interpolating",
                        "discrete": "Discrete",
                        "fast": "Fast"}[sweep.type],
        )
    log.record("setup_sweep", setup=setup_spec.name, frequency=frequency,
               passes=setup_spec.max_passes, sweep=sweep_name or "none",
               read_back=read_back)


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


def _frequency_pair(spec: DesignSpec, sweep) -> tuple[str, float, float]:
    """`(unit, start, stop)` for the sweep API's one-unit-plus-floats shape.

    Literal endpoints keep their own unit, so `3.2GHz` stays `("GHz", 3.2,
    4.2)` and reads correctly in the AEDT UI. An endpoint written as an
    expression over variables is evaluated against the spec's variable table
    and falls back to Hz, because there is no authored unit to preserve.
    """
    from .expressions import evaluate, resolve_all
    from .units import UnitError, parse_quantity

    try:
        start_q, stop_q = parse_quantity(sweep.start), parse_quantity(sweep.stop)
    except UnitError:
        scope = resolve_all(spec.variable_scope())
        start = evaluate(sweep.start, scope).si
        stop = evaluate(sweep.stop, scope).si
        return "Hz", start, stop
    unit = start_q.unit or "Hz"
    return unit, start_q.value, stop_q.to(unit).value


# --- the setup, and proving it landed ---------------------------------------

# Key spellings the model may use when it reports its own setup back. Only
# `Frequency`, `MaximumPasses` and `MaxDeltaS` are corpus-verified — all five
# real captured snapshots in `knowledge/cases/_snapshots/` spell them that way,
# as does patch-array-5800's own `model_snapshot.json`. The remaining frequency
# spellings are candidates for the object-oriented fetch view, which
# env-compat #16 records as naming the same property differently (`BasisOrder`
# vs `Basis Order`, `IsEnabled` vs `Enabled`). They are listed one by one on
# purpose: #16 also warns that a blanket "strip the spaces" rule collapses
# genuinely distinct keys, and this setup carries two of those — `MaximumPasses`
# (the adaptive-pass ceiling) sits beside `MaxPass` (the port solver's), and
# reading the wrong one would check nothing while looking like a check.
_FREQUENCY_KEYS = ("Frequency", "Solution Freq", "Solution Frequency",
                   "Adaptive Frequency")
_PASSES_KEYS = ("MaximumPasses", "Maximum Passes")
_DELTA_S_KEYS = ("MaxDeltaS", "Max Delta S")


def _solution_frequency(spec: DesignSpec) -> tuple[str, float]:
    """`setup.solution_frequency` as a LITERAL AEDT string, plus its value in Hz.

    A spec writes `solution_frequency: f0`, and `f0` must not be handed to AEDT
    as `f0`. The HfssDriven `Frequency` field is a literal frequency, not an
    expression slot: `EditSetup` takes an arg carrying a bare variable name
    without complaining and keeps the value the setup already had. That is how
    patch-array-5800 came to solve at pyAEDT's template default of `5GHz` while
    its spec said 5.8GHz — adapting the mesh at the bottom edge of its own
    5.0-6.5GHz sweep. Nothing looked wrong, because `MaximumPasses=15` in the
    very same `EditSetup` call landed exactly as asked: the transport was never
    the problem, the value was.

    A literal keeps its authored unit and a bare `f0` borrows the unit `f0` was
    written in, so the variable table and the setup dialog agree and read
    `5.8GHz` rather than `5800000000Hz`. Anything more involved than one
    variable name resolves to Hz — the same fallback, for the same reason, that
    `_frequency_pair` makes for sweep endpoints.
    """
    from .expressions import ExpressionError, as_quantity, evaluate, resolve_all
    from .units import FREQUENCY, UnitError, parse_quantity

    raw = spec.setup.solution_frequency
    try:
        literal = parse_quantity(raw)
    except UnitError:
        literal = None
    if literal is not None and literal.unit:
        if literal.dimension != FREQUENCY:
            raise CompileError(
                f"setup.solution_frequency {raw!r} is not a frequency")
        return str(literal), literal.si

    table = spec.variable_scope()
    try:
        value = evaluate(raw, resolve_all(table))
    except ExpressionError as exc:
        raise CompileError(f"setup.solution_frequency {raw!r}: {exc}") from None
    if value.dimension != FREQUENCY:
        raise CompileError(
            f"setup.solution_frequency {raw!r} resolves to {value}, "
            f"which is not a frequency")
    unit = "Hz"
    declared = table.get(raw) if isinstance(raw, str) else None
    if declared is not None:
        try:
            unit = parse_quantity(declared).unit or "Hz"
        except UnitError:
            unit = "Hz"
    return str(as_quantity(value, unit)), value.si


def _reported_setup(setup) -> list[tuple[str, dict]]:
    """The views the model can be asked for its own setup, most independent first.

    `properties` re-reads through AEDT on every access — `GetPropNames` /
    `GetPropValue` against the setup's child object — so inside the writing
    session it is the only view that can disagree with what was just written.
    `props` is pyAEDT's own copy of the arg it sent, so it can only ever agree
    with it; that makes it the last resort, and the Verification line names
    which view answered so a run that fell back to the weak one says so out
    loud. The strong reading of the same property is the one a *separate*
    session takes — `capture_state.py` did exactly that on patch-array-5800 and
    wrote `Frequency: "5GHz"` into the snapshot, where nothing compared it to
    the spec.

    Both views are wrapped: the raw COM surface is partially broken over gRPC
    on this box (env-compat #3), and a view that raises must fall through to
    the next rather than end the build.
    """
    views = []
    for name in ("properties", "props"):
        try:
            candidate = getattr(setup, name, None)
        except Exception:      # noqa: BLE001 - a broken fetch view is not an error
            continue
        if isinstance(candidate, dict) and candidate:
            views.append((name, candidate))
    return views


def _reported(props: dict, keys: tuple[str, ...]):
    """The first of `keys` the view actually carries, or None."""
    for key in keys:
        if key in props:
            return props[key]
    return None


def _verify_setup(setup, setup_spec, frequency: str, frequency_hz: float) -> str:
    """Read the setup back out of the model and refuse a write that did not land.

    This is the lesson of the patch-array-5800 solve, not a belt-and-braces
    extra. The compiler wrote a solution frequency, AEDT kept its own, no call
    raised, no log line differed, and a month of results came off a mesh
    converged 800MHz away from where the design lives. A build stage that
    writes and does not look is indistinguishable from one that does nothing.

    Returns the name of the view that answered, for the Verification line.
    """
    unreadable = None
    for view, props in _reported_setup(setup):
        reported = _reported(props, _FREQUENCY_KEYS)
        if reported is None:
            continue
        hz = _as_hz(reported)
        if hz is None:
            # This view names the field but answers in something that is not a
            # frequency. Ask the next view before failing: the file-shaped
            # `props` spelling is the one five real snapshots agree on, and a
            # build should not die because the object-oriented view formatted
            # itself in a way this box has never been observed to produce.
            unreadable = unreadable or (view, reported)
            continue
        if not math.isclose(hz, frequency_hz, rel_tol=1e-6):
            raise CompileError(
                f"setup {setup_spec.name!r}: the spec asked for "
                f"solution_frequency {setup_spec.solution_frequency!r} "
                f"({frequency}) but the model reports {reported!r} — the write "
                f"did not land, and a mesh adapted at the wrong frequency "
                f"invalidates every result from the solve")
        _verify_number(setup_spec.name, props, _PASSES_KEYS,
                       setup_spec.max_passes, "max_passes")
        _verify_number(setup_spec.name, props, _DELTA_S_KEYS,
                       setup_spec.delta_s, "delta_s")
        return view
    if unreadable is not None:
        view, reported = unreadable
        raise CompileError(
            f"setup {setup_spec.name!r}: the model reports its adaptive "
            f"frequency as {reported!r} in its {view} view, which does not read "
            f"as a frequency, so the write cannot be confirmed")
    raise CompileError(
        f"setup {setup_spec.name!r}: the model would not report its adaptive "
        f"frequency under any of {list(_FREQUENCY_KEYS)}, so the write cannot "
        f"be confirmed")


def _verify_number(setup_name: str, props: dict, keys: tuple[str, ...],
                   wanted, field: str) -> None:
    """A numeric setup property, checked only where the view reports it.

    Absent is not a failure: the object-oriented view spells some keys
    differently (env-compat #16), and guessing a spelling wrong would fail a
    correct build. A key that IS present and disagrees is a hard error.
    """
    reported = _reported(props, keys)
    if reported is None:
        return
    try:
        ok = math.isclose(float(reported), float(wanted), rel_tol=1e-9)
    except (TypeError, ValueError):
        ok = False
    if not ok:
        raise CompileError(
            f"setup {setup_name!r}: the spec asked for {field} {wanted!r} but "
            f"the model reports {reported!r} — the write did not land")


def _as_hz(reported):
    """A reported adaptive frequency in Hz, or None if it does not read as one.

    Everything is compared in Hz so `5.8GHz`, `5800000000` and `5.8e9Hz` are
    one value. A bare number is taken as Hz. None means the view answered with
    something that is not a frequency at all — a variable name that survived
    into the field, say — which is a reason to look elsewhere, not to pass.
    """
    from .units import FREQUENCY, UnitError, parse_quantity

    try:
        quantity = parse_quantity(reported)
    except UnitError:
        return None
    if quantity.unit:
        return quantity.si if quantity.dimension == FREQUENCY else None
    return quantity.value
