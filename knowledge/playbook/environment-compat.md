# Environment-compat entry

**The single accumulation point for backend-compat facts** (ADR 0004). Facts
here are appendable only through the smoke-matrix ceremony or an approved
learning-loop amendment (ADR 0002). Readers: the hfss-agent skill consults
this entry before promising any API on this machine.

Last updated: **2026-08-17** — entry #6 (readout) amended under ADR 0002 with
maintainer approval; the 08-02 text is retained inline for provenance. Base
matrix still 2026-08-02 (ticket 02). Machine context: local Windows,
AEDT 2024 R1 (`v241`, `C:\Program Files\AnsysEM\v241\Win64`), Python 3.10.0,
pyAEDT **1.3.0** (importable namespace `ansys.aedt.core`; `pip check` clean).

## Standing prerequisites

- **License**: AEDT requires the UM license server
  (`1055@LICENSE-ANSYS.ENGIN.UMICH.EDU`); the server is reachable **only
  with the UM VPN (Cisco Secure Connect) connected**. Without VPN+license,
  design-open and every solve stall. (FlexNet `-15,10032`, feature
  `hfss_gui`, observed verbatim in stock-AEDT scripting.)
- **No `pyaedt` top-level import**: by design at 1.3.0 (verified against
  the official wheel — zero `pyaedt/` files). Always `import ansys.aedt.core`.

## Transport

- pyAEDT 1.3.0 on Windows uses the gRPC "wnua" transport **exclusively**:
  the client loads (in-process via ctypes/PyDLL) AEDT's own
  `PyDesktopPlugin.dll` and launches a real `ansysedt.exe` server process
  (`aedt_process_id`). `settings.use_grpc_api=False` does **not** change the
  transport (verified in logs). pyaedt 1.2.0 behaved identically
  (venv-tested) — not a client-version issue.
- DLL calls hold the GIL: a blocked call freezes the entire client process
  (watchdog threads stop). Guard against indefinite stalls by design.

## Matrix outcomes (probe verdicts + route-around decisions)

### 1. Launch new graphical desktop — WORKS
`Hfss(version="2024.1", new_desktop=True, non_graphical=False, design=...)`
launches, creates project + design, writes objects, and releases. Cold
start 6–23 s; then project operations ~instant.
**Route-around**: none needed; this is the baseline launch preamble.
Artifact: `workspaces/env-probe/src/env_probe.py` (PASS).

