# 08 — KB top-up: reports, plots, advanced visualization, solve setups

**What to build:** close the four remaining KB gaps for the later Spine stages (verified absent from `scraping/pyaedt_ai_context/` as of ticket 03, session 2026-08-02). The scraper's `--topup` machinery from ticket 03 already provides the incremental-crawl mechanics (gateway seeds for link discovery, focus-pattern link filtering, never re-write existing pages, corpus rebuild + provenance record per run) — this ticket is new top-up targets, not new machinery. Priority per user: **report generation first, solve setup second**; plots and advanced follow.

Gap inventory (unique autosummary pages counted from the `/version/stable/` sitemap; on-disk files ≈ 2× per page because both `.html` and `.rst` forms are stored, matching the existing corpus convention):

1. **`ansys.aedt.core.visualization.report.*`** — ~695 pages, zero files today. The report-class surface (`Fields`, `FarField`, `NearField`, `AntennaParameters`, `Standard`/`Spectral`, eye-diagram + EMI classes) behind the reports stage. Docs tree: `/API/visualization/report/`.
2. **`ansys.aedt.core.modules.solve_setup` + `solve_sweeps` + `design_xploration` + `modules.profile`** — ~190 HFSS-relevant pages, zero files today. The setup/sweep/parametric surface (`SetupHFSS`, `SetupHFSSAuto`, `Setup` base, `SweepHFSS`, `SetupParam`/`SetupOpti`, profile classes for convergence QA). Docs trees: `/API/_autosummary/ansys.aedt.core.modules.solve_setup.*` etc.
3. **`ansys.aedt.core.visualization.plot.*`** — ~93 pages, zero files today (`ReportPlotter`/matplotlib, `ModelPlotter`/pyvista, `AnsysReport`/pdf). Docs tree: `/API/visualization/plot/`.
4. **`ansys.aedt.core.visualization.advanced.*`** — ~128 pages, zero files today; includes `FfdSolutionData` (far-field solution data — the radiation-pattern readout the antenna stages need). Docs tree: `/API/visualization/advanced/`.

**Blocked by:** None (scraping does not touch the desktop or license)

**Status:** ready-for-agent

- [x] `visualization.report.*` crawled: new KB category has a non-trivial file count (expected ~1,300–1,400 files), all filenames under the `report.` subtree
- [x] Solve-setup surfaces crawled: `setup_and_mesh/` grows from 155 files using focused seeds on the HFSS-relevant classes (`Setup`, `SetupHFSS`, `SetupHFSSAuto`, `SweepHFSS`, `SetupParam`, `SetupOpti`, profile classes)
- [x] `visualization.plot.*` crawled: new KB category populated (expected ~180 files)
- [x] `visualization.advanced.*` crawled: new KB category populated (expected ~250 files), with `FfdSolutionData` method sub-pages captured
- [x] The run is incremental per target: no pre-existing page is re-fetched or re-written (gateway seeds may be re-fetched for link discovery only); `git status` after all runs shows zero modifications to previously tracked KB pages
- [x] Provenance records appended for each target run (existing `provenance.md` mechanism: date, pages fetched/new/kept, corpus size); RAG JSONL corpus regenerated and consistent with the per-page files
- [x] `scraping/verify_kb.py` extended with the new categories and thresholds; all checks pass

## Implementation notes

