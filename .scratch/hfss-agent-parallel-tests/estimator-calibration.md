# Estimator calibration against hardware - the patch family, n=1

Written 2026-08-31 from the 2026-08-18 hardware run `patch-array-5800`
(`workspaces/patch-array-5800/summary.md`, `state.md`,
`results/state/solved.txt`). This file exists because RECOMMENDATIONS.md
section 8 asked for a check of `hfss_spec/physics.py` that is not a check of
`hfss_spec/physics.py`, and the array run produced one without anybody
noticing.

## The datapoint

| | value |
|---|---|
| estimator | `hfss_spec.physics.patch_resonance` (Balanis 14-1 / 14-2 / 14-7) |
| inputs | patch_L 13.6238 mm, patch_W 17.2679 mm, h 0.762 mm, er 3.48 |
| intermediate | ereff 3.242632, dL 0.364125 mm |
| **predicted** | **5.8000 GHz** (recomputed 2026-08-31: 5.799999 GHz) |
| **measured** | **5.6 GHz** - S11 dip, user's UI read, both designs |
| signed error, repo convention | **+3.57%** - `100*(predicted - target)/target` with the solve as target |
| signed error, prediction as denominator | **-3.45%** |
| stack | RO4350B er 3.48, tand 0.0037, h 0.762 mm, 1 oz copper (cu_t 0.035 mm), inset-fed |
| solver | AEDT 2024 R1 (`v241`), Modal, adaptive-only mesh, radiation airbox at lambda0/3 |
| solves | `#1b` ElementsOnly, Normal Completion, 10 adaptive passes, 150 sweep points; `#2` PatchArray, Normal Completion, 14 adaptive passes, 150 sweep points |
| readout route | AEDT UI (user-arbitrated); scripted readout failed, see `readouts.txt` |
| **n** | **1** |

Roughly 3.5% either way. Which denominator is right is a convention question,
not a physics one; the repo's `Prediction.delta_pct` uses the target as
denominator, so `+3.57%` is the number a re-registered `precheck` entry would
print if the solve were the target.

## Why this is the first honest residual on the patch family

RECOMMENDATIONS.md section 8 records the circularity precisely: a `consistent`
verdict on an authored spec means *fitted*, not *checked*.

- X0a ran `precheck` three times until the delta read -0.00%.
- S1 computed its patch dimensions by importing `hfss_spec.physics`, the same
  module `precheck` then validated it against.
- S3's -0.09% was held up as "what an honest residual looks like" - and S3 is
  a **horn**, a different estimator (`horn_cutoff`) on a different structure.
- `physics.py` itself now prints a NOTE when the delta is under 0.005%,
  telling the reader that the check is confirming its own arithmetic.

