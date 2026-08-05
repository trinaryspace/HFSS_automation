# State ledger — <workspace name>

The conversation runs as three phase sessions bound by this file (ADR 0007):
Clarification → Build (through the Review gate incl. read-back sync) →
Solve+QA. Each session starts here, not from the prior conversation. Keep
this file at most ~2 KB: stage progress, locked parameters, pitfalls, and
pointers. Machine state lives in `results/state/*.txt` — never edit it by
hand; the staged scripts write it.

## Session 1 — Clarification (locked here, in the UI, never changed after)

- Recipe: <recipe name>
- Assumptions: <every assumption stated in the Clarification block>
- Approved Result QA signals: <convergence, ports excited, in-band resonance, …>

## Session 2 — Build

- Stage progress (one row per stage; each stage's script ends in its
  `PASS: <stage> <assertions>` Verification line):

  | Stage | Script | Verification line |
  |-------|--------|-------------------|
  | Solution type + design | `src/01_solution_type_and_design.py` | <paste PASS line> |
  | Geometry | `src/02_geometry.py` | <paste PASS line> |
  | Materials | `src/03_materials.py` | <paste PASS line> |
  | Excitations / boundaries | `src/04_excitations.py` | <paste PASS line> |
  | Mesh | `src/05_mesh.py` | <paste PASS line> |
  | Setup + sweep | `src/06_setup_sweep.py` | <paste PASS line> |
  | Validation | `src/07_validate.py` | <paste PASS line> |
  | Review gate + read-back sync | `src/capture_state.py` + `src/12_verify_sync.py` | <paste PASS line> |

- Locked parameters / variables: <name = value — script edits, never literals>
- Pitfalls hit: <one line each: what, why, which script it amends>

## Session 3 — Solve + QA

- Solve watchdog: `results/state/solve_progress.txt` (status: running |
  settling | complete | stalled; the agent reads only)
- QA signal values: <numbers per agreed signal, or "unreadable — flaky readout">
- Run card: appended to `summary.md` by the harness (`scripts/run_card.py`)

## Pointers

- Model snapshot: `results/state/model_snapshot.json` (written by
  `src/capture_state.py`; replayed + diffed by `src/12_verify_sync.py`)
- Machine state: `results/state/*.txt` (`aedt_port`, `aedt_process_id`,
  `solve_progress`, …)
