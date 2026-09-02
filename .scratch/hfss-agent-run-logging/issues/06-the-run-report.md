# 06 — The run report

**What to build:** `scripts/run_report.py --workspace W`, which runs the trace
(ticket 04) if it is stale, loads events and machine state, runs the
classifiers (ticket 05), and writes two files next to `summary.md`:
`run-report.md` for people and `run-report.json` for the index and the
`runcard` subagent. Both are tracked (the workspace `results/` directory is
gitignored; `summary.md` is not, and the report follows it).

`run-report.md`, in this order, two pages at most:

1. **Headline** — outcome, completions, billed per completed simulation,
   raw wall, active wall, tokens by phase session and by subagent, step count
   by phase. Every number machine-derived or marked `unmeasurable: <reason>`.
2. **Top pain points** — the ten highest-cost findings, one line each:
   cost, kind, stage, evidence, fix hint. This is the section the acceptance
   test reads.
3. **Stage timeline** — one row per stage: start, wall, steps, tokens, runs
   of a script, fails, retries. Between-stage time shown as its own row.
4. **Waiting** — idle gaps by class; total user-wait, solver-wait,
   unexplained.
5. **Retries and rebuilds** — every retry loop and rebuild chain with what
   changed between attempts.
6. **Context** — the ten heaviest outputs and ten longest reasoning blocks,
   with the command and how long each stayed in context.
7. **Backend** — errors by AEDT command, desktop recycles, readout routes.
8. **Solve** — from the watchdog: mesh, adaptive and sweep durations,
   submissions, terminal line, bank status.
9. **Discipline** — late declarations, undeclared sessions, probes, polls.
10. **Versus previous runs** — the index rows (ticket 07) for the last five
    runs of the same recipe, same columns as the headline.
11. **The run card**, unchanged, as the last section (call `run_card.summary_section`).

`run-report.json` holds the same content as data: headline, findings, stage
rows, gaps, index row. Nothing in the markdown is computed a second time.

The report never opens a transcript for content; it reads `steps.jsonl`, so
it stays cheap to regenerate and safe to commit.

**Blocked by:** 05.

**Status:** ready-for-agent

- [ ] One `PASS: run_report ... findings=N` line; exit 1 only on a missing workspace
- [ ] Byte-idempotent: running twice yields the same files (the `upsert_summary` discipline)
- [ ] Every `unmeasurable` in the headline names its reason, matching `run_card`'s wording
- [ ] Rendered on the `patch-array-5800` workspace and on `bowtie-3500-pilot`; both committed as the first two reports
- [ ] `verify_skill.py` asserts the script and both output files' names
