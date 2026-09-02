"""Structural test for the hfss-agent skill deliverable (ticket 04).

Checks that SKILL.md encodes every contract element and ADR, that the
execution reference carries the operational semantics (face-object ports,
no estimation, cleanup), that the workspace template exists in the agreed
shape, that workspace outputs are gitignored, and that the user-provided
reference-papers KB (drop-PDF-in, analyze-papers skill) wiring is present.
No AEDT or license required.

Usage: python verify_skill.py
"""

import json
import re
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
    "verification line": ["Verification line", "PASS: <stage>", "assertions"],
    "state ledger": ["State ledger", "state.md", "results/state"],
    "run card": ["Run card", "summary.md"],
    "solve watchdog": ["poll_solve", "solve_progress.txt", "never foreground-poll"],
    "sync verify": ["capture_state.py", "model_snapshot.json", "12_verify_sync.py",
                    "port-pinned", "second desktop"],
    "static gate": ["py_compile", "import", "before any AEDT launch"],
    "idempotent stages": ["delete-then-create", "idempotent"],
    "kb rules": ["spine-api.md", ".rst.md", "rg -l"],
    # Post-pilot solve ceremony (ADR 0006 amendment). SKILL.md carried none
    # of this while execution.md did, so the skill told the agent to solve
    # but never to bank — the drift that made these markers necessary.
    "bank before teardown": ["confirm_solve", "solved.txt", "banked",
                             "close_projects=False", "refuses"],
    "stage-aware watchdog": ["stage-aware", "Normal Completion",
                             "never pass a predicted output count"],
    "resolve-once": ["escalate", "never re-submit"],
    "readout one shot": ["one shot", "never iterate readout shapes"],
    # The retry has to be a fresh PROCESS. patch-array-5800 read "one retry on
    # a fresh attach" literally, `attach()` reconnects by the pinned port, and
    # the run recorded a hypothesis it had never tested as a pairing verdict.
    # The route tokens are how a later session tells the three outcomes apart.
    "readout retries a fresh process": ["fresh process", "recycle_desktop",
                                        "ReadoutSession", "readouts.txt",
                                        "live-channel", "fresh-process",
                                        "both-failed", "untested"],
    # Phase 2: the Build session has two routes and the skill has to say so,
    # or the compiler exists and no run ever uses it.
    "build routes": ["Route A", "Route B", "design.yaml", "escape hatch",
                     "reference/design-spec.md"],
    "physics pre-check": ["precheck.py", "INCONSISTENT", "never blocks"],
    # The skill runs under two harnesses. It has to say so, point at the one
    # table of differences, and never tell an agent a skill is "installed
    # globally" when its host cannot see it.
    "two harnesses": ["opencode", "Claude Code", "Harness notes",
                      "install_skill.py", "10 minutes"],
    "analyze-papers is per host": ["~/.agents/skills/", "~/.claude/skills/",
                                   "ask the user to run the installer"],
    # Run logging 02/09: the outcome is recorded by script, the report is
    # written at the end of every run after the card, and the retro reads it.
    "run report": ["run_report.py", "run-report.md", "run-report.json",
                   "record_outcome.py", "docs/agents/run-retro.md"],
}

DESIGN_SPEC_REFERENCE = REFERENCE.parent / "design-spec.md"

DESIGN_SPEC_MARKERS = {
    "offline gates first": ["validate_spec.py", "precheck.py", "no desktop, no license"],
    "compile route": ["compile_spec.py", "--dry-run", "--launch", "never solves"],
    "what does not change": ["ADR 0007", "ADR 0006", "Review gate",
                             "Verification-line contract"],
    "selectors are symbolic": ["face_of", "never ids", "pick: largest_area"],
    "units mandatory": ["carries a unit", "dimensionless"],
    "escape hatch is measured": ["escape_hatch", "tracked metric"],
    "sync as a snapshot diff": ["spec_acceptance.py", "as_built.json", "loud ledger entry"],
}

# Tooling the Design Spec route cannot run without.
SPEC_TOOLING = ("validate_spec.py", "precheck.py", "compile_spec.py",
                "spec_from_snapshot.py", "spec_acceptance.py", "validate_cases.py")

REFERENCE_PAPERS_README = REPO / "knowledge" / "reference-papers" / "README.md"

REFERENCE_PAPERS_MARKERS = {
    "drop pdfs here": ["Drop user-provided PDFs", "academic papers, book chapters"],
    "analyze-papers flow": ["analyze-papers", "agent notes", "Clarification"],
    "no automatic playbook writes": ["NOT playbook entries", "Learning-loop", "user-approved"],
}

