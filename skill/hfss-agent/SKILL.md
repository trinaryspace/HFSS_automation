---
name: hfss-agent
description: Use when the user wants a complete ANSYS HFSS 3D simulation in one conversation — a greenfield EM structure (antenna, filter, RF part, …), a Re-entry into or modification of an existing AEDT project (an RCS pivot included), or a solve / plots / results for one. Walks the Spine with a single up-front Clarification, stage-by-stage construction on the live AEDT desktop, a visual Review gate before any solve, background solves, Result QA, and deliverables (.aedt, plots, summary.md).
---

# HFSS Agent

Turn one conversation into a complete, correct HFSS simulation on the live AEDT desktop: geometry, materials, excitations, setups, a solved result, and the requested plots — driven by staged scripts through the Spine, with the user reviewing the Math model in the UI before anything solves.

## Read first (in order)

1. This repo's `CONTEXT.md` — the vocabulary. The Spine, Stage, Staged script, Run, Recipe, Project, Design, Model, Workspace, Re-entry, Clarification, Assumption, Review gate, Result QA, Learning loop, Summary are used exactly as defined there.
2. `docs/adr/0001..0005` — settled decisions; the hard rules below quote them.
3. `knowledge/playbook/environment-compat.md` — the compat truth for this machine; **consult it before promising any pyAEDT API** (ADR 0004). The playbook's other entries hold Recipe technique.
4. `scraping/pyaedt_ai_context/` — the KB: how to call each pyAEDT API. It teaches the API, not the design.
5. **User-provided reference papers** — when the user drops PDFs (papers, book chapters) into `knowledge/reference-papers/`, run the `analyze-papers` skill (installed globally) on them and read the resulting agent notes before Clarification; they are context, and only a user-approved Learning-loop proposal may turn them into playbook amendments.

## Preconditions — block and escalate if unmet

- UM VPN connected: the license server must be reachable (env-compat “Standing prerequisites”); verify reachability before any run that opens a design or solves.
- AEDT 2024 R1 (`v241`) running or launchable; pyAEDT 1.3.0 via `ansys.aedt.core` (the `pyaedt` alias does not exist — env-compat).
- If a precondition fails, stop and report the evidence; do not work around it.

## Hard rules (ADR-backed)

