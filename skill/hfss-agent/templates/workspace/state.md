# State ledger — <workspace name>

Three phase sessions bound by this file (ADR 0007): Clarification → Build
(through the Review gate incl. read-back sync) → Solve+QA. Each starts here,
not from the prior conversation. Keep ≤ ~2 KB: stage progress, locked
parameters, pitfalls, pointers. Machine state lives in `results/state/*.txt` —
never hand-edited; the staged scripts write it.

## Session 1 — Clarification (locked in the UI, never changed after)

- Started: <UTC ISO-8601 session start, e.g. 2026-08-05T14:00:00Z — written once, never changed>
- Recipe: <name>
- Assumptions: <each assumption from the Clarification block>
- Approved Result QA signals: <convergence, ports, in-band resonance, …>

## Session 2 — Build

One stage = one script = one Run, each ending in its `PASS:` Verification line:

| Stage | Script | Verification line |
|-------|--------|-------------------|
| Solution type + design | `01_solution_type_and_design.py` | <paste PASS line> |
| Geometry | `02_geometry.py` | <paste PASS line> |
| Materials | `03_materials.py` | <paste PASS line> |
| Excitations / boundaries | `04_excitations.py` | <paste PASS line> |
| Mesh | `05_mesh.py` | <paste PASS line> |
| Setup + sweep | `06_setup_sweep.py` | <paste PASS line> |
| Validation | `07_validate.py` | <paste PASS line> |
| Review gate + sync verify | `capture_state.py` + `12_verify_sync.py` | <paste PASS line> |

- Locked parameters / variables: <name = value — script edits, never literals>
- Pitfalls hit: <one line each: what, why, which script it amends>

## Session 3 — Solve + QA

- Watchdog: `results/state/solve_progress.txt` (running | settling |
  complete | stalled — the agent reads only)
- QA signals: <numbers per agreed signal, or "unreadable — flaky readout">
- Run card: appended to `summary.md` by `scripts/run_card.py`

## Pointers

- Model snapshot: `results/state/model_snapshot.json` (`capture_state.py`;
  replayed + diffed by `12_verify_sync.py`)
- Machine state: `results/state/*.txt` (`aedt_port`, `aedt_process_id`,
  `solve_progress`, …)
