# The Design Spec build route

The Build session has two routes to the same Spine. This one writes **one
`design.yaml`** and lets a tested compiler walk the stages, instead of writing
ten staged scripts per run.

Use it when the structure is expressible in schema v1 — which is every
canonical case in `knowledge/cases/`, the horn included. Fall back to staged
scripts when it is not, and say so in the ledger: the escape-hatch rate is a
tracked metric, and a schema that is wrong should show up as a number rather
than as quiet improvisation.

**What does not change.** Phase sessions and the State ledger (ADR 0007), the
visual Review gate (ADR 0003), the detached watchdog and bank-before-teardown
(ADR 0006), copy-first Re-entry (ADR 0001), the Verification-line contract, and
the Learning loop (ADR 0002). Solve submission stays imperative. The Spine's
stages and their completion criteria are identical — only who writes the code
that walks them changes.

## The route, end to end

Everything before `compile_spec` is **offline**: no desktop, no license, and it
runs in about a second. That is the point — the errors it catches used to cost
a desktop launch, a failed stage, a traceback read, and a self-correction round.

```
# 0. pre-flight, before any AEDT launch
python scripts/tier0.py                       # PASS: tier0 suites=10 failed=0

# 1. write workspaces/<name>/design.yaml       (Clarification's output)

# 2. offline gates — repeat until both pass
python scripts/validate_spec.py workspaces/<name>/design.yaml
python scripts/precheck.py     workspaces/<name>/design.yaml

# 3. see the plan without touching a desktop
python scripts/compile_spec.py --workspace workspaces/<name> \
       --spec workspaces/<name>/design.yaml --dry-run

# 4. build on the live desktop (never solves)
python scripts/compile_spec.py --workspace workspaces/<name> \
       --spec workspaces/<name>/design.yaml --launch

# 5. capture the as-built model
cd workspaces/<name> && python src/capture_state.py
```

Then the Review gate, then Solve + QA exactly as `SKILL.md` describes.

## Writing the spec

Start from a canonical case if one fits — `knowledge/cases/*/design.yaml` are
four worked examples, and `patch-2400` describes a model that has been built
and solved on this box. Otherwise:

- **Every dimensional value carries a unit** (`52.64mm`, `2.4GHz`, `50ohm`) or
  is an expression over declared variables (`patch_W + 6*h`). A bare number is
  legal only where the quantity is genuinely dimensionless (`er: 4.4`).
- **Expressions pass through to AEDT verbatim**, so the parametric link stays
  live in the variable table. Confirmed on the desktop: a compiled microstrip
  reads back `sub_W: 'trace_W + 12*h'`, not an evaluated number.
- **Faces are symbolic, never ids** — `{face_of: Feed, direction: "-y"}`. An
  ambiguous selector is an ERROR; add `pick: largest_area` or
  `nearest: [x, y, z]` to opt in. Silently choosing the wrong face builds a
  model that simulates nonsense, which is the worst failure this tool has.
- **`on:` must be quoted in YAML** — bare `on` is boolean `true` in YAML 1.1.
  The loader maps it back, but quoting it is clearer.
- Metal can be a `material: pec` on a sheet **or** a `perfect_e` boundary. Both
  are legal and real models use both; pick one per object and be consistent.

## Reading a validator finding

Every finding carries a path and a severity:

```
FAIL: validate_spec errors=1 warnings=0

  errors:
  geometry[3].size[2]        size[2] must be length, got time^-1
                             value read as 'f0'
```

Fix the spec, re-run. Do **not** launch a desktop against a spec with errors —
`compile_spec` refuses anyway, because `require_valid()` is a hard gate at the
top of the compiler.

## Reading a pre-check verdict

The pre-check predicts the design's target from closed-form relations and
compares. It **never blocks and never overrides you**:

```
      target                 3.5000 GHz
      closed-form            3.8782 GHz      delta: +10.81%   tolerance: 8%

FAIL: precheck recipe=bow-tie-patch verdict=INCONSISTENT — arbitrate before building
```

An `INCONSISTENT` verdict goes to the **user** with both numbers, in the
Clarification block, before anything builds. The user decides which reading is
canonical and the choice is recorded in `provenance.canonical_reading`. This is
the Astuti gate: that disagreement survived four solves and about twenty hours
on the pilot, and it is visible here in microseconds.

## Read-back sync, without the replay ceremony

The old route copied the workspace, launched a port-pinned second desktop, and
replayed eight staged scripts — roughly eight minutes a round. Under this route
the Review gate's tweaks are a snapshot diff:

```
# right after compiling, before the user touches anything
cd workspaces/<name> && python src/capture_state.py
cp results/state/model_snapshot.json results/state/as_built.json

# ... user inspects and tweaks in the AEDT UI ...

cd workspaces/<name> && python src/capture_state.py
cd ../.. && python scripts/spec_acceptance.py \
    --reference workspaces/<name>/results/state/as_built.json \
    --offline   workspaces/<name>/results/state/model_snapshot.json
```

Differences are the user's tweaks, each classified. Fold the representable ones
back into `design.yaml`. Anything the spec **cannot** express gets a
loud ledger entry naming exactly what could not be tracked — the spec is then
knowingly stale rather than quietly wrong, which is the whole of Q5.

## What the schema does not cover in v1

Explicit mesh operations (adaptive-only, Q4), and geometry received rather than
designed — for that use `op: import_cad`, accepting that imported bodies carry
no construction history and cannot be parameterized. Anything else the schema
cannot express takes `op: escape_hatch` with a `reason:` and a `script:`, which
the caller runs. Count them; the escape-hatch rate is how we learn the schema
is wrong.

## Known sharp edges, all measured on this box

- `lumped_port` must be given a sheet **name** plus an explicit integration
  line. Passing a `FacePrimitive` serialises the face id into
  `props["Objects"]` and the macro layer rejects it. The compiler already does
  the right thing; this matters if you drop to a staged script.
- `create_rectangle("XZ")` maps sizes to `[z, x]`. The spec always states sizes
  in axis order and the compiler swaps once, so do not pre-swap.
- `Hfss.delete_boundary` does not exist on pyAEDT 1.3.0 — use
  `BoundaryObject.delete()`.
- `Materials.checkifmaterialexists` does not exist either; it is
  `exists_material`, and `materials[name]` returns None rather than raising.
- `PYAEDT_LOG_LEVEL=WARNING` set before the import does **not** silence pyAEDT.
  It installs handlers on the `Global` logger at import time, so the level has
  to be re-applied afterwards.