REFERENCE_MARKERS = {
    "preamble semantics": ["remove_lock", "Release", "os._exit", "environment-compat"],
    "port guidance": ["face object", "solid's face", "Never pass int ids"],
    "solve semantics": ["blocking=False", "Never estimate"],
    "self-correction detail": ["3 consecutive failed Runs", "GetMessages", "substitution"],
    "read-back sync steps": ["capture_state.py", "model_snapshot.json", "12_verify_sync.py",
                             "port-pinned", "does not close until sync"],
    "watchdog flow": ["poll_solve.py", "solve_progress.txt", "detached", "stall"],
    "static gate": ["py_compile", "import", "before any AEDT launch"],
    "bash discipline": ["timeout", "90 s"],
    "idempotency detail": ["delete-then-create", "in place"],
    "kb rules detail": ["spine-api.md", ".rst.md", "rg -l"],
    "reference papers before clarification": ["reference-papers", "analyze-papers", "before drafting the block"],
    # The one table of per-host differences: subagent invocation, links,
    # session naming, the run card, and the Claude Code bash-timeout ceiling.
    "harness notes": ["Harness notes", "opencode.json", ".claude/agents/",
                      "subagent_type", "CLAUDE.md", "600 000 ms",
                      "session.json", "verify_agents.py"],
    # Run logging 03: every PASS:/FAIL: line is also an event, machine-written.
    "event log": ["events.jsonl", "also an event", "hfss_spec/events.py"],
    # Run logging 02/09: gate verdicts and the outcome are recorded by script
    # at the moment they happen; the report is the Summary step's last act;
    # the harness table carries the step trace row for both stores.
    "gate and outcome recorded": ["record_gate.py", "review_gate.txt",
                                  "record_outcome.py", "outcome.txt"],
    "run report step": ["run_report.py", "run-report.md", "run-report.json",
                        "run-retro.md"],
    "step trace row": ["run_trace.py", "steps.jsonl", "subagents/"],
}

# Run logging 09: the workspace template names the end-of-run order and the
# report, so a fresh workspace cannot close out without producing it.
TEMPLATE_MARKERS = {
    "README.md": {"end-of-run checklist": ["record_outcome.py", "run_card.py",
                                           "run_report.py", "run-report.md"]},
    "summary.md": {"report pointer": ["run-report.md", "run_report.py"]},
    "state.md": {"report pointer": ["run_report.py"]},
}

# The retro doc and the `runcard` subagent's contract (both hosts, verbatim
# per scripts/verify_agents.py; the Claude Code copy is checked here).
RUN_RETRO = REPO / "docs" / "agents" / "run-retro.md"
AGENTS_MD = REPO / "AGENTS.md"
RUNCARD_AGENT = REPO / ".claude" / "agents" / "runcard.md"

ADRS = {
    "0001": "copy",
    "0002": "approval",
    "0003": ("Math model", "visual"),
    "0004": "environment-compat",
    "0005": "read-back sync",
    "0006": ("watchdog", "solve_progress.txt"),
    "0007": ("state.md", "ledger"),
    "0008": ("delete-then-create", "idempotent"),
}

