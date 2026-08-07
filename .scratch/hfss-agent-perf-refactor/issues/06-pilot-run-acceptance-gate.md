# 06 — Pilot run + acceptance gate

**What to build:** one greenfield pilot through the refactored tool — the same problem class as the baseline: bow-tie patch antenna ~3.5 GHz (paper-exact plain bowtie, no DGS, driven modal, single waveport). Run the full three-phase ceremony (Clarification → Build → Gate+sync → Solve+QA) on the live AEDT desktop with the user in the loop only at the Clarification block and the Review gate. Then measure with ticket 01's harness and append the run card to the pilot's summary.md.

**Acceptance (per spec and the grilling session):** vs the `silent-engine` baseline (398,130 billed tokens, 424 parts, ~1.6 h):

- billed tokens (`input + output`) **≥50% lower**
- step count (parts in the session DB) **≥40% lower**
- wall time excluding solver physics **≥40% lower**

Plus functional pass: delivered `.aedt` validates (`validate_simple()` True) and shows the expected in-band resonance per the approved QA signals.

**Calibration findings to record in the run card/ticket:** `variant: low` availability and its observed effect; `kb-lookup` spot-check verdict (did it return exact signatures? any 'not found' misses that cost a re-lookup?); watchdog behavior (solve_progress cadence, exit on completion); verify-runner outcome; any residual KB lookups after spine-api.md.

**Go/no-go:** the recorded results decide the deferred expansion — per-stage API cards (analysis §6.2), more cheap-tier subagents (analysis §7 routing table), or nothing further.

**Status:** ready-for-human
**Blocked by:** 01, 02, 03, 04, 05

- [x] Pilot completes all phases on the live desktop (terminated by user at the corrected-geometry QA read; build + solve + verify completed)
- [x] Run card appended to the pilot's summary.md with the three baseline-comparison numbers + calibration findings
- [x] Acceptance verdict recorded (go / no-go + reasons)

## Comments

