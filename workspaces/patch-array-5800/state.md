# State ledger — patch-array-5800

Three phase sessions bound by this file (ADR 0007): Clarification -> Build
(through the Review gate incl. read-back sync) -> Solve+QA. Keep ~2 KB.
Machine state lives in `results/state/*.txt` — never hand-edited.

## Session 1 — Clarification (locked, never changed after)

- Started: 2026-08-18T09:27:37Z (`session.json`); task: `.scratch/hfss-agent-parallel-tests/TASK-verify-2x2-feed.md` (read fully; the briefing's constraints are binding).
- Session name: `patch-array-5800-clarify`; session.json phase=clarify.
- Recipe: `corporate-patch-array` (Modal; adaptive-only mesh; wave port; radiation airbox).
- Candidate: **C1-generalized** — the S7-corrected network (all-50-ohm lines, three lambda_g/4 @ 35.3553 ohm) as the base, chain re-synthesised to the MEASURED active impedance after stage 1. Why: only routing that is reviewed, corrected and known to fit at lambda/2; C2 cannot fit its 7.98 mm element lambda/4 into the 6.11 mm run (meanders add parasitics); C3 presumes 100 ohm elements, contradicting the expected ~41-50 ohm active value, and collapses into C1's topology once element impedance is measured.
- Methodology (user-approved): two solves in order — (1) ElementsOnly (4 lumped ports at the notch mouths; no network) -> 4x4 S-matrix -> Z_act via `hfss_spec.physics.active_impedance` (uniform broadside; 2x2 symmetry -> one number); (2) PatchArray (fed) built against 50/isolated first (validator warning IS the question), then revised to element_impedance: Z_act / active_measured, chain + inset retuned, and if the geometry changes: phase re-declare -> rebuild -> re-gate -> re-solve (user approved the second build pass, question Q2).
- User verdicts (verbatim): "Yeah so proceed, looks good" (Q1 candidate, assumptions, QA list). "Try to read your own results but if not i will tell u" (Q2 approved; readout: scripted first, UI authoritative fallback).
- Assumptions: (1) port plane = notch mouth = the fed design's real feed plane; line-into-notch is the same conductor. (2) match to Re(Z_act); residual reactance accepted if small — the -25 dB band arbitrates. (3) lumped ports normalized to 50 ohm; Hammerstad closed forms, W/h bounds enforced by the walk. (4) sweep 5.0-6.5 GHz both designs (briefing-locked; the validator's near-side-bracket warning was reviewed and accepted). (5) elements-only design mirrors the fed design's substrate/airbox/flush -y exactly, so the coupled environment is identical; the only planned difference is ports vs wave-port region, plus the fed design's conductor network (thin lines, parasitic currents accepted; the QA band arbitrates).
- Approved Result QA signals: convergence · ports excited · energy pass · resonance 5.8 GHz ±5% (dip position) · **dip-depth band** (the feed verdict: < -25 dB = matched to active Z; ~ -20 dB = matched to isolated 50 while elements present Z_act; ~ -9..-10 dB in band = 2:1 feed defect — THE falsification target; no dip = elements wrong) · broadside gain 12-13 dBi · element balance (near-field symmetry, UI-arbitrated).
- Offline gates (all green): `validate_spec` fed errors=0 warnings=2 (isolated-source warning = the run's question; sweep bracket accepted), elements errors=0 warnings=1; `compile_spec --dry-run` fed PASS (9 stages / 28 ops / 1 port / 1 boundary / escape_hatch=0), elements PASS (9 / 20 / 4 ports / 1 boundary); `tier0` PASS suites=14 failed=0 elapsed=101s. `precheck` verdict=no-estimator (UNCHECKED) BOTH — no estimator registered for `corporate-patch-array`; LEARNING-LOOP PROPOSAL pending at run end: add patch_resonance estimator entry to `precheck-tolerances.json` (ADR 0002 — append only after user approval).
- Element closed form verified offline 2026-08-18: patch_resonance(13.6238, 17.2679, 0.762, 3.48) = 5.8000 GHz exact. Hammerstad on this stack: 1.7427 mm = 50.00 ohm; 2.9084 mm = 35.3553 ohm (eeff 2.8491, q_x 7.6556); re-synthesis commodities if Z_act ~ 41 ohm: feed line 2.3562 mm (41 ohm), T2 transformers 3.3326 mm (32.0 ohm, q_x 7.6133), arms/trunk/input unchanged at 1.7427 mm, T1 2.9084 mm.
- Specs written: `design.yaml` (PatchArray fed) + `design_elements.yaml` (ElementsOnly), both compiled-gated above.

## Session 2 — Build

| Stage | Script/command | Verification line |
|-------|----------------|-------------------|
| Elements: compile | `compile_spec --launch` (ws_common DESIGN=ElementsOnly) | PASS: compile_spec spec=elements-5800 stages=9 (validate_simple=True) |
| Elements: snapshot | `capture_state.py` | PASS: capture_state bboxes=11 boundaries=5 objects=11 variables=14 |
| REVIEW GATE #1 | user inspects ElementsOnly; 3 fixes requested, applied, sync-verified | PASS (user: "geometry looks fine"; then passed after fixes) |
| Elements: fixes | notches per-patch (4 subtracts); ports rotated yz->xz across mouths; port sheets pec | RE-COMPILED: PASS stages=9; sync verify PASS: replay matches snapshot |
| Fed: compile | `compile_spec` (ws_common DESIGN=PatchArray) | PASS: compile_spec spec=patch-array-5800 stages=9 (validate_simple=True) |
| Fed: snapshot | `capture_state.py` | PASS: capture_state bboxes=5 objects=5 variables=17 |
| REVIEW GATE #2 | user inspects PatchArray; passed; material question closed with evidence (see pitfalls #5) | PASS: sync replay matches snapshot (verify 20260818_173423) |

## Session 3 — Solve + QA

**Live state block** (refreshed per decision):
- pin — aedt_port=64554 | watchdog pid = relaunched per solve
- solve status — solve #1a COMPLETE + BANKED but SUPERSEDED (flat-PEC-geometry record: status=Normal Completion, sweep_points=150, banked_at=1787089477); solve #1b = re-solve on the copper-box ElementsOnly (user-approved model-state change)
- solved marker — present (1a record); re-bank after 1b
- next action — RUN FINISHED: solve #2 banked (Normal Completion, 14 adp, 150 pts, 19:07:16); readouts UI-arbitrated (route recorded in readouts.txt — scripted surface systematically gRPC-broken: GetVariables/GetPropValue); summary.md + run card (slug hidden-falcon, runs 2) written; outcome.txt/completions.txt=2 recorded. User verdict (verbatim): resonance 5.6 GHz ~7 dB BOTH designs = "not outright failure, its just a tuning issue that can be corrected with a human hand" (element-level shift: Balanis fringing/er on this stack; feed NOT falsified as a defeat; lambda/4 for 5.8 operating at 5.6 + active/isolated question open). Pending: broadside gain + element balance UI reads (desktop stays alive, banked); learning-loop proposals pending user approval (summary.md Learning-loop notes 1-3).
- DISCIPLINE NOTE: the solve-phase declaration came one step late (08_solve submitted while session.json still read build — the staged scripts are not on the phase-gated surface); corrected immediately after; the solve itself is legitimate (user-approved model-state change).

Copper-revision notes (gate #3 passed by user 2026-08-18): patches + ground are 1 oz copper boxes (cu_t=0.035mm) in BOTH designs; notch cuts are through-copper boxes; airboxes + cu_t; fed wave-port sheet spans ground-copper bottom to lid. USER VERDICT on the fed array: "the unite box + sheet doesn't work because it can't work. Boxes have to unite with boxes and planar structures must unite with planars" — PatchArray accepted as 18 objects (4 patch boxes + 10 feed strips + ground + port + air; strips stay sheets so the feed walk keeps gating). COMPAT NOTE (learning-loop candidate #2): AEDT 2024 R1/pyAEDT 1.3.0 `unite` silently no-ops on mixed box+sheet sets; all-sheet unite proven (flat build); rule: like-to-like only.
COMPAT NOTE (candidate #3): sync-verify runner sees setups-prop key spelling variance (raw vs normalized) between the pinned live session and the fresh replay desktop — every model section replays EXACTLY (objects/bboxes/boundaries/ports/variables), setups keys differ (BasisOrder vs Basis Order, IsEnabled vs Enabled, ...). Proposal: normalize setup prop keys (strip spaces) in 12_verify_sync canon() — for run end, ADR 0002.
- FED REBUILD LOG (build-3, second DESIGN mishap + recovery): (1) ws_common.DESIGN was still ElementsOnly (left from solve 1b) -> the first copper-fed compile misrouted: fed spec built OVER ElementsOnly; the Subtract failure observed then was REAL but in the wrong design context; (2) desktop recycled (GetVariables + Subtract gRPC failures on the long-lived channel); (3) per-patch subtracts reverted to ONE subtract on the united P1 — the union (all-boxes) consumes P2/P3/P4, so per-patch blanks are ghosts (GrpcApiError Subtract is the symptom of a missing blank); with the union working, S7's single-subtract pattern is correct again; (4) recovered ElementsOnly (recompile + stray PortSheet/Port1 cleanup) — captured 11 objects, same shape as gate#3-passed; (5) PatchArray rebuilt clean: 5 objects (P1 united copper body: faces=66 edges=192 verts=128 — 8 through-slots present; PortSheet; Substrate; GroundPlane copper; AirBox), boundaries = Port1 (wave) + Rad only. DISCIPLINE NOTE #2: BOTH misroutes came from the same foot-gun — the DESIGN constant; attach always prints "Active Design set to X" and it WILL be read at every compile/solve from now on; the ledger records this as the run's standing Pitfall (7).

- Solve #1: ElementsOnly -> Z_act extraction -> ledger; then fed solve #2 (re-synthesis path approved by user, Q2).
- Watchdog: `results/state/solve_progress.txt` (running | complete | stalled | aborted — agent reads only).
- QA signals: numbers per agreed list, or "unreadable — flaky readout, UI-arbitrated".
- Deliverables: S11 5.0-6.5 GHz (fed), broadside gain, element balance, Z_act value, verdict on which candidate the run supports, summary.md + run card (by slug).

- Locked parameters / variables: f0 5.8GHz; er 3.48; tand 0.0037; h 0.762mm; cu_t 0.035mm; patch_W 17.2679mm; patch_L 13.6238mm; S 25.8442mm; feed50_W 1.7427mm; inset_d 2.0mm (match tuner, expected to move); inset_g 1.0mm; sub_W/L 70mm; air_pad 17.2295mm; port_w 8mm; xfmr_W 2.9084mm; q_x 7.6556mm (fed: to be re-derived from Z_act).
- ws_common DESIGN switches: ElementsOnly -> PatchArray (recorded here; edit `src/ws_common.py` between compiles; 12_verify_sync/capture_state read DESIGN from it).
- Pitfalls hit: (1) template copy nested one level (`workspaces/<name>/workspace/`) - fixed; (2) `validate_spec` near-side sweep warning is advisory - brief locked 5.0-6.5, accepted; (3) GATE-1 REVIEW FIXES: single-subtract cut notches in only 1 of 4 separate patches -> one subtract per patch; ports were built in the yz plane at the notch side edge -> xz across the mouth; port sheets lacked pec -> material: metal (all caught by user in UI, applied, sync-verified PASS); (4) GATE-1 REVIEW FIX (fed): Xfmr2L/R centered on the junction poked (xfmr_W-feed50_W)/2 = 0.58285 mm outboard and left the same air gap to the arms - both T2 junctions open; origins now -S/2 resp S/2-q_x, verified in model DB (XStart='-S/2', 'S/2 - q_x'); (5) NEW COMPAT NOTE: pyAEDT 1.3.0 Object3d.material_name reads '' for ALL 2D sheets (boxes fine) - capture_state material map blanks for sheets; the saved .aedt's MaterialValue= is the authority (verified pec on every sheet). Learning-loop candidate (ADR 0002, propose at end); (6) verify_spec_replay.py (workspace-local, design-spec-route sync verifier): pass --spec <name> to match ws_common DESIGN; default both specs compiles them into one design on the copy (replay-only artifact).
- Elements design integrity note: elements-only airbox/substrate mirror the fed design exactly (flush -y, lambda0/3), so the coupled environment is the same; the fed design's conductor network replaces the four mouth ports.

## Pointers

- Model snapshot: `results/state/model_snapshot.json` (`capture_state.py`; replayed + diffed by `12_verify_sync.py`).
- Machine state: `results/state/*.txt` (`aedt_port`, `aedt_process_id`, `solve_progress`, ...).
- Bid/phase: `results/state/session.json` (re-declare --phase build before any launch).
- Design docs: task brief `.scratch/hfss-agent-parallel-tests/TASK-verify-2x2-feed.md`; source of truth for the fed chain: `.scratch/hfss-agent-parallel-tests/cells/fixed/S7.design.yaml`.
