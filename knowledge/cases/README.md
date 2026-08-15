# Canonical case set

Five structures the tool is expected to build correctly, used as the
regression set that ends N=1 acceptance (ticket 05).

The `shiny-canyon` pilot is the argument for this directory. With a single
case there was no way to separate "the refactor regressed" from "this
paper's geometry was internally inconsistent" from "the readout path was
broken" — and the retrospective shows all three tangled together. Five
cases do not make a benchmark (Foam-Agent runs 110, ChatCFD 315), but they
are enough to localise a regression to a layer.

Chosen for coverage of the Spine, not variety of physics:

| case | why it is here | schema v1 | Tier 1 cost |
|---|---|---|---|
| `patch-2400` | the original Proof-1 recipe; the reference inset-fed patch | yes | medium |
| `bowtie-3500` | the measured baseline and pilot class, so history stays comparable | yes | medium |
| `microstrip-50r` | trivial geometry, exercises ports and Z0; the routine Tier 1 case | yes | cheap |
| `coupled-filter-2400` | multi-object geometry, multiple ports, synthesised dimensions | yes | medium |
| `horn-10ghz` | swept/lofted geometry; **in** schema v1 from 2026-08-14 | yes | expensive |

`horn-10ghz` was written as the scope-pressure case, on the assumption that
schema v1 would not express a swept/lofted flare. The Q1 decision moved it
**into** scope: `sweep_along_vector` (with `draft_angle`) and `connect`
(loft) are native `Modeler3D` operations, so horns are built natively and
stay parametric. The escape-hatch metric therefore needs a new out-of-scope
case — the proposal is imported vendor CAD (a connector or housing), which
is genuinely not expressible as a parametric spec. Still open.

## Layout

Each case directory holds:

- `case.json` — machine-readable: recipe, substrate, target quantity, key
  dimensions with their provenance, QA signals, tolerance. Read by the
  closed-form physics pre-check (ticket 09) and, once it exists, by the
  Tier 1 runner.
- `notes.md` — the human record: where the dimensions come from, what the
  design equations say, and anything known to be fragile.

Once the spec schema lands (ticket 07) each case also gains a
`design.yaml`, and `case.json`'s dimensions become the assertion that the
spec agrees with its source.

## Provenance rule

Every dimension traces to a vetted source: a textbook relation that can be
recomputed, or a measured artifact in this repo. **No dimension is carried
over from Astuti et al. 2022** — that paper's equations do not reproduce
its own Table I / Fig 1, it is the failure this whole corrective phase
exists because of, and it is recorded in `bowtie-3500/notes.md` as the
known-inconsistent counter-example rather than as a source.

Closed-form values recorded here are estimates from the cited relation,
carried to more digits than the physics justifies so that ticket 09's
estimators can be checked against them exactly. They are inputs to a
cross-check, not ground truth about hardware.
