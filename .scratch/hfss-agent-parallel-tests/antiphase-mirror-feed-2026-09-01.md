# The 2x2 feed is broken, and every gate passed it

Found 2026-09-01, from the radiation pattern of the banked `patch-array-5800`
solve. This is the falsification `TASK-verify-2x2-feed.md` was written to
produce and did not get on 2026-08-18, because the pattern was never read.

**The corporate feed excites the two E-plane element pairs 180 degrees out of
phase. There is no length error anywhere in the network, every line is the
impedance it should be, the chain closes, and S11 looks plausible. The defect
is that mirrored elements are fed from a mirror-symmetric network, which
inverts the resonant mode of one of them.**

---

## The measurement

Read from the banked solve (Normal Completion, 150 sweep points) via the native
`ReportSetup` route, infinite sphere theta -90..90 step 2 deg, phi 0 and 90.

| cut | broadside (theta=0) | lobes |
|---|---|---|
| 5.66 GHz, phi=0 (H-plane) | -6.85 dB | one, -28 deg / -3.34 dBi |
| 5.66 GHz, phi=90 (E-plane) | -6.85 dB | **-36 deg / +6.85 dBi and +36 deg / +9.25 dBi** |
| 5.00 GHz, phi=90 (E-plane) | -11.47 dB | **-36 deg / +6.03 dBi and +34 deg / +6.08 dBi** |

The E-plane cut is a **split beam with a null on boresight**: a local minimum of
-8.97 dBi at theta = -2 deg, about 18 dB below the peak. At 5.00 GHz the two
lobes are matched to within 0.05 dB, so the amplitude split is fine - the error
is purely phase.

S11 at the same frequency is -7.369 dB, and `RealizedGain - Gain` is -0.91 dB
against a mismatch loss of -0.879 dB predicted from that S11 (agreement 0.03
dB), so the far-field and S-parameter data are mutually consistent.

## Why a split beam with a boresight null means antiphase

Two elements driven in phase add at broadside. Driven 180 degrees apart they
cancel there, and the array factor's maxima move off-axis; for lambda/2 spacing
the factor alone would peak at +/-90 deg, and the patch element pattern rolling
off toward the horizon pulls the product inward - to +/-36 deg here. Spacing is
confirmed lambda0/2: `S = 25.8442 mm = 0.5000 lambda0` at 5.8 GHz, in **both**
axes, verified in the spec and independently in the built model (united-body
extents 21.556 and 19.734 mm match `S/2 + W/2` and `S/2 + L/2` exactly).

A progressive phase taper would squint a **single** beam. Two symmetric lobes is
specifically an antiphase pair.

## Walking the feed: the lengths are all correct

Port at the board edge (y = -35 mm), trunk running +y, T1 splitting to +/-x
arms, T2 splitting each arm to +/-y branches.

| segment | Z | length (mm) |
|---|---|---|
| `InLine` | 50 | 27.3444 |
| `Xfmr1` | 35.36 | 7.6556 (= `q_x` = lambda_g/4) |
| `Arm` L/R | 50 | 5.2665 |
| `Xfmr2` L/R | 35.36 | 7.6556 (= `q_x`) |
| `Up`/`Down` | 50 | 8.1102 |
| **total port -> patch** | | **56.0323, identical for all four** |

`UpL` and `DownL` are exactly mirror-equal about y = 0. **There is no
path-length error to find.** That is what makes this defect interesting: the
usual suspect is absent.

## Where the 180 degrees actually comes from

```
P1 (lower) spans y[-19.734, -6.110]
P2 (upper) spans y[ +6.110, +19.734]

DownL reaches y = -8.110  ->  enters P1 at its HIGH-y edge (-6.110), inset 2 mm
UpL   reaches y = +8.110  ->  enters P2 at its LOW-y  edge (+6.110), inset 2 mm
```

The two patches are fed **from opposite radiating edges**, because the feed is
mirror-symmetric about y = 0 and so are the elements. Feeding a patch from the
opposite radiating edge inverts the sign of its resonant mode, which is a 180
degree flip of the radiated field. The network is symmetric; the excitation is
antisymmetric.

This also predicts the other cut correctly. y is `patch_L`, the resonant
direction, so a y-mirror inverts the mode and the E-plane splits. x is
`patch_W`, the non-resonant direction, so an x-mirror does **not** invert the
mode - and the H-plane shows only a modest single squinted lobe (-28 deg) from
lesser asymmetries. The mechanism accounts for both axes, not just the one it
was derived from.

## Why every existing gate passed it

- `feed_check.walk` verifies **impedances and chain closure**. Every line is the
  width it should be, both quarter-wave transformers are `lambda_g/4`, and the
  chain closes to 50 ohm. All true, and all irrelevant to this defect.
- Path lengths are equal, so any length-based check would also pass.
- `validate_spec`, `precheck` and `compile_spec --dry-run` all passed on
  2026-08-18 with `errors=0`.
- **S11 does not reveal it.** An antiphase pair still presents a sensible input
  impedance; the -7.4 dB in-band dip looked like a tuning issue. The run
  concluded exactly that.

Nothing in the repo examines **the sense of the feed point relative to the
element's resonant axis**. That is the gap.

## Proposed gate — flagged, not built

**Rule:** for an array of resonant elements fed by one network, every element
must be fed from the same-sense radiating edge relative to its own resonant
axis. Mirrored elements fed by a mirror-symmetric network are antiphase.

Shape it as a relational check in `model_checks` (the family that already owns
`radiation_clearance` and `port_geometry`): for each element, determine the
resonant axis from its own dimensions, find where the feed conductor meets it,
and compare the sense across elements. Disagreement is the finding.

Three cautions before anyone builds it:

1. **Antiphase is sometimes deliberate.** Some designs invert an element and
   compensate with a `lambda_g/2` offset. The check must compare *net* phase
   sense - feed edge together with branch length - not feed edge alone, or it
   will fire on correct designs.
2. It needs the element's resonant axis, which for a patch is inferable from
   `patch_L` vs `patch_W` but is not a general property of an arbitrary
   conductor. Scope it to the recipes where the axis is known.
3. This is exactly the "gate that encodes a relation the agent cannot tune"
   that RECOMMENDATIONS section 3 argued for - and unlike clearance, it is not a
   rule of thumb with a fuzzy threshold. A sense mismatch is discrete. That
   makes it a better candidate for ERROR than either gate currently in that
   family. See the deferred severity decision in `RECOMMENDATIONS.md`.

## The fix to the design itself

Any one of: route both +/-y branches so each patch is entered from the same
sense; add `lambda_g/2` to one branch to undo the mirror; or move one patch's
inset to its opposite edge. All are one-variable or one-op changes to the spec.

## Standing caveat

The solve these numbers come from adapted its mesh at **5 GHz**, not the design
frequency, because of the compiler defect recorded separately (`compiler.py`
wrote pyAEDT's template default). The dB values here will move after a correct
re-solve. The **diagnosis** should not: the split-beam structure is present at
both 5.00 and 5.66 GHz, it is a geometric phase effect, and it follows from the
feed topology by inspection independently of any solve.
