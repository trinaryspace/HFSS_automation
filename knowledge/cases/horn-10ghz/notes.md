# horn-10ghz - in schema v1 (changed 2026-08-14)

This case exists to be **hard**, and it was originally written as the
scope-pressure case: a pyramidal horn's flare is swept/lofted geometry, and
schema v1 was not going to express it.

**That changed on 2026-08-14.** Checking the KB before reaching for an
external CAD kernel showed the HFSS native modeler already has the
operations: `sweep_along_vector` carries a `draft_angle` (a pyramidal horn
is a rectangle swept with draft), and `connect` is HFSS's loft between
profiles (throat rectangle to aperture rectangle). Horns are a structure
that matters here, so the schema covers them natively — which also keeps
them fully parametric, where an externally-built and imported horn would
not be (imported CAD retains no construction history).

So this case is now a **build target**, not a scope-pressure case. The
escape-hatch metric needs a different out-of-scope case; the proposal is
imported vendor CAD — a connector or housing — which is genuinely not
expressible as a parametric spec and is a real need. That is still open.

## Reference numbers

- WR-90: `a` = 22.86 mm, `b` = 10.16 mm, TE10 cutoff **6.5571 GHz**
- free-space wavelength at 10 GHz: **29.9792 mm**
- aperture and flare lengths follow standard-gain horn synthesis for
  about 15 dBi

## Cost warning

This is the expensive case: an air volume many wavelengths across, and a
gain/pattern QA signal that needs a far-field setup. It runs at Tier 2, on
purpose, and only at a phase gate.

## Aperture and flare dimensions — added 2026-08-15

The case shipped with only WR-90's feed dimensions and a note that "aperture
and flare lengths follow standard-gain horn synthesis for ~15 dBi". Those
numbers now exist, synthesised rather than copied, by
`hfss_spec.physics.optimum_pyramidal_horn` (Balanis ch.13 optimum-gain
procedure):

| quantity | value | relation |
|---|---|---|
| aperture a1 | 77.3482 mm | `a1 = sqrt(3*lambda*rho_h)` |
| aperture b1 | 57.1475 mm | `b1 = sqrt(2*lambda*rho_e)` |
| rho_e | 54.4683 mm | E-plane flare slant |
| rho_h | 66.5209 mm | H-plane flare slant |
| axial length | 38.1275 mm | `pe = ph`, the realisability condition |

**Optimum** means the flare that maximises gain for a given axial length,
which fixes the aperture phase error at the classic values above. A pyramidal
horn additionally has to be *buildable*: both flares must meet the feed
waveguide at the same axial station, `pe == ph`. Balanis reduces that pair to
one transcendental equation in `chi = rho_e / lambda`; the implementation
solves it by bisection instead of by hand iteration.

### Two checks, because these are computed numbers rather than sourced ones

- **Closed the loop.** Feeding the synthesised aperture back through the gain
  relation `G0 = 0.51 * (4*pi/lambda^2) * a1 * b1` returns **14.9859 dBi**
  against the 15.0 requested (−0.09%), and `pe − ph` comes out below a
  micron. The synthesis is self-consistent.
- **Reproduced a textbook example.** The same routine at 22.6 dB and 11 GHz on
  WR-90 — Balanis's own worked pyramidal-horn example — returns a1 163.59 mm,
  b1 128.50 mm, rho_e 302.94 mm, rho_h 327.31 mm, which is the published
  answer.

### Known fragile

- `chi` must be solved for by scanning, not by iterating up from Balanis's
  trial value `G0/(2*pi*sqrt(2*pi))`. At 15 dBi on WR-90 that trial value
  (2.008) sits **above** the root (1.817), so an upward search never brackets
  it. Higher-gain horns do not have this problem, which is exactly why it is
  easy to miss.
- 15 dBi is a small horn: the aperture is only ~2.6 x 1.9 wavelengths, so the
  0.51 aperture-efficiency constant is doing more work here than it would on a
  20 dB horn. Treat the gain prediction as ±0.5 dB, not ±0.05 dB.
- The gain estimator predicts aperture gain only. Pattern symmetry — one of
  this case's QA signals — is not predicted by any closed form here.