- New top-up targets in `TOP_UP_TARGETS` (`scraping/generate_pyaedt_ai_context.py`), each with gateway seeds + focus patterns:
  - `reports`: seeds `API/visualization/report.html`; focus `visualization\.(report)` — actually keep one pattern per subtree: `r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.visualization\.report"`
  - `plots`: seed `API/visualization/plot.html`; focus `r"…\.visualization\.plot"`
  - `advanced`: seed `API/visualization/advanced.html`; focus `r"…\.visualization\.advanced"` (covers `FfdSolutionData`, `FRTMData`/`FRTMPlotter`, `HDMPlotter`, `TouchstoneData`; `sbrplus` pages are fine to include — RCS/SBR+ solve remains out of scope per ADR 0004, this is just documentation)
  - `solve_setups`: seeds the class pages `Setup`, `SetupHFSS`, `SetupHFSSAuto` (solve_setup), `SweepHFSS` (solve_sweeps), `SetupParam`, `SetupOpti` (design_xploration), `Profiles`, `SimulationProfile` (profile); the base `Setup` class is a seed because `SetupHFSS` inherits its surface. Skip `SetupCircuit`/`SetupMaxwell`/`SetupQ3D`/`Setup3DLayout`/`SetupSBR` — other-solver/3DLayout/RCS surfaces (out of HFSS scope; SBR per ADR 0004). Focus includes `modules\.(solve_setup|solve_sweeps|design_xploration|profile)` — implementations may tighten to the seeded classes.
- Category mapping (KB layout stays otherwise untouched; `categorize_url` gains the new keys): `reports` ← `visualization.report.*`, `plots` ← `visualization.plot.*`, `advanced_visualization` ← `visualization.advanced.*`, `setup_and_mesh` ← the solve/profile modules (existing category).
- Run order: `reports` → `solve_setups` → `plots` → `advanced` (user priority). Each run ends with corpus rebuild + provenance record; no AEDT or license involved.

## Comments

- 2026-08-02: Filed after ticket 03 review — the gaps were verified against the docs sitemap and KB on disk (`solve_setup`, `solve_sweeps`, `design_xploration`, `modules.profile`, `visualization.report/plot/advanced` all at 0 files; counts above from the same sitemap analysis). `application.variables` (156 files, under `desktop_app`) and the full `visualization.post.*` tree are confirmed present — not gaps. Other-solver apps (circuit, icepak, maxwell, q3d, rmxprt, twinbuilder, emit, filtersolutions) remain out of scope per the HFSS-focused KB spec.
- 2026-08-02: **DONE.** `TOP_UP_TARGETS` gained `reports`, `solve_setups`, `plots`, `advanced` (no new machinery); `categorize_url` gained the `reports`, `plots`, `advanced_visualization` categories and routed the solve/profile modules into the existing `setup_and_mesh`. The solve-setup focus is tightened to the HFSS-relevant class roots (`solve_setup.Setup|SetupHFSS|SetupHFSSAuto`, `solve_sweeps.SweepHFSS`, `design_xploration.SetupParam|SetupOpti`, the full `modules.profile` module) — the other-solver classes (`SetupCircuit`/`SetupMaxwell`/`SetupQ3D`/`Setup3DLayout`/`SetupSBR`, `SweepHFSS3DLayout`/`SweepMatrix`) stay out per the ticket and ADR 0004.
- Runs (order = user priority), all incremental — 0 `[FAILED]` fetches, 0 pre-existing pages re-written (`git status`: only new KB pages; `provenance.md`/`rag_knowledge_base.jsonl` are the per-run records the mechanism regenerates): reports 1,391 fetched / 1,390 new (`reports/` 0 → 1,390); solve_setups 310 new (`setup_and_mesh/` 155 → 465: solve_setup 210, profile 42, design_xploration 42, solve_sweeps 16); plots 187 fetched / 186 new (`plots/` 0 → 186); advanced 257 fetched / 256 new (`advanced_visualization/` 0 → 256, incl. `FfdSolutionData` full method surface). Corpus 4,099 → 6,241 entries; one provenance record per run.
- Checks: `scraping/verify_kb.py` extended with the four ticket-08 groups (subtree populated + surface-naming + HFSS class roots present + profile module + other-solver classes absent + `FfdSolutionData` present); all 22 checks pass. Pre-crawl baseline run failed exactly the 9 new checks — the gaps the ticket measured. The in-scope/out-of-scope setup class lists live once in the scraper (`HFSS_SETUP_CLASSES` / `NON_HFSS_SETUP_CLASSES`) and drive both the top-up focus patterns and the verify checks, so the two cannot drift. Also fixed a stray provenance bullet inconsistency (records now carry the `- ` bullet, matching the stored history, which also makes the dedupe check able to hit).
