# Execution reference for the hfss-agent skill

Reference for `SKILL.md`; loaded by the agent when executing stages. Facts from the environment-compat entry are marked (EC#n) — the entry is authoritative and living. Enablement decisions are quoted as ADR 0006 / 0007 / 0008.

## Phase sessions and the State ledger (ADR 0007)

One run is three named sessions — `<name>-clarify`, `<name>-build`, `<name>-solve` — each starting fresh from `workspaces/<name>/state.md`, the **State ledger**. Only the ledger (plus the relevant staged scripts) crosses a session boundary.

- The Clarification session **writes** the ledger; the Build session **amends** it (one-line delta per stage, snapshot pointer at the gate); the Solve+QA session **reads it and amends it** (one delta per solve decision + a live-state block — see Solve-session discipline below).
- Ledger contents: stage progress, locked parameters/variables, decisions and pending decisions, pitfalls hit, the model-snapshot pointer. Keep it ≤ ~2 KB, owned by the agent per stage.
- **Machine state stays in `results/state/*.txt`** (`aedt_port.txt`, `aedt_process_id.txt`, `solve_progress.txt`, `solve_watchdog_pid.txt`, …) — written by scripts, read by the agent (or by a later session). Never hand-machine-state off in prose.
- Resume rule: a killed session resumes from the ledger, never by replaying the prior conversation.

## Attach-or-launch preamble (every staged script)

Session state lives in the AEDT project — never in a Python process. Each script begins with the preamble, which either launches a desktop or attaches to the running one, and ends by leaving the desktop alive for the next stage.

- Launch: `Hfss(version="2024.1", new_desktop=True, non_graphical=False, project=PROJECT, design=DESIGN, solution_type=<set from the Recipe — explicit, never the default>)` (EC#1, EC#11). Cold start is ~6–25 s.
- Attach (preferred when a session is alive): `Desktop(version="2024.1", new_desktop=False)` then `Hfss(project=PROJECT, design=DESIGN, solution_type=<from the Recipe>, new_desktop=False)` — cross-process attach works, including reading state written by earlier stages (EC#2). Resumes connect by the pinned port with a **bounded connect** (short timeout): a dead pin fails fast with the `stale pin — re-pinning` verdict, is cleared, and a fresh desktop is launched and re-pinned — never a hanging attach (pilot retrospective B5; see Solve-session discipline).
- Project paths: absolute, inside the Workspace. Pass `remove_lock=True` when opening a project a crashed session may have locked (EC#9).
- **Port-pinning for verify runners**: any desktop a runner launches is pinned to a dedicated port that can never collide with the user's desktop (helpers in the workspace template's `src/ws_common.py`); the runner records the port in `results/state/aedt_port.txt`, launches against it, and tears down against it.
- Teardown at session end ONLY: `desktop.release_desktop(close_projects=True, close_on_exit=True)`, then kill the launched `aedt_process_id` tree until gone and assert zero `ansysedt.exe` left; end the script with `sys.stdout.flush()` + `os._exit(0)` (gRPC teardown hangs; release alone may not reap — EC#10). Release hygiene applies between stages: release the client WITHOUT closing (keep the server) or simply exit the script — the next preamble attaches. Runner teardown is port-pinned (previous bullet): only the process on the pinned port dies.

## Verification contract (every staged script)

- Every staged script ends with exactly one machine-parseable **Verification line** on success: `PASS: <stage> <assertions>` — e.g. `PASS: geometry object count == 3, bbox sane, all dims variables`. The assertions listed are the checks the script performed (a missing assertion is a script bug).
- **Static gate before any AEDT launch**: `py_compile` + import check over all `src/*.py` — the template's `00_static_gate.py`. Nothing launches AEDT while the gate is red.
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
- **`poll_solve.py`** (the watchdog): every ~20 s it reads two independent observables under `<project>.aedtresults/` — the **stage-family artifacts** (`*.imesh`/`*.cmesh` → initial meshing, `*_ADP<pass>_*` → adaptive meshing, `*_F####_SU.txt` → frequency sweep) and the **newest `.profile`'s stage ledger** (`Initial Meshing` → `Adaptive Meshing` → `Frequency Sweep`, per-stage elapsed, adaptive-pass count) with its terminal `Status` footnote. One line per tick lands in `results/state/solve_progress.txt` carrying the stage plus evidence (stage-ledger extract, elapsed, family counts). Terminal states are evidenced before claiming: `status=complete` **only** when the profile's terminal `Status` is `Normal Completion` and the profile was written during the solve, plus a settle; `status=stalled` when there is no growth in the current stage past its window — the stage is named in the evidence (a mesh stuck forever and a running sweep never look alike); `status=aborted` when the profile status is anything non-Normal (appended **verbatim** — an engine-error profile is never claimed complete) or the in-flight semaphores are gone with no completion and the solver process is dead. No output-count prediction anywhere: the sweep-point guess parameter is removed — completion never depends on a guessed count. Exit codes mirror the last line: 0 complete, 2 stalled, 3 aborted.
- **The agent**: reads machine state only — `results/state/*.txt`, the solve's own state in `solve_progress.txt`. **Never foreground-poll, never estimate solve time** — no `analyze(...)` looping, no manual process wrangling. Re-attach for model reads and retry flaky readouts (EC#6) — reads are fine, polling is not. *The solve is complete only when the progress file's terminal line says `status=complete` **with** `profile_status=normal_completion` and the results are on disk*; any terminal line that is not `status=complete` is an anomaly — escalate with the evidence tail (the profile's verbatim Status footnote distinguishes done from plateau). Bank the solve evidence before any teardown (ADR 0006 amendment / ticket 13).

## Solve-session discipline: resolve-once + live ledger (ADR 0007 practice)

The Solve+QA session obeys a discipline that ends the five-submission failure class (pilot retrospective B4–B5): each verified model state gets at most one submission, every solve decision is evidence-first, and the ledger carries a live-state block so "where is the sim" is one read — never archaeology.

**Resolve-once.** After ANY solve anomaly — a watchdog `stalled`/`aborted` terminal line, an engine-error profile (verbatim non-Normal status), a false tick, a dead watchdog, or a resume against a changed world — read the evidence exactly once, and only from machine state: the watchdog's terminal line in `results/state/solve_progress.txt` (stage + evidence extract), the newest solve profile's terminal `Status` (verbatim), and the counts (sweep entries). One read. Then escalate to the user with that evidence; no re-reads, no re-archaeology, no silent re-submission while the question is out.

Re-submission is legal through exactly two routes:

1. **the user's explicit go** after that escalation; or
2. **a user-approved model-state change** — Clarification-locked corrections or Review-gate edits run through read-back sync — that legitimately invalidates the solve (a submitted solve is evidence for the state it was submitted on, and only that state).

A submission through any other route is a discipline violation, not a retry.

**Ledger discipline.** The solve session appends exactly ONE delta to the State ledger per solve decision: `solve #<n> — reason: <one-line evidence>; user: <answer verbatim>` — the submission number, the reason (the anomaly evidence or the approved state change that invalidated it), and the user's answer. After every decision, refresh the ledger's **live-state block** (≤ 4 lines):

- pin — the `results/state/aedt_port.txt` value; probed this session? re-pinned? (stale pins are cleared, never attached against)
- solve status — the last terminal line of `results/state/solve_progress.txt`
- solved marker — does `results/state/solved.txt` exist (banked, via `confirm_solve.py`), and its `status=` line
- next action — one line: report to user, bank, guarded teardown, close out.

Resume reads the ledger FIRST, always (ADR 0007): the live-state block plus the last delta answer "where is the sim" without disk archaeology. The run card attributes every submission to a user-approved reason from these deltas — an unattributed submission is a bug in the session record.

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
