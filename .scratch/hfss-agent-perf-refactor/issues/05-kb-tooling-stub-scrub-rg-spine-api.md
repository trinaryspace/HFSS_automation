# 05 — KB tooling: stub scrub, ripgrep, spine-api

**What to build:** three items.

1. **`.rst.md` stub scrub.** 4,035 of 8,411 KB files are `.rst.md` stubs (~0.9 MB; sphinx re-exports of the real `.md` twins — analysis §6). The scraper (`scraping/generate_pyaedt_ai_context.py`) must stop emitting them; a one-off pruning script removes the existing stubs; record the scrub in the KB provenance note. KB corpus content otherwise unchanged — no re-crawl.
2. **ripgrep install.** `winget install BurntSushi.ripgrep.MSVC` (user-opted, machine-wide), verified with `rg --version`; the skill (ticket 03) then uses `rg -l` for filename discovery.
3. **`scraping/generate_spine_api.py`.** Distills the ~35-call spine set (Hfss lifecycle, geometry modeler primitives, materials update, wave_port/assign_radiation_boundary_to_objects, create_setup/create_linear_count_sweep, validate_simple, analyze, create_report/get_solution_data, …) from the KB into `knowledge/playbook/spine-api.md`: signature + one-line semantics + EC gotcha link per call. Emits a provenance header (generation date, KB file count, content hash); regenerate in the KB top-up ceremony so it never rots; rerunning with no KB change must be byte-stable.

**Status:** ready-for-agent
**Blocked by:** none

- [ ] Zero `.rst.md` files remain; scraper no longer emits them; KB provenance notes the scrub
- [ ] ripgrep installed and `rg -l wave_port` answers in <1 s from the KB root
- [ ] `generate_spine_api.py` produces `knowledge/playbook/spine-api.md` with provenance header
- [ ] Determinism: second run with unchanged KB produces an identical file

## Comments

- 2026-08-04: ripgrep install is the only machine-wide (winget) change in the refactor — explicitly opted into by the user in the grilling session.
