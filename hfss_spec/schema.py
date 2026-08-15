"""Design Spec schema v1 — the artifact that replaces ten generated scripts.

Ticket 07. Sections mirror the Spine so the mapping stays obvious, and the
three decisions that carry the value are encoded as *types* rather than as
rules someone has to remember:

- **Symbolic selectors.** No field anywhere accepts a face or edge id. A port
  sits on `{face_of: Feed, direction: -y}`, resolved against the live model at
  build time. That is env-compat #7/#8 made structural.
- **Mandatory units.** Every dimensional value is a literal-with-unit or an
  expression over variables. A bare float is legal only where the quantity is
  genuinely dimensionless.
- **Variables first.** Every geometry dimension is a variable reference or a
  literal-with-unit, and the compiler emits AEDT design variables for all of
  them, so PLAN.md's full-parameterization rule is mechanical.

Scope comes from the Q1-Q8 answers in `phase-2-detail.md`: full geometry
including sweeps and lofts on the **native HFSS modeler** (Q1c), expressions in
variables (Q2), ambiguous selectors refuse by default (Q3), adaptive-only mesh
(Q4), setup and sweep in the schema (Q6), one spec per design (Q8).

Five real captured models shaped the non-geometry sections (ticket 12a), and
four of its findings are visible here as fields that a from-scratch design
would have missed: project-scoped `$vars`, inline material definitions,
metal-as-boundary alongside metal-as-material, and sweeps that must not be
confused with AEDT's parametric variation strings.
"""

from __future__ import annotations

import json
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from .expressions import ExpressionError, references
from .units import UnitError, parse_quantity

SPEC_VERSION = 1

# Geometry ops, per ticket 07's Comments. Every one exists on `Modeler3D` and
# is already in the KB -- (c) costs ops in a schema, not a CAD kernel.
PRIMITIVE_OPS = ("box", "sheet", "cylinder", "polyline")
BOOLEAN_OPS = ("unite", "subtract", "intersect")
SWEEP_OPS = ("sweep_along_vector", "sweep_along_path", "sweep_around_axis", "connect")
OTHER_OPS = ("thicken_sheet", "import_cad", "escape_hatch")
# `unknown` is the reducer's honest output (ticket 12a): an object that exists
# in a captured model whose construction op a bounding box cannot name. It is a
# first-class value so the drift is visible (Q5) — and the validator refuses to
# let one reach the compiler.
REDUCER_OPS = ("unknown",)
GEOMETRY_OPS = PRIMITIVE_OPS + BOOLEAN_OPS + SWEEP_OPS + OTHER_OPS + REDUCER_OPS

AXES = ("x", "y", "z")
DIRECTIONS = ("+x", "-x", "+y", "-y", "+z", "-z")
PLANES = ("xy", "yz", "xz")


class SpecModel(BaseModel):
    """Base: unknown fields are an error, not a shrug."""

    model_config = ConfigDict(extra="forbid", validate_assignment=True)


# --- values ---------------------------------------------------------------

# A dimensional value: a literal with a unit ("52.64mm"), an expression over
# variables ("patch_W + 6*h"), or a bare number where dimensionless is meant.
Expr = Union[str, float, int]


def _check_expression(raw: Expr, field: str) -> Expr:
    """A dimensional field must parse as a quantity or as an expression."""
    if isinstance(raw, bool):
        raise ValueError(f"{field}: a boolean is not a dimensional value")
    if isinstance(raw, (int, float)):
        return raw
    text = str(raw).strip()
    if not text:
        raise ValueError(f"{field}: empty value")
    try:
        parse_quantity(text)
        return text
    except UnitError:
        pass
    # Not a literal, so it must be a well-formed expression over names.
    if not references(text):
        raise ValueError(
            f"{field}: {raw!r} is neither a number with a unit "
            f"(e.g. '52.64mm') nor an expression over variables"
        )
    return text


# --- selectors ------------------------------------------------------------


