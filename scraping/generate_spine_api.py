"""Generate knowledge/playbook/spine-api.md — the distilled pyAEDT reference
behind an HFSS build (ticket 05, Implementation Decision 8).

For every call in the spine set (~35, currently 36 — across the Hfss
lifecycle, geometry modeler primitives, materials, boundaries_and_ports,
setup_and_mesh sweeps, and postprocessing/visualization reports) the
generator extracts from the matching KB page: the signature line, a
one-sentence semantics, and the
environment-compat gotcha entry (knowledge/playbook/environment-compat.md,
ADR 0004) when the call has one. Emits a provenance header (generation date,
KB file count, content hash).

Determinism contract: the spine set is fixed-ordered and the hash input
sorted, so a same-day second run over an unchanged KB produces a
byte-identical file (the provenance header stamps the generation date by
design, so a cross-day rerun changes only that date line).

Usage: python scraping/generate_spine_api.py   (exit code 0 = written)
"""

import hashlib
import re
import sys
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple

KB_DIR = Path(__file__).parent / "pyaedt_ai_context"
PLAYBOOK_DIR = Path(__file__).parent.parent / "knowledge" / "playbook"
EC_FILE = PLAYBOOK_DIR / "environment-compat.md"
OUT_FILE = PLAYBOOK_DIR / "spine-api.md"
HASH_ALGO = "sha256"
MAX_SIGNATURE_CHARS = 620
MAX_DESCRIPTION_CHARS = 220

