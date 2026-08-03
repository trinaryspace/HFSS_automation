# 09 — KB top-up: modeler surface, logger, optimetrics managers, generic utilities

**What to build:** close the remaining KB gaps for general HFSS use, found by a
sitemap diff (8,001 stable autosummary pages vs 3,292 on disk; `sitemap.xml` at
the site root). Everything listed is documentation-only — no desktop or license.

Verified gap inventory (missing pages / sitemap total, on-disk file counts ≈
2x pages because both `.html` and `.rst` forms are stored):

1. **`ansys.aedt.core.modeler.modeler_3d`** — 223 / 224 missing, 1 file on disk.
   `Modeler3D` is the whole geometry surface of the current docs line
   (`create_box`, `create_cylinder`, `create_rectangle`, `create_polyline` all
   live there — there is no separate `primitives_3d` tree any more): the
   Spine's geometry stage currently has zero method documentation.
2. **`ansys.aedt.core.modeler.cad.*`** — ~268 / 316 missing (~48 files on
   disk). `Object3d` (position/rotate/unite/etc.), `polylines.Polyline` +
   `PolylineSegment`, `elements_3d` (Face/Edge/VertexPrimitive, Plane, Point,
   HistoryProps), `CoordinateSystem`, `ComponentArray`, `components_3d`.
3. **`ansys.aedt.core.modeler.geometry_operators`** — 57 / 57 missing.
   `GeometryOperators` (slice/rotate/mirror helpers used in scripted geometry).
4. **`ansys.aedt.core.modeler.advanced_cad.*`** — 351 / 353 missing (2 on
   disk). OSM/stackup/actor scene-prep docs used by SBR+ scenes; documentation
   only — RCS/SBR+ solve remains out of scope per ADR 0004 (ticket-08
   precedent: sbrplus docs are fine to include).
5. **`ansys.aedt.core.aedt_logger`** — 47 / 47 missing (0 on disk). The
   message manager (`AedtLogger.add_message`/`add_error_message`/...,
   `AppFilter`) the skill's self-correction stage reads after every run.
6. **`ansys.aedt.core.modules.design_xploration` managers** — 15 missing
   (ParametricSetups + OptimizationSetups; SetupParam/SetupOpti already
   present from ticket 08). The parametric/optimization manager classes the
   skill uses for variable sweeps.
7. **`ansys.aedt.core.modules.profile` remainder** — 41 / 63 missing
   (AdaptivePass, FrequencySweepProfile, TransientProfile, MemoryGB, module
   functions). Ticket 08's crawl only reached the pages its seeds link; the
   gateway `/API/Profiles.html` links the rest.
8. **`ansys.aedt.core.generic.*`** — 121 / 121 missing (file_utils,
   configurations, quaternion, numbers_utils, math_utils) plus
   `syslib.nastran_import.nastran_to_stl` (1). Shared utilities incl. the
   file/dir helpers staged scripts use.

Deliberately out of scope (verified present-or-irrelevant / excluded): other
solvers (maxwell, q3d, icepak, circuit, twinbuilder, rmxprt, maxwellcircuit,
emit, mechanical, filtersolutions ≈ 2,784 pages), circuit/PCB modelers
(`modeler.circuits`, `modeler.schematic`, `modeler.pcb`, `modeler.modeler_pcb` ≈
546), `modules.layer_stackup` (67, HFSS 3D Layout), `modules.substrate_circuit`
(42), `modules.cable_modeling` (15), non-HFSS `Setup*`/`Sweep*` classes
(ticket 08 / ADR 0004).

**Blocked by:** None (scraping does not touch the desktop or license)

**Status:** ready-for-agent

- [x] `modeler` target crawls `modeler.modeler_3d` + `modeler.cad` +
      `modeler.geometry_operators` + `modeler.advanced_cad`; `geometry_modeler/`
      grows to a non-trivial count with `Modeler3D` method pages and
      `GeometryOperators` present; no circuit/PCB/2D modeler pages added
- [x] `logger` target crawls `aedt_logger`; `desktop_app/` gains the message
      manager surface (`AedtLogger` method pages present)
- [x] `solve_setups` incremental re-run adds the design_xploration managers
      (ParametricSetups, OptimizationSetups) and the missing profile classes
      (AdaptivePass, FrequencySweepProfile, TransientProfile, MemoryGB),
      keeping all ticket-08 pages untouched
- [x] `generic` target crawls `generic.*` + `syslib.nastran_import`; new
      `generic_utils/` category populated
- [x] The runs are incremental per target: no pre-existing page is re-written;
      existing pages are re-fetched only as class-page discovery hubs;
      `git status` after all runs shows zero modifications to previously
      tracked KB pages
- [x] Provenance records appended per run (date, pages fetched/new/kept, corpus
      size); RAG JSONL corpus regenerated and consistent with the per-page files
- [x] `scraping/verify_kb.py` extended with the new checks; all checks pass

## Implementation notes

