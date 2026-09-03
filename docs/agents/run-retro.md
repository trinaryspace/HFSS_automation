# Run retro

After every Tier-2 run, once `scripts/run_report.py --workspace workspaces/<name>` has written `run-report.md`, read **sections 1–2 only** — the headline and the top pain points — never a transcript; every number there is machine-derived or marked `unmeasurable: <reason>`, and a hand-corrected report is a defect to file, not a fix.

Then, in order:

1. **One issue per `high` finding that is a tool defect** — a script, runner, template, skill sentence or classifier that let the cost happen (a probe loop, a whole-file read, a rebuild chain, a late declaration, a readout that failed by route). A design defect — a resonance off target, a feed the Recipe got wrong — belongs in `summary.md` and the Learning loop, never in the tracker. File it under `.scratch/<feature-slug>/issues/` (`docs/agents/issue-tracker.md`), `Status: needs-triage`, quoting the finding's kind, cost and evidence line verbatim.
2. **Append the row to the campaign log** — `.scratch/hfss-agent-parallel-tests/campaign-log.md`, "Wave log": the report's `index_row` values (`run_id`, `skill_commit`, outcome, completions, billed, active wall, `findings_high`, top finding kind) and the report path. `docs/runs/index.jsonl` carries the same row by machine; the log carries what the machine cannot — what the wave concluded.
3. A pain point the ledger records and the report missed is a classifier ticket (`hfss_spec/painpoints.py`), not a note in the ledger.
