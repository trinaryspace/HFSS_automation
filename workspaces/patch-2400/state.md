# State ledger — patch-2400

Three phase sessions bound by this file (ADR 0007): Clarification → Build
(through the Review gate incl. read-back sync) → Solve+QA. Each starts here,
not from the prior conversation. Keep ≤ ~2 KB: stage progress, locked
parameters, pitfalls, pointers. Machine state lives in `results/state/*.txt` —
never hand-edited; the staged scripts write it.

## Session 1 — Clarification (locked in the UI, never changed after)

- Started: 2026-08-14T21:00:00Z (written once, never changed)
- Recipe: inset-fed rectangular microstrip patch (case-backed: `knowledge/cases/patch-2400/case.json` — canonical; closed-form Balanis 14-1/14-2/14-6/14-7; NOT paper-sourced, no dimension gate)
- Assumptions: FR4_epoxy stock library (er 4.4, tan-d 0.02 — matches case; verified stage 03); PEC copper; ground = substrate footprint 80x80; patch centered, feed on centerline x=0 along -Y from substrate edge to inset island (united, 0.001mm overlap); lumped port on substrate -Y face between ground-top and trace-bottom (XZ rect, integration line vertical, 50 ohm); airbox gap 31mm (~lambda0/4) + radiation; adaptive-only mesh; Setup1 2.4GHz/15pass/dS0.02 + discrete sweep 2.0-3.0GHz/201pts; results path: S11 read via AEDT UI on this box, scripted readout a bonus.
- User confirmation (verbatim): "Confirm as proposed (Recommended)".
- Approved Result QA signals: (1) convergence dS<=0.02; (2) ports excited (lumped port + radiation, S11 populated); (3) in-band resonance S11 min inside 2.28-2.52 GHz (5% of 2.4; depth target <= -10 dB); (4) energy pass (single-port passive, S11<=0 dB, profile Normal Completion).

## Session 2 — Build

One stage = one script = one Run, each ending in its `PASS:` Verification line:

| Stage | Script | Verification line |
|-------|--------|-------------------|
| Solution type + design | `01_solution_type_and_design.py` | PASS: solution_type Modal, design Patch2400, project saved (launch 24.0 s, port 59131) |
| Geometry | `02_geometry.py` | PASS: geometry 5 solids (Substrate Ground Patch AirBox PortSheet), Patch bbox 38.01x29.4216x0.035 at z=1.6, all dims variables |
| Materials | `03_materials.py` | PASS: materials Substrate=FR4_epoxy(er 4.4 tan-d 0.02), Patch=pec, Ground=pec, AirBox=air |
| Excitations / boundaries | `04_excitations.py` | PASS: excitations lumped port '1' (50 ohm, integration line vertical) on PortSheet, radiation Rad1 on AirBox |
| Mesh | `05_mesh.py` | PASS: mesh adaptive-only (0 mesh operations) |
| Setup + sweep | `06_setup_sweep.py` | PASS: setup Setup1 2.4GHz/15pass/dS0.02, sweeps [Setup1 : LastAdaptive, Setup1 : Sweep_2R59H1, ...] |
| Validation | `07_validate.py` | PASS: validation validate_simple() returns True |
| Review gate + sync verify | `capture_state.py` + `12_verify_sync.py` | gate: user PASS, no tweaks ("yeah i think this looks good"); sync verify: PASS: sync replay matches snapshot (run 20260814_213905, copy port 61007, teardown port-pinned) |

- Locked parameters / variables: PatchW=38.01mm, PatchL=29.4216mm, SubW=80mm,
  SubL=80mm, SubH=1.6mm, CuT=0.035mm, FeedW=3.06mm (50-ohm Hammerstad),
  InsetDepth=7.4mm (match tuner), InsetGap=3.0mm, AirGap=31mm (script edits,
  never literals).
