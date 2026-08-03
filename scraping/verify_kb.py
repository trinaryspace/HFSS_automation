"""Verify the scraped KB against the KB acceptance checks (tickets 03 + 08).

Standalone document-level check (this repo has no test framework; the spec's
verification baseline for the KB is file counts per category, provenance
fields present, and corpus consistency):

- postprocessing subtree populated (was 0 before ticket 03)
- materials depth-checked with method sub-pages (was 2 before ticket 03)
- reports subtree populated (ansys.aedt.core.visualization.report.*, was 0)
- solve-setup surfaces in setup_and_mesh (solve_setup/solve_sweeps/
  design_xploration/profile, was 0; other-solver classes still absent)
- plots subtree populated (visualization.plot.*, was 0)
- advanced visualization subtree populated (visualization.advanced.*, was 0)
- provenance readable: scrape date, docs URL tree, documented pyAEDT version
- RAG JSONL corpus consistent with the per-page markdown files

Usage: python verify_kb.py   (exit code 0 = all checks pass)
"""

import json
import re
import sys
from pathlib import Path

from generate_pyaedt_ai_context import (
    HFSS_SETUP_CLASSES,
    NON_HFSS_SETUP_CLASSES,
    split_frontmatter,
)

OUTPUT_DIR = Path(__file__).parent / "pyaedt_ai_context"


def _is_method_page(file_path: Path) -> bool:
    """A method/style page has a snake_case final component; class pages are PascalCase."""
    stem = file_path.stem
    if stem.endswith(".rst"):
        stem = stem[:-4]
    return bool(re.search(r"\.[a-z_][a-z0-9_]*$", stem))


