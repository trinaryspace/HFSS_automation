"""Units and dimensional algebra for the Design Spec.

Mandatory units are the schema's first defence (ticket 07): a bare number is
legal only where the quantity is genuinely dimensionless, so `52.64mm` cannot
be silently read as metres and a frequency cannot be added to a length. The
pilot's Astuti episode was a *value* error the physics pre-check catches; this
module catches the cheaper, dumber class underneath it.

Dimensions are exponent vectors over four bases — length, time, resistance,
angle. Frequency is time^-1 rather than a base of its own so that `c0 / f0`
comes out as a length without a special case.

Stdlib only, Python 3.10 compatible: this module is imported by the Tier 0
validator, which must run with no AEDT, no license and no pyAEDT.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

# --- dimensions -----------------------------------------------------------

BASES = ("length", "time", "resistance", "angle")


@dataclass(frozen=True)
class Dimension:
    """An exponent vector over BASES. Empty means dimensionless."""

    length: int = 0
    time: int = 0
    resistance: int = 0
    angle: int = 0

    def __mul__(self, other: "Dimension") -> "Dimension":
        return Dimension(*(getattr(self, b) + getattr(other, b) for b in BASES))

    def __truediv__(self, other: "Dimension") -> "Dimension":
        return Dimension(*(getattr(self, b) - getattr(other, b) for b in BASES))

    def __pow__(self, n: int) -> "Dimension":
        return Dimension(*(getattr(self, b) * n for b in BASES))

    @property
    def dimensionless(self) -> bool:
        return all(getattr(self, b) == 0 for b in BASES)

    def __str__(self) -> str:
        if self.dimensionless:
            return "dimensionless"
        parts = []
        for b in BASES:
            e = getattr(self, b)
            if e:
                parts.append(b if e == 1 else f"{b}^{e}")
        return "·".join(parts)


DIMENSIONLESS = Dimension()
LENGTH = Dimension(length=1)
TIME = Dimension(time=1)
FREQUENCY = Dimension(time=-1)
RESISTANCE = Dimension(resistance=1)
ANGLE = Dimension(angle=1)

# --- units ----------------------------------------------------------------

# unit -> (SI-ish scale, dimension). Length scales are metres, frequency Hz.
UNITS: dict[str, tuple[float, Dimension]] = {
    # length -- AEDT's spellings, including the ones its modeler reports back
    "m": (1.0, LENGTH),
    "cm": (1e-2, LENGTH),
    "mm": (1e-3, LENGTH),
    "um": (1e-6, LENGTH),
    "nm": (1e-9, LENGTH),
    "in": (0.0254, LENGTH),
    "mil": (2.54e-5, LENGTH),
    "ft": (0.3048, LENGTH),
    # frequency
    "Hz": (1.0, FREQUENCY),
    "kHz": (1e3, FREQUENCY),
    "MHz": (1e6, FREQUENCY),
    "GHz": (1e9, FREQUENCY),
    "THz": (1e12, FREQUENCY),
    # time
    "s": (1.0, TIME),
    "ms": (1e-3, TIME),
    "us": (1e-6, TIME),
    "ns": (1e-9, TIME),
    "ps": (1e-12, TIME),
    # impedance
    "ohm": (1.0, RESISTANCE),
    "Ohm": (1.0, RESISTANCE),
    # angle
    "deg": (math.pi / 180.0, ANGLE),
    "rad": (1.0, ANGLE),
}

# Case-insensitive lookup, but the canonical spelling is what we emit back.
_UNIT_BY_LOWER: dict[str, str] = {}
for _u in UNITS:
    _UNIT_BY_LOWER.setdefault(_u.lower(), _u)

LENGTH_UNITS = tuple(u for u, (_s, d) in UNITS.items() if d == LENGTH)

_QUANTITY_RE = re.compile(
    r"^\s*(?P<value>[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)\s*(?P<unit>[A-Za-z]*)\s*$"
)


class UnitError(ValueError):
    """A malformed or unknown unit."""


@dataclass(frozen=True)
class Quantity:
    """A number with a unit. `unit == ""` means dimensionless."""

    value: float
    unit: str = ""

    @property
    def dimension(self) -> Dimension:
        if not self.unit:
            return DIMENSIONLESS
        return UNITS[self.unit][1]

    @property
    def si(self) -> float:
        """The value in metres / Hz / ohm / radians."""
        if not self.unit:
            return self.value
        return self.value * UNITS[self.unit][0]

    def to(self, unit: str) -> "Quantity":
        unit = canonical_unit(unit)
        if unit and self.dimension != UNITS[unit][1]:
            raise UnitError(
                f"cannot convert {self} to {unit}: "
                f"{self.dimension} is not {UNITS[unit][1]}"
            )
        if not unit:
            if not self.dimension.dimensionless:
                raise UnitError(f"cannot strip the unit from {self}")
            return Quantity(self.value, "")
        return Quantity(self.si / UNITS[unit][0], unit)

    def __str__(self) -> str:
        text = repr(round(self.value, 10))
        if text.endswith(".0"):
            text = text[:-2]
        return f"{text}{self.unit}"


def canonical_unit(unit: str) -> str:
    """Normalise a unit's spelling, or raise UnitError."""
    if not unit:
        return ""
    if unit in UNITS:
        return unit
    lowered = _UNIT_BY_LOWER.get(unit.lower())
    if lowered is None:
        raise UnitError(f"unknown unit {unit!r}")
    return lowered


def parse_quantity(raw) -> Quantity:
    """`'52.64mm'` / `2.4` / `'2.4GHz'` -> Quantity. Raises UnitError.

    Bare numbers are accepted and come back dimensionless; it is the schema's
    job, not this function's, to decide whether a bare number is legal in a
    given field.
    """
    if isinstance(raw, Quantity):
        return raw
    if isinstance(raw, bool):
        raise UnitError("a boolean is not a quantity")
    if isinstance(raw, (int, float)):
        return Quantity(float(raw), "")
    if not isinstance(raw, str):
        raise UnitError(f"cannot read a quantity from {type(raw).__name__}")
    match = _QUANTITY_RE.match(raw)
    if match is None:
        raise UnitError(f"{raw!r} is not a number with an optional unit")
    unit = canonical_unit(match.group("unit"))
    return Quantity(float(match.group("value")), unit)


def is_quantity_literal(raw) -> bool:
    """True when `raw` parses as a literal quantity (so it is not an expression)."""
    try:
        parse_quantity(raw)
    except UnitError:
        return False
    return True


# Constants available inside spec expressions, as (SI value, dimension).
#
# A pair rather than a Quantity because c0 is metres-per-second and no single
# unit string spells that: with frequency modelled as time^-1, `c0 / f0` has to
# come out as a length, which only works if c0 carries length·time^-1.
CONSTANTS: dict[str, tuple[float, Dimension]] = {
    "c0": (299792458.0, LENGTH / TIME),
    "pi": (math.pi, DIMENSIONLESS),
    "eps0": (8.8541878128e-12, DIMENSIONLESS),
    "mu0": (1.25663706212e-6, DIMENSIONLESS),
}
