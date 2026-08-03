# Knowledge base provenance

The trailing edge of the facts in this corpus is knowable from this file.

## Sources

- Docs tree: https://aedt.docs.pyansys.com/version/stable/ (Sphinx autosummary + API overview pages)
- Docs index: https://aedt.docs.pyansys.com/version/stable/API/index.html
- Documented pyAEDT line: the `stable` tree documents the current release
  line; the pinned client on this machine is pyAEDT 1.3.0, importable as
  `ansys.aedt.core` (ADR 0004)
- Generator: `scraping/generate_pyaedt_ai_context.py` (crawl4ai)

## Crawl runs

- 2026-08-02 — top-up crawl (materials): 224 pages fetched, 222 new page files written, 2 existing page files kept; RAG corpus rebuilt with 4099 entries
- 2026-08-02 — top-up crawl (visualization): 1184 pages fetched, 1182 new page files written, 0 existing page files kept; RAG corpus rebuilt with 3876 entries
- pre-2026-08-02 — initial full crawl, 2,694 page files; scrape date was not recorded at the time (this provenance file was added 2026-08-02, ticket 03)
