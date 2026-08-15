# Phase 2 in detail — the Design Spec and the compiler

Status: needs-triage (this is the document to argue with)
Feature: hfss-agent-spec-driven

Phase 2 is the one real bet in the plan, and the tickets state *what* to
build without showing *what it looks like*. This document shows it — real
YAML, real call sequences, real failure messages — and ends with the open
questions where your judgement decides the design. Everything here is a
proposal, not a decision.

---

## 1. What actually changes

Today, one Spine stage means: the model writes a `.py` file, we compile it,
launch AEDT, run it, read a `PASS:` line, and hope re-running it converges.
The script is the artifact. It is generated fresh every run, it can fail in
unbounded ways, and it can silently drift from the model it built.

Under phase 2, the model writes **one document** for the whole build, and a
tested compiler turns it into AEDT calls. The document is the artifact.

```
                     TODAY                              PHASE 2
              ---------------------            ---------------------------
  artifact    10 generated .py files           1 design.yaml
  validity    py_compile + PASS line           JSON Schema + reference +
                                                units + physics pre-check
  when        after AEDT launched              before AEDT launched
  idempotent  because each script                by construction
                remembers to be
  sync        replay 8 scripts on a            diff two documents
                second desktop
  re-derived  every run                        never (compiler is library code)
```

The Spine does not change. The stages do not change. Their completion
criteria do not change. What changes is **who writes the code that walks
them** — a model, per run, versus a tested compiler, once.

---

## 2. A real `design.yaml`

This is `patch-2400` from the canonical set, written out in full. Numbers
are the ones in `knowledge/cases/patch-2400/case.json`.

```yaml
spec_version: 1
name: patch-2400
recipe: inset-fed-rectangular-patch
solution_type: Modal            # explicit, never the default (env-compat #11)

provenance:
  source: "Balanis, Antenna Theory ch.14 design procedure"
  canonical_reading: closed-form   # Table | Figure | equations | closed-form
  case: knowledge/cases/patch-2400

target:
  quantity: resonant_frequency
  value: 2.4GHz
  tolerance_pct: 5

variables:                      # every one becomes an AEDT design variable
  f0:        2.4GHz
  er:        4.4
  h:         1.6mm
  patch_W:   38.0100mm
  patch_L:   29.4216mm
  feed_W:    3.0829mm
  inset_d:   9.0mm
  inset_g:   1.0mm
  sub_W:     "patch_W + 6*h"    # expressions reference earlier variables
  sub_L:     "patch_L + 6*h"
  air_pad:   "0.25 * c0 / f0"   # c0 is a provided constant

materials:
  substrate: {library: FR4_epoxy, permittivity: er, loss_tangent: 0.02}

geometry:
  - {op: box,   name: Substrate, material: substrate,
     origin: ["-sub_W/2", "-sub_L/2", 0], size: [sub_W, sub_L, h]}
  - {op: sheet, name: GroundPlane, material: pec, plane: xy,
     origin: ["-sub_W/2", "-sub_L/2", 0], size: [sub_W, sub_L]}
  - {op: sheet, name: Patch, material: pec, plane: xy,
     origin: ["-patch_W/2", "-patch_L/2", h], size: [patch_W, patch_L]}
  - {op: sheet, name: Feed, material: pec, plane: xy,
     origin: ["-feed_W/2", "-sub_L/2", h], size: [feed_W, "sub_L/2 - patch_L/2 + inset_d"]}
  - {op: sheet, name: InsetL, plane: xy,
     origin: ["-feed_W/2 - inset_g", "-patch_L/2", h], size: [inset_g, inset_d]}
  - {op: sheet, name: InsetR, plane: xy,
     origin: ["feed_W/2", "-patch_L/2", h], size: [inset_g, inset_d]}
  - {op: subtract, name: Patch, tools: [InsetL, InsetR], keep_tools: false}
  - {op: unite,    name: Patch, with: [Feed]}
  - {op: box, name: AirBox, material: vacuum,
     origin: ["-sub_W/2 - air_pad", "-sub_L/2 - air_pad", "-air_pad"],
     size:   ["sub_W + 2*air_pad", "sub_L + 2*air_pad", "h + 2*air_pad"]}

excitations:
  - name: P1
    type: lumped_port
    on: {face_of: Feed, direction: "-y"}      # symbolic — never a face id
    integration_line: {from: {edge_mid: [Feed, "-y", "min_z"]},
                       to:   {edge_mid: [Feed, "-y", "max_z"]}}
    impedance: 50ohm

boundaries:
  - {name: Rad, type: radiation, on: {outer_faces: AirBox}}
  - {name: GndPEC, type: perfect_e, on: {object: GroundPlane}}

mesh:
  - {type: adaptive_only}

setup:
  name: Setup1
  solution_frequency: f0
  max_passes: 6
  delta_s: 0.02
  sweep:
    name: Sweep1
    type: interpolating
    start: 2.0GHz
    stop: 3.0GHz
    count: 101

qa_signals: [convergence, ports_excited, in_band_resonance, energy_pass]
```

