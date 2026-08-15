# 15 — Token discipline: quiet output, cached prefix, tiered effort

**What to build:** The mechanical savings, which are worth collecting whether or
not the architecture bet proceeds. The pilot's own accounting names the leaks:
staged scripts printing tens of pyAEDT INFO lines across roughly 35 process
launches, whole progress files and verify logs read into context instead of
single-line summaries, ad-hoc throwaway probe scripts, and 695 KB of reasoning
traces. Four changes.

**Quiet by default:** pyAEDT logging at WARNING everywhere, and every runner
filtered to its `PASS:` / `STAGE_FAILED` line plus assertions. **Never read a
whole state file:** tail one to three lines of `solve_progress.txt`; the
watchdog's line format is already designed for exactly this and the habit, not
the format, is what failed. **Cache the stable prefix:** the spec schema,
`spine-api.md`, and the active recipe are fixed across every seam in a run —
order them first and cache them rather than re-sending, which is the single
largest structural saving available on a long run. **Tier the effort:** low for
mechanical seams, high only for diagnosis and clarification, rather than one
global `variant` for everything.

Also fold in perf-refactor ticket 10's one-diagnostics-script rule: a single
`diag.py` that prints pin liveness, project path, object and boundary counts,
profile status, sweep-entry count, and a one-shot readout in one attach —
replacing the pilot's scattered throwaway probes.

**Blocked by:** None — independent of the architecture bet. Supersedes and
absorbs perf-refactor ticket 10.

**Status:** ready-for-agent

- [ ] pyAEDT logging at WARNING in every runner; a full build prints one line per stage
- [ ] No runner or agent step reads a whole progress or verify log; tails only
- [ ] Stable prefix identified, ordered first, and demonstrably cached — measured on one run
- [ ] Per-seam effort settings rather than one global variant
- [ ] One `diag.py`; throwaway probe files are a documented anti-pattern in `execution.md`
- [ ] Measured on a canonical case: context bytes per stage down against the pilot's recorded figures
