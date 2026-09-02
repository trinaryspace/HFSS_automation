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

**Status:** ready-for-agent

- [ ] SKILL.md, execution.md and the template updated; `verify_skill.py` markers extended
- [ ] `docs/agents/run-retro.md` written and linked from `AGENTS.md`
- [ ] Both `runcard` prompts changed identically; `python scripts/verify_agents.py` passes
- [ ] Tier 0 green
