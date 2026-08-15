"""Closed-form physics pre-check — the part that helps with EM. Ticket 09.

The highest-value-per-token component in the plan, because the thing it
answers in microseconds is the thing that otherwise costs a 7-minute solve and
hours of conversation. The motivating failure is exact: the Astuti bow-tie's
equations did not reproduce its own Table I / Figure 1, the discrepancy
survived clarification, geometry, materials, excitations, mesh, setup,
validation and **four solves**, and the user caught it at the results read
roughly twenty hours in.

Three rules, all of them load-bearing:

- **It never blocks and never overrides.** It prints both numbers and the
  signed disagreement; the user arbitrates and the choice is recorded in
  `provenance.canonical_reading`.
- **Tolerances are data, not code.** They live in
  `knowledge/playbook/precheck-tolerances.json`, because what counts as a
  disagreement worth raising is a domain judgement about how good a given
  closed form is.
- **Every estimator cites its relation** and is tested against a worked
  example whose answer is known independently — the `knowledge/cases/*` files
  carry those numbers recomputed rather than copied.

Stdlib only. No AEDT, no license, no pyAEDT.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .expressions import Value, resolve_all
from .schema import DesignSpec
from .units import FREQUENCY, LENGTH, RESISTANCE

C0 = 299792458.0

REPO = Path(__file__).resolve().parent.parent
TOLERANCE_FILE = REPO / "knowledge" / "playbook" / "precheck-tolerances.json"


# --- estimators -------------------------------------------------------------


def effective_permittivity(er: float, h: float, w: float) -> float:
    """Balanis 14-1: the quasi-static effective permittivity of a microstrip.

        ereff = (er+1)/2 + (er-1)/2 * (1 + 12h/W)^(-1/2)

    Worked example (knowledge/cases/patch-2400): er 4.4, h 1.6 mm,
    W 38.0100 mm -> 4.0857.
    """
    if w <= 0 or h <= 0:
        raise ValueError("width and height must be positive")
    return (er + 1) / 2.0 + (er - 1) / 2.0 * (1.0 + 12.0 * h / w) ** -0.5


def fringing_extension(ereff: float, h: float, w: float) -> float:
    """Balanis 14-2: the length a patch appears to gain to fringing fields.

        dL/h = 0.412 * ((ereff+0.3)(W/h+0.264)) / ((ereff-0.258)(W/h+0.8))

    Worked example (patch-2400): ereff 4.0857, h 1.6 mm, W 38.0100 mm
    -> 0.7388 mm.
    """
    ratio = w / h
    return 0.412 * h * ((ereff + 0.3) * (ratio + 0.264)) / \
                       ((ereff - 0.258) * (ratio + 0.8))


def patch_resonance(patch_l: float, patch_w: float, h: float, er: float) -> float:
    """Resonant frequency of a rectangular microstrip patch, in Hz.

    Balanis 14-7 solved for frequency rather than length:

        f = c / (2 * (L + 2*dL) * sqrt(ereff))

    Worked example (patch-2400): L 29.4216 mm, W 38.0100 mm, h 1.6 mm,
    er 4.4 -> 2.4 GHz, the frequency the case was synthesised for.
    """
    ereff = effective_permittivity(er, h, patch_w)
    dl = fringing_extension(ereff, h, patch_w)
    return C0 / (2.0 * (patch_l + 2.0 * dl) * math.sqrt(ereff))


def bowtie_resonance(side: float, base: float, h: float, er: float) -> float:
    """Dominant-mode resonance of a bow-tie patch, in Hz.

    A bow-tie is treated as a pair of triangular patches, and the dominant
    TM10 mode of an equilateral triangular patch (Balanis, triangular
    microstrip antenna) gives

        f = 2c / (3 * a * sqrt(ereff))

    with `a` the side (leg) length, and ereff from the microstrip relation
    using the base as the effective width.

    Honesty note, and the reason this estimator is trusted at all: against
    the delivered pilot model — leg 26.3269 mm, base 20.2168 mm, h 1.6 mm,
    er 4.3 — it predicts 3.88 GHz against a **measured 3.85 GHz**, about
    +0.8%. It also predicts +10.9% against that model's 3.5 GHz target,
    which is the Astuti disagreement, flagged in microseconds instead of
    twenty hours.
    """
    ereff = effective_permittivity(er, h, base)
    return 2.0 * C0 / (3.0 * side * math.sqrt(ereff))


def microstrip_impedance(w: float, h: float, er: float) -> tuple[float, float]:
    """`(Z0 in ohm, ereff)` for a microstrip line — Hammerstad.

        W/h >= 1:  Z0 = 120*pi / (sqrt(ereff) * (W/h + 1.393
                                   + 0.667*ln(W/h + 1.444)))
        W/h <  1:  Z0 = 60/sqrt(ereff) * ln(8h/W + W/(4h))

    Worked example (knowledge/cases/microstrip-50r): W 3.0829 mm, h 1.6 mm,
    er 4.4 -> ereff 3.3323, Z0 50.0 ohm.
    """
    ereff = effective_permittivity(er, h, w)
    ratio = w / h
    if ratio >= 1.0:
        z0 = (120.0 * math.pi) / (math.sqrt(ereff) *
                                  (ratio + 1.393 + 0.667 * math.log(ratio + 1.444)))
    else:
        z0 = (60.0 / math.sqrt(ereff)) * math.log(8.0 / ratio + ratio / 4.0)
    return z0, ereff


def guide_wavelength(frequency: float, ereff: float) -> float:
    """Guide wavelength in metres: lambda_g = c / (f * sqrt(ereff)).

    Worked example (microstrip-50r): 2.4 GHz at ereff 3.3323 -> 68.4282 mm.
    """
    return C0 / (frequency * math.sqrt(ereff))


def rectangular_waveguide_cutoff(a: float) -> float:
    """TE10 cutoff of a rectangular waveguide, in Hz: f_c = c / (2a).

    Worked example (knowledge/cases/horn-10ghz): WR-90's a = 0.9 in
    = 22.86 mm -> 6.5571 GHz.
    """
    return C0 / (2.0 * a)


# --- the check ---------------------------------------------------------------


@dataclass
class Prediction:
    quantity: str
    target: Optional[float]
    predicted: float
    unit: str
    tolerance_pct: float
    detail: list[tuple[str, str]]
    note: str = ""
    # Set only where a percentage disagreement is the wrong test — the horn's
    # check is "does TE10 propagate and stay single-mode", which is a band
    # membership question, not a distance from a number.
    ok: Optional[bool] = None

    @property
    def delta_pct(self) -> Optional[float]:
        if self.target in (None, 0):
            return None
        return 100.0 * (self.predicted - self.target) / self.target

    @property
    def consistent(self) -> bool:
        if self.ok is not None:
            return self.ok
        delta = self.delta_pct
        return delta is None or abs(delta) <= self.tolerance_pct

    def _fmt(self, value: Optional[float]) -> str:
        if value is None:
            return "n/a"
        scale = {"GHz": 1e9, "ohm": 1.0, "mm": 1e-3}.get(self.unit, 1.0)
        return f"{value / scale:.4f} {self.unit}"

    def text(self) -> str:
        lines = []
        for label, value in self.detail:
            lines.append(f"      {label:<22} {value}")
        lines.append("")
        lines.append(f"      {'target':<22} {self._fmt(self.target)}")
        delta = self.delta_pct
        suffix = "" if delta is None else \
            f"      delta: {delta:+.2f}%   tolerance: {self.tolerance_pct:g}%"
        lines.append(f"      {'closed-form':<22} {self._fmt(self.predicted)}{suffix}")
        if self.note:
            lines.append("")
            lines.append(f"      note: {self.note}")
        return "\n".join(lines)


@dataclass
class Precheck:
    recipe: str
    prediction: Optional[Prediction]
    reason: str = ""

    @property
    def verdict(self) -> str:
        if self.prediction is None:
            return "no-estimator"
        return "consistent" if self.prediction.consistent else "INCONSISTENT"

    def text(self) -> str:
        head = "PASS" if self.verdict != "INCONSISTENT" else "FAIL"
        body = ""
        if self.prediction is not None:
            body = self.prediction.text() + "\n\n"
        elif self.reason:
            body = f"      {self.reason}\n\n"
        tail = ("" if self.verdict != "INCONSISTENT"
                else " — arbitrate before building")
        return (f"{body}{head}: precheck recipe={self.recipe} "
                f"verdict={self.verdict}{tail}\n")


def load_tolerances() -> dict:
    try:
        return json.loads(TOLERANCE_FILE.read_text(encoding="utf-8"))["recipes"]
    except (OSError, ValueError, KeyError):
        return {}


def check(spec: DesignSpec) -> Precheck:
    """Predict the spec's target quantity and compare. Never raises, never blocks."""
    recipes = load_tolerances()
    entry = recipes.get(spec.recipe, {})
    estimator = entry.get("estimator")
    if estimator is None:
        return Precheck(spec.recipe, None,
                        reason=f"no estimator registered for recipe "
                               f"{spec.recipe!r} in {TOLERANCE_FILE.name}")
    try:
        scope = resolve_all(spec.variable_scope())
    except Exception as exc:                      # noqa: BLE001 - never blocks
        return Precheck(spec.recipe, None, reason=f"variables unresolved: {exc}")

    # The spec's own tolerance wins when it states one; the playbook is the
    # fallback and the record of how far the closed form can be trusted.
    tolerance = (spec.target.tolerance_pct if spec.target is not None
                 else entry.get("tolerance_pct", 5.0))
    target = _target_si(spec, scope)
    try:
        prediction = _ESTIMATORS[estimator](spec, scope, target, tolerance,
                                            entry.get("note", ""))
    except Exception as exc:                      # noqa: BLE001 - never blocks
        return Precheck(spec.recipe, None, reason=f"estimator failed: {exc}")
    return Precheck(spec.recipe, prediction)


