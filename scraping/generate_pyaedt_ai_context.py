import asyncio
import json
import re
from pathlib import Path
from typing import Set, Dict, List
from urllib.parse import urljoin, urlparse

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

# Base configuration
START_URL = "https://aedt.docs.pyansys.com/version/stable/API/index.html"
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
    ],
    "desktop_app": [
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.desktop",
        r"/_autosummary/.*(pyaedt|ansys\.aedt\.core)\.application",
        r"/API/Desktop\.html",
        r"/API/Application\.html",
    ],
}

ALL_PATTERNS = [pattern for sublist in TARGET_PATTERNS.values() for pattern in sublist]

def categorize_url(url: str) -> str:
    """Categorize URL into appropriate AI context sub-folder."""
    for category, patterns in TARGET_PATTERNS.items():
        if any(re.search(p, url, re.IGNORECASE) for p in patterns):
            return category
    return "general_api"

def is_target_url(url: str) -> bool:
    """Check if URL matches targeted HFSS or shared AEDT modules."""
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != BASE_DOMAIN:
        return False
    
    path = parsed.path
    if any(path.endswith(ext) for ext in [".png", ".jpg", ".zip", ".pdf", ".py", ".css", ".js"]):
        return False

    return any(re.search(pattern, path, re.IGNORECASE) for pattern in ALL_PATTERNS)

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

async def generate_ai_context(max_depth: int = 2, max_concurrent: int = 5):
    """Main crawler loop to build structured AI context repository."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Create subdirectories for categorized context
    for cat in set(TARGET_PATTERNS.keys()) | {"general_api"}:
        (OUTPUT_DIR / cat).mkdir(exist_ok=True)

    visited_urls: Set[str] = set()
    to_visit: Set[str] = {START_URL}
    
    rag_chunks: List[Dict] = []
    page_count = 0

    markdown_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.45, min_word_threshold=8)
    )

    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        css_selector="article.bd-article, main#main-content",
        excluded_tags=["nav", "header", "footer", "aside", "dialog", "script", "style", "form"],
        markdown_generator=markdown_generator,
    )

    print("Starting PyAEDT AI Context Scraper...")
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
                title = result.metadata.get("title", "").replace(" — PyAEDT", "").strip()
                category = categorize_url(url)
                
                raw_md = result.markdown.raw_markdown if result.markdown else ""
                ai_md = clean_markdown_for_ai(raw_md, title, url, category)

                # Generate clean filename based on URL path or title
                url_filename = Path(urlparse(url).path).stem or "index"
                if url_filename.startswith("pyaedt."):
                    url_filename = url_filename.replace("pyaedt.", "")
                
                file_path = OUTPUT_DIR / category / f"{url_filename}.md"
                
                # Write individual markdown context file
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(ai_md)

                # Append to unified RAG JSONL corpus
                rag_chunks.append({
                    "id": f"pyaedt_doc_{page_count}",
                    "title": title,
                    "url": url,
                    "category": category,
                    "filename": str(file_path.relative_to(OUTPUT_DIR)),
                    "content": raw_md
                })

                print(f"  [SAVED] [{category}]: {file_path.name}")

                # Extract internal links for deep crawling
                for link_info in result.links.get("internal", []):
                    href = link_info.get("href", "")
                    full_url = urljoin(url, href).split("#")[0]
                    
                    if full_url not in visited_urls and is_target_url(full_url):
                        to_visit.add(full_url)

    # Write unified RAG knowledge base JSONL file
    jsonl_path = OUTPUT_DIR / "rag_knowledge_base.jsonl"
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for chunk in rag_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print("\n" + "="*60)
    print(f"SUCCESS! PyAEDT AI Context dataset generated successfully.")
    print(f"Total Markdown files: {page_count}")
    print(f"Root Output Path: {OUTPUT_DIR.resolve()}")
    print(f"Unified RAG Dataset: {jsonl_path.resolve()}")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(generate_ai_context(max_depth=3))
