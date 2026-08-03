"""Structural test for the hfss-agent skill deliverable (ticket 04).

Checks that SKILL.md encodes every contract element and ADR, that the
execution reference carries the operational semantics (face-object ports,
no estimation, cleanup), that the workspace template exists in the agreed
shape, that workspace outputs are gitignored, and that the user-provided
reference-papers KB (drop-PDF-in, analyze-papers skill) wiring is present.
No AEDT or license required.

Usage: python verify_skill.py
"""

import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO / "skill" / "hfss-agent"
SKILL = SKILL_DIR / "SKILL.md"
REFERENCE = SKILL_DIR / "reference" / "execution.md"
TEMPLATE = SKILL_DIR / "templates" / "workspace"
GITIGNORE = REPO / ".gitignore"

CONTRACT_MARKERS = {
    "spine stages": ["Clarification", "solution type", "Design", "Geometry", "Materials",
                     "excitations", "Mesh", "Setup + sweep", "solve", "post-process", "reports"],
    "clarification contract": ["Recipe", "Assumption", "Result QA signals"],
    "staged scripts": ["staged script", "attach", "launch", "session state"],
    "parameterization": ["design variable"],
    "review gate": ["Review gate", "Math model", "never to the scripts", "before any solve"],
    "read-back sync": ["read-back sync", "amends the owning stage", "summary"],
    "background solve": ["blocking=False", "poll", "Never estimate"],
    "self-correction": ["3 consecutive failed", "escalate", "identical error twice"],
    "result qa": ["convergence", "ports excited", "energy pass", "in-band", "plausibility"],
    "learning loop": ["Learning loop", "amendment", "approval"],
    "high-level api rule": ["environment-compat", "high-level", "route around"],
    "re-entry copy": ["copy", "never"],
    "glossary vocabulary": ["Spine", "Stage", "Run", "Workspace", "Recipe", "Assumption", "Model"],
    "reference papers kb": ["knowledge/reference-papers", "analyze-papers", "before Clarification",
                            "playbook amendments"],
}

REFERENCE_PAPERS_README = REPO / "knowledge" / "reference-papers" / "README.md"

REFERENCE_PAPERS_MARKERS = {
    "drop pdfs here": ["Drop user-provided PDFs", "academic papers, book chapters"],
    "analyze-papers flow": ["analyze-papers", "agent notes", "Clarification"],
    "no automatic playbook writes": ["NOT playbook entries", "Learning-loop", "user-approved"],
}

REFERENCE_MARKERS = {
    "preamble semantics": ["remove_lock", "Release", "os._exit", "environment-compat"],
    "port guidance": ["face object", "solid's face", "Never pass int ids"],
    "solve semantics": ["blocking=False", "Never estimate solve time"],
    "self-correction detail": ["3 consecutive failed Runs", "GetMessages", "substitution"],
    "read-back sync steps": ["Introspect", "Amend that script", "does not close until sync"],
    "reference papers before clarification": ["reference-papers", "analyze-papers", "before drafting the block"],
}

ADRS = {
    "0001": "copy",
    "0002": "approval",
    "0003": ("Math model", "visual"),
    "0004": "environment-compat",
    "0005": "read-back sync",
}

TEMPLATE_FILES = ["README.md", "summary.md", "src"]


def check(label, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {label}{'  (' + detail + ')' if detail and not ok else ''}")
    return ok


def main() -> int:
    failures = 0
    text = SKILL.read_text(encoding="utf-8")
    ref_text = REFERENCE.read_text(encoding="utf-8")
    for label, markers in CONTRACT_MARKERS.items():
        missing = [m for m in markers if m.lower() not in text.lower()]
        if not check(label, not missing, f"missing: {missing}"):
            failures += 1
    for label, markers in REFERENCE_MARKERS.items():
        missing = [m for m in markers if m.lower() not in ref_text.lower()]
        if not check(f"reference: {label}", not missing, f"missing: {missing}"):
            failures += 1

    for adr, needles in ADRS.items():
        needles = needles if isinstance(needles, tuple) else (needles,)
        if not check(f"adr {adr} honored", all(n.lower() in text.lower() for n in needles),
                     f"want: {needles}"):
            failures += 1

    rp_text = ""
    if not check("reference-papers README exists", REFERENCE_PAPERS_README.is_file()):
        failures += 1
    else:
        rp_text = REFERENCE_PAPERS_README.read_text(encoding="utf-8")
    for label, markers in REFERENCE_PAPERS_MARKERS.items():
        missing = [m for m in markers if m.lower() not in rp_text.lower()]
        if not check(f"reference-papers: {label}", not missing, f"missing: {missing}"):
            failures += 1

    if not check("reference file exists", REFERENCE.is_file()):
        failures += 1
        ref_text = ""
    for f in TEMPLATE_FILES:
        target = TEMPLATE / f
        if not check(f"template has {f}", target.is_dir() if f == "src" else target.is_file()):
            failures += 1

    gi = GITIGNORE.read_text(encoding="utf-8") if GITIGNORE.is_file() else ""
    for pat in ["workspaces", "aedt", "results", "__pycache__"]:
        if not check(f"gitignore covers {pat}", pat in gi):
            failures += 1

    print("ALL PASS" if failures == 0 else f"{failures} FAILURE(S)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