Three things to notice, because they are the design decisions:

**Units are on every dimensional value.** `1.6mm`, `2.4GHz`, `50ohm`. A
bare number is only legal where the quantity is dimensionless (`er: 4.4`,
`count: 101`). Unit mismatch becomes a schema error rather than a geometry
that silently builds a thousand times too large.

**Variables carry expressions.** `sub_W: "patch_W + 6*h"` is not evaluated
away — it is passed through to AEDT as a design variable expression, so the
parametric link survives into the UI. Change `patch_W` in the AEDT variable
table and the substrate follows, exactly as PLAN.md's full-parameterization
rule intends. The validator evaluates it too, but only to check
dimensionality and catch cycles.

**Faces are named symbolically, never by id.** `{face_of: Feed,
direction: "-y"}` is resolved by the compiler against the live model at
build time. This is env-compat #7/#8 ("assign by face object, never
ids/edges") encoded as a *type* rather than as a rule someone has to
remember while writing a script.

---

## 3. What the compiler does with it

`compile(spec, hfss)` walks the same Spine stages, in the same order, and
emits the same Verification lines. For the geometry stage it is roughly:

```python
def build_geometry(spec, hfss, log):
    created = []
    for item in spec.geometry:
        if item.op in ("box", "sheet", "polyline"):
            # Idempotency is a property here, not a discipline (ADR 0008):
            # the compiler always deletes what it is about to create.
            if item.name in hfss.modeler.object_names:
                hfss.modeler.delete(item.name)
            obj = PRIMITIVES[item.op](hfss, item)      # tested per primitive
            if item.material:
                obj.material_name = resolve_material(spec, item.material)
            created.append(obj.name)
        elif item.op == "subtract":
            hfss.modeler.subtract(item.name, item.tools, keep_originals=item.keep_tools)
        elif item.op == "unite":
            hfss.modeler.unite([item.name] + item.with_)
    bbox = hfss.modeler.get_bounding_box(created)
    log.verification("geometry", objects=len(created), bbox=bbox)
    #  -> PASS: geometry objects=6 bbox=[...] 
```

The important part is what is *not* there: no branching on what the model
decided to do this time, no re-derivation, no per-run creativity. Every
primitive has a golden test (`spec fragment -> expected call sequence`,
mocked) that runs in Tier 0 with no license.

Selector resolution is the one genuinely tricky piece:

```python
def resolve_face(hfss, selector):
    """{face_of: Feed, direction: '-y'} -> a FacePrimitive, or a clear error."""
    obj = hfss.modeler[selector.object]
    axis, sign = parse_direction(selector.direction)      # 'y', -1
    candidates = [f for f in obj.faces if normal_is(f, axis, sign)]
    if not candidates:
        raise SelectorError(f"{selector!r}: {selector.object} has no {selector.direction} face")
    if len(candidates) > 1:
        # Disambiguation rule — see open question Q3.
        candidates.sort(key=lambda f: -f.area)
    return candidates[0]
```

---

## 4. What the validator catches, before AEDT is ever launched

All of this runs in Tier 0, in milliseconds, with no license:

```
$ python scripts/validate_spec.py knowledge/cases/patch-2400/design.yaml

FAIL: validate_spec errors=3 warnings=1

  errors:
    geometry[3].size[1]        unit mismatch: 'sub_L/2 - patch_L/2 + inset_d'
                               mixes mm and GHz via 'inset_d' (declared 9.0GHz)
    excitations[0].on          face_of: 'Fed' is not a declared object
                               (did you mean 'Feed'?)
    variables.air_pad          cycle: air_pad -> sub_W -> air_pad

  warnings:
    setup.sweep                range 2.0-3.0GHz brackets target 2.4GHz by
                               only 0.4GHz on the low side; a resonance
                               below 2.0GHz would be invisible
```

Four check classes, in order of how often they will fire:

1. **Schema** — shape, types, required fields. Free, from Pydantic.
2. **Reference resolution** — every selector names a declared object, every
   variable reference resolves, every material exists. This is the class
   that today costs an AEDT launch and a failed stage to discover.
