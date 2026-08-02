# 03 — KB top-up: visualization subtree, materials depth check, provenance

**What to build:** the scraped knowledge base is complete enough to support every later stage. The scraper gains a `visualization` pattern covering the post-processing API tree (`ansys.aedt.core.visualization.post.*` — today zero files are captured because the existing patterns match nothing there), an incremental crawl runs over that subtree only, the materials subtree gets a depth check of its method sub-pages (today only 2 files), and provenance (scrape date, docs URL tree, documented pyAEDT version) is recorded with the KB. The unified RAG corpus is regenerated so it stays in sync with the per-page files.

**Blocked by:** None — can start immediately (scraping does not touch the desktop or license)

**Status:** ready-for-agent

- [ ] Post-processing category has files covering the `ansys.aedt.core.visualization.post.*` surface (count moves from 0 to non-trivial)
- [ ] Materials category grows beyond 2 files, with method sub-pages captured
- [ ] Provenance fields (scrape date, docs URL tree, documented pyAEDT version) are readable in the KB output
- [ ] The crawl is incremental — only the missing subtree and depth-check targets are fetched; the existing 2,600+ pages are not re-crawled
- [ ] RAG JSONL corpus is regenerated and consistent with the per-page markdown files
