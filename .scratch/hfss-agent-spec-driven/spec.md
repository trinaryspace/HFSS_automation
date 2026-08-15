# Spec: Spec-driven HFSS agent — robustness and token efficiency from one change of artifact

Status: needs-triage
Feature: hfss-agent-spec-driven

## Problem Statement

Two runs and one pilot have now measured the tool. The baseline (`silent-engine`)
cost 398,130 tokens / 424 parts / ~1.6 h. The post-refactor pilot
(`shiny-canyon`) cost 1,579,333 tokens / 1,392 parts / 25 h and returned
**NO-GO on all three acceptance axes** (`.scratch/hfss-agent-perf-refactor/pilot-retrospective.md`).

The perf refactor was not wrong — its instrumentation is what caught the
regression, and its doctrines (phase sessions, State ledger, Verification
line, idempotent stages, detached watchdog) are sound and are **kept in
full** by this spec. But it optimized the containment machinery around a
decision that was never revisited: **the agent's primary output artifact is
free-form Python.**

Every expensive mechanism in the current design exists to contain the blast
radius of that one choice:

- the `py_compile`/import static gate exists because generated code may not parse;
- the `PASS:` Verification line exists because a run's success is otherwise unknowable;
- ADR 0008 idempotency is a *discipline* the model must remember per script;
- read-back sync needs `capture_state.py` + `12_verify_sync.py` replaying eight
  scripts on a port-pinned second desktop (36 steps in baseline; 6 replays × ~8 min
  in the pilot) because the scripts and the live model can silently diverge;
- the 4,376-file KB exists so the model can look up call signatures it would
  not need if the surface were typed (~20 discovery steps in baseline).

Three further findings sharpen the case:

1. **The safety machinery is currently decorative.** `confirm_solve.terminal_status()`
   returns `None` on **9 of 9** real profiles on this box — its regex omits the
   escaped quotes AEDT actually writes (`\'Status\', \'Normal Completion\'`). So
   `ws_common.guard_verdict()` returns `proceed` for every solved workspace,
   teardown runs `close_projects=True`, and the results-purge incident that
   ticket 13 exists to prevent is still fully live. Separately,
   `poll_solve.scan_results()` applies its stage-family regexes only to
   `filenames`, but `.imesh` / `.cmesh` / `_ADP*` are **directories** in all four
   workspaces — so `mesh=(0,0)` and `adp=(0,0)` on every real tree. Since ticket
   14's own evidence records that the `.profile` is written *at the end of the
   solve, not per stage*, artifact growth is the only live stage signal, and the
   watchdog is therefore blind to stage until the sweep starts.
2. **Both bugs passed 72 green tests**, because the fixtures were hand-written:
   real artifact *names* written as files instead of directories, and a profile
   fixture with unescaped quotes. Ticket 14's Comments record the escaped-quote
   quirk correctly; ticket 13 landed minutes later without it. The knowledge had
   nowhere to live but one ticket's comment thread.
3. **The published state of the art does not generate free-form code.**
   Foam-Agent generates OpenFOAM dictionaries under Pydantic validation and
   reports 88.2% success on a 110-case benchmark; ChatCFD reports 82.1%
   execution success on 315 cases; Zoo built KCL as a constrained deterministic
   language expressly so LLM output is checkable. Foam-Agent's ablations also
   show model capability is the single largest lever (88.2% Claude 3.5 Sonnet vs
   59.1% GPT-4o on an identical harness) — larger than their retrieval
   improvement. This repo pinned a flash model at `variant: low` to save tokens
   and then spent 4× the baseline on flailing.

Robustness and token efficiency are **the same problem here**: tokens are burned
on flailing, and flailing is what an unconstrained artifact permits.

## Solution

Move the centre of gravity from *generated code* to a **validated Design Spec
plus a hand-written compiler**.

```
user request ──► Clarification (LLM) ──► design.yaml  ◄── the artifact the user reviews,
                                             │              git tracks, and diffs
                          ┌──────────────────┴──────────────────┐
                          ▼                                     ▼
                 offline validation                     spec compiler
            (schema · references · units ·        (hand-written, unit-tested,
             closed-form physics pre-check)        idempotent, emits PASS lines)
                    no AEDT · no license                       │
                                                               ▼
                                                       live AEDT desktop
```

Five layers, of which only the first and the diagnosis seam involve an LLM:

1. **Design Spec (`design.yaml`)** — a schema-validated document describing
   solution type, variables, geometry, materials, excitations, boundaries, mesh,
   setup/sweep, and QA signals. It is the single source of truth, replacing "ten
   staged scripts" as the thing that *is* the simulation.
