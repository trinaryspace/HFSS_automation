# Plan: AI-generated HFSS simulations in one conversation

March-statement: get a complete HFSS project (geometry, materials, excitations, setups, solves, plots, results) out of a single conversation with an agent, driven by pyAEDT against a live AEDT 2024 R1 desktop on Windows.

## Confirmed decision stack

**Form & shape**
- Agent-driven: the agent calls pyAEDT directly; the scraped KB (under `scraping/pyaedt_ai_context/`) tells it *which* API call to make.
- One solution-type-agnostic **Spine**: interpret & clarify → solution type → design → geometry → materials → excitations/boundaries → mesh → setup+sweep → solve → post-process → reports/plots.
- Scope: **HFSS 3D** first (proving prototype), **HFSS 3D Layout** second. Nothing else.

**Conversation contract**
- **Clarification**: one up-front block when the prompt is ambiguous. Agent gathers the minimum, notices missing critical setup features, proposes (or derives) a **Recipe**, and states inferrable gaps as **assumptions**. The recipe's Result QA signals are proposed and approved as part of this block.
- **Execution**: staged scripts written to `src/` — one stage = one staged script = one run. Every script carries a standard attach-or-launch preamble (`new_desktop=False` onto the running desktop, else launch). Session state lives in the AEDT project, never in a Python process.
- **Full parameterization**: all geometry is built with design variables, so user tweaks are variable edits — trivially readable, syncable, and re-solvable.
- **Review gate**: before any solve, the user inspects the full, built setup in the AEDT UI and passes or adjusts it.
- **Read-back sync**: after any user UI tweak, the agent introspects the live model (variables, boundaries, excitations, setups, mesh ops) and amends the owning stage's script so re-running top-to-bottom reproduces the final model. The delta is recorded in `summary.md` and feeds the learning loop.
- **Solves**: always launched as a background OS process; the agent polls with short status checks (script log, message manager, results on disk). No solve-time estimation.
- **Self-correction**: cap of 3 consecutive failed runs per stage; the agent reads the AEDT message manager after every run (tool-level success + sim-level error still counts as failure). Escalate on cap-hit, identical error twice in a row, or an error unmapped to any KB/playbook cause — with the staged script, the error, and attempted fixes attached.
- **Result QA**: the agent automatically checks the recipe's physics signals post-solve (convergence, ports excited, energy, in-band resonance, plausibility vs playbook), flags anomalies, and reports them. The user decides if results are junk.
- **Learning loop**: three triggers earn a playbook amendment proposal — (a) a user tweak that generalizes to the recipe class, (b) a backend-compat discovery (lands in the environment-compat entry), (c) a Result-QA anomaly whose resolution generalizes. Fix the current model first, propose, append only on approval. Project-specific values stay in the summary.
- **Re-entry**: copy-first — the original `.aedt` (results folder included) is copied into the workspace as a plain filesystem operation and never opened. Introspection runs on the copy and produces a short **model card** (designs, solution types, setups, boundaries, materials, variables, existing results) reported in conversation. All changes and re-solves happen on the copy. Re-planning upstream layers (e.g. antenna→RCS) is treated as the same ceremony, as a recipe switch.

**Environment & artifacts**
- Local Windows, AEDT 2024 R1, graphical desktop launch, version is `2024.1` to pyAEDT.
- **pyAEDT pinned at 1.3.0** (supports AEDT 2022 R1+; 2024 R1 is in range — see ADR 0004). The KB is scraped from `/version/stable/` docs, which document exactly this pyAEDT line.
- Per-conversation workspace `workspaces/<name>/`: `src/` staged scripts, `<name>.aedt`, `results/`, `summary.md`. Tool + knowledge stay clean.
- Deliverables: `.aedt` + requested plots + a **summary** of the acute design decisions and what the design is.

## Environment tasks (do first)

1. **Fix the broken pyAEDT install**: `pyaedt-1.3.0.dist-info` exists but the `pyaedt/` package directory is missing; `import pyaedt` fails. Reinstall 1.3.0; verify `import pyaedt` and a trivial graphical desktop launch.
2. **Smoke-test matrix against the live 2024.1 backend**: RCS/SBR+ APIs (`get_rcs_data`, `MonostaticRCSExporter`), `analyze(blocking=False)`, and attach-onto-running-desktop behavior. Record every outcome in the playbook's environment-compat entry.
3. **KB top-up crawl**: add a `visualization.*` pattern to the scraper (the post-processing API tree lives at `ansys.aedt.core.visualization.post.*` and is currently absent — 0 files), crawl only that subtree, and depth-check materials method sub-pages. Record KB provenance (scrape date, docs URL, pyAEDT version) in the KB.

## Repository layout (agreed)

```
HFSS_automation/
├── CONTEXT.md              # domain glossary (written)
├── scraping/               # the KB (pyaedt_ai_context/) + scrapers
├── skill/                  # the agent-facing skill definition (markdown + tool wiring)
│   └── hfss-agent/
├── knowledge/
│   └── playbook/           # recipe entries + environment-compat entry (append-only by approval)
├── workspaces/             # one folder per conversation (gitignored outputs)
│   └── <name>/
│       ├── src/            # staged .py scripts
│       ├── <name>.aedt
│       ├── results/
│       └── summary.md
└── docs/adr/               # decision records
```

## Build order

1. **Environment**: the three environment tasks above (fix+pin, smoke-test matrix, KB top-up).
2. **Scaffold**: the hfss-agent skill text encoding the conversation contract above, plus the workspace folder template.
3. **Proof 1 — patch antenna**: inset-fed rectangular patch (~2.4 GHz, FR4, driven modal, radiation boundary) greenfield end-to-end. Exercises every Spine stage, clarification, review gate, background solve, Result QA, summary. Seeds recipe #1 via the clarification block.
4. **Proof 2 — microstrip filter**: second greenfield; recipe #2 is *derived* through clarification — the first test of recipe expansion.
5. **Re-entry**: copy the proof-1 project, add a scatterer, re-solve; then the antenna→RCS recipe switch (recipe #3).
6. **HFSS 3D Layout**: second product through the same Spine.
7. **Playbook enrichment**: seed from canonical EM-simulation texts (parallel, ongoing); expand to more recipes on demand.

## Open items to keep an eye on

- License: a valid AEDT license on this box is a hard prerequisite for every solve.

(Settled by environment task 2: RCS/SBR+ API compat, `new_desktop`/attach behavior. Mooted by copy-first re-entry: 3D Layout duplicate semantics — a file copy works for any project type.)
