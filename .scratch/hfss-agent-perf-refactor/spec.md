# Spec: HFSS agent performance refactor — cost & time optimization

Status: ready-for-agent
Feature: hfss-agent-perf-refactor

## Problem Statement

The hfss-agent skill delivers a complete HFSS simulation in one long conversation, but the measured cost of doing so is pathological. Two runs against the live AEDT desktop (2026-08-02/03, model `accounts/fireworks/models/deepseek-v4-flash-0731`) consumed **1,352,762 tokens / ~2.3 h** (`playful-river`) and **398,130 tokens / ~1.6 h** (`silent-engine`). Analysis (`docs/hfss-agent-performance-analysis.md`) shows the cost is not the model but the loop:

- **Context growth without a lifecycle.** 152 steps, no compaction; the conversation grew to ~500 k tokens and ~260 k tokens were re-read on every step (39.2 M cache-read tokens).
- **Reasoning overflow.** The session ran `variant: max`; 695 KB of reasoning traces (35% of the conversation store) on a flash model, including a 78.9 KB block on a trivial step.
- **Solve orchestration eaten alive.** Foreground PowerShell poll loops silently hit the tool's 120-second bash timeout, the agent then fought process detach (WMI), re-submitted the solve 4 times, double-solved once (a solve was already in flight on the user's desktop), and burned ~30 steps and ~1 h on what is a two-file jobspec problem.
- **KB discovery by brute force.** ~20 steps listing an 8,411-file corpus to find API doc filenames; 48% of the corpus is `.rst.md` stubs; `ripgrep` is not installed.
- **Three wipe-and-rebuild chains** from the EC#8 same-name duplication trap; **36 steps** in the read-back-sync verify ceremony with two killed desktops.

The refactor turns these into deterministic, bounded, measurable machinery. Success is defined by measured acceptance thresholds on one pilot run, not by vibes.

## Solution

Rebuild the conversation shell around five doctrines, all accepted in the grilling session (2026-08-04):

1. **Phase sessions.** One conversation becomes three named sessions — Clarification; Build (through the Review gate incl. read-back sync); Solve+QA — each starting fresh and carrying only the **State ledger** (`state.md`) plus relevant files.
2. **Deterministic runners for the dangerous parts.** The solve runs under a detached watchdog writing `results/state/solve_progress.txt`; sync-verify runs as one script (`capture_state.py` → `model_snapshot.json`, `12_verify_sync.py` replays + diffs on a port-pinned second desktop). The agent reads `PASS:`/state lines, never process-wrangles.
3. **Verification contract.** Every staged script ends in one machine-parseable `PASS:` line with assertions; a static py_compile/import gate runs before any AEDT launch; bash calls take explicit timeouts and caps on output.
4. **Idempotent stages.** Delete-then-create per object replaces wipe-and-rebuild as the default (ADR 0008); the EC#8 route-around changes accordingly.
5. **Tiered cognition.** Main loop stays `deepseek-v4-flash` at `variant: low`; two cheap-model subagents (`kb-lookup`, `runcard`) absorb memory-free work; verbosity caps cut prose.

Plus KB tooling (`.rst.md` scrub at the scraper, `ripgrep` install, generated `spine-api.md` distilled reference with provenance) and a measurement harness whose **run card** is appended to `summary.md` so every run is comparable.

User stories and full decision detail: see the grilling record in `docs/hfss-agent-performance-analysis.md` §7 and this feature's tickets.

## User Stories

