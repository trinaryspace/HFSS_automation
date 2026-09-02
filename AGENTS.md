# HFSS Automation

This repo lets a conversation with an agent produce a complete, correct ANSYS HFSS simulation — geometry, materials, excitations, setups, solves, plots, and results. Read `CONTEXT.md` for the domain glossary and `docs/adr/` for settled decisions before working.

## Agent skills

### Issue tracker

Issues and specs live as local markdown under `.scratch/<feature-slug>/` (one spec, one issues/ folder per feature). See `docs/agents/issue-tracker.md`.

### Triage labels

Five canonical labels, each string equal to its name (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`), recorded as `Status:` lines in issue files. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` at the repo root is the domain glossary; decisions live in `docs/adr/`. See `docs/agents/domain.md`.

### Fixture fidelity

Test fixtures are captured from real artifacts, never written from memory; a synthetic fixture is valid only alongside a real one it provably matches. Two P0 bugs passed a green suite because this was not enforced. See `docs/agents/fixture-fidelity.md`.

### Harnesses

The `hfss-agent` skill runs under both opencode and Claude Code from one source tree: links for locations, a tier-0 verbatim check for the one thing that cannot be linked (subagent prompts), and `scripts/run_card.py` reading either session store. See `docs/agents/harnesses.md`.

### Run retro

Every Tier-2 run ends with `scripts/run_report.py` writing `workspaces/<name>/run-report.md`; the retro reads its sections 1–2, files one issue per `high` finding that is a tool defect, and appends the row to the campaign log. See `docs/agents/run-retro.md`.

### Verification tiers

`scripts/tier0.py` (seconds, no license) before any AEDT launch; `scripts/tier1.py` builds on the live desktop but never solves; Tier 2 is the full end-to-end run.
