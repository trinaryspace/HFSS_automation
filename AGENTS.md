# HFSS Automation

This repo lets a conversation with an agent produce a complete, correct ANSYS HFSS simulation — geometry, materials, excitations, setups, solves, plots, and results. Read `VISION.md` for what the project is for and what work is answerable to, `CONTEXT.md` for the domain glossary, and `docs/adr/` for settled decisions before working.

## Agent skills

### Issue tracker

Issues and specs live as local markdown under `.scratch/<feature-slug>/` (one spec, one issues/ folder per feature). See `docs/agents/issue-tracker.md`.

### Triage labels

Five canonical labels, each string equal to its name (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`), recorded as `Status:` lines in issue files. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` at the repo root is the domain glossary; decisions live in `docs/adr/`. See `docs/agents/domain.md`.
