# Spec: HFSS automation foundation — environment, hfss-agent skill, Proof 1

Status: ready-for-agent
Feature: hfss-agent-foundation

## Problem Statement

I am an EM engineer who wants to describe a simulation in plain language and, within that conversation, receive a complete, correct HFSS model: geometry, materials, excitations, setups, a real solved result, and the standard plots. The design of that pipeline is settled and recorded (PLAN.md, the glossary in CONTEXT.md, and five ADRs), but nothing that runs exists yet, and this machine cannot run it today:

- pyAEDT is registered at version 1.3.0 but the package files are missing — `import pyaedt` fails, so no script can drive the desktop at all.
- The scraped API knowledge base is incomplete: the entire post-processing tree (`ansys.aedt.core.visualization.post.*`) has zero files because the scraper's URL patterns match nothing there, and the materials subtree has only 2 files.
- The behavior of modern pyAEDT APIs against the installed AEDT 2024 R1 backend is unverified — building the skill on unverified assumptions would make it silently promise APIs the backend does not deliver.

Until these are fixed and the skill exists, every conversation fails on the first run.

## Solution

Deliver the foundation in three layers, accepted end-to-end by Proof 1:

1. **Environment.** Fix the pyAEDT install (pinned at 1.3.0) and verify `import pyaedt` plus a trivial graphical desktop launch on the live AEDT 2024 R1. Run the one-time smoke-test matrix against the live backend and record every outcome in the playbook's environment-compat entry. Top up the knowledge base (post-processing visualization subtree, materials depth check, provenance).
2. **Scaffold.** The hfss-agent skill text encoding the conversation contract (Spine, Clarification, staged scripts, review gate, read-back sync, background solves, self-correction, Result QA, learning loop), the per-conversation Workspace template, and the playbook store seeded with the environment-compat entry.
3. **Proof 1.** One greenfield conversation — an inset-fed rectangular patch antenna (~2.4 GHz, FR4, driven modal, radiation boundary; Recipe #1, derived through Clarification) — walked through every Spine stage to a solved result with requested plots, a summary, and re-runnable staged scripts.

## User Stories

1. As an EM engineer, I want `import pyaedt` to succeed on this machine at the pinned 1.3.0 version, so that every later stage can actually drive the AEDT desktop.
2. As an EM engineer, I want a trivial graphical desktop launch script to open AEDT 2024 R1 and create a throwaway model, so that the whole environment is proven workable before any meaningful work starts.
3. As an EM engineer, I want the smoke-test matrix to run once against the live 2024 R1 backend, so that every API I might be offered is verified against the backend I actually have.
4. As an EM engineer, I want the smoke-test outcomes recorded in the playbook's environment-compat entry, so that future conversations know which APIs work, which are broken, and how to route around them.
5. As an EM engineer, I want the `analyze(blocking=False)` behavior verified and documented, so that background solves with polling are built on fact, not hope.
6. As an EM engineer, I want the "attach onto the running desktop" behavior verified and documented, so that staged script re-runs reuse the open session exactly as the conversation contract promises.
7. As an EM engineer, I want the `get_rcs_data` / `MonostaticRCSExporter` surface probed against the 2024 R1 backend, so that the skill never promises RCS/SBR+ features the backend cannot deliver (ADR 0004).
8. As an EM engineer, I want the knowledge base's post-processing subtree crawled (`ansys.aedt.core.visualization.post.*`), so that plotting and report stages can be written with accurate API facts instead of guesses.
9. As an EM engineer, I want the materials subtree depth-checked and backfilled, so that material assignment stages have the full method surface documented.
10. As an EM engineer, I want provenance (scrape date, docs URL tree, documented pyAEDT version) recorded with the knowledge base, so that the trailing edge of its facts is knowable.
11. As an EM engineer, I want the hfss-agent skill to encode the one solution-type-agnostic Spine (interpret → clarify → solution type → design → geometry → materials → excitations → mesh → setup/sweep → solve → post-process → reports), so that every conversation walks the same ordered ceremony.
12. As an EM engineer, I want the Clarification to be one up-front block that proposes or derives a Recipe and states inferrable gaps as explicit assumptions, so that I confirm the design intent once instead of re-answering per stage.
13. As an EM engineer, I want the Result QA signals proposed and approved as part of that block, so that "good enough" is agreed before the solve, not argued after.
14. As an EM engineer, I want execution to be staged scripts — one Stage, one script, one run — each carrying a standard attach-or-launch preamble, so that each run is short, checkable, and crash-recoverable.
15. As an EM engineer, I want all geometry built with design variables, so that any tweak of mine is a variable edit — trivially readable and re-solvable.
16. As an EM engineer, I want a review gate before any solve where I inspect the fully built model in the AEDT UI — the visuals, not the scripts — so that I judge geometry quality the way I already do, by looking (ADR 0003).
17. As an EM engineer, I want read-back sync after any UI tweak of mine, so that the owning stage's script is amended to match the live model and running top-to-bottom still reproduces what I approved (ADR 0005).
18. As an EM engineer, I want solves launched as background OS processes with short status polls, so that the desktop stays usable and the conversation is never hung on progress bars.
19. As an EM engineer, I want self-correction capped at three consecutive failed runs per stage, with the message manager read after every run, so that bounded retries fix fixable things and escalate the rest with the script, error, and attempts attached.
20. As an EM engineer, I want Result QA to automatically check the recipe's physics signals post-solve (convergence, ports excited, energy, in-band resonance, plausibility vs playbook) and report anomalies, so that junk results are flagged before I waste time believing them.
21. As an EM engineer, I want the three learning-loop triggers honored — a generalizing user tweak, a backend-compat discovery, a generalizable QA anomaly — and playbook amendments appended only after my approval, so that the playbook stays the reproducibility contract (ADR 0002).
22. As an EM engineer, I want the Workspace template — staged scripts in `src/`, the `.aedt`, `results/`, `summary.md` — created per conversation, so that tool and knowledge stay clean and each conversation's outputs are self-contained.
23. As an EM engineer, I want the deliverables to be the `.aedt`, the requested plots, and a summary of the acute design decisions, so that the design survives the conversation.
24. As an EM engineer, I want Proof 1 to walk the full Spine end-to-end in one conversation and return a solved patch antenna at ~2.4 GHz, so that I know the whole system works before it is trusted with anything more.
25. As an EM engineer, I want Recipe #1 (patch antenna) itself to be the product of Proof 1's Clarification, so that the recipe shelf starts with a recipe that was actually exercised.
26. As an EM engineer, I want a user UI tweak injected at Proof 1's review gate and the read-back sync demonstrating the script amendment, so that the sync machinery is proven, not assumed.
27. As an EM engineer, I want Proof 1's Result QA to confirm the in-band resonance and convergence and report them in the summary, so that the acceptance signals are visible in the artifact itself.
28. As an EM engineer, I want the staged scripts of Proof 1 replayed top-to-bottom in a fresh workspace to reproduce the delivered model, so that "re-runnable record" is a tested property, not a claim.
29. As an EM engineer, I want the learning-loop machinery exercised at least once by Proof 1's outcome, so that the loop is open for real discoveries rather than wired up dead.

## Implementation Decisions

1. **pyAEDT pin and repair.** pyAEDT is pinned at 1.3.0 (ADR 0004). The environment fix is a clean reinstall of that pinned version so `import pyaedt` succeeds (the installed dist-info is registered but the package directory is missing). The trivial graphical desktop launch against AEDT 2024 R1 (version `2024.1`) is the hard gate: if it fails, all downstream work in this spec is blocked and the failure is escalated to the user with the traceback, since no script can run otherwise.
2. **Knowledge base source stays put.** The KB remains scraped from the `/version/stable/` docs tree, which documents exactly the pinned client line (ADR 0004) — no re-crawl of the whole tree is needed, only the missing subtree.
3. **Smoke-test matrix (one-time knowledge seam).** The probes are: import + trivial desktop launch; attach-onto-running-desktop semantics; `analyze(blocking=False)` non-blocking behavior; the RCS/SBR+ data surface (`get_rcs_data`, `MonostaticRCSExporter`) — expected to fail against 2024 R1 per ADR 0004 — plus any additional APIs the scaffold needs, discovered as they come up. Each probe runs once against the live backend; the outcome (works / broken / behavior notes) is recorded in the playbook's environment-compat entry. The matrix is a one-time fact-gathering run, not an automated suite.
4. **Environment-compat entry.** The playbook store is created with exactly one entry populated by the matrix — the environment-compat entry — and otherwise-empty recipe shelves. It is the single accumulation point for backend-compat facts (ADR 0004) and the source of truth the skill consults before promising an API. Playbook growth beyond this entry happens only through the learning loop's approved-amendment ceremony (ADR 0002). Note: entries under the environment-compat heading are also amended through the same ceremony, but the matrix is its own pre-approved seeding of that entry.
5. **KB top-up crawl.** The scraper gains a `visualization` pattern covering the `ansys.aedt.core.visualization.post.*` subtree (verified: the current postprocessing patterns match zero URLs); an incremental crawl runs over that subtree only. The materials subtree gets a depth check of method sub-pages (verified: 2 files today). Provenance — scrape date, docs URL tree, documented pyAEDT version — is recorded with the KB (in the KB itself). KB outputs keep their existing category layout and the RAG JSONL corpus is regenerated so it stays in sync with the markdown files.
6. **hfss-agent skill encodes the conversation contract.** The skill text (in the `skill/` directory per the approved layout) encodes, in this order: the Spine (one solution-type-agnostic order of stages); the single Clarification block that proposes or derives the Recipe, states gaps as Assumptions, and proposes the Result QA signals for approval; staged scripts (one Stage = one script = one Run) with the standard attach-or-launch preamble; session state living in the AEDT project, never in a Python process; full parameterization of geometry via design variables; the visual review gate (ADR 0003); read-back sync that introspects the live model (variables, boundaries, excitations, setups, mesh ops) after user UI tweaks and amends the owning stage's script, recording the delta in `summary.md` (ADR 0005); background solves with short status polls; self-correction capped at 3 consecutive failed Runs per Stage with the message manager read after every Run; Result QA against the approved signals; and the three learning-loop triggers.
7. **Workspace template.** A per-conversation Workspace holds `src/` (staged scripts), the `<name>.aedt` project file, `results/`, and `summary.md`. Workspace artifacts are gitignored outputs; tool and knowledge directories stay clean.
8. **Recipe #1 seeding.** Recipe #1 (inset-fed rectangular patch, ~2.4 GHz, FR4, driven modal, radiation boundary) is derived through Proof 1's Clarification block — the Clarification is the seeding ceremony, and the user's approval of the proposed signals at that block satisfies ADR 0002's approval requirement.
9. **Proof 1 scope.** The greenfield build exercises every Spine stage with the live desktop: clarification → solution type → design → geometry → materials → excitations/boundaries → mesh → setup + sweep → solve (background) → post-process → reports/plots → Result QA → summary. It includes one deliberate user UI tweak at the review gate to prove read-back sync, and the replay of the final staged scripts in a fresh Workspace to prove re-runnability.

## Testing Decisions

- **What makes a good test here:** external, user-visible behavior — a run of the pipeline and a check of its physics output, judged at the seams below. Script internals are never the test surface; the user is the final judge of whether results are junk, with the agent reporting the QA signals (per PLAN.md).
- **Seam 1 — environment probe (lowest, the gate):** `import pyaedt` at 1.3.0 succeeds, then a trivial script launches the graphical desktop, creates a throwaway design, and exits cleanly. Failure of this probe blocks everything else in this spec.
- **Seam 2 — smoke-test matrix (mid, knowledge):** the probe list in Implementation Decisions runs once against the live 2024 R1 backend. "Pass" is not binary: each probe's outcome is recorded in the environment-compat entry with enough fidelity that the skill can decide promise-vs-route-around (ADR 0004). An expected gap recorded is a good outcome; an unrecorded assumption is the failure mode.
- **Seam 3 — Proof 1 (highest, the acceptance seam):** a full greenfield conversation through the entire Spine. Pass requires all of: (a) Result QA signals green — S11 minimum in band at ~2.4 GHz within the agreed tolerance, driven-modal convergence, port excited, energy pass, plausibility vs the recipe; (b) deliverables on disk — the solved `.aedt`, the requested plots, and `summary.md` with the design decisions; (c) re-runnability — the final staged scripts replayed top-to-bottom in a fresh Workspace reproduce the delivered model, including the post-sync state after the injected UI tweak.
- **Prior art:** none in the repo — this is the first code. The verification baseline is the live AEDT desktop itself (a solve that converges is the test), plus document-level checks: KB file counts per category (postprocessing subtree populated, materials backfilled, provenance fields present), and the environment-compat entry containing a record per matrix probe.
- **Prerequisite:** a valid AEDT license on the box — every solve depends on it; Proof 1 cannot pass without one, and its absence must be raised with the user rather than worked around.

## Out of Scope

- Proof 2 (microstrip filter) and the second Recipe — a follow-on spec (build order step 4).
- Re-entry (copy-first per ADR 0001), the antenna→RCS recipe switch, and any RCS/SBR+ solve (build order steps 5).
- HFSS 3D Layout (build order step 6).
- Playbook enrichment from canonical EM-simulation texts (build order step 7).
- Any automated/CI test harness — no remote, one-time probes only.
- Upgrading AEDT (a license/IT decision, ADR 0004) and procuring licenses.

## Further Notes

- Verified facts this spec rests on (recorded in the handoff, re-confirmed at spec time): pip registers pyaedt 1.3.0 but `import pyaedt` raises ModuleNotFoundError; the KB has 2,695 files with `postprocessing` at 0 and `materials` at 2; the KB's postprocessing URL patterns match the `visualization.post` subtree nowhere.
- The plan's remaining open item stands: license availability on this box is unverified and is the hard prerequisite for every solve.
- If the smoke matrix reveals unexpected gaps beyond RCS/SBR+, the skill text must encode "route around, don't promise" for each — degrading silently would violate the environment-compat trust model (ADR 0004).
- Proof 1's `summary.md` seeds the learning-loop machinery (deltas, QA anomalies) — but playbook content grows only via approved amendments (ADR 0002), so Proof 1's discoveries must not bypass the ceremony.

## Comments

- 2026-08-02: Spec synthesized from PLAN.md, CONTEXT.md, ADRs 0001–0005, and the grilling-session handoff. Scope, issue-tracker location, and the three test seams confirmed with the user. Published with Status: ready-for-agent.