Nothing in that list is a measurement of the rectangular-patch closed form
against a solve. The array run is: the dimensions were locked by the task brief
before the run started (`TASK-verify-2x2-feed.md`: "Elements: patch_W
17.2679 mm, patch_L 13.6238 mm. Do not re-synthesise these"), the estimator was
run offline against them, and then a solver that knows nothing about Balanis
14-7 put the resonance 200 MHz lower. The prediction could not be tuned toward
the answer because the answer arrived afterwards, from a different tool.

Nobody connected the run to section 8 at the time. The run's own summary read
the shift as an element-level tuning issue and moved on - which was the right
call for that conversation, and leaves the calibration finding unfiled. This
file is that filing.

## It is element-level, not the feed

The same 5.6 GHz dip appeared in **both** designs - `ElementsOnly` (four
patches, one lumped port per notch mouth, no network) and `PatchArray` (the fed
corporate network). The elements-only design carries no feed network at all, so
no property of the feed can explain a shift that is present without it. That is
what makes the number usable as an estimator calibration point rather than a
feed diagnosis: the quantity `patch_resonance` predicts is the quantity that
moved.

The user's verdict on the run, verbatim: *"Yes looks good. So the resonance for
both the single patch and the array is at 5.6 GHz and are about 7dB deep. That
isn't outright failure, its just a tuning issue that can be corrected with a
human hand."*

## Consequence for the pending estimator proposal

The run proposed registering `patch_resonance` for the `corporate-patch-array`
recipe at a 5% tolerance, matching the existing `inset-fed-rectangular-patch`
entry (`workspaces/patch-array-5800/summary.md`, Learning-loop note 1; queued
in `knowledge/playbook/pending-amendments.md` item 1).

Approving that as written would be dishonest on this evidence. A
`tolerance_pct: 5.0` entry asserts that a disagreement under 5% is not worth
raising with the user. The single hardware check available against this
estimator, on this recipe, consumed about 70% of that budget. The tolerance
would then be quietly wider than the only error anyone has measured - and the
verdict it produces would read `consistent` on a spec whose real resonance sits
a quarter-band away.

The `inset-fed-rectangular-patch` entry's own note says why 5% was chosen there:
"Balanis 14-1/14-2/14-7 are good to a few percent on a thin substrate; FR4's own
permittivity tolerance dominates the error." That note is a statement about FR4.
This measurement is on RO4350B, whose permittivity tolerance is much tighter
than FR4's, and the residual is still 3.5%. So the existing justification does
not transfer to this stack unexamined.

At n=1 the defensible options are: register nothing and leave the recipe
`UNCHECKED`; or register with the measured residual written into the entry's
`note` so it travels with the number. Setting a tolerance from one point is
fitting a line to one dot.

## What the 3.5% is attributable to - unresolved

Three candidates, none tested, and this run cannot separate them:

- **The Balanis fringing model on this stack.** 14-2 gives dL = 0.364 mm here.
  The model is quasi-static and quoted at a few percent; a thin, low-er
  substrate is the regime where it is usually best, which argues against this
  being the whole story but does not rule it out.
- **The added copper thickness shifting the effective permittivity.** The run
  changed the conductor from zero-thickness sheets to 1-oz copper boxes
  (cu_t = 0.035 mm) at Review gate #3, and `effective_permittivity` takes no
  conductor-thickness term at all. Finite strip thickness lowers ereff, which
  moves resonance the wrong way (up), so on its own this predicts a shift
  opposite in sign to the one measured - worth stating, because it is the
  candidate most easily dismissed and the dismissal is itself evidence.
- **The inset notch perturbing the effective L.** The estimator takes patch_L
  and the fringing extension; it has no term for the notch that the feed line
  cuts into the patch (inset_d 2.0 mm, inset_g 1.0 mm). A notch loads the patch
  and moves resonance down, which is the observed direction.

**Attribution is open.** With one measurement and three plausible mechanisms -
one of which points the wrong way and two of which point down - there is no
basis for choosing. Do not let a plausible story about the notch become a
recorded cause. The correct statement is: the estimator over-predicted by about
3.5% on this stack, once, and why is not known.

Separating two of the three is a solve each, not a redesign: re-solve
`ElementsOnly` with the notch removed and the port moved to a patch edge, and
compare against the zero-thickness-conductor case. Solve `#1a` is already that
second control - flat-PEC `ElementsOnly`, Normal Completion, 2 adaptive passes,
150 sweep points, banked at 1787089477 - but **its resonance was never read
out**: it was superseded by the gate-3 copper change before any results were
taken, and the run's only readouts are of `#1b` and `#2`. If that solve's data
survives in the banked project, the copper-thickness arm costs a readout rather
than a solve. That is a future task, not a claim.

## What would make this a tolerance rather than a datapoint

- A second hardware point on the same estimator at a different frequency or
  substrate. Two points on the same stack tell you about scatter; two stacks
  tell you whether the error is the model or the material.
- The notch-vs-no-notch control above, which would move the residual from
  "unattributed" to "attributable", and a residual with a known cause can be
  corrected rather than budgeted for.
- Re-running the estimator against the pilot's delivered bow-tie and patch
  cases, where solved results already exist on disk, to see whether a
  systematic over-prediction shows up there too. That is offline work and needs
  no licence.

Until then: one dot, recorded, with its error bars unknown.