class FaceOf(SpecModel):
    """The face of an object on a given side. Ambiguity is an ERROR (Q3)."""

    face_of: str
    direction: Literal["+x", "-x", "+y", "-y", "+z", "-z"]
    pick: Optional[Literal["largest_area", "smallest_area"]] = None
    nearest: Optional[list[Expr]] = Field(default=None, min_length=3, max_length=3)

    @model_validator(mode="after")
    def _one_tiebreak(self):
        if self.pick is not None and self.nearest is not None:
            raise ValueError("give either `pick` or `nearest`, not both")
        return self


class ObjectRef(SpecModel):
    """A whole object, by name."""

    object: str


class OuterFaces(SpecModel):
    """Every outward face of an object — the radiation-boundary shape."""

    outer_faces: str


Selector = Annotated[Union[FaceOf, ObjectRef, OuterFaces], Field(union_mode="left_to_right")]


class EdgeMid(SpecModel):
    """Midpoint of an object's edge, for integration lines."""

    edge_mid: list[str] = Field(min_length=3, max_length=3)


class Point(SpecModel):
    """An explicit point, in spec units."""

    point: list[Expr] = Field(min_length=3, max_length=3)


Endpoint = Annotated[Union[EdgeMid, Point], Field(union_mode="left_to_right")]


class IntegrationLine(SpecModel):
    """A port's integration line, given by two symbolic endpoints."""

    from_: Endpoint = Field(alias="from")
    to: Endpoint

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


# --- provenance and target -------------------------------------------------


class Provenance(SpecModel):
    """Where the numbers came from, and which reading is canonical.

    `canonical_reading` is perf-refactor ticket 09 landing as data instead of
    prose: for a paper-sourced design the Clarification block has to record
    which of Table / Figure / equations won, and the pilot proved that an
    unrecorded answer costs twenty hours.
    """

    source: str
    canonical_reading: Literal["Table", "Figure", "equations", "closed-form", "measured"]
    case: Optional[str] = None
    notes: Optional[str] = None


class Target(SpecModel):
    """The design's headline goal, and how close counts."""

    quantity: Literal["resonant_frequency", "center_frequency",
                      "characteristic_impedance", "impedance",
                      "gain", "bandwidth"]
    value: Expr
    tolerance_pct: float = Field(gt=0, le=100)

    @field_validator("value")
    @classmethod
    def _dimensional(cls, v):
        return _check_expression(v, "target.value")


# --- materials -------------------------------------------------------------


class MaterialDef(SpecModel):
    """An inline material definition.

    12a found `myfr4` on the coplanar model — a user-defined material with no
    library entry. A schema with only library references cannot describe it.
    """

    permittivity: Expr = 1.0
    permeability: Expr = 1.0
    loss_tangent: Expr = 0.0
    conductivity: Optional[Expr] = None


class MaterialRef(SpecModel):
    """A reference to an AEDT library material."""

    library: str


Material = Annotated[Union[MaterialRef, MaterialDef], Field(union_mode="left_to_right")]


# --- geometry --------------------------------------------------------------


