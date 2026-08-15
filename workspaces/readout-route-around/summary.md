# readout-route-around workspace — Ticket 16 (DONE 2026-08-07)

Probe: validate a route-around for the pyAEDT 1.3.0
`HfssConstants.default_solution` client bug and pin the scripted-readout
call shapes that work on this box (AEDT 2024 R1, pyAEDT 1.3.0, Python
3.10.0, UM license via VPN — standing prerequisites verified before the
run). All evidence is in `evidence/`; authoritative entry text proposed in
ticket 16 Comments (playbook file itself untouched — ADR 0002 approval
required).

Throwaway protocol: `projects/readout_probe.aedt` + `.aedtresults/` is a
Re-entry copy (ADR 0001) of the ticket-02 solved smoke antenna
(`smoke_solve.aedt`, design `solve_design`, `solve_design.asol` present,
108 frequency-point dirs). No solves ran; the original
`workspaces/smoke-matrix/projects/smoke_solve.aedt` was never touched.

## Findings

### 1. The client bug is real, but latent on this box's normal readout flow
- `HfssConstants` (1.3.0) defines `solution_default`, **not**
  `default_solution`; `HFSSDesignSolution.solution_type` getter/setter
  fallbacks and the base-class setter all reference `default_solution`
  (installed `application/design_solutions.py:218,220,249,251`; base
  setter `:89,94,96`). Verified source of truth, and reproduced offline:
  `HFSSDesignSolution(None, DesignType.HFSS, "2024.1").solution_type`
  → `AttributeError: type object 'HfssConstants' has no attribute
  'default_solution'` (run5 5a). pyaedt main (fetched 2026-08-07) still
  pairs `default_solution` references with `solution_default`-only
  constants — the mismatch ships in the current release.
- On the live box the open+readout path NEVER hits it (with a design
  attached, `GetSolutionType()` works over gRPC → getter returns 'Modal',
  runs 1/2/3/4a/5b). The trap fires only when `design_solutions` has no
  odesign or `GetSolutionType()` raises — e.g. gRPC transport flakes
  (run4 4b hit `GrpcApiError: Failed to execute ... OpenProject` mid-session,
  per EC#3 the raw surface partially raises).
- **Route-around (validated, one line, safe):**
  `HfssConstants.default_solution = HfssConstants.solution_default`
  before creating an `Hfss` app. Runs 2/3+5a prove the previously-crashing
  paths then return `'HFSS Terminal Network'`. Keep it applied
  defensively; it changes nothing on the working path.

### 2. Scripted readout WORKS on a solved project — with 1.3.0's own accessors
Fresh attach to the copy, all runs 2026-08-07 (licenses checked in):

| shape | result |
|---|---|
| `existing_analysis_sweeps` | `['Setup1 : LastAdaptive', 'Setup1 : Sweep_MM13NY']` — auto-sweep suffix confirmed (EC#6 pattern) |
| `post.get_solution_data("dB(S(1,1))")` (no ctx) | SolutionData, **filled**: `_solutions_real` shape (101,2), Freq 2.0–3.0 GHz |
| `post.get_solution_data(..., setup_sweep_name="Setup1 : Sweep_MM13NY")` | filled (101,2) in all 3 independent sessions (runs 2, 3, 4a) |
| `post.get_solution_data(..., "Setup1 : LastAdaptive")` | filled (1,2) @2.4 GHz |
| `post.create_report` on the sweep | `Standard` report created |
| `post.export_report_to_file(csv/tab)` | 102-line files, real values |
| `SolutionData.export_data_to_csv` | 101-row CSV of the sweep |
| `post.export_report_to_jpg` | True, jpg written |

### 3. The EC#6 "unfilled" flake is (today) an accessor artifact — refine the negative route
- `SolutionData.data_real` does **not exist in pyAEDT 1.3.0** (verified:
  zero `data_real` occurrences in the installed wheel). The prior-art
  readers `diag_readout*.py` / `s11_readout.py` judged fill-state via
  `hasattr(data, "data_real")` / `data.data_real()` → on 1.3.0 they
  *always* read "unfilled", and `diag_solve_status.py` polls
  `hfss.results.*` which doesn't exist on `Hfss` either
  (`AttributeError: 'Hfss' object has no attribute 'results'`, run2 G).
  Two of the three fail-era probes were therefore structurally broken
  readers, not evidence of an empty server.
- Correct 1.3.0 accessors: `data.full_matrix_real_imag`, or
  `data.get_expression_data(expr, formula="real")` (this is what the
  touchstone parser uses), plus `data.primary_sweep_values`.
- The one historical positive (S11 min ≈ 0.47 dB, `diag_readout.py`,
  2026-08-02) remains unmatched by today's trace (copy S11 sweeps
  −0.038 → −0.054 dB, 2.4 GHz ≈ −0.044 dB) — different project instance;
  not needed to reconcile. The "fresh attach → filled" pattern of that
  positive matched today's 3/3 sessions; today no run produced the
  in-session-after-analyze / reopen empty state (that state cannot be
  exercised without a solve, which this ticket forbids).

## Still failing / not available on this box (recorded)
- `data.data_real()` / `data.data_imag` — absent in 1.3.0.
- `hfss.results.get_solution_data(...)` — no `results` attribute.
- `HfssConstants.default_solution` — absent until the one-line alias.

## Environment-compat amendment
Proposed entry text (item 6 rewrite + new item text) drafted in ticket 16
Comments per the established amendment discipline (ADR 0002 — approval
required; ADR 0004 — single accumulation point). File untouched.

## Hygiene
No `ansysedt.exe` left running; probe server processes killed until gone at
each run's end (EC#9/10 pattern). Original smoke-matrix project untouched.
