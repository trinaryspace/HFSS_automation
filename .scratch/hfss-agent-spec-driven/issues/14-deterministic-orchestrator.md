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

**Status:** needs-triage — **now the highest-priority item in the backlog**
(2026-08-17 campaign; see `.scratch/hfss-agent-parallel-tests/RECOMMENDATIONS.md`)

## Why this moved to the top — three independent measurements

The original case for this ticket was cost: the run *is* a conversation and the
conversation's length is the bill. The campaign found two stronger reasons, both
about **boundaries** rather than length.

1. **A session with no boundary will spend without limit.** Cell S11 was asked
   for a coupled-line filter. On finding the repo has no even/odd-mode
   synthesis, it began writing a 2D finite-difference field solver and spent
   **51 minutes, 151,526 tokens and 250 parts** debugging it inside a
   *Clarification* block, delivering nothing. This is `shiny-canyon`'s 25-hour
   failure reproduced in under an hour, on demand. Hard rule 8 and the session
   budget in SKILL.md are the advisory patch; the structural fix is a state
   machine where "Clarification may not write code" is not a sentence an agent
   can reason its way past.

2. **Identical inputs cost 2x apart.** Cells X0a and X0b received byte-identical
   prompts, the same variant and the same clean-roomed base, and both succeeded
   — at **106,932 and 201,765 billed**. An 88% spread on the same task is
   run-to-run variance, and a deterministic orchestrator is the only item in the
   backlog that removes it. Nothing else here touches variance at all.

3. **The parts axis is stuck before the build starts.** Every Wave A cell spent
   **109–301 parts** on Clarification plus one document, against a whole-run
   target of ≤60, with nothing built and nothing solved. The remaining cost is
   in the conversation reaching its first decision, which is precisely the seam
   this ticket replaces with code.

**Scope it narrowly.** The valuable core is not "three LLM seams" as an
aesthetic; it is *what a session of each type may and may not do*, enforced by
the runner. Ship that boundary first, with the three seams following.

- [ ] **Session boundaries enforced by the runner: Clarification cannot write
      code or run implementation loops; Build cannot solve; a breach escalates**
- [ ] **A per-session budget the runner owns, so a loop is capped by the harness
      rather than by the agent noticing**
- [ ] Exactly three LLM call sites; a test asserts no others exist
- [ ] All three use structured output against the exported JSON Schema
- [ ] Ledger remains the sole resume point; a killed run resumes without redoing clarification
- [ ] Diagnosis is capped and escalates with the script, the finding, and the attempts attached
- [ ] Run card breaks tokens down by seam
- [ ] Both human gates preserved, in the same place, with the same authority