3. **Units and dimensions** — expression dimensionality, sweep brackets the
   target, no negative or zero extents.
4. **Recipe completeness** — the spec declares everything its recipe needs.
   This is the "critical setup features the user left out" check from the
   Clarification contract, made mechanical.

---

## 5. The physics pre-check (ticket 09)

Separate from validation, and the part that actually helps with
electromagnetics rather than with driving AEDT:

```
$ python scripts/precheck.py knowledge/cases/patch-2400/design.yaml

  patch resonant length (Balanis 14-7)
      spec patch_L        29.4216 mm
      closed-form         29.4216 mm       agreement: exact

  implied resonance from spec geometry
      target              2.4000 GHz
      closed-form         2.4000 GHz       delta: +0.00%   tolerance: 5%

PASS: precheck recipe=inset-fed-rectangular-patch verdict=consistent
```

And the case it exists for — the Astuti bow-tie, whose dimensions killed
the pilot:

```
  dims cross-check: INCONSISTENT
      Table I says     46.00 x 23.00 mm
      Fig 1 reading    52.64 x 26.32 mm     disagreement: 14.4%
      equations give   52.64 x 26.32 mm

  implied resonance from Table I geometry
      target           3.5000 GHz
      closed-form      4.0100 GHz          delta: +14.6%   tolerance: 8%

FAIL: precheck verdict=inconsistent — arbitrate before building
```

That verdict costs microseconds. In the pilot, the same discovery cost
roughly twenty hours, four solves, and the run.

It never blocks and never overrides — the user arbitrates which reading is
canonical, and the choice is recorded in `provenance.canonical_reading`.

---

## 6. Where the spec runs out

The escape hatch stays, and it is not a failure mode. A stage the schema
cannot express falls back to a hand-written staged script exactly as today:

```yaml
geometry:
  - {op: escape_hatch, name: HornFlare, script: src/geom_horn_flare.py,
     reason: "swept/lofted flare is not expressible in schema v1",
     provides: [HornFlare]}
```

The compiler runs it, records it in the ledger, and the run card counts it.
`provides:` tells the validator which object names to expect afterwards, so
selectors elsewhere in the spec can still be checked. **Escape-hatch rate
is the metric that tells us whether the schema is right.** `horn-10ghz` is
in the canonical set precisely to keep that number honest.

---

## 7. Sync as a spec diff (ticket 12)

After a Review-gate tweak in the AEDT UI:

```
$ python scripts/sync_check.py --workspace workspaces/patch-2400

  variables.inset_d     spec 9.0mm        model 8.4mm       <- user tweak
  setup.max_passes      spec 6            model 8           <- user tweak
  geometry[2].size[0]   spec 38.0100mm    model 38.0100mm      ok

  2 differences, both representable in the spec.
  Apply to design.yaml? [y/N]
```

That replaces: copy the workspace, launch a second port-pinned desktop,
replay eight staged scripts, capture a snapshot, diff, tear down. Six
rounds of that at roughly eight minutes each was a measurable fraction of
the pilot.

The interesting case is a tweak the spec *cannot* represent — the user
adds a fillet, say. Then the diff has to say so rather than silently
dropping it, which is open question **Q5**.

---

## 8. Open questions — where I want your judgement

These are the decisions I do not think I should make alone. My
recommendation is given, but the reasoning matters more than the answer.

**Q1 — How much geometry does v1 need?**
Options: (a) primitives only — box, sheet, cylinder, polyline+cover;
(b) primitives plus booleans — unite, subtract, intersect; (c) plus
sweeps and lofts. The patch and microstrip need (a). The bowtie and the
inset feed need (b). The horn needs (c).
*Recommendation: (b).* It covers four of five canonical cases, and (c) is
where the schema starts turning into a CAD kernel. But you know the EM
structures you actually want to build — if half of them need lofts, (b) is
the wrong line and I should know that now.

**Q2 — Should variables carry expressions, or only literals?**
Expressions keep the parametric link alive in AEDT and make user tweaks
propagate, which is what PLAN.md wants. The cost is that the validator
needs a small expression evaluator with unit awareness.
*Recommendation: yes, expressions* — the parametric link is most of the
tool's value. But it is real work and it could be deferred to v2.

**Q3 — How should ambiguous selectors disambiguate?**
`face_of(Feed, -y)` can match several faces. Candidate rules: largest area
(my default above); nearest to a stated point; or refuse and require the
spec to be more specific.
*Recommendation: refuse by default, with an explicit `pick: largest_area`
opt-in.* Silent selection of the wrong face is the kind of bug that
produces a model that builds fine and simulates nonsense — which is the
worst failure class this tool has.

