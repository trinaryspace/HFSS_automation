# The airbox clearance defect: not a missing default

Written 2026-08-31, while trying to implement RECOMMENDATIONS section 1. The
implementation was abandoned deliberately. Section 1's premise is wrong, and
what is underneath it is more actionable than the feature would have been.

Every claim here was re-verified against the code on 2026-08-31.

---

## What section 1 assumed

> `air_pad` (or the boundary's clearance) defaults to `c0/(3*f0)` when
> unspecified. Keep it overridable - but then the override is a visible decision.

That presumes a named clearance field with an "unspecified" state. Neither
exists.

## Why there is nothing to default

**There is no clearance field.** `hfss_spec/schema.py` has no airbox, pad or
clearance field anywhere; `Boundary` carries `name`, `type`, `on`,
`conductivity`. Clearance is an emergent property of six independent expressions
in the `origin` and `size` of an ordinary `op: box`, which is identified as the
airbox only by being the target of a `radiation` boundary selector.

**There is no unspecified state to default.** All 13 specs in the repo declare an
explicit pad. Zero omit one. A default-when-absent would fire on none of them,
including none of the six measured campaign cells:

| spec | pad as authored | clearance today |
|---|---|---|
| S1 | `air_pad: 13mm` | 13.00 mm on +z vs 17.23 required |
| S3 | `air_pad: 0.4in` | unchecked - see below |
| S4 | `AirGap: 30.6mm` | 30.60 mm on -z vs 40.79 |
| S7 | `air_pad: 12.9221mm` | 12.92 mm on -x vs 17.23 |
| X0a | `air_pad_side: 15mm`, `air_pad_top: 31.2mm` | 15.00 mm on -x vs 41.64 |
| X0b | `air_pad: "0.25 * c0 / f0"` | 31.23 mm on +z vs 41.64 |

X0b is the one that settles it. That author already had `c0` and already used
the expression idiom - and still chose the coefficient `0.25`. The measured
defect is authors choosing a **too-small coefficient**, not authors omitting a
value. No defaulting mechanism of any shape addresses that.

**The pad has no canonical name or shape.** Names in the corpus: `air_pad` (9),
`AirGap` (2), `air_pad_side` + `air_pad_top` (1). Shapes differ deliberately:
patch-2400 pads symmetrically on six faces; horn-10ghz is flush at -z (port
plane); patch-array-5800 and S7 are flush at -y (port face); bowtie-3500 pads
singly on x and doubly on y; microstrip-50r has no lateral pad at all. One
scalar cannot express that.

## The actual mechanism: one contaminated exemplar, copied

RECOMMENDATIONS called this "a missing default, not five mistakes". It is
neither.

- `skill/hfss-agent/SKILL.md:53` and `skill/hfss-agent/reference/design-spec.md:53`
  both tell the authoring agent by name to start from `knowledge/cases/*/design.yaml`,
  singling out `patch-2400` as "a model that has been built and solved here".
- `knowledge/cases/patch-2400/design.yaml:38` reads
  `air_pad: 31mm   # ~lambda0/4 at f0`. Lambda0/3 at 2.4 GHz is 41.64 mm. **The
  named exemplar under-pads at exactly lambda0/4, and says so in a comment.**
  It trips the very warning that was added to catch this.
- No case file anywhere uses the compliant `c0 / (3 * f0)` idiom, so there is no
  worked example of the correct form to copy instead.
- `reference/design-spec.md`, the "how to write a design.yaml" document, never
  mentions airbox sizing, clearance or lambda0 at all. Its "reading a validator
  finding" section shows only an errors block, never warnings - which is where
  clearance lands.
- `hfss_spec/schema.py` carries zero `description=` arguments, so the JSON Schema
  used for constrained decoding gives no field-level guidance either.

Four independent agents choosing lambda0/4 is what copying a lambda0/4 exemplar
looks like.

## A second defect: the clearance check is inert on a whole class of specs

`hfss_spec/model_checks.py`, `_target_frequency`:

```python
setup = getattr(spec, "setup", None)
if setup is not None:
    hz = _num(getattr(setup, "frequency", None), {}, FREQUENCY)
```

`Setup`'s field is `solution_frequency`, not `frequency`. Verified:
`sorted(Setup.model_fields)` is
`['delta_s', 'max_passes', 'name', 'solution_frequency', 'sweep']`, and the model
is `extra="forbid"`. **The fallback is dead.** So whenever `target.quantity` is
not one of the frequency literals, `_target_frequency` returns `None` and
`radiation_clearance` returns `[]` immediately - the check silently does not run.

Measured consequences:

- `horn-10ghz` (target `gain`) - **unchecked**. It would pass if checked, so
  RECOMMENDATIONS' "only the horn met lambda0/3" is true by luck: the checker
  never verified it.
- `S3` (target `gain`) - **unchecked**. Would pass.
- `microstrip-50r` (target `characteristic_impedance`) - **unchecked**, and
  *would warn if the fallback were repaired*: 12.00 mm on +z against 41.64 mm.

The `"cutoff_frequency"` branch in the same function is also dead - it is not a
member of `Target.quantity`'s `Literal`.

This was left unfixed on purpose. Repairing the attribute name is a one-word
change, but it immediately raises a question that is not the fixer's to settle:
whether a lambda0/3 radiation-clearance rule should apply to a non-radiating TEM
line like `microstrip-50r`. That is adjacent to the open WARNING-vs-ERROR
decision and belongs to the rule's owner.

## A third defect, found while repairing the second (2026-09-01, NOT fixed)

`port_geometry` reads `exc.on.object` raw instead of going through
`_selector_object`. `Excitation.on` is a
`Union[FaceOf, ObjectRef, OuterFaces]`, and **5 of the 12 lumped ports in the
corpus declare `face_of`** - S1, X0b, patch-2400 and the `fixed/` copies of the
first two. Those ports are invisible to the width check.

This is the same class of defect as the one `_selector_object`'s own docstring
records having already fixed for the clearance rule: a selector read one way in
one place and another way elsewhere. It is currently *masked*, because
`port_geometry` returns early unless the spec contains a cylinder - so no
finding is missing today. It is a latent false negative that will surface the
first time a `face_of` port meets a cylindrical conductor.

Left unfixed deliberately: it was found during a scoped repair of
`_target_frequency`, and fixing it would have changed the blast radius that
repair was measuring. It wants its own change with its own before/after count.

Worth noting what these three defects have in common. None of them made a gate
say something wrong; each made a gate **quietly say nothing**. The clearance
rule returned `[]` on a whole class of specs, `port_geometry` skips half the
ports it was written for, and the lambda0/3 default was believed to exist for
two weeks. A gate that is silent is indistinguishable from a gate that passed,
which is the same reason `read_results.py` exists and the same reason section 2
of RECOMMENDATIONS made `UNCHECKED` its own word.

## What the fix actually looks like

1. **Fix the exemplar. Cheapest, highest yield, and the thing that actually
   binds.** `patch-2400`'s `air_pad: 31mm` becomes `"c0 / (3 * f0)"`, and
   `reference/design-spec.md` shows the compliant idiom. The catch that makes
   this a maintainer call: `patch-2400` is documented as a model built and
   solved on this box, so editing its geometry breaks that correspondence -
   `docs/agents/fixture-fidelity.md` territory. Either re-solve it, or split the
   exemplar from the solved record.
2. **A schema-level preventer needs a new `radiation_box` geometry op**, not a
   defaulted field: the author declares `encloses: [...]` and `flush: [...]`
   explicitly and `pad` defaults to `c0/(3*f0)`. The box can be emitted
   parametrically with `min(...)`/`max(...)` over the enclosed ops' own
   expressions - both are already in `expressions.FUNCTIONS` and AEDT evaluates
   them - so the parametric link survives. `model_checks` already has most of the
   machinery (`bounding_box`, excitation-exclusion, the flush-face rules).
   This was not built: it extends schema v1's op set, which is the LLM's
   constrained-decoding contract; it changes no defect rate until the skill and
   the exemplar point at it; and inferring which bodies to enclose and which
   faces are deliberately flush would be a heuristic *writing geometry*, which is
   the confident-but-wrong failure `model_checks`' own docstring exists to
   prevent. With `encloses`/`flush` explicit it is safe - but then it is a new
   authoring burden, not the zero-cost default section 1 promised.
3. Repair `_target_frequency`'s dead fallback, and decide separately whether the
   clearance rule applies to non-radiating recipes.

## The general lesson

Section 1 was the campaign's most confident cheap recommendation - "If only one
*cheap* thing gets done: the lambda0/3 default, one value, five of six specs
corrected, zero agent cost." It was diagnosed from the specs' output without
reading the authoring path that produced them. The defect was upstream of
everything it proposed to change.
