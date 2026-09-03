# 05 — Pain-point classifiers

**What to build:** `hfss_spec/painpoints.py`: pure functions that take the
steps (ticket 04), the events (ticket 03) and the machine state of one run,
and return findings. A finding is `{kind, severity, phase, stage, cost_tokens,
cost_wall_ms, steps: [seq...], evidence: one line, fix_hint}`. No I/O in the
classifiers; `run_report.py` feeds them.

First, **attribution**: assign every step a phase (from its session's
declaration in `sessions.jsonl`) and a stage (the last `stage.start` event
before it, or `between-stages`). Everything below reports cost by that.

Classifiers, one per spec pain class, with the threshold as a named constant:

| kind | rule | evidence line |
|---|---|---|
| `heavy_output` | tool result > 8 KB | tool, command, bytes, how many later steps it stayed in context |
| `long_reasoning` | reasoning block > 4 KB | bytes, the step's tool |
| `whole_file_read` | `cat`/`Get-Content`/Read of `solve_progress.txt`, `*.log`, `verify/*` without `tail`/`-Tail`/`head` | command |
| `recursive_listing` | `ls -R`, `Get-ChildItem -Recurse`, `find` over KB or workspace | command, bytes |
| `retry_same_command` | same normalised command ≥ 2 times in a stage | count, first and last seq |
| `identical_error_twice` | consecutive tool results with the same error signature | signature |
| `rebuild_chain` | `compile.start` ≥ 2 in one build phase | count, what changed between (from `stage.end` verdicts) |
| `foreground_poll` | ≥ 3 tail/status reads of the same state file within 60 s, or `sleep` loops in bash | count, span |
| `probe_script` | `python -c` or a write to a file named `*probe*`/`*tmp*` under `src/` | command |
| `idle_gap` | ≥ 5 min between steps; classified `user_wait` if the next step is a user message, `solver_wait` if inside `solve.submitted`..`solve.terminal`, else `unexplained` | span, class |
| `escalation` | user messages containing a question from the agent's previous turn; `phase.refused`; `budget.escalate` | the question, one line |
| `late_declaration` | `desktop.launch` or `solve.submitted` before the phase's `phase.declared` | events |
| `undeclared_session` | a session in the store with no declaration | session id |
| `backend_error` | `GrpcApiError`/`AEDTRuntimeError` in a tool result, grouped by AEDT command (`GetVariables`, `Subtract`, ...) | command, count, stage |
| `desktop_recycle` | `desktop.attach` port or pid changes within a phase | old → new |
| `design_misroute` | `Active Design set to X` in a tool result differing from the spec's declared design | X vs declared |
| `solve_anomaly` | watchdog terminal `stalled`/`aborted`; `solve.submitted` count > 1 | terminal line |
| `unbanked` | `solve.terminal complete` with no `solve.banked` | — |

Severity is by cost: `high` if the finding's attributed tokens exceed 5 % of
the run or its wall exceeds 15 min; the rest `medium`, with `low` reserved
for discipline findings that cost nothing this time.

The DESIGN-misroute and readout-failure classes are there because
`patch-array-5800` had both, and today only the ledger knows.

**Blocked by:** 03, 04.

**Status:** ready-for-human

- [x] Every classifier has a positive and a negative test on captured fixtures (no synthetic-only fixtures) — see the provenance table in Comments; three classifiers have no real positive on this box and are tested synthetic-beside-real, named as such
- [x] Attribution: a step-count-by-stage table for the fixture run matches a hand count
- [x] Findings carry cost; the sum of attributed tokens does not exceed the run total
- [x] The two DESIGN misroutes and the six-desktop readout failure in `patch-array-5800` are found from its transcripts and state, without the ledger — one misroute confirmed, the other surfaced as `POSSIBLE` on the trace as shipped (confirmed once the trace carries full commands); the readout failure from the state files plus the 33 desktop kill loops of the 09-01 session. Details and the one caveat in Comments.