def _target_si(spec: DesignSpec, scope: dict[str, Value]) -> Optional[float]:
    if spec.target is None:
        return None
    from .expressions import evaluate
    try:
        return evaluate(spec.target.value, scope).si
    except Exception:                             # noqa: BLE001 - never blocks
        return None


def _var(scope: dict[str, Value], *names: str) -> float:
    """The first variable that exists, by SI magnitude."""
    for name in names:
        if name in scope:
            return scope[name].si
    raise KeyError(f"none of {names} is a declared variable")


def _mm(value: float) -> str:
    return f"{value * 1000:.4f} mm"


# Relative permittivity of the AEDT library materials a v1 recipe might use as
# a substrate. Only needed when the spec references a library material rather
# than defining one inline or declaring an `er` variable.
LIBRARY_PERMITTIVITY = {
    "fr4_epoxy": 4.4,
    "rogers rt/duroid 5880 (tm)": 2.2,
    "rogers rt/duroid 6002 (tm)": 2.94,
    "teflon_based": 2.1,
    "polyimide": 3.5,
    "alumina_96pct": 9.4,
    "quartz": 3.78,
    "air": 1.0,
    "vacuum": 1.0,
}

_NON_SUBSTRATE = {"air", "vacuum", "pec", "copper", "gold", "silver",
                  "aluminum", "aluminium"}


