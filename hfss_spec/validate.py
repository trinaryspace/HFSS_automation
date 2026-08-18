"""Offline validation: refuse a spec before AEDT is ever launched. Ticket 08.

No desktop, no license, no pyAEDT import — so this runs in Tier 0 in
milliseconds. That is the whole economic argument: the errors caught here are
the ones that currently cost a desktop launch, a failed stage, a read of the
traceback and a self-correction round. Schema and reference errors should cost
zero AEDT time and near-zero tokens.

Four check classes beyond Pydantic conformance, in the order they fire:

1. **Reference resolution** — every symbolic selector names an object the spec
   actually declares, every variable reference resolves, every material is a
   library name or declared inline.
2. **Units and dimensions** — expressions are dimensionally sound, a frequency
   is not added to a length, extents are positive, and the sweep brackets the
   target.
3. **Topological sanity** — ports sit on objects that exist, a boolean's tools
   exist *at the point it runs*, and the radiation boundary encloses something.
4. **Recipe completeness** — the spec declares what its recipe needs. This is
   the "critical setup features the user left out" clause of the Clarification
   contract, made mechanical.

Every finding carries the offending path (`geometry[2].size[0]`) so a
diagnosis seam gets a location rather than a stack trace.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from . import feed_check, model_checks
from .expressions import ExpressionError, Value, evaluate, resolve_all
from .schema import DesignSpec, MaterialDef, MaterialRef
from .units import (
    DIMENSIONLESS,
    FREQUENCY,
    LENGTH,
    RESISTANCE,
    Dimension,
    UnitError,
    parse_quantity,
)

ERROR = "error"
WARNING = "warning"

# Materials AEDT ships that a spec may reference without defining.
LIBRARY_MATERIALS = {
    "air", "vacuum", "pec", "copper", "gold", "silver", "aluminum", "aluminium",
    "brass", "tin", "lead", "nickel", "iron", "steel_stainless", "tungsten",
    "fr4_epoxy", "rogers rt/duroid 5880 (tm)", "rogers rt/duroid 6002 (tm)",
    "teflon_based", "polyimide", "silicon", "alumina_96pct", "diamond",
    "duroid (tm)", "quartz", "sapphire", "water", "mylar",
}

# What each target quantity must be dimensionally.
TARGET_DIMENSIONS = {
    "resonant_frequency": FREQUENCY,
    "center_frequency": FREQUENCY,
    "bandwidth": FREQUENCY,
    "impedance": RESISTANCE,
    "characteristic_impedance": RESISTANCE,
    # Gain is stated in dBi, which is a bare number here rather than a
    # dimensioned quantity — the unit is in the target's name, not its value.
    "gain": DIMENSIONLESS,
}


@dataclass(frozen=True)
class Finding:
    path: str
    severity: str
    message: str
    hint: str = ""

    def __str__(self) -> str:
        text = f"  {self.path:<26} {self.message}"
        return f"{text}\n  {'':<26} {self.hint}" if self.hint else text


@dataclass
class Report:
    findings: list[Finding]

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == ERROR]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == WARNING]

    @property
    def ok(self) -> bool:
        return not self.errors

    def summary(self) -> str:
        verdict = "PASS" if self.ok else "FAIL"
        return (f"{verdict}: validate_spec errors={len(self.errors)} "
                f"warnings={len(self.warnings)}")

    def text(self) -> str:
        lines = [self.summary()]
        for label, group in (("errors", self.errors), ("warnings", self.warnings)):
            if group:
                lines.append("")
                lines.append(f"  {label}:")
                lines.extend(str(f) for f in group)
        return "\n".join(lines) + "\n"


class SpecNotValidated(RuntimeError):
    """Raised by the compiler's gate when handed an unvalidated spec."""


def validate(spec: DesignSpec) -> Report:
    """Every check class, in order. Never raises on spec content."""
    findings: list[Finding] = []
    scope = _check_variables(spec, findings)
    _check_materials(spec, findings)
    _check_geometry(spec, findings, scope)
    _check_excitations(spec, findings, scope)
    _check_boundaries(spec, findings)
    _check_setup(spec, findings, scope)
    _check_recipe_completeness(spec, findings)
    _check_model_relations(spec, findings, scope)
    return Report(findings)


