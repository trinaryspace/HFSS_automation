# State ledger — patch-2400

Three phase sessions bound by this file (ADR 0007): Clarification → Build
(through the Review gate incl. read-back sync) → Solve+QA. Each starts here,
not from the prior conversation. Machine state lives in `results/state/*.txt` —
never hand-edited; the staged scripts write it.

## Session 1 — Clarification (locked in the UI, never changed after)

- Started: 2026-08-16T21:25:00Z
- Recipe: `inset-fed-rectangular-patch` (reference canonical case `patch-2400`)
- Assumptions (all confirmed by the user, 2026-08-16):
  - FR4 εr = 4.4 (AEDT `FR4_epoxy` library value), tan δ 0.02; FR4's own
    permittivity tolerance dominates error, so the 5% band is honest.
  - Standard ground plane at z=0; patch on top of the substrate; no SMA or
    connector modeled — the lumped port sits at the substrate edge face.
  - Resonance judged by the S11 dip in the 2.0–3.0 GHz sweep; "within 5%"
    means the dip lands in 2.28–2.52 GHz.
- Approved Result QA signals: convergence (ΔS 0.02), port excited, S11 dip in
  band, dip depth < −10 dB (schema: convergence, ports_excited,
  in_band_resonance, energy_pass).
- Locked parameters / variables (derived closed-form, cross-checked against
  hfss_spec/physics worked examples; the reference case file is absent in this
  clean-room cell by design, so these were derived, not transcribed):
  - f0 2.4GHz, er 4.4, h 1.6mm
  - patch_W 38.0100mm (Balanis 14-6), patch_L 29.4216mm (14-7, ereff 4.0857,
    dL 0.7388mm) — precheck predicted resonance 2.4000 GHz, delta +0.00%
  - feed_W 3.0829mm (Hammerstad → Z0 50.00 ohm), inset_d 9.0mm,
    inset_g 1.0mm (cos²(π·d/L) ≈ 0.33, the 50-ohm tap)
  - sub_W/sub_L 80mm (reference snapshot values), air_pad 0.25·c0/f0
  - Setup1: 15 passes, ΔS 0.02, discrete sweep 2.0–3.0 GHz, 201 pts
    (values pinned by the golden tests in hfss_spec/test_hfss_spec.py)
- Offline gates: validate_spec PASS, precheck verdict=consistent
  (PASS: precheck recipe=inset-fed-rectangular-patch verdict=consistent)

## Session 2 — Build

Route A — Design Spec (`design.yaml`) via the tested compiler. One stage per
Spine step, each ending in its `PASS:` Verification line:

| Stage | Script | Verification line |
|-------|--------|-------------------|
| (all stages) | `scripts/compile_spec.py --launch` | <paste PASS line> |
| Solution type + design | (compiler, explicit Modal — env-compat #11) | |
| Geometry | (compiler, delete-then-create, ADR 0008) | |
| Materials | (compiler; FR4_epoxy, pec, air) | |
| Excitations / boundaries | (compiler; lumped port P1 on Substrate face + Rad) | |
| Mesh | (compiler; adaptive-only, Q4) | |
| Setup + sweep | (compiler; Setup1 + Sweep1) | |
| Validation | (compiler; `validate_simple()` hard gate) | |
| Review gate + sync verify | `capture_state.py` + `spec_acceptance.py` | <paste PASS line> |

- Locked parameters / variables: as Session 1; every dimension is a design
  variable, user tweaks are variable edits (script edits, never literals).
- Pitfalls hit: none yet.

## Session 3 — Solve + QA

- Watchdog: `results/state/solve_progress.txt` (running | settling |
  complete | stalled — the agent reads only)
- QA signals: <numbers per agreed signal, or "unreadable — flaky readout">
- Run card: appended to `summary.md` by `scripts/run_card.py`

## Pointers

- Model snapshot: `results/state/model_snapshot.json` (`capture_state.py`;
  replayed + diffed by sync verify)
- Machine state: `results/state/*.txt` (`aedt_port`, `aedt_process_id`,
  `solve_progress`, …)
- Predecessor: `patch-2400` is the reference inset-fed patch recipe; the
  golden tests in `hfss_spec/test_hfss_spec.py` assert its call sequence,
  port shape and sweep — the structural record used here.