def _permittivity(spec: DesignSpec, scope: dict[str, Value]) -> float:
    """The substrate's relative permittivity, from wherever the spec put it.

    Three legal places, and a real spec uses different ones: an `er` variable
    (patch-2400), an inline material definition (the bow-tie's user-defined
    `FR4_43`, which is not a library entry), or a library reference whose
    value the spec never states.
    """
    from .schema import MaterialDef, MaterialRef

    for name in ("er", "epsilon_r", "eps_r", "Er", "ER"):
        if name in scope:
            return scope[name].si

    for key, material in spec.materials.items():
        if key.lower() in _NON_SUBSTRATE:
            continue
        if isinstance(material, MaterialDef):
            return resolve_all({"_er": material.permittivity})["_er"].si
        if isinstance(material, MaterialRef):
            value = LIBRARY_PERMITTIVITY.get(material.library.lower())
            if value is not None and value > 1.0:
                return value

    raise KeyError(
        "no permittivity: declare an `er` variable, define the substrate "
        "material inline, or reference a known library material"
    )


def _patch(spec, scope, target, tolerance, note) -> Prediction:
    length = _var(scope, "patch_L", "PatchL", "L")
    width = _var(scope, "patch_W", "PatchW", "W")
    h = _var(scope, "h", "SubH", "sub_h")
    er = _permittivity(spec, scope)
    ereff = effective_permittivity(er, h, width)
    dl = fringing_extension(ereff, h, width)
    predicted = patch_resonance(length, width, h, er)
    return Prediction(
        "resonant_frequency", target, predicted, "GHz", tolerance,
        [("patch length (14-7)", _mm(length)),
         ("patch width (14-6)", _mm(width)),
         ("ereff (14-1)", f"{ereff:.4f}"),
         ("fringing dL (14-2)", _mm(dl))],
        note,
    )


