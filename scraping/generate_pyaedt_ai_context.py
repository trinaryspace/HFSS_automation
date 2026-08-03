import argparse
import asyncio
import json
import re
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

# Base configuration
START_URL = "https://aedt.docs.pyansys.com/version/stable/API/index.html"
DOCS_TREE_URL = "https://aedt.docs.pyansys.com/version/stable/"
BASE_DOMAIN = "aedt.docs.pyansys.com"
OUTPUT_DIR = Path("pyaedt_ai_context")

# Targeted URL patterns matching PyAEDT HFSS and shared infrastructure (supporting both pyaedt and ansys.aedt.core namespaces)
TARGET_PATTERNS = {
    "hfss": [
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.hfss",
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.hfss3dlayout",
    ],
    "geometry_modeler": [
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.modeler",
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.primitives",
        r"/API/Primitives\.html",
    ],
    "setup_and_mesh": [
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.(modules\.)?(SetupTemplates|Mesh)",
        r"/API/Setup\.html",
        r"/API/Mesh\.html",
    ],
    "boundaries_and_ports": [
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.(modules\.)?Boundary",
        r"/API/Boundaries\.html",
    ],
    "materials": [
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.(modules\.)?Material",
        r"/API/Material\.html",
    ],
    "postprocessing": [
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.(modules\.)?PostProcessor",
        r"/API/PostProcessor\.html",
        # visualization pattern: the post-processing API tree lives at
        # ansys.aedt.core.visualization.post.* (docs path
        # /API/visualization/_autosummary/...); no older pattern matches it.
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.visualization\.post",
    ],
    "desktop_app": [
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.desktop",
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.application",
        r"/API/Desktop\.html",
        r"/API/Application\.html",
    ],
}

ALL_PATTERNS = [pattern for sublist in TARGET_PATTERNS.values() for pattern in sublist]

# Incremental top-up targets: a "focus" set of URL patterns and gateway seed
# pages. A top-up crawl follows only links matching the focus patterns (plus
# the seeds themselves, used for link discovery) and never re-writes pages
# that already exist on disk. Focus patterns must be a subset of the full
# pattern set (every focus-matching page is stored under the category its
# ALL-pattern match picks).
TOP_UP_TARGETS = {
    "visualization": {
        "focus_patterns": [
            r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.visualization\.post",
        ],
        "seeds": [
            DOCS_TREE_URL + "API/Visualization.html",
            DOCS_TREE_URL + "API/visualization/post.html",
        ],
    },
    "materials": {
        "focus_patterns": TARGET_PATTERNS["materials"],
        "seeds": [
            DOCS_TREE_URL + "API/_autosummary/ansys.aedt.core.modules.material.Material.html",
            DOCS_TREE_URL + "API/_autosummary/ansys.aedt.core.modules.material.MatProperty.html",
            DOCS_TREE_URL + "API/_autosummary/ansys.aedt.core.modules.material.MatProperties.html",
            DOCS_TREE_URL + "API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.html",
            DOCS_TREE_URL + "API/_autosummary/ansys.aedt.core.modules.material.SurfMatProperties.html",
            DOCS_TREE_URL + "API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.html",
        ],
    },
}

def categorize_url(url: str) -> str:
    """Categorize URL into appropriate AI context sub-folder."""
    for category, patterns in TARGET_PATTERNS.items():
        if any(re.search(p, url, re.IGNORECASE) for p in patterns):
            return category
    return "general_api"


def is_target_url(url: str, patterns: Optional[List[str]] = None) -> bool:
    """Check if URL matches target patterns (defaults to the full set)."""
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != BASE_DOMAIN:
        return False

    path = parsed.path
    if any(path.endswith(ext) for ext in [".png", ".jpg", ".zip", ".pdf", ".py", ".css", ".js"]):
        return False

    return any(re.search(pattern, path, re.IGNORECASE) for pattern in (patterns or ALL_PATTERNS))


def page_output_path(url: str) -> Path:
    """Path where a page would be stored under the KB, mirroring the write logic."""
    url_filename = Path(urlparse(url).path).stem or "index"
    if url_filename.startswith("pyaedt."):
        url_filename = url_filename.replace("pyaedt.", "")
    return OUTPUT_DIR / categorize_url(url) / f"{url_filename}.md"