1. **High-level API only.** Every call goes through `ansys.aedt.core`; never the raw COM surface (SetActiveDesign, GetDesignNames, GetActiveProjectName, GetMessages… are broken over gRPC — env-compat #3). Before promising any API, check the environment-compat entry; route around what it marks unsupported (e.g. RCS/SBR+ — env-compat #12).
2. **Visual Review gate.** The user reviews the built Math model in the AEDT UI — never to the scripts (ADR 0003). Nothing solves until the user passes the gate.
3. **Read-back sync.** After every user UI tweak, introspect the live model — the sync amends the owning stage's script so re-running top-to-bottom reproduces the delivered model; record the delta in the summary; no gate closes until sync has run (ADR 0005).
4. **Playbook discipline.** The playbook grows only through the Learning loop's amendment ceremony with explicit user approval (ADR 0002). Nothing appends silently.
5. **Re-entry copies.** Re-entry never opens the original Project: copy it (results included) into the Workspace first, work on the copy only (ADR 0001).
6. **Full parameterization.** All geometry is built with design variables; user tweaks are variable edits — readable, syncable, re-solvable.

## The run — the Spine (Greenfield build)

One Stage = one staged script = one Run. A stage is done when its completion criterion below is met **and** the user has seen the stage's state in the open desktop. Walk in order; a failed completion criterion makes the stage a failed Run (see self-correction).

1. **Interpret + Clarification** — one block, nothing builds before it. Gather the minimum information, spot critical setup features the user left out, map the request onto a playbook Recipe (or derive a new one), state every Assumption explicitly, and propose the Result QA signals for approval. *Done when: the user confirmed the Recipe, the assumptions, and the QA signals.*
2. **Solution type** — set from the Recipe, explicitly (never the default — env-compat #11). *Done when: the design reports the Recipe's type.*
3. **Design** — create the design in the Workspace Project and save (`remove_lock=True` if a stray lock exists — env-compat #9). *Done when: the project file exists on disk with the named design.*
4. **Geometry** — every dimension a design variable; units per recipe. *Done when: the Model's solids match the Recipe in the UI and each dimension is a variable, not a literal.*
5. **Materials** — per Recipe; tunables as variables. *Done when: each solid reports its Recipe material.*
6. **Excitations / boundaries** — port strategy per Recipe; port assignment by **face object** on a solid's face — never ids/edges, and beware sheet-port auto-integration (env-compat #7/#8). *Done when: the ports/boundaries list matches the Recipe.*
7. **Mesh** — Recipe mesh operations, or adaptive-only for proof stages. *Done when: the mesh operations list matches the Recipe (or is deliberately empty).*
8. **Setup + sweep** — per Recipe (adaptive passes, delta-S, frequency, sweep range/interp). *Done when: `existing_analysis_sweeps` shows the named setup with its sweep.*
9. **Validation** — `validate_simple()` must pass; an invalid design is a failed stage (env-compat #8). Build deterministic: fresh project state or exact rebuild — re-created same-name objects duplicate silently and invalidate. *Done when: validation returns True.*
10. **Review gate** — present the fully built Math model in the AEDT UI; the user inspects and may tweak; run read-back sync on any tweak; *nothing solves until the user passes the gate.* *Done when: the user passed the gate and sync is complete.*
11. **Solve** — background: `analyze(setup=…, blocking=False)`; its `True` return means *submission*, not completion (env-compat #5). Poll with short status checks: results-on-disk growth is the trustworthy signal; `post.get_solution_data` is flaky — never treat an unfilled SolutionData as final; re-attach (fresh session) for reads and retry (env-compat #6). Never estimate solve time — poll only. *Done when: independent completion signals appear on disk.*
12. **Post-process + reports/plots** — Recipe plots, delivered to `results/`. *Done when: each requested plot exists in `results/`.*
13. **Result QA** — check the agreed signals: convergence, ports excited, energy pass, in-band resonance, plausibility against the Recipe. Flag anomalies and report them; only the user decides whether results are junk. *Done when: every agreed signal is reported (or explicitly "unreadable — flaky readout") and anomalies are surfaced.*
14. **Summary** — the acute design decisions + what the Model is; deliverables are the project file, the requested plots, and `summary.md`. *Done when: `summary.md` is written per the template.*

**Re-entry** runs the same ceremony on the copy: introspect the copy and report a model card (designs, solution types, setups, boundaries, materials, variables, existing results) first. A pivot (e.g. antenna → RCS) is a recipe switch — handled as a fresh Clarification.

## Execution mechanics

- **Staged scripts**: one file per stage `NN_<stage>.py` in the Workspace `src/`, carrying the attach-or-launch preamble and following the per-stage checklist — both in `reference/execution.md`. Session state lives in the AEDT project, never in a Python process.
- **Runs and self-correction**: after every Run, read the available error surfaces (high-level exceptions, `validate_simple()`, on-disk logs — the raw message manager is read via those surfaces; `GetMessages` itself is broken, env-compat #3). Cap self-correction at 3 consecutive failed Runs per Stage; escalate on the cap, on the identical error twice in a row, or on an error unmapped to any KB/playbook cause — with the script, the error, and the attempted fixes attached. Full detail: `reference/execution.md`.
- **Release hygiene**: keep the desktop alive across stages (the next staged script's preamble attaches to it); at session end close the session and reap the launched server process (kill-until-gone — env-compat #10). `os._exit` after teardown because gRPC teardown hangs otherwise. Full preamble: `reference/execution.md`.
- **Learning loop**: when a user tweak generalizes to the Recipe class, or a backend-compat discovery surfaces, or a QA anomaly's resolution generalizes — fix the current Model first, THEN propose the playbook amendment, and append only after approval. Project-specific values stay in `summary.md`. Triggers and ceremony: `reference/execution.md`.

## Workspace shape and deliverables

Every conversation gets a Workspace: `src/` (staged scripts), the project file, `results/`, `summary.md`. The template lives in `templates/workspace/` (README + summary skeleton). Tool and knowledge directories stay clean; workspace outputs are gitignored.

## Reference

- `reference/execution.md` — attach-or-launch preamble, per-stage checklist and typical checks, read-back sync, self-correction, learning-loop triggers.
- Pointers live in “Read first” above; the environment-compat entry is the compat authority.