1. As the maintainer, I want a fresh greenfield run of the same problem class (bowtie ~3.5 GHz) to cost **≥50% fewer billed tokens** than `silent-engine`'s 398,130, so that the refactor visibly pays for itself.
2. As the maintainer, I want it to take **≥40% fewer steps** and **≥40% less wall time excluding solver physics** than baseline, so that the conversation time shrinks, not just the bill.
3. As the maintainer, I want the run card (tokens, steps, wall time) appended to `summary.md` by a harness, so that every future run is comparable without manual archaeology.
4. As the maintainer, I want the solve phase to proceed without a single foreground poll loop or process-detach hack, so that the 30-step solve saga cannot recur.
5. As the maintainer, I want the read-back sync verified by a deterministic runner comparing `model_snapshot.json` against a replayed copy, so that the 36-step two-desktop saga cannot recur.
6. As the maintainer, I want a pre-submit guard that refuses to double-solve when a solve already looks in-flight, so that the hour-long stall cannot recur.
7. As the maintainer, I want every staged script to emit one `PASS:` line and to be idempotent, so that self-correction is one step and rebuild chains are unnecessary.
8. As the maintainer, I want the KB findable via `rg -l`, `.rst.md` stubs ignored, and a generated `spine-api.md`, so that script generation reads ~10 KB once instead of ~20 discovery steps.
9. As the maintainer, I want the main loop's reasoning budget capped (`variant: low`, verbosity caps), so that the 695 KB of reasoning traces shrink.
10. As the maintainer, I want the spec/ADR/glossary set (0006–0008 + three terms) published, so that the new doctrines are decision-carrying and discoverable.

## Implementation Decisions