## Comments

### 2026-09-02 — landed

What landed, by file:

- `hfss_spec/painpoints.py` (new, stdlib only, no I/O): `attribute(steps,
  events, history)`, the eighteen `find_<kind>` classifiers of the table,
  `analyze(steps, events, history, machine_state)` (findings costed, graded,
  heaviest first) and `stage_table(steps, events, history)` (rows
  `{phase, phase_index, stage, stage_source, start, wall_ms, steps, tokens,
  script_runs, fails, retries}`). Every threshold is a named constant
  (`HEAVY_OUTPUT_BYTES`, `LONG_REASONING_BYTES`, `RETRY_MIN`, `REBUILD_MIN`,
  `FOREGROUND_POLL_MIN` / `_WINDOW_MS`, `IDLE_GAP_MS`, `HIGH_TOKEN_SHARE`,
  `HIGH_WALL_MS`, `LOW_TOKEN_SHARE`, `LOW_WALL_MS`, `ROUTING_FILE`,
  `COMMAND_CHARS`). A finding is `{kind, severity, phase, stage,
  cost_tokens, cost_wall_ms, steps, evidence, fix_hint}` plus `session` and
  `source` (`trace` / `events` / `state`). `machine_state` is
  `{file name: text}` for `results/state/` (`STATE_FILES`); the caller reads
  the files.
- **Attribution.** Phase = the latest declaration at or before the step that
  names its session or its parent's, from three sources merged:
  `sessions.jsonl`, `phase.declared` events, and — because the real run
  predates both — the `scripts/session.py --phase X` commands in the trace
  itself. A phase re-declared within 10 s is one cluster and the cluster's
  LATEST instant governs (solve-1b: the 22:29:16Z declaration ran in a
  command whose cwd broke it; 22:29:25Z landed). A session's steps before
  its own first declaration are backfilled to that phase (`phase_source =
  backfill`); a session no declaration reaches stays `undeclared`. Stage =
  the event window containing the step's tool call (`compile.start` ..
  `compile.end`, `solve.submitted` .. `solve.terminal`, `stage.start` ..
  `stage.end`; the compiler's own `stage.start` sub-stages stay `compile`;
  the point events snapshot / sync.verify / gate.* / readout.attempt /
  card.written are zero-length windows), else `between-stages`. With no
  stage events at all, shell calls get a stage read off the command
  (`stage_hint`) and every step says `stage_source = commands`, so ticket
  06 can label the fallback.
