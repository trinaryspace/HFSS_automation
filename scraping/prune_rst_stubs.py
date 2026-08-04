"""One-off prune of the .rst.md sphinx re-export stubs (ticket 05, ID 8).

Every `scraping/pyaedt_ai_context/**/*.rst.md` file is a ~280-byte sphinx
re-export of the plain `.md` twin (its content is only frontmatter pointing
at `_sources/...rst.txt`). Delete them all, rebuild the RAG corpus from the
surviving pages, and record the scrub in provenance.md — without re-crawling
the corpus (plain `.md` pages are untouched).

Kept in scraping/ for provenance; re-running when nothing remains to prune is
a no-op (no duplicate provenance record).
"""

from datetime import date
from pathlib import Path

import generate_pyaedt_ai_context as gen

# Anchor to this script's directory so the prune works from any CWD: the
# scraper's OUTPUT_DIR is relative, and rebuild/write_provenance read the
# module global at call time.
gen.OUTPUT_DIR = Path(__file__).parent / "pyaedt_ai_context"
OUTPUT_DIR = gen.OUTPUT_DIR


def main() -> int:
    stubs = sorted(p for p in OUTPUT_DIR.rglob("*.rst.md") if p.is_file())
    if not stubs:
        print("no .rst.md stubs present; nothing to prune (no-op)")
        return 0

    for stub in stubs:
        stub.unlink()

    rebuilt = gen.rebuild_rag_corpus()
    record = (
        f"- {date.today().isoformat()} \u2014 .rst.md stub scrub (ticket 05): "
        f"{len(stubs)} sphinx re-export stub files pruned; the scraper no longer "
        f"emits them (/_sources/ pages excluded); plain .md pages untouched; "
        f"RAG corpus rebuilt with {rebuilt} entries"
    )
    gen.write_provenance(record)

    print(f"pruned {len(stubs)} .rst.md stubs from {OUTPUT_DIR}")
    print(f"RAG corpus rebuilt with {rebuilt} entries; provenance updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
