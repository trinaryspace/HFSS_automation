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

**Status:** ready-for-human

- [x] Index appended idempotently; `--reindex` rebuilds it byte-identically from the reports
- [x] The two historical baselines are seed rows and `run_card.py --verdict` reads them from the index; `test_run_card.py` still passes
- [x] `--compare` on the two committed reports prints a two-row table with deltas
- [x] `docs/runs/README.md` exists

## Comments

### 2026-09-02 — landed

What landed, by file:

- `docs/runs/index.jsonl` (new, tracked): one JSON object per line, the
  ticket's columns plus `started` (the first traced step — the instant the
  file is ordered by, oldest first; a row with none sorts first), the two
  seed rows carrying `"seed": true` and a `source`. Nested dicts are
  key-sorted and the columns are in a fixed order (`run_card.ordered_row`),
  so a line appended from memory and one rebuilt from `run-report.json`
  are the same bytes. `docs/runs/README.md`: ten lines.
- `scripts/run_card.py`: `BASELINE` / `PILOT` gain `recipe`, `workspace`,
  `started`; `SEED_SOURCE` names where each number came from (analysis doc
  section 1 for silent-engine; the perf-refactor pilot retrospective's
  verdict table for shiny-canyon). New: `INDEX_PATH`, `INDEX_COLUMNS`,
  `seed_rows()`, `ordered_row`, `index_sort_key`, `read_index`,
  `index_rows` (file rows + seeds, the seeds from the constants overriding
  a hand-edited seed line), `recipe_of` (moved from run_report),
  `choose_baseline`, `print_verdict`. `--verdict` takes `--baseline
  <run_id>` and `--index PATH`; the default is the newest completed run of
  the workspace's recipe in the index, this workspace's own row excluded
  (one report per workspace dir, ADR 0001), else the `silent-engine` seed;
  it prints `baseline: <run_id> (<how>)` above the table, e.g. `baseline:
  silent-engine (seed; no completed corporate-patch-array run in
  docs/runs/index.jsonl besides patch-array-5800)`. `_cmp_row` is
  None-safe: a baseline with `parts: null` (a trace-only report) gives an
  informational parts row, verdict `-`, billed still scored.
- `scripts/run_report.py`: after writing the report, `upsert_index`
  appends the run's line (replacing by `run_id`; seeds always present);
  the PASS line ends `index=<rows>`. `--reindex [--workspaces DIR]
  [--index PATH]` rebuilds from the seeds plus every
  `workspaces/*/run-report.json` (`PASS: run_report reindex reports=N
  rows=M index=... changed=yes|no`; a broken report is a `warning: skipped`
  on stderr). `--compare` (with `--workspace`, its recipe) or `--compare
  <run_id> ...` prints the rows newest last with deltas on billed, parts
  and active wall against the row above (`+177,476 (+7%)`; `n/a` when a
  side is null). Section 10 is that table for the recipe's rows up to and
  including this run (last five before it, itself last), built from what
  the index holds once the report is written, so section 10, the index and
  `--compare` agree and a second render is byte-identical. The headline
  gains `- started: <iso> (first traced step)`; `index_row` fills `parts`
  from the carded run total when the workspace has a history (null for the
  two committed reports: trace only). `--workspace` is no longer required
  for `--reindex` / `--compare <ids>`.
- `scripts/test_run_card.py` (80 tests; +7 `TestRunsIndexBaseline`): the
  seeds equal the literals and cite their sources; `index_rows` ordering
  and seed override; default = newest completed of the recipe, not this
  workspace, not an abandoned newer one; the fallback and its message;
  `--baseline` (seed and index row) and an unknown one failing; null
  parts informational. The two existing `--verdict` tests pin
  `--baseline silent-engine` and a throwaway `--index`.
- `scripts/test_run_report.py` (29 tests; +4 `TestRunsIndex`): every
  `run_main` gets a throwaway `--index` so no test touches the tracked
  file; append once after the seeds and idempotent; `--reindex` from a
  deleted index byte-identical to the append, `changed=no` on rerun, a
  hand-edited seed line restored, a broken report skipped with a warning;
  `--compare` by recipe and by run ids with the exact delta cells;
  section 10 == the index == `--compare`. `test_previous_runs_from_an_index`
  rewritten to the new shape (previous five + this run, a newer run not
  shown, the stale own line replaced). `scripts/tier0.py`: no new suite
  needed (both suites were registered by tickets 01/06); unchanged.
- Both committed reports re-rendered with `--no-trace` (stores and trace
  files untouched): the md diff is the `started` line and section 10.

Design notes, stated: the pilot's seed (`shiny-canyon`, 1,579,333 billed
at the retrospective) and `bowtie-3500-pilot-2026-08-06` (2,581,078 by
the time it was traced) are one opencode session at two instants; both
rows stay and the README says so. Neither committed report has an
`outcome=completed`, so today every default verdict falls back to the
seed and says so — that is the honest state, not a defect.

For ticket 09's owner (markers to enforce in `verify_skill.py`, if wanted):
`docs/runs/index.jsonl`, `run_report.py --reindex`, `run_report.py
--compare`, `run_card.py --baseline`, `docs/runs/README.md`.