2. **Offline validation** — schema, symbolic-reference resolution, unit
   consistency, and a **closed-form physics pre-check** (predicted resonance /
   line impedance vs the spec's target), all with no desktop and no license.
3. **Compiler** — deterministic Python, `spec → pyAEDT`. Idempotent by
   construction. Emits the existing `PASS:` Verification lines.
4. **Typed tool surface** — the ~36 spine calls wrapped as validated functions.
   The KB is demoted to a cold-path fallback.
5. **Orchestrator** — a deterministic state machine that runs the Spine and calls
   the LLM at exactly three seams: clarify, diagnose-failure, narrate-QA.

**What this deletes:** the sync-verify replay ceremony (spec diff replaces it),
KB signature discovery, per-run re-derivation of ten stage scripts, and most
self-correction loops (schema errors are caught before AEDT launches).

**What this keeps, unchanged:** phase sessions and the State ledger (ADR 0007),
the Verification line, the visual Review gate (ADR 0003), the detached watchdog
(ADR 0006), delete-then-create semantics (ADR 0008 — now a compiler property
rather than a per-script discipline), copy-first Re-entry (ADR 0001), and the
Learning loop (ADR 0002).

**Escape hatch:** when the spec cannot express something, the agent writes a
stage script exactly as today. That path stays supported, is flagged in the
ledger, and its frequency is a tracked metric — if it fires often, the schema is
wrong and that is a signal, not a failure.

## User Stories

1. As the user, I want a wrong dimension caught by a closed-form check **before**
   a 7-minute solve, so that the Astuti-class failure (inconsistent paper
   geometry discovered ~20 h in, at the results read) cannot recur.
2. As the user, I want to review and edit **one `design.yaml`** instead of ten
   Python scripts, so that the Review gate is a diff I can actually read.
3. As the maintainer, I want the whole build path testable **without an AEDT
   license**, so that regressions are caught in CI-speed seconds rather than by
   a pilot 20 hours in.
4. As the maintainer, I want read-back sync to be a **spec diff**, so that the
   two-desktop replay ceremony (36 baseline steps; 6 × ~8 min in the pilot) is
   deleted rather than optimized.
5. As the maintainer, I want the agent to never look up a call signature, so
   that KB discovery (~20 baseline steps) costs zero.
6. As the maintainer, I want a **regression set of canonical cases** with a
   no-solve fast tier, so that acceptance is not N=1 and does not need
   license-hours.
7. As the maintainer, I want the headline metric to be **cost per successfully
   completed simulation**, so that a cheap model that flails is correctly scored
   as expensive.
8. As the user, I want to sweep a parameter across N designs from one spec, so
   that the tool does something I would not do by hand.
9. As the maintainer, I want every fixture derived from **real captured
   artifacts**, so that the escaped-quote / directory-vs-file bug class cannot
   pass a green suite again.
10. As the user, I want the solve, banking, and teardown guarantees to actually
    hold, so that a solved result is never purged.

## Implementation Decisions

1. **Spec format: YAML, schema-validated by Pydantic.** YAML for human review and
   git diffs; Pydantic because it is the validation layer *and* the
   structured-output schema for the LLM call in one definition. JSON Schema is
   exported from it for the model's constrained decoding.
2. **Symbolic selectors, never ids.** Faces and objects are referenced
   symbolically (`face_of(PatchBowtie, +z)`, `nearest_face(Substrate, [x,y,z])`),
   resolved by the compiler against the live model at build time. This encodes
   env-compat #7/#8 (assign by face object, never id/edge) as a *type*, not a
   remembered rule.
3. **Units are mandatory and explicit** on every dimensional value (`52.64mm`,
   `3.5GHz`). Unit consistency is a validation error, not a runtime surprise.
4. **Every geometry dimension is a variable reference or a literal-with-unit;**
   the compiler emits AEDT design variables for all of them, preserving PLAN.md's
   full-parameterization rule mechanically.
5. **Idempotency is a compiler property.** The compiler always deletes the
   objects/boundaries/setups/mesh-ops/sweeps named in the spec before creating
   them. ADR 0008 survives as doctrine but stops depending on model discipline.
6. **Physics pre-check is deterministic and offline.** A per-recipe module of
   closed-form estimates (patch resonant length, bowtie/dipole resonance,
   Hammerstad microstrip Z0, substrate-λ scaling) predicts the design's target
   quantity from the spec and compares against the stated goal. Disagreement
   beyond a per-recipe tolerance is surfaced in Clarification with both numbers.
   It never blocks; the user arbitrates (this generalizes ticket 09's paper
   dimension gate from a prose instruction into a function).
7. **Read-back sync = spec diff.** `capture_state.py` keeps writing
   `model_snapshot.json`; a new `snapshot_to_spec` reduces it to spec shape and
   diffs against `design.yaml`. `12_verify_sync.py` and the port-pinned second
   desktop are retired once the diff path is proven equivalent on the pilot
   workspace.
8. **Orchestrator seams (exactly three LLM call sites).**
   `clarify(request, playbook, papers) → SpecDraft + questions`;
   `diagnose(failure_evidence, spec) → SpecPatch | escalate`;
   `narrate(qa_signals, spec) → summary prose`. Everything else is code. Each
   call uses structured output against the Pydantic schema.
9. **Model tiering reversed on the main loop.** The three seams run on a capable
   reasoning model; `kb-lookup`-style mechanical work stays cheap. Ticket 02's
   single-swap-point provider alias makes this a config change. Justified by
   Foam-Agent's 88.2%-vs-59.1% same-harness ablation and by this repo's own
   measurement that the cheap model cost 4× baseline.
10. **Prompt-cache the stable prefix.** Spec schema + spine-api + the active
    recipe are a fixed prefix across all seams in a run; they are ordered first
    and cached rather than re-sent.
11. **Fixture fidelity is enforced, not remembered.** A `fixtures/real/` tree is
    captured from actual workspaces by a script (entity type and byte content
    preserved), and parser tests run against it. Hand-written fixtures are
    permitted only alongside a real one.
12. **One parser per evidence type.** Profile status, stage ledger, and artifact
    families each get exactly one implementation, imported by every consumer.
    The current two-parser split is the proximate cause of the banking bug.

## Testing Decisions

- **What makes a good test here:** the live AEDT desktop stays the final judge,
  but it stops being the *first* judge. Three tiers:
  - **Tier 0 — offline (seconds, no license):** schema validation, reference
    resolution, unit checks, physics pre-check, compiler golden tests
    (`spec → expected pyAEDT call sequence`, mocked), all parsers against
    `fixtures/real/`.
  - **Tier 1 — build-only (minutes, license, no solve):** compile each canonical
    spec onto a live desktop through `validate_simple()`, capture the snapshot,
    diff against the spec. No solver physics, so it can run often.
  - **Tier 2 — full (hours):** one canonical case end to end including solve,
    readout, and QA.
- **Compiler acceptance is already on disk.** `workspaces/bowtie-3500-pilot/`
  holds a solved model and its `model_snapshot.json`. A spec that compiles to a
  snapshot matching it is the compiler's proof — no new solve required.
- **Regression set:** five canonical structures (inset-fed patch, bowtie,
  microstrip line, coupled-line filter, horn) as specs, run at Tier 0 always and
  Tier 1 per phase gate.
- **Acceptance thresholds** vs the `silent-engine` baseline (398,130 tokens /
  424 parts): **≤80,000 billed tokens and ≤60 parts** for a clean greenfield run,
  plus zero escape-hatch stage scripts on the canonical set. Stretch: ≤50,000.
- **Prior art:** the pilot workspace is the reference implementation for stages
  01–10 and the source of the compiler's target behaviour.

## Out of Scope

- HFSS 3D Layout, RCS/SBR+ (env-compat #12 says unusable on this box), and new
  product surfaces.
- Optimization / inverse design. Parametric sweep (ticket 16) is generation of N
  specs, not a search algorithm.
- Full KB re-crawl. The corpus is unchanged; it is demoted, not rebuilt.
- Replacing the AEDT UI as the Review surface (ADR 0003 stands).
- Automated CI infrastructure. Tier 0/1 are scripts the maintainer runs.

## Further Notes

- Phases 0 and 1 deliver value and are worth doing **whatever is decided about
  the architecture bet** — they fix live bugs and make measurement trustworthy.
  Phase 2 is the bet. Sequencing is deliberate: the cheapest, highest-expected-
  value experiment (ticket 06, main-loop model) runs *before* the expensive
  rewrite, and could partly moot it.
- Existing perf-refactor tickets 10 (context hygiene), 12 (solve-session
  discipline), 16/17 (readout) remain valid and are prerequisites or
  near-neighbours; this spec does not duplicate them.
- The escape-hatch rate is the honest measure of whether the schema is right.
  Budget for it being wrong twice before it is right.

## Comments

- 2026-08-14: **Phase 2 detail published** in `phase-2-detail.md` — a full
  worked `design.yaml`, the compiler's actual call shape, sample validator
  and physics-pre-check output, the escape-hatch form, and eight open
  design questions (geometry scope, expression variables, selector
  disambiguation, mesh ownership, unrepresentable UI tweaks, setup
  coverage, sequencing, one-spec-per-design). Q7 proposes reordering
  07 -> 12a (`snapshot_to_spec`) -> 08 -> 10 -> 11 so the schema is shaped
  by a real model instead of by guesswork. Phase 2 stays `needs-triage`
  pending those answers.
- 2026-08-14: **Phases 0 and 1 implemented** (tickets 01-05 done; 06 is
  ready but needs a live desktop). Both P0 bugs fixed and verified against
  the real artifacts, the real-artifact fixture corpus is in place with an
  enforced fidelity rule, the run card now reports cost per completed
  simulation, Tier 0 runs 7 suites in ~13 s with no license, and the
  five-case canonical set is written. Details in each ticket's Comments.

- 2026-08-14: Spec drafted from a full repo review plus a survey of published
  agentic-simulation architectures (Foam-Agent 2.0, ChatCFD, Zoo KCL,
  Text-to-CadQuery, agentic-EDA handoff survey). Two live P0 bugs found during
  the review and filed as tickets 01/02 with reproduction evidence. Status
  `needs-triage`: phases 0–1 are ready to run; phase 2+ needs the maintainer's
  go/no-go on the architecture bet.
