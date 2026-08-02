import asyncio
import json
import re
from pathlib import Path
from typing import Set, List
from urllib.parse import urljoin, urlparse

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

# Base configuration
START_URL = "https://aedt.docs.pyansys.com/version/stable/API/index.html"
BASE_DOMAIN = "aedt.docs.pyansys.com"
OUTPUT_DIR = Path("pyaedt_hfss_docs")

# Regex patterns targeting HFSS and supporting core modules
# - API index & high-level overview pages
# - Hfss / Hfss3dLayout classes
# - Modeler / Geometry / Primitives (modeler, primitives, geometry)
# - Setup, Mesh, Boundaries, Ports, PostProcessor, Material, Desktop
TARGET_URL_PATTERNS = [
    r"/API/(index|Application|CoreModules|Primitives|Setup|Mesh|PostProcessor|Material|Boundaries|Desktop|Common)\.html",
    r"/_autosummary/pyaedt\.Hfss",
    r"/_autosummary/pyaedt\.Hfss3dLayout",
    r"/_autosummary/pyaedt\.modeler",
    r"/_autosummary/pyaedt\.modules",
    r"/_autosummary/pyaedt\.application",
    r"/_autosummary/pyaedt\.desktop",
]

def is_target_url(url: str) -> bool:
    """Check if the URL belongs to HFSS or supporting PyAEDT core features."""
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != BASE_DOMAIN:
        return False
    
    # Ignore non-HTML resources or external anchors
    path = parsed.path
    if any(path.endswith(ext) for ext in [".png", ".jpg", ".zip", ".pdf", ".py", ".css", ".js"]):
        return False

    return any(re.search(pattern, path, re.IGNORECASE) for pattern in TARGET_URL_PATTERNS)

async def crawl_pyaedt_hfss_docs(max_depth: int = 2, max_concurrent: int = 5):
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    visited_urls: Set[str] = set()
    to_visit: Set[str] = {START_URL}
    extracted_docs = []

    # Configure Crawl4AI markdown generator to filter out Sphinx UI noise
    markdown_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.48, min_word_threshold=10)
    )

    # Configure crawler run to target main Sphinx content container & ignore nav header/footer
    crawl_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        css_selector="article.bd-article, main#main-content, div.document",
        excluded_tags=["nav", "header", "footer", "aside", "dialog", "script", "style"],
        markdown_generator=markdown_generator,
    )

    async with AsyncWebCrawler(verbose=True) as crawler:
        for depth in range(max_depth + 1):
            if not to_visit:
                break
                
            current_batch = list(to_visit - visited_urls)
            to_visit.clear()
            
            print(f"\n--- Depth {depth}: Crawling {len(current_batch)} URLs ---")
            
            # Process batch concurrently
            results = await crawler.arun_many(
                urls=current_batch,
                config=crawl_config
            )

            for result in results:
                url = result.url
                visited_urls.add(url)

                if not result.success:
                    print(f"[FAILED] {url} - Error: {result.error_message}")
                    continue

                print(f"[SUCCESS] Crawled: {url}")

                # Extract markdown content for AI context
                markdown_content = result.markdown.raw_markdown if result.markdown else ""
                
                # Save structured metadata & clean markdown content
                doc_item = {
                    "url": url,
                    "title": result.metadata.get("title", ""),
                    "content": markdown_content
                }
                extracted_docs.append(doc_item)

                # Extract internal links for next depth iteration
                internal_links = result.links.get("internal", [])
                for link_info in internal_links:
                    href = link_info.get("href", "")
                    full_url = urljoin(url, href).split("#")[0]  # strip fragment anchors
                    
                    if full_url not in visited_urls and is_target_url(full_url):
                        to_visit.add(full_url)

    # Save aggregated knowledge base JSON for AI Agent Context
    kb_file = OUTPUT_DIR / "pyaedt_hfss_knowledge_base.json"
    with open(kb_file, "w", encoding="utf-8") as f:
        json.dump(extracted_docs, f, indent=2, ensure_ascii=False)
        
    print(f"\nCompleted! Total pages scraped: {len(extracted_docs)}")
    print(f"Saved aggregated knowledge base to: {kb_file.resolve()}")

if __name__ == "__main__":
    asyncio.run(crawl_pyaedt_hfss_docs(max_depth=2))
