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

**Status:** ready-for-human

- [x] `hfss_spec/events.py` with tests: append-only, never raises, no-op without a state dir
- [x] Every runner in the table emits its events; a tier-0 test drives the template runners against fixtures and asserts the event sequence
- [x] A compile of a canonical case on Tier 1 leaves one `stage.start`/`stage.end` pair per stage — **proven offline** (the compiler driven over the real `patch-2400` spec with the golden tests' `FakeHfss`, and `compile_spec.py` end to end with the workspace module faked); the live Tier-1 run on a desktop is still pending — see Comments
- [x] `execution.md` verification contract gains one sentence: every `PASS:` line is also an event

## Comments

### 2026-09-02 — landed

Two corrections to the ticket's table first. **There is no compiled solve
stage** (ticket 02's finding): the solve events live in the template's
`08_solve.py`, `poll_solve.py`, `confirm_solve.py` and `ws_common.teardown`.
And **`run_report.py` does not exist yet** (ticket 06), so `report.written`
is not emitted by anything; `card.written` is.

What landed, by file:

- `hfss_spec/events.py` (new): `emit(state_dir, event, *, phase, stage,
  verdict, detail, duration_ms)` appends `{ts, ts_ms, run_id, phase, stage,
  event, verdict, detail, duration_ms, pid, argv0}` to
  `results/state/events.jsonl`. Never raises (an unwritable file, an
  unserialisable detail, a torn `run.json` all return False); a no-op when
  the state dir does not exist; `detail` and `verdict` are cut to their
  first line (cap 1000 chars). `run_id` is read from `run.json` (ticket 01)
  and is `null` before the first declaration; `phase` defaults to the
  current `session.json` phase. **Deliberately self-contained** — it imports
  nothing else from `hfss_spec`, so the template can load it by file path
  without dragging the package's Pydantic import into the watchdog.
  `read()` / `names()` for tests and the report.
- `skill/hfss-agent/templates/workspace/src/run_events.py` (new): the
  workspace's one hook. Walks up from its own directory to the nearest
  `hfss_spec/events.py` (works from `workspaces/<name>/src/` and from a
  sync-verify copy nested under `results/state/verify/<stamp>/copy/src/`),
  loads it by file, forwards. Stdlib only; silent no-op when no checkout is
  above the workspace. Added to `TEMPLATE_SRC_FILES` with `08_solve.py`
  (ticket 02's leftover) and to `12_verify_sync.INFRA`.
- Events emitted, by script:

  | script | events |
  |---|---|
  | `hfss_spec/session.py` | `phase.declared` (in `start()`), `phase.refused` (module `require()`, detail `action=<a>: <refusal>`), `budget.escalate` (`budget_verdict(state_dir=…)`, which `scripts/session.py` now passes) |
  | `hfss_spec/compiler.py` | `stage.start` / `stage.end` per Spine stage via `BuildLog(state_dir=…)`; the end's verdict is that stage's own `PASS:` line, or `FAIL: <stage> <Exc>: …` when it raised (then re-raised) |
  | `scripts/compile_spec.py` | `compile.start`, `compile.end` (verdict = the printed summary / `STAGE_FAILED:` line, with `duration_ms`); `gate.compile_spec` for `--dry-run` |
  | `scripts/tier0.py` | `gate.tier0` — only with the new `--workspace` (tier 0 has no workspace of its own) |
  | `scripts/tier1.py` | `stage.start` / `stage.end` per staged script (verdict = its Verification line as `PASS: …`, or `FAIL: <script> <last output line>`), `gate.tier1` (also for `--dry-run`) |
  | `scripts/validate_spec.py`, `scripts/precheck.py` | `gate.validate_spec`, `gate.precheck` — the summary / verdict line; new `--workspace`, defaulting to the spec's own directory (a spec under `knowledge/cases/` has no state dir, so nothing is written) |
  | `scripts/record_outcome.py`, `scripts/record_gate.py` | `outcome.recorded`, `gate.recorded` |
  | `scripts/run_card.py` | `card.written` (both the run and the single-session path) |
  | template `ws_common.py` | `desktop.attach` / `desktop.launch` with `port=<p> pid=<pid>` (a stale pin re-pinned says so), `desktop.recycle` (the recycle note), `teardown` (aborted-no-pin / refused-unbanked / `verdict=… close_projects=… port= pid= gone=`) |
  | template `08_solve.py` | `solve.submitted` (verdict = the `PASS:` line; detail carries setup, gate instant, watchdog pid), `solve.refused` (the `FAIL:` line) |
  | template `poll_solve.py` | `solve.terminal` — the terminal progress line **verbatim** as detail, with the watchdog's elapsed as `duration_ms`; the tick log stays in `solve_progress.txt`. `main()` split into `run(project, state_dir, cfg, sleep, process_alive)` so a test can drive a real tree to its terminal line |
  | template `confirm_solve.py` | `solve.banked` (the `PASS:` line), `solve.unbanked` (the abort line) |
  | template `capture_state.py` | `snapshot.captured` |
  | template `12_verify_sync.py`, `verify_spec_replay.py` | `sync.verify` — every terminal verdict line (`PASS: sync replay matches snapshot`, every `FAIL:` form) |
  | template `read_results.py` | `readout.attempt` from `ReadoutSession.read` — `expression=… route=<token> error_class=<Exc or -> points=<n>`; `error_class()` takes the first `*Error` / `*Exception` the note names |

- `skill/hfss-agent/reference/execution.md`: the Verification contract's new
  bullet ("Every `PASS:` / `FAIL:` line is also an event …"), enforced by a
  new `verify_skill.py` marker (`event log`) plus an existence check for
  `hfss_spec/events.py`.
- Tests: `hfss_spec/test_events.py` (27, tier 0 `events`): the module's
  rules; session events; the compiler's pairs and the failing-stage pair;
  `compile_spec.main` end to end with `load_ws_common` faked and `os._exit`
  turned into `SystemExit` (compile.start, 9 pairs, compile.end with the
  printed line; the clarify refusal; run_id/phase stamped in a build
  session); the gates, recorders, tier1 (dry-run and a two-script run with
  one failing), `run_card --transcript` on ticket 04's real Claude Code
  slice. `src/test_run_events.py` (20, tier 0 `run-events`): the shim; the
  **solve session in order from the real runners** — `08_solve` (its own
  attach) → the watchdog run to completion on the materialized
  `pilot-normal` tree with the real `DV3019_S1911_V2586.profile` slice
  landing mid-run → `confirm_solve` → `teardown` — asserting
  `[desktop.attach, solve.submitted, solve.terminal, solve.banked,
  teardown]`, the terminal detail equal to the last `solve_progress.txt`
  line, the banked verdict equal to the printed line; the stalled/unbanked
  pair; refusal; launch, recycle and stale-pin details; teardown aborted and
  refused; `capture_state`; `12_verify_sync` PASS against a real captured
  snapshot (`knowledge/cases/_snapshots/horn-10ghz.json`) with the replay
  subprocess faked, and its FAIL lines; `verify_spec_replay`'s two FAIL
  lines; both readout routes.

Two things the tests found, both fixed:

- **`ws_common.teardown()` re-imported `Desktop` locally**
  (`from ansys.aedt.core import Desktop` inside the function), bypassing the
  module-level name every no-AEDT test fakes. The first run of the sequence
  test launched a real 2024 R1 desktop for 13 s and released it. Teardown
  now uses the module-level `Desktop` like `attach` / `recycle_desktop`, and
  `test_run_events` puts a refusing stand-in for `ansys.aedt.core` in
  `sys.modules` so any such path fails loudly instead of costing a seat.
- `hfss_spec/acceptance.py` loads `12_verify_sync.py` by file path with
  `src/` off `sys.path`; `12_verify_sync` now falls back to loading
  `run_events` by path beside itself.

**Tier 1, honestly:** the checkbox is ticked on the offline proof only. The
compiler over the canonical `patch-2400` spec against `FakeHfss` leaves
exactly `[stage.start, stage.end] × 9` in Spine order with the `PASS:`
lines as verdicts, and `compile_spec.py` end to end brackets them with
`compile.start` / `compile.end`. What has not run is the same command on a
live desktop (`python scripts/compile_spec.py --workspace … --spec … --launch`
in a declared build session, then read `results/state/events.jsonl`); the
`desktop.attach` / `desktop.launch` port and pid on a real `ws_common` is
the one line the fakes cannot vouch for. No AEDT was launched on purpose
for this ticket.

Also not done: `report.written` (no `run_report.py` until ticket 06);
opencode-side nothing changes (host-neutral). `run-events` costs ~15 s of
tier 0, almost all of it three materializations of the 495 MB pilot tree.

Verification, verbatim:

- `PASS: events tests=27 failed=0`
- `PASS: run_events tests=20 failed=0`
- `python skill/hfss-agent/verify_skill.py` → `ALL PASS`
- `PASS: verify_agents agents=2 failed=0`
- `PASS: static_gate compiled=17 imported=16`
- `PASS: run_events repo_root=<checkout> state=<template>/results/state logger=found`
- `PASS: tier0 suites=19 failed=0 elapsed=38.3s` (with `python hfss_spec/test_hfss_spec.py` → `PASS: hfss_spec tests=95 failed=0` after the `acceptance.py` fix)
- CLI smoke on a temp workspace (all six lines landed in its `events.jsonl`
  with `run_id=ws-2026-09-02`, `phase=build` and the script name as
  `argv0`):
  `PASS: session declared phase=build name=smoke budget=60 host=opencode session_id=quiet-owl run=ws-2026-09-02 declared=1`;
  `PASS: validate_spec errors=0 warnings=2`;
  `PASS: precheck recipe=inset-fed-rectangular-patch verdict=consistent`;
  `PASS: compile_spec dry-run spec=patch-2400 escape_hatch=0`;
  `PASS: record_gate gate=1 verdict=pass recorded=1 file=…\review_gate.txt`;
  `PASS: record_outcome outcome=escalated completions=0 file=…\outcome.txt`;
  `PASS: ok: session phase=build calls unaccounted (no trace) budget=60`.
