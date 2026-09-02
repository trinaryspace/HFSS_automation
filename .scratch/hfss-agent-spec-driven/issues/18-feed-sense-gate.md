# 18 — Feed-sense gate: mirrored elements fed by a symmetric network are antiphase

**Status:** needs-triage — raised 2026-09-01 from a confirmed hardware defect.

**What to build:** a relational check, in the `model_checks` family that already
owns `radiation_clearance` and `port_geometry`, that compares **the sense of
each element's feed point relative to that element's own resonant axis** across
an array, and reports a finding when they disagree without compensating phase.

## Why — this is not hypothetical

`workspaces/patch-array-5800` was built, gated and solved with **`errors=0` on
every offline check**, and its corporate feed excites the two E-plane element
pairs 180 degrees out of phase. Measured from the banked solve: a split beam
with lobes at -36 deg / +6.85 dBi and +36 deg / +9.25 dBi and an ~18 dB null on
boresight; at 5.00 GHz the lobes match within 0.05 dB, so it is purely phase.

Full evidence and the walk:
`.scratch/hfss-agent-parallel-tests/antiphase-mirror-feed-2026-09-01.md`.

The defect has an unusual shape, and that shape is the argument for the gate:

- **No length error exists.** All four port-to-patch paths are 56.0323 mm.
- **No impedance error exists.** Every line is its intended width, both
  transformers are `lambda_g/4`, the chain closes to 50 ohm.
- `feed_check.walk` therefore passes, correctly, and is blind to it.
- **S11 does not show it.** An antiphase pair still presents a sensible input
  impedance; the in-band -7.4 dB dip was read as a tuning issue and the run
  closed with the feed declared *not* falsified.

The 180 degrees comes from geometry alone: the network is mirror-symmetric about
y = 0 and so are the elements, so one patch is entered at its low-y radiating
edge and its mirror twin at its high-y edge. Feeding a patch from the opposite
radiating edge inverts its resonant mode.

Only the radiation pattern reveals this, and the pattern is not part of any
offline gate. That is the hole.

## Design cautions, from the investigation

1. **Antiphase is sometimes deliberate.** A design may invert an element and
   compensate with a `lambda_g/2` offset. The check must compare **net** phase
   sense — feed edge *together with* branch electrical length — not feed edge
   alone, or it fires on correct designs. This is the main reason it is filed
   rather than built.
2. It requires the element's **resonant axis**. For a rectangular patch that is
   inferable from `patch_L` vs `patch_W`; for an arbitrary conductor it is not.
   Scope it to recipes where the axis is known, and return no finding rather
   than a guess elsewhere — `model_checks`' own docstring records that a
   confident-but-wrong geometric inference is the failure mode to avoid.
3. It needs to identify which conductor is the feed for which element, which the
   spec does not state directly. After the `unite` op the whole top conductor is
   one body, so the check must run on the pre-unite ops or on the spec, not on
   the built model.

## Severity — a better ERROR candidate than the two that exist

RECOMMENDATIONS section 3 argued that a gate only binds if it blocks, and
`validate.py` shipped `radiation_clearance` and `port_geometry` as WARNINGs
because both encode a rule of thumb with a fuzzy threshold, where an ERROR would
block legitimate designs.

**A feed-sense mismatch is not a rule of thumb.** It is discrete: either the
net excitation of two elements agrees in sign or it does not. There is no
tolerance to argue about, and no legitimate design is blocked by being asked to
declare a deliberate inversion. If any check in this family should be an ERROR,
this is the strongest candidate — stronger than the two the original
recommendation was written about.

That decision is still the maintainer's, and it is coupled to the deferred
severity call recorded in `RECOMMENDATIONS.md`.

## Acceptance

- [ ] Reproduces the defect: the check fires on `patch-array-5800`'s spec as
      authored, with a message naming the two elements and their feed edges.
- [ ] Does not fire on a corrected variant (one branch offset by `lambda_g/2`,
      or both patches entered from the same sense).
- [ ] Does not fire on any single-element case in `knowledge/cases/`.
- [ ] Returns no finding, rather than a guess, when the resonant axis cannot be
      determined.
- [ ] Severity decided explicitly and the reasoning recorded, per section 3.