- 2026-08-04: Thresholds locked in the grilling session (question 2).
- 2026-08-06: **PILOT RUN COMPLETE — VERDICT: NO-GO.** The pilot session
  (`shiny-canyon`, titled "Ticket-06 pilot acceptance gate", launched from
  this repo) was terminated by the user at the corrected-geometry QA read,
  after the refactored ceremony had built and solved the model. Full
  breakdown + corrective plan: `pilot-retrospective.md` in this feature
  folder. Summary:

  - Run card (final measure, appended via `python scripts/run_card.py
    --slug shiny-canyon --summary workspaces/bowtie-3500-pilot/summary.md`;
    numbers grow as the writing session accrues — the acceptance
    comparison in summary.md uses these): billed 1,981,137 (input
    1,777,402 + output 203,735) · parts 1,580 · duration 25 h 35 min 8 s
    (incl. ~21 h idle gap, not separately measurable) · store 2,113,689 B.
  - vs baseline: **+397% tokens, +273% parts, wall +1463% raw** — FAIL on
    all three acceptance axes; NOT the refactor's mechanism but its
    operation: solve resubmissions (5), watchdog false-stall (EXPECTED_SD
    guess vs F###-dir sweep outputs), teardown-before-banking that purged
    results once, engine-error plateau read as "complete" once, and an
    unrecoverable scripted readout (EC#6 flaky + pyAEDT 1.3.0 client bug
    `HfssConstants.default_solution`) burned the tokens.
  - Domain outcome: user audit caught a genuine Fig-1 dimension reading
    error (I had base/leg swapped vs paper L/W) via the UI at the first
    QA read; corrected geometry solved to Normal Completion (202 sweep
    points); the paper itself is internally inconsistent (the authors'
    equations do not reproduce Table I), which is why a second
    resonance read was requested before the user terminated the run.
  - **What the pilot bought (the acceptance's real output):**
    1. `capture_state` honored the variables contract (variable_manager
       fallback; `model.variables` is None on fresh attach).
    2. `12_verify_sync` diff normalized AEDT random suffixes
       (`Sweep_XXXXXX`, `Rad__XXXXXX`) — raw diffs can never pass.
    3. `12_verify_sync` copy layout fixed (scripts into `copy/src/` so
       `ws_common` WORKSPACE resolves in the copy).
    4. `poll_solve` counts `.sd`/`.asol` FILES, not just dirs (this box's
       sweep writes `F###` dirs + ~11 `.sd` files, not 201 `.sd`).
    5. `04_excitations` idempotency uses `BoundaryObject.delete()`
       (`Hfss.delete_boundary` does not exist in 1.3.0).
    6. `08_solve` skip-if-no-stale cleanup (raw `DeleteFullVariation`
       errors on first-ever solve) + deterministic detached watchdog
       launch (`subprocess.Popen(DETACHED_PROCESS)`; the PowerShell
       Start-Process quoting broke twice).
    Synced to `skill/hfss-agent/templates/workspace/src/` during the
    pilot: `capture_state.py`, `12_verify_sync.py`, `poll_solve.py`,
    `test_template_runners.py` (26/26). Fixes 5-6 live only in the pilot
    workspace's staged scripts (`04_excitations.py`, `08_solve.py` — the
    template has no per-stage files to sync them into; the workspace
    scripts are the reference implementation until a future template
    pass adds full stage exemplars). verify_skill 58/58 green at this
    commit.
  - Calibration findings, as ticketed:
    - `variant: low`: session metadata records the pilot at `variant:
      max` (config file says low; the session was launched before/outside
      the pin or the harness did not apply the agent variant — see the
      session's model metadata). Observed effect: unmeasurable on top of
      the orchestration churn; every comparison axis is dominated by
      stage/submission/readout counts, so variant choice is not the
      gate.
    - `kb-lookup` spot-check: PASS — exact signature returned with KB
      path (`Hfss.delete_setup(name) -> bool` from
      `hfss/ansys.aedt.core.hfss.Hfss.delete_setup.md`); no NOT FOUND
      misses on the two calls checked (setup deletion, sweep deletion);
      the one concrete miss was mine (`delete_boundary` assumed from the
      spine list — the KB has `BoundaryObject.delete`, which the spot
      check for "delete a boundary" would have caught if asked).
    - Watchdog: wrote `solve_progress.txt` every ~20 s as designed;
      **false-stalled** once when an agent-set `EXPECTED_SD` never
      matched the sweep's output shape; **false-completed** once on an
      engine-error plateau (profile said `Engine Detected Error`).
      Hangover fix: watchdog must append the profile `Status:` line
      before claiming complete/stalled (retrospective §B2).
    - Verify runner: 6 runs during the pilot; first two + build fixes
      landed `PASS: sync replay matches snapshot` twice (exit 0), then
      one replay hit a 900 s flaky-gRPC timeout on the copy's setup
      stage (runner guard correctly failed the run; retry PASSed).
    - Residual KB lookups beyond spine-api.md: 5 (delete_setup,
      delete_sweep, material_keys semantics ×2 attempts, materials
      getitem behavior, BoundaryObject.delete). Each was a real API
      question the spine didn't cover; all resolved from KB files.
  - Delivered state: `workspaces/bowtie-3500-pilot/` — all staged
    scripts, state ledger, snapshots, and the corrected solved `.aedt`
    (solves 4-5 Normal Completion; results banked on disk; the run card's
    QA section records the UI reads: first build resonated 3.85 GHz /
    −4 dB (geometry reading error), corrected build solved clean but the
    user terminated before reading its S11; paper dims internally
    inconsistent).
  - Go/no-go on the deferred expansion: **no-go** on per-stage API cards
    and further subagent tiering for the refactor as-is; the money is in
    the orchestration/readout discipline of the retrospective, not in
    more cards. Re-run eligibility: next pilot uses a self-consistent
    paper and the §C readout policy (single scripted attempt → UI), a
    bank-before-teardown rule, and watchdog profile-confirmed completion;
    measure the same three axes.
