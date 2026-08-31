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

## `narrate(qa_signals, spec)` is substantively blocked on the readout (2026-08-31)

The third seam takes `qa_signals` as an input. On this machine, today, there is
no reliable way to produce that input in code.

The 2026-08-18 hardware run (`workspaces/patch-array-5800`) solved three times,
banked all three, and then could not read a single number out:

- `results/state/outcome.txt`: `create_report` raised
  `GrpcApiError: Failed to execute gRPC AEDT command: GetVariables`
- `results/state/readouts.txt`: `get_solution_data` raised
  `GrpcApiError: Failed to execute gRPC AEDT command: GetPropValue`

Every QA signal that run reports came from a human reading the AEDT UI and
typing the number into the conversation - resonance, dip depth, the verdict.
Two of the agreed signals (broadside gain, element balance) were never read at
all and are still outstanding 13 days later.

**An orchestrator that cannot read QA signals has nothing to narrate.** This is
not a polish item on the seam; it is the seam's only argument. `narrate` under
a broken readout degrades to transcribing what a human already read and judged,
which is the conversation the ticket exists to replace. The same applies, more
weakly, to `diagnose(failure_evidence, spec)` whenever the failure evidence is
a result rather than a build error.

This does **not** block the session-boundary work, which is where the ticket's
measured value is and which shipped without touching a readout. It blocks
`narrate` specifically, and it changes the sequencing: the readout has to be
trustworthy before the third seam is worth building, not after.

What settles it: `.scratch/hfss-agent-parallel-tests/TASK-readout-channel-vs-systematic.md`,
a two-arm experiment on whether the failure is channel degradation over a
long-lived session or genuinely systematic on this pyAEDT/AEDT pairing. The run
concluded "systematic" from two failures that are both the transport error
class, on a channel the same run had already seen degrade and recover once; the
conclusion is queued but held back in
`knowledge/playbook/pending-amendments.md` (item 2c) rather than approved. If
the experiment says "channel", `narrate` is unblocked by a fresh-process readout
policy and the seam can be scoped normally. If it says "systematic", `narrate`
needs a different input surface than pyAEDT, and that is a design question this
ticket has not asked yet.

- [x] **Session boundaries enforced: Clarification cannot reach a licence or a
      solver; Build cannot solve; a breach exits non-zero** — `hfss_spec/session.py`,
      17 tier-0 tests, wired into `compile_spec` (`--launch` and `compile_model`).
      Verified end to end: a declared clarify session refuses
      `compile_spec --launch` with exit 1 *before* any AEDT contact, and a build
      session passes through. **Partial by construction** — it covers every
      expensive action that goes through this repo's tooling (licence, live
      model, solver) and does **not** cover an arbitrary `python -c`, which is
      how S11 actually wrote its solver. Closing that needs per-phase tool
      gating in the harness; see the remaining item below.
- [x] **A per-session call budget with an escalation verdict** — default 60, matching
      SKILL.md. Honest limit: it binds whoever calls `note_call`, so today it
      serves a driver rather than a conversation. S11's 250 parts would have
      escalated four times over.
- [ ] **Per-phase tool gating in the harness** — the residual from the two items
      above: deny the tools a phase has no business using, so the boundary holds
      for arbitrary bash as well as for repo entry points. This is the piece that
      would actually have stopped S11.
- [ ] An undeclared session is currently unguarded (deliberate, so the guard
      could land without breaking existing workspaces). Decide when to flip that
      default to "declare or refuse".
- [ ] **A readout that produces `qa_signals` in code** - the precondition for
      `narrate`, and today unmet: the 2026-08-18 hardware run banked three solves
      and read zero numbers scripted (see the section above). Settled by
      `TASK-readout-channel-vs-systematic.md`, not by work in this ticket.
- [ ] Exactly three LLM call sites; a test asserts no others exist
- [ ] All three use structured output against the exported JSON Schema
- [ ] Ledger remains the sole resume point; a killed run resumes without redoing clarification
- [ ] Diagnosis is capped and escalates with the script, the finding, and the attempts attached
- [ ] Run card breaks tokens down by seam
- [ ] Both human gates preserved, in the same place, with the same authority