def require_valid(spec: DesignSpec) -> Report:
    """The compiler's hard gate — an invalid spec never reaches the desktop."""
    report = validate(spec)
    if not report.ok:
        raise SpecNotValidated(report.text())
    return report


# --- 1. references and 2. dimensions ---------------------------------------


def _check_variables(spec: DesignSpec, findings: list[Finding]) -> dict[str, Value]:
    table = spec.variable_scope()
    try:
        return resolve_all(table)
    except ExpressionError as exc:
        message = str(exc)
        path = "variables"
        if message.startswith("variables."):
            name, _, rest = message[len("variables."):].partition(": ")
            path, message = f"variables.{name}", rest or message
        findings.append(Finding(path, ERROR, message))
        # Resolve what we can so later checks still say something useful.
        partial: dict[str, Value] = {}
        for name, raw in table.items():
            try:
                partial[name] = evaluate(raw, partial)
            except (ExpressionError, UnitError):
                continue
        return partial


def _dimension_of(raw, scope, path, findings, expected: Dimension | None,
                  what: str) -> Value | None:
    try:
        value = evaluate(raw, scope)
    except (ExpressionError, UnitError) as exc:
        findings.append(Finding(path, ERROR, str(exc)))
        return None
    if expected is not None and value.dimension != expected:
        findings.append(Finding(
            path, ERROR,
            f"{what} must be {expected}, got {value.dimension}",
            hint=f"value read as {raw!r}",
        ))
        return None
    return value


def _check_materials(spec: DesignSpec, findings: list[Finding]) -> None:
    for key, material in spec.materials.items():
        if isinstance(material, MaterialRef):
            if material.library.lower() not in LIBRARY_MATERIALS:
                findings.append(Finding(
                    f"materials.{key}", WARNING,
                    f"{material.library!r} is not a known AEDT library material",
                    hint="define it inline if the desktop does not carry it",
                ))
        elif isinstance(material, MaterialDef):
            pass    # its fields are dimensionless and schema-checked


def _check_geometry(spec: DesignSpec, findings: list[Finding],
                    scope: dict[str, Value]) -> None:
    """Reference, dimension and ordering checks over the geometry section."""
    available: set[str] = set()
    for index, op in enumerate(spec.geometry):
        path = f"geometry[{index}]"

        if op.op == "unknown":
            findings.append(Finding(
                f"{path}.op", ERROR,
                f"{op.name!r} is `op: unknown` — a reduced placeholder, not a "
                f"construction op",
                hint="a snapshot records an object's extent, not how it was "
                     "built; complete this op by hand before compiling",
            ))
            available.add(op.name)
            continue

        # Reference: a boolean's operands must already exist at this point.
        for operand in op.consumes:
            if operand not in available:
                findings.append(Finding(
                    f"{path}", ERROR,
                    f"{op.op} on {op.name!r} references {operand!r}, which is "
                    f"not created by an earlier op",
                    hint=_did_you_mean(operand, available),
                ))
        if op.op in ("unite", "subtract", "intersect") and op.name not in available:
            findings.append(Finding(
                f"{path}.name", ERROR,
                f"{op.op} target {op.name!r} does not exist yet",
            ))

        # Dimensions: every dimensional field must be a length (angles aside).
        _check_op_dimensions(op, path, scope, findings)

        for name in op.object_names:
            available.add(name)

    if not spec.geometry:
        findings.append(Finding("geometry", ERROR, "no geometry declared"))


def _check_op_dimensions(op, path, scope, findings) -> None:
    for field in ("origin", "size", "sweep_vector"):
        values = getattr(op, field, None) or []
        for i, raw in enumerate(values):
            value = _dimension_of(raw, scope, f"{path}.{field}[{i}]", findings,
                                  LENGTH, f"{field}[{i}]")
            if value is not None and field == "size" and value.si <= 0:
                findings.append(Finding(
                    f"{path}.{field}[{i}]", ERROR,
                    f"extent must be positive, got {value.si:g} m",
                ))
    for field in ("radius", "height", "thickness"):
        raw = getattr(op, field, None)
        if raw is not None:
            value = _dimension_of(raw, scope, f"{path}.{field}", findings,
                                  LENGTH, field)
            if value is not None and value.si <= 0:
                findings.append(Finding(
                    f"{path}.{field}", ERROR,
                    f"{field} must be positive, got {value.si:g} m",
                ))
    for i, point in enumerate(op.points or []):
        for j, raw in enumerate(point):
            _dimension_of(raw, scope, f"{path}.points[{i}][{j}]", findings,
                          LENGTH, "coordinate")


