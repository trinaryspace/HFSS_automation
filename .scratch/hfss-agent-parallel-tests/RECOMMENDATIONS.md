# What to do next — recommendations from the campaign

Written 2026-08-17, after Wave A (6 authoring cells), the honesty cells (S6, S11)
and maintainer review. Every claim here traces to a measurement in
`wave-a-batch-1-findings.md`, `FALSE-GREEN-RATE.md` or `honesty-cells-findings.md`.

## The one-paragraph version

Phase 2's bet is sound: **an LLM can write a valid `design.yaml`** — six of six
did, with zero escape hatches, including a blind horn and a 2×2 array. The schema
is not the bottleneck. What the campaign found instead is that **half of the
specs that pass every automated gate are wrong**, that the wrongness is always a
*relational* property no current gate examines, and that the tool's worst cost
sink is not building or solving but **unbounded scope expansion when it hits
something the repo cannot do**. So the work ahead is not more schema and not
better prompting. It is: make the right thing the default, make three cheap
checks block, and put a boundary around what a session is allowed to attempt.

## What is now settled, and should stop being debated

| question | answer | evidence |
|---|---|---|
| Can an LLM author a valid spec? | **Yes** | 6/6, `escape_hatch=0`, incl. blind horn (−0.09% gain) and 2×2 array |
| Is schema v1 the bottleneck? | **No** | S7 expressed a 2×2 array in 27 ops with no escape hatch |
| Does the array/duplicate op unblock anything? | **No** — it is verbosity | same |
| Does the agent lie to pass gates? | **No** | S6 declared a new recipe rather than relabel |
| Does the agent tune to satisfy gates? | **Yes** | X0a ran `precheck` 3× to reach −0.00% |
| Is the readout broken? | **Was our reader** | fixed, tested, landed in env-compat #6 |

## Status of these recommendations, checked 2026-08-31

Checked against the code and `git log`, not against memory or commit subjects.
Two of them did **not** land in the form written here, and both differences
matter.