### 2. Attach onto running desktop — WORKS (cross-process)
Launch script releases with `release_desktop(close_projects=False,
close_on_exit=False)`, leaving the server alive; a **second python
process** re-attaches with `Desktop(new_desktop=False)` /
`Hfss(project=..., new_desktop=False)`: discovers the session
("Found active AEDT gRPC session on port …"), reads launcher-written state
(design variables), works. Attach to a stock-launched `ansysedt.exe`
(native gRPC :50051) also connects.
**Route-around**: staged scripts may attach instead of relaunching; keep
the server alive between stages (that matches "session state lives in the
AEDT project"). Artifact: `workspaces/smoke-matrix/src/launch_keep.py` +
`attach_reuse.py` (PASS).

### 3. Raw COM call surface over gRPC — PARTIALLY BROKEN (use high-level API)
On project/design objects: `NewProject`, `GetActiveProject`, `GetName`,
`InsertDesign("HFSS", name, "HFSS Modal Network", "")` work.
`SetActiveDesign`, `GetDesignNames`, `GetNumDesigns`,
`GetActiveProjectName`, `GetMessages` raise GrpcApiError (even licensed);
`GetActiveDesign` returns None with no design; `InsertDesign("CIRCUIT",…)`
→ server-side "unsupported design type = circuit". pyaedt 1.3.0's own
high-level paths (Hfss etc.) sidestep the broken surface and work
end-to-end.
**Route-around**: never call the raw COM surface directly; use the
high-level `ansys.aedt.core` API everywhere. A plain high-level flow is
the only supported pattern. Artifact: `workspaces/env-probe/src/
diag_call_surface.py`, `diag_transport_bisect.py` (evidence).

### 4. Blocking solve — WORKS
Minimal valid Modal design (wave port on face of PEC solid + radiation
airbox, 3-pass adaptive 2.4 GHz, 101-pt discrete sweep 2–3 GHz):
`validate_simple()` True; `analyze(setup="Setup1", blocking=True)` returns
True after ~147 s (mesh+solve+sweep).
**Route-around**: none; the reference outcome for recipe QA.
Artifact: `workspaces/smoke-matrix/src/probe_solve_blocking.py` (PASS).

### 5. Non-blocking solve — WORKS (submission); background completion INFERRED
`analyze(blocking=False)` returns `True` in ~3 s — submission only, as
documented (a `True` return does not mean solved). Background completion
is *inferred* from two observations, not directly asserted by the probe:
(a) the same design solves in ~150 s when run `blocking=True` (item 4),
and (b) solver artifacts (`solve_design.asol`, per-frequency `.sd` files)
appeared on disk in the project results folder while the non-blocking run
polled. The non-blocking probe itself can only confirm submission + poll
for data (whose readout is flaky, item 6); it cannot fail on "solve did
not complete". Follow-up ticket 07 exists to close this gap for Proof 1.
**Route-around**: launched with `blocking=False`, then poll for completion
(see 6); do NOT treat the `True` return as "solved"; verify completion by
an independent signal (results-on-disk growth or a blocking re-analyze).
Artifact: `workspaces/smoke-matrix/src/probe_solve.py` (submission PASS).

### 6. Reading results (`post.get_solution_data`) — WORKS. The "flakiness" was mostly a broken reader.

**Amended 2026-08-17 (approved learning-loop amendment, ADR 0002).** The entry
below is the 2026-08-02 matrix observation and is kept for provenance, but its
conclusion is superseded: the dominant cause of "unfilled SolutionData" was
**our own fill-state check**, not the server.

- **`SolutionData.data_real` does not exist in pyAEDT 1.3.0** — zero occurrences
  in the installed wheel. Every reader that judged fill-state with
  `hasattr(data, "data_real")` or `data.data_real()` therefore reported
  "unfilled" **on a perfectly good fetch**, and discarded it. That is what the
  fail-era probes were measuring.
- **`hfss.results` does not exist either** — `Hfss` has no `results` attribute,
  so `hfss.results.get_solution_data(...)` always raises.
- **Correct 1.3.0 accessors**: `full_matrix_real_imag`, or
  `get_expression_data(expr, formula="real")` (what the touchstone parser uses),
  plus `primary_sweep_values` for the axis.
- **Verified working on a solved project** (2026-08-07, three independent fresh
  attaches): `get_solution_data("dB(S(1,1))")` with no context returned filled
  data; with `setup_sweep_name` set to the real sweep name it filled in all
  three sessions. `post.export_report_to_file` (csv/tab) and
  `SolutionData.export_data_to_csv` both wrote real values, and
  `export_report_to_jpg` returned True.
- **Sweep names carry a random suffix** (`Setup1 : Sweep_MM13NY`), so read the
  name back from `existing_analysis_sweeps` — never hardcode it.
- **`HfssConstants.default_solution` does not exist**, and pyAEDT's own
  `HFSSDesignSolution` solution_type getter/setter fallbacks reference it.
  Confirmed live on this box 2026-08-17: `HfssConstants.solution_default` is
  `'HFSS Terminal Network'` while `HfssConstants.default_solution` raises
  `AttributeError`. The class lives in
  **`ansys.aedt.core.generic.aedt_constants`** (not `application.design_solutions`,
  where an earlier note placed it). The trap only fires when `design_solutions`
  has no odesign or `GetSolutionType()` raises — i.e. when the gRPC transport is
  already flaking, which is exactly when a readout is being retried.
  **Route-around**: alias `default_solution = solution_default` before
  constructing `Hfss`. One line, changes nothing on the working path.

**Route-around, consolidated**: use
`skill/hfss-agent/templates/workspace/src/read_results.py`. It carries all of
the above — the correct accessors, the sweep-name read-back, the export
fallbacks and the constants alias — and is covered by the tier-0 `readout`
suite so the `data_real` regression cannot return silently. Do not hand-write a
fill-state check; every run that did got it wrong.

**Still true**: the readout can genuinely raise (`GrpcApiError` on
`GetVariables`/`GetSetups`) on a partially functional channel, reproducibly, even
on a fresh attach to a copy. So keep the skill's one-shot policy: one scripted
attempt plus one retry on a fresh attach, then hand the plot to the user and
report the signal as read from the UI. `read_results.read_expression` never loops
and returns an actionable note instead of raising.

---

**Original 2026-08-02 observation, retained for provenance:**
`hfss.post.get_solution_data(expressions="dB(S(1,1))")` returned real S11
data (min ≈ 0.47 dB for the smoke antenna) exactly once — on a fresh
attach to a project solved by an earlier session (`diag_readout.py`).
Every other attempt was an **unfilled `SolutionData`** (has
`primary_sweep_values`, no `data_real`) with AEDT warnings "Solution Data
failed to load / No Data Available": in the solving session right after
`analyze`, and on subsequent reopens (`diag_readout2.py`,
`diag_solve_status.py` — sweeps listed pre-solve, `.asol` present,
readout never filled). Retries within a session don't reliably heal it;
the positive case has not been reproduced since. Explicit
`setup_sweep_name` must use the *actual* sweep name (auto-generated with a
random suffix, e.g. `Setup1 : Sweep_2AGE6M`).
**Route-around**: treat an unfilled SolutionData as "not ready"; retry
with backoff; prefer re-attaching (fresh session) to read results; print
what is observed — a flaky readout is expected, a missing `.asol` is not.
Do not put QA verdicts on this readout until ticket 07 lands a reliable
pattern. Artifact: `workspaces/smoke-matrix/src/s11_readout.py` +
`diag_readout*.py`, `diag_solve_status.py`.

### 7. Excitation assignments — WORKS with caveats (pattern matters)
`wave_port(<face object>, ...)` works (boundary created). Assigning by
**id** (int) or edge breaks: pyaedt maps ids to the `Objects` selection
kind and the 2024 R1 macro layer rejects it ("a geometry selection is
required for assignment"); `lumped_port(edge_id)` same failure; passing an
`EdgePrimitive` as `integration_line` crashes pyaedt (`'<' not supported
between edgeprimitive and int`).
**Route-around**: always pass the **face object** (`<sheet>.faces[0]`) to
wave_port; never pass int ids; a port sheet auto-integration has
validation risk (see 8) — the solid-face port with default integration is
the reliable shape.
Artifact: `workspaces/smoke-matrix/src/micro_probe_excitation.py`.

### 8. Validation gates — MUST use before solve
`validate_simple()` returns int (1 = valid). The sheet-based wave port
with auto integration line produced an INVALID design; the solid-face port
pattern validates True. Reusing a project file with same-name objects
silently duplicates geometry/ports and invalidates.
**Route-around**: `validate_simple()` before every solve. Staged scripts
are delete-then-create (ADR 0008): each script deletes the objects,
boundaries, excitations, mesh operations, and sweeps it (re)creates before
creating them, so re-running any stage in place converges — no fresh
project needed; wipe-and-rebuild is demoted to an explicit escalation
tool, while probe workspaces still wipe their project dir first.

### 9. Project files and locks — manage explicitly
AEDT writes `<name>.aedt` + `<name>.aedtresults/` beside the project
(probe projects live in the probe workspace). Killed sessions leave
`.lock` files; `Hfss(remove_lock=True)` clears them. Crash-killed runs
leave the `ansysedt.exe` server process alive and the project locked.
**Route-around**: pass `remove_lock=True`; after any crashed run, kill
stray `ansysedt.exe` (kill `aedt_process_id` until gone; psutil) before
the next run.

### 10. Release / process hygiene — kill-until-gone required
`release_desktop(close_on_exit=True)` closes AEDT in the attach case but
sometimes only logs "released" without terminating the launched server;
interpreter exit also hangs on gRPC teardown.
**Route-around**: probe pattern = release, then kill the
`aedt_process_id` until gone (psutil), assert exit, then `os._exit(0)` —
never rely on release to reap the process. (See env_probe.py.)

### 11. Solution-type default — Terminal, not Modal
`Hfss(design=..., solution_type=None)` creates the design with
**Terminal** solution default (observed 2026-08-02, 1.3.0/2024 R1).
**Route-around**: recipe Clarification must pass `solution_type="Modal"`
explicitly for driven-modal recipes.

### 12. RCS/SBR+ surface — PRESENT BUT NOT USABLE ON THIS BOX
`Hfss.get_rcs_data` attribute exists; `MonostaticRCSExporter` imports.
Calling `get_rcs_data([2.4], setup=...)` on a plain Modal design fails
past a chain of optional deps (pandas — installed 2.3.3 → pyvista — absent)
into the geometry export, and could only ever proceed with a licensed SBR+
design/solve anyway (SBR+ feature not evidenced on this license).
`frequencies` must be a list (float raises `len()` TypeError client-side).
**Route-around**: do not promise `get_rcs_data`/`MonostaticRCSExporter`
for 2024 R1 flows (matches ADR 0004's expectation); keep optional deps of
the client surface documented (pandas installed, pyvista missing — install
only if an SBR flow is ever licensed). Artifact: `probe_rcs.py`.

### 13. `HFSSCOMENGINE.exe` — opportunistic observation (outside matrix scope)
Exits with code -3 standalone; no WER report. Recorded during the ticket-01
escalation investigation, not part of the matrix probe list; not on any
current flow's path; revisit only if a stage needs it.

## Appendix: environment state the matrix left behind

- pandas 2.3.3 installed (needed by rcs_exporter import chain).
- Probe workspaces: `workspaces/env-probe/` (ticket 01) and
  `workspaces/smoke-matrix/` (ticket 02), each with `projects/` outputs.
- No `ansysedt.exe` / probe python processes left running.

## Verification of this entry

Cross-checked by the final full-matrix run (2026-08-02): attach pair PASS,
blocking solve True @147 s, non-blocking submission True @3.3 s,
readout flakiness reproduced as recorded, RCS chain stops at optional-dep
as recorded.
