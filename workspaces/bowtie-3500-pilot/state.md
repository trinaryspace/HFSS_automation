# State ledger — bowtie-3500-pilot

Three phase sessions bound by this file (ADR 0007): Clarification → Build
(through the Review gate incl. read-back sync) → Solve+QA. Each starts here,
not from the prior conversation. Keep ≤ ~2 KB: stage progress, locked
parameters, pitfalls, pointers. Machine state lives in `results/state/*.txt`
— never hand-edited; the staged scripts write it.

## Session 1 — Clarification (locked in the UI, never changed after)

- Recipe: bowtie-5g-baseline (derived; paper-exact plain bowtie from Astuti
  et al. 2022 Table I; NO DGS; driven Modal; single waveport; ~3.5 GHz).
- Assumptions: FR-4 er 4.3, tan-d 0.02; Cu t 0.1; PEC ground; feed stub
  Wz 3.1118 x Lz 45 mm to the +X edge; airbox gap 25 mm (>= lambda/4);
  waveport 3*FeedW square on external boundary (Ports.pdf), 50 ohm
  renormalized, assigned by face object (EC#7); port plane flush at
  x = SubW/2; adaptive-only mesh.
- User note (verbatim): "One of the main issues was the feed location.
  Pay extra attention to that and I think we'll be good with the confirmed
  recipe." -> feedstock: petals MUST overlap the feed-stub footprint at the
  waist (point-contact fails to unite); feed runs from waist (0,0) along
  +X to x=+SubW/2 exactly.
- Approved Result QA signals: (1) convergence dS<=0.02; (2) port excited,
  S11 populated; (3) in-band resonance S11 min <= -10 dB in 3.4-3.6 GHz;
  (4) VSWR<=2 span >= 2.6% of center; (5) single-port plausibility.

## Session 2 — Build

One stage = one script = one Run, each ending in its `PASS:` Verification line:

| Stage | Script | Verification line |
|-------|--------|-------------------|
| Solution type + design | `01_solution_type_and_design.py` | PASS: solution_type Modal design Bowtie3500 project saved (launch 54.3 s, port 50847) |
| Geometry | `02_geometry.py` | PASS: geometry 4 solids, feed xmax==+SubW/2, airbox flush, petal span y in [-PatchL,+PatchL], z in [SubH,SubH+CuT] |
| Materials | `03_materials.py` | PASS: materials AirBox=air, Ground=pec, PatchBowtie=pec, Substrate=FR4_43, FR4_43 er=4.3 tand=0.02 |
| Excitations / boundaries | `04_excitations.py` | PASS: excitations waveport on PortSheet face, boundaries 1, Rad__R2CD63 (port + radiation) |
| Mesh | `05_mesh.py` | PASS: mesh adaptive-only (0 mesh operations) |
| Setup + sweep | `06_setup_sweep.py` | PASS: setup Setup1 3.5GHz/15pass/dS0.02, sweeps Setup1 : LastAdaptive, Setup1 : Sweep_0LJAL0, ... |
| Validation | `07_validate.py` | PASS: validation validate_simple() returns True |
| Review gate + sync verify | `capture_state.py` + `12_verify_sync.py` | gate 1: user PASS no tweaks (2026-08-05); gate 2 after pilot-QA geometry correction (base=L, leg=W per user Fig-1 reading): PASS, sync replay matches snapshot (verify run6, exit 0); run4 exposed orphaned variables (PatchL/PatchW) fixed by variable delete-then-create; run5 hit a flaky gRPC timeout in copy stage 06 (900 s runner guard caught it) |

- Locked parameters / variables (CORRECTED 2026-08-05 per user's Fig-1
  reading: triangle base = paper L, legs toward feed = paper W):
  PatchBase=20.2168mm, PatchLeg=26.3269mm, PatchH=24.3094mm (derived),
  SubW=90mm, SubL=80mm, SubH=1.6mm, CuT=0.1mm, FeedW=3.1118mm,
  FeedL=45mm, AirGap=25mm, PortW=3*FeedW, PortH=3*FeedW (script edits,
  never literals).
- Pitfalls hit:
  - material_keys is a cold index on fresh attach (4 entries; FR4_43 absent);
    materials["name"] getitem returns None (no raise) when absent — 02/03 use
    index-then-add (1 failed run).
  - hfss.variables is None on fresh attach — capture_state falls back to
    variable_manager.variables (Variable objects -> .expression); TM fix
    synced to template.
  - hfss.excitations is flaky over gRPC (hung a probe once; empty in
    capture_state) — waveport read via boundaries ("1"/"Wave Port").
  - verify-runner bugs found + fixed mid-pilot (template synced): (a)
    random AEDT auto-suffixes (Sweep_XXXXXX, Rad__XXXXXX) broke the diff —
    canon() normalizes them; (b) make_copy put scripts at copy root, so
    ws_common's WORKSPACE resolved one level up — scripts now copy into
    copy/src/; (c) third concurrent ansysedt.exe (a leftover scratch-copy
    desktop) stalled the next launch — orphan copy desktops must be killed
    before a rerun (license seats).
  - feed-location discipline held: PatchBowtie xmax == 45.0 mm exactly.

## Session 3 — Solve + QA

- Watchdog: `results/state/solve_progress.txt` (running | settling |
  complete | stalled — the agent reads only). solve_started 1785991595;
  watchdog pid 52116 EXPECTED_SD=201; stage-08 fixes mid-pilot (cleanup
  no-op handling; Start-Process argument shape). poll_solve fixed to
  count .sd FILES too (template synced).
- QA signals (user terminated the pilot at the corrected-geometry read;
  read route = AEDT UI, scripted readout down per EC#6 + pyAEDT 1.3.0
  client bug):
  (1) convergence dS<=0.02: NOT met — dS 0.074 after 6 passes; adaptive
      stopped at the pass limit (MaximumPasses stayed 6: props["MaxPasses"]
      does not map to the internal key) — reported as an anomaly.
  (2) port excited: yes (waveport "1" + radiation); S11 readout
      "unreadable — flaky readout" (GrpcApiError GetVariables/GetSetups).
  (3) in-band resonance: uncorrected build UI-read at 3.85 GHz / -4 dB
      (surfaced the base/leg fix); corrected build solved clean, read not
      completed before termination.
  (4) bandwidth: unreadable — flaky readout.
  (5) plausibility: single-port passive; profile Normal Completion x2.
- Run card: appended to `summary.md` by `scripts/run_card.py`

## Pointers

- Model snapshot: `results/state/model_snapshot.json` (`capture_state.py`;
  replayed + diffed by `12_verify_sync.py`)
- Machine state: `results/state/*.txt` (`aedt_port`, `aedt_process_id`,
  `solve_progress`, ...)
