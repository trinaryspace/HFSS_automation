"""The Design Spec: schema, validation, reduction, and compilation.

Phase 2 of `.scratch/hfss-agent-spec-driven/spec.md`. The centre of gravity
moves from generated Python to a validated document plus a hand-written
compiler:

    design.yaml --> validate (offline, no license) --> compile --> live AEDT

Import layering matters and is enforced by a test: `units`, `expressions`,
`schema`, `validate` and `snapshot_to_spec` are Tier 0 — stdlib plus Pydantic,
no pyAEDT anywhere. Only `compiler` touches the desktop, and it imports pyAEDT
lazily so that importing this package never costs a license check.
"""

from .schema import SPEC_VERSION, DesignSpec, json_schema
from .units import Quantity, UnitError, parse_quantity

__all__ = [
    "SPEC_VERSION",
    "DesignSpec",
    "Quantity",
    "UnitError",
    "json_schema",
    "parse_quantity",
]
