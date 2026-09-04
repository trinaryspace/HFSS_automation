# State ledger — uslot-6300

Three phase sessions bound by this file (ADR 0007): Clarification → Build
(through the Review gate incl. read-back sync) → Solve+QA. Each starts here,
not from the prior conversation. Keep ≤ ~2 KB: stage progress, locked
parameters, pitfalls, pointers. Machine state lives in `results/state/*.txt` —
never hand-edited; the staged scripts write it.

## Session 1 — Clarification (locked in the UI, never changed after)

- Started: 2026-09-03T14:48:00Z (written once, never changed)
- Request: U-slot patch, S11 ≤ -10 dB over at least 5.8–6.8 GHz (f0 = 6.3 GHz,
  ≥ 15.9 % fractional BW).
- Papers read: `Global/` (HFSS intro, Ports) + `U-slot/` Borchardt & LaPointe
  IEEE Access 2019 (analyze-papers notes in Literature_analyzer/agent_out).
- Recipe: probe-fed-u-slot-patch — the paper's Sec. VI PTFE design example
  (2.4 GHz, h 10 mm, er 2.1, 31 % 10-dB BW) frequency-scaled by 2.4/6.3.
  PAPER-SOURCED. dims cross-check: consistent (Balanis L 35.3 vs 35; Ul λg/2
  50.2 vs 50; eq.5 2.05/2.75 vs CMA 2.00/2.72; p1 = 22 = 22). precheck:
  UNCHECKED — no estimator for this recipe (learning-loop candidate).
- Build route: A (design spec) — `design.yaml` validates (0 errors, 1 warning:
  'Teflon (tm)' not in the validator's library list; the desktop carries it,
  snapshot patch-10GHZ-probe-fed read it back), dry-run PASS, 0 escape hatches.
- Assumptions: PTFE `Teflon (tm)` er 2.1 h 3.81 mm (exact scaling); PEC sheets
  for patch + ground, zero thickness; square PEC probe 0.38 mm on the
  centreline inside the U; feed = lumped port on an xz sheet (0.38 × 0.2 mm)
  from ground to probe base (paper: gap source at probe base); finite
  substrate/ground 50 × 40 mm (paper: infinite); airbox pad λ0/3 = 15.86 mm
  all faces incl. below ground; adaptive-only mesh, Setup1 6.3 GHz / 20 passes /
  dS 0.02; discrete sweep 4.5–8.5 GHz, 201 pts; results path: S11 read in the
  AEDT UI, scripted readout a bonus.
- Locked variables (mm): h 3.81, patch_W 25.9, patch_L 13.33, slot_W 7.62,
  slot_H 10.67, slot_Uo 1.33, slot_tw 0.95, slot_th 0.95, probe_po 2.67,
  probe_d 0.38, port_gap 0.2, sub_W 50, sub_L 40; air_pad = c0/(3 f0);
  slot_bot = patch_L/2 - slot_Uo - slot_H; probe_y = slot_bot + slot_tw + probe_po.
- Predicted: coupled resonances 5.37 / 7.23 GHz (eq. 5); 10-dB band ≈ 5.32–7.28 GHz.
- Proposed Result QA signals: (1) convergence dS ≤ 0.02 within 20 passes;
  (2) port excited: P1 lumped + Rad1 present, S11 populated; (3) in-band:
  S11 ≤ -10 dB at every sweep point in 5.8–6.8 GHz, two dips near 5.4 and
  7.2 GHz (±5 %), measured 10-dB band vs 31 % predicted; (4) energy pass:
  S11 ≤ 0 dB everywhere, profile Normal Completion.
- Decisions: substrate = exact-scaled PTFE 3.81 mm; feed = the paper's gap
  source at the probe base, realised as the lumped port on PortSheet (no spec
  change); learning-loop estimator proposal deferred by the user (not filed).
- User confirmation (verbatim): "PTFE is good. Mimic what is done in the paper
  for the port. Don't add the learning loop yet." — Recipe, assumptions and
  QA signals confirmed 2026-09-03. Clarification DONE; next: build session.

## Session 2 — Build

