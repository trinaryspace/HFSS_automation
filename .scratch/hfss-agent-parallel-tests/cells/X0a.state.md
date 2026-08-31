# State ledger — patch-2400-inset

Three phase sessions bound by this file (ADR 0007): Clarification → Build
(through the Review gate incl. read-back sync) → Solve+QA. Each starts here,
not from the prior conversation. Keep ≤ ~2 KB: stage progress, locked
parameters, pitfalls, pointers. Machine state lives in `results/state/*.txt` —
never hand-edited; the staged scripts write it.

## Session 1 — Clarification (locked in the UI, never changed after)

- Started: 2026-08-16T21:13:08Z
- Recipe: inset-fed-rectangular-patch
- Locked: 2026-08-16T21:13:08Z — user confirmed recipe, assumptions and QA
  signals; all agent-recommended values adopted (inset_d 9.77mm, sub 60x60mm,
  gap 2mm, sweep 1.8-3.0GHz/401pts)
- Assumptions:
  - FR4_epoxy library material (er 4.4, tan d 0.02); real FR4 permittivity
    tolerance dominates resonance error — covered by the 5% target tolerance.
  - Patch + ground + feed as zero-thickness PEC sheets (cu_t 0.035mm
    documented but not modelled); consistent with microstrip-50r.
  - Inset depth y0 = 9.77 mm from the slot-conductance model
    (R_in(edge)=197 ohm; cos^2(pi y0/L)=50/R). Alternative relation gives
    10.82 mm; the inset is the match tuning variable, not the resonance.
  - Substrate/ground 60x60 mm (margin ~7h each side); airbox lambda0/4 top
    (31.2mm), ~lambda0/10 sides (15mm), feed wall flush at y=0.
  - Wave port at the board feed edge, full substrate width, ground to
    h+12mm (smoke-matrix validated sheet-port shape).
  - S11 read via the AEDT UI on this box; a scripted readout is a bonus,
    never a blocker (env-compat #6 flakiness).
- Approved Result QA signals: convergence, ports_excited, in_band_resonance
  (S11 min <= -10 dB within 2.28-2.52 GHz; precheck anchor 2.4000 GHz, tol 5%)

## Session 2 — Build

| Stage | Script | Verification line |
|-------|--------|-------------------|
| Route A: design.yaml + compile_spec | `design.yaml` | (pending) |

- Locked parameters / variables: see `design.yaml` (f0 2.4GHz, er 4.4,
  h 1.6mm, patch_W 38.0100mm, patch_L 29.4216mm, feed_W 3.0829mm,
  inset_d 9.77mm, gap 2mm, sub_W/sub_L 60mm, air_pad_top 31.2mm,
  air_pad_side 15mm, port_h 13.6mm)
- Pitfalls hit: tier0 fails 3 suites (skill-markers case.json presence,
  skill-install link path, design-spec real-patch/corpus tests) — every one
  from knowledge/cases/patch-2400/ being absent in this blind-cell worktree;
  environmental, not a spec defect. kb-checks ~210s, so tier0 needs a long
  timeout. My spec's own gates are green (validate_spec + precheck).

## Session 3 — Solve + QA

- Watchdog: `results/state/solve_progress.txt` (running | settling |
  complete | stalled — the agent reads only)
- QA signals: (pending)
- Run card: appended to `summary.md` by `scripts/run_card.py`

## Pointers

- Spec: `design.yaml` (offline gates green 2026-08-16: validate_spec
  errors=0 warnings=0; precheck verdict=consistent delta=-0.00% vs 2.4GHz)
- Model snapshot: `results/state/model_snapshot.json` (`capture_state.py`)
- Machine state: `results/state/*.txt` (`aedt_port`, `aedt_process_id`, …)
