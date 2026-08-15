# Summary — patch-2400

Written by the hfss-agent conversation at its end; appended to by read-back
sync deltas and learning-loop notes as they occur.

## What the Model is

- Design: Patch2400 · Project: `workspaces/patch-2400/patch_2400.aedt` ·
  Solution type: Modal (explicit, EC#11)
- Purpose / prompt: inset-fed rectangular microstrip patch antenna at
  2.4 GHz on FR4; lumped port on the inset feed tuned for 50 ohm; radiation
  boundary; S11 vs frequency requested. Dimensions from the vetted case
  `knowledge/cases/patch-2400/case.json` (canonical; Balanis closed-form).
- Model: patch 38.0100 x 29.4216 x 0.035 mm (PEC) with two inset notches
  (InsetGap 3.0 mm, InsetDepth 7.4 mm) at the -Y radiating edge; 50-ohm
  microstrip feed (FeedW 3.06 mm, Hammerstad) from the 80x80x1.6 mm
  FR4_epoxy substrate -Y edge into the inset, united with the patch; full
  PEC ground below; airbox + 31 mm gap with radiation boundary Rad1; lumped
  port '1' on the XZ sheet at the trace end (ground-top to trace-bottom,
  vertical integration line, 50 ohm). Setup1: 2.4 GHz, 15 passes, dS 0.02;
  discrete sweep 2.0-3.0 GHz, 201 pts. Adaptive-only mesh.

## Acute design decisions

- **Case-backed recipe, not paper-sourced**: case.json closed-form Balanis
  dims are canonical (no paper dimension gate); notes.md fragility read:
  inset depth is the match tuner, QA judges resonance position not absolute
  depth.
- **Port construction worked around a pyAEDT 1.3.0 defect**: passing a
  FacePrimitive to `lumped_port` serializes the face id into
  `props["Objects"]` and the macro layer rejects it ("a geometry selection
  is required for assignment") — unlike `wave_port`, which resolves face ids
  to object names. Working shape: pass the stable **sheet name** with the
  explicit 2-point integration line derived from the sheet's bbox.
- **XZ rectangle size order on this pairing**: `create_rectangle("XZ")`
  maps sizes to [z, x], not [x, z] (measured via bbox: a transposed sheet
  was caught and fixed; sizes [SubH, FeedW] are correct).
- **Inset tuned by variable, not geometry**: InsetDepth 7.4 mm (about L/4)
  landed a -20 dB match on the first solve — unusually good; depth stays a
  design variable for retune.
- Adaptive-only mesh; Setup1 + discrete 201-pt sweep 2-3 GHz (proven
  baseline shape).

## Clarification record

- Recipe: inset-fed rectangular microstrip patch (case-backed
  `patch-2400`).
- Assumptions: FR4_epoxy stock values (er 4.4, tan-d 0.02; verified from
  the design post-solve); PEC copper; ground = substrate footprint 80x80;
  patch centered, feed on centerline x=0 along -Y; airbox gap 31 mm
  (~lambda0/4); lumped port 50 ohm at the trace end; adaptive-only mesh;
  results path: S11 read via AEDT UI on this box, scripted readout a bonus.
- User answers (verbatim): Clarification -> "Confirm as proposed
  (Recommended)"; Review gate -> "yeah i think this looks good"; watchdog
  anomaly -> "Bank and continue (Recommended)".
- Approved Result QA signals: (1) convergence dS<=0.02; (2) ports excited;
  (3) in-band resonance within 5% of 2.4 GHz (2.28-2.52); (4) energy pass.

## Read-back sync deltas

- None from UI tweaks (gate passed clean; sync verify PASS after the
  stage-02/04 amendments described above).
Model shape record: `results/state/model_snapshot.json` — the machine-precise
snapshot of objects/bboxes/materials/boundaries/excitations/setups/variables,
written by `src/capture_state.py` and verified by replaying the amended
scripts (`src/12_verify_sync.py`, one PASS/FAIL line).

## Results

Solve #1 (the only submission): watchdog detached pid 36936; the watch-dog
process died at tick 8 (no terminal line, root cause undetermined) but the
solve itself completed: profile DV85_S82_V100 `Normal Completion`, Stop
08/14/2026 21:44:52, 6 adaptive passes, 200 sweep points; evidence banked to
`results/state/solved.txt`. Readout route: **AEDT UI** (scripted
`get_solution_data` failed with GrpcApiError GetVariables — the known
EC#6 flaky readout; one attempt, not iterated).

QA signals (locked set):
- (1) convergence: profile Normal Completion, 6 adaptive passes, target
  dS 0.02 (throttled to the pass limit — the final dS is visible in the
  UI Convergence dialog). PASS.
- (2) port excited: lumped port '1' + radiation Rad1 present; S11 curve
  populated (200 pts). PASS.
- (3) in-band resonance: S11 min **2.317 GHz, -20 dB** (in 2.28-2.52 GHz
  band, 3.5% below 2.4 — within the 5% tolerance; FR4 permittivity
  tolerance is the dominant uncertainty). -10 dB BW 2.295-2.340 GHz
  (45 MHz, ~1.9% — typical thin-FR4 patch). PASS.
- (4) energy pass: single-port passive, deep matched dip, profile Normal
  Completion. PASS.

Note: the first UI reading was transcribed as "3.317 GHz" — outside the
swept band; the user corrected it to 2.317 GHz. No anomaly remains.

## Learning-loop notes

Proposed amendments (awaiting user approval, ADR 0002):
- env-compat: `Hfss.lumped_port` on this pairing must NOT be passed a
  FacePrimitive — face ids land in `props["Objects"]` and the macro layer
  rejects them; pass the sheet NAME (+ explicit integration line). Also:
  `create_rectangle("XZ", ...)` sizes map to [z, x] on 2024 R1.
- environment-compat/08_solve: the in-flight probe uses the same
  .asol-skeleton criterion as the cleanup step (it flagged build-time
  skeletons as a live solve on a first-ever layout).
- watchdog death class without a terminal line: banked solve evidence made
  the anomaly benign; consider a watchdog journal/heartbeat for diagnosis.

## Run card

- slug: kind-rocket
- created: 2026-08-15T01:19:01Z
- updated: 2026-08-15T02:00:41Z
- duration: 0 h 41 min 40 s
- active_wall_start: n/a
- solve_gate: n/a
- active_wall: unmeasurable: no session-1 start in state.md
- tokens_input: 196481
- tokens_output: 72897
- tokens_reasoning: 0
- tokens_cache_read: 8990483
- tokens_cache_write: 0
- billed: 269378
- parts: 412
- store_bytes: 1086371
- outcome: completed (S11 minimum 2.317 GHz at -20 dB, inside the 2.28-2.52 GHz acceptance band (3.5% low, tolerance 5%); all four locked QA signals reported PASS. One solve submission, profile Normal Completion, 200 sweep points, banked to solved.txt. Readout route was the AEDT UI after one failed scripted get_solution_data (EC#6); no S11 plot artifact was written to results/, so the numeric result is user-transcribed from the UI. escape_hatch_scripts=0 is recorded pro forma: the spec-language escape hatch does not exist before phase 2, so every stage script here is the normal path, not an escape.)
- escape_hatch_scripts: 0
- billed_per_completed_sim: 269,378
