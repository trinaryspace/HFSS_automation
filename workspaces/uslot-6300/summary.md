# Summary — uslot-6300

## What the Model is

- Design: `USlot6300` · Project: `workspaces/uslot-6300/uslot-6300.aedt` ·
  Solution type: Modal (explicit, never the default — env-compat #11)
- Prompt: read the U-slot reference paper, then build an HFSS simulation of a
  U-slot patch resonating (S11 <= -10 dB) across at least 5.8-6.8 GHz.
- The Model: a probe-fed U-slot patch on PTFE. A 50 x 40 x 3.81 mm
  `Teflon (tm)` (er 2.1) substrate; a 25.90 x 13.33 mm patch with a U-shaped
  slot cut into it (7.62 wide, 10.67 tall, 0.95 thick walls, arm tips stopping
  1.33 mm short of the +y patch edge); a 0.38 mm square PEC probe on the
  centreline inside the U, from the port gap up to the patch; patch and ground
  are 2D sheets carrying **Perfect E** boundaries; a 50 ohm lumped port on a
  0.38 x 0.2 mm gap sheet between ground and probe base; an air box padded
  lambda0/3 (15.86 mm) on all six faces carrying the radiation boundary.
  18 design variables — every dimension is a variable, no literals.
- Build route: **A (Design Spec)** — one `design.yaml` compiled by
  `scripts/compile_spec.py`. 0 geometry escape hatches.

## Acute design decisions

1. **Scaled the converged design of the paper rather than re-deriving from its
   equations.** The dimensions are the Borchardt & LaPointe (IEEE Access,
   2019) Section VI PTFE example — 2.4 GHz, h = 10 mm, er 2.1, 31 % 10-dB
   bandwidth — with every length multiplied by 2.4/6.3. With lossless
   conductors and unchanged permittivity this is exact Maxwell scaling: the
   response translates in frequency and the fractional bandwidth is preserved.
   Section V of the paper gives no closed-form synthesis and states the design
   needs numerical iterations guided by characteristic mode analysis; its
   equations produce starting points the authors then moved. The slot is the
   proof: the lambda_g/2 starting rule gives 19.11 mm, while the converged
   design is 28.96 mm — 1.51x larger, the same ratio the paper shows at
   2.4 GHz. Deriving from the equations alone would have left the slot about a
   third too short. Closing that gap needs a CMA solver this repo does not
   have, and building one was out of scope (hard rule 8).
2. **Dimension gate before anything was built.** `dims cross-check:
   consistent` — Balanis patch length 35.3 mm vs 35 in the paper; slot length
   lambda_g/2 50.2 mm vs 50; equation (5) resonances 2.05/2.75 GHz vs CMA
   2.00/2.72; probe position p1 = 22 mm by two independent routes.
   `precheck.py` returned `UNCHECKED` (no estimator for this recipe), so the
   closed-form check was done by hand and recorded rather than skipped.
3. **Coupling chosen for margin.** Equation (11): fractional bandwidth ~ kappa
   ~ Uw/W. The requested band needs only kappa ~ 0.159; the build keeps
   kappa = 0.294, predicting ~29 % and delivering 32.3 %.
4. **Metal as Perfect E boundaries, not as a sheet material** — see the gate
   record below. The one substantive correction of the run.
5. **Airbox clearance as an expression**, `c0 / (3 * f0)`, so the pad stays
   lambda0/3 if the design frequency is retuned; a literal would not.

## Clarification record

- Recipe: `probe-fed-u-slot-patch` — paper-sourced (Borchardt & LaPointe,
  IEEE Access 7 (2019) 109375, Sec. VI design example), frequency-scaled.
  `provenance.canonical_reading: Table` (the Sec. VI-C final-dimensions list).
- Papers read: `knowledge/reference-papers/Global/` (HFSS introduction, Ports)
  on every run, plus the one matching project folder `U-slot/`. No other
  project folder was read.
- Assumptions: PTFE `Teflon (tm)` er 2.1 at the exact scaled thickness
  3.81 mm; patch and ground as zero-thickness sheets; square PEC probe as the
  paper models it (cuboid, area-matched to a round probe); the gap source of
  the paper, at the probe base, realised as a lumped port on a gap sheet;
  finite 50 x 40 mm substrate and ground where the paper used infinite planes;
  airbox lambda0/3 on every face including below ground; adaptive-only mesh;
  Setup1 at 6.3 GHz, 20 passes, delta-S 0.02; discrete sweep 4.5-8.5 GHz,
  201 points; S11 read in the AEDT UI as the authoritative route, a scripted
  readout a bonus.
- User decisions: PTFE confirmed; the port to mimic the excitation of the
  paper (the lumped gap port already did, so no change); the proposed precheck
  estimator amendment deferred. Verbatim in `state.md`.
- Approved Result QA signals: convergence (delta-S <= 0.02 within 20 passes);
  ports excited (port + radiation present, S11 populated); in-band resonance
  (S11 <= -10 dB at every point in 5.8-6.8 GHz, two dips, measured band vs the
  31 % predicted); energy pass (S11 <= 0 dB, profile Normal Completion).

## Read-back sync deltas

No UI tweaks were made, so no staged script needed amending. The one model
change of the run came from user **inspection** at the Review gate, and was
folded into `design.yaml` — the single source of truth — before rebuilding:

- **Review gate 1, verdict `fixes`** (`results/state/review_gate.txt`): the
  user observed that the patch and ground-plane sheets carried no boundary in
  the UI. That was correct and it was a real defect. The spec made them metal
  by assigning the `pec` **material** to a 2D sheet. HFSS does not honour
  that: it treats the surfaces of a *3D* pec body as PEC automatically, but a
  2D sheet needs a boundary — "You can define PEC boundary on 2D sheet
  objects to represent lossless conductors such as ... patch antenna elements"
  (HFSS guide, Perfect E). An unbounded sheet is invisible to the solver, so
  the patch and ground would not have existed and the solve would have
  produced a confident, converged, meaningless S11. Corroborated by the
  human-built reference model
  `knowledge/cases/_snapshots/patch-10GHZ-probe-fed.json`, whose metal is
  `antennaMetal` / `groundMetal` Perfect E boundaries with blank materials.
  **Fix**: dropped `material` from both sheets, added `PatchMetal` and
  `GroundMetal` `perfect_e` boundaries; recompiled in place (idempotent,
  ADR 0008) — boundary count 1 -> 3, then 4 including the port.
- **Review gate 1, verdict `pass`** after the fix.

Model shape record: `results/state/model_snapshot.json`, written by
`src/capture_state.py`. The post-fix capture reads `bboxes=6 boundaries=4
materials=3 objects=6 setups=1 sweeps=3 variables=18`, with boundaries
`GroundMetal: Perfect E`, `PatchMetal: Perfect E`, `P1: Lumped Port`,
`Rad1: Radiation`. The spec-replay verification (`verify_spec_replay.py`) was
**not** run: there were no script amendments to replay, and the desktop
crashed twice afterwards (below).

## Results

Solve: `analyze(blocking=False)` submitted once, watched by the detached
watchdog. Terminal line `status=complete stage=done elapsed_s=464
profile_status=normal_completion`, evidence "profile status: Normal
Completion (stop 09/03/2026 15:49:06)". Stages: initial meshing 3 s, adaptive
meshing 27 s over 9 passes, frequency sweep 6 m 07 s. Banked to
`results/state/solved.txt` (Normal Completion, 200 sweep points) before any
teardown — which is what made the two later desktop crashes harmless.

Readout route: `route=report-export` on the live channel.
`get_solution_data` returned unfilled exactly as env-compat #6 predicts (it
dies in a ctypes callback in the gRPC plugin), and the `CreateReport` +
`export_report_to_file` CSV route read it on the same process. The single
fresh-process escalation was never spent.