The index, verbatim (`docs/runs/index.jsonl`):

```
{"run_id": "silent-engine", "workspace": "bowtie-3500", "recipe": "bowtie-5g-baseline", "skill_commit": "unrecorded", "host": "opencode", "outcome": "completed", "completions": 1, "billed": 398130, "billed_per_completion": "398,130", "parts": 424, "raw_wall_ms": null, "active_wall_ms": null, "started": "2026-08-03T04:43:14Z", "tokens_by_phase": null, "findings_high": null, "top_finding_kind": null, "report_path": null, "seed": true, "source": "docs/hfss-agent-performance-analysis.md section 1 (billed, parts; the session 'bowtie-3500', created 2026-08-03T04:43:14Z per the reference SQL of section 10, pinned in scripts/test_run_card.py); outcome and completions re-scored by scripts/run_card.py BASELINE"}
{"run_id": "shiny-canyon", "workspace": "bowtie-3500-pilot", "recipe": "bowtie-5g-baseline", "skill_commit": "unrecorded", "host": "opencode", "outcome": "abandoned", "completions": 0, "billed": 1579333, "billed_per_completion": "infinite (1,579,333 billed, 0 completed)", "parts": 1392, "raw_wall_ms": null, "active_wall_ms": null, "started": "2026-08-06T03:56:43Z", "tokens_by_phase": null, "findings_high": null, "top_finding_kind": null, "report_path": null, "seed": true, "source": ".scratch/hfss-agent-perf-refactor/pilot-retrospective.md verdict table (billed, parts) as scripts/run_card.py PILOT; started = the session's first traced step in workspaces/bowtie-3500-pilot/run-report.json"}
{"run_id": "bowtie-3500-pilot-2026-08-06", "workspace": "bowtie-3500-pilot", "recipe": "bowtie-5g-baseline", "skill_commit": "unrecorded", "host": "opencode", "outcome": "unrecorded", "completions": "unrecorded", "billed": 2581078, "billed_per_completion": "unrecorded", "parts": null, "raw_wall_ms": 127611821, "active_wall_ms": null, "started": "2026-08-06T03:56:43Z", "tokens_by_phase": {"undeclared": 2581078}, "findings_high": 17, "top_finding_kind": "undeclared_session", "report_path": "workspaces/bowtie-3500-pilot/run-report.md"}
{"run_id": "patch-array-5800-2026-08-18", "workspace": "patch-array-5800", "recipe": "corporate-patch-array", "skill_commit": "unrecorded", "host": "claude-code+opencode", "outcome": "unrecorded (outcome.txt is not key=value: completed - user verdict: tuning issue (element resonance 5.6 GHz, ~7 dB in both designs), not a feed defeat; solves #1b + #2 banked Normal Completion)", "completions": "unrecorded", "billed": 2758554, "billed_per_completion": "unrecorded", "parts": null, "raw_wall_ms": 1240320776, "active_wall_ms": null, "started": "2026-08-18T19:20:40Z", "tokens_by_phase": {"build #1": 250244, "build #3": 297873, "build #5": 26238, "clarify #0": 509747, "solve #2": 241503, "solve #4": 556663, "solve #6": 338595, "solve #7": 398515, "undeclared": 139176}, "findings_high": 35, "top_finding_kind": "long_reasoning", "report_path": "workspaces/patch-array-5800/run-report.md"}
```

`python scripts/run_report.py --compare bowtie-3500-pilot-2026-08-06 patch-array-5800-2026-08-18`:

```
| run_id | started | outcome | completions | billed | billed delta | parts | parts delta | active_wall | active_wall delta | findings_high | top_finding_kind |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bowtie-3500-pilot-2026-08-06 | 2026-08-06T03:56:43Z | unrecorded | unrecorded | 2,581,078 | - | n/a | - | n/a | - | 17 | undeclared_session |
| patch-array-5800-2026-08-18 | 2026-08-18T19:20:40Z | unrecorded (outcome.txt is not key=value: completed - user verdict: tuning issue (element resonance 5.6 GHz, ~7 dB in both designs), not a feed defeat; solves #1b + #2 banked Normal Completion) | unrecorded | 2,758,554 | +177,476 (+7%) | n/a | n/a | n/a | n/a | 35 | long_reasoning |
```

Verification, verbatim:

- `PASS: run_report workspace=patch-array-5800 sessions=2/2 steps=4106 findings=378 high=35 trace=kept index=4`
- `PASS: run_report workspace=bowtie-3500-pilot sessions=1/1 steps=1449 findings=114 high=17 trace=kept index=4`
- `PASS: run_report reindex reports=2 rows=4 index=docs/runs/index.jsonl changed=no` (after a fresh append and again after a second render; `md5sum -c` OK on the index and all four report files)
- `PASS: run_report tests=29 failed=0`
- `python scripts/test_run_card.py` -> `Ran 80 tests in 3.369s` / `OK`
- `PASS: tier0 suites=21 failed=0 elapsed=44.2s` (skill-markers `ok` at the time of the run)
