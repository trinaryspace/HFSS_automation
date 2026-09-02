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

**Status:** ready-for-human

- [x] One `PASS: run_report ... findings=N` line; exit 1 only on a missing workspace
- [x] Byte-idempotent: running twice yields the same files (the `upsert_summary` discipline)
- [x] Every `unmeasurable` in the headline names its reason, matching `run_card`'s wording
- [x] Rendered on the `patch-array-5800` workspace and on `bowtie-3500-pilot`; both committed as the first two reports
- [x] `verify_skill.py` asserts the script and both output files' names

## Comments

### 2026-09-02 — landed

**Trace improvements ticket 05 asked for (part 1), by file:**

- `scripts/claude_transcript.py`: `COMMAND_CHARS` 200 -> 8192 (a command
  is carried whole; the longest real one is 1,659 chars), `HEAD_CHARS =
  2048`, `head_of` / `result_text` / `input_head_of`. A slice's `tool_use`
  block gains `input_head` (a write's content head, or `{"old", "new"}`
  heads of an edit's strings; None for every other tool) and a
  `tool_result` gains `content_head`. Re-slicing a slice is still the
  identity; the card check still refuses a mismatch.
- `scripts/run_trace.py`: `STEP_KEYS` gains `input_head` (after `command`)
  and `output_head` (after `out_bytes`); the opencode tool_use `ts` is the
  part row's `time_created` (the emission), the result's `state.time.end`
  — measured: the `Start-Sleep -Seconds 240` call reads 241 s now, 32 ms
  before. Slices carry `input_head` / `output_head`; capture still refuses
  a slice that traces differently. Docstring mapping updated.
- Fixtures recaptured from the real stores and byte-stable on a second
  capture (sha256 checked): `opencode/ses_fe9ae6dd…` (neon-eagle family,
  484 -> 772 KB), `claude-code/f0c832a3-…`, and `claude-code/a0e9c38f-…`
  with its two subagents — whose old slices held **no content blocks at
  all** (their originals have 20 and 18 tool calls); the top-level
  `index.json` now carries their cards too.
- `scripts/test_run_trace.py` (36 tests): the synthetic DB inflates output
  and input heads so it still traces identically to the real slice; new
  tests for whole commands, heads on both hosts, and the
  `time_created` timestamp.
- `hfss_spec/test_painpoints.py` (68): `_variant` accepts `output_head`
  as both a step key and a text key; literals moved to the recaptured
  trace (build declaration at seq 243; `Start-Sleep` at 517 precedes the
  user's mid-sleep message at 518 — so `escalation` reads 11, not 12,
  because that message was typed while a tool ran; probes 20 / 12 in
  build #1; rebuild chains 3 / 4 / 6; a real-steps-under-the-floor
  negative for `heavy_output` since every real session now shows one).
- **Two `hfss_spec/painpoints.py` edits, both constants, no rule
  changed:** `COMMAND_CHARS = 8192` (its documented meaning is "what
  run_trace keeps"; left at 200 it would have marked every whole compile
  command's `--spec` unknown), and the inline `10_000` in `declarations`
  promoted to `DECLARE_CLUSTER_MS = 30_000`: on emission timestamps the
  failed solve-1b declaration (22:29:06, `can't open file ...\scripts\
  session.py`) and the one that landed (22:29:24) are 18 s apart, not 8.
  The docstring paragraph on "what the trace does not carry" now says
  what it does. Follow-up for ticket 05's owner: the failed declaration's
  result now carries its error text and no `PASS: session declared` line,
  which is the honest signal — a declaration whose result is not a PASS
  did not land; that rule would retire the window.

**DESIGN misroute #2: confirmed.** `find_design_misroute` on the
recaptured neon-eagle slice returns exactly two findings and no POSSIBLE:
#1 `design.yaml compiled at seq 568 ... edit at seq 596, then again at seq
599` (build-2) and #2 `design.yaml compiled at seq 743 under the DESIGN
ws_common.py named before its edit at seq 791, then again at seq 794`
(build-3, steps 743..799). Seq 401 is a `--dry-run` gate, as ticket 05
predicted. Also read off the trace now: 7 `backend_error` groups
(`GetPropertyValue x2`, `GetVariables x4` in readout, `Subtract x2` in
compile, `GetDesignNames x1`, `GetPropValue x4`, plus two from
hidden-falcon's `read` of `readouts.txt` / `z_act.txt` — a read that
quotes an error counts as one; for ticket 05's owner), and the `DESIGN =`
edits themselves in `input_head`.

**The report (part 2), by file:**

- `scripts/run_report.py` (new): `--workspace W [--db] [--projects-dir]
  [--session HOST:ID ...] [--top N] [--no-trace] [--index PATH]`. Writes
  `run-report.md` / `run-report.json` beside `summary.md`, the eleven
  sections in the ticket's order; one dict renders both files; byte-
  idempotent (proved on both real workspaces and in the suite); exit 1
  only on a missing workspace; emits `report.written` (filtered out of its
  own analysis). Session discovery, in order: `sessions.jsonl` /
  `session.json` with an id (`declared`); a declaration recorded with a
  name but no id, found as the Claude Code transcript whose own
  `session.py --phase ... --name <name>` tool_use command made it (a
  mention in a prompt or a file read is not a declaration); a slug the
  ledger or summary names, resolved in the opencode DB and walked up
  `parent_id` to its root; `--session`. The trace is refreshed when a
  session's file is missing or older than its store (or `sessions.jsonl`
  is newer than the newest file); a missing store is reported per session
  as `unresolved: <reason>` and the trace on disk is used. Section 10 reads
  `docs/runs/index.jsonl` (same recipe, last five) and says `no index yet`
  otherwise; the JSON carries ticket 07's `index_row`. Section 11 is
  `run_card.run_summary_section` when the workspace has a history, else
  `run_card.summary_section` of a trace-built card whose store-only fields
  (`parts`, `store_bytes`) read `unmeasurable: no store access (trace
  only)`. Findings tables are capped at `--top` with a "N more not shown,
  by kind" line; the patch-array report is 267 lines.
- `scripts/test_run_report.py` (25 tests; tier 0 `run-report`): rendered
  with `--no-trace` on a workspace materialized from the real ledger slice
  + the captured state + a trace written from the neon-eagle slice.
- `scripts/tier0.py` registers the suite; `verify_skill.py` asserts
  `scripts/run_report.py`, both output names and `report.written`.

**Sessions the trace resolved, and how:**

- `patch-array-5800` (state materialized from `scripts/fixtures/
  patch-array-5800/state/`; no `sessions.jsonl`, `session.json` names
  `readout-experiment-2026-09-01` with no host or id):
  `ses_fe9ae6dd3ffe2a8knbeE1b4yrr` = **neon-eagle** with its subagents
  **cosmic-knight** (`ses_fe964cc55ffeHbmOUhRVH9huBi`) and
  **hidden-falcon** (`ses_fe8c117fdffeX8Q8m5QQ6By5Cz`), found from the
  ledger's `slug hidden-falcon` walked one level up to its root (954 steps,
  2,220,863 tokens); and `e5cdcdf5-e3fe-4a62-9402-0e4010171c51` (Claude
  Code, "project status assessment", 2026-08-31 -> 09-02) with 11
  subagents, found from its own `--name readout-experiment-2026-09-01`
  declaration command (3152 steps, 537,691 tokens). Nothing unresolved:
  all seven Aug 18 phase declarations (`patch-array-5800-clarify` …
  `-solve-2`) live inside the one opencode session, so the ledger's session
  names are `--name` values, not sessions. No transcript's cwd is the
  workspace and no title mentions patch-array; the declaration command
  is what links them.
- `bowtie-3500-pilot`: `ses_02ac8a0abffeZ11jkrOvvXgcxR` = **shiny-canyon**
  with 3 subagents (1449 steps, 2,581,078 tokens) from the summary's
  `slug: shiny-canyon`. Its machine state is absent here (only
  `model_snapshot.json`), and the headline says so:
  `machine state: absent (no machine state (results/state/ holds no state
  file))`; `active_wall: unmeasurable: no session-1 start in state.md`.

**For ticket 10 (not mine to fix):** all five ledger items are in the
findings, but only the readout kill loop (`foreground_poll`, 33 sleeping
calls, 27 min) is in the top ten; the state-sourced ones — `GrpcApiError
GetVariables x3 quoted by readouts.txt x2, z_act.txt x1`, the two pin
moves, the late solve-1b declaration — cost 0 tokens and sort last (#374-
377 of 378), and the two misroutes sit at #24 and #109. The overwrite of
`session.json` by the readout experiment has no classifier. Two classifier
false positives seen on the real data: `LAUNCH_RE` matches `launch=True`
inside a heredoc that writes `STATUS.md` (a `late_declaration` "desktop
launch"), and `GrpcApiError GrpcApiError x5` is the label when no AEDT
command is named. With the command whole, the 09-01 session is now
**declared** (`solve #7`, its `session.py --phase solve` sat past the
200th character of a compound command), so `undeclared_session` no longer
fires for it. `raw_wall` (344 h) spans both sessions; the per-session spans
are on the headline's `sessions:` lines.

Verification, verbatim:

- `PASS: run_trace tests=36 failed=0`
- `PASS: painpoints tests=68 failed=0`
- `PASS: run_report tests=25 failed=0`
- `PASS: run_report workspace=patch-array-5800 sessions=2/2 steps=4106 findings=378 high=35 trace=fresh`
- `PASS: run_report workspace=bowtie-3500-pilot sessions=1/1 steps=1449 findings=114 high=17 trace=fresh`
- `PASS: run_trace captured ses_fe9ae6dd3ffe2a8knbeE1b4yrr.jsonl from opencode.db` (twice, byte-stable)
- `PASS: run_trace captured f0c832a3-cb36-4168-ac07-70c2793c74a2.jsonl from C--Users-afpim-Repos-HFSS-automation`
- `PASS: run_trace captured a0e9c38f-3117-4d93-8086-9b4f16ee0d52.jsonl from C--Users-afpim-Repos-HFSS-automation`
- `python skill/hfss-agent/verify_skill.py` -> `ALL PASS`
- `PASS: tier0 suites=21 failed=0 elapsed=40.5s`