1. **Phase sessions (ADR 0007).** Session 1: Clarification → locked Recipe/Assumptions/QA-signals + Ledger written. Session 2: build stages → Review gate → read-back sync (Level-set: sync runs in session 2; the delta is recorded in the Ledger and summary). Session 3: solve submission + watchdog + QA + summary + run card. Sessions are named (`<workspace>-clarify|build|solve`) and resume-points are only the Ledger.
2. **State ledger.** `workspaces/<name>/state.md` — stage progress, locked parameters/variables, pitfalls hit, snapshot pointer, pending decisions. Owned by the agent per stage; at most ~2 KB. Machine state stays in `results/state/*.txt` (process id, port, solve progress, etc.).
3. **Solve watchdog (ADR 0006).** `08_solve.py` cleans stale results (`cleanup_solution`), probes for an in-flight solve (results-dir age + solver processes; asks the user before submitting if one looks live), submits `analyze(blocking=False)`, launches the watchdog detached, exits. `poll_solve.py` (detached via `Start-Process`, owned PID recorded) updates `solve_progress.txt` from recursive `.asol`/`.sd` growth every ~20 s and exits on completion/stall signal. The agent reads `solve_progress.txt` and polls nothing.
4. **Sync verify runner.** `capture_state.py` writes `model_snapshot.json` (objects + bboxes + materials + boundaries + setups/sweeps + variables) from the live model; `12_verify_sync.py` replays the amended scripts on a fresh copy on a port-pinned second desktop, captures the same shape, diffs, prints one `PASS:`/`FAIL:` line, tears down port-pinned (user's desktop untouchable). Snapshot doubles as solve-session handoff and QA input.
5. **Verification contract.** Per-stage `PASS: <stage> <assertions>` line (objects exist, bbox sane, `validate_simple()`); static gate `py_compile` + import-check all `src/*.py` before any AEDT launch; bash calls that can exceed ~90 s pass an explicit timeout; no full recursive directory listings (count/size summaries, `tail`, state files only).
6. **Idempotent stages (ADR 0008).** Each script deletes the objects/boundaries/setups/mesh-ops/sweeps it (re)creates before creating them; wipe-and-rebuild demoted to an explicit escalation tool; execution.md EC#8 route-around rewritten.
7. **Tiered cognition (same model, cheaper thinking).** Main loop: `accounts/fireworks/models/deepseek-v4-flash-0731` pinned, `variant: low` (verify availability with `opencode models`; if unsupported, record and keep current, output caps still apply). Subagents in opencode.json: `kb-lookup` (read-only; exact-signature-or-"not found" contract; spot-checked on the pilot) and `runcard` (drafts summary.md + run card for main-loop revision), both running the SAME deepseek-v4-flash model at `variant: low` — the dollar delta versus cheap-tier models is negligible at measured volumes (~$0.03–0.06 per refactor), so a second unknown model is not worth the correctness risk. Subagent models resolve through a single swap point (env-var or provider alias; ticket 08) so a genuinely cheaper tier stays a one-line option after the pilot validates the contracts. Script authoring, sync FAIL-diff interpretation, and solve diagnosis stay in the main loop.
8. **KB tooling.** Scraper stops emitting `.rst.md` stubs and existing stubs are pruned; `ripgrep` installed (winget, user-opted, machine-wide) and the skill uses `rg -l`; `scraping/generate_spine_api.py` generates `knowledge/playbook/spine-api.md` (~35 spine calls: signature + one-line semantics + EC gotcha link) with a provenance header (date, KB hash, file count), regenerated in the KB top-up ceremony.
9. **Config (opencode.json).** `compaction: {auto: true, prune: true, reserved: 10000}`; both subagents on deepseek-v4-flash `variant: low` via a single swappable model reference (tickets 02 + 08); main-model variant options per ticket 02.
10. **Bash/output discipline in execution.md.** Explicit timeouts; output caps; `.rst.md` never read; `rg -l` for discovery; final agent messages ≤ ~250 words.
11. **Pilot gate.** One greenfield bowtie (~3.5 GHz) run through the refactored tool; acceptance per user stories 1–3 vs the `silent-engine` baseline; calibration findings (kb-lookup spot-check, variant low availability) recorded in the run card; go/no-go decides the deferred expansion (per-stage API cards, more subagents). The pilot uses the same problem class as baseline and includes the user in the loop only at the Clarification block and the Review gate.

## Testing Decisions

- **What makes a good test here:** same as the foundation spec — external behavior judged at seams; the live AEDT desktop is the final judge.
- **Seam 1 — machine state (lowest):** run-card harness emits the baseline numbers from the opencode DB for `silent-engine` and the pilot run; `verify_skill.py` still passes (26/26) against the rewritten skill text; `opencode debug config` shows compaction + agents loaded.
- **Seam 2 — KB cold start (mid):** `rg -l wave_port` returns filenames in <1 s; `spine-api.md` covers the spine call set with a provenance header; zero `.rst.md` stubs remain; `generate_spine_api.py` rerun is stable (no drift when nothing changed).
- **Seam 3 — the pilot (the acceptance seam):** greenfield bowtie through all phases; run card records billed tokens, step count (parts), and wall time excluding solver physics. Pass: **≥50% fewer billed tokens, ≥40% fewer parts, ≥40% less wall time** vs the `silent-engine` baseline, and the delivered `.aedt` passes validation with the expected in-band resonance.
- **Prior art:** `silent-engine`/`bowtie-3500` is the baseline; its state-file and pinned-port patterns are the seed of the watchdog/verify runners.
- **Prerequisite:** valid AEDT license + VPN (standing prerequisites) for the pilot.

## Out of Scope

- Product changes: new recipes, new analysis types, HFSS 3D Layout, re-entry flows (ADR 0001 ceremony unchanged).
- Model changes beyond the tiering decision (no new main-loop model, no fine-tunes, no learned routers).
- Full KB re-crawl (only `.rst.md` pruning + spine-api generation; corpus content unchanged).
- Automated CI test harness (one pilot on the live desktop, per foundation spec precedent).

## Further Notes

- Verified facts the spec rests on: baseline numbers from the opencode DB (see analysis §1); 4,035/8,411 KB files are `.rst.md` stubs (analysis §6); the tool's bash default timeout is 120 s and accepts an explicit `timeout` argument; `ripgrep` absent from this box; `silent-engine` already seeds the state-file + pinned-port pattern.
- The grilling session (2026-08-04) locked every Implementation Decision above; ADR drafts 0006–0008 and the three glossary terms were written in that session (ticket 07 validates and links them).
- Pilot goes through the same live-desktop ceremony as any run; if AEDT/license preconditions fail, the pilot escalates per the skill's precondition contract.

## Comments

- 2026-08-04: Spec synthesized in a grill-with-docs session from `docs/hfss-agent-performance-analysis.md` (§§1–7) and 13 user decisions (scope, acceptance thresholds, session model, watchdog shape, double-solve guard, verification contract, idempotency, bash discipline, sync-verify runner, KB tooling, model tiering, docs footprint, plan shape). Published with 7 tickets; Status: ready-for-agent.
