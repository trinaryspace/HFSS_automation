# State ledger — patch-2400-2

Three phase sessions bound by this file (ADR 0007): Clarification → Build
(through the Review gate incl. read-back sync) → Solve+QA. Each starts here,
not from the prior conversation. Keep ≤ ~2 KB: stage progress, locked
parameters, pitfalls, pointers. Machine state lives in `results/state/*.txt` —
never hand-edited; the staged scripts write it.

## Session 1 — Clarification (locked, never changed after)

- Started: 2026-08-16T00:00:00Z
- Recipe: inset-fed rectangular microstrip patch (Modal), vetted case
  `knowledge/cases/patch-2400`; dimensions = `case.json` (source of truth),
  construction shape = `design.yaml` (validated 2026-08-15 build,
  S11 min 2.317 GHz @ -20 dB). Closed-form sourced: no paper dims gate.
- Assumptions (lock confirmed in-session; question tool dismissed — user
  brief already specified Recipe/variables/QA signals):
  1. Metal (patch, ground, feed) = PEC sheets; `cu_t` kept as a variable but
     not meshed as thickness (FR4 tan d dominates loss; resonance unaffected).
  2. Lumped port P1 on Substrate -y face (ground->patch edge vertical
     integration line), 50 ohm; radiation boundary on airbox outer faces;
     mesh adaptive-only.
  3. Setup1: 15 adaptive passes, delta-S 0.02 @ f0; discrete sweep 2.0-3.0 GHz,
     201 pts.
  4. Result readout locked up front (EC#6 flaky): S11 read in the AEDT UI on
     this box; scripted readout is a bonus, never a blocker.
  5. Workspace `workspaces/patch-2400-2/`, project `patch_2400.aedt`.
- Approved Result QA signals: convergence, ports excited, in-band resonance
  within +-5% of 2.4 GHz, energy pass.

## Locked parameters / variables (design variables, script edits only)

| Variable   | Value            | Meaning                      |
|------------|------------------|------------------------------|
| f0         | 2.4GHz           | target                       |
| er         | 4.4              | FR4_epoxy permittivity       |
| h          | 1.6mm            | substrate height             |
| cu_t       | 0.035mm          | copper thickness (unused by PEC sheets) |
| patch_W    | 38.0100mm        | Balanis 14-6                 |
| patch_L    | 29.4216mm        | Balanis 14-7 (fringing 14-2) |
| feed_W     | 3.06mm           | Hammerstad 50 ohm on stack   |
| inset_d    | 7.4mm            | inset depth (match tuner)    |
| inset_g    | 3.0mm            | inset gap width              |
| sub_W      | 80mm             | substrate width              |
| sub_L      | 80mm             | substrate length             |
| air_pad    | 31mm             | ~lambda0/4 at f0             |
| feed_run   | sub_L/2 - patch_L/2 | feed line reach             |

Solution type: Modal — explicit, never the default (EC#11).

## Session 2 — Build

| Stage | Script | Verification line |
|-------|--------|-------------------|
| Solution type + design | `01_solution_type_and_design.py` | PASS: solution_type Modal, design Patch2400, project saved (launch 62.6 s, port 58442) |
| Geometry | `02_geometry.py` | PASS: geometry 5 solids (Substrate Ground Patch AirBox PortSheet), Patch bbox 38.01x29.4216x0.035 at z=1.6, all dims variables |
| Materials | `03_materials.py` | PASS: materials Substrate=FR4_epoxy(er 4.4 tan-d 0.02), Patch=pec, Ground=pec, AirBox=air |
| Excitations / boundaries | `04_excitations.py` | PASS: excitations lumped port '1' (50 ohm, integration line vertical) on PortSheet face, radiation boundary Rad1 on AirBox |
| Mesh | `05_mesh.py` | PASS: mesh adaptive-only (0 mesh operations) |
| Setup + sweep | `06_setup_sweep.py` | PASS: setup Setup1 2.4GHz/15pass/dS0.02, sweeps ['last-adaptive', 'Sweep_TZ5L6X', ...] |
| Validation | `07_validate.py` | PASS: validation validate_simple() returns True |
| Review gate + sync verify | `capture_state.py` + `12_verify_sync.py` | PASS: sync replay matches snapshot (replay on port 54216, torn down) |

- Review gate: PASSED by user (no tweaks) 2026-08-16; sync verify PASS; snapshot
  pointer: `results/state/model_snapshot.json` (5 objects, 10 variables,
  boundaries 1/Rad1, Setup1 + Sweep)

- Pitfalls hit: (none yet; predecessor patch-2400 notes: sheet-port auto
  integration invalidates EC#8 — this Recipe uses solid-face lumped port)

## Session 3 — Solve + QA

- solve #1 — submitted via 08_solve (no stale results, no in-flight probe
  trigger); watchdog PID 36604; user: passed gate, "Looks good, solve"
- Live state: pin 58442 (probed this session: yes) · solve = running ·
  banked = no (solved.txt absent) · next: read solve_progress.txt to
  terminal line, then bank via confirm_solve
- Watchdog: `results/state/solve_progress.txt` (running | settling |
  complete | stalled — agent reads only)
- QA signals: reported in summary.md per locked list
- Run card: appended to `summary.md` by `scripts/run_card.py`

## Pointers

- Model snapshot: `results/state/model_snapshot.json` (`capture_state.py`;
  replayed + diffed by `12_verify_sync.py`)
- Machine state: `results/state/*.txt` (`aedt_port`, `aedt_process_id`,
  `solve_progress`, …)
- Predecessor run (reference, not to be mutated): `workspaces/patch-2400/`
