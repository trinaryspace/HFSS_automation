# 03 — KB top-up: visualization subtree, materials depth check, provenance

**What to build:** the scraped knowledge base is complete enough to support every later stage. The scraper gains a `visualization` pattern covering the post-processing API tree (`ansys.aedt.core.visualization.post.*` — today zero files are captured because the existing patterns match nothing there), an incremental crawl runs over that subtree only, the materials subtree gets a depth check of its method sub-pages (today only 2 files), and provenance (scrape date, docs URL tree, documented pyAEDT version) is recorded with the KB. The unified RAG corpus is regenerated so it stays in sync with the per-page files.

**Blocked by:** None — can start immediately (scraping does not touch the desktop or license)

**Status:** ready-for-agent

- [x] Post-processing category has files covering the `ansys.aedt.core.visualization.post.*` surface (count moves from 0 to non-trivial)
- [x] Materials category grows beyond 2 files, with method sub-pages captured
- [x] Provenance fields (scrape date, docs URL tree, documented pyAEDT version) are readable in the KB output
- [x] The crawl is incremental — only the missing subtree and depth-check targets are fetched; the existing 2,600+ pages are not re-crawled
- [x] RAG JSONL corpus is regenerated and consistent with the per-page markdown files

## Comments

- 2026-08-02: **DONE.** Scraper (`scraping/generate_pyaedt_ai_context.py`) gained a `visualization` pattern
  (`/API/visualization/_autosummary/...visualization.post.*` — the docs moved the post-processing tree to
  `ansys.aedt.core.visualization.post`, which no older pattern matched) plus `--topup {visualization,materials}`
  incremental mode: gateway seeds are fetched only for link discovery, only focus-pattern links are followed,
  and pages that already exist on disk are never re-fetched or re-written. Runs end by rebuilding the RAG
  JSONL corpus from the per-page markdown files and appending a provenance record (scrape date, docs tree,
  documented pyAEDT line = stable docs → pinned client 1.3.0 per ADR 0004) to `provenance.md`.
- Runs: visualization top-up 1,184 fetched / 1,182 new (`postprocessing/` 0 → 1,182 files, seed gateways
  not stored); materials top-up 224 fetched / 222 new, 2 existing class pages kept untouched (was 2 → 224
  files). `git status` after both runs: no pre-existing tracked page modified. Corpus 2,694 → 4,099 entries.
- Checks: `scraping/verify_kb.py` (document-level seam: category counts, provenance fields, corpus ↔ files
  consistency, one chunk per file) passes all 11 checks; corpus content per chunk equals the page file body.
