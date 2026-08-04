"""Verify the scraped KB against the KB acceptance checks (tickets 03/08/09).

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
- modeler surface populated (Modeler3D/cad/GeometryOperators/advanced_cad;
  was ~1 file before ticket 09; no circuit/schematic pages added)
- message manager populated (aedt_logger; was 0 before ticket 09)
- profile convergence-QA classes present (ticket 09)
- generic utilities populated (generic.* + syslib.nastran_import; was 0)
- provenance readable: scrape date, docs URL tree, documented pyAEDT version
- zero .rst.md stubs (ticket 05 scrub; provenance records it)
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
    """A method/style page has a snake_case final component; class pages are
    PascalCase (the same class-vs-leaf rule the scraper's is_class_page uses)."""
    stem = file_path.stem
    if stem.endswith(".rst"):
        stem = stem[:-4]
    return bool(re.search(r"\.[a-z_][a-z0-9_]*$", stem))


def _missing_class_roots(roots, files):
    """Roots (e.g. 'SetupHFSS') with no file whose dotted name has that root
    as its last-or-prefix component."""
    return [
        r for r in roots
        if not any(re.search(r"\.(?:" + re.escape(r) + r")(?:\.|$)", p.name) for p in files)
    ]


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

    # Ticket 09: modeler surface, message manager, optimetrics managers,
    # profile remainder, generic utilities.
    geom_count = len(md_by_category.get("geometry_modeler", []))
    geom_files = md_by_category.get("geometry_modeler", [])
    # Thresholds halved vs the pre-scrub numbers: before ticket 05 the counts
    # were inflated ~2x by .rst.md stubs (every stub had a real .md twin).
    check("modeler surface crawled (was ~1 file of Modeler3D)", geom_count > 600, f"{geom_count} files in geometry_modeler")
    for prefix, label in (
        ("ansys.aedt.core.modeler.modeler_3d.", "Modeler3D (create_box/cylinder/...)"),
        ("ansys.aedt.core.modeler.cad.", "cad objects (Object3d/Polyline/...)"),
        ("ansys.aedt.core.modeler.geometry_operators.", "GeometryOperators"),
        ("ansys.aedt.core.modeler.advanced_cad.", "advanced_cad (SBR+ scene prep docs)"),
    ):
        check(f"{label} surface present", any(p.name.startswith(prefix) for p in geom_files))
    leaked_modelers = [p.name for p in geom_files
                       if any(p.name.startswith(f"ansys.aedt.core.modeler.{m}.")
                              for m in ("circuits", "schematic"))]
    check("no circuit/schematic modeler pages added",
          not leaked_modelers,
          f"unexpected: {leaked_modelers}" if leaked_modelers else "circuit/schematic modelers absent; PCB/2D modelers excluded by the modeler focus patterns (offline pattern test)")

    desktop_files = md_by_category.get("desktop_app", [])
    check(
        "message manager crawled (aedt_logger)",
        any("aedt_logger" in p.name for p in desktop_files),
        f"{sum('aedt_logger' in p.name for p in desktop_files)} aedt_logger files",
    )
    logger_files = [p for p in desktop_files if "aedt_logger" in p.name]
    check(
        "message read/write methods present",
        any(p.name.startswith("ansys.aedt.core.aedt_logger.AedtLogger.add_") for p in logger_files),
        "AedtLogger.add_* method pages",
    )

    profile_files = [p for p in md_by_category.get("setup_and_mesh", []) if p.name.startswith("ansys.aedt.core.modules.profile.")]
    extra_profile_roots = ["AdaptivePass", "FrequencySweepProfile", "TransientProfile", "MemoryGB"]
    missing_profile = _missing_class_roots(extra_profile_roots, profile_files)
    check("profile convergence-QA classes present", not missing_profile,
          f"missing: {missing_profile}" if missing_profile else "AdaptivePass/FrequencySweepProfile/TransientProfile/MemoryGB present")

    generic_count = len(md_by_category.get("generic_utils", []))
    generic_files = md_by_category.get("generic_utils", [])
    check("generic utilities subtree populated (was 0)", generic_count > 80, f"{generic_count} files")
    check(
        "generic covers generic.* + nastran_import surface",
        bool(generic_files) and all(".generic." in p.name or "syslib.nastran_import" in p.name for p in generic_files),
        f"all {len(generic_files)} files",
    )

    # Ticket 08: report generation, solve setup, plots, advanced visualization.
    check("reports subtree populated (was 0)", reports_count > 350, f"{reports_count} files")
    report_files = md_by_category.get("reports", [])
    check(
        "reports covers visualization.report.* surface",
        bool(report_files) and all("visualization.report" in p.name for p in report_files),
        f"all {len(report_files)} files",
    )

    setup_files = [p for p in md_by_category.get("setup_and_mesh", []) if "modules." in p.name]
    setup_roots = [cls for classes in HFSS_SETUP_CLASSES.values() for cls in classes]
    check("solve-setup surface crawled", setup_count > 250, f"{setup_count} files in setup_and_mesh")
    missing_roots = _missing_class_roots(setup_roots, setup_files)
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

    check("plots subtree populated (was 0)", plots_count > 60, f"{plots_count} files")
    plot_files = md_by_category.get("plots", [])
    check(
        "plots covers visualization.plot.* surface",
        bool(plot_files) and all("visualization.plot" in p.name for p in plot_files),
        f"all {len(plot_files)} files",
    )

    check("advanced visualization subtree populated (was 0)", adv_count > 80, f"{adv_count} files")
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
    check("provenance: .rst.md stub scrub recorded", ".rst.md stub scrub" in prov_text,
          "ticket 05 scrub record present" if ".rst.md stub scrub" in prov_text else "missing scrub record")

    # Ticket 05: the scraper no longer fetches _sources/ re-export pages, so no
    # .rst.md stubs may exist anywhere in the KB.
    stub_files = sorted(p for p in OUTPUT_DIR.rglob("*.rst.md"))
    check("no .rst.md stubs remain (ticket 05)",
          not stub_files,
          f"unexpected: {[str(p.relative_to(OUTPUT_DIR)) for p in stub_files[:5]]}" if stub_files else "stubs pruned; scraper excludes _sources/ pages")

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
