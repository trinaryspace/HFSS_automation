# 09 — Wire the report into the skill and the retro

**What to build:** The report only helps if it is produced at the end of every
run and read at the start of every retrospective. Four text changes and one
subagent change.

- `skill/hfss-agent/SKILL.md`, Session 3 *Done when*: add "and
  `run-report.md` is written by `scripts/run_report.py`". The summary and
  run-card bullet names `record_outcome.py` (ticket 02) before the report.
- `skill/hfss-agent/reference/execution.md`: per-stage checklist gains the
  `record_gate.py` call at each Review gate; the harness table gains the
  rows from tickets 01, 04 and 08; the Summary step names the report.
- `skill/hfss-agent/templates/workspace/README.md` and `summary.md`: the
  summary skeleton gets a one-line pointer to `run-report.md`; the README's
  end-of-run checklist lists `record_outcome` → `run_card` → `run_report`.
- `docs/agents/` gains `run-retro.md`: after every Tier-2 run, the maintainer
  reads sections 1–2 of the report, files one issue per `high` finding that
  is a tool defect (not a design defect), and appends the row to the campaign
  log. Ten lines, linked from `AGENTS.md`.
- The `runcard` subagent prompt (in both `opencode.json` and
  `.claude/agents/runcard.md`, verbatim, `verify_agents.py` enforced) reads
  `run-report.json` when present and narrates from it, never computing a
  number itself.

**Blocked by:** 06.

**Status:** ready-for-human

- [x] SKILL.md, execution.md and the template updated; `verify_skill.py` markers extended
- [x] `docs/agents/run-retro.md` written and linked from `AGENTS.md`
- [x] Both `runcard` prompts changed identically; `python scripts/verify_agents.py` passes
- [x] Tier 0 green

## Comments

### 2026-09-02 — landed

What tickets 01–06 had already put in place, verified rather than redone:
execution.md checklist 10 names `record_gate.py` (ticket 02), checklist 14
opens with `record_outcome.py` (ticket 02), the harness table carried ticket
01's two rows (session history, subagent discovery) but **no row for ticket
04's trace** — added below. SKILL.md Session 3 already named
`record_outcome.py`.

What landed, by file:

- `skill/hfss-agent/SKILL.md`: Session 3 states the close-out order
  `record_outcome.py` → `run_card.py --summary` → `run_report.py --workspace`,
  and its *Done when* ends "and `run-report.md` is written by
  `scripts/run_report.py`"; the Solve+QA bullet is now "Summary + run card +
  run report" (the `runcard` subagent drafts from `run-report.json` when one
  exists and computes no number); the workspace shape lists
  `run-report.md` + `run-report.json` as tracked beside `summary.md`.
- `skill/hfss-agent/reference/execution.md`: checklist 14 (Summary) ends
  with the report — what it reads, what it writes, its `PASS:` line, the
  fixed order, and that the retro reads it; harness table gains the **Step
  trace (run report)** row (opencode `opencode.db` / `parent_id`; Claude Code
  transcript + `subagents/` tree; one `steps.jsonl` shape; `run_report.py`
  refreshes a stale trace itself). No hooks row: ticket 08's row goes
  directly after it.
- Template `README.md`: `run-report.md` in the shape tree; a numbered
  **End-of-run checklist** (`record_outcome` → `run_card` → `run_report`,
  each with its command, "closed out when all three have printed `PASS:`");
  the tracked record names both report files. `summary.md`: a three-line
  pointer under `## Run card`. `state.md`: the Session 3 run-card line
  names the order and the report.
- `docs/agents/run-retro.md` (new, ten lines): read sections 1–2 only; one
  issue per `high` finding that is a tool defect, design defects go to
  `summary.md` / the Learning loop; append the `index_row` values to the
  campaign log's Wave log; a ledger-known pain point the report missed is a
  classifier ticket. Linked from `AGENTS.md` as "### Run retro", same shape
  as the other entries.
- `docs/agents/harnesses.md`: two rows — **Session store (step trace)** and
  **Live tool timing (run logging 08)**, the latter marked as landing with
  ticket 08 (opencode plugin `tool.execute.before/after` named as the
  follow-up); a "changed a step-trace field?" bullet (recapture via
  `run_trace.py --capture`).
- `CLAUDE.md`: the session-id bullet now names `run_report.py` and the
  `subagents/` tree.
- `runcard` prompt, identical in `opencode.json` and
  `.claude/agents/runcard.md`: when `run-report.json` exists beside
  `summary.md`, narrate from it — every number from `headline` / `findings`
  as written, top findings by kind and cost, `unmeasurable` / `unrecorded`
  kept — "you never compute, sum, or estimate a number yourself".
- `skill/hfss-agent/verify_skill.py`: SKILL marker `run report`; reference
  markers `gate and outcome recorded` (ticket 02's unenforced pair),
  `run report step`, `step trace row`; `TEMPLATE_MARKERS` for README /
  summary / state; existence + three-step check on `run-retro.md`; the
  `AGENTS.md` link; the runcard file naming `run-report.json` and "never
  compute".

Judgement call, stated: the mandated order puts `run_report.py` after the
card, so on a first pass the `runcard` draft precedes `run-report.json`;
the subagent's "when present" clause serves regeneration and backfill
(ticket 10). Running the report once before the draft is byte-idempotent
and legal if a maintainer prefers the narration on every run.

Verification, verbatim:

- `python skill/hfss-agent/verify_skill.py` → `ALL PASS`
- `PASS: verify_agents agents=2 failed=0`
- `PASS: tier0 suites=21 failed=0 elapsed=40.7s`
