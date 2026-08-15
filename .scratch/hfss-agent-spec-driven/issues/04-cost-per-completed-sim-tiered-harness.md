# 04 — Cost per completed simulation, and the three-tier test harness

**What to build:** Two measurement changes that make every later decision
legible. First, the run card's headline metric becomes **cost per successfully
completed simulation**, not tokens per run — a run that burns 1.58 M tokens and
delivers no readable result must score worse than one that burns 400 k and
delivers, and today's metric cannot express that. Extend `scripts/run_card.py`
with an outcome field (`completed` / `escalated` / `abandoned`), the escape-hatch
stage-script count, and a derived cost-per-completion; keep the existing token /
parts / wall-time columns so the `silent-engine` and `shiny-canyon` history stays
comparable. Second, split verification into three tiers so that "did I break it"
stops requiring license-hours: **Tier 0** offline (schema, references, units,
physics pre-check, parsers against `fixtures/real/`, compiler golden tests) in
seconds with no AEDT; **Tier 1** build-only on a live desktop through
`validate_simple()` and snapshot capture, no solve; **Tier 2** full end-to-end
including solve, readout, and QA. One runner script per tier, each printing a
single machine-parseable summary line in the established `PASS:` house style.

**Blocked by:** None. Land the harness before the architecture work so its
effect is measurable.

**Status:** ready-for-human

- [x] Run card records outcome, escape-hatch count, and cost per completed simulation; existing baselines re-scored under the new metric with the re-scoring documented
- [x] `scripts/tier0.py` runs with no AEDT installed and no license, in under ~30 s
- [ ] `scripts/tier1.py` builds a named canonical spec on a live desktop and captures its snapshot without solving
- [x] Each tier prints exactly one summary line; no tier dumps pyAEDT INFO logs into stdout
- [x] `verify_skill.py` extended to assert the tier scripts and the metric exist
- [x] Tier 0 wired into the template README as the pre-flight the agent runs before any AEDT launch

## Comments

- 2026-08-14: **DONE** (Tier 1 written and dry-run verified; its live run
  needs a desktop).
- **Metric.** `run_card.Outcome` reads `results/state/outcome.txt`
  (`outcome=` / `completions=` / `escape_hatch_scripts=` / `note=`),
  overridable by `--outcome/--completions/--escape-hatch`. The card gains
  three lines: `outcome`, `escape_hatch_scripts`,
  `billed_per_completed_sim`. An unrecorded outcome reports `unrecorded` —
  never guessed.
- **Baselines re-scored** and kept as constants: `silent-engine` completed
  one simulation, so its cost per completed simulation is its billed total,
  398,130. `shiny-canyon` delivered nothing, so its cost is
  `infinite (1,579,333 billed, 0 completed)` — under tokens-per-run it
  scored as merely 4x worse, which is what the metric change is for. A
  sweep divides: 240,000 over 8 completions reads `30,000`.
- **Tier 0** (`scripts/tier0.py`) runs the corpus check plus six suites —
  template runners, watchdog stages, run card, static gate, skill markers,
  KB checks — in **~13 s with no AEDT and no license**, and prints one
  `PASS: tier0 suites=7 failed=0` line.
- **Tier 1** (`scripts/tier1.py`) runs a workspace's `NN_*.py` build stages
  in order and **refuses every stage numbered 08 or above** rather than
  skipping it quietly, so it cannot consume solver time by accident. It
  reads each stage's Verification line, stops at the first failure, and
  captures the snapshot. Dry-run against the pilot workspace lists 8 build
  stages and refuses 4. Sets `PYAEDT_LOG_LEVEL=WARNING` so INFO logs stay
  out of the caller's context.
- `verify_skill.py` extended for the single-parser rule, the corpus, the
  tier scripts, the metric, and the case set. Tier 0 wired into the
  template README as the pre-flight before any AEDT launch.
- Open: the acceptance item for a live Tier 1 build is unchecked pending a
  desktop run.