**Q4 — Does the spec own mesh operations, or is v1 adaptive-only?**
The pilot ran adaptive-only and it was fine.
*Recommendation: adaptive-only in v1*, with mesh operations as an
escape-hatch stage — unless your real work routinely needs explicit mesh
refinement, in which case it belongs in the schema from the start.

**Q5 — What happens when a UI tweak cannot be represented in the spec?**
Options: (a) report it and let the spec go stale, recording the drift;
(b) refuse to close the Review gate until the tweak is expressible or
reverted; (c) auto-generate an escape-hatch fragment capturing it.
*Recommendation: (a) with a loud ledger entry.* (b) fights the user, and
(c) is magic that will eventually produce something wrong. But this is a
workflow question about how you actually use the Review gate.

**Q6 — Should the spec cover setup and sweep, or stop at the model?**
*Recommendation: cover them* — they are purely declarative and it makes the
spec a complete description of the simulation. The solve *submission* stays
imperative, under the watchdog, unchanged.

**Q7 — Sequencing: should `snapshot_to_spec` come first?**
Ticket 12 needs a snapshot-to-spec reducer anyway. If it is built *first*,
it can generate `design.yaml` for the pilot workspace automatically from
the snapshot already on disk — which would validate the schema against a
real model on day one instead of after the compiler exists.
*Recommendation: yes, build it first*, and reorder 07 -> 12a
(`snapshot_to_spec`) -> 08 -> 10 -> 11. It converts ticket 11's acceptance
from "write a spec by hand and hope" into "generate it, then prove the
compiler reproduces it". This is the change I am most confident about and
the one I would most like your read on.

**Q8 — Is one `design.yaml` per run right, or one per design?**
A sweep (ticket 16) generates N. Re-entry copies an existing project that
has no spec at all.
*Recommendation: one spec per design, with the workspace holding one by
default* — and for Re-entry, `snapshot_to_spec` produces the spec from the
copied project, which is a rather good answer to "how do we handle projects
we did not build".

---

## 9. What I would do first, once you have answered

1. `snapshot_to_spec` against the pilot snapshot (Q7) — produces a real
   `design.yaml` with no schema guesswork.
2. Schema v1 shaped by what that reducer actually had to emit.
3. Validator, then physics pre-check — both Tier 0, both immediately
   useful even if the compiler slips.
4. Compiler, one primitive at a time, each with a golden test.
5. Ticket 11's acceptance: compile the generated spec, diff against the
   stored snapshot, classify every residual difference.

Steps 1-3 are useful on their own. If phase 2 stalls after step 3, the repo
still gains a physics pre-check and a way to describe a model as data —
which is most of the leverage for a fraction of the work.

---

## Comments

### Answers to the open questions

Fill in the `Answer:` lines below (or strike a question out if it is moot).
My recommendation is restated in one line so you can just agree or push
back; the reasoning is in section 8. Anything left blank stays open and
blocks nothing except the ticket that depends on it.

**Q1 — geometry scope for v1.** Recommend (b) primitives + booleans.
Answer: C. I want this to be flexible for future use as well, horns are important structures. Since you said it would increase complexity drastically, can we look into using an external cad kernel thats better at these things?

**Q2 — expressions in variables, or literals only.** Recommend expressions.
Answer: yes, absolutely

**Q3 — ambiguous selector disambiguation.** Recommend refuse by default,
with an explicit `pick:` opt-in.
Answer: Your reccomendation is good. 

**Q4 — mesh ops in the schema, or adaptive-only v1.** Recommend adaptive-only.
Answer: adaptive only for now

**Q5 — UI tweaks the spec cannot represent.** Recommend (a) report and
record the drift.
Answer: Loud ledger entry is good. Keep track of what cannot be tracked so the user knows

**Q6 — does the spec cover setup + sweep.** Recommend yes.
Answer:yes

**Q7 — build `snapshot_to_spec` first.** Recommend yes, reordering to
07 -> 12a -> 08 -> 10 -> 11.
Answer: Yes, tell me what I need to do on my end to make this more robust 

**Q8 — one spec per design.** Recommend yes, with Re-entry getting its spec
from `snapshot_to_spec`.
Answer: yes, good catch because sometimes I will want to start with an existing project. 

### Anything else

Free-form: constraints I have not asked about, structures you actually
build that the canonical set misses, or parts of section 2's `design.yaml`
that look wrong to you.

---

## 10. Resolved — decisions from the answers above (2026-08-14)

