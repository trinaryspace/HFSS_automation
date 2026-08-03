# 10 — User-provided reference papers: runtime KB top-up via analyze-papers

**What to build:** the agent can absorb new domain knowledge at runtime — the user
drops PDFs (academic papers, textbook chapters) into `knowledge/reference-papers/`
and the conversation uses them to guide Recipe choice, geometry generation, and
setup design (e.g. a bowtie patch antenna from a paper). The hfss-agent skill
runs the globally installed `analyze-papers` skill (drives the Literature_analyzer
CLI, agent notes to `<analyzer repo>/agent_out`) on every PDF in that folder and
reads the resulting agent notes **before Clarification**. Notes are context only;
turning a paper's technique into the playbook still requires the user-approved
Learning-loop amendment ceremony (ADR 0002).

**Blocked by:** None (no AEDT or license involved; needs only the `analyze-papers`
skill and the Literature_analyzer CLI, both present on this machine)

**Status:** ready-for-agent

- [x] `knowledge/reference-papers/` exists with a README documenting the
      drop-PDF-in flow (tracked; only user-supplied PDFs live here)
- [x] `skill/hfss-agent/SKILL.md` "Read first" rule #5 instructs: run
      `analyze-papers` on the folder, read the agent notes before Clarification,
      propose user-approved Learning-loop amendments before any playbook write
- [x] `skill/hfss-agent/reference/execution.md` Clarification checklist points at
      the folder + skill so the stage actually acts on the rule
- [x] Deployed copy `~/.agents/skills/hfss-agent/` is in sync (rule #5 present —
      the earlier deploy predated the wiring)
- [x] `verify_skill.py` extended with reference-papers checks (SKILL rule markers,
      README flow, Clarification-reference marker); all 37 checks pass
- [x] End-to-end chain verified: `lit-analyzer.exe process --json <folder>` on a
      PDF folder → manifest (`lit-analyzer.process-manifest/v1`) with `agent_note`
      path; re-runs are cache-hit, $0, instant

## Implementation notes

- Why this is separate from tickets 03/08/09: the KB there is the *scraped pyAEDT
  API documentation* (teaches the API, not the design). This feature is the
  user-facing knowledge top-up: primary-source design context (geometry,
  materials, test setups) injected per-conversation. The spec's "playbook
  enrichment from EM texts" remains out of scope — this feature is the
  non-amending ingest path that feeds Context/Recipe without touching the
  playbook contract.
- The `analyze-papers` skill lives in the sibling Literature_analyzer repo
  (`skill/analyze-papers/`, installed at `~/.agents/skills/analyze-papers/`).
  Invocation contract: `<bin> process --json <folder>`, stdout = one JSON
  manifest (v1), prose on stderr, exit 0 = all ok. Hard rule: never
  `uv run`/`uv sync` inside that repo (CUDA-PyTorch venv); call
  `.venv/Scripts/lit-analyzer.exe` directly.
- Verification used a cached sample PDF from the analyzer's own `papers/` (hit
  the existing cache → $0, instant) staged in a temp folder — deliberately NOT
  committed into `knowledge/reference-papers/`, which stays user-PDF-only.
- First real ingestion is expected at the manual test or Proof 1 (user's own
  paper, e.g. a patch/bowtie antenna reference).

## Comments

- 2026-08-02: Filed and implemented in one session. The wiring (README + SKILL
  rule #5) existed uncommitted from a prior session; this ticket completed it:
  execution-reference pointer, deployed-copy sync (the deployed hfss-agent was
  stale — rule #5 was absent), structural checks in `verify_skill.py` (37 pass),
  and a live CLI end-to-end (cached PDF: manifest + agent note read back,
  `cached: true`, `cost_usd: null`).