def _bowtie(spec, scope, target, tolerance, note) -> Prediction:
    side = _var(scope, "PatchLeg", "patch_leg", "leg")
    base = _var(scope, "PatchBase", "patch_base", "base")
    h = _var(scope, "SubH", "h", "sub_h")
    er = _permittivity(spec, scope)
    ereff = effective_permittivity(er, h, base)
    predicted = bowtie_resonance(side, base, h, er)
    return Prediction(
        "resonant_frequency", target, predicted, "GHz", tolerance,
        [("leg / side", _mm(side)),
         ("base", _mm(base)),
         ("ereff (14-1 on base)", f"{ereff:.4f}")],
        note,
    )


def _microstrip(spec, scope, target, tolerance, note) -> Prediction:
    width = _var(scope, "trace_W", "feed_W", "W", "w")
    h = _var(scope, "h", "SubH", "sub_h")
    er = _permittivity(spec, scope)
    z0, ereff = microstrip_impedance(width, h, er)
    return Prediction(
        "impedance", target, z0, "ohm", tolerance,
        [("trace width", _mm(width)),
         ("W/h", f"{width / h:.5f}"),
         ("ereff (14-1)", f"{ereff:.4f}")],
        note,
    )


def _horn(spec, scope, target, tolerance, note) -> Prediction:
    a = _var(scope, "wg_a", "WG_a", "guide_a", "a")
    cutoff = rectangular_waveguide_cutoff(a)
    operating = _var(scope, "f0", "design_freq", "freq")
    ratio = operating / cutoff
    # A band-membership test, not a percentage: TE10 must propagate (f > f_c)
    # and the guide should stay single-mode (f < 2*f_c, where TE20 starts).
    # The stated target is a gain in dBi, which no closed form here predicts,
    # so `target` is deliberately None rather than a number to compare against.
    return Prediction(
        "te10_band", None, cutoff, "GHz", tolerance,
        [("guide broad wall a", _mm(a)),
         ("TE10 cutoff", f"{cutoff / 1e9:.4f} GHz"),
         ("operating frequency", f"{operating / 1e9:.4f} GHz"),
         ("f / f_c", f"{ratio:.4f}  (want 1 < f/f_c < 2)")],
        note or "v1 checks TE10 propagation, not aperture gain",
        ok=1.0 < ratio < 2.0,
    )


_ESTIMATORS = {
    "patch_resonance": _patch,
    "bowtie_resonance": _bowtie,
    "microstrip_impedance": _microstrip,
    "horn_cutoff": _horn,
}
