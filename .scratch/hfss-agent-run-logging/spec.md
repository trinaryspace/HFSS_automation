# Run logging: see exactly where a run hurt, after it is over

Written 2026-09-02 from a read of the code and of `workspaces/patch-array-5800`
as it stands on disk. Every gap named below was observed there, not inferred.

## The goal, in one sentence

After a run finishes, one command produces one report that says where the
tokens, the wall time, the retries and the escalations went — by phase, by
Spine stage, and by kind of pain — without anyone re-reading a transcript.

## Why the current logging cannot answer that

The repo already measures runs, but at the wrong grain and from inputs the
agent has to remember to write. What exists:

| Layer | Where | What it gives | What it cannot give |
|---|---|---|---|
| Harness session stores | `~/.local/share/opencode/opencode.db` (11 GB); `~/.claude/projects/*/<id>.jsonl` | Every step: tool call, tool result, tokens per request, timestamps. Complete. | Nothing in the repo reads them below the session total. |
| Run card | `scripts/run_card.py`, `scripts/claude_transcript.py` | ~19 session totals; cost per completed simulation; verdict vs two hardcoded baselines | Per-stage or per-step anything. Reads ONE session; a run is three sessions plus subagents. |
| Machine state | `workspaces/<name>/results/state/*.txt` | Watchdog tick log (`solve_progress.txt`), bank status, pinned desktop, declared phase, readout route | Stage boundaries for the build; anything before the solve; survives only on disk (gitignored). |
| Ledger + summary | `state.md`, `summary.md` | The human narrative of what went wrong | Hand-written, so it is exactly as complete as the agent's memory at the time. |
| Campaign notes | `.scratch/hfss-agent-parallel-tests/*.md`, `docs/hfss-agent-performance-analysis.md` | The one deep step-level analysis ever done | Produced with throwaway probe scripts in `%TEMP%` that were never checked in. |

And what the last run's record actually looks like, which is the case for
this spec:

- Its `## Run card` reads `outcome: unrecorded`, `active_wall: unmeasurable`,
  and describes a **20-second** session (`hidden-falcon`), not the run.
- `results/state/outcome.txt` holds free text (`completed - user verdict: ...`);
  the parser wants `outcome=completed`, so the outcome is lost.
- `results/state/solve_submitted_at.txt` is empty. Nothing in the repo writes
  it (campaign runbook defect D2), so active wall can never be measured.
- The ledger's `- Started:` line has trailing text; `run_card.ledger_start_ms`
  rejects it. Second reason active wall is unmeasurable.
- `results/state/session.json` was overwritten by the 2026-09-01 readout
  experiment and now carries no `host` / `host_session_id`. The run's own
  three phase sessions are no longer findable from the workspace.
- `calls: 0` against a budget of 60: `note_call` is never invoked, so the
  budget measures nothing.
- The pain points a maintainer would want to see — two DESIGN-constant
  misroutes forcing rebuilds, six desktop launches failing the readout, a
  stale live-state block, a late phase declaration, a mid-run desktop
  recycle — exist only because the agent wrote them into `state.md` by hand.

## What "pain point" means, concretely

The report must surface these nine classes. Each is detectable from data the
repo can already collect or will collect under this spec.

1. **Time and token sinks by stage** — wall, steps, tokens for each phase and
   each Spine stage (compile, snapshot, gate, sync-verify, solve, readout,
   summary), so the heaviest stage is the first line of the report.
2. **Retry loops** — the same script or command run ≥2 times, the identical
   error twice in a row, rebuild chains, self-correction cap hits.
3. **Context bloat** — tool outputs above a size floor, reasoning blocks above
   a size floor, whole-file reads of `solve_progress.txt` or verify logs,
   recursive listings.
4. **Waiting** — idle gaps, split into user-gated (Review gate, questions),
   solver time, and unexplained.
5. **Escalations and corrections** — questions asked, user verdicts, gate
   fixes requested, phase re-declarations.
6. **Discipline violations** — phase declared after a launch, undeclared
   session, foreground polling, `python -c` probes, DESIGN-constant
   misroutes, budget unaccounted.