Route A: `python scripts/compile_spec.py --workspace workspaces/uslot-6300
--spec workspaces/uslot-6300/design.yaml --launch` after tier0 + VPN check;
then `src/capture_state.py` → `as_built.json`; Review gate; `record_gate.py`.

| Stage | Verification line |
|-------|-------------------|
| compile_spec --launch | PASS: compile_spec spec=uslot-6300 stages=9 (40.6 s; launch port 59432 pid 45592; validate_simple=True) |
| capture_state | PASS: capture_state bboxes=6 boundaries=2 excitations=0 materials=3 objects=6 setups=1 sweeps=3 variables=18 |
| Recompile after gate fix 1 | PASS: compile_spec spec=uslot-6300 stages=9 (boundaries count=3, validate_simple=True) |
| Review gate + sync verify (`verify_spec_replay.py`) | <paste PASS line> |

- As-built: 6 objects (AirBox GroundPlane Patch PortSheet Probe Substrate) —
  the 3 slot rectangles were consumed by the subtract; P1 Lumped Port + Rad1
  Radiation; Setup1 6.3GHz/20 passes + Sweep1; 18 design variables.
  Patch bbox 25.9 x 13.33 @ z=3.81, Probe y=-1.905..-1.525 z=0.2..3.81,
  PortSheet x +-0.19 z 0..0.2 @ y=-1.715, airbox pad 15.862 mm every face.
- Pitfalls hit:
  1. TOOL DEFECT (fixed in repo, uncommitted): `scripts/compile_spec.py`
     `load_ws_common()` loads the workspace preamble by file path without
     putting `<ws>/src` on sys.path, so the template's `import run_events`
     (run logging ticket 03) raised ModuleNotFoundError and Route A could not
     launch. Sibling scripts (`12_verify_sync.py`, `capture_state.py`) guard
     the same import; the compiler did not. First Route A launch against a
     template workspace carrying `run_events.py`. Retro issue candidate.
  3. MODEL DEFECT found by the user at Review gate 1 (fixed): Patch and
     GroundPlane were 2D sheets carrying `material: pec` and NO boundary, so
     the UI showed them unassigned. `pec` on a sheet is not the mechanism:
     HFSS treats the surfaces of a 3D pec body as PEC automatically, but a 2D
     sheet needs an explicit boundary ("You can define PEC boundary on 2D
     sheet objects to represent lossless conductors such as ... patch antenna
     elements" — HFSS guide, Perfect E section; the guide also states
     boundaries are assigned ON 2D sheets). An unbounded sheet is invisible to
     the solver: the patch and ground would not have existed. Corroborated by
     the 12a human-built snapshot patch-10GHZ-probe-fed, whose metal is
     `antennaMetal` / `groundMetal` Perfect E with blank materials. FIX:
     dropped `material` from both sheets, added `PatchMetal` / `GroundMetal`
     perfect_e boundaries; recompiled in place, boundaries count 1 -> 3.
     NOTE for the retro: `knowledge/cases/patch-2400/design.yaml` and the
     authoring exemplar `patch-2400-authoring/design.yaml` carry the same
     shape (pec sheets, only Rad1), and `reference/design-spec.md` states both
     patterns are legal — that prose is wrong for sheets and the exemplar
     propagates it. No offline gate catches a floating conductor. Playbook
     amendment NOT filed (user deferred the learning loop).
  2. Sheet materials read back '' for GroundPlane/Patch/PortSheet — expected,
     env-compat #15 (2D sheets expose no Material property); pec is in the
     saved model DB. Not a defect, not a model change.

## Session 3 — Solve + QA

- Watchdog: `results/state/solve_progress.txt` (the agent reads only);
  watchdog pid 21636, submitted_at 1788464544.