def main() -> int:
    failures = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" \u2014 {detail}" if detail else ""))
        if not cond:
            failures.append(name)

    md_by_category = {
        d.name: sorted(d.glob("*.md"))
        for d in sorted(OUTPUT_DIR.iterdir())
        if d.is_dir()
    }

    post_count = len(md_by_category.get("postprocessing", []))
    mat_count = len(md_by_category.get("materials", []))
    reports_count = len(md_by_category.get("reports", []))
    plots_count = len(md_by_category.get("plots", []))
    adv_count = len(md_by_category.get("advanced_visualization", []))
    setup_count = len(md_by_category.get("setup_and_mesh", []))

    check("postprocessing populated (was 0)", post_count > 100, f"{post_count} files")
    check("materials depth-checked (was 2)", mat_count > 50, f"{mat_count} files")

    viz_files = md_by_category.get("postprocessing", [])
    check(
        "postprocessing covers visualization.post.* surface",
        bool(viz_files) and all("visualization.post" in p.name for p in viz_files),
        f"all {len(viz_files)} files",
    )

    mat_methods = [p for p in md_by_category.get("materials", []) if _is_method_page(p)]
    check("materials method sub-pages captured", len(mat_methods) > 50, f"{len(mat_methods)} method/style pages")

    # Ticket 08: report generation, solve setup, plots, advanced visualization.
    check("reports subtree populated (was 0)", reports_count > 800, f"{reports_count} files")
    report_files = md_by_category.get("reports", [])
    check(
        "reports covers visualization.report.* surface",
        bool(report_files) and all("visualization.report" in p.name for p in report_files),
        f"all {len(report_files)} files",
    )

    setup_files = [p for p in md_by_category.get("setup_and_mesh", []) if "modules." in p.name]
    setup_roots = [cls for classes in HFSS_SETUP_CLASSES.values() for cls in classes]
    check("solve-setup surface crawled", setup_count > 400, f"{setup_count} files in setup_and_mesh")
    missing_roots = [
        r for r in setup_roots
        if not any(
            re.search(r"\.(?:" + re.escape(r) + r")(?:\.|$)", p.name)
            for p in setup_files
        )
    ]
    check("solve-setup class surfaces present", not missing_roots,
          f"missing: {missing_roots}" if missing_roots else "all HFSS-relevant class roots present")
    check(
        "profile module crawled (convergence QA classes)",
        any(p.name.startswith("ansys.aedt.core.modules.profile.") for p in setup_files),
    )
    skipped_setups = [p.name for p in md_by_category.get("setup_and_mesh", [])
                      if any(p.name.startswith(f"ansys.aedt.core.modules.{mod}.{cls}")
                             for mod, classes in NON_HFSS_SETUP_CLASSES.items()
                             for cls in classes)]
    check("other-solver setups skipped", not skipped_setups, f"unexpected: {skipped_setups}" if skipped_setups else "no SetupCircuit/Maxwell/Q3D/3DLayout/SBR pages")

    check("plots subtree populated (was 0)", plots_count > 120, f"{plots_count} files")
    plot_files = md_by_category.get("plots", [])
    check(
        "plots covers visualization.plot.* surface",
        bool(plot_files) and all("visualization.plot" in p.name for p in plot_files),
        f"all {len(plot_files)} files",
    )

    check("advanced visualization subtree populated (was 0)", adv_count > 160, f"{adv_count} files")
    adv_files = md_by_category.get("advanced_visualization", [])
    check(
        "advanced covers visualization.advanced.* surface",
        bool(adv_files) and all("visualization.advanced" in p.name for p in adv_files),
        f"all {len(adv_files)} files",
    )
    check(
        "FfdSolutionData captured (radiation-pattern readout)",
        any("FfdSolutionData" in p.name for p in adv_files),
        "far-field solution data class present",
    )

    prov_path = OUTPUT_DIR / "provenance.md"
    prov_text = prov_path.read_text(encoding="utf-8") if prov_path.exists() else ""
    check("provenance file exists", prov_path.exists())
    check("provenance: scrape date recorded", bool(re.search(r"\d{4}-\d{2}-\d{2}", prov_text)), "YYYY-MM-DD present")
    check(
        "provenance: docs URL tree",
        "https://aedt.docs.pyansys.com/version/stable/" in prov_text,
    )
    check("provenance: documented pyAEDT version", "1.3.0" in prov_text and "ADR 0004" in prov_text)

    # Corpus consistency: one chunk per KB page file; chunk content must equal
    # the page body (file minus frontmatter); filenames must match on both sides.
    corpus_path = OUTPUT_DIR / "rag_knowledge_base.jsonl"
    checked_corpus, checked_files = {}, set()
    if corpus_path.exists():
        seen_ids = set()
        dup_ids, bad_files = [], {}
        for line in corpus_path.read_text(encoding="utf-8").splitlines():
            chunk = json.loads(line)
            if chunk["id"] in seen_ids:
                dup_ids.append(chunk["id"])
            seen_ids.add(chunk["id"])
            checked_corpus[chunk["filename"]] = chunk
            checked_files.add(chunk["filename"])

    disk_files = set()
    for cat, files in md_by_category.items():
        for p in files:
            disk_files.add(str(p.relative_to(OUTPUT_DIR)))
    disk_files.add("provenance.md")

    check("corpus has one entry per KB file", checked_files == disk_files,
          f"{len(disk_files)} files vs {len(checked_files)} chunks")
    check("corpus ids unique", not dup_ids)

    mismatches = []
    for cat, files in md_by_category.items():
        for p in files:
            rel = str(p.relative_to(OUTPUT_DIR))
            if rel not in checked_corpus:
                mismatches.append(rel)
                continue
            chunk = checked_corpus[rel]
            meta, body = split_frontmatter(p.read_text(encoding="utf-8"))
            if chunk["content"] != body or chunk["category"] != meta.get("category", cat):
                mismatches.append(rel)
    check("corpus content consistent with page files", not mismatches,
          f"{len(mismatches)} mismatches" if mismatches else "all page bodies match")

    print()
    if failures:
        print(f"FAILED: {len(failures)} check(s)")
        return 1
    print("ALL KB CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
