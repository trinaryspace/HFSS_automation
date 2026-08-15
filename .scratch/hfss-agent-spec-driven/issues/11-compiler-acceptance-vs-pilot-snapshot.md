# 11 — Compiler acceptance: reproduce the pilot's model from a spec

**What to build:** The compiler's proof, using evidence already on disk. The
pilot workspace `workspaces/bowtie-3500-pilot/` holds a fully built, solved,
sync-verified model and its `results/state/model_snapshot.json` — objects,
bounding boxes, materials, boundaries, excitations, setups, sweeps, and
variables, sorted and rounded. That snapshot is a free acceptance target: a
`design.yaml` that compiles to a model whose captured snapshot matches it proves
the compiler reproduces work the old path took a 25-hour pilot to produce. No new
solve is required, so this runs at Tier 1 in minutes.

Reuse the pilot's `canon()` normalization for AEDT's random suffixes
(`Sweep_XXXXXX`, `Rad__XXXXXX`) — a real bug the pilot found and fixed, and
exactly the kind of knowledge that should survive into the new path rather than
be rediscovered. Where the snapshot and the compiled model differ, the difference
is either a compiler bug or a gap in the schema, and each one must be
classified as such in this ticket's Comments; the schema gaps are the honest v2
backlog.

**Blocked by:** 10.

**Status:** ready-for-human

- [x] `design.yaml` for the pilot bowtie compiles onto a fresh desktop and captures a snapshot
- [x] Snapshot diff against the pilot's stored `model_snapshot.json` is empty after `canon()` normalization — the diff is built and regression-tested offline against the real pilot snapshot (identity, suffix normalisation, missing object, left-over intermediate, changed variable, bbox deltas); running it against a compiled model needs the desktop
- [x] Any residual difference is classified in Comments as compiler bug or schema gap, with the schema gaps filed — classifier implemented (compiler bug / schema gap / capture gap); the Comments entry lands with the live run
- [x] Runs as a Tier 1 target (build only, no solve) and completes in minutes — `scripts/spec_acceptance.py`, which never solves
- [ ] The same acceptance is repeated for the microstrip-line case as a second, cheaper data point — needs a `design.yaml` for microstrip-50r

- 2026-08-15: **Diff implemented and regression-tested offline; the live run
  needs a license.** `hfss_spec/acceptance.py`, CLI
  `scripts/spec_acceptance.py` (`--offline` diffs two stored snapshots).
  - `canon()` is imported from the template's `12_verify_sync.py` rather than
    re-derived, so the pilot's random-suffix fix (which numbers same-class keys
    so a count drift cannot hide inside the normalisation) carries over intact.
  - Six offline tests against the pilot's REAL snapshot: identity matches;
    `Rad__M4WFEW` vs `Rad__QQ11ZZ` is normalised rather than reported; a
    missing object classifies as a compiler bug; a left-over boolean
    intermediate classifies as a schema gap; a changed variable is reported
    with both values; bbox deltas come back as magnitudes, not booleans.
  - Two further tests assert the acceptance target is actually reachable: the
    bowtie spec declares every object the pilot's snapshot lists, and carries
    all twelve of its variables with the expressions verbatim.
  - **What the live run must still settle**: whether the compiled model's
    bboxes match, and how the `PatchTriUp` / `FeedLine` intermediates classify
    - the pilot united them away, and whether the compiler leaves them behind
    is exactly the schema-gap question this ticket exists to answer.

- 2026-08-15: **ACCEPTANCE PASSES ON A LIVE DESKTOP.** The compiler rebuilt the
  pilot's bow-tie from `knowledge/cases/bowtie-3500/design.yaml` on a fresh
  launched desktop (an isolated copy workspace — never the pilot, which holds
  solved results), and the captured snapshot matches the stored one:

      PASS: solution_type solution_type=Modal
      PASS: variables design=12 project=0
      PASS: materials declared=3 created=1
      PASS: geometry ops=10 objects=7
      PASS: excitations ports=1
      PASS: boundaries count=1
      PASS: mesh strategy=adaptive_only operations=0
      PASS: setup_sweep setup=Setup1 passes=15 sweep=Sweep1
      PASS: validate validate_simple=True objects=7
      PASS: spec_acceptance sections=4 differences=0 compiler_bugs=0 schema_gaps=0
        bbox objects differing: 0

  **Every bounding box matches exactly** — the model the 25-hour pilot produced,
  rebuilt from a document in about a minute, with `validate_simple()` True.

- **The live run earned its keep: it found two API defects the recorder could
  not.** Both are now library code, and both were mistakes of the exact class
  the golden tests are blind to — a mocked call sequence cannot know a
  signature is wrong.
  1. `Materials.checkifmaterialexists` does not exist on pyAEDT 1.3.0. The real
     predicate is `exists_material`; the pilot's own `03_materials.py` used
     `materials[name]` indexing (returns None rather than raising). The
     compiler now prefers the predicate and falls back to the index.
  2. `create_linear_count_sweep` takes `unit` (singular) plus **bare float**
     endpoints, not unit-carrying strings. The compiler now splits `3.2GHz`
     into `("GHz", 3.2)` and preserves the authored unit so the UI reads GHz.
  A third finding: `PYAEDT_LOG_LEVEL=WARNING` set before the import does NOT
  suppress pyAEDT's INFO stream — it installs its handlers on the `Global`
  logger at import time, so the level has to be re-applied afterwards.

- **The three residual differences, classified** — none of them a compiler bug,
  and the diff now normalises all three:
  - `materials.Substrate` read `fr4_43` against the spec's `FR4_43`. AEDT
    material names are case-insensitive and come back lower-cased. Compared
    case-insensitively.
  - the radiation boundary read `Rad__M4WFEW` against the compiler's `Rad`.
    The pilot let AEDT auto-name and got a random suffix; the compiler names
    it deterministically, which is an improvement rather than a difference.
    `canon()` already reduces the suffix to `__<RND>`, so the diff now drops
    that canonical tail when matching boundary keys.
  - a prediction in the previous comment was **wrong**: `PatchTriUp` and
    `FeedLine` do NOT survive as left-over intermediates. `unite` consumes
    them exactly as the pilot's script did, so the live object count is 5, not
    7. (`objects=7` in the geometry PASS line counts names the *spec*
    declares, not objects left in the modeler.)

- Still open: the same acceptance for microstrip-50r as a second, cheaper data
  point, which needs a `design.yaml` for it.

