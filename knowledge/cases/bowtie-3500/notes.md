# bowtie-3500 - the baseline and pilot class

Kept so measurement history stays comparable: `silent-engine` (398,130
tokens) and `shiny-canyon` (1,579,333) both built this class, and any
future run card is read against them.

## Provenance - read this before using any number here

The dimensions come from **the delivered pilot model on disk**
(`workspaces/bowtie-3500-pilot/`), not from the paper the pilot started
from. Astuti et al. 2022's bow-tie is **internally inconsistent**: the
authors' equations do not reproduce their own Table I / Fig 1, and their
real patch was about `2*26.32` base with roughly `26.32` sides. That
discrepancy survived clarification, geometry, materials, excitations, mesh,
setup, validation and four solves, and was caught by the user at the
results read roughly twenty hours in.

That failure is why ticket 09 (closed-form pre-check) exists. This case
keeps the paper as a **counter-example fixture**: a good dimension gate
should flag it, and that is a test, not a build target.

## Known fragile

- The delivered model resonates at **3.85 GHz against a 3.5 GHz target**
  (S11 about -4 dB). That is recorded honestly rather than corrected: it is
  the measured behaviour of the geometry that was actually built, and
  ticket 09's estimator should be checked against it.
- Tolerance is 8%, wider than the patch case, because the bow-tie's
  resonance is less sharply set by a single closed-form length.