class GeometryOp(SpecModel):
    """One geometry operation. `op` selects which fields are meaningful.

    Kept as a single permissive model rather than a discriminated union of
    fifteen classes: the per-op required-field check lives in `_op_fields`
    below, which keeps the error messages in one place and readable.
    """

    op: Literal[GEOMETRY_OPS]  # type: ignore[valid-type]
    name: str
    material: Optional[str] = None

    # primitives
    origin: Optional[list[Expr]] = None
    size: Optional[list[Expr]] = None
    plane: Optional[Literal["xy", "yz", "xz"]] = None
    radius: Optional[Expr] = None
    height: Optional[Expr] = None
    axis: Optional[Literal["x", "y", "z"]] = None
    points: Optional[list[list[Expr]]] = None
    cover: bool = False
    close: bool = False
    segment_type: Optional[Literal["Line", "Arc", "Spline", "AngularArc"]] = None

    # booleans
    tools: Optional[list[str]] = None
    with_: Optional[list[str]] = Field(default=None, alias="with")
    keep_tools: bool = False

    # sweeps and lofts (Q1c)
    sweep_vector: Optional[list[Expr]] = None
    draft_angle: Optional[Expr] = None
    draft_type: Optional[Literal["Round", "Natural", "Extended"]] = None
    path: Optional[str] = None
    profiles: Optional[list[str]] = None
    angle: Optional[Expr] = None
    thickness: Optional[Expr] = None

    # received geometry / escape hatch
    file: Optional[str] = None
    script: Optional[str] = None
    reason: Optional[str] = None
    provides: Optional[list[str]] = None

    # reducer output (op: unknown) — the captured evidence, carried so a human
    # or the sync diff can complete the op without re-capturing
    bbox: Optional[list[float]] = Field(default=None, min_length=6, max_length=6)
    bbox_units: Optional[str] = None
    derived_from: Optional[Literal["bbox"]] = None

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    @model_validator(mode="after")
    def _required_per_op(self):
        required, dimensional = _op_fields(self.op)
        missing = [f for f in required if getattr(self, f, None) in (None, [])]
        if missing:
            raise ValueError(
                f"geometry op {self.op!r} ({self.name}) needs: {', '.join(missing)}"
            )
        for field in dimensional:
            value = getattr(self, field, None)
            if value is None:
                continue
            if isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, list):
                        for j, deep in enumerate(item):
                            _check_expression(deep, f"{self.name}.{field}[{i}][{j}]")
                    else:
                        _check_expression(item, f"{self.name}.{field}[{i}]")
            else:
                _check_expression(value, f"{self.name}.{field}")
        return self

    @property
    def buildable(self) -> bool:
        """False for a reducer placeholder the compiler cannot execute."""
        return self.op != "unknown"

    @property
    def object_names(self) -> list[str]:
        """Every object name this op leaves behind."""
        if self.op == "escape_hatch":
            return list(self.provides or [])
        return [self.name]

    @property
    def consumes(self) -> list[str]:
        """Object names this op reads (and may destroy)."""
        names: list[str] = []
        if self.tools:
            names += list(self.tools)
        if self.with_:
            names += list(self.with_)
        if self.profiles:
            names += list(self.profiles)
        if self.path:
            names.append(self.path)
        return names


def _op_fields(op: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """(required fields, dimensional fields) for a geometry op."""
    table: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
        "box": (("origin", "size"), ("origin", "size")),
        "sheet": (("origin", "size", "plane"), ("origin", "size")),
        "cylinder": (("origin", "radius", "height", "axis"), ("origin", "radius", "height")),
        "polyline": (("points",), ("points",)),
        "unite": (("with_",), ()),
        "subtract": (("tools",), ()),
        "intersect": (("tools",), ()),
        "sweep_along_vector": (("sweep_vector",), ("sweep_vector", "draft_angle")),
        "sweep_along_path": (("path",), ()),
        "sweep_around_axis": (("axis", "angle"), ("angle",)),
        "connect": (("profiles",), ()),
        "thicken_sheet": (("thickness",), ("thickness",)),
        "import_cad": (("file",), ()),
        "escape_hatch": (("script", "reason"), ()),
        "unknown": (("bbox",), ()),
    }
    return table.get(op, ((), ()))


# --- excitations, boundaries, mesh, setup ----------------------------------


class Excitation(SpecModel):
    """A port. Lumped and wave ports only in v1."""

    name: str
    type: Literal["lumped_port", "wave_port"]
    on: Selector
    integration_line: Optional[IntegrationLine] = None
    impedance: Expr = "50ohm"
    renormalize: bool = True

    @field_validator("impedance")
    @classmethod
    def _dimensional(cls, v):
        return _check_expression(v, "excitations.impedance")

    @model_validator(mode="after")
    def _lumped_needs_a_line(self):
        if self.type == "lumped_port" and self.integration_line is None:
            raise ValueError(
                f"excitation {self.name!r}: a lumped port needs an integration_line "
                "(pyAEDT 1.3.0 rejects a bare face — see the patch-2400 run)"
            )
        return self


class Boundary(SpecModel):
    """A boundary condition.

    `perfect_e` on a sheet is how real models assign metal — 12a found
    `antennaMetal` / `groundMetal` as Perfect E boundaries, not materials. Both
    patterns are legal and the schema must express both (findings, ticket 12a).
    """

    name: str
    type: Literal["radiation", "perfect_e", "perfect_h", "finite_conductivity",
                  "symmetry", "impedance", "fe_bi"]
    on: Selector
    conductivity: Optional[Expr] = None


