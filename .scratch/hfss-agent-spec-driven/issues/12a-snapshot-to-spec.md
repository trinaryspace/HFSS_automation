# 12a — `snapshot_to_spec`: derive a spec from a live model

**What to build:** The reducer that turns `results/state/model_snapshot.json`
into a `design.yaml`. Sequenced **before** the schema (Q7): a schema designed
in the abstract is guesswork, and the pilot workspace already holds a real
captured model to shape it against. It also answers Re-entry (Q8) — a project
we did not build gets a spec by reduction rather than by archaeology, which is
the mechanism ADR 0001's copy-first ceremony has been missing.

Scope is set by what `capture_state.py` actually captures, and that boundary
must be explicit because it is **descriptive, not constructive**:

- **Exact, build these first:** variables (with their AEDT expressions
  intact), materials, boundaries, excitations with their types and
  assignments, setups, sweeps, solution type, design and project names.
- **Approximate, and honestly marked:** geometry. A bounding box cannot
  distinguish a box from a lofted horn, so the reducer emits geometry as
  best-effort — a `box`/`sheet` guess where the bbox and object type agree,
  and an explicit `op: unknown` carrying the captured bbox and object name
  where they do not. `op: unknown` is a first-class value, never a silent
  wrong guess.

The geometry op list is therefore designed **from the construction side**
(ticket 07, using the canonical cases), not from the reducer. The reducer's
job is to prove the other ~70% of the schema against a real model on day one,
and to make Re-entry work.

Where `capture_state.py` turns out to lack something the spec needs, extend
it here and record the addition — it is the same seam.

**Blocked by:** None. Do it before 07 so the schema is shaped by a real model.

**Status:** ready-for-human

- [x] `snapshot_to_spec(snapshot) -> dict` reduces variables, materials, boundaries, excitations, setup and sweep exactly, with AEDT variable expressions preserved verbatim
- [x] Geometry is best-effort; anything not confidently identified emits `op: unknown` with its bbox and name, and a count of unknowns is reported
- [x] Run against `workspaces/bowtie-3500-pilot/results/state/model_snapshot.json` and record in Comments exactly which fields came out exact, approximate, or missing — that list is ticket 07's input
- [x] Round-trip test at Tier 0: snapshot -> spec -> snapshot-shaped dict, comparing the exact fields only
- [x] Any `capture_state.py` extension needed is made here and noted
- [x] Re-entry path documented: copy project (ADR 0001) -> `capture_state` -> `snapshot_to_spec` -> spec is the model card

## Comments

- 2026-08-14: Filed per Q7/Q8 of `phase-2-detail.md`. Recommended order is
  now **12a -> 07 -> 08 -> 10 -> 11**, which turns ticket 11's acceptance
  from "hand-write a spec and hope" into "generate it, then prove the
  compiler reproduces it".

- 2026-08-14: **Two reference models captured by hand** (`scripts/capture_live.py`,
  read-only against a live UI session) and cross-checked offline with
  `scripts/verify_snapshot.py`. Both are in `knowledge/cases/_snapshots/`.
  They immediately surfaced three defects and four schema findings.

**Defects found in `capture_state.py` — all silent, all now fixed:**

1. **Setup properties were never captured.** pyAEDT 1.3.0's `Setup` has no
   `get_properties()`; it exposes `props` / `properties`. The probe was
   `hasattr(setup, "get_properties")`, always False, so every snapshot ever
   taken recorded `{}` for every setup — including the pilot's, which is
   ticket 11's acceptance target. **This is a live false-negative in the
   sync-verify runner (ticket 12): setups compared `{}` to `{}`, so a user
   changing max-passes or delta-S in the UI produced a PASS.**
2. **Model units were not recorded.** Bbox numbers are in the modeler's
   display units while variables carry explicit units, so the two could
   only be compared by inferring the scale. Observed across three models:
   **inches** (horn), **centimetres** (patch), **millimetres** (pilot).
3. **Ports were invisible.** `excitations` came back empty on all three
   models across both solution types (Modal and Terminal); ports live in
   `boundaries` typed `Wave Port`. A reducer reading `excitations` would
   have found no ports at all. A derived `ports` section now handles this;
   both raw sections are untouched.

Snapshot format is now `snapshot_version: 2`. Regression tests added for
all three.

**Schema findings for ticket 07:**

- **Variable-to-variable expressions are real and in use.** The patch
  carries `gnd_x: subX`, `gnd_y: subY` — AEDT stores them as expressions,
  confirming Q2 from live evidence rather than from argument.
- **Non-length variables share the table.** `design_freq: 10GHz` sits
  beside lengths, so the schema's `variables` section must be typed by
  quantity, not assumed dimensional.
- **Metal is boundary-assigned, not material-assigned.** `antennaMetal`,
  `groundMetal`, `coax_outer` are `Perfect E` boundaries on sheets. The
  draft `design.yaml` in `phase-2-detail.md` used `material: pec` on a
  sheet, which is the other valid pattern — **the schema must express
  both**, and the reducer must not confuse them.
- **`sweeps` mixes real sweeps with parametric variation strings.** Both
  the patch and the pilot carry an entry like
  `"ATK_Solution - coax_inner_rad='0.025cm' ... : Table"` alongside
  `LastAdaptive` / `SParam_Sweep` / `FF_Sweep`. The reducer must split
  these; the variation string is a parametric table, not a sweep.

**What the bbox check validated (offline, no AEDT):** horn 11/14 bbox
dimensions derive exactly from its design variables, patch 20/24. The
unexplained ones are the radiation box in both cases — sized with a
literal pad (10.000 mm per side on the horn), not a variable. That is
precisely the object a spec would parameterize (`air_pad`), and it is a
good argument that the reducer should flag literal-driven objects rather
than silently emitting magic numbers.

