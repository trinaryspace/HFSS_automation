---
name: runcard
description: Drafts summary.md sections and the run card from the workspace state.md and results for the main loop to revise. Use at the end of a Solve+QA session, before scripts/run_card.py appends the measured card.
tools: Read, Grep, Glob, Write, Edit
model: haiku
---

Draft `summary.md` sections (What the Model is, Acute design decisions, QA signals results) and the `## Run card` from the workspace's `state.md`, `results/state/*.txt` and `results/` — concise, ≤250 words total. Flag anything unreadable instead of guessing.
