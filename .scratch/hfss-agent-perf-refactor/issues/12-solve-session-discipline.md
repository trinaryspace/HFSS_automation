# 12 — Solve-session discipline: resolve-once, live pin, ledger state

**What to build:** The five-submission failure class ends. After any solve anomaly (stall, abort, false tick) the agent reads the evidence exactly once — the watchdog's terminal line, the newest solve profile's status, and the counts — then escalates to the user with that evidence; re-submission happens only on the user's explicit go after that escalation, or on a user-approved model-state change (Clarification-locked corrections, Review-gate edits) that legitimately invalidates a solve. Resuming a session checks the pinned desktop with a bounded connect instead of a hanging attach: a stale pin is cleared and re-pinned, never probed. The State ledger gains a live-state block — desktop pin, solve status, solved marker pointer, next action — and the solve session appends one delta per decision (submission number, reason, user's answer), so a resumed session and the run card can attribute every submission.

**Blocked by:** None — can start immediately.

**Status:** ready-for-human

- [x] Execution text states resolve-once and the two legal re-submission routes (anomaly + user go; user-approved state change)
- [x] Resume against a dead pinned desktop fails fast with a clear stale-pin message and re-pins without hanging
- [x] Solve session appends one ledger delta per decision (submission number, reason, user's answer)
- [x] Run card can attribute every submission to a user-approved reason

## Comments

- 2026-08-07 (ticket 12, solve-session discipline): New section `## Solve-session
  discipline: resolve-once + live ledger` in `skill/hfss-agent/reference/execution.md`
  (started after Batch-1 landed — ticket 14's completion rule was already in the
  solve section; template test suite + static gate were green before this change),
  plus the bounded-connect attach path in the template's `src/ws_common.py` and a
  new no-AEDT `TestStalePin` suite in `test_template_runners.py`.
- **Resolve-once (execution.md §Solve-session discipline).** After ANY solve anomaly
  (stalled/aborted watchdog line, engine-error profile verbatim, false tick, dead
  watchdog, resume against a changed world) the agent reads the evidence exactly
  once — watchdog terminal line + newest profile terminal Status (verbatim) +
  counts — then escalates to the user; re-submission is legal only through the two
  routes: (1) the user's explicit go after that escalation, (2) a user-approved
  model-state change (Clarification-locked corrections, Review-gate edits via
  read-back sync) that legitimately invalidates the solve. Anything else is "a
  discipline violation, not a retry."
- **Ledger practice (documented in execution.md only — state.md template untouched).**
  One delta per solve decision, `solve #<n> — reason: <evidence>; user: <answer
  verbatim>`, plus a ≤ 4-line live-state block (pin probed/re-pinned; solve status =
  last terminal line; solved marker = `results/state/solved.txt` present + `status=`;
  next action). Session-1 ledger line amended so the Solve+QA session "reads **and
  amends**" the ledger. Run card attribution path: the deltas live in `state.md`,
  which the runcard subagent drafts from (run_card.py also reads the machine marker
  `solve_submitted_at.txt` — attribution is ledger delta + machine marker, no gap).
- **Bounded connect (ws_common.py).** `STALE_PIN_TIMEOUT = 2.0` + `_pin_probe(port)`
  — pure-socket TCP connect with `settimeout`, no AEDT, no launch side effects.
  `attach(launch=False, probe=...)` (probe injectable for tests) runs the probe
  before any pinned attach: a dead pin prints
  `stale pin: aedt_port=<n> has no live desktop ... clearing the pin and re-pinning
  (no hanging attach)`, is cleared (`aedt_port` + `aedt_process_id` → 0), and the
  attach branches into a fresh pinned launch. A stale pin is never handed to a
  pyAEDT attach (the pilot's hang/spawn class) — it is cleared and re-pinned, never
  attached against. Launch and no-pin paths are unchanged and never probe.
- **Verification (no AEDT anywhere).** Template tree: `test_template_runners.py`
  54/54 (47 prior + 7 TestStalePin), `test_poll_solve_stages.py` 18/18, static gate
  `PASS: static_gate compiled=9 imported=8`, py_compile clean. TestStalePin proves
  the route and the verdict: dead-pin probe → stale-pin print, zero attaches, one
  fresh launch, pin re-written from the fresh desktop (61234/4242); live pin →
  pinned attach only, pin untouched; no pin → attach-anywhere, probe not called;
  the socket seam is mocked for the timeout path (`socket.timeout` → False with
  `settimeout(STALE_PIN_TIMEOUT)` and the exact addressed port asserted). Real
  socket smoke on this box: live port → True in 0.6 ms; closed-after-bind port →
  False in 2.006 s (the bound's real timeout path, not a hang). Pilot workspaces
  untouched; other batch-1 work (t13/t14 files, ADR 0006, SKILL.md, poll_solve,
  confirm_solve, teardown) not modified.

**Status:** ready-for-human
