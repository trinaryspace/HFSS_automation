# coupled-filter-2400 - multi-object geometry, two ports

The first case where the geometry is not one solid. Three coupled sections
plus two feed lines means the spec has to express repeated, related objects
with a gap dimension between them - the shape that most pressures a
declarative schema.

## Where the dimensions come from

- Section length is a quarter guide wavelength on the same stack as
  `microstrip-50r`: **17.1071 mm** at 2.4 GHz.
- Feed width reuses that case's 50 ohm synthesis, **3.0829 mm**, which is
  deliberate: two cases sharing a derived number is a cross-check.
- Even/odd-mode impedances for the coupled sections follow the standard
  Cohn synthesis for a 3-section, 10% fractional-bandwidth Chebyshev
  response. Gap and width per section are produced by that synthesis and
  land in `design.yaml` when ticket 07 lands.

## Known fragile

- FR4 dispersion moves the passband center by a percent or two across the
  band; tolerance is 5% for that reason.
- Coupled-line gaps get small at this substrate height. A gap below roughly
  0.2 mm is a manufacturability flag, not a simulation error, and QA should
  say so rather than silently accepting it.
