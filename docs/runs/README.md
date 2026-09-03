# Runs index

`index.jsonl` holds one JSON line per run: the headline of its run report (`run_id`, `workspace`, `recipe`, `skill_commit`, `host`, `outcome`, `completions`, `billed`, `billed_per_completion`, `parts`, `raw_wall_ms`, `active_wall_ms`, `started`, `tokens_by_phase`, `findings_high`, `top_finding_kind`, `report_path`), oldest first by `started`.
The report is the source, the index is derived: `python scripts/run_report.py --workspace workspaces/<name>` writes `run-report.md` / `run-report.json` beside `summary.md` and then appends the run's line here, replacing any line with the same `run_id` — never edit a line by hand.
The first two lines are seed rows (`"seed": true`): the `silent-engine` baseline and the `shiny-canyon` pilot, the literals of `scripts/run_card.py` (`BASELINE`, `PILOT`) with `active_wall_ms: null` because nothing measured their build-to-solve window; each names its `source`.
The pilot's seed and the `bowtie-3500-pilot` report are the same opencode session read at two instants (1,579,333 billed at the retrospective; 2,581,078 by the time it was traced), which is why both lines exist.
`scripts/run_card.py --verdict` scores a run against the newest completed run of the same recipe here (`--baseline <run_id>` to pick one; the `silent-engine` seed when nothing is comparable, and it says so).
`scripts/run_report.py --workspace workspaces/<name> --compare` (or `--compare <run_id> ...`) prints the rows of one recipe newest last, each with its deltas on billed, parts and active wall against the row above — the same table as a report's section 10.
To re-seed the file, run `python scripts/run_report.py --reindex`: it rebuilds the index from the seed rows plus every `workspaces/*/run-report.json`, byte-identical to what the appends produced (`changed=no` on a clean checkout).
`null` means the report could not measure the column (a trace-only report has no `parts`; a run before ticket 02 has no `active_wall_ms`); it is never a zero.
