# 07 — Runs index and cross-run comparison

**What to build:** `docs/runs/index.jsonl`, tracked, one line per run,
appended (or replaced by `run_id`) by `run_report.py`. Columns are the
headline: `run_id, workspace, recipe, skill_commit, host, outcome,
completions, billed, billed_per_completion, parts, raw_wall_ms,
active_wall_ms, tokens_by_phase, findings_high, top_finding_kind,
report_path`.

Then two changes so the baselines stop being constants:

- `scripts/run_card.py` `BASELINE` and `PILOT` become the first two seed
  lines of the index (`silent-engine`, `shiny-canyon`), with their fields
  as recorded there and `active_wall_ms: null`. The `--verdict` table takes
  `--baseline <run_id>` and defaults to the newest completed run of the same
  recipe, so a verdict is always against something comparable.
- `scripts/run_report.py --compare` (also the report's section 10) prints
  the index rows for the same recipe, newest last, with deltas on billed,
  parts and active wall.

Add a `docs/runs/README.md` of ten lines: what a row is, that the report is
the source and the index is derived, and how to re-seed it
(`run_report.py --reindex` walks every `workspaces/*/run-report.json`).

**Blocked by:** 06.

**Status:** ready-for-agent

- [ ] Index appended idempotently; `--reindex` rebuilds it byte-identically from the reports
- [ ] The two historical baselines are seed rows and `run_card.py --verdict` reads them from the index; `test_run_card.py` still passes
- [ ] `--compare` on the two committed reports prints a two-row table with deltas
- [ ] `docs/runs/README.md` exists
