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

- 2026-08-04 — .rst.md stub scrub (ticket 05): 4035 sphinx re-export stub files pruned; the scraper no longer emits them (/_sources/ pages excluded); plain .md pages untouched; RAG corpus rebuilt with 4376 entries
- 2026-08-02 — top-up crawl (generic): 11 pages fetched, 2 new page files written, 7 existing page files kept; RAG corpus rebuilt with 8411 entries
- 2026-08-02 — top-up crawl (generic): 127 pages fetched, 122 new page files written, 3 existing page files kept; RAG corpus rebuilt with 8409 entries
- 2026-08-02 — top-up crawl (generic): 121 pages fetched, 120 new page files written, 0 existing page files kept; RAG corpus rebuilt with 8287 entries
- 2026-08-02 — top-up crawl (solve_setups): 123 pages fetched, 112 new page files written, 9 existing page files kept; RAG corpus rebuilt with 8167 entries
- 2026-08-02 — top-up crawl (logger): 95 pages fetched, 94 new page files written, 0 existing page files kept; RAG corpus rebuilt with 8055 entries
- 2026-08-02 — top-up crawl (modeler): 1027 pages fetched, 988 new page files written, 36 existing page files kept; RAG corpus rebuilt with 7961 entries
- 2026-08-02 — top-up crawl (modeler): 735 pages fetched, 732 new page files written, 0 existing page files kept; RAG corpus rebuilt with 6973 entries
- 2026-08-02 — top-up crawl (advanced): 257 pages fetched, 256 new page files written, 0 existing page files kept; RAG corpus rebuilt with 6241 entries
- 2026-08-02 — top-up crawl (plots): 187 pages fetched, 186 new page files written, 0 existing page files kept; RAG corpus rebuilt with 5985 entries
- 2026-08-02 — top-up crawl (solve_setups): 310 pages fetched, 310 new page files written, 0 existing page files kept; RAG corpus rebuilt with 5799 entries
- 2026-08-02 — top-up crawl (reports): 1391 pages fetched, 1390 new page files written, 0 existing page files kept; RAG corpus rebuilt with 5489 entries
- 2026-08-02 — top-up crawl (materials): 224 pages fetched, 222 new page files written, 2 existing page files kept; RAG corpus rebuilt with 4099 entries
- 2026-08-02 — top-up crawl (visualization): 1184 pages fetched, 1182 new page files written, 0 existing page files kept; RAG corpus rebuilt with 3876 entries
- pre-2026-08-02 — initial full crawl, 2,694 page files; scrape date was not recorded at the time (this provenance file was added 2026-08-02, ticket 03)
