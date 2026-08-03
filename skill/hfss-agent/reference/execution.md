# Execution reference for the hfss-agent skill

Reference for `SKILL.md`; loaded by the agent when executing stages. Facts from the environment-compat entry are marked (EC#n) — the entry is authoritative and living.

## Attach-or-launch preamble (every staged script)

Session state lives in the AEDT project — never in a Python process. Each script begins with the preamble, which either launches a desktop or attaches to the running one, and ends by leaving the desktop alive for the next stage.

- Launch: `Hfss(version="2024.1", new_desktop=True, non_graphical=False, project=PROJECT, design=DESIGN, solution_type="Modal")` (EC#1). Cold start is ~6–25 s.
- Attach (preferred when a session is alive): `Desktop(version="2024.1", new_desktop=False)` then `Hfss(project=PROJECT, design=DESIGN, solution_type="Modal", new_desktop=False)` — cross-process attach works, including reading state written by earlier stages (EC#2).
- Project paths: absolute, inside the Workspace. Pass `remove_lock=True` when opening a project a crashed session may have locked (EC#9).
- Teardown at session end ONLY: `desktop.release_desktop(close_projects=True, close_on_exit=True)`, then kill the launched `aedt_process_id` tree until gone and assert zero `ansysedt.exe` left; end the script with `sys.stdout.flush()` + `os._exit(0)` (gRPC teardown hangs; release alone may not reap — EC#10). Between stages: release the client WITHOUT closing (keep the server) or simply exit the script — the next preamble attaches.

## Per-stage checklist

1. **Clarification** — deliver one block: request minimums, missing critical setup features, proposed Recipe + Assumptions, proposed Result QA signals. Record the confirmation verbatim in the summary.
2. **Solution type** — explicit (do not rely on defaults; new designs default to Terminal — EC#11).
3. **Design** — create + save; record design/project names in the summary.
4. **Geometry** — all dims variables (`hfss["name"] = "value"`); sheet-vs-solid choices per Recipe; keep names stable across runs (same-name rebuilds on a dirty project duplicate silently — start from a clean project or wipe, EC#8).
5. **Materials** — by name from the library (`FR4_epoxy`, `pec`, `air`, …); record which and why.
6. **Excitations/boundaries** — pass **face objects**: `hfss.wave_port(<sheet>.faces[0], impedance=50, ...)`; never int ids or edge objects (EC#7). Radiation: `assign_radiation_boundary_to_objects(<airbox>)`.
7. **Mesh** — only what the Recipe requires; adaptivity covers the rest.
8. **Setup + sweep** — one setup named `Setup1`; `create_linear_count_sweep(...)` auto-suffixes the sweep name — read the real name back from `existing_analysis_sweeps` before any report uses it (EC#6).
9. **Validation** — `bool(hfss.validate_simple())` must be True; on False, treat as a failed run and diagnose via the active design errors before retrying (EC#8).
10. **Review gate** — hand the floor to the user; they inspect the Math model in the UI and may tweak. On any tweak: run read-back sync (below).
11. **Solve** — `analyze(setup="Setup1", blocking=False)`; short polls; completion signal = results-on-disk growth (`.asol`/`.sd` files appearing in `<project>.aedtresults/`) — not the return value (EC#5).
12. **Plots** — per Recipe; write to `results/`.
13. **Result QA** — check the agreed signals; report each with numbers or explicit "unreadable (flaky readout)" where the readout fails, and route via re-attach before concluding (EC#6, ticket 07 pending).
14. **Summary** — write `summary.md`: acute decisions, the Model description, Recipe + signals used, any deltas recorded by sync.

## Read-back sync (ADR 0005)

Trigger: any user tweak in the AEDT UI after a stage has run.

1. Introspect the live model with the high-level API: design variables, boundaries, excitations, setups, mesh operations (all enumerable).
2. Diff against the owning stage's staged script.
3. Amend that script so re-running top-to-bottom reproduces the delivered model; keep the change minimal and parameterized.
4. Record the delta in `summary.md`.
5. The Review gate does not close until sync has run.

## Self-correction details

- After every Run, capture errors from the surfaces that work: raised exceptions, `validate_simple()` results, on-disk logs. Raw message-manager calls are broken over gRPC (EC#3).
- Max 3 consecutive failed Runs per Stage; each attempt amends the script with a stated hypothesis.
- Escalate (report to the user with script + error + attempts) on: 3-run cap reached, the identical error twice in a row, or an error unmapped to any KB/playbook cause.

## Learning-loop triggers (ADR 0002)

A proposal to amend the playbook is earned by any of: a user tweak that generalizes to the Recipe class; a backend-compat discovery (lands in the environment-compat entry); a Result-QA anomaly whose resolution generalizes. Fix the current Model first; append only after explicit user approval; project-specific values stay in the summary.
