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

- [ ] `design.yaml` for the pilot bowtie compiles onto a fresh desktop and captures a snapshot — **needs a license**; the spec exists and validates clean
- [~] Snapshot diff against the pilot's stored `model_snapshot.json` is empty after `canon()` normalization — the diff is built and regression-tested offline against the real pilot snapshot (identity, suffix normalisation, missing object, left-over intermediate, changed variable, bbox deltas); running it against a compiled model needs the desktop
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
