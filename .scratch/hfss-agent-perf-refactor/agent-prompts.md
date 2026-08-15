# Agent launch prompts — tickets 01–05 (parallel)

How to launch: start a new opencode session in `C:\Users\afpim\Repos\HFSS_automation` and paste one prompt (or `opencode run -p "<prompt>"`). Five sessions can run at once; each prompt owns a disjoint file set (see the ownership map below). None of tickets 01–05 need AEDT or the VPN/license.

Note: ticket 08 (subagent model swap point, written 2026-08-04) is config-domain and is implemented by the same session as ticket 02 — prompt 02 carries its requirements; no sixth prompt needed.

## Parallel-safety rules (for every agent)

- Only touch files in your ownership set. Others are being edited by parallel agents.
- Do NOT commit; leave changes in the working tree for a single integration review.
- Read first, in this order: your ticket file, the feature spec, then anything else cited.
- When done: append a dated `## Comments` entry to your ticket file with what you built and your verification evidence; set `Status: ready-for-human` (triage-labels.md).

Ownership map:

| Ticket | Owns | Must not touch |
|---|---|---|
| 01 | `scripts/` (new dir) | everything else |
| 02 | `opencode.json` (repo root) | everything else |
| 03 | `skill/hfss-agent/SKILL.md`, `skill/hfss-agent/reference/execution.md` | verify_skill.py, templates/, ADRs, CONTEXT.md |
| 04 | `skill/hfss-agent/templates/workspace/**`, `skill/hfss-agent/verify_skill.py` | SKILL.md, execution.md |
| 05 | `scraping/*.py` (generator + new spine-api script), `scraping/pyaedt_ai_context/**` (stub pruning), `knowledge/playbook/spine-api.md` (generated) + winget install | skill text, templates, ADRs, CONTEXT.md |
| 07 | `docs/adr/0006-…0008-….md`, `CONTEXT.md` | SKILL.md, execution.md (report drift, don't edit) |

Launch order note: **ticket 07 is last** — it validates the ADR/glossary drafts against the landed skill text, so start it after 03/04 complete (or run it in review-mode early and fix only after they land). **Ticket 06 (pilot)** can start once 01–05 land and the user approves the live-desktop run; it is the only prompt needing VPN + AEDT license.

---

## Prompt 01 — measurement harness

Implement ticket 01 of the `hfss-agent-perf-refactor` feature. Read the ticket file `.scratch/hfss-agent-perf-refactor/issues/01-measurement-harness-baseline.md`, then the spec `.scratch/hfss-agent-perf-refactor/spec.md` (Implementation Decision on the run card, Testing Decisions Seam 1), and `docs/hfss-agent-performance-analysis.md` sections 1 and 10 (baseline numbers and the reference SQL).

Build `scripts/run_card.py` (new `scripts/` directory):
- Reads the opencode session database (default `~/.local/share/opencode/opencode.db`; overridable via CLI flag/env var). Open it read-only (`file:...?mode=ro` URI) with a generous busy timeout — opencode may be running and holding it (WAL).
- Given a session slug (or `--latest` for the HFSS project, identified via the `project` table's worktree containing `HFSS_automation`), print the run card: slug, created/updated timestamps, `tokens_input`, `tokens_output`, `tokens_reasoning`, `tokens_cache_read`, `tokens_cache_write`, billed (`input+output`), part count, conversation store bytes (sum of `length(data)` in `part`), and wall-clock duration.
- A `--summary <path>` mode that appends a `## Run card` section to a `summary.md` (idempotent: replace any existing Run card section).

Then capture the baseline: run it for session slug `silent-engine` and paste the printed card into the ticket's Comments. Python must be 3.10-compatible, stdlib only.

Verification (show evidence): (a) slug invocation prints a full card; (b) `--summary` on a throwaway copy is idempotent across two runs; (c) the baseline numbers match the analysis doc's section-1 figures. Report files created, the evidence, and the baseline.

## Prompt 02 — opencode config

Implement ticket 02 of the `hfss-agent-perf-refactor` feature. Read the ticket file `.scratch/hfss-agent-perf-refactor/issues/02-opencode-config.md`, the spec (Implementation Decisions 7 and 9, user stories 9–10), and `docs/hfss-agent-performance-analysis.md` section 7 (the tiering row of the SOTA table).

Create or edit `opencode.json` at the repo root (it may be absent; the global config is NOT yours to touch):
- `compaction`: `{ "auto": true, "prune": true, "reserved": 10000 }`
- Main model pin: `accounts/fireworks/models/deepseek-v4-flash-0731` with `variant: low` via provider model options. FIRST verify availability: run `opencode models` and inspect what variants the fireworks provider exposes for this model (schema `provider.fireworks-ai.models.<id>.variants` or options). If `low` (or an equivalent effort-lowering variant) is unavailable, record the evidence in the ticket and apply the option only if it exists; do not invent option names.
- Two subagents, `mode: subagent`, BOTH on the same `accounts/fireworks/models/deepseek-v4-flash-0731` at `variant: low` (decision 2026-08-04: the cheap-tier delta is ~$0.03–0.06 — not worth a second unknown model). Each agent's `model` resolves through ONE swap point per ticket 08 (prefer env substitution `{env:HFSS_SUBAGENT_MODEL}` defaulting to the flash ID; else a single provider alias) — do not hardcode per-agent:
  - `kb-lookup`: read-only (permission `edit`/`write` denied; read/glob/grep/list allowed; no bash unless needed for search). Its prompt: "You answer how to call pyAEDT APIs. Read the local KB under `scraping/pyaedt_ai_context/`, return the exact signature and argument names by quoting the KB file (include the file path). If a call is not in the KB, reply exactly `NOT FOUND — <what you searched>`. Never paraphrase from memory. Keep answers to the signature + the one example."
  - `runcard`: permission scoped to the given workspace path. Its prompt: "Draft `summary.md` sections (What the Model is, Acute design decisions, QA signals results) and the `## Run card` from the workspace's `state.md`, `results/state/*.txt` and `results/` — concise, ≤250 words total. Flag anything unreadable instead of guessing."
- Do not touch skill files, templates, or the DB.

Verification (show evidence): `opencode debug config` output showing compaction + both agents + model pinness; the `opencode models`/variant availability evidence; the swap-point resolution working (env or alias) per ticket 08.

## Prompt 03 — SKILL.md + execution.md rewrite

Implement ticket 03 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/03-skill-execution-doc-rewrite.md`, the spec (Implementation Decisions 1–6, 8, 10), the ADRs `docs/adr/0006-solves-run-under-a-detached-watchdog.md`, `docs/adr/0007-phase-sessions-bound-by-state-ledger.md`, `docs/adr/0008-idempotent-stage-scripts.md`, and the three new glossary terms in `CONTEXT.md` (State ledger, Run card, Verification line). Use the glossary vocabulary throughout.

Rewrite ONLY `skill/hfss-agent/SKILL.md` and `skill/hfss-agent/reference/execution.md` to encode, exactly per the ticket:
1. Three phase sessions (Clarification → Build incl. gate+sync → Solve+QA) bound by the State ledger (`workspaces/<name>/state.md`); named sessions; machine state in `results/state/*.txt`.
2. Verification contract: one `PASS: <stage> <assertions>` line per staged script; static py_compile+import gate before any AEDT launch.
3. Bash discipline: explicit `timeout` on anything >~90 s; no full recursive directory listings; final agent messages ≤ ~250 words.
4. Solve under the detached watchdog: 08_solve (cleanup + in-flight-solve probe that asks the user before submitting if one looks live + submit + detach), `poll_solve.py` writing `solve_progress.txt`; agent reads state only — never foreground-polls, never estimates.
5. Sync verify: `capture_state.py` → `model_snapshot.json`; `12_verify_sync.py` replay+diff on port-pinned second desktop; one PASS/FAIL line; teardown port-pinned.
6. Idempotent stages (delete-then-create); EC#8 route-around rewritten to match.
7. KB rules: `knowledge/playbook/spine-api.md` is the first-class reference for the spine call set; `.rst.md` files are stubs — never read or grep; use `rg -l` for discovery.
8. Cross-reference ADRs 0006–0008 and the glossary terms.

Constraint: `verify_skill.py` belongs to a parallel agent (ticket 04) — do NOT edit it, but DO run it before and after: every EXISTING marker must still pass against your rewritten text (fix wording, not the test). Reference the subagents from ticket 02 by NAME (`kb-lookup`, `runcard`) without inventing config.

Verification (show evidence): `python skill/hfss-agent/verify_skill.py` existing-markers result; a bullet list of the new concepts and where they landed in each file. Report pending-on-04 items if any.

## Prompt 04 — workspace template + runner scripts

Implement ticket 04 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/04-workspace-template-runners.md`, the spec (Implementation Decisions 3, 4, 5), and ADRs 0006 and 0008. NOTE: ticket 03 (a parallel agent) is rewriting SKILL.md/execution.md at the same time — base the template contracts on the ticket + ADR text; if the skill text looks mid-flight, proceed anyway and note any assumption in your report.

Own and change ONLY these paths:
- `skill/hfss-agent/templates/workspace/src/ws_common.py` — port-pinned attach/launch helpers, `write_state`/`read_state` for `results/state/*.txt`, and a teardown that is port-pinned and can never kill the user's desktop (model on `workspaces/bowtie-3500/src/ws_common.py`, which is the proven seed).
- `skill/hfss-agent/templates/workspace/src/poll_solve.py` — the detached solve watchdog: recursive `.asol`/`.sd` growth under `<project>.aedtresults/`, update `results/state/solve_progress.txt` every ~20 s, exit on completion or stall signal.
- `skill/hfss-agent/templates/workspace/src/capture_state.py` — write `results/state/model_snapshot.json` (objects + bboxes + materials + boundaries + excitations + setups/sweeps + variables) from a live model.
- `skill/hfss-agent/templates/workspace/src/12_verify_sync.py` — replay amended scripts on a fresh copy on a port-pinned second desktop, capture the same shape, diff against the snapshot, print one `PASS:`/`FAIL:` line (differing keys on FAIL), teardown port-pinned.
- A static-gate script (py_compile + import-check of all `src/*.py`).
- `state.md` skeleton; summary.md gains `## Run card` (filled by ticket 01) + a `model_snapshot.json` pointer; README updated for the new ceremonies.
- `skill/hfss-agent/verify_skill.py` — update its marker sets (add: Verification line/PASS, watchdog, State ledger, verify runner, .rst rule; adjust template-file expectations) so it passes against ticket-03's rewritten skill text. Keep the no-AEDT/no-license requirement.

Verification (show evidence): `python -m py_compile` on every new script; the static-gate script runs clean on the template; `verify_skill.py` output (if red only because 03 hasn't landed, say so explicitly in the report with the failing markers). Report files created + markers added.

## Prompt 05 — KB tooling

Implement ticket 05 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/05-kb-tooling-stub-scrub-rg-spine-api.md`, the spec (Implementation Decision 8), and `docs/hfss-agent-performance-analysis.md` section 6.

1. **Stub scrub.** Modify `scraping/generate_pyaedt_ai_context.py` so it stops emitting `*.rst.md` files. Prune the existing ~4,035 `.rst.md` stubs under `scraping/pyaedt_ai_context/` with a one-off script (leave it in `scraping/` for provenance). Record the scrub in the KB's provenance note (wherever the generator records provenance). Do not re-crawl the corpus; plain `.md` files stay untouched.
2. **ripgrep.** Install machine-wide with `winget install BurntSushi.ripgrep.MSVC` (explicitly approved by the user). Verify `rg --version` and time `rg -l wave_port scraping\pyaedt_ai_context` from the repo root (<1 s expected).
3. **`scraping/generate_spine_api.py`.** Define the spine call set (~35 calls across the Hfss lifecycle, geometry modeler primitives, materials, boundaries_and_ports, setup_and_mesh sweeps, postprocessing/visualization reports — e.g. `Hfss` create/validate/analyze, `create_box/create_polyline/unite/subtract/thicken_sheet`, material update, `wave_port`/`assign_radiation_boundary_to_objects`, `create_setup`/`create_linear_count_sweep`, `create_report`/`get_solution_data`). For each: extract the signature line, one-sentence description, and EC gotcha link (the environment-compat entry `knowledge/playbook/environment-compat.md` if the call has one) from the matching KB markdown files. Emit `knowledge/playbook/spine-api.md` with a provenance header (generation date, KB file count, content hash). Deterministic: fixed ordering, stable sort — a second run over an unchanged KB must be byte-identical.
4. Only touch the ownership set above. The skill rules that USE these (`.rst.md` never read, `rg -l`) land in ticket 03 — do not edit skill text.

Verification (show evidence): deletion count of stubs; `rg --version` + the timing; first-run vs second-run of the spine generator are byte-identical (`fc.exe` or hash); `scraping/verify_kb.py` still green (update it only if its expectations legitimately change, and say so). Report files + evidence.

---

## Prompt 07 — publish docs (ADRs + glossary)

Implement ticket 07 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/07-publish-docs-adrs-glossary.md`, then the house formats: `docs/agents/issue-tracker.md`, `C:\Users\afpim\.agents\skills\domain-modeling\ADR-FORMAT.md` (and CONTEXT-FORMAT.md), and one existing ADR for style (`docs/adr/0005-scripts-resync-after-ui-tweaks.md`).

Context: the ADRs 0006–0008 and the three CONTEXT.md terms were DRAFTED in the 2026-08-04 grilling session and already exist in the tree. Your job is to finalize, not re-decide — the decisions are locked (see the spec's Implementation Decisions). This ticket runs LAST: it validates the drafts against the skill text that tickets 03/04 land.

Tasks:
1. **Review the three ADR drafts** (`docs/adr/0006-solves-run-under-a-detached-watchdog.md`, `0007-phase-sessions-bound-by-state-ledger.md`, `0008-idempotent-stage-scripts.md`) for: house one-paragraph style, correct numbering after 0005, accuracy against the landed SKILL.md/execution.md behavior (read them; if they drifted, fix the ADR — NOT the skill text, which 03 owns), and a genuine decision each (not a how-to). Make only consistency fixes to the drafts; escalate any substantive disagreement (e.g. behavior contradicts an ADR) in the ticket Comments without rewriting the decision.
2. **Glossary**: verify the three terms in `CONTEXT.md` — State ledger, Run card, Verification line — match their usage in the landed skill text and house format (definition + `_Avoid_`). Fix wording if the skill uses them differently; add `_Avoid_` entries only where real synonyms exist.
3. **Cross-links**: grep SKILL.md + execution.md for `ADR 0006/0007/0008` and the three glossary terms. If tickets 03/04 referenced them, confirm the citations resolve to the right ADR titles. If a citation is missing or wrong wording was used, do NOT edit the skill files — record the exact spots in the ticket Comments as pending-03-fix items.
4. Update the ticket: append a dated Comments entry with what you changed and the verification evidence; set `Status: ready-for-human`.

Scope constraint: touch ONLY `docs/adr/0006…0008`, the three term entries in `CONTEXT.md`, and the ticket file. Do not edit SKILL.md/execution.md/templates/verify_skill.py — those are parallel-ticket territory.

Verification (show evidence): the ADR files after your pass; the CONTEXT.md term entries; the grep results for citations; your pending-03-fix list (if any).

---

## Prompt 06 — pilot run + acceptance gate (LIVE AEDT)

Run the ticket-06 pilot: `.scratch/hfss-agent-perf-refactor/issues/06-pilot-run-acceptance-gate.md`. This is the acceptance seam of the whole refactor — a real greenfield HFSS build on the live desktop using the refactored tooling, measured against the baseline. **Preconditions (verify before starting): UM VPN connected and the license server reachable, AEDT 2024 R1, pyAEDT 1.3.0 via `ansys.aedt.core`** — see `knowledge/playbook/environment-compat.md` Standing prerequisites. If a precondition fails, stop and report the evidence; do not work around it.

Read first: the ticket (acceptance thresholds), `skill/hfss-agent/SKILL.md` + `reference/execution.md` (the REFACTORED ceremony — three phase sessions, State ledger, PASS-lines, static gate, watchdog solve, verify runner, idempotent stages — follow it exactly), the feature spec (Testing Decisions Seam 3), and the prior-art workspace `workspaces/bowtie-3500/` (summary.md + `src/ws_common.py` + `results/state/`) whose designs this pilot reproduces at ~3.5 GHz. Baseline numbers for the gate: **silent-engine = 398,130 billed tokens, 24 parts, ~1.6 h**.

### Pre-flight (one short checklist, results go in the pilot's run card)
1. `python skill/hfss-agent/verify_skill.py` → 26/26; `python scripts/run_card.py --latest` prints a card (harness from ticket 01 works).
2. `knowledge/playbook/spine-api.md` exists with provenance header; `rg -l wave_port scraping/pyaedt_ai_context` answers fast.
3. Diff the installed skill (`C:\Users\afpim\.agents\skills\hfss-agent\`) against the repo copy (`skill/hfss-agent\`). If the refactored text is NOT live, ASK the user whether to deploy the repo copy over the installed one before proceeding; never touch `~/.agents` without approval.

### Pilot protocol (the refactored ceremony; user in the loop ONLY at the two gates)
- **Phase 1 — Clarification:** analyze the reference PDFs per the skill's read-first rules, derive the Recipe (paper-exact plain bowtie, no DGS, driven modal, single waveport, ~3.5 GHz), state Assumptions, propose QA signals — ONE block via the question tool; wait for confirmation. Then write `state.md` (the ledger) with the locked parameters.
- **Phase 2 — Build:** stages per the skill (solution type → design → geometry → materials → excitations → mesh → setup+sweep → validation), each staged script run with the static gate first, one `PASS:` line per run, self-correction per the cap rules, ledger appended per stage. **Review gate:** stop and hand the floor to the user to inspect the Math model in the AEDT UI (ADR 0003) — they may pass or tweak; record the outcome verbatim. If tweaks: run read-back sync + `capture_state.py` → `model_snapshot.json` + `12_verify_sync.py` → read its single PASS/FAIL line. If the user passes without tweaks, note it (parity with baseline is cleaner).
- **Phase 3 — Solve + QA:** `08_solve.py` (pre-submit in-flight guard, `analyze(blocking=False)`, detached watchdog); read `results/state/solve_progress.txt` — never foreground-poll, never estimate (physics may take 5–30+ min; the watchdog's stall signal is your escalation trigger). Then QA against the approved signals (EC#6 flaky-readout: report "unreadable — flaky readout" explicitly if so), plots to `results/`, `summary.md` with the run card.

### Measurement & verdict
- `python scripts/run_card.py --latest --summary <pilot summary path>` to append the run card; recompute the three deltas vs the baseline ticketed above: billed tokens (≥50% lower), parts (≥40% lower), wall time excluding solver physics (≥40% lower). Record the acceptance table + verdict in the run card and the ticket Comments.
- Calibration findings to capture (this is what the gate buys): whether `variant: low` was active on the session (check the session's model message metadata) and its observed effect; one `kb-lookup` spot-check during a stage (was the returned signature exact/good?); watchdog cadence and exit behavior; the verify-runner's PASS line; number of residual KB lookups beyond `spine-api.md`.
- End with release hygiene per the skill (teardown, kill-until-gone). Do NOT commit. Set ticket status to `ready-for-human`; the go/no-go on expansion (per-stage API cards, re-tiering subagents) is the USER's call from the verdict.

Constraints: nothing else about this pilot runs in parallel with you (single desktop, single license); user-interaction is capped at the two gates; if anything in the ceremony itself misbehaves (watchdog bug, verify-runner bug), capture the evidence and report — fixing refactor bugs mid-pilot is fine, but log every fix into the ticket Comments so the calibration is legible.

---

# Agent launch prompts — tickets 09–19 (corrective plan, batched)

How to launch: start a new opencode session in `C:\Users\afpim\Repos\HFSS_automation` (or `opencode run -p "<prompt>"`) and paste one prompt below. Batches of 3–4 parallel agents per the schedule at the bottom. The decision context every prompt assumes was settled in the 2026-08-07 grilling session; the retrospective is the primary source.

## Parallel-safety rules (for every agent)

- Only touch files in your ownership set; others' files are being edited by parallel agents. Where a file is shared, touch ONLY your allotted lines — never reformat, restructure, or reflow the file.
- Do NOT commit. Leave changes in the working tree for the batch's integration review. Sole exception: prompt 19 (its agent commits exactly one file).
- One AEDT-bound agent per batch, and that agent owns the license/desktop; never start AEDT work if the earlier batch's desktop is still alive (kill pinned desktops only per the port-pinned teardown rule).
- Read first, in this order: your ticket file, the relevant ADR(s), the cited skill text/template file, then the retrospective's section for your theme.
- When done: append a dated `## Comments` entry to your ticket file with what you built + verification evidence; set `Status: ready-for-human`.

Ownership map:

| Ticket | Owns (and only these) | Must not touch |
|---|---|---|
| 09 | `skill/hfss-agent/SKILL.md` — the Clarification block section only | execution.md, templates, ADRs, CONTEXT.md |
| 10 | `ws_common.py` (logging-default only), new `templates/workspace/src/diag_solve.py`, `execution.md` (bash-discipline lines only), template tests (new leaf module) | poll_solve.py, confirm_solve.py, SKILL.md |
| 11 | `scripts/run_card.py`, `templates/workspace/state.md` (header timestamps only) | templates/src, skill text |
| 12 | `execution.md` (solve-session section only), `ws_common.py` (bounded connect / pin liveness only) — start AFTER ticket 14 has landed its execution.md text | SKILL.md, templates/src, ADRs |
| 13 | `ws_common.py` (teardown guard only), new `templates/workspace/src/confirm_solve.py`, template tests (append-only) | poll_solve.py, execution.md, SKILL.md |
| 14 | `templates/workspace/src/poll_solve.py`, `execution.md` (solve-completion rule only), template tests (new leaf module) | ws_common.py, confirm_solve.py, SKILL.md |
| 15 | a new probe workspace only (e.g. `workspaces/watchdog-compare/`); uses the installed templates | repo code, templates (report drift, don't edit) |
| 16 | a new probe workspace only (e.g. `workspaces/readout-routearound/`) + env-compat amendment | everything else |
| 17 | `execution.md` (readout-policy lines only), `state.md`/`summary.md` templates (read-route lines only) | SKILL.md, templates/src, ADRs |
| 19 | `docs/adr/0006-solves-run-under-a-detached-watchdog.md` (the only ticket whose agent may COMMIT — that one file) | everything else |

## Batch schedule (3–4 agents per batch; ONE AEDT-bound agent max)

- **Batch 1 (4, non-AEDT):** 14 (start it first — biggest, and 12/15 depend on its text) · 13 · 09 · 11.
- **Batch 2 (3):** 12 (needs 14's landed execution.md) · 16 (the AEDT probe — solo desktop user) · background research agent for the re-pilot paper (research skill, no code — see prompt 18's precondition).
- **Batch 3 (4):** 10 · 15 (AEDT — THE USER WATCHES THE UI ~10 min for this one) · 17 (un-parked; needs 16's verdict) · 19 (reconcile + the one allowed commit; needs 13+14 landed).
- **Batch 4 (1):** 18 — the re-pilot; solo session, needs everything green + deployed + paper vetted.

- Between batches: run one integration review (code-review skill; fixed point = last commit) — merge shared-file overlaps (test file in B1, `execution.md`/`ws_common.py` in B2–B3), run `python src/test_template_runners.py` and `python skill/hfss-agent/verify_skill.py` green, commit per ticket.
- Deploy to `~/.agents/skills/hfss-agent/` (user-approve the diff) after B1 and again before B3 — 15 and 18 run against the INSTALLED skill.

---

## Prompt 09 — paper dimension gate

Implement ticket 09 of the `hfss-agent-perf-refactor` feature (corrective plan). Read the ticket `.scratch/hfss-agent-perf-refactor/issues/09-paper-dimension-gate.md`, then the retrospective's §A1–A2, then `skill/hfss-agent/SKILL.md` (the Clarification block).

Edit ONLY the Clarification block section of `skill/hfss-agent/SKILL.md` so that for paper-sourced Recipes the agent must: (1) cross-check the paper's equations against its own Table and Figure readings for the key dimensions (base/height/feed; the analyze-papers notes feed the check), (2) print a consistency verdict line in the Clarification block with the actual disagreeing numbers when present, (3) require the user to arbitrate which reading is canonical when inconsistent — no build until the dims are locked — and record the canonical source (Table/Figure/equations) in the State ledger, and (4) include the results-path note (S11 read via the UI on this box; scripted readout a bonus, never a blocker). Non-paper recipes keep today's Clarification.

Verification (show evidence): a sample Clarification-block excerpt with a verdict line for the Astuti-class case (inconsistent paper); the results-path note present; confirmation that non-paper wording is untouched. Report files + evidence; `Status: ready-for-human`.

## Prompt 10 — context hygiene

Implement ticket 10 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/10-context-hygiene.md`, the retrospective §D, and `skill/hfss-agent/templates/workspace/src/ws_common.py` + `skill/hfss-agent/reference/execution.md`.

Own exactly: (1) a logging-default in `ws_common.py`'s shared preamble so every staged script suppresses pyAEDT INFO output in its console output (WARNING or quieter); (2) a NEW `templates/workspace/src/diag_solve.py` printing the whole machine snapshot in one attach — pin liveness, project path, object/boundary counts, newest solve profile status, sweep-entry count, and the scripted readout one-shot only where that path exists — no banking logic (ticket 13's confirm script owns that); (3) the bash-discipline lines in `execution.md` (tail exactly 1–3 lines, never whole progress/log files; diagnostics script is the only legitimate diagnostics surface — no throwaway probe files); (4) a template test for the logging default (new leaf test module, or appended test functions).

Do NOT touch `poll_solve.py`, `confirm_solve.py`, `12_verify_sync.py`, or SKILL.md. No AEDT needed. Verification: run a staged script from the template (compile-only is fine if no desktop) showing zero INFO lines; diag_solve.py py-compiles and its snapshot shape matches its docstring; `python src/test_template_runners.py` green. Report + evidence; `Status: ready-for-human`.

## Prompt 11 — measurable wall metric

Implement ticket 11 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/11-measurable-wall-metric.md`, the retrospective (run-card references), `scripts/run_card.py`, and `skill/hfss-agent/templates/workspace/state.md`.

Own exactly: (1) `state.md` template gains a session-1 start timestamp (header area only); (2) `scripts/run_card.py` gains wall reporting — raw wall plus active wall defined as session start → the user-gated solver submission instant (`solve_submitted_at` in the machine state; if absent, report active wall as "unmeasurable: no solve_gate timestamp" rather than guessing); (3) the verdict-table helper reports active wall as the comparison only when a baseline build-to-solve window is derivable, and marks wall informational otherwise. Keep the existing run-card fields intact (tokens/parts/store). Python 3.10, stdlib.

Verification: run_card on a fixture session prints raw + active wall; the unmeasurable-marking path demonstrable; existing `--summary` idempotency preserved. Report + evidence; `Status: ready-for-human`.

## Prompt 12 — solve-session discipline

Implement ticket 12 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/12-solve-session-discipline.md`, the retrospective §B4–B5 and §E1, and the CURRENT `skill/hfss-agent/reference/execution.md` solve section (ticket 14's completion rule should already be in it — start only after Batch-1 lands).

Own exactly: (1) the solve-session section of `execution.md` encoding resolve-once — after any solve anomaly the agent reads the evidence once (watchdog terminal line + newest profile status + counts) and escalates to the user; re-submission only on the user's explicit go after that escalation or on a user-approved model-state change; (2) the ledger practice: one delta per solve decision (submission number, reason, user's answer) plus a live-state block (pin, solve status, solved-marker pointer, next action) — documented in execution.md, not a state.md template rewrite; (3) `ws_common.py` attach path gains a bounded connect (short timeout) so a dead pinned desktop fails fast as "stale pin — re-pinning", never a hanging attach.

Do NOT touch SKILL.md, `poll_solve.py`, `confirm_solve.py`, or the teardown function. No AEDT needed. Verification: show the new execution.md solve-session text; a ws_common code path that returns the stale-pin verdict instead of indefinite attach (a unit-level simulation of the timeout path is fine). Report + evidence; `Status: ready-for-human`.

## Prompt 13 — bank-before-teardown

Implement ticket 13 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/13-bank-before-teardown.md`, the retrospective §B3 and §E2, the amended ADR 0006 (draft already in `docs/adr/` — read it, do not edit it), and `skill/hfss-agent/templates/workspace/src/ws_common.py`.

Own exactly: (1) a NEW `templates/workspace/src/confirm_solve.py` (filesystem-only, no pyAEDT) that reads the newest solve profile status + sweep-point count from the project results tree and writes the solved marker to the machine state (status, sweep count, bank time); (2) the teardown function in `ws_common.py` becomes guarded: banked workspace → release with projects left on disk (`close_projects=False`) and still reap the pinned process; unbanked but solve evidence on disk (terminal profile status, no in-flight semaphores) → refuse with an actionable "bank it first — run confirm_solve" message and non-zero exit; neither → today's behavior. (3) Append template tests for the guard's decision logic (banked / unbanked-with-evidence / neither) using fixture state; keep existing tests passing.

Do NOT touch `poll_solve.py`, `execution.md`, SKILL.md. No AEDT needed. Verification: `python src/test_template_runners.py` green with your new cases; confirm_solve.py py-compiles; a trace showing each guard branch. Report + evidence; `Status: ready-for-human`.

## Prompt 14 — stage-aware solve watchdog

Implement ticket 14 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/14-stage-aware-solve-watchdog.md`, the retrospective §B1–B2 (and §1 for the pilot's evidence), the amended ADR 0006 draft (read, do not edit), the CURRENT `poll_solve.py`, and the pilot's real artifacts for the observable shapes: `workspaces/bowtie-3500-pilot/bowtie_3500_pilot.aedtresults/Bowtie3501.results/` (a `.profile` with `ProfileItem('Initial Meshing'/'Adaptive Meshing'/'Frequency Sweep')` and a final `'Status'` footnote — the terminal Status line), the `F####_SU.txt`/`.sd`/`.cmesh`/`.imesh`/`_ADP#_` families, the `.asol.semaphore` in-flight markers, and `results/state/solve_progress.txt` (the format to evolve). Inspect as many of those artifacts as you need to pin the parsing rules — this is the ground truth for the stage model.

Rewrite `poll_solve.py` to: per tick, detect the stage (initial meshing / adaptive meshing / frequency sweep / finalizing / done) from the newest profile's stage ledger plus stage-family artifact growth, and append one line to `solve_progress.txt` carrying stage + evidence (stage ledger extract, elapsed, counts). Terminal states, evidenced before claiming: `complete` (profile Status "Normal Completion" + settle), `stalled` (no growth in the current stage past its window — stage named in evidence), `aborted` (in-flight markers gone + no completion + solver process dead). Appended verbatim for any non-Normal profile status; the sweep-count guess parameter is removed completely. Keep it filesystem-and-process only (std library + psutil at most; no pyAEDT import, no attach, no desktop kill). Update the solve-completion rule in `execution.md` (that section only). Tests: new leaf test module with synthetic result trees covering every stage sequence and each terminal path — including the engine-error profile that must NEVER be claimed complete, and the stuck-at-mesh stall with its stage in the evidence.

Verification: `python src/test_template_runners.py` (and your new module) green; a sample progress line in the new format; a note on whether the profile is observed write-incrementally (the open question ticket 15 answers live too). Report + evidence; `Status: ready-for-human`.

## Prompt 15 — live watchdog stage-agreement test (AEDT — user watches the UI)

Run ticket 15 of the `hfss-agent-perf-refactor` feature: `.scratch/hfss-agent-perf-refactor/issues/15-live-watchdog-comparison.md`. This is a LIVE exercise — preconditions: UM VPN + license reachable, AEDT 2024 R1 (see `knowledge/playbook/environment-compat.md` standing prerequisites). Preflight: diff the INSTALLED skill `C:\Users\afpim\.agents\skills\hfss-agent\` against the repo copy — the stage-aware `poll_solve.py` and latest `ws_common.py` must be deployed; if not, ASK the user to deploy before continuing (never edit `~/.agents` yourself). Also verify the B1 suites: `python src/test_template_runners.py` and `python skill/hfss-agent/verify_skill.py` green.

Protocol: create a new probe workspace; make a Re-entry-style COPY of a solve-ready design (suggest: the smoke-matrix probe project or the pilot's corrected project — the original is never opened, mutated, or touched; verify the original's integrity after the run). Submit a non-blocking solve with the launcher, run the deployed stage-aware watchdog, and — with the USER watching the desktop UI for the solve's duration — record the user-observed stage sequence and the watchdog's stage lines. Diff the two sequences; log any mismatch in the ticket Comments as a watchdog bug (the UI is ground truth), with the profile/artifact evidence from that moment. Answer the open question: is the profile written incrementally per stage or only at the end? Clean up per the port-pinned teardown rule; do NOT bank anything real (this is a probe workspace).

Constraint: you are the batch's only AEDT agent; check no other desktop is running (count `Get-Process ansysedt`) before starting. When done: comments + evidence; `Status: ready-for-human`.

## Prompt 16 — readout route-around (AEDT probe)

Run ticket 16 of the `hfss-agent-perf-refactor` feature: `.scratch/hfss-agent-perf-refactor/issues/16-readout-route-around.md`. Live exercise — same preconditions as prompt 15 (VPN+license; one AEDT agent per batch). Read the ticket, `knowledge/playbook/environment-compat.md` (EC#3, EC#6), and `workspaces/smoke-matrix/`'s diag scripts for prior-art shapes.

Protocol: in a fresh throwaway probe workspace, validate a route-around for the pyAEDT 1.3.0 missing `HfssConstants.default_solution` client bug that blocks the scripted readout/export paths — monkeypatch or route-around, exercised against a copy of an already-solved project so no crowds or long solves are needed. One readout shape minimum that returns real data (e.g. `get_solution_data` with the actual auto-sweep name); record exactly which shapes work and which still fail on this box. If the surface remains flaky per EC#6, record the refined negative route instead — and in BOTH cases the finding is documented as evidence in the probe workspace and the environment-compat entry amended through the established amendment discipline (ADR 0004/0002 paths; if amendment approval is required, draft the proposed entry text into the ticket Comments and leave the file untouched).

Do not touch repo code or templates. When done: comments + evidence; `Status: ready-for-human`.

## Prompt 17 — readout one-shot policy (un-parked before the re-pilot)

Implement ticket 17 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/17-readout-one-shot-policy.md`, the retrospective §C, and the CURRENT `execution.md` readout/Result-QA lines. Ticket 16's verdict should be in (route-around worked / didn't) — its answer fixes the policy's precondition.

Own exactly: (1) the readout lines of `execution.md` — replace the "re-attach and retry until it works" guidance with the one-shot policy: at most one scripted Readout attempt (with one fresh-attach retry), then the plot goes to the user via the UI; the scripted attempt runs only when the route-around (ticket 16) is in place, otherwise the first move is the UI handoff; (2) the read-route line in the `state.md`/`summary.md` templates (record UI vs scripted per run, so Result QA is honest). Do NOT touch SKILL.md, `templates/src/`, ADRs. No AEDT needed. Verification: the new execution.md readout lines; grep shows no leftover archaeology guidance; template lines in place. Report + evidence; `Status: ready-for-human`.

## Prompt 18 — re-pilot acceptance run (LIVE AEDT — solo)

Run ticket 18 of the `hfss-agent-perf-refactor` feature: `.scratch/hfss-agent-perf-refactor/issues/18-re-pilot-acceptance.md`. This is the acceptance seam of the corrective plan — a full three-phase ceremony on a USER-VETTED, self-consistent paper (the Astuti class is the gate: the paper's Table ↔ Figure ↔ equations must have been cross-checked by the research-vetting agent and approved by the user before you start — evidence in the ticket Comments). Preconditions (verify BEFORE starting): VPN + license, AEDT 2024 R1, all corrective tickets' suites green (`python src/test_template_runners.py`, `python skill/hfss-agent/verify_skill.py`, run_card harness), the INSTALLED skill deployed and in sync with the repo (diff + user approval if not), no other desktop alive. Read-first: the ticket, the amended ADR 0006, SKILL.md + execution.md (the corrected ceremony), the retrospective's corrective plan, and the pilot workspace `workspaces/bowtie-3500-pilot/` as the worked exemplar. Baseline: `silent-engine` = 398,130 billed tokens, 424 parts, ~1.6 h.

Protocol: exactly prompt 06's protocol (Clarification → Build → Review gate → Solve+QA), now WITH the corrected disciplines: paper gate + locked dims from Clarification (ticket 09), resolve-once anomaly handling (12), stage-aware watchdog reading (14), banking before any teardown (13), one-shot readout policy honoring the UI-arbiter default (17), active-wall timing (11). User in the loop only at Clarification and the Review gate plus the post-solve UI read.

Measured verdict: run card with tokens/parts/active-wall under the re-locked definitions; acceptance table vs baseline; calibration notes (watchdog stage agreement, submission attribution, banking evidence). End with release hygiene (banked, teardown, kill-until-gone). Do NOT commit. When done: comments + evidence; `Status: ready-for-human`; the go/no-go on the corrected ceremony is the user's call.

Constraint: single desktop, single license, nothing parallel with you. If a corrective discipline itself misbehaves, capture evidence and report — log every fix into the ticket Comments.

## Prompt 19 — reconcile + commit the ADR 0006 amendment

Implement ticket 19 of the `hfss-agent-perf-refactor` feature. Read the ticket `.scratch/hfss-agent-perf-refactor/issues/19-adr-0006-amendment.md`, the draft amendment already in `docs/adr/0006-solves-run-under-a-detached-watchdog.md`, the landed `poll_solve.py` (ticket 14) and `ws_common.py`/`confirm_solve.py` (ticket 13) — both tickets must be done before you start.

Your job: reconcile the draft's wording against the implemented behavior (stage model + terminal states + evidence rules + banking + teardown guard — adjust numbers/names/contract wording only, never re-decide), fix house style (one tight paragraph per the repo's ADR convention), update cross-references in `execution.md` only where they cite the amended contract, and COMMIT — the sole agent permitted to commit: stage ONLY `docs/adr/0006-solves-run-under-a-detached-watchdog.md` (and nothing else; check `git status` first, never bundle others' files) with a concise message in repo style.

Verification: the committed ADR diff; grep showing cross-refs resolve; evidence that git status shows your staged file only. `Status: ready-for-human`.