TEMPLATE_FILES = ["README.md", "summary.md", "state.md", "src"]
# The two sync verifiers are both required, because the two Build routes each
# have exactly one: `12_verify_sync.py` replays numbered staged scripts, and
# `verify_spec_replay.py` replays the design-spec route's `design*.yaml`. A
# design-spec run has no numbered scripts, so without the second file the
# primary route ships with no way to satisfy ADR 0005 and every workspace
# reinvents it — the same "nowhere for the fix to live" pathology recorded in
# read_results.py's docstring.
TEMPLATE_SRC_FILES = ["ws_common.py", "poll_solve.py", "capture_state.py",
                      "12_verify_sync.py", "verify_spec_replay.py",
                      "00_static_gate.py", "stage_skeleton.py",
                      "confirm_solve.py", "profile_evidence.py", "real_fixtures.py",
                      # The one submission path (run logging 02) and the
                      # workspace's hook into the event log (run logging 03).
                      "08_solve.py", "run_events.py"]


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

    if not check("design-spec reference exists", DESIGN_SPEC_REFERENCE.is_file()):
        failures += 1
    else:
        spec_text = DESIGN_SPEC_REFERENCE.read_text(encoding="utf-8")
        for label, markers in DESIGN_SPEC_MARKERS.items():
            missing = [m for m in markers if m.lower() not in spec_text.lower()]
            if not check(f"design-spec: {label}", not missing, f"missing: {missing}"):
                failures += 1

    for name in SPEC_TOOLING:
        if not check(f"spec tooling has {name}", (REPO / "scripts" / name).is_file()):
            failures += 1

    if not check("design spec package importable offline",
                 (REPO / "hfss_spec" / "schema.py").is_file()
                 and (REPO / "hfss_spec" / "compiler.py").is_file()):
        failures += 1
    # Run logging 03: the event log the template's run_events.py forwards to.
    if not check("event log module exists", (REPO / "hfss_spec" / "events.py").is_file()):
        failures += 1

    if not check("reference file exists", REFERENCE.is_file()):
        failures += 1
        ref_text = ""
    for f in TEMPLATE_FILES:
        target = TEMPLATE / f
        if not check(f"template has {f}", target.is_dir() if f == "src" else target.is_file()):
            failures += 1
    for f in TEMPLATE_SRC_FILES:
        if not check(f"template src has {f}", (TEMPLATE / "src" / f).is_file()):
            failures += 1
    for f, groups in TEMPLATE_MARKERS.items():
        target = TEMPLATE / f
        body = target.read_text(encoding="utf-8").lower() if target.is_file() else ""
        for label, markers in groups.items():
            missing = [m for m in markers if m.lower() not in body]
            if not check(f"template {f}: {label}", not missing, f"missing: {missing}"):
                failures += 1

    # Run logging 09: the retro is reachable from AGENTS.md, and the runcard
    # subagent narrates run-report.json rather than computing a number.
    if not check("run retro doc exists", RUN_RETRO.is_file()):
        failures += 1
    else:
        retro = RUN_RETRO.read_text(encoding="utf-8")
        missing = [m for m in ("sections 1–2", "`high` finding", "tool defect",
                               "campaign log") if m not in retro]
        if not check("run retro names its three steps", not missing, f"missing: {missing}"):
            failures += 1
    agents_md = AGENTS_MD.read_text(encoding="utf-8") if AGENTS_MD.is_file() else ""
    if not check("AGENTS.md links the run retro", "docs/agents/run-retro.md" in agents_md):
        failures += 1
    runcard = RUNCARD_AGENT.read_text(encoding="utf-8") if RUNCARD_AGENT.is_file() else ""
    missing = [m for m in ("run-report.json", "never compute") if m not in runcard]
    if not check("runcard subagent narrates run-report.json", not missing,
                 f"missing: {missing}"):
        failures += 1

    gi = GITIGNORE.read_text(encoding="utf-8") if GITIGNORE.is_file() else ""
    for pat in ["workspaces", "aedt", "results", "__pycache__"]:
        if not check(f"gitignore covers {pat}", pat in gi):
            failures += 1

    # Ticket 01: profile evidence has exactly one parser. A second regex for
    # the terminal Status is how the banking guard silently went inert.
    src = TEMPLATE / "src"
    if not check("template src has profile_evidence.py",
                 (src / "profile_evidence.py").is_file()):
        failures += 1
    # A second *compiled* Status pattern is the defect; prose and test
    # fixtures legitimately contain the word.
    status_re = re.compile(r"re\.compile\((?:[^()]|\([^()]*\))*Status")
    own_parser = [p.name for p in sorted(src.glob("*.py"))
                  if p.name != "profile_evidence.py"
                  and not p.name.startswith("test_")
                  and status_re.search(p.read_text(encoding="utf-8", errors="replace"))]
    if not check("single profile parser (ticket 01)", not own_parser,
                 f"modules carrying their own Status regex: {own_parser}"):
        failures += 1

    # Ticket 03: the real-artifact corpus, without which the parser tests
    # silently become no-ops.
    corpus = src / "fixtures" / "real"
    if not check("real-artifact fixture corpus present", (corpus / "index.json").is_file()):
        failures += 1
    if not check("template src has real_fixtures.py", (src / "real_fixtures.py").is_file()):
        failures += 1

    # Ticket 04: the tiered harness and the cost-per-completion metric.
    for name in ["tier0.py", "tier1.py", "capture_fixtures.py", "run_card.py"]:
        if not check(f"scripts has {name}", (REPO / "scripts" / name).is_file()):
            failures += 1
    card_text = (REPO / "scripts" / "run_card.py").read_text(encoding="utf-8")
    if not check("run card reports cost per completed simulation",
                 "billed_per_completed_sim" in card_text):
        failures += 1

    # Run logging 06: the report and its two tracked outputs next to summary.md.
    report_script = REPO / "scripts" / "run_report.py"
    if not check("scripts has run_report.py", report_script.is_file()):
        failures += 1
    else:
        report_text = report_script.read_text(encoding="utf-8")
        for name in ("run-report.md", "run-report.json"):
            if not check(f"run_report writes {name}", f'"{name}"' in report_text):
                failures += 1
        if not check("run_report emits report.written", '"report.written"' in report_text):
            failures += 1

    # Ticket 05: the canonical case set that ends N=1 acceptance.
    cases = REPO / "knowledge" / "cases"
    if not check("canonical case index exists", (cases / "index.json").is_file()):
        failures += 1
    else:
        listed = json.loads((cases / "index.json").read_text(encoding="utf-8"))["cases"]
        missing = [c for c in listed if not (cases / c / "case.json").is_file()]
        if not check("every listed case has a case.json", not missing,
                     f"missing: {missing}"):
            failures += 1
        if not check("case set has at least five cases", len(listed) >= 5,
                     f"found {len(listed)}"):
            failures += 1

    print("ALL PASS" if failures == 0 else f"{failures} FAILURE(S)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