class Mesh(SpecModel):
    """Mesh strategy. v1 is adaptive-only (Q4); operations go via escape hatch."""

    type: Literal["adaptive_only"] = "adaptive_only"


class Sweep(SpecModel):
    """A frequency sweep.

    Not to be confused with AEDT's parametric variation strings, which the
    reducer found sharing the same `sweeps` list on real models
    (`"Setup1 - AirGap='25mm' ... : Table"`). Those are parametric tables and
    never become a Sweep here.
    """

    name: str = "Sweep1"
    type: Literal["interpolating", "discrete", "fast"] = "interpolating"
    start: Expr
    stop: Expr
    count: int = Field(gt=1)

    @field_validator("start", "stop")
    @classmethod
    def _dimensional(cls, v):
        return _check_expression(v, "setup.sweep")


class Setup(SpecModel):
    """The solution setup. Solve submission stays imperative (ADR 0006)."""

    name: str = "Setup1"
    solution_frequency: Expr
    max_passes: int = Field(default=6, gt=0)
    delta_s: float = Field(default=0.02, gt=0, lt=1)
    sweep: Optional[Sweep] = None

    @field_validator("solution_frequency")
    @classmethod
    def _dimensional(cls, v):
        return _check_expression(v, "setup.solution_frequency")


# --- the spec --------------------------------------------------------------


class DesignSpec(SpecModel):
    """One design. The single source of truth for a simulation."""

    spec_version: Literal[1] = 1
    name: str
    recipe: str
    solution_type: Literal["Modal", "Terminal"] = "Modal"   # explicit, EC#11
    provenance: Provenance
    target: Optional[Target] = None

    variables: dict[str, Expr] = Field(default_factory=dict)
    # Project-scoped AEDT variables (`$losstan`), a separate namespace from
    # design variables — 12a found one live on the coplanar model, and a
    # reducer that flattens the two writes back to the wrong place.
    project_variables: dict[str, Expr] = Field(default_factory=dict)

    materials: dict[str, Material] = Field(default_factory=dict)
    geometry: list[GeometryOp] = Field(default_factory=list)
    excitations: list[Excitation] = Field(default_factory=list)
    boundaries: list[Boundary] = Field(default_factory=list)
    mesh: list[Mesh] = Field(default_factory=lambda: [Mesh()])
    setup: Setup
    qa_signals: list[Literal["convergence", "ports_excited", "in_band_resonance",
                             "energy_pass", "gain_plausible"]] = Field(default_factory=list)

    # Anything the reducer could not identify (12a). Never silently dropped:
    # an unresolved entry here is what makes the drift visible (Q5).
    unresolved: list[dict[str, Any]] = Field(default_factory=list)

    @field_validator("variables", "project_variables")
    @classmethod
    def _variable_names(cls, table: dict[str, Expr], info):
        prefix = "$" if info.field_name == "project_variables" else ""
        for name in table:
            if prefix and not name.startswith("$"):
                raise ValueError(f"project variable {name!r} must start with '$'")
            if not prefix and name.startswith("$"):
                raise ValueError(
                    f"variable {name!r} is project-scoped; put it in project_variables"
                )
        return table

    @property
    def declared_objects(self) -> list[str]:
        """Every object name the geometry section leaves in the modeler."""
        names: list[str] = []
        for op in self.geometry:
            for name in op.object_names:
                if name not in names:
                    names.append(name)
        return names

    @property
    def escape_hatch_count(self) -> int:
        """The metric that says whether the schema is right."""
        return sum(1 for op in self.geometry if op.op == "escape_hatch")

    def variable_scope(self) -> dict[str, Expr]:
        """Design and project variables in one table, for expression checks."""
        return {**self.project_variables, **self.variables}


def json_schema() -> dict:
    """JSON Schema for the LLM's constrained decoding.

    Exported from the same models as the validator so the generation contract
    and the validation contract cannot drift (ticket 07).
    """
    return DesignSpec.model_json_schema()


def json_schema_text() -> str:
    return json.dumps(json_schema(), indent=2, sort_keys=True) + "\n"
