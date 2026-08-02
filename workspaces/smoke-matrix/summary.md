# smoke-matrix workspace — Ticket 02 (DONE 2026-08-02)

One-time smoke-test matrix against the live AEDT 2024 R1 backend; all
outcomes recorded in `knowledge/playbook/environment-compat.md` (the
single accumulation point per ADR 0004). No other playbook content was
added (ADR 0002).

## Matrix run log (final full run)

| probe | outcome |
|---|---|
| launch_keep.py | PASS — launch, design, save, server left alive (pid printed) |
| attach_reuse.py | PASS — cross-process attach, launcher-written variable read |
| probe_solve_blocking.py | PASS — validate True; analyze(blocking=True) True @ ~147 s |
| probe_solve.py | PASS — analyze(blocking=False) True @ ~3.3 s; background completion |
| probe_rcs.py | Surface present; chain stops at optional deps + no SBR design (recorded) |
| readout (diag_readout) | Works once (S11 min ≈ 0.47 dB) then flaky unfilled-SolutionData |

## Notes for later tickets

- The smoke antenna design (pedestal + airbox + wave port) is a proven
  valid+solveable template (`src/smoke_design.py`) — Proof 1 can reuse the
  port/validation patterns.
- Readout flakiness (item 6) is the main open annoyance: route-around =
  fresh attach + retry + honest recording; revisit if Proof 1 QA fights it.