7. **Backend failures** — `GrpcApiError` by AEDT command, desktop recycles
   (pin changes), readout route outcomes.
8. **Solve lifecycle** — stage durations from the watchdog, stalls,
   re-submissions, banked vs unbanked.
9. **Outcome and cost** — outcome, completions, billed per completed
   simulation, and the same numbers for every previous run.

## Architecture: three sources, one trace, one report

```
harness stores ──► scripts/run_trace.py ──► steps.jsonl (per session, incl. subagents)
                                                   │
repo tooling ───► hfss_spec/events.py ───► results/state/events.jsonl   (stage boundaries,
                                                   │                      verdicts, markers)
                                                   ▼
                                     hfss_spec/painpoints.py  (pure classifiers)
                                                   │
                                                   ▼
                              scripts/run_report.py ──► workspaces/<name>/run-report.md  (tracked)
                                                    ──► workspaces/<name>/run-report.json
                                                    ──► docs/runs/index.jsonl  (one line per run)
```

- **Steps** come from the harness stores, which already hold everything at
  step grain. The repo gains one extractor, not a second logger.
- **Events** come from the repo's own scripts, which are the only place stage
  boundaries and verdicts are known. Every runner that prints a `PASS:` /
  `FAIL:` line also appends it as an event. Machine-written, never
  hand-written.
- **Classifiers** join steps to events by timestamp and phase session, and
  emit findings with a cost attached (tokens and wall). Pure functions over
  JSONL, tested on captured fixtures.
- **The report** ranks findings by cost, and is tracked next to `summary.md`
  so it survives the gitignored `results/` and the disposable worktrees.

## Rules this work inherits

- **Fixture fidelity** (`docs/agents/fixture-fidelity.md`): every parser
  fixture is a slice captured from a real transcript or a real workspace,
  through a capture that refuses a slice that parses differently from its
  source. `claude_transcript.capture` is the model.
- **Machine state is never hand-edited.** Any boundary the report depends on
  is written by a script at the moment it happens, or reported as
  `unmeasurable: <reason>`. Never guessed.
- **Host-neutral.** Both stores feed the same `steps.jsonl` shape; the
  harness table in `skill/hfss-agent/reference/execution.md` is the only
  place a per-host difference is written down.
- **Deterministic first.** No model reads a transcript in v1. The `runcard`
  subagent may narrate `run-report.json` later; it never computes numbers.
- **One `PASS:` line per tool**, tier-0 coverage for every pure part.

## What is deliberately not built

- No external observability stack. The stores are local and complete.
- No live dashboard. The report is post-mortem by design; the watchdog tick
  log already covers "is it alive" during a run.
- No per-step logging from inside the agent's prose. Steps are extracted
  from what the harness already writes.

## Order of work

Tickets 01–03 make the *next* run recordable and cost a few hours. Land them
before any further Tier-2 run, or that run will be as unmeasurable as the
last one. 04 runs in parallel. 05–07 build the analysis. 08 is optional.
09 wires the skill. 10 is the acceptance test: the report, run over
`patch-array-5800`, must independently surface the pain points the ledger
already records by hand.

| # | ticket | blocked by |
|---|---|---|
| 01 | run identity and phase-session history | — |
| 02 | machine-written boundaries and outcome | — |
| 03 | event log from the repo's own tooling | 01 |
| 04 | step trace extractor over both stores | — |
| 05 | pain-point classifiers | 03, 04 |
| 06 | the run report | 05 |
| 07 | runs index and cross-run comparison | 06 |
| 08 | harness hooks for live tool timing (optional) | 01 |
| 09 | wire the report into the skill and the retro | 06 |
| 10 | backfill and acceptance on the last runs | 06 |

## Acceptance for the whole feature

Run `python scripts/run_report.py --workspace workspaces/patch-array-5800`
and read only the top of `run-report.md`. It must name, without help, at
least these five things the ledger already knows: the two DESIGN misroute
rebuilds, the readout failing across six desktop launches, the mid-run
desktop recycle, the late solve-phase declaration, and the readout
experiment overwriting the run's session record. Every one it misses is a
classifier ticket, not a pass.