| QA signal | Value | Verdict |
|---|---|---|
| Convergence | final delta-S 0.01742 (target 0.02) in 9 passes of 20; history 0.705 -> 0.128 -> 0.088 -> 0.108 -> 0.031 -> 0.035 -> 0.0217 -> 0.0174 | PASS |
| Ports excited | P1 lumped + Rad1 radiation present; S11 populated, 201 points | PASS |
| In-band resonance | worst S11 in 5.8-6.8 GHz = **-11.32 dB**; widest -10 dB band **5.185-7.181 GHz** (1996 MHz, 32.3 % fractional); dips -18.9 dB @ 5.38 GHz and -18.7 dB @ 6.56 GHz | PASS |
| Energy pass | max S11 = -0.311 dB <= 0, single passive port, Normal Completion | PASS |

Prediction vs measurement: the method of the paper predicted a 31 % band of
5.32-7.28 GHz at 6.3 GHz; the solve gives 32.3 % over 5.185-7.181 GHz — both
band edges within about 2 %. The requested 5.8-6.8 GHz sits inside the
achieved band with 615 MHz of margin below and 381 MHz above.

Deliverables in `results/`: `s11.png` (the S11 plot),
`AgentReadout_dB_S_1_1.csv` (201 rows, the exported trace), `model_top.jpg`
and `model_isometric.jpg` (the as-built model at the gate). The
`AgentReadout_dB_S_1_1` report is left standing in the design tree so the
authoritative UI read opens the same plot.

