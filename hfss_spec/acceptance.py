"""Compiler acceptance: does a spec rebuild the model the old path produced?

Ticket 11. The proof is already on disk and costs no solve: the pilot
workspace holds a fully built, solved, sync-verified model plus its
`model_snapshot.json`. A `design.yaml` that compiles to a model whose captured
snapshot matches that one proves the compiler reproduces work the old path took
a 25-hour pilot to produce.

Two pieces of hard-won knowledge are reused rather than rediscovered:

- **`canon()`** from `12_verify_sync.py`, which normalises AEDT's random
  suffixes (`Sweep_XXXXXX`, `Rad__XXXXXX`). The pilot found that bug the
  expensive way, and its fix numbers same-class keys so a *count* drift cannot
  hide inside the normalisation.
- **`split_ports()`**, so a terminal is never counted as a port on either side
  of the diff.

Every residual difference is classified — compiler bug, schema gap, or
capture gap — because "the diff is not empty" is not a finding, and the schema
gaps are the honest v2 backlog.
"""

from __future__ import annotations

import importlib.util
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
_TEMPLATE_SRC = REPO / "skill" / "hfss-agent" / "templates" / "workspace" / "src"

# Sections a compiled model can be held to. Geometry bboxes are in, because
# reproducing them is exactly the claim; `sweeps` is out, because a snapshot's
# sweep list mixes real sweeps with parametric variation strings.
COMPARED_SECTIONS = ("objects", "materials", "boundaries", "variables")

COMPILER_BUG = "compiler bug"
SCHEMA_GAP = "schema gap"
CAPTURE_GAP = "capture gap"


def _load_verify_sync():
    """`canon` from the template, not a second copy of the suffix rule."""
    path = _TEMPLATE_SRC / "12_verify_sync.py"
    spec = importlib.util.spec_from_file_location("_verify_sync", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_verify_sync = _load_verify_sync()
canon = _verify_sync.canon


@dataclass(frozen=True)
class Difference:
    path: str
    expected: object
    actual: object
    classification: str
    note: str = ""

    def __str__(self) -> str:
        head = f"  {self.path:<28} {self.classification}"
        body = f"    expected {self.expected!r}\n    actual   {self.actual!r}"
        return f"{head}\n{body}" + (f"\n    {self.note}" if self.note else "")


@dataclass
class Acceptance:
    differences: list[Difference] = field(default_factory=list)
    compared: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.differences

    def by_class(self, classification: str) -> list[Difference]:
        return [d for d in self.differences if d.classification == classification]

    def summary(self) -> str:
        verdict = "PASS" if self.ok else "FAIL"
        return (f"{verdict}: spec_acceptance sections={len(self.compared)} "
                f"differences={len(self.differences)} "
                f"compiler_bugs={len(self.by_class(COMPILER_BUG))} "
                f"schema_gaps={len(self.by_class(SCHEMA_GAP))} "
                f"capture_gaps={len(self.by_class(CAPTURE_GAP))}")

    def text(self) -> str:
        lines = [self.summary()]
        if self.differences:
            lines.append("")
            lines.extend(str(d) for d in self.differences)
        return "\n".join(lines) + "\n"


_RND_TAIL = "__<RND>"


def _match_key(section: str, key: str) -> str:
    """The form two snapshots of the same model must agree on.

    Two normalisations, both learned from the first live acceptance run and
    both about AEDT's own behaviour rather than about the compiler:

    - **A boundary AEDT auto-named carries a random suffix; one the compiler
      named does not.** `canon()` reduces the pilot's `Rad__M4WFEW` to
      `Rad__<RND>`, and the compiler's deterministic `Rad` is the same
      boundary. Dropping the canonical tail makes them comparable. The
      determinism is an improvement, not a difference worth reporting.
    - **Material names are case-insensitive in AEDT and come back
      lower-cased.** The pilot's spec said `FR4_43` and its snapshot reads
      `fr4_43`.
    """
    if section == "boundaries" and key.endswith(_RND_TAIL):
        return key[: -len(_RND_TAIL)]
    return key


def _match_value(section: str, value):
    if section == "materials" and isinstance(value, str):
        return value.lower()
    return value


def compare(reference: dict, built: dict,
            sections: tuple[str, ...] = COMPARED_SECTIONS) -> Acceptance:
    """Diff a stored snapshot against a freshly captured one.

    `reference` is the model the old path produced; `built` is what the
    compiler made. Both are canonicalised first.
    """
    acceptance = Acceptance(compared=list(sections))
    left, right = canon(reference), canon(built)
    for section in sections:
        expected, actual = left.get(section), right.get(section)
        if expected == actual:
            continue
        if section == "objects":
            _diff_objects(expected or [], actual or [], acceptance)
        elif isinstance(expected, dict) or isinstance(actual, dict):
            _diff_mapping(section, expected or {}, actual or {}, acceptance)
        else:
            acceptance.differences.append(Difference(
                section, expected, actual, COMPILER_BUG))
    return acceptance


def _diff_objects(expected: list, actual: list, acceptance: Acceptance) -> None:
    missing = [n for n in expected if n not in actual]
    extra = [n for n in actual if n not in expected]
    for name in missing:
        acceptance.differences.append(Difference(
            f"objects.{name}", "present", "absent", COMPILER_BUG,
            note="the spec did not produce an object the reference model has",
        ))
    for name in extra:
        acceptance.differences.append(Difference(
            f"objects.{name}", "absent", "present", SCHEMA_GAP,
            note="the compiler left an intermediate the old path consumed "
                 "(a boolean's tool, most likely)",
        ))


def _diff_mapping(section: str, expected: dict, actual: dict,
                  acceptance: Acceptance) -> None:
    left = {_match_key(section, k): v for k, v in expected.items()}
    right = {_match_key(section, k): v for k, v in actual.items()}
    for key in sorted(set(left) | set(right)):
        a, b = left.get(key), right.get(key)
        if _match_value(section, a) == _match_value(section, b):
            continue
        acceptance.differences.append(Difference(
            f"{section}.{key}", a, b, _classify(section, key, a, b),
        ))


def _classify(section: str, key: str, expected, actual) -> str:
    """Compiler bug, schema gap, or capture gap — never just "different"."""
    if expected is None:
        return SCHEMA_GAP
    if actual is None:
        return COMPILER_BUG
    if section == "variables":
        # Both sides have the variable and the expressions differ: the spec
        # said something the model does not agree with, which is the compiler's
        # fault unless the spec never carried it.
        return COMPILER_BUG
    if section == "materials" and not str(expected).strip():
        return CAPTURE_GAP
    return COMPILER_BUG


def bbox_deltas(reference: dict, built: dict, tolerance: float = 1e-6):
    """Per-object bbox differences beyond `tolerance`, in model units.

    Kept separate from `compare` because a bbox mismatch is a *magnitude*, and
    a spec that is 0.1 mm out is a different conversation from one that built
    the wrong object.
    """
    left = (reference.get("bboxes") or {})
    right = (built.get("bboxes") or {})
    out = {}
    for name in sorted(set(left) | set(right)):
        a, b = left.get(name), right.get(name)
        if a is None or b is None or len(a) != 6 or len(b) != 6:
            out[name] = None
            continue
        deltas = [round(y - x, 9) for x, y in zip(a, b)]
        if any(abs(d) > tolerance for d in deltas):
            out[name] = deltas
    return out
