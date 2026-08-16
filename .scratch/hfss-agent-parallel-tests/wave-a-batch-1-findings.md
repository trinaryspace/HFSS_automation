# Wave A batch 1 — results, 2026-08-16

Six cells, headless, `--variant max`, two turns each (Clarification, then a
uniform non-steering operator confirmation). Clean-roomed from base branches;
X0a, X0b and S3 had their whole case directory removed, so they authored blind.

## The table

| cell | structure | billed | parts | spec? | validate | precheck | escape hatch |
|---|---|---|---|---|---|---|---|
| **X0a** | patch 2.4 GHz FR4 (blind) | 106,932 | 183 | yes | errors=0 warnings=0 | consistent -0.00% | **0** |
| **X0b** | patch 2.4 GHz FR4 (blind) — *replicate of X0a* | 167,957 | 179 | **no** | — | — | — |
| **S1** | inset patch 5.8 GHz RO4350B | 69,446 | 109 | yes | errors=0 warnings=1 | consistent -0.00% | **0** |
| **S3** | horn 10 GHz WR-90 (blind) | 162,788 | 262 | **no** | — | — | — |
| **S4** | half-wave dipole 2.45 GHz | 96,054 | 114 | yes | errors=0 warnings=0 | **no-estimator** | — |
| **S7** | 2x2 patch array 5.8 GHz | 161,882 | 163 | **no** | — | — | — |
| | **total** | **765,059** | **1,010** | 3/6 | | | |

Acceptance threshold, for a *complete* run: ≤80,000 billed, ≤60 parts.

## 1. U1 is answered: yes, an LLM can write a valid design.yaml

Three did. All three passed `validate_spec` with zero errors, and the two that
compiled did so with **`escape_hatch=0`** — 9 stages, 9 geometry ops, 1 port,
1 boundary each. `S1` is the strongest result: 5.8 GHz on RO4350B is **not in
the case set**, so its dimensions had to be produced rather than found.

That question had never been tested once. It is now, and the answer is positive.

## 2. The noise floor destroys per-cell comparison

X0a and X0b received **byte-identical prompts**, the same variant, the same
clean-roomed base branch, and ran concurrently.

- X0a: **106,932** billed, produced a complete valid spec.
- X0b: **167,957** billed, produced **nothing**.

Spread on tokens: **44.4%** against the plan's own ≤25% stop rule. So by the
rule written before the data: **no single-cell delta in this campaign is
interpretable, and cells must not be ranked.** That rule earned its place — the
temptation to read S1's 69,446 as "the cheapest structure" is exactly what it
forbids.

The stronger statement is qualitative: identical inputs produced opposite
outcomes, and the failing run cost **57% more** than the succeeding one. Cost
here is not tracking difficulty; it is tracking flailing.

## 3. Half the cells never reached a spec

X0b, S3 and S7 spent 160k+ each and ended without one, despite an explicit
"write the design.yaml" instruction in turn 2. They were still reading, checking
compiler face-resolution, and re-deriving when the turn ended. This is not a
crash — it is the reading protocol consuming the whole budget.

**Parts tell the same story more sharply.** Every cell — including the three
successes — spent between 109 and 262 parts against a ≤60 target, on
Clarification and one spec. The parts axis was already the stuck one (424 → 477
→ 312); Wave A shows it is stuck *before the build session even starts*.

## 4. The physics pre-check cannot validate an authored spec

Both X0a and S1 report `delta: -0.00%`. That is too perfect, and the transcripts
say why:

- **S1** ran `from hfss_spec import physics as P` and computed W and L with the
  **same module `precheck.py` validates against**.
- **X0a** invoked `precheck.py` three times, adjusting between runs.

So a `consistent` verdict here means *"the spec was fitted to the gate"*, not
*"the design is right"*. The pre-check remains valuable for its original job —
catching a paper whose stated target disagrees with its own dimensions, the
Astuti failure — because there the target and the dimensions arrive independently.
It has close to **zero value as a check on a spec the agent authored**, because
the agent can trivially satisfy it, and one of these two demonstrably iterated
until it did.

**Consequence for the campaign:** for authored specs the only real correctness
signals are the human verdict and the solve. Record, per cell, whether the agent
invoked `physics.py` or re-ran `precheck` — a fitted green is not a green.

## 5. Precheck blindness confirmed, exactly as predicted

S4's dipole: `PASS: precheck recipe=half-wave-dipole verdict=no-estimator`.

The gate **passes while checking nothing**, and it says `PASS:`. A reader
skimming for the verification line sees a pass. Whether the agent surfaced the
blindness to the user is the open question for the cell record; the tooling
certainly does not make it loud.

Cheap estimators (dipole λ/2, monopole λ/4, circular patch) would close this, and
the data now justifies them.

## What this says about where the cost is

Combining with the dry cell: fixed overhead is ~10,086 billed / 5 parts, and
Clarification-plus-spec ranges 69k–168k and 109–262 parts. Nothing here has
built or solved anything.

The phase-2 gap is **not** build overhead and **not** solve churn — `kind-rocket`
already showed both shrinking. It is the cost of reaching the first design
decision, and it varies by 2.4x between identical runs. Tickets 15 (token
discipline) and 14 (orchestrator) are the only backlog items pointing here.

## Status

- Turn 2 completed for all six; X0b and S3 ended mid-work without a spec.
- No AEDT was launched by any cell. Verified throughout.
- Not yet done: human correctness verdicts (yours), and re-running the three
  cells that produced nothing.
