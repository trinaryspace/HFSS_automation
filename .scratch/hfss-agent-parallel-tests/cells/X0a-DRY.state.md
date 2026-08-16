# State ledger — patch-2400

Three phase sessions bound by this file (ADR 0007): Clarification → Build
(through the Review gate incl. read-back sync) → Solve+QA. Each starts here,
not from the prior conversation. Keep ≤ ~2 KB: stage progress, locked
parameters, pitfalls, pointers. Machine state lives in `results/state/*.txt` —
never hand-edited; the staged scripts write it.

## Session 1 — Clarification (locked in the UI, never changed after)

- Started: 2026-08-16T00:00:00Z
- Recipe: inset-fed-rectangular-patch (canonical case `knowledge/cases/patch-2400`)
- Assumptions: εr = 4.4 (FR4_epoxy library; user confirmed); inset depth sets
  match, not resonance (tuned, not synthesized); patch/ground PEC — S11-valid,
  not efficiency-valid; feed overhang 12 mm + slot gap 2 mm are convention;
  airbox pad λ₀/4 = 32 mm.
- Approved Result QA signals: convergence, ports_excited, in_band_resonance,
  energy_pass. Deliverable: S11 plot (UI readout authoritative; scripted is a bonus).
- Locked variables: f0 2.4 GHz, er 4.4, h 1.6 mm, cu_t 0.035 mm,
  patch_W 38.0100 mm (14-6), patch_L 29.4216 mm (14-7+14-2), feed_W 3.0829 mm
  (H-J, 50 Ω), inset_d 11.65 mm (cos² match), notch_g 2 mm,
  sub_W = patch_W+12h, sub_L = patch_L+6h+feed_run (12 mm), air_pad 32 mm.
  Sweep 1.9–3.0 GHz / 101 pts (user widened from 2.0).
- Offline gates (user approved them): validate_spec PASS errors=0 warnings=0;
  precheck verdict consistent (2.4000 GHz, −0.00%).
- Spec: `design.yaml` (Route A). Build session: gate offline, then
  `compile_spec.py --dry-run`, then `--launch`.

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

- Locked parameters / variables: see Session 1 — script edits, never literals.
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
