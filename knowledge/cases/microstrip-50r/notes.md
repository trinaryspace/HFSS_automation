# microstrip-50r - the cheap Tier 1 case

Deliberately the most boring structure in the set. Two wave ports and one
rectangular trace: it builds in well under a minute, so it is the case that
runs on every Tier 1 pass while the others run per phase gate.

## Where the dimensions come from

Hammerstad-Jensen, `W/h > 1` branch, solved for 50 ohm on 1.6 mm FR4:

- `W/h` = **1.92684** -> width **3.0829 mm**
- effective permittivity **3.3323**
- guide wavelength at 2.4 GHz **68.4282 mm**; the line is a half wavelength,
  **34.2141 mm**, so a mismatch shows as a clear periodic ripple rather than
  a flat trace

## Why it earns its place

It is the only case whose target is an **impedance** rather than a
resonance, so it exercises a different closed-form estimator and a
different QA signal. A tool that gets patches right and lines wrong has a
port problem, and this case isolates it.
