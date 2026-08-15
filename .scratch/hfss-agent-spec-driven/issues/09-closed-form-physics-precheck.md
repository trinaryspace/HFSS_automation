# 09 — Closed-form physics pre-check: the EM value-add

**What to build:** A deterministic, offline module that predicts a design's
target quantity from its spec using textbook closed-form relations, and compares
that prediction against the design's stated goal *before* anything solves. This
is the part of the tool that helps with **electromagnetics** rather than with
driving AEDT, and it is the highest-value-per-token component in this plan: a
7-minute solve and hours of downstream conversation are spent to discover things
a formula answers in microseconds. Per recipe: patch resonant length from
effective permittivity, bowtie/dipole resonance, Hammerstad-Jensen microstrip
Z0 and effective permittivity, substrate-λ scaling, and a coupled-line estimate.
The check prints both numbers and the disagreement — `target 3.5 GHz, closed-form
predicts 4.21 GHz (+20%)` — and Clarification surfaces it for the user to
arbitrate. It never blocks and it never overrides the user; the playbook's
tolerance per recipe decides what counts as a disagreement worth raising.

This generalises perf-refactor ticket 09 (paper dimension gate) from a prose
instruction in `SKILL.md` into a function that runs. The motivating failure is
exact: the Astuti bow-tie's equations did not reproduce its own Table I / Fig 1,
the discrepancy survived clarification, geometry, materials, excitations, mesh,
setup, validation, and **four solves**, and was caught by the user at the results
read roughly twenty hours in. A closed-form check on the locked dimensions would
have flagged it in the Clarification block.

**Blocked by:** 07 (needs the spec to read dimensions from).

**Status:** ready-for-human

- [x] One estimator per v1 recipe, each citing its source relation in a docstring
- [x] Estimators unit-tested against textbook worked examples with known answers
- [x] Per-recipe tolerance lives in the playbook, not in code
- [x] Verdict line prints target, prediction, and signed disagreement; never blocks
- [x] Astuti bow-tie dimensions reproduced as a fixture and flagged by the check
- [x] The pilot's delivered geometry (resonance measured at 3.85 GHz against a 3.5 GHz target) is reproduced and the check's prediction compared against the measured result — an honesty test of the estimator itself

## Comments

- 2026-08-15: **IMPLEMENTED** - `hfss_spec/physics.py`, CLI
  `scripts/precheck.py`, tolerances in
  `knowledge/playbook/precheck-tolerances.json`. Reported (never enforced) for
  every canonical case by `scripts/validate_cases.py`, which runs in Tier 0.

- **The honesty test passed, and it is the reason to trust the rest.** The
  bow-tie estimator - a bow-tie as a pair of triangular patches, dominant TM10
  of an equilateral triangle, `f = 2c / (3a*sqrt(ereff))` with `a` the leg -
  predicts **3.8782 GHz** for the pilot's delivered geometry. That model
  **measured 3.85 GHz**: an error of **+0.7%**. An estimator that could not
  reproduce a measured result has no business flagging anyone's paper.

- **And it flags the failure it exists for.** Against the pilot's own 3.5 GHz
  target the same prediction is **+10.81%**, past the 8% tolerance:

        leg / side             26.3269 mm
        base                   20.2168 mm
        ereff (14-1 on base)   3.8317

        target                 3.5000 GHz
        closed-form            3.8782 GHz      delta: +10.81%   tolerance: 8%

        FAIL: precheck recipe=bow-tie-patch verdict=INCONSISTENT - arbitrate before building

  That verdict costs microseconds. In the pilot the same discovery cost
  roughly twenty hours, four solves, and the run.

- **The Astuti fixture.** Table I's 46 x 23 mm reading predicts ~4.33 GHz,
  **+23.7%** against the stated 3.5 GHz target, and disagrees with the Figure
  reading (52.64 x 26.32) by more than a GHz. Both readings are in the test
  suite, so the paper's self-contradiction is now a regression test rather
  than a story.

- **Estimators and their worked examples**, each checked against numbers
  recomputed in `knowledge/cases/*/case.json` rather than copied:
  Balanis 14-1 effective permittivity (4.0857), 14-2 fringing (0.7388 mm),
  14-7 patch resonance (returns the 2.4 GHz the case was synthesised for),
  Hammerstad microstrip (ereff 3.3323, Z0 50.0 ohm at W/h 1.92684), guide
  wavelength (68.4282 mm), WR-90 TE10 cutoff (6.5571 GHz).

- **Two design decisions worth recording.**
  1. **Permittivity is read from wherever the spec puts it** - an `er`
     variable, an inline material definition, or a known library reference.
     The bow-tie spec has no `er` variable because its substrate is a
     user-defined `FR4_43` material; an estimator that only looked at
     variables could not check it at all.
  2. **The horn's check is band membership, not a percentage.** Its stated
     target is a gain in dBi, which no closed form here predicts, so the
     check asks whether TE10 propagates and stays single-mode
     (`1 < f/f_c < 2`) and says so, rather than inventing a number to
     disagree with.

- Not done: a coupled-line estimator. The filter recipe currently reuses the
  microstrip synthesis for its feed line only, and the playbook entry says so
  explicitly - a PASS there means less than it does for the other recipes.

