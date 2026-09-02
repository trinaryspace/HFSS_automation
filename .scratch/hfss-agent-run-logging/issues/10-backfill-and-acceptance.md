# 10 — Backfill and acceptance on the last runs

**What to build:** Nothing new; this ticket runs the pipeline over the runs
that already exist and grades it against what their ledgers record by hand.
Both stores still hold the transcripts: the 2026-08-18 `patch-array-5800`
sessions in `opencode.db` (`hidden-falcon` and its siblings) and the
2026-08-31 / 09-01 sessions under `~/.claude/projects/`.

- Backfill `sessions.jsonl` for `patch-array-5800` by hand from the slugs and
  session ids named in its `state.md`, `summary.md` and the campaign log;
  mark each line `backfilled: true`. Same for `bowtie-3500-pilot`
  (`shiny-canyon`) and `patch-2400` (`kind-rocket`).
- Events cannot be backfilled; the report must degrade to
  `between-stages` attribution and say so in the headline.
- Run `run_report.py` on all three. Commit the reports.
- Grade `patch-array-5800` against its ledger. The report must surface, in
  its top-ten findings and without reading the ledger:
  1. the two DESIGN-constant misroutes and the rebuilds they forced,
  2. the readout failing across six freshly launched desktops
     (`backend_error` grouped on `GetVariables`),
  3. the mid-run desktop recycle (pin 64554 → 57850),
  4. the solve-phase declaration arriving after the solve submission,
  5. the readout experiment overwriting the run's session record.
- Grade `shiny-canyon` against `docs/hfss-agent-performance-analysis.md`
  sections 2–3: the heaviest outputs, the 78.9 KB reasoning block, the
  ~36-step sync saga, and the ~30-step solve-poll saga must all appear.

Every miss becomes a comment on ticket 05 with the evidence the classifier
should have matched. Only when the five-of-five and the analysis-doc checks
pass does this feature close.

**Blocked by:** 06.

**Status:** ready-for-agent

- [ ] Three backfilled `sessions.jsonl` files, each line marked backfilled
- [ ] Three `run-report.md` / `.json` pairs committed; index has five rows (two seeds plus three)
- [ ] The five `patch-array-5800` findings and the four `shiny-canyon` findings are present, quoted in this ticket's comments with their report lines
- [ ] Misses filed against ticket 05