def clean_markdown_for_ai(raw_md: str, title: str, url: str, category: str) -> str:
    """Format markdown for LLM consumption with clean frontmatter and stripped Sphinx noise."""
    # Clean Sphinx link anchors like [¶](#header) or [#]
    cleaned = re.sub(r"\[¶\]\([^)]+\)", "", raw_md)
    cleaned = re.sub(r"\[#\]\([^)]+\)", "", cleaned)

    # Remove consecutive blank lines
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()

    # Prepend structured YAML metadata frontmatter for RAG / Agent ingestion
    frontmatter = f"""---
title: "{title}"
url: "{url}"
category: "{category}"
domain: "PyAEDT / HFSS"
---

"""
    return frontmatter + cleaned


def split_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    """Return (frontmatter dict, body) for a KB page file. Empty dict if no frontmatter."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    meta: Dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip('"')
    return meta, text[end + 5:]


def rebuild_rag_corpus() -> int:
    """Regenerate the RAG JSONL corpus from the per-page markdown files on disk.

    Reads every KB page file (category sub-folders) plus provenance.md, so the
    corpus is always consistent with the KB files as they exist now.
    """
    chunks: List[Dict] = []
    page_count = 0

    for cat_dir in sorted(p for p in OUTPUT_DIR.iterdir() if p.is_dir()):
        for md_file in sorted(cat_dir.glob("*.md")):
            text = md_file.read_text(encoding="utf-8")
            meta, body = split_frontmatter(text)
            page_count += 1
            chunks.append({
                "id": f"pyaedt_doc_{page_count}",
                "title": meta.get("title", ""),
                "url": meta.get("url", ""),
                "category": meta.get("category", cat_dir.name),
                "filename": str(md_file.relative_to(OUTPUT_DIR)),
                "content": body,
            })

    provenance_file = OUTPUT_DIR / "provenance.md"
    if provenance_file.exists():
        page_count += 1
        chunks.append({
            "id": f"pyaedt_doc_{page_count}",
            "title": "Knowledge base provenance",
            "url": "",
            "category": "provenance",
            "filename": "provenance.md",
            "content": provenance_file.read_text(encoding="utf-8"),
        })

    jsonl_path = OUTPUT_DIR / "rag_knowledge_base.jsonl"
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    return page_count


def write_provenance(record: str) -> None:
    """Prepend a crawl-run record to provenance.md, preserving the run history verbatim."""
    provenance_file = OUTPUT_DIR / "provenance.md"
    if provenance_file.exists():
        current = provenance_file.read_text(encoding="utf-8")
        history = []
        in_runs = False
        for line in current.splitlines():
            if line.startswith("## Crawl runs"):
                in_runs = True
                continue
            if in_runs and line.startswith("## "):
                in_runs = False
                continue
            if in_runs and line.strip():
                history.append(line.strip())
    else:
        history = [
            "- pre-2026-08-02 \u2014 initial full crawl, 2,694 page files; "
            "scrape date was not recorded at the time (this provenance file "
            "was added 2026-08-02, ticket 03)"
        ]

    if record not in history:
        history.insert(0, record)
    notes = "\n".join(history)

    doc = f"""# Knowledge base provenance

The trailing edge of the facts in this corpus is knowable from this file.

## Sources

- Docs tree: {DOCS_TREE_URL} (Sphinx autosummary + API overview pages)
- Docs index: {START_URL}
- Documented pyAEDT line: the `stable` tree documents the current release
  line; the pinned client on this machine is pyAEDT 1.3.0, importable as
  `ansys.aedt.core` (ADR 0004)
- Generator: `scraping/generate_pyaedt_ai_context.py` (crawl4ai)

## Crawl runs

