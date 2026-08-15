# 14 — Deterministic orchestrator: three LLM seams, everything else code

**What to build:** A Python state machine that runs the Spine and calls the
model at exactly three places. Today the run *is* a conversation, and the
conversation's length is the cost — 424 parts at baseline, 1,392 in the pilot.
Under the compiler most of what those parts were doing (writing scripts, reading
logs, looking up signatures, wrangling processes) is code, so the remaining
model work is small and well-shaped:

- `clarify(request, playbook, papers) → SpecDraft + questions` — the one genuinely
  open-ended seam, and the one that most rewards a capable model;
- `diagnose(failure_evidence, spec) → SpecPatch | escalate` — fires only on
  failure, receives the validator's precise finding rather than a log dump;
- `narrate(qa_signals, spec) → summary prose` — the QA write-up and `summary.md`.

Each uses structured output against the ticket-07 schema, so a malformed
response is a retry at the decoding layer rather than a failed AEDT run. The
phase sessions and the State ledger (ADR 0007) survive as the orchestrator's
persistence: the ledger stays the resume point, and the three sessions map onto
orchestrator states rather than onto separate conversations. Human gates stay
exactly where they are — Clarification agreement and the visual Review gate —
because the pilot proved both catch things nothing else does.

Failure paths matter more than the happy path: the orchestrator must escalate
with evidence rather than retry silently, cap diagnosis attempts per stage as
`SKILL.md` already specifies, and record which seam fired how many times so the
run card can show where the tokens went.

**Blocked by:** 08, 10, 13.

**Status:** needs-triage

- [ ] Exactly three LLM call sites; a test asserts no others exist
- [ ] All three use structured output against the exported JSON Schema
- [ ] Ledger remains the sole resume point; a killed run resumes without redoing clarification
- [ ] Diagnosis is capped and escalates with the script, the finding, and the attempts attached
- [ ] Run card breaks tokens down by seam
- [ ] Both human gates preserved, in the same place, with the same authority
