# Execution reference for the hfss-agent skill

Reference for `SKILL.md`; loaded by the agent when executing stages. Facts from the environment-compat entry are marked (EC#n) — the entry is authoritative and living. Enablement decisions are quoted as ADR 0006 / 0007 / 0008.

## Phase sessions and the State ledger (ADR 0007)

One run is three named sessions — `<name>-clarify`, `<name>-build`, `<name>-solve` — each starting fresh from `workspaces/<name>/state.md`, the **State ledger**. Only the ledger (plus the relevant staged scripts) crosses a session boundary.

- The Clarification session **writes** the ledger; the Build session **amends** it (one-line delta per stage, snapshot pointer at the gate); the Solve+QA session **reads** it.
- Ledger contents: stage progress, locked parameters/variables, decisions and pending decisions, pitfalls hit, the model-snapshot pointer. Keep it ≤ ~2 KB, owned by the agent per stage.
- **Machine state stays in `results/state/*.txt`** (`aedt_port.txt`, `aedt_process_id.txt`, `solve_progress.txt`, `solve_watchdog_pid.txt`, …) — written by scripts, read by the agent (or by a later session). Never hand-machine-state off in prose.
- Resume rule: a killed session resumes from the ledger, never by replaying the prior conversation.

## Attach-or-launch preamble (every staged script)

Session state lives in the AEDT project — never in a Python process. Each script begins with the preamble, which either launches a desktop or attaches to the running one, and ends by leaving the desktop alive for the next stage.

- Launch: `Hfss(version="2024.1", new_desktop=True, non_graphical=False, project=PROJECT, design=DESIGN, solution_type=<set from the Recipe — explicit, never the default>)` (EC#1, EC#11). Cold start is ~6–25 s.
- Attach (preferred when a session is alive): `Desktop(version="2024.1", new_desktop=False)` then `Hfss(project=PROJECT, design=DESIGN, solution_type=<from the Recipe>, new_desktop=False)` — cross-process attach works, including reading state written by earlier stages (EC#2).
- Project paths: absolute, inside the Workspace. Pass `remove_lock=True` when opening a project a crashed session may have locked (EC#9).
- **Port-pinning for verify runners**: any desktop a runner launches is pinned to a dedicated port that can never collide with the user's desktop (helpers in the workspace template's `src/ws_common.py`); the runner records the port in `results/state/aedt_port.txt`, launches against it, and tears down against it.
- Teardown at session end ONLY: `desktop.release_desktop(close_projects=True, close_on_exit=True)`, then kill the launched `aedt_process_id` tree until gone and assert zero `ansysedt.exe` left; end the script with `sys.stdout.flush()` + `os._exit(0)` (gRPC teardown hangs; release alone may not reap — EC#10). Release hygiene applies between stages: release the client WITHOUT closing (keep the server) or simply exit the script — the next preamble attaches. Runner teardown is port-pinned (previous bullet): only the process on the pinned port dies.

## Verification contract (every staged script)

- Every staged script ends with exactly one machine-parseable **Verification line** on success: `PASS: <stage> <assertions>` — e.g. `PASS: geometry object count == 3, bbox sane, all dims variables`. The assertions listed are the checks the script performed (a missing assertion is a script bug).
- **Static gate before any AEDT launch**: `py_compile` + import check over all `src/*.py` (the template's static-gate script). Nothing launches AEDT while the gate is red.
- **Self-correction reads the Verification line** of the failed Run — not filtered logs — and the stage's own error surfaces; see Self-correction below.

## Bash discipline

- Pass an explicit `timeout` argument to any bash call that can exceed ~90 s; never rely on the harness default.
- No full recursive directory listings: use count/size summaries, `tail`, and `results/state/*.txt` — never `dir /s`-style scans of the project or corpus.
- Final agent messages ≤ ~250 words (verbosity cap), including after each stage.

## Per-stage checklist

1. **Clarification** — deliver one block: request minimums, missing critical setup features, proposed Recipe + Assumptions, proposed Result QA signals; lock the parameters/variables. Record the confirmation verbatim in the summary, then **write the State ledger**. If `knowledge/reference-papers/` holds user PDFs, run the `analyze-papers` skill on the folder first and read the resulting agent notes before drafting the block (SKILL.md "Read first" #6) — the notes are context for the Recipe and QA signals, never automatic playbook material.
2. **Solution type** — explicit, from the Recipe (do not rely on defaults; new designs default to Terminal — EC#11).
3. **Design** — create + save; record design/project names in the summary.
4. **Geometry** — all dims variables (`hfss["name"] = "value"`); sheet-vs-solid choices per Recipe; **delete-then-create** — every script deletes each object, boundary, excitation, mesh operation, and sweep it (re)creates, before creating them, so re-running the stage in place always converges (ADR 0008). Wipe-and-rebuild is demoted to an explicit escalation tool, never the default route-around. Keep names stable across runs — the read-back sync contract depends on them.
5. **Materials** — by name from the library (`FR4_epoxy`, `pec`, `air`, …); record which and why.
6. **Excitations/boundaries** — port assignment by **face object**, and prefer a port on a **solid's face** — the reliable shape (EC#7, EC#8). Example: `hfss.wave_port(hfss.modeler.objects_by_name["<solid>"].faces[0], impedance=50, ...)`. Sheet-based ports with auto integration lines have produced invalid designs (EC#8); if a sheet port is unavoidable, expect that risk and have a fallback in the Recipe. Never pass int ids or edge objects (EC#7). Radiation: `assign_radiation_boundary_to_objects(<airbox>)`.
7. **Mesh** — only what the Recipe requires; adaptivity covers the rest.
8. **Setup + sweep** — one setup named `Setup1`; `create_linear_count_sweep(...)` auto-suffixes the sweep name — read the real name back from `existing_analysis_sweeps` before any report uses it (EC#6).
9. **Validation** — `bool(hfss.validate_simple())` must be True; on False, treat as a failed run and diagnose before retrying (EC#8). Because every stage is delete-then-create (ADR 0008), the retry is a single in-place re-run — no teardown → wipe → replay chain.
10. **Review gate** — hand the floor to the user; they inspect the Math model in the UI and may tweak. On any tweak: run read-back sync (below), then the sync-verify runner (below); the gate does not close until sync has run **and** the runner printed its PASS line.
11. **Solve** — do not poll by hand; go through the watchdog flow (below).
12. **Plots** — per Recipe; write to `results/`.
13. **Result QA** — check the agreed signals; report each with numbers or explicitly "unreadable — flaky readout" where the readout fails, and route via re-attach before concluding (EC#6).
14. **Summary** — write `summary.md`: acute decisions, the Model description, Recipe + signals used, any deltas recorded by sync; have `runcard` draft the `## Run card` from `state.md`, `results/state/*.txt` and `results/`, revise, and append it via the measurement harness.

## Read-back sync (ADR 0005)

Trigger: any user tweak in the AEDT UI after a stage has run.

1. Introspect the live model with the high-level API: design variables, boundaries, excitations, setups, mesh operations (all enumerable).
2. Diff against the owning stage's staged script.
3. Amend that script so re-running top-to-bottom reproduces the delivered model; keep the change minimal and parameterized.
4. Record the delta in `summary.md` and in the State ledger.
5. The Review gate does not close until sync has run.

**Sync-verify runner** (deterministic, replaces anything interactive): `capture_state.py` writes `results/state/model_snapshot.json` — objects + bboxes + materials + boundaries + excitations + setups/sweeps + variables — from the live model. Then `12_verify_sync.py` replays the amended staged scripts on a fresh copy on a **port-pinned second desktop**, captures the same shape, diffs against the snapshot, and prints exactly one PASS:/FAIL: line — `PASS: sync replay matches snapshot` or `FAIL: sync mismatch — <differing keys>` — then tears down port-pinned (previous preamble bullet): only the runner's desktop is killed. The snapshot doubles as the Solve+QA session's model baseline and as Result QA input.

## Solve under the detached watchdog (ADR 0006)

Two scripts orchestrate the solve; the agent does nothing but read machine state.

- **`08_solve.py`** (in Workspace `src/`):
  1. **Cleanup**: `cleanup_solution` on the named setup, stale results removed from `<project>.aedtresults/`.
  2. **In-flight-solve probe**: results-dir age + live solver processes (`ansysedt.exe`); **if a solve looks live, ask the user before submitting** (double-solves cost an hour — the guard exists to stop that class).
  3. **Submit**: `analyze(setup=<name>, blocking=False)`; its `True` return is *submission only*, not completion (EC#5).
  4. **Detach**: launch `poll_solve.py` via `Start-Process` (detached, `-WindowStyle Hidden`); record its PID in `results/state/solve_watchdog_pid.txt`; exit.
- **`poll_solve.py`** (the watchdog): every ~20 s, recursively scan `.asol`/`.sd` growth under `<project>.aedtresults/` and append the state to `results/state/solve_progress.txt`; exit on completion, or signal a stall if growth stops before convergence.
- **The agent**: reads machine state only — `results/state/*.txt`, the solve's own state in `solve_progress.txt`. **Never foreground-poll, never estimate solve time** — no `analyze(...)` looping, no manual process wrangling. Re-attach for model reads and retry flaky readouts (EC#6) — reads are fine, polling is not. *The solve is complete when the watchdog's independent completion signals appear* (progress file says done + results on disk).

## Self-correction details

- Max 3 consecutive failed Runs per Stage; each attempt amends the script with a stated hypothesis.
- After every Run, capture errors from the surfaces that work: the **Verification line** (its absence or its `FAIL` content), raised exceptions, `validate_simple()` results, on-disk logs. The raw message-manager call (`GetMessages`) is broken over gRPC (EC#3) — the message manager is read via the surfaces above; this substitution is a known gap of the backend pairing, flagged for a follow-up against the original contract wording.
- Because stages are idempotent (ADR 0008), retrying is one in-place script Run; escalation (wipe-and-rebuild, teardown) is the escalation-only route-around.
- Escalate (report to the user with script + error + attempts) on: the 3-run cap reached, the identical error twice in a row, or an error unmapped to any KB/playbook cause.

## KB rules

- `knowledge/playbook/spine-api.md` is the **first-class reference for the spine call set** — signature, one-line semantics, EC gotcha links, provenance header. Script generation reads it once; do not re-derive.
- The `.rst.md` files under `scraping/pyaedt_ai_context/` are **stubs — never read or grep them** (a scrape artifact, pruned provenance: the KB's own note).
- Discovery: `rg -l` only (`rg -l wave_port scraping/pyaedt_ai_context`), never a full recursive listing. Find the filenames first, then read the specific `.md` files.
- For any call not in `spine-api.md`, ask the read-only `kb-lookup` subagent: exact signature quoted from the KB file with its path, or `NOT FOUND — <what you searched>`; never paraphrase from memory. Keep its answer in the script as authored, then route around any EC-noted gotcha.

## Learning-loop triggers (ADR 0002)

A proposal to amend the playbook is earned by any of: a user tweak that generalizes to the Recipe class; a backend-compat discovery (lands in the environment-compat entry); a Result-QA anomaly whose resolution generalizes. Fix the current Model first; append only after explicit user approval; project-specific values stay in the summary.