- **Cost.** `cost_tokens` = billed tokens of the requests the finding's
  steps belong to (a tool_result borrows its tool_use's request);
  `attach_costs` lets a request count once per kind, heaviest finding
  first, so per-kind sums never exceed the run (tested). `idle_gap` costs
  wall only. Severity: `high` above 5 % of the run's tokens or 15 min of
  wall; `low` for a discipline kind under 0.5 % and 60 s; else `medium`.
- `hfss_spec/test_painpoints.py` (67 tests, tier 0 suite `painpoints`).
- `scripts/tier0.py`: the suite registered after `run-events`.
- `scripts/fixtures/patch-array-5800/capture.py`: now also captures every
  top-level file of `results/state/` into `state/` (13 files, byte for
  byte, sha256 in `index.json`; `verify/` and `zact_export/` excluded);
  byte-stable on rerun; the main checkout untouched.

Per-classifier fixture provenance (real = a shipped slice or the captured
state; synthetic-beside-real = a copy of a real step with one field changed
through `_variant`, which asserts the key set is `run_trace.STEP_KEYS`, or a
record from the real writer — `events.record`, `session.history_record`,
`poll_solve.format_progress`):

| kind | positive | negative |
|---|---|---|
| `heavy_output` | real: neon-eagle (19; `physics.py` 27,707 B; `spine-api.md` in context for 883 later steps), f0c832a3 (2) | real: a0e9c38f's text-only subagents |
| `long_reasoning` | real: neon-eagle (31 blocks, largest 60,572 B); f0c832a3 (estimated from `tokens_reasoning`, Claude Code stores no thinking text) | real: hidden-falcon |
| `whole_file_read` | real: hidden-falcon's `read` of the whole `solve_progress.txt` (19,295 B) | real: the main session's `-Tail` reads; plus a `cat`-without-tail variant |
| `recursive_listing` | real: f0c832a3 `ls -R`; neon-eagle `Get-ChildItem -Recurse` (seq 50, 62, 84) | real: hidden-falcon |
| `retry_same_command` | real: `capture_state.py` twice in `snapshot` | real: f0c832a3 |
| `identical_error_twice` | **no real positive on this box** (errors are never consecutive); synthetic-beside-real: the real failed read (seq 39/40) duplicated | real: neon-eagle, f0c832a3 |
| `rebuild_chain` | real: build #1 (3 compiles), #3 (5), #5 (5); events path synthetic-beside-real | real: f0c832a3 |
| `foreground_poll` | real: `Start-Sleep -Seconds 240` (wall = the declared 240 s); **≥3 reads in 60 s has no real positive** — synthetic-beside-real from the real `-Tail 1` step | real: no such window in neon-eagle |
| `probe_script` | real: 19 in build #1 (11 `python -c`, 8 `Temp\opencode\probe_*.py`) | real: hidden-falcon |
| `idle_gap` | real: 5 gaps, all `user_wait` (71 / 37 / 22 / 10 / 6 min); `solver_wait` / `unexplained` **have no real positive** — synthetic-beside-real inside watchdog run 1 | — |
| `escalation` | real: 12 user replies after the agent stopped; events synthetic-beside-real | real: f0c832a3 |
| `late_declaration` | real: state + trace, below | real: no state; events synthetic-beside-real |
| `undeclared_session` | real: f0c832a3 | real: neon-eagle and its subagents |
| `backend_error` | real: `readouts.txt` ×2 + `z_act.txt` ×1 = `GetVariables x3`, `route=both-failed` | real: the trace carries no output text; output-head variant synthetic-beside-real |
| `desktop_recycle` | real: `Stop-Process -Id 29756` (seq 761, the mid-run recycle) + the two pin moves `readouts.txt` records (55583 -> 64077, 57850/25840 -> 64077/29620) | real: f0c832a3; events synthetic-beside-real |
| `design_misroute` | real: confirmed at seq 568 -> edit 596 -> 599/603 (build-2); `POSSIBLE` at 743 (build-3) and 401 | real: f0c832a3 |
| `solve_anomaly` | real: 3 submissions (three watchdog runs, all `complete`); stalled line from the real formatter | real: no state |
| `unbanked` | real state minus `solved.txt` (3 unbanked completes); events synthetic-beside-real | real: every complete was banked |

Hand count (attribution): the seven declarations sit at seq 149, 245, 473,
536, 652, 740, 822 of the 908-step main session; the phase instances
therefore hold 245+16 (cosmic-knight), 228, 63, 116, 88, 82, 86+30
(hidden-falcon) steps — `attribute` reproduces exactly that, 149 of them
`backfill`. Stage rows for the build compiles hold 2 x the compile calls
and `script_runs` = the calls; `snapshot` in build #1 shows `retries=1`.

Acceptance check, run against the REAL stores (opencode DB read-only for
`ses_fe9ae6dd3ffe2a8knbeE1b4yrr` = neon-eagle; Claude Code projects dir for
`e5cdcdf5-e3fe-4a62-9402-0e4010171c51`, the 2026-08-31/09-01 session with
its 11 subagents; machine state from the main checkout's `results/state`):

- `PASS: run_trace sessions=3 steps=954` (neon-eagle), `PASS: run_trace
  sessions=12 steps=3152` (e5cdcdf5).
- **DESIGN misroute #1 (build-2, 21:47Z): FOUND, confirmed** — `design.yaml
  compiled at seq 568 under the DESIGN ws_common.py named before its edit
  at seq 596, then again at seq 599`.
- **DESIGN misroute #2 (build-3, 22:51Z): FOUND as `POSSIBLE`** — `POSSIBLE
  misroute: 2 compile(s) whose --spec the 200-char command cut lost, then
  design.yaml, compiled at seq 743 ... edit at seq 791, then again at seq
  794`. The three fed compiles before the edit (22:51:26, 22:52:38,
  22:53:40) are all cut at 200 chars before their `--spec`, so the rule
  cannot confirm the spec. A third `POSSIBLE` at seq 401 is NOT a misroute:
  its command is cut exactly where `--dry-run` began. Re-running with the
  full commands read from the store (variant C of the probe) gives
  **exactly the two misroutes, both confirmed, no POSSIBLE**; the same
  variant with 2 KB output heads adds 5 `backend_error` groups from the
  trace itself (`GetVariables x4`, `GetPropValue x4`, `Subtract x2`,
  `GetPropertyValue x2`, `GetDesignNames x1`). This is the trace's gap, not
  the rule's; the rule was not weakened.
- **Readout failure across the desktops: FOUND** — `backend_error`:
  `GrpcApiError GetVariables x3 quoted by readouts.txt x2, z_act.txt x1
  (readouts.txt: route=both-failed)`; `desktop_recycle`: the two pin moves
  above from `readouts.txt`; and in the 09-01 session 33 `desktop_recycle`
  findings, one per `for i in 1 2 3; do taskkill //IM ansysedt.exe //F`
  loop (the ledger's "6+ independently launched desktops" is a lower
  bound), plus one `foreground_poll` of 33 sleeping calls, 27 min of wall.
  The count comes from the kill commands, not from launch output.
- Also found without the ledger: the mid-run desktop recycle (`Stop-Process
  -Id 29756`, build-3, seq 761); the late solve declaration (`solve
  submitted 2026-08-18T22:29:16Z (watchdog_started=1787092156) in phase
  build, 9 s before the solve declaration at 2026-08-18T22:29:25Z`); the
  09-01 session as `undeclared_session` (1341 steps, 372,020 tokens — it
  declared through no visible `session.py --phase` command); the run's
  biggest sink is reasoning (28 % of tokens in 31 blocks over 4 KB) and
  its longest wall a 71-min gate wait.
- Analyzing the 09-01 session ALONE also reports the three Aug 18 watchdog
  runs as `late_declaration` "with no solve declaration at all", because
  that family holds none; pooled with neon-eagle (what `run_report.py` will
  do) the declarations cover them. Ticket 06 should analyze a run's
  sessions together.

Rule deviations from the ticket table, stated: `probe_script` counts a
probe/tmp file anywhere, not only under `src/` (every real one lived in
`%TEMP%\opencode\`); `design_misroute` is the command-level signature
above, with the `Active Design set to X -> Y` names quoted when a step
carries `output_head`; `escalation` uses "a user turn after the agent
stopped" as the question proxy, since the trace has no text; `identical_error_twice`
signatures fall back to the command when there is no error text;
`long_reasoning` on Claude Code is `tokens_reasoning x 4` because the
thinking text is not stored.

What the trace should carry (for ticket 04's owner / a follow-up):

1. The full command, or at least 400 chars: the 200-char cut hid
   `--dry-run` (seq 401), `--spec` (743, 750, 757, 565) and the tail of
   `design_elements.yaml` (784).
2. A tool-output head (~2 KB): `Active Design set to`, `GrpcApiError ...
   command: X` (11 in neon-eagle), `PASS:` / `STAGE_FAILED:` lines.
3. An edit's old/new heads (the `DESIGN = "ElementsOnly" -> "PatchArray"`
   edits would turn the misroute signature into a direct read).
4. The opencode tool_use timestamp: `run_trace` uses `state.time.start`,
   which opencode writes at completion (start and end ~30 ms apart; the
   `Start-Sleep 240` call reads 32 ms); the real start is the part row's
   `time_created` (241 s for that call). Until then every opencode call
   measures ~0 wall and the sleep classifier reads the declared seconds.

Verification, verbatim:

- `PASS: painpoints tests=67 failed=0`
- `PASS: tier0 suites=20 failed=0 elapsed=39.6s`
- `python skill/hfss-agent/verify_skill.py` -> `ALL PASS`
- `PASS: capture patch-array-5800 fixtures state.session1.md=4231 outcome.txt=155 state/aedt_port.txt=5 state/aedt_process_id.txt=5 state/completions.txt=6 state/model_snapshot.json=3333 state/outcome.txt=155 state/readouts.txt=2523 state/session.json=159 state/solve_progress.txt=18916 state/solve_started.txt=18 state/solve_watchdog_pid.txt=5 state/solved.txt=66 state/z_act.txt=108` (twice, byte-stable)

### 2026-09-02 — misses from the acceptance run (ticket 10)

Graded against `docs/hfss-agent-performance-analysis.md` sections 2–3,
which describe `playful-river` (bowtie-3670, `ses_03a8008c2ffeEN5jJusT7PyFuO`,
625 steps traced from opencode.db; report rendered on a temp copy with
`--session`). Two misses, one small fix made and re-graded:

1. **`rebuild_chain` sees only `compile_spec` calls.** The doc's "three full
   clean rebuild chains (teardown → wipe project → rerun stages 01→04)" in
   steps 46–89 are staged scripts run by hand — the run predates the
   compiler — and the report shows only `retry_same_command`: `x2 in
   between-stages: python src\02_geometry.py 2>&1 (seq 232..251)`. What the
   classifier should match: the same ordered run of `src/0N_*.py` scripts
   (01 → 02 → 03 → 04) repeated ≥ `REBUILD_MIN` times in one phase, with the
   files edited between as the evidence, exactly as the compile form does.
   Every pre-compiler run (playful-river, silent-engine) has this shape.
2. **The sync saga has no finding of its own.** Steps 89–125 (introspect →
   diff → amend → verify in a second desktop, twice, both desktops killed)
   surface only as parts: `retry_same_command` `x3 in between-stages: python
   src\diag_sync.py 2>&1 | Select-String … (seq 402..476)`, `desktop_recycle`
   at seq 567 (below), `identical_error_twice` `RedirectStandardError at
   seq 591 and 595`, and a 79,472 B reasoning block. What it should match:
   a verify / diag script (`diag_sync`, `12_verify_sync`, `verify_spec_replay`)
   run ≥ 2 times in one phase with a kill or launch between its runs — one
   finding whose wall spans the first run to the last, costed like a chain.
   On a post-ticket-03 run the `sync.verify` events give the same window.
3. **Fixed here, re-graded FOUND:** `find_desktop_recycle` required
   `ansysedt` in the kill command; playful-river killed by pid and checked
   `Get-Process | Where-Object { $_.Name -match "ansys" }` (seq 567), so the
   two desktops the doc says died were invisible. `ANSYSEDT_RE` now also
   accepts `\bansys\b`; the real step is
   `scripts/fixtures/opencode/ses_03a8008c2ffeEN5jJusT7PyFuO.steps-slice.jsonl`
   (`TestDesktopRecycleByPid`), neon-eagle's kills unchanged, a `python -c
   "import ansys.aedt.core"` variant stays negative.

Not a miss, noted: the doc's output sizes (89–90 KB listings, 43.9 KB grep)
are store-part bytes; the trace's `out_bytes` is the output text, so the
same steps read `51,315 B` and `20,445 B` in the report.
