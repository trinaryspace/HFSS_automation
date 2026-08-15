# 02 — Watchdog stage families must count directories (P0, live bug)

**What to build:** `poll_solve.scan_results()` applies the `mesh` / `adp` / `fsu`
family regexes only inside the `filenames` loop, but on this box `.imesh`,
`.cmesh`, and `_ADP*` artifacts are **directories** — verified across all four
workspaces (`bowtie-3500`, `bowtie-3500-pilot`, `bowtie-3670`,
`readout-route-around`): zero files, N directories, every time. Measured against
the real solved trees the counters read `mesh=(0,0) adp=(0,0)` even though all
three runs completed initial meshing and six adaptive passes. The consequence is
worse than a wrong counter: ticket 14's own evidence establishes that the
`.profile` is written **at the end of the solve, not per stage**, so
artifact-family growth is the *only* live stage signal — which means the
watchdog is blind to stage for the entire meshing and adaptive phase and only
wakes up when `_F####_SU.txt` sweep files appear. "A mesh stuck forever and a
running sweep never look alike" is the promise of ticket 14; it does not
currently hold. Apply the family regexes to `dirnames` as well as `filenames`,
counting a directory once (size 0 or recursive size — pick one and document it),
and add per-stage stall windows so a slow initial mesh is not scored against the
same 30-tick budget as a sweep plateau.

**Blocked by:** None — can start immediately. Pairs naturally with 01 and 03.

**Status:** ready-for-human

- [x] `scan_results()` counts directory-form `.imesh` / `.cmesh` / `_ADP*` artifacts; measured against all four real trees, `mesh` and `adp` are non-zero
- [x] `stage_floor()` reaches rank 1 from adaptive artifacts alone, with no profile present (the live mid-solve condition)
- [x] Per-stage stall windows, defaulted per stage and documented; a stall names the stage it is actually in
- [x] Tests driven from `fixtures/real/` (ticket 03) reproduce the directory shape; the existing `test_families_match_pilot_artifact_names` is rewritten to create directories where AEDT creates directories
- [ ] Ticket 15's live watchdog stage-agreement check re-run or re-scoped against the fix

## Comments

- 2026-08-14: **DONE** (except the live re-check, which needs a solve).
  `scan_results()` now applies the mesh/adp/fsu patterns to `dirnames` as
  well as `filenames`. Directories count once and contribute no bytes of
  their own; growth inside them still lands in the `files` / `bytes_total`
  counters, so stall detection is unaffected.
- **Measured on the real trees.** Before: `mesh=(0,0) adp=(0,0)` on all
  three solved workspaces. After: `bowtie-3500` `mesh=(2,0) adp=(1,0)`,
  `bowtie-3500-pilot` `mesh=(8,0) adp=(4,0)`, `bowtie-3670`
  `mesh=(2,0) adp=(1,0)` — every one of which completed initial meshing and
  six adaptive passes, so zero was wrong by inspection.
- **Why this mattered more than a wrong counter.** Ticket 14's own evidence
  records that the `.profile` is written at the END of a solve, not per
  stage. Artifact growth is therefore the ONLY live stage signal, so with
  both mesh families reading zero the watchdog could not distinguish
  meshing from adaptive at all — it reported `initial_meshing` until sweep
  files appeared. `test_stage_floor_reaches_adaptive_without_a_profile`
  pins the fixed behaviour at exactly that condition (no profile present).
- **Per-stage stall windows** added (`STALL_TICKS_BY_STAGE`): initial
  meshing 60 ticks (~20 min), adaptive 45, sweep 30, finalizing 9. A
  blanket `stall_ticks` in `cfg` still overrides, which is how the tests
  drive short windows. `START_TICKS` raised 30 -> 45 for the same reason:
  meshing can legitimately write nothing for a long time, and the pilot's
  false stall came from one window applied to every stage.
- Open: the acceptance item for re-running ticket 15's live stage-agreement
  check is left unchecked — it needs a real solve on the live desktop.