# The spine call set: (section, display label, KB page path relative to
# KB_DIR without the .md suffix, environment-compat item numbers). Fixed
# order is part of the output contract — do not re-sort.
SPINE_CALLS: List[Tuple[str, str, str, List[int]]] = [
    # --- Hfss lifecycle / desktop -----------------------------------------
    ("Lifecycle & desktop", "Hfss",
     "hfss/ansys.aedt.core.hfss.Hfss", [1, 2, 9, 11]),
    ("Lifecycle & desktop", "Hfss.analyze",
     "hfss/ansys.aedt.core.hfss.Hfss.analyze", [4, 5]),
    ("Lifecycle & desktop", "Hfss.validate_simple",
     "hfss/ansys.aedt.core.hfss.Hfss.validate_simple", [8]),
    ("Lifecycle & desktop", "Hfss.save_project",
     "hfss/ansys.aedt.core.hfss.Hfss.save_project", []),
    ("Lifecycle & desktop", "Hfss.release_desktop",
     "hfss/ansys.aedt.core.hfss.Hfss.release_desktop", [10]),
    ("Lifecycle & desktop", "Hfss.cleanup_solution",
     "hfss/ansys.aedt.core.hfss.Hfss.cleanup_solution", []),
    ("Lifecycle & desktop", "Hfss.change_validation_settings",
     "hfss/ansys.aedt.core.hfss.Hfss.change_validation_settings", []),
    # --- Geometry modeler ---------------------------------------------------
    ("Geometry modeler", "Modeler3D.create_box",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_box", []),
    ("Geometry modeler", "Modeler3D.create_cylinder",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_cylinder", []),
    ("Geometry modeler", "Modeler3D.create_rectangle",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_rectangle", []),
    ("Geometry modeler", "Modeler3D.create_circle",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_circle", []),
    ("Geometry modeler", "Modeler3D.create_polyline",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_polyline", []),
    ("Geometry modeler", "Modeler3D.create_region",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_region", []),
    ("Geometry modeler", "Modeler3D.create_airbox",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_airbox", []),
    ("Geometry modeler", "Modeler3D.thicken_sheet",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.thicken_sheet", []),
    ("Geometry modeler", "Modeler3D.unite",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.unite", []),
    ("Geometry modeler", "Modeler3D.subtract",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.subtract", []),
    ("Geometry modeler", "Modeler3D.duplicate_along_line",
     "geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.duplicate_along_line", []),
    ("Geometry modeler", "Object3d.move",
     "geometry_modeler/ansys.aedt.core.modeler.cad.object_3d.Object3d.move", []),
    # --- Materials -----------------------------------------------------------
    ("Materials", "Material.update",
     "materials/ansys.aedt.core.modules.material.Material.update", []),
    ("Materials", "Materials.add_material",
     "materials/ansys.aedt.core.modules.material_lib.Materials.add_material", []),
    # --- Boundaries & ports ----------------------------------------------------
    ("Boundaries & ports", "Hfss.wave_port",
     "hfss/ansys.aedt.core.hfss.Hfss.wave_port", [7, 8]),
    ("Boundaries & ports", "Hfss.assign_radiation_boundary_to_objects",
     "hfss/ansys.aedt.core.hfss.Hfss.assign_radiation_boundary_to_objects", []),
    ("Boundaries & ports", "Hfss.assign_finite_conductivity",
     "hfss/ansys.aedt.core.hfss.Hfss.assign_finite_conductivity", []),
    ("Boundaries & ports", "Hfss.assign_perfecte_to_sheets",
     "hfss/ansys.aedt.core.hfss.Hfss.assign_perfecte_to_sheets", []),
    # --- Setup & mesh -----------------------------------------------------------
    ("Setup & mesh", "Hfss.create_setup",
     "hfss/ansys.aedt.core.hfss.Hfss.create_setup", []),
    ("Setup & mesh", "Hfss.create_linear_count_sweep",
     "hfss/ansys.aedt.core.hfss.Hfss.create_linear_count_sweep", []),
    ("Setup & mesh", "Setup.update",
     "setup_and_mesh/ansys.aedt.core.modules.solve_setup.Setup.update", []),
    ("Setup & mesh", "SweepHFSS",
     "setup_and_mesh/ansys.aedt.core.modules.solve_sweeps.SweepHFSS", []),
    ("Setup & mesh", "Mesh.assign_length_mesh",
     "setup_and_mesh/ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh", []),
    ("Setup & mesh", "Mesh.assign_skin_depth",
     "setup_and_mesh/ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth", []),
    # --- Postprocessing, reports & readout --------------------------------------
    ("Postprocessing, reports & readout", "PostProcessor3D.create_report",
     "postprocessing/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.create_report", []),
    ("Postprocessing, reports & readout", "PostProcessor3D.create_report_from_configuration",
     "postprocessing/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.create_report_from_configuration", []),
    ("Postprocessing, reports & readout", "PostProcessor3D.get_solution_data",
     "postprocessing/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.get_solution_data", [6]),
    ("Postprocessing, reports & readout", "SolutionData",
     "postprocessing/ansys.aedt.core.visualization.post.solution_data.SolutionData", [6]),
    ("Postprocessing, reports & readout", "AedtLogger.get_messages",
     "desktop_app/ansys.aedt.core.aedt_logger.AedtLogger.get_messages", []),
]

# Sphinx links are [label](href) or [label](href "title"); the title may
# contain escaped parens ("\(in Python v3.11\)"), so the optional title is
# matched as a quoted string rather than any-( non-quote run.
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\" ]+)(?:\s+\"[^\"]*\")?\)")


def demark(text: str) -> str:
    """Strip Sphinx markdown links, keeping the display label."""
    return LINK_RE.sub(r"\1", text)


def clean_signature(raw: str) -> str:
    """Signature line minus Sphinx link/emphasis noise, single-spaced.

    Sphinx italicizes parameter markers as _param_, including defaults
    (``_name : str = None_``); strip the marker underscores at word-token
    boundaries (``_x`` after open/sep, ``x_`` before close/sep).
    """
    sig = demark(raw)
    sig = re.sub(r"(?<=[\s(,])_(\w)", r"\1", sig)  # opening _param
    sig = re.sub(r"_\*", "*", sig)                  # the **_kwargs marker
    sig = re.sub(r"(\w|')_(?=[\s,)])", r"\1", sig)  # closing param_ (after word or quoted default)
    sig = re.sub(r"\(_", "(", sig)
    sig = re.sub(r"_\)", ")", sig)
    sig = re.sub(r"\(\s+", "(", sig)
    sig = re.sub(r"\s+", " ", sig).strip()
    if len(sig) > MAX_SIGNATURE_CHARS:
        cut = sig.rfind(" ", 0, MAX_SIGNATURE_CHARS)
        sig = sig[:cut] + " \u2026"
    return sig


def first_sentence(text: str) -> str:
    """First sentence of a doc paragraph, links stripped, length-capped."""
    desc = re.sub(r"\s+", " ", demark(text)).strip()
    if not desc:
        return ""
    sentence = re.split(r"(?<=[.])\s+(?=[A-Z])", desc, maxsplit=1)[0]
    if len(sentence) > MAX_DESCRIPTION_CHARS:
        cut = sentence.rfind(" ", 0, MAX_DESCRIPTION_CHARS)
        sentence = sentence[:cut] + " \u2026"
    return sentence


def extract_page(path: Path) -> Tuple[str, str]:
    """Return (clean signature, one-line description) from a KB page file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    head_idx = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if head_idx is None:
        raise ValueError(f"no '# ' heading in {path}")
    rest = lines[head_idx + 1 :]
    sig = ""
    desc_lines: List[str] = []
    sig_seen = False
    for line in rest:
        s = line.strip()
        if not s:
            # Blank right after the (single-line) signature separates it from
            # the description paragraph; blank after the paragraph ends it.
            if sig_seen and desc_lines:
                break
            continue
        if not sig_seen:
            sig = s
            sig_seen = True
            if "(" not in sig:
                raise ValueError(f"signature line looks wrong in {path}: {s[:80]!r}")
        else:
            desc_lines.append(s)
    if not sig_seen:
        raise ValueError(f"no signature line found in {path}")
    return clean_signature(sig), first_sentence(" ".join(desc_lines))


def kb_pages() -> List[Path]:
    """All KB page files — *.md, .rst.md stubs excluded, provenance excluded."""
    return sorted(
        p for p in KB_DIR.rglob("*.md")
        if p.is_file() and not p.name.endswith(".rst.md") and p.name != "provenance.md"
    )


def kb_content_hash(pages: List[Path]) -> str:
    """sha256 over each page's relative path + content, in sorted order."""
    digest = hashlib.new(HASH_ALGO)
    for page in pages:
        digest.update(str(page.relative_to(KB_DIR)).encode("utf-8"))
        digest.update(b"\0")
        digest.update(page.read_bytes())
    return digest.hexdigest()


def load_ec_items() -> Dict[int, str]:
    """Environment-compat matrix items: {number: heading title}."""
    text = EC_FILE.read_text(encoding="utf-8")
    return {int(n): title.strip() for n, title in
            re.findall(r"^### (\d+)\.\s+(.+)$", text, re.MULTILINE)}


def anchor_from_heading(title: str) -> str:
    """GitHub-slugger anchor for a '### N. Title' heading.

    Lowercase, drop punctuation (em dashes included, leaving their
    surrounding spaces), then spaces to hyphens WITHOUT collapsing runs —
    GitHub anchors '— WORKS' as '--works', and collapsing would 404 the link.
    """
    slug = re.sub(r"[^a-z0-9 -]", "", title.lower())
    slug = re.sub(r" ", "-", slug)
    return slug.strip("-")


def build_doc(pages: List[Path]) -> str:
    ec_items = load_ec_items()
    out: List[str] = []
    out.append("# Spine API \u2014 the verified call set behind an HFSS build")
    out.append("")
    out.append(
        "Distilled reference for the hfss-agent Spine: script authoring reads "
        "this file instead of crawling `scraping/pyaedt_ai_context/` (analysis "
        "\u00a76); per-file KB reads happen only for off-spine calls. Each entry: "
        "signature + one-line semantics + the environment-compat gotchas that "
        "apply on this machine (ADR 0004). Generated, do not hand-edit."
    )
    out.append("")
    out.append("## Provenance")
    out.append("")
    out.append(f"- Generated: {date.today().isoformat()} by `scraping/generate_spine_api.py`")
    out.append(
        f"- KB files: {len(pages)} (markdown pages under `scraping/pyaedt_ai_context/`, "
        ".rst.md stubs and provenance.md excluded)"
    )
    out.append(f"- KB content hash ({HASH_ALGO}): {kb_content_hash(pages)}")
    out.append(f"- Spine call count: {len(SPINE_CALLS)}; regenerate in the KB top-up ceremony")
    out.append("")

    section = None
    for sec_name, label, rel, ec_nums in SPINE_CALLS:
        if sec_name != section:
            section = sec_name
            out.append(f"## {section}")
            out.append("")
        page = KB_DIR / f"{rel}.md"
        if not page.exists():
            raise FileNotFoundError(f"spine KB page missing (re-scrape?): {page}")
        sig, desc = extract_page(page)
        out.append(f"### {label}")
        out.append(f"`{sig}`")
        out.append(desc)
        kb_link = f"../scraping/pyaedt_ai_context/{rel}.md"
        refs = []
        for n in ec_nums:
            if n not in ec_items:
                raise ValueError(f"environment-compat item {n} not found for {label}")
            title = ec_items[n]
            refs.append(f"[EC#{n} {title}](environment-compat.md#{anchor_from_heading(f'{n}. {title}')})")
        suffix = " \u00b7 ".join(refs)
        out.append(f"KB: `{rel}.md`" + (f" \u00b7 EC gotchas: {suffix}" if suffix else ""))
        out.append("")
    return "\n".join(out)


def main() -> int:
    if not EC_FILE.exists():
        raise FileNotFoundError(f"environment-compat entry missing: {EC_FILE}")
    pages = kb_pages()
    doc = build_doc(pages)
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(doc, encoding="utf-8", newline="\n")
    print(f"wrote {OUT_FILE.resolve()}")
    print(f"{len(SPINE_CALLS)} spine calls extracted from {len(pages)} KB pages")
    print(f"{len(doc.encode('utf-8'))} bytes, sha256 {kb_content_hash(pages)[:16]}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
