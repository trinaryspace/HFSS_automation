---
name: hfss-agent
description: Drive a complete ANSYS HFSS 3D simulation from a plain-language prompt — clarification up front, stage-by-stage construction in the live AEDT desktop with a visual review gate before any solve, background solves, Result QA, and deliverables (.aedt, plots, summary.md). Use when the user wants an HFSS simulation built greenfield (antenna, filter, RF structure, …), a Re-entry into or modification of an existing AEDT project, a solve / plots / results, or an RCS pivot on this machine's pyAEDT/AEDT stack.
---

# HFSS Agent

Turn one conversation into a complete, correct HFSS simulation on the live AEDT desktop: geometry, materials, excitations, setups, a solved result, and the requested plots — driven by staged scripts through the Spine, with the user reviewing the Math model in the UI before anything solves.

## Read first (in order)

1. This repo's `CONTEXT.md` — the vocabulary. The Spine, Stage, Staged script, Run, Recipe, Project, Design, Model, Workspace, Re-entry, Clarification, Assumption, Review gate, Result QA, Learning loop, Summary are used exactly as defined there.
2. `docs/adr/0001..0005` — settled decisions; the hard rules below quote them.
3. `knowledge/playbook/environment-compat.md` — the compat truth for this machine; **consult it before promising any pyAEDT API** (ADR 0004). The playbook's other entries hold Recipe technique.
4. `scraping/pyaedt_ai_context/` — the KB: how to call each pyAEDT API. It teaches the API, not the design.

## Preconditions — block and escalate if unmet

- UM VPN connected: the license server must be reachable (env-compat “Standing prerequisites”); verify reachability before any run that opens a design or solves.
- AEDT 2024 R1 (`v241`) running or launchable; pyAEDT 1.3.0 via `ansys.aedt.core` (the `pyaedt` alias does not exist — env-compat).
- If a precondition fails, stop and report the evidence; do not work around it.

## Hard rules (ADR-backed)

1. **High-level API only.** Every call goes through `ansys.aedt.core`; never the raw COM surface (SetActiveDesign, GetDesignNames, GetActiveProjectName, GetMessages… are broken over gRPC — env-compat #3). Before promising any API, check the environment-compat entry; route around what it marks unsupported (e.g. RCS/SBR+ — env-compat #12).
2. **Visual Review gate.** The user reviews the built Math model in the AEDT UI — never to the scripts (ADR 0003). Nothing solves until the user passes the gate.
3. **Read-back sync.** After every user UI tweak, introspect the live model and amend the owning stage's script — the sync amends the owning stage so re-running top-to-bottom reproduces the delivered model; record the delta in the summary; no gate closes until sync has run (ADR 0005).
4. **Playbook discipline.** The playbook grows only through the Learning loop's amendment ceremony with explicit user approval (ADR 0002). Nothing appends silently.
5. **Re-entry copies.** Re-entry never opens the original Project: copy it (results included) into the Workspace first, work on the copy only (ADR 0001).
6. **Full parameterization.** All geometry is built with design variables; user tweaks are variable edits — readable, syncable, re-solvable.

## The run — the Spine (Greenfield build)

One Stage = one staged script = one Run. A stage is done when its completion criterion is met **and** the user has seen the stage's state in the open desktop. Walk in order:

1. **Interpret + Clarification** — one block, nothing builds before it. Gather the minimum information, spot critical setup features the user left out, map the request onto a playbook Recipe (or derive a new one), state every Assumption explicitly, and propose the Result QA signals for approval. *Done when: the user confirmed the Recipe, the assumptions, and the QA signals.*
2. **Solution type** — set from the Recipe (e.g. driven Modal; pass it explicitly — env-compat #11).
3. **Design** — create the design in the Workspace Project and save (`remove_lock=True` if a stray lock exists — env-compat #9).
4. **Geometry** — every dimension a design variable; units per recipe.
5. **Materials** — per Recipe; tunables as variables.
6. **Excitations / boundaries** — port strategy per Recipe. Port assignment: pass the **face object** to `wave_port`/`lumped_port`, never ids or edges — env-compat #7.
7. **Mesh** — Recipe mesh operations, or adaptive-only for proof stages.
8. **Setup + sweep** — per Recipe (adaptive passes, delta-S, frequency, sweep range/interp).
9. **Validation** — `validate_simple()` must pass; an invalid design is a failed stage (env-compat #8). Build deterministic: fresh project state or exact rebuild — re-created same-name objects duplicate silently and invalidate.
10. **Review gate** — present the fully built Math model in the AEDT UI; the user inspects and may tweak; run read-back sync on any tweak; *nothing solves until the user passes the gate.*
11. **Solve** — background: `analyze(setup=…, blocking=False)`; its `True` return means *submission*, not completion (env-compat #5). Poll with short status checks: results-on-disk growth is the trustworthy signal; `post.get_solution_data` is flaky — never treat an unfilled SolutionData as final, re-attach (fresh session) for reads and retry (env-compat #6).
12. **Post-process + reports/plots** — Recipe plots, delivered to `results/`.
13. **Result QA** — check the agreed signals: convergence, ports excited, energy pass, in-band resonance, plausibility against the Recipe. Flag anomalies and report them; only the user decides whether results are junk.
14. **Summary** — the acute design decisions + what the Model is; deliverables are the project file, the requested plots, and `summary.md`.

**Re-entry** runs the same ceremony on the copy: introspect the copy and report a model card (designs, solution types, setups, boundaries, materials, variables, existing results) first. A pivot (e.g. antenna → RCS) is a recipe switch — handled as a fresh Clarification.

## Execution mechanics

- **Staged scripts**: one file per stage `NN_<stage>.py` in the Workspace `src/`, carrying the attach-or-launch preamble — see `reference/execution.md` for the preamble and the per-stage checklist. Session state lives in the AEDT project, never in a Python process.
- **Runs and self-correction**: after every Run, read the available error surfaces (high-level exceptions, `validate_simple()`, on-disk logs — raw `GetMessages` is broken, env-compat #3). Cap self-correction at 3 consecutive failed Runs per Stage. Escalate on cap-hit, on the identical error twice in a row, or on an error unmapped to any KB/playbook cause — with the script, the error, and the attempted fixes attached.
- **Release hygiene**: keep the desktop alive across stages (the next staged script's preamble attaches to it); at session end close the session and reap the launched server process (kill-until-gone — env-compat #10). `os._exit` after teardown because gRPC teardown hangs otherwise.
- **Learning loop**: when a user tweak generalizes to the Recipe class, or a backend-compat discovery surfaces, or a QA anomaly's resolution generalizes — fix the current Model first, THEN propose the playbook amendment, and append only after approval. Project-specific values stay in `summary.md`.

## Workspace shape and deliverables

Every conversation gets a Workspace: `src/` (staged scripts), the project file, `results/`, `summary.md`. The template lives in `templates/workspace/` (README + summary skeleton). Tool and knowledge directories stay clean; workspace outputs are gitignored.

## Reference

- `reference/execution.md` — attach-or-launch preamble, per-stage checklist and typical checks, read-back sync detail.
- Pointers live in “Read first” above; the environment-compat entry is the compat authority.
