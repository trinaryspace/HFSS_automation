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

**Status:** ready-for-agent

- [ ] Every classifier has a positive and a negative test on captured fixtures (no synthetic-only fixtures)
- [ ] Attribution: a step-count-by-stage table for the fixture run matches a hand count
- [ ] Findings carry cost; the sum of attributed tokens does not exceed the run total
- [ ] The two DESIGN misroutes and the six-desktop readout failure in `patch-array-5800` are found from its transcripts and state, without the ledger