{notes}
"""
    provenance_file.write_text(doc, encoding="utf-8")


async def generate_ai_context(
    max_depth: int = 3,
    seed_urls: Optional[List[str]] = None,
    focus_patterns: Optional[List[str]] = None,
    skip_existing: bool = False,
    top_up_label: Optional[str] = None,
):
    """Build or top-up the structured AI context repository.

    Full crawl (default): seeds the API index and follows every internal link
    matching the full pattern set, overwriting pages as it goes.
    Top-up crawl (--topup): seeds the target's gateway pages, follows only
    links matching the focus patterns, and never re-writes existing pages.
    """
    seeds = list(seed_urls) if seed_urls else [START_URL]
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Create subdirectories for categorized context
    for cat in set(TARGET_PATTERNS.keys()) | {"general_api"}:
        (OUTPUT_DIR / cat).mkdir(exist_ok=True)

    visited_urls: Set[str] = set()
    to_visit: Set[str] = set(seeds)

    page_count = 0
    existing_skipped = 0
    written_new = 0

    markdown_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.45, min_word_threshold=8)
    )

    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        css_selector="article.bd-article, main#main-content",
        excluded_tags=["nav", "header", "footer", "aside", "dialog", "script", "style", "form"],
        markdown_generator=markdown_generator,
    )

    mode = f"top-up crawl ({top_up_label})" if top_up_label else "full crawl"
    print(f"Starting PyAEDT AI Context Scraper ({mode})")
    print(f"Target Output Directory: {OUTPUT_DIR.resolve()}\n")

    async with AsyncWebCrawler(verbose=False) as crawler:
        for depth in range(max_depth + 1):
            if not to_visit:
                break

            current_batch = list(to_visit - visited_urls)
            to_visit.clear()

            print(f"Depth {depth}: Scraping {len(current_batch)} pages...")

            results = await crawler.arun_many(urls=current_batch, config=crawl_config)

            for result in results:
                url = result.url
                visited_urls.add(url)

                if not result.success:
                    print(f"  [FAILED] {url}")
                    continue

                page_count += 1
                title = (result.metadata or {}).get("title", "").replace(" — PyAEDT", "").strip()
                category = categorize_url(url)

                raw_md = result.markdown.raw_markdown if result.markdown else ""
                ai_md = clean_markdown_for_ai(raw_md, title, url, category)

                file_path = page_output_path(url)
                write_page = is_target_url(url) or not skip_existing
                if write_page and not (skip_existing and file_path.exists()):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(ai_md)
                    written_new += 1
                    print(f"  [SAVED] [{category}]: {file_path.name}")
                elif skip_existing and file_path.exists():
                    existing_skipped += 1
                    print(f"  [EXISTS] [{category}]: {file_path.name} (kept)")

                # Extract internal links for deep crawling
                for link_info in result.links.get("internal", []):
                    href = link_info.get("href", "")
                    full_url = urljoin(url, href).split("#")[0]

                    if full_url not in visited_urls and is_target_url(full_url, focus_patterns):
                        if skip_existing and page_output_path(full_url).exists():
                            continue
                        to_visit.add(full_url)

    written = rebuild_rag_corpus()
    record = (
        f"{date.today().isoformat()} \u2014 {mode}: {page_count} pages fetched, "
        f"{written_new} new page files written, {existing_skipped} existing page files kept; "
        f"RAG corpus rebuilt with {written} entries"
    )
    write_provenance(record)

    print("\n" + "=" * 60)
    print(f"SUCCESS! PyAEDT AI Context dataset generated successfully.")
    if top_up_label:
        print(f"Total pages fetched ({mode}, incl. link-discovery seeds): {page_count}")
    else:
        print(f"Total Markdown files: {page_count}")
    print(f"Root Output Path: {OUTPUT_DIR.resolve()}")
    print(f"Unified RAG Dataset: {(OUTPUT_DIR / 'rag_knowledge_base.jsonl').resolve()}")
    print(f"Provenance: {OUTPUT_DIR / 'provenance.md'}")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape the PyAEDT /version/stable/ docs into the KB "
        "(full crawl by default, or an incremental --topup of one subtree)."
    )
    parser.add_argument(
        "--topup",
        choices=sorted(TOP_UP_TARGETS),
        default=None,
        help="incremental crawl of one subtree only; existing pages are never re-crawled",
    )
    parser.add_argument("--max-depth", type=int, default=3)
    args = parser.parse_args()

    if args.topup:
        target = TOP_UP_TARGETS[args.topup]
        asyncio.run(
            generate_ai_context(
                max_depth=args.max_depth,
                seed_urls=target["seeds"],
                focus_patterns=target["focus_patterns"],
                skip_existing=True,
                top_up_label=args.topup,
            )
        )
    else:
        asyncio.run(generate_ai_context(max_depth=args.max_depth))