- Pitfalls hit:
  - stage 02 run1 FAIL: patch-y-span assertion expected the patch alone but the
    united Patch includes the 40-mm trace — assertion amended to the union bbox
    (x +-19.005, y -40..+14.7108, z 1.6..1.635); no model change needed.
  - create_rectangle("XZ", ...) on this pairing maps sizes to [z, x], not
    [x, z] — first PortSheet was transposed (x-span 1.6, z-span 3.06); 02
    amended to sizes=[SubH, FeedW], sheets now x +-1.53, z 0..1.6.
  - pyAEDT 1.3.0 lumped_port defect: a FacePrimitive id is stringified into
    props["Objects"] and the macro layer rejects it ("a geometry selection is
    required for assignment") — unlike wave_port, which resolves face ids to
    object names. Working shape: pass the SHEET NAME + explicit 2-point
    integration line (04 amended). Learning-loop candidate.

## Session 3 — Solve + QA

- Watchdog: `results/state/solve_progress.txt` (running | settling |
  complete | stalled — the agent reads only); banked:
  `results/state/solved.txt` status=Normal Completion sweep_points=200
  banked_at=1786758729.
- Solve decisions (resolve-once, ADR 0007 practice):
  - solve #1 — submitted on the verified state (gate PASS, sync verify PASS).
    The 08 in-flight probe WARNED (results_age 107s, 2 live ansysedt) BUT the
    evidence shows a false positive: results-dir holds only build-time .asol
    skeletons (no .sd sweep files; cleanup's own classifier calls them
    "not solve results"), and both live processes are accounted for (user's
    pre-existing desktop 25460 + our pinned 36572). No prior solve, no other
    solve target. Watchdog pid 36936. Learning-loop candidate: probe should
    reuse the cleanup .asol-size/.sd criterion.
  - solve #1 ANOMALY + resolution: watchdog pid 36936 died at tick 8 (~161 s,
    stage=frequency_sweep, fsu=109) without a terminal verdict — process gone;
    on-disk solve evidence is complete: 200 *_SU.txt + profile
    DV85_S82_V100.profile Status "Normal Completion", Stop 08/14/2026 21:44:52
    (Initial 1 s, Adaptive 17 s 6p, Sweep 4m06s). Escalated to user; answer
    verbatim: "Bank and continue (Recommended)". No re-submission.
    Learning-loop candidate: watchdog death class — no terminal line, no crash
    trace; bank path unaffected.
- Live state: pin=59131 (probed this session); solve status=complete by
  profile evidence (watchdog line absent — died tick 8); solved marker=none;
  next action=bank via confirm_solve, then plots/QA/UI read.
- QA signals (read route: AEDT UI — scripted get_solution_data failed with
  GrpcApiError GetVariables, EC#6, one attempt + no retry shapes; material
  er=4.4/0.02 verified from the design after the cold-index skip):
  (1) convergence: solve Normal Completion, 6 adaptive passes, dS<=0.02
      target (final dS in the UI Convergence dialog); PASS.
  (2) port excited: lumped port '1' + Rad1 present; S11 populated, 200-pt
      curve read in UI. PASS.
  (3) in-band resonance: min 2.317 GHz / -20 dB in [2.28, 2.52] — PASS;
      -10 dB BW 2.295-2.340 GHz (1.9%, typical thin-FR4 patch).
  (4) energy pass: single-port passive, profile Normal Completion, deep
      matched dip. PASS.
  Anomaly note: first UI readout said 3.317 GHz — outside the swept band
  (2.0-3.0); user corrected to 2.317 (typo). Also: FR4_epoxy absent from the
  cold material index (materials stage skipped its er assertion — fixed in
  QA via design-side read).
- Run card: appended to `summary.md` by `scripts/run_card.py`

## Pointers

- Model snapshot: `results/state/model_snapshot.json` (`capture_state.py`;
  replayed + diffed by `12_verify_sync.py`)
- Machine state: `results/state/*.txt` (`aedt_port`, `aedt_process_id`,
  `solve_progress`, ...)