**User verdict (verbatim)**: "The results are actually really good. Matched across the band, I also checked the gain flatness across the band and the peak is 0.6 dB from the lowest, which is good. This is a great success." The gain flatness was a user UI
measurement, not an agreed QA signal and not one this run measured; it is
recorded because it corroborates the paper, which reports that both coupled
modes radiate broadside and co-polarized, giving a stable pattern across the
whole impedance bandwidth.

## Learning-loop notes

Nothing was appended to the playbook. These are **candidates only**, awaiting
the approval ceremony (ADR 0002); the estimator proposal was deferred by the
user during Clarification.

1. **Metal on 2D sheets — the exemplar propagates a modelling error.**
   `reference/design-spec.md` states that a `material: pec` on a sheet and a
   `perfect_e` boundary are both legal. That is wrong for sheets per the HFSS
   guide, and it is not a documentation-only problem:
   `knowledge/cases/patch-2400/design.yaml` and the maintained authoring
   exemplar `patch-2400-authoring/design.yaml` — the file `SKILL.md` tells
   patch authors to copy — both carry pec-material sheets with only a
   radiation boundary. This run inherited the defect from the exemplar and it
   was caught only by the user at the Review gate. No offline gate catches a
   floating conductor; `validate_spec`, `precheck` and the dry-run all passed.
   Candidate: a validator rule that errors when a sheet is neither the target
   of a metal boundary nor a port, plus a fix to the exemplar and the prose.
2. **No pre-check estimator for the U-slot recipe.** `precheck.py` returned
   `UNCHECKED`, so the dimension gate was done by hand. Candidate: an
   estimator from equation (5) plus the Balanis patch length. Deferred.
3. **`compile_spec.py` could not launch a template workspace (fixed).**
   `load_ws_common()` loads the workspace preamble by file path without
   putting `<ws>/src` on `sys.path`, so `import run_events` raised
   `ModuleNotFoundError` and Route A could not run at all. Fixed in
   `scripts/compile_spec.py` (uncommitted, in the checkout of the user).
   A tool defect for the retro, not a playbook amendment.
4. **Agent error, not a tool defect**: a watchdog-liveness check using
   `tasklist /FI "PID eq <n>"` under Git Bash returned a false negative, so a
   live watchdog was reported dead and a second one launched. Both only
   observe; no re-submission occurred and the solve was untouched. Use
   PowerShell `Get-Process -Id`.
5. **Transient client block**: `capture_state.py` hung over 20 minutes on one
   attempt while the desktop was in use, then passed in seconds after the
   client process was killed. Consistent with the env-compat note that DLL
   calls hold the GIL. One observation, no control — not a channel verdict.
6. **Two desktop crashes during post-processing**, one in a network outage,
   one user-caused. Neither cost anything: the solve was banked first, so
   `src/14_relaunch.py` reopened the saved project, cleared the stale lock
   (env-compat #9) and re-pinned. Evidence that bank-before-teardown does the
   job it was added for.

## Run card

### clarify+build+solve — u-slot patch antenna design

- slug: u-slot patch antenna design
- host: claude-code
- created: 2026-09-03T14:46:31Z
- updated: 2026-09-03T23:53:46Z
- duration: 9 h 7 min 15 s
- tokens_input: 3056
- tokens_output: 126869
- tokens_reasoning: 54689
- tokens_cache_read: 25250069
- tokens_cache_write: 872409
- billed: 129925
- parts: 411
- store_bytes: 2111813
- subagents: 2
- subagent: kb-lookup "Look up model picture export API" billed=1690 parts=67 duration=0 h 1 min 20 s
- subagent: runcard "Draft summary sections and run card" billed=3378 parts=35 duration=0 h 4 min 36 s

### Run total

- run_id: uslot-6300-2026-09-03
- skill_commit: 6a991f5
- sessions: 1 (clarify+build+solve)
- unresolved: 0
- subagents: 2
- created: 2026-09-03T14:46:31Z
- updated: 2026-09-03T23:53:46Z
- duration: 9 h 7 min 15 s
- active_wall_start: 2026-09-03T14:48:00Z
- active_wall_start_source: sessions.jsonl
- solve_gate: 2026-09-03T19:42:24Z
- solve_submissions: 1
- active_wall: 4 h 54 min 23 s
- tokens_input: 3292
- tokens_output: 131701
- tokens_reasoning: 55870
- tokens_cache_read: 25817423
- tokens_cache_write: 952852
- billed: 134993
- billed_sessions: 129925
- billed_subagents: 5068
- parts: 513
- store_bytes: 2578099
- outcome: completed (The results are actually really good. Matched across the band, I also checked the gain flatness across the band and the peak is 0.6 dB from the lowest, which is good. This is a great success.)
- escape_hatch_scripts: 0
- billed_per_completed_sim: 134,993