def _check_excitations(spec: DesignSpec, findings: list[Finding],
                       scope: dict[str, Value]) -> None:
    declared = set(spec.declared_objects)
    seen: set[str] = set()
    for index, port in enumerate(spec.excitations):
        path = f"excitations[{index}]"
        if port.name in seen:
            findings.append(Finding(f"{path}.name", ERROR,
                                    f"duplicate excitation name {port.name!r}"))
        seen.add(port.name)
        _check_selector(port.on, f"{path}.on", declared, findings)
        _dimension_of(port.impedance, scope, f"{path}.impedance", findings,
                      RESISTANCE, "impedance")
        line = port.integration_line
        if line is not None:
            for label, endpoint in (("from", line.from_), ("to", line.to)):
                target = getattr(endpoint, "edge_mid", None)
                if target and target[0] not in declared:
                    findings.append(Finding(
                        f"{path}.integration_line.{label}", ERROR,
                        f"edge_mid references undeclared object {target[0]!r}",
                        hint=_did_you_mean(target[0], declared),
                    ))
                for k, raw in enumerate(getattr(endpoint, "point", None) or []):
                    _dimension_of(raw, scope,
                                  f"{path}.integration_line.{label}.point[{k}]",
                                  findings, LENGTH, "coordinate")


def _check_boundaries(spec: DesignSpec, findings: list[Finding]) -> None:
    declared = set(spec.declared_objects)
    for index, boundary in enumerate(spec.boundaries):
        path = f"boundaries[{index}]"
        _check_selector(boundary.on, f"{path}.on", declared, findings)
        if boundary.type == "finite_conductivity" and boundary.conductivity is None:
            findings.append(Finding(
                f"{path}.conductivity", ERROR,
                "a finite-conductivity boundary needs a conductivity",
            ))


def _check_selector(selector, path: str, declared: set[str],
                    findings: list[Finding]) -> None:
    target = (getattr(selector, "face_of", None)
              or getattr(selector, "object", None)
              or getattr(selector, "outer_faces", None))
    if target is None:
        findings.append(Finding(path, ERROR, "selector names no object"))
        return
    if target == "UNRESOLVED":
        findings.append(Finding(
            path, ERROR, "selector is the reducer's UNRESOLVED placeholder",
            hint="a snapshot records a boundary's name and type, not its faces",
        ))
        return
    if target not in declared:
        findings.append(Finding(
            path, ERROR, f"{target!r} is not a declared object",
            hint=_did_you_mean(target, declared),
        ))


def _check_setup(spec: DesignSpec, findings: list[Finding],
                 scope: dict[str, Value]) -> None:
    frequency = _dimension_of(spec.setup.solution_frequency, scope,
                              "setup.solution_frequency", findings,
                              FREQUENCY, "solution frequency")
    target_value = None
    if spec.target is not None:
        expected = TARGET_DIMENSIONS.get(spec.target.quantity)
        target_value = _dimension_of(spec.target.value, scope, "target.value",
                                     findings, expected, spec.target.quantity)

    sweep = spec.setup.sweep
    if sweep is None:
        return
    start = _dimension_of(sweep.start, scope, "setup.sweep.start", findings,
                          FREQUENCY, "sweep start")
    stop = _dimension_of(sweep.stop, scope, "setup.sweep.stop", findings,
                         FREQUENCY, "sweep stop")
    if start is None or stop is None:
        return
    if start.si >= stop.si:
        findings.append(Finding(
            "setup.sweep", ERROR,
            f"start {start.si/1e9:g}GHz is not below stop {stop.si/1e9:g}GHz",
        ))
        return
    checked: list[float] = []
    for label, value in (("target", target_value),
                         ("solution frequency", frequency)):
        if value is None or value.dimension != FREQUENCY:
            continue
        # The solution frequency usually *is* the target; saying it twice is
        # noise, and a noisy validator gets ignored.
        if any(abs(value.si - seen) <= 1e-6 * max(value.si, seen) for seen in checked):
            continue
        checked.append(value.si)
        if not start.si <= value.si <= stop.si:
            findings.append(Finding(
                "setup.sweep", ERROR,
                f"sweep {start.si/1e9:g}-{stop.si/1e9:g}GHz does not contain the "
                f"{label} {value.si/1e9:g}GHz",
            ))
            continue
        # A resonance that lands outside the swept band is invisible, and a
        # target hugging the edge is nearly as bad -- the pilot read its
        # resonance 10% off target, which a tight bracket would have hidden.
        margin = min(value.si - start.si, stop.si - value.si)
        if margin < 0.2 * value.si:
            findings.append(Finding(
                "setup.sweep", WARNING,
                f"sweep brackets the {label} {value.si/1e9:g}GHz by only "
                f"{margin/1e9:g}GHz on the near side",
                hint="a resonance just outside the band would be invisible",
            ))