- Solve decisions (resolve-once, ADR 0007 practice):
  - solve #1 — submitted on the verified state (Review gate 1: one fix round
    then PASS, `results/state/review_gate.txt`; capture_state PASS with
    boundaries=4). 08's in-flight probe WARNED (results_age 4357 s, 2 live
    ansysedt) and its own classifier cleared it: "no stale solve results
    (asol skeletons only)" — no .sd sweep files, and both processes are
    accounted for (user's desktop 31896 + our pinned 45592). No prior solve.
    analyze(blocking=False) -> True (submission only, EC#5) in 3.2 s.
    user: "Ok then, go ahead and solve".
- Live state: pin=59432 (probed this session, pid 45592); solve status=running
  (watchdog 21636); solved marker=none; next action=read terminal line, then
  bank via confirm_solve.
- Pitfall (build->solve boundary): `capture_state.py` blocked >20 min on the
  first attempt after the recompile (no output, desktop alive, client wedged
  in a gRPC/DLL call while the UI was in use — EC transport note: DLL calls
  hold the GIL). Killed the client process only (pid 26888; the desktop was
  never touched) and re-ran: PASS in seconds. Not a desktop recycle, not a
  channel verdict — a transient block, recorded for the retro.
- Solve terminal line: tick=23 status=complete stage=done elapsed_s=464
  profile_status=normal_completion evidence="profile status: Normal Completion
  (stop 09/03/2026 15:49:06)"; stages Initial_Meshing 3 s, Adaptive_Meshing
  27 s / 9 passes, Frequency_Sweep 6 m 07 s. Banked:
  `results/state/solved.txt` status=Normal Completion sweep_points=200.
- QA signals (read route: report-export on the live channel — `get_solution_data`
  returned unfilled as EC#6 predicts, the CreateReport + export CSV route read
  it; token `route=report-export` in `results/state/readouts.txt`; no fresh
  process was needed, escalation budget unspent):
  (1) convergence: 9 adaptive passes of 20 allowed, final delta S = 0.01742
      (<= 0.02 target; history 0.705 -> 0.128 -> 0.088 -> 0.108 -> 0.031 ->
      0.035 -> 0.0217 -> 0.0174), profile Normal Completion. PASS.
  (2) ports excited: P1 lumped + Rad1 radiation present; S11 populated,
      201 points over 4.5-8.5 GHz. PASS.
  (3) in-band resonance: worst S11 in 5.8-6.8 GHz = -11.32 dB (<= -10 dB
      required, 1.32 dB margin); widest -10 dB band 5.185-7.181 GHz =
      1996 MHz = 32.3% fractional; two dips 5.38 GHz @ -18.9 dB and
      6.56 GHz @ -18.7 dB. PASS — the requested band sits inside the
      achieved band with ~615 MHz below and ~381 MHz above.
  (4) energy pass: max S11 = -0.311 dB (<= 0), single passive port. PASS.
- Prediction vs measurement: predicted 10 dB band (paper eq. 11, 31% at
  6.3 GHz) 5.32-7.28 GHz; measured 5.185-7.181 GHz — band edges within 2.5%
  and 1.4%, fractional BW 32.3% vs 31%. The scaling held.
- Deliverables in `results/`: s11.png, AgentReadout_dB_S_1_1.csv (201 rows),
  model_top.jpg, model_isometric.jpg.
- Pitfall (agent error, NOT a tool defect): my watchdog-liveness check used
  `tasklist /FI "PID eq <n>"` under Git Bash and returned a false negative, so
  I reported the watchdog dead while it was alive and launched a second one.
  Both only observe; no re-submission occurred and the solve was untouched.
  Duplicate reaped, canonical pid restored. Use PowerShell `Get-Process -Id`.
- Run card: `record_outcome.py` → `run_card.py --summary` → `run_report.py`

- Desktop crash + relaunch (user-reported, 2026-09-03 after QA): both AEDT
  processes died (user's and our pinned 45592) during a network outage. No
  loss: the solve was already banked (`solved.txt`), 200 *_SU.txt sweep files
  and the 104 KB project were on disk, and every deliverable in `results/`
  predates the crash. `src/14_relaunch.py` relaunched and re-pinned
  (port 59312, pid 62476), the preamble's remove_lock cleared the stale
  `.lock` (EC#9), and the `AgentReadout_dB_S_1_1` report was RE-created —
  it had been made after the last save, so it did not survive — then the
  project was saved. PASS: relaunch ... saved=True.

## Pointers

- Spec: `design.yaml`; snapshot: `results/state/model_snapshot.json`
- Machine state: `results/state/*.txt`, `session.json`, `events.jsonl`
