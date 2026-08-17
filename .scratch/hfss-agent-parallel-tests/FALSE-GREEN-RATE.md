# The false-green rate — measured 2026-08-17

The number this campaign was built to produce. Human verdicts from the
maintainer, against six specs that had **all passed every automated gate**.

## Result

**6 of 6 specs passed `validate_spec`, `precheck` and `compile_spec --dry-run`
with zero errors and zero escape hatches. 3 of them had real defects.**

**False-green rate: 3/6 = 50%** — and 5/6 = 83% if the λ₀/3 airbox rule of thumb
is applied uniformly, which the maintainer stated as general guidance.

No automated gate flagged any of the three. Two were caught by a human reading
the spec; one only because a reviewer knew the design convention.

| cell | verdict | defect | would any gate have caught it? |
|---|---|---|---|
| X0a | **subtly wrong** | airbox side pad λ₀/10, needs ≥ λ₀/3 | no |
| X0b | correct | (airbox λ₀/4, under the λ₀/3 rule) | no |
| S1 | correct | (airbox λ₀/4, under the λ₀/3 rule) | no |
| S3 | correct | — | — |
| S4 | **subtly wrong** | port ribbon 4 mm on a 1 mm wire | no |
| S7 | **wrong** | all four elements mismatched 2:1 | no |

Confirmed correct by review: the patch dimensions (both replicates, blind), the
horn synthesis, the dipole's end-effect shortening, and every individual
microstrip line width in the array.

## The three defects, and why no gate could see them

### S7 — the array: right arithmetic, wrong design

This is the most instructive failure in the campaign.

Every line width was **individually correct**: 1.7427 mm really is 50 Ω on this
stack, 0.9464 mm really is 70.71 Ω, 0.4403 mm really is 100 Ω, and 70.71 =
√(50·100) is the right transformer impedance for that pairing. The network was
even **internally self-consistent**: 50 Ω in, two 100 Ω arms in parallel = 50 Ω,
a λ_g/4 at 70.71 Ω converting the 50 Ω parallel node up to match the 100 Ω arm.

The defect is at the **termination**. Those four 100 Ω lines end at patches whose
inset was computed for a **50 Ω** match. Every element was mismatched 2:1. A
network that is internally coherent and terminates into the wrong impedance is
invisible to any check that examines parts rather than the whole.

Maintainer's prescription — two transformer stages, patches kept at 50 Ω — is
also the cleaner topology, and it is what the fix implements:

```
patch 50 | two 50 in parallel = 25 | lambda_g/4 @ 35.36 -> 50   (T2, one per arm)
         | two 50 arms in parallel = 25 | lambda_g/4 @ 35.36 -> 50   (T1, trunk)
         | 50 ohm input
```

`Z = 50/√2 = 35.3553 Ω` since `√(25·50) = 35.3553`. Solved on this stack:
**W = 2.9084 mm, ε_eff = 2.8491, λ_g/4 = 7.6556 mm**. Three sections: one on the
trunk, one per arm. Substrate 52 → 70 mm (the array spans ±21.55 mm, so 52 mm
left only ~4 mm of board beyond the outer element edges).

### S4 — the dipole port

`PortW: 4mm` on a 1 mm wire across a 2 mm gap: the port sheet was 4× the
conductor width. The lumped port then presents a cross-section unrelated to the
dipole's, so the impedance it reports is not the antenna's. Fixed to `PortW:
WireD` — as wide as the wire, filling the gap.

Note this spec's `precheck` verdict was **`no-estimator`**, printed behind the
word `PASS:`. So the one cell with a genuinely unchecked physics path also had a
port defect, and the tooling said `PASS` twice.

### X0a — the airbox

λ₀/10 on the sides against λ₀/4 on top. λ₀/3 on every side is the rule of thumb;
15 mm at 2.4 GHz is too close for a radiation boundary. Fixed to 41.64 mm all
round.

**This one generalises.** Of six specs only S3 (the horn, ≈λ₀/3) met the rule.
X0b, S1 and S7 all chose λ₀/4 — better than X0a but still under. Four of five
patch-family specs under-padded, independently. That is not six random errors; it
is a **systematic default the tool does not have**, and it belongs in the playbook
or as a schema default rather than being rediscovered per run.

## What this says about the gates

The gates are not worthless — they caught nothing here because there was nothing
of *their* kind to catch. They verify units, dimensions, expression validity,
face resolvability and schema coverage, and all six specs were clean on all of
that. What they cannot see:

1. **Whether a network terminates into the impedance it was designed for** (S7).
2. **Whether an excitation's geometry matches the conductor it excites** (S4).
3. **Whether a boundary is far enough away to be a boundary** (X0a, and 3 more).

All three are relational properties of the whole model. Every one is also
**mechanically checkable** — see the improvement notes below. None of them
requires an LLM to be smarter; they require the gate to ask a question it does
not currently ask.

And the physics pre-check specifically cannot help, because §3 of the batch-1
findings showed it is *fitted to* rather than *checking* an authored spec: S1
computed its dimensions with the same `hfss_spec.physics` module `precheck`
validates against, and X0a ran `precheck` three times adjusting between runs.
Both reported `-0.00%`.

## Candidate gates this justifies building

Ranked by defect-caught per line of code:

1. **Airbox clearance check** — compute the distance from every radiating body's
   bounding box to the radiation boundary; warn below λ₀/3 at the target
   frequency. Would have caught 4 of 6 specs. Cheapest, broadest.
2. **Port-geometry sanity** — compare a lumped port sheet's width to the
   conductor it bridges; warn on a ratio beyond ~1.5x. Would have caught S4.
3. **Feed-network impedance walk** — from each port, walk the united conductor
   graph and check that the impedance presented at each junction matches the
   line meeting it, given the λ/4 sections in between. Would have caught S7.
   Much the hardest, and the only one that needs real topology reasoning.
4. **Flag `no-estimator` as its own verdict, not behind `PASS:`** — one line, and
   it stops a gate that checked nothing from looking like a gate that passed.

Items 1, 2 and 4 are small and would have caught 5 of the 6 defects. That is the
strongest argument in the campaign for spending effort on gates rather than on
prompting.

## Corrected specs

`cells/fixed/{X0a,S4,S7}.design.yaml` — all three re-gated:

```
X0a  validate errors=0 warnings=0   dry-run 9 ops   escape_hatch=0
S4   validate errors=0 warnings=0   dry-run 4 ops   escape_hatch=0
S7   validate errors=0 warnings=1   dry-run 28 ops  escape_hatch=0
```

Originals are untouched in `cells/` as evidence. X0b, S1 and S3 were judged
correct and are unmodified; their λ₀/4 airboxes are noted above but not changed,
since the maintainer passed them — that is a decision to confirm, not to assume.
