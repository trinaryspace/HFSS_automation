# 03 — Event log from the repo's own tooling

**What to build:** `hfss_spec/events.py` with one function,
`emit(state_dir, event, *, phase=None, stage=None, verdict=None, detail="",
duration_ms=None)`, appending one JSON line to
`results/state/events.jsonl`: `{ts, run_id, phase, stage, event, verdict,
detail, duration_ms, pid, argv0}`. Stdlib only, never raises (a logging
failure must not fail a stage), and a no-op when the state dir does not
exist yet.

Wire it into every place a stage boundary or verdict is already known:

| where | events |
|---|---|
| `hfss_spec/session.py` | `phase.declared`, `phase.refused` (with the action), `budget.escalate` |
| `scripts/compile_spec.py` / `hfss_spec/compiler.py` | `compile.start`, one `stage.start` / `stage.end` per emitted stage with its `PASS:`/`FAIL:` line as `verdict`, `desktop.launch`, `desktop.attach` (port, pid), `compile.end` |
| `scripts/tier0.py`, `scripts/tier1.py`, `scripts/validate_spec.py`, `scripts/precheck.py` | `gate.<name>` with the summary line |
| template `capture_state.py`, `12_verify_sync.py`, `verify_spec_replay.py` | `snapshot.captured`, `sync.verify` with verdict |
| solve stage, `confirm_solve.py`, `poll_solve.py` | `solve.submitted`, `solve.terminal` (the watchdog's terminal line verbatim), `solve.banked`, `teardown` |
| template `read_results.py` | `readout.attempt` with route and error class |
| `scripts/record_outcome.py`, `scripts/record_gate.py` (ticket 02) | `outcome.recorded`, `gate.recorded` |
| `scripts/run_card.py`, `scripts/run_report.py` | `card.written`, `report.written` |

Two rules. First, the event is the same string the runner already prints:
the `PASS:` house style is the `verdict` field, so nothing is worded twice.
Second, `detail` is one line, never a dump; the watchdog's tick log stays in
`solve_progress.txt`, only its terminal line becomes an event.

The `desktop.attach` event carries port and pid, which is what makes a
mid-run desktop recycle visible to the report without anyone writing it in
the ledger.

**Blocked by:** 01 (for `run_id`).

**Status:** ready-for-agent

- [ ] `hfss_spec/events.py` with tests: append-only, never raises, no-op without a state dir
- [ ] Every runner in the table emits its events; a tier-0 test drives the template runners against fixtures and asserts the event sequence
- [ ] A compile of a canonical case on Tier 1 leaves one `stage.start`/`stage.end` pair per stage
- [ ] `execution.md` verification contract gains one sentence: every `PASS:` line is also an event
