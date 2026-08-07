# Summary — bowtie-3500-pilot

Written by the hfss-agent conversation at its end; appended to by read-back
sync deltas and learning-loop notes as they occur.

## What the Model is

- Design: Bowtie3500 · Project: `workspaces/bowtie-3500-pilot/bowtie_3500_pilot.aedt` ·
  Solution type: Modal (explicit, EC#11)
- Purpose / prompt: pilot acceptance run (ticket 06) of the perf refactor —
  reproduce the baseline bow-tie microstrip patch antenna (Astuti et al.
  2022, JCM 17:12) at ~3.5 GHz through the refactored ceremony.
- Model: NO DGS baseline bowtie; FR4_43 (er 4.3, tan-d 0.02), PEC ground
  and patch, substrate 90 x 80 x 1.6 mm, airbox with 25 mm gap (>= lambda/4
  @ 3.5 GHz) and radiation boundary, single waveport at x = +SubW/2.

## Acute design decisions

- **User-corrected Fig-1 reading (2026-08-05):** in the paper the triangle
  BASE — the edge farthest from the feed — is dimension L (20.2168 mm), and
  the two LEGS pointing inward toward the feed are dimension W
  (26.3269 mm). First build had them swapped (PatchW as base); the user
  caught it at the first QA UI read: resonance at 3.85 GHz / −4 dB instead
  of in-band ~3.5 GHz. Corrected: PatchBase=20.2168mm, PatchLeg=26.3269mm,
  PatchH=24.3094mm (derived). (The paper is internally inconsistent — its
  equations do not reproduce Table I; the user terminated the pilot at the
  second QA read.)
- Feed-location discipline (user steering note, held exactly): feed stub
  runs from the waist (0,0) along +X to x = +SubW/2; PatchBowtie xmax ==
  45.0 mm asserted; petals overlap the feed footprint at the waist (no
  point-contact petals — prior-art pitfall).
- Every dimension is a design variable; stale variables from the first
  parameterization are deleted-then-created away (ADR 0008), so the sweep
  variation table carries only live variables.
- Port: YZ sheet at x = +SubW/2 (flush with airbox +X face), 3*FeedW
  square, wave_port by FACE OBJECT (EC#7), 50 ohm renormalized; radiation
  boundary on AirBox (assign_radiation_boundary_to_objects).

## Clarification record

- Recipe: bowtie-5g-baseline (derived; paper-exact plain bowtie, no DGS,
  driven Modal, single waveport).
- Assumptions: FR-4 er 4.3, tan-d 0.02 (paper states er only); copper
  t = 0.1 (Table I); 50 ohm line width Wz = 3.1118; airbox gap 25 mm;
  port 3*FeedW; adaptive-only mesh; Setup1 @ 3.5 GHz 15 passes dS 0.02 +
  discrete sweep 3.2–4.2 GHz 201 pts (proven baseline shape).
- User answers (verbatim): Clarification Q → "One of the main issues was
  the feed location. Pay extra attention to that and I think we'll be good
  with the confirmed recipe." Review gate Q → "Pass — no tweaks".
- Approved Result QA signals: (1) convergence dS<=0.02; (2) port excited,
  S11 populated; (3) in-band resonance S11 min <= −10 dB in 3.4–3.6 GHz;
  (4) VSWR<=2 span >= 2.6% of center; (5) single-port plausibility.

## Read-back sync deltas

- None from UI tweaks (gate passed clean). Pilot QA read surfaced the
  Fig-1 base/leg correction, applied as a stage-02 amendment
  (PatchBase/PatchLeg/PatchH + stale-variable deletion) and verified by
  the sync-verify runner (PASS: sync replay matches snapshot, exit 0).
Model shape record: `results/state/model_snapshot.json` — the machine-precise
snapshot of objects/bboxes/materials/boundaries/excitations/setups/variables,
written by `src/capture_state.py` and verified by replaying the amended
scripts (`src/12_verify_sync.py`, one PASS/FAIL line).

## Results

Solve history (all on the corrected parameterization unless noted):
- Solve 1 (old base/leg): completed (user confirmed "simulation complete");
  results purged by an early teardown (pre-bank) — lesson banked.
- Solve 2: engine error mid-sweep (profile: Engine Detected Error) — first
  watchdog "complete" was a false plateau read.
- Solve 3: Normal Completion, 202 sweep points (old parameterization);
  invalidated by design when the corrected stage-06 rebuilt the setup.
- Solve 4: corrected geometry, Normal Completion, 202 sweep points.
- Solve 5: corrected geometry, Normal Completion, 202 sweep points
  (Stop 2026-08-06 23:38:17) — results banked on disk.

QA signals (locked set):
- (1) convergence: dS reached 0.074 (corrected) after 6 adaptive passes —
  NOT <= 0.02; the adaptive loop stopped at the pass limit (MaximumPasses
  stayed 6: `setup.props["MaxPasses"]` does not map to the internal key;
  same behavior as the silent-engine baseline) — reported as an anomaly.
- (2) port excited: waveport "1" + radiation present; S11 readout
  "unreadable — flaky readout" (EC#6; GrpcApiError GetVariables/GetSetups
  + pyAEDT 1.3.0 client bug HfssConstants.default_solution on every
  scripted shape).
- (3) in-band resonance: first (uncorrected) build measured in the UI at
  3.85 GHz / −4 dB (anomaly that surfaced the geometry fix); corrected
  build solved clean, readout not completed before the user terminated.
- (4) bandwidth: unreadable — flaky readout.
- (5) plausibility: single-port passive, profile Normal Completion ×2.
User verdict at termination: the paper's dimensions are internally
inconsistent; the pilot was stopped rather than chase a phantom paper.

## Learning-loop notes

- Pilot findings are recorded in the ticket 06 Comments and
  `pilot-retrospective.md` (feature folder): template fixes landed
  (capture_state variables fallback; verify-sync suffix canon + copy
  layout; poll_solve file counting; BoundaryObject.delete; 08_solve
  skip-no-stale + Popen detach) and five operational disciplines
  (single-shot readout -> UI; bank-before-teardown; watchdog
  profile-confirmed completion; one submission per verified state;
  PIN-liveness-bounded resume).
- A follow-up umbrella ticket for the corrective plan is pending the
  user's go on the retrospective.

## Run card

- slug: shiny-canyon
- created: 2026-08-06T03:56:43Z
- updated: 2026-08-07T05:31:51Z
- duration: 25 h 35 min 8 s
- tokens_input: 1777402
- tokens_output: 203735
- tokens_reasoning: 0
- tokens_cache_read: 68891381
- tokens_cache_write: 0
- billed: 1981137
- parts: 1580
- store_bytes: 2113689

## Acceptance comparison (ticket 06 gate)

Pilot session `shiny-canyon` vs the `silent-engine` baseline (398,130 billed
tokens / 424 parts / ~1.6 h), measured by `scripts/run_card.py`:

| Metric | baseline | pilot | delta | threshold | verdict |
|---|---|---|---|---|---|
| billed tokens | 398,130 | 1,981,137 | **+397%** | >=50% lower | FAIL |
| parts | 424 | 1,580 | **+273%** | >=40% lower | FAIL |
| wall (raw) | ~1.6 h | 25 h 35 min | **+1463%** | >=40% lower | FAIL |

Wall time "excluding solver physics" was NOT measurable post-hoc: the
session's raw duration includes ~21 h idle between solve-3 completion and
the user's return; no sub-session timestamp record exists, so the honest
claim is raw wall only. Functional pass: delivered `.aedt` validates
(validate_simple() True) and the corrected solve reached Normal Completion
(202 sweep points, profile-confirmed), but the in-band resonance QA read
was not completed — the user terminated the pilot at that read (paper
dimensions internally inconsistent: the authors' equations do not reproduce
Table I).

**Verdict: NO-GO** — all three acceptance axes failed; the pilot's value is
diagnostic. Calibration findings and the corrective plan are in
`.scratch/hfss-agent-perf-refactor/pilot-retrospective.md` and the ticket
06 Comments (variant-low availability, kb-lookup spot-check verdict,
watchdog cadence + false-stall/false-complete episodes, verify-runner
outcome, residual KB lookups, template fixes landed).