# --- 4. recipe completeness -------------------------------------------------

# Signals that need a thing to exist before they can be reported.
_SIGNAL_REQUIREMENTS = {
    "ports_excited": ("excitations", "no excitation is declared"),
    "in_band_resonance": ("setup.sweep", "no sweep is declared, so there is no "
                                         "S-curve to find a resonance in"),
}


def _check_recipe_completeness(spec: DesignSpec, findings: list[Finding]) -> None:
    if not spec.excitations:
        findings.append(Finding(
            "excitations", ERROR, "no excitation declared — nothing drives the model",
        ))
    if not spec.qa_signals:
        findings.append(Finding(
            "qa_signals", WARNING,
            "no QA signals declared, so Result QA has nothing to report",
        ))
    for signal in spec.qa_signals:
        requirement = _SIGNAL_REQUIREMENTS.get(signal)
        if requirement is None:
            continue
        field, reason = requirement
        present = spec.excitations if field == "excitations" else spec.setup.sweep
        if not present:
            findings.append(Finding(
                f"qa_signals.{signal}", ERROR,
                f"{signal} cannot be reported: {reason}",
            ))
    radiating = any(b.type == "radiation" for b in spec.boundaries)
    if not radiating and "in_band_resonance" in spec.qa_signals:
        findings.append(Finding(
            "boundaries", WARNING,
            "no radiation boundary — an antenna with no open boundary will not "
            "radiate, and its resonance will be wrong",
        ))
    if spec.escape_hatch_count:
        findings.append(Finding(
            "geometry", WARNING,
            f"{spec.escape_hatch_count} escape-hatch op(s) — the schema could not "
            f"express this geometry",
            hint="escape-hatch rate is the metric that says whether v1 is right",
        ))


def _check_model_relations(spec: DesignSpec, findings: list[Finding],
                           scope: dict[str, Value]) -> None:
    """Whole-model checks (`model_checks`), reported as warnings.

    Warnings, not errors, and the distinction is deliberate. Both rules encode a
    rule of thumb rather than a law: a deliberately tight airbox or a flared port
    can be right, and an ERROR would block a legitimate design on a heuristic —
    the one failure mode worse than missing a defect. They are loud enough to be
    read and cheap enough to be acted on.

    They exist because the 2026-08-17 review found three real defects in six
    machine-clean specs and **no existing check could have seen any of them**.
    These two would have caught five of the six specs between them.
    """
    for path, message, hint in model_checks.radiation_clearance(spec, scope):
        findings.append(Finding(path, WARNING, message, hint=hint))
    for path, message, hint in model_checks.port_geometry(spec, scope):
        findings.append(Finding(path, WARNING, message, hint=hint))
    # The feed-network walk is an ERROR, unlike the other two. It is not a rule
    # of thumb: the designer has declared what the elements present, and either
    # the arithmetic closes or the network is mismatched. S7 shipped a 2:1
    # mismatch on every element past three green gates.
    for path, severity, message, hint in feed_check.walk(spec, scope):
        findings.append(Finding(path, ERROR if severity == "error" else WARNING,
                                message, hint=hint))


def _did_you_mean(name: str, candidates: Iterable[str]) -> str:
    """The cheap Levenshtein-free suggestion: same length, one edit apart."""
    import difflib
    # 0.6 rather than the 0.7 default: a transposition in a short name
    # ('Sbu' for 'Sub') scores 0.67, and that is exactly the typo worth catching.
    close = difflib.get_close_matches(name, sorted(candidates), n=1, cutoff=0.6)
    return f"did you mean {close[0]!r}?" if close else ""