- New top-up targets in `TOP_UP_TARGETS` (`scraping/generate_pyaedt_ai_context.py`):
  - `modeler`: seeds `API/Primitives3D.html` (links `Modeler3D`) +
    `API/Primitive_Objects.html` (links the `cad.*`, `geometry_operators` and
    `advanced_cad.*` class roots) + `API/visualization/advanced.html` (links the
    remaining `advanced_cad.osm` classes); focus
    `r"/_autosummary/.*\.modeler\.(modeler_3d|cad|geometry_operators|advanced_cad)"`.
  - `logger`: seed `API/DesktopMessenger.html` (links `AedtLogger` +
    `AppFilter`); focus `r"/_autosummary/.*\.aedt_logger"`.
  - `generic`: seed `API/generic.html`; focus
    `r"/_autosummary/.*\.(generic|syslib\.nastran_import)\."`.
  - `solve_setups` (existing target, extended): add `API/Optimetrics.html`
    (links SetupParam/SetupOpti/ParametricSetups/OptimizationSetups) and
    `API/Profiles.html` (links the full profile module) to its seeds, and add
    `ParametricSetups`/`OptimizationSetups` to
    `HFSS_SETUP_CLASSES["design_xploration"]` (single source stays: focus
    patterns and verify presence both derive from it). Re-running the existing
    target is incremental — the 310 ticket-08 pages are skipped as existing.
- Category mapping (`categorize_url`): `modeler.*` → `geometry_modeler`
  (existing); `aedt_logger` → `desktop_app` (existing; the message manager is
  desktop infrastructure); `generic.*` + `syslib.nastran_import` → new
  `generic_utils` category; design_xploration + profile remain
  `setup_and_mesh`.
- Run order: `modeler` → `logger` → `solve_setups` (incremental re-run) →
  `generic`.

## Comments

- 2026-08-02: Filed from a live gap audit: sitemap-at-root diff (`sitemap.xml`,
  8,001 autosummary pages) against the KB on disk (3,292 pages). Complete
  coverage already verified for: `hfss` (307), `hfss3dlayout` (246), the four
  visualization subtrees (1,507), `modules.boundary` incl. excitations (420),
  material/mesh modules, `application.variables` (78), `desktop.Desktop` (63),
  the ticket-08 solve_setup HFSS classes, `SweepHFSS`. Scope (8 groups +
  exclusions) approved by the user.
- 2026-08-02: **DONE.** New `TOP_UP_TARGETS`: `modeler` (seeds Primitives3D +
  Primitive_Objects + visualization/advanced), `logger` (DesktopMessenger),
  `generic` (generic + Configuration + Quantity + nastran_to_stl seeds);
  `solve_setups` extended with the Optimetrics + Profiles gateways and
  `ParametricSetups`/`OptimizationSetups` in `HFSS_SETUP_CLASSES`. New
  `generic_utils` category; `aedt_logger` routed into `desktop_app`.
- **Machinery fix found and made:** the modeler first run stopped at 735
  fetches because pre-existing class-root pages (e.g. `Modeler3D.md`, captured
  by the original full crawl) were skipped at enqueue — but their method pages
  are only reachable through them. Top-up enqueue now re-fetches existing
  **class pages** (PascalCase last component, `is_class_page`) as discovery
  hubs and never re-writes them; existing method pages stay untouched.
  Verified: second modeler run fetched 1,027 pages, wrote 988 new files, kept
  36 existing class hubs byte-identical.
- Runs (all incremental, 0 `[FAILED]` fetches, corpus 6,241 → 8,411 entries):
  modeler 1,027 fetched / 988 new (+36 hubs kept) — `Modeler3D` full method
  surface (`create_box`/`create_cylinder`/`create_region`/...), `cad.*`
  (Object3d/Polyline/elements_3d/ComponentArray/...), `GeometryOperators`
  (57/57), `advanced_cad.*` (SBR+ scene-prep docs); logger 95 / 94 —
  `AedtLogger` + `AppFilter`; solve_setups re-run 123 / 112 — the 15
  design_xploration manager pages + 41 profile pages (AdaptivePass,
  FrequencySweepProfile, TransientProfile, MemoryGB, module functions), the
  465 ticket-08 files untouched; generic 121 / 120, then 127 / 122
  (configurations 38 + numbers_utils `Quantity` 23 — reachable only via the
  `Configuration.html` gateway and the API index, added as seeds), then 11 / 2
  (`syslib.nastran_import.nastran_to_stl` — linked only from the visualization
  gateway).
- Verify: `scraping/verify_kb.py` gained the ticket-09 checks (modeler Surface
  ≥ threshold + four subtree-presence + no circuit modelers; aedt_logger work
  methods; profile QA classes; generic subtree + surface naming); all 30
  checks pass; pre-crawl baseline failed exactly the 8 new checks. Sitemap
  re-diff: **0 of 950 in-scope modeler pages missing**, 0 in-scope gaps in any
  ticket-09 target. Remaining 3,693 un-crawled pages are the documented
  exclusions (other-solver apps ≈ 2,784, circuit/PCB modelers ≈ 546,
  layer_stackup/substrate_circuit/cable_modeling ≈ 124, non-HFSS setup/sweep
  classes per ticket 08).