| § | recommendation | status | evidence |
|---|---|---|---|
| 1 | λ₀/3 as the schema **default** | **WITHDRAWN — premise wrong** | No clearance default in `hfss_spec/schema.py` or `loader.py`; `air_pad` appears there only in docstrings and tests. Commit `9ed76b4` "airboxes to lambda/3 across the board" edited **two cell specs** (`S1`, `X0b`) by hand and touched no code. An attempt to implement it on 2026-08-31 found there is nothing to default: there is no clearance *field* (clearance is emergent from a plain `op: box`'s expressions), and all 13 specs declare an explicit pad, so a default-when-absent fires on none of them. The defect is authors choosing a too-small **coefficient**, copied from a contaminated exemplar. See `clearance-defect-mechanism.md`. |
| 2 | `no-estimator` as its own verdict | **LANDED** | `Precheck.text()` in `hfss_spec/physics.py`: `head = "UNCHECKED"` with the tail "no estimator for this recipe; nothing was verified". Commit `ad7e4da`, 2026-08-17. |
| 3 | two **blocking** validator rules | **PARTIAL — warnings; severity decision DEFERRED 2026-09-01** | `_check_model_relations` in `hfss_spec/validate.py` appends `radiation_clearance` and `port_geometry` as `WARNING`, deliberately, with a docstring giving the reason. Only `feed_check.walk` emits `ERROR`. Commit `ad7e4da`. Deferred on purpose — see the note below. |
| — | (a third gate, not recommended here) | landed, blocking | The feed-network walk: `hfss_spec/feed_check.py`, commits `b98c9a7` / `e797189` / `b45680d` (2026-08-18) and `2d9a6d0` (2026-08-31). It is an ERROR because the designer declared what the elements present and the arithmetic either closes or it does not. |
| 4 | scope stop-rule as a hard rule | **LANDED** | `skill/hfss-agent/SKILL.md` hard rule 8, "Never build the missing capability", with S11 written in as the measurement. |
| 5 | per-session budget cap | **LANDED** | `hfss_spec/session.py`: `DEFAULT_CALL_BUDGET = 60`, `note_call`, `over_budget`, `budget_verdict`. Commit `ad7e4da`. Honest limit: it binds whoever calls `note_call`. |
| 6 | ticket 14, first item | **LANDED** | `hfss_spec/session.py` + wired into `scripts/compile_spec.py` (`require_phase("launch_desktop")`, `require_phase("compile_model")`); tier-0 suite `session`. Commit `8a223d3`, 2026-08-18. Partial by construction, and ticket 14 says so. |
| 7 | Wave B on hardware | **first cell run** | `S7SIM`, 2026-08-18, `workspaces/patch-array-5800` — three solves banked. See `campaign-log.md`. |
| 8 | break the pre-check's circularity | **first datapoint exists** | The §7 run produced one: predicted 5.8000 GHz, solved 5.6 GHz, +3.57%. `estimator-calibration.md`. The `abs(delta) < 0.005` suspicion NOTE also landed, in `Prediction.text()`. |
| 9 | cheap missing estimators | **partly** | `circular_patch_resonance` is registered in `precheck-tolerances.json` and implemented in `physics.py`; dipole λ/2 and monopole λ/4 are not. |

**§1 is the one to re-read.** This document argued the default *because* a
check is weaker: "A default costs the agent nothing and **prevents** the defect
rather than detecting it." A detector landed and the preventer did not, so the
five-of-six defect rate is still reachable by any new spec — it will now be
warned about, in a warning that §"What I got wrong" already predicts will be
read and ignored.

**§3 landed in the form this document itself called insufficient.** The
recommendation survives, in its own words, "only for gates that **block** or
that encode a relation the agent cannot tune". Both rules encode such a
relation, and both were shipped as warnings anyway. The reasoning in
`validate.py` is honest and may well be right — an ERROR on a heuristic blocks
legitimate designs, "the one failure mode worse than missing a defect" — but it
is the opposite call from the one made here, and nobody recorded the reversal
until now. Whether a warning binds is an empirical question this campaign
already has an answer to (S11 read a note and ignored it), and no cell has run
against the warnings yet.

**Severity decision deferred 2026-09-01, and the reason is a dependency.** The
question is currently *un-decidable on the available evidence*, because the
evidence is contaminated by the defect in §1. The clearance warning fires on
nearly every spec in the repo — not because nearly every spec is badly designed,
but because the exemplar the skill tells authors to copy under-pads at λ₀/4
(`clearance-defect-mechanism.md`). Escalating a gate whose false-positive rate
is set by a broken template would block nearly everything, and would "prove" the
warn-camp right for the wrong reason. There is no clean baseline to measure
against yet.

Sequence: fix the exemplar first, regenerate the picture, then decide. If the
warning stops firing broadly, a warning may be sufficient after all; if it still
fires on genuine designs, there is a real case for blocking.

When it is decided, stop treating the two rules as one question. They are not
the same kind of rule. `radiation_clearance` has a defensible physical floor —
below some clearance the absorbing boundary reflects and the result is simply
invalid — and could reasonably be two-tier: warn below λ₀/3, error below a hard
floor. `port_geometry`'s ~1.5× really is a rule of thumb; a flared port can be
right, and it should stay a warning. Offered as an option, not a settled call.

**A third candidate appeared 2026-09-01, and it is a stronger one than either.**
The 2×2 array's feed excites its two E-plane element pairs 180° out of phase —
confirmed from the radiation pattern of the banked solve — while passing every
offline gate with `errors=0`. No length error exists (all four paths are
56.0323 mm), no impedance error exists (`feed_check.walk` passes, correctly),
and S11 does not show it. The 180° comes from mirrored elements being fed by a
mirror-symmetric network, which inverts one element's resonant mode. Filed as
ticket 18; evidence in `antiphase-mirror-feed-2026-09-01.md`.

It matters for *this* section because a feed-sense mismatch is **discrete**, not
a rule of thumb with a fuzzy threshold: two elements' net excitation either
agrees in sign or it does not. The argument that shipped clearance and port
geometry as warnings — that an ERROR on a heuristic blocks legitimate designs —
does not apply to it. If any member of this family should block, it is that one.

## Do now — small, certain, high yield

These are cheap and each is justified by a measured defect. In order.

### 1. Make λ₀/3 the schema default for radiation-boundary clearance
Four of five patch-family specs independently chose λ₀/4 or worse; only the horn
met λ₀/3. That is a **missing default**, not five mistakes. A default costs the
agent nothing and prevents the defect rather than detecting it.

*Shape:* `air_pad` (or the boundary's clearance) defaults to `c0/(3*f0)` when
unspecified. Keep it overridable — but then the override is a visible decision.

### 2. Render `no-estimator` as its own verdict, not behind `PASS:`
One line. Today a pre-check that validated **nothing** prints
`PASS: precheck recipe=half-wave-dipole verdict=no-estimator`. A reader skimming
for the verification line sees a pass. S4 was exactly that spec, and it also had
the port defect.

### 3. Two blocking validator rules
- **Airbox clearance** — distance from every radiating body's bbox to the
  radiation boundary; fail below λ₀/3 at the target frequency. Would have caught
  **5 of 6** specs.
- **Port-geometry ratio** — a lumped port sheet's width against the conductor it
  bridges; fail beyond ~1.5×. Would have caught **S4** (4 mm port, 1 mm wire).

Both are geometric relations the agent **cannot tune its way past** — you cannot
satisfy a λ₀/3 clearance without moving the boundary. That property is what makes
them worth building; see the caveat in §"What I got wrong" below.

### 4. A scope stop-rule with the force of a hard rule
`precheck-tolerances.json` already documents that coupled-line synthesis is not
implemented. S11 **read it, quoted it, and implemented a PDE solver anyway.**
Prose in a data file does not bind. This belongs in SKILL.md's hard rules:

> *If the Recipe requires synthesis or capability the repo does not implement,
> stop and escalate to the user. Do not implement it.*

### 5. A per-session budget cap with escalation on breach
S11 spent **250 parts and 151,526 tokens with nothing on disk**. Any cap — parts,
tokens or wall — that escalates rather than continues would have converted a
51-minute total loss into a 5-minute question.

## Do next — the structural one

### 6. Ticket 14, scoped as a session-boundary state machine
This is the largest lever and the campaign gave it three independent
justifications:

- **S11**: a Clarification block became an unbounded numerical-methods project.
- **`shiny-canyon`**: 1.58 M tokens, abandoned — the same mechanism at scale.
- **88% cost spread on byte-identical prompts** (X0a 106,932 vs X0b 201,765,
  both succeeding). Run-to-run variance is what a deterministic orchestrator
  removes; nothing else in the backlog touches it.

Scope it narrowly: *what a session of each type may and may not do*. Clarification
may not write code. Build may not solve. That is structural, where §4 and §5 are
advisory and will hold only until they are inconvenient.

## Do after that

### 7. Wave B — build the five corrected specs on hardware
**Everything measured so far is offline.** The compiler has never met the
geometry these cells produced. Wave B is now the highest-information work
remaining: it tests the compiler on novel structures, exercises the landed
readout fix, and produces the first solved result since it. Prep is done —
license reachable, no stray desktops, five corrected specs at `escape_hatch=0`.

### 8. Break the pre-check's circularity
X0a iterated `precheck` to −0.00%; S1 computed its dimensions with the same
`hfss_spec.physics` module `precheck` validates against. A `consistent` verdict
on an authored spec currently means *fitted*, not *checked*.

Cheapest useful step: **flag a delta of exactly 0.00% as suspicious** rather than
ideal, and record per run whether the agent invoked `physics.py` or re-ran
`precheck`. A genuinely independent second implementation is the real fix and is
much more work — S3's −0.09% shows what an honest residual looks like.

### 9. Cheap missing estimators
Dipole λ/2, monopole λ/4, circular patch (S6 already drafted
`circular_patch_resonance` from Balanis 14-8/14-9/14-10 and proposed it for
approval). Each closes a `no-estimator` hole. Low priority *individually* — but
S6 did the work already, so accepting that amendment is nearly free.

## What I would NOT do

- **A v2 array/duplicate op as a priority.** S7 disproved the standing
  hypothesis. It is a token-cost and readability win, not an unblocking one.
- **More offline authoring cells.** U1 is answered. S9/S10/S2 would add coverage
  with low marginal learning against Wave B.
- **Prompt engineering as the lever.** Every defect found was a *domain default*
  or a *missing boundary*, not a misunderstanding of the request. The agent
  reasoned correctly and thoroughly in all six cells.

## What I got wrong, recorded

- I reported **3/6 cells producing specs** while four runs were still in flight,
  and built a headline on it. All six produced specs. Fixed, and the rule is now
  in the runbook: do not read a cell until its run has exited.
- I recommended **"build gates"** before S11 ran. S11 showed gates that *inform*
  get read and ignored. The recommendation survives only for gates that **block**
  or that encode a relation the agent cannot tune — which the three in §1–§3 do.
- I flagged **X0b's `c0`** as possibly undeclared; it is a correct built-in.

## Sequencing, honestly

§1–§3 and §5 are days of work and would have prevented five of six measured
defects and one 51-minute loss. §4 is an hour. §6 is the real project. §7 is
where the next unknown lives.

If only one thing gets done: **§6**, because §1–§5 are guards on a process that
has no boundaries, and the two most expensive events in this tool's history
(`shiny-canyon`, S11) were both that missing boundary.

If only one *cheap* thing gets done: **§1**, the λ₀/3 default — one value,
five of six specs corrected, zero agent cost.

## A caveat that should travel with every number here

The X0 replicates cost **106,932 and 201,765** for the same prompt, both
succeeding. **No single-cell cost figure in this campaign is reliable**, and cells
must not be ranked by cost. Every conclusion above rests on *behaviour* observed
across cells, or on defects confirmed by human review — not on single-run
token counts.
