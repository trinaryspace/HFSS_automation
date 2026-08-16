# Wave A batch 1 — results, 2026-08-16

Six cells, headless, `--variant max`, two turns each (Clarification, then a
uniform non-steering operator confirmation). Clean-roomed from base branches;
X0a, X0b and S3 had their whole case directory removed, so they authored blind.

> **Correction, recorded deliberately.** An earlier version of this file reported
> 3 of 6 cells producing a spec, and built a headline on X0a and X0b reaching
> "opposite outcomes" from identical prompts. That was wrong: it was tabulated
> while four turn-2 runs were still in flight, and read their partial state as
> their final state. All six produced specs. The methodological lesson is the
> campaign's own: **do not read a cell until its run has exited.** The `idle=Ns`
> session check exists for this and was not used before reporting.

## The table

| cell | structure | billed | parts | validate | precheck | geom ops | escape hatch |
|---|---|---|---|---|---|---|---|
| **X0a** | patch 2.4 GHz FR4 (blind) | 106,932 | 183 | 0 errors, 0 warn | consistent -0.00% | 9 | **0** |
| **X0b** | patch 2.4 GHz FR4 (blind) — *replicate* | 201,765 | 205 | 0 errors, 1 warn | consistent | 9 | **0** |
| **S1** | inset patch 5.8 GHz RO4350B | 69,446 | 109 | 0 errors, 1 warn | consistent -0.00% | 9 | **0** |
| **S3** | horn 10 GHz WR-90 (blind) | 169,984 | 301 | 0 errors, 0 warn | consistent **-0.09%** | 8 | **0** |
| **S4** | half-wave dipole 2.45 GHz | 99,239 | 122 | 0 errors, 0 warn | **no-estimator** | — | — |
| **S7** | 2x2 patch array 5.8 GHz | 161,882 | 163 | 0 errors, 1 warn | (blind) | **27** | **0** |
| | **total** | **809,248** | **1,083** | 6/6 | | | **0** |

Acceptance threshold, for a *complete* run: ≤80,000 billed, ≤60 parts.

## 1. U1 is answered, emphatically: yes

**Six of six** authored a `design.yaml` that validates with zero errors, and
every one that compiled did so with **`escape_hatch=0`**. That question had never
been tested once before today.

Two results carry more weight than the rest:

- **S3 built the horn blind.** Its case directory was removed entirely, and it
  still produced a spec whose closed-form gain lands at 14.9858 dBi against a
  15 dBi target — **-0.09%, not -0.00%**. A small non-zero residual is what a
  real synthesis looks like; see §3 for why the perfect zeros are the suspicious
  ones.
- **S1 is a structure not in the case set** (5.8 GHz on RO4350B), so its
  dimensions had to be produced rather than found.

## 2. The 2x2 array did not need an escape hatch

The standing hypothesis — that the compiler's missing array/duplicate op is the
largest schema-v1 gap — **does not survive contact with S7**. It enumerated the
four elements and the corporate feed as **27 geometry ops**, three times a single
patch's nine, and compiled with `escape_hatch=0`.

So the gap is real as *verbosity* and not as *capability*, at least at 2x2. That
is a materially different v2 requirement: a `duplicate`/array op would be an
ergonomics and token-cost win, not an unblocking one. Whether it holds at 4x4 or
for an SIW via fence is untested — S8 is the cell that would say.

## 3. The physics pre-check cannot validate a spec the agent wrote

X0a and S1 both report `delta: -0.00%`. That is too perfect, and the transcripts
say why:

- **S1** ran `from hfss_spec import physics as P` and computed W and L with the
  **same module `precheck.py` validates against**.
- **X0a** invoked `precheck.py` three times, adjusting between runs.

A `consistent` verdict there means *"the spec was fitted to the gate"*, not
*"the design is right"*. Contrast **S3's -0.09%**: a residual consistent with an
independent synthesis being checked by a separate relation.

The gate keeps its original value — catching a paper whose stated target
disagrees with its own dimensions, the Astuti failure, where target and
dimensions arrive independently. It has close to **zero value as a check on an
authored spec**, because the author can trivially satisfy it and one of these
demonstrably iterated until it did.

**Record per cell whether the agent invoked `physics.py` or re-ran `precheck`.**
A fitted green is not a green. Consider whether the delta being *exactly* zero
should itself be reported as suspicious.

## 4. Precheck blindness confirmed, exactly as predicted

S4's dipole: `PASS: precheck recipe=half-wave-dipole verdict=no-estimator`.

The gate **passes while checking nothing**, and prints `PASS:` while doing it. A
reader skimming for the verification line sees a pass. Cheap estimators (dipole
λ/2, monopole λ/4, circular patch) would close this and the data now justifies
them — but the more urgent fix is that `no-estimator` should not render as a pass.

## 5. Cost: the noise floor forbids ranking cells

X0a and X0b received **byte-identical prompts**, the same variant, the same
clean-roomed base branch, and ran concurrently. Both succeeded. They cost
**106,932** and **201,765** — an **88% spread**, against the plan's own ≤25% stop
rule.

By the rule written before the data: **no single-cell delta in this campaign is
interpretable, and cells must not be ranked.** Reading S1's 69,446 as "the
cheapest structure" is precisely what that rule forbids — the replicate spread is
larger than any between-structure difference in the table.

Every cell overshot both thresholds on Clarification and one document, with
nothing built and nothing solved: **69k–202k billed against ≤80,000**, and
**109–301 parts against ≤60**. The parts axis was already the stuck one
(424 → 477 → 312); Wave A shows it is stuck *before the build session starts*.

## What this says about where the cost is

Fixed overhead is ~10,086 billed / 5 parts before any work. Clarification plus
one spec then ranges 69k–202k and 109–301 parts.

The phase-2 gap is **not** build overhead and **not** solve churn — `kind-rocket`
already showed both shrinking. It is the cost of reaching the first design
decision, and it varies ~2x between byte-identical runs. Tickets 15 (token
discipline) and 14 (deterministic orchestrator) are the only backlog items
pointing here, and the variance argues specifically for 14: a deterministic
orchestrator is what removes run-to-run spread.

## Status

- All six turn-2 runs exited; all six specs gated independently after exit.
- No AEDT was launched by any cell. Verified throughout.
- **Outstanding, and not delegable: the human correctness verdict.** Six specs
  pass every automated gate. Whether they describe the right antennas is the
  false-green measurement, and §3 shows the automated gates cannot answer it.
  Copies are in `cells/*.design.yaml`.