**What remains unrecoverable, confirming the `op: unknown` design:** the
horn's flare and a rectangular box of the same extent are byte-identical
in a snapshot. The construction op is not recorded and cannot be inferred
from a bounding box — the variables carry the design intent, the bboxes
only confirm it.

- 2026-08-14: **Three more reference models captured** — parabolic reflector,
  cavity bandpass filter, coplanar waveguide. Five models total now, and they
  broke the port derivation and settled the `op: unknown` design question.

**Defect found and fixed: terminals were counted as ports.** Ports and their
terminals are BOTH typed `Wave Port` in the boundary list. The coplanar
waveguide lists six port-typed boundaries — `1, 1_T1, 1_T2, 2, 2_T1, 2_T2` —
for a **two-port** line, because terminal-solution designs add one
`<name>_T<n>` terminal per conductor per port. `split_ports()` now applies a
`_T\d+$` rule, verified across all seven snapshots: coplanar 6 -> 2 ports +
4 terminals, bandpass 4 -> 2 + 2, probe-fed patch 2 -> **1 port** + 1
terminal, horn and parabolic 1 -> 1 + 0. A separate `terminals` section is
recorded. **This corrects an earlier claim that the probe-fed patch has two
ports — it has one.** No re-capture needed: raw `boundaries` are preserved,
so ports/terminals recompute from existing snapshots.

**The parabolic settles `op: unknown`.** Only **2 of 18** bbox dimensions
derive from its design variables, and that is the correct answer rather than
a failure: a paraboloid's bounding box is a NONLINEAR consequence of focal
length and radius. `Reflector` z reads `2*Major_Radius`, but the y extent
(10.6671 cm) is the parabolic sag, which no linear combination of
`Focal_Length` / `Major_Radius` / `Offset` reproduces. For curved geometry
the snapshot says almost nothing about construction — the bbox is a
consequence of the op, not a restatement of it. The reducer must emit
`op: unknown` and lean on the variables for intent.

**Low scores have two distinct causes, and the reducer should say which:**

| model | explained | cause |
|---|---|---|
| coplanar WG | 14/19 | clean parametric box geometry |
| bandpass | 21/45 | **unparameterized** — only `Cavity_*` and `line_thickness` are variables; `l1`-`l4` lengths are literals |
| parabolic | 2/18 | **curved** — nonlinear geometry, not expressible linearly |

**Further schema findings for ticket 07:**

- **Project-scoped variables exist.** The coplanar model carries `$losstan`;
  the `$` prefix is a separate AEDT namespace from design variables. The
  schema needs both scopes, and a reducer that flattens them writes back to
  the wrong place.
- **User-defined materials.** The coplanar substrate is `myfr4`, not a
  library entry. The schema needs inline material DEFINITIONS, not only
  library references — the draft `design.yaml` had only the latter.
- **Boundary and setup shapes vary more than two models suggested.** The
  parabolic uses `FE-BI` boundaries (hybrid FEM-BI region) and has **42**
  setup properties against 38 for the others.
- **Duplicate/mirror naming.** The bandpass carries `l1`/`l1_1`,
  `feedpin1`/`feedpin1_1` across all 15 objects — a duplication pattern the
  schema should be able to express rather than enumerate.

**Still untested:** every port across all five models is a **wave port**. The
port-detection logic has never seen a lumped port.

- 2026-08-15: **IMPLEMENTED** - `hfss_spec/snapshot_to_spec.py`, CLI
  `scripts/spec_from_snapshot.py`. Reduction runs against all six real
  snapshots (five reference models plus the pilot's) in the Tier 0 suite.
  - **Ports are recomputed, never read from the stored section.** Every
    snapshot captured before the terminal-suffix rule stored terminals AS
    ports - the coplanar waveguide's `ports` section lists all six of
    `1, 1_T1, 1_T2, 2, 2_T1, 2_T2` for a two-port line. Raw `boundaries` are
    preserved on every snapshot, so the reducer recomputes with the same
    `split_ports` capture_state uses (imported, not copied - ticket 01's two
    profile parsers are why). Verified counts now match this ticket's own
    numbers exactly: coplanar 2, bandpass 2, probe-fed patch 1, horn 1,
    parabolic 1, pilot 1.
  - **`capture_state.py` extended** with `object_kinds` (solid / sheet / line
    / point), bumping the snapshot to **version 3**. Without it a bounding box
    cannot even distinguish a planar sheet from a solid, so *every* object
    reduced to `op: unknown`. With it, a `sheet` kind plus one degenerate axis
    yields a `sheet` op and a `solid` kind with no degenerate axis yields a
    `box`; everything else stays `unknown`. It still does not pin the outline -
    a bow-tie and a rectangle share a bounding box - and the reducer says so.
  - **Field-by-field report on the pilot snapshot** (`--report`), which is
    ticket 07's input: EXACT - 12 variables with expressions verbatim, 3
    materials, 1 port, 1 boundary name+type, setup name. APPROXIMATE - all 5
    geometry objects (`unknown`), boundary assignments (`on: UNRESOLVED`),
    sweep name only. MISSING - `model_units` (v1 snapshot), `object_kinds`,
    the port's face selector, and all setup properties (the `get_properties`
    defect). NOTES - `fr4_43` is user-defined so its properties are not in the
    snapshot, and one parametric variation string was correctly NOT read as a
    sweep.
  - **Re-entry path**: copy the project (ADR 0001) -> `capture_state` ->
    `scripts/spec_from_snapshot.py --workspace <dir>` -> the spec is the model
    card. Documented in the module docstring and the CLI's.