| Q | decision |
|---|---|
| Q1 | **(c) full geometry incl. sweeps and lofts — built on the HFSS native modeler, NOT an external kernel.** See below. |
| Q2 | Expressions in variables. Passed through to AEDT as design-variable expressions. |
| Q3 | Ambiguous selectors **refuse** by default; explicit `pick:` opt-in. |
| Q4 | Adaptive-only mesh in v1; mesh ops via escape hatch. |
| Q5 | Report drift with a **loud ledger entry**, and explicitly record what could not be tracked. |
| Q6 | Spec covers setup + sweep. Solve submission stays imperative under the watchdog. |
| Q7 | Build `snapshot_to_spec` first. Reorder 07 -> 12a -> 08 -> 10 -> 11. |
| Q8 | One spec per design; Re-entry derives its spec from `snapshot_to_spec`. |

### Q1 in detail — why the external CAD kernel is the wrong tool here

The request was (c) with horns as a first-class structure, and an ask to
look at an external CAD kernel since (c) sounded expensive. Checking the
KB first changed the answer: **the HFSS native modeler already has the
operations a horn needs**, and they are already scraped.

- `Modeler3D.sweep_along_vector(assignment, sweep_vector, draft_angle,
  draft_type)` — extrude with a **draft angle**. A pyramidal horn is a
  rectangle swept along a vector with a draft angle. One call.
- `Modeler3D.connect(assignment=[...])` -> `oEditor.Connect` — HFSS's
  loft/blend between profiles. Connect a throat rectangle to an aperture
  rectangle and the flare is exact rather than approximated.
- `sweep_along_path` / `sweep_around_axis` — conical horns, bends, helices,
  bodies of revolution.
- `create_polyline` (with segment types) + `thicken_sheet` — arbitrary
  profiles for anything the above misses.

So (c) costs **three or four more ops in the schema**, not a CAD kernel.

Going the external route (CadQuery / build123d / OCCT -> STEP ->
`import_3d_cad`) would cost more than it buys, and the cost lands precisely
on the answers given above:

1. **It destroys parametrics — which contradicts Q2.** Ansys is explicit:
   imported structures retain no construction history and *are not
   parameterizable on import*; editing is limited to scaling, reorienting,
   and booleans. A horn built externally could not be swept from the AEDT
   variable table, so ticket 16's parametric sweep would not work on it,
   and "user tweaks are variable edits" would stop being true for exactly
   the structures that matter most.
2. **It makes Q3 worse.** Imported bodies have no meaningful face names, so
   "refuse ambiguous selectors" degrades into "cannot select at all", and
   port assignment by face object (env-compat #7/#8) gets much harder.
3. **It adds a heavy dependency and a second geometry semantics** to build,
   test, and keep in sync — plus STEP healing and tolerance debugging,
   a classic EM-simulation time sink.

The one parametric external route Ansys does support is the live SpaceClaim
link (`import_spaceclaim_document` / `break_spaceclaim_connection`), which
is a different product dependency and out of scope here.

**Where external CAD does belong: the escape hatch.** `import_3d_cad` is
the right op for geometry you *receive* rather than design — vendor
connectors, housings, radomes. That is a real need, it is genuinely not
expressible as a parametric spec, and it is the honest thing for the
escape-hatch rate to be measuring.

### Consequences to fold in

- Schema v1 op list gains: `sweep_along_vector` (with `draft_angle`),
  `connect` (loft), `sweep_along_path`, `sweep_around_axis`,
  `polyline`, `thicken_sheet`, and `import_cad` (escape-hatch op).
- `horn-10ghz` moves **into** schema v1 (`case.json` updated). It stops
  being the scope-pressure case, so the escape-hatch metric needs a new
  out-of-scope case — proposed: an imported vendor connector. **Open: is
  that the right one, or is there a structure you build that you expect
  the schema to fail on?**
- Ticket 07's scope widens; ticket 10 gains one tested primitive per op.

### One honest caveat on Q7

`snapshot_to_spec` can only reduce what `capture_state.py` captures:
objects + bboxes + materials + boundaries + excitations + setups/sweeps +
variables. That is **descriptive, not constructive** — a bounding box
cannot tell you whether a solid was a box or a lofted horn, so the reducer
recovers roughly the non-geometry 70% of a spec exactly, and the geometry
ops only approximately.

This does not sink Q7, it scopes it: build the reducer first for
variables, materials, boundaries, excitations, setup and sweep (where it
is exact and immediately useful, including for Re-entry per Q8), and design
the **geometry op list from the construction side** using the canonical
cases. Ticket 12a records this split explicitly.
