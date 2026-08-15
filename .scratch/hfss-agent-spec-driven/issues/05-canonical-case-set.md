# 05 — Canonical case set: end N=1 acceptance

**What to build:** A regression set of five canonical structures, so that
acceptance stops being a single pilot whose failure modes cannot be
disentangled. The `shiny-canyon` NO-GO is the argument: with N=1 there is no way
to separate "the refactor regressed" from "this paper's geometry was internally
inconsistent" from "the readout path was broken" — and the retrospective shows
all three tangled together. Published comparators run 110 cases (Foam-Agent) and
315 (ChatCFD); five is not that, but five is enough to localise a regression.
Choose for coverage of the Spine rather than variety of physics: **inset-fed
rectangular patch** (the original Proof-1 recipe), **bowtie** (the measured
baseline, so history is comparable), **microstrip line** (trivial geometry,
exercises ports and Z0 — the fastest Tier 1 case), **coupled-line filter**
(multi-object geometry, multiple ports), **horn** (swept/lofted geometry, the
schema's hardest shape). Each case is a directory holding its source recipe
notes, its expected key dimensions, its QA signals, and — once ticket 07 lands —
its `design.yaml`. Until then they are fixture data and Tier 1 build targets.

**Blocked by:** None. Becomes far more useful after 07/10, but the cases can be
written now and are needed to scope the schema honestly.

**Status:** ready-for-human

- [x] Five case directories under `knowledge/cases/`, each with recipe source, key dimensions, target quantity, and QA signals
- [x] Every dimension traceable to a vetted source (textbook or self-consistent paper); the Astuti bowtie is explicitly excluded or annotated as the known-inconsistent case
- [x] At least one case is deliberately cheap enough for routine Tier 1 runs (microstrip line)
- [x] The horn case is written even though the schema will not cover it at v1 — it is the scope pressure that keeps the schema honest
- [x] Cases referenced from the spec's testing section and from `verify_skill.py`

## Comments

- 2026-08-14: **DONE.** Five cases under `knowledge/cases/`, each with a
  machine-readable `case.json` (recipe, substrate, target quantity and
  tolerance, key dimensions with provenance, QA signals) and a `notes.md`
  recording where the numbers come from and what is fragile.
- **Every dimension recomputed, not copied.** Patch: Balanis ch.14 —
  W=38.0100 mm, ereff=4.0857, dL=0.7388 mm, L=29.4216 mm at 2.4 GHz on
  1.6 mm FR4. Microstrip: Hammerstad-Jensen solved for 50 ohm — W/h=1.92684,
  W=3.0829 mm, ereff=3.3323, guide wavelength 68.4282 mm. Filter reuses
  that 50 ohm synthesis for its feed width, which makes the shared number a
  cross-check. Horn: WR-90, TE10 cutoff 6.5571 GHz, lambda 29.9792 mm.
  Digits are carried past what the physics justifies so ticket 09's
  estimators can be checked against them exactly.
- **Astuti et al. 2022 is excluded as a source** and annotated in
  `bowtie-3500/notes.md` as the known-inconsistent counter-example. That
  case's dimensions come from the delivered pilot model on disk instead,
  and its measured 3.85 GHz resonance against a 3.5 GHz target is recorded
  honestly rather than corrected — ticket 09's estimator should be checked
  against the behaviour that was actually observed.
- `microstrip-50r` is the cheap routine Tier 1 case (two ports, one trace),
  and the only one whose target is an impedance rather than a resonance, so
  it exercises a different estimator and a different QA signal.
- `horn-10ghz` is written and marked `schema_v1: false` on purpose: it is
  the scope pressure. If the other four need zero escape-hatch scripts and
  the horn needs some, the schema is correctly scoped.
