# 16 — pyAEDT readout route-around (tooling pre-work)

**What to build:** A validated route-around for the pyAEDT 1.3.0 client bug blocking the scripted Readout paths on this box — the missing `HfssConstants.default_solution` — validated on a throwaway copy of a project so the fix never risks a real workspace. The route-around's findings (exact call shape that does work on pyAEDT 1.3.0 / AEDT 2024 R1) land in the environment-compat entry through the established amendment discipline. This is pre-work: it is non-blocking for every other corrective ticket, and the acceptance of any flow never depends on a scripted Readout succeeding — the UI read is authoritative (see ticket 17).

**Blocked by:** None — can start immediately.

**Status:** ready-for-human

- [x] Route-around validated on a throwaway copy: at least one scripted Readout shape returns data
- [x] Evidence artifact recorded in the probe workspace
- [x] Environment-compat amendment drafted into Comments (approval required per ADR 0002; entry file untouched)

## Comments

### Agent run 2026-08-07 (ticket 16, live probe — VPN+license verified, sole AEDT agent)

Probe workspace: `workspaces/readout-route-around/` (throwaway Re-entry copy of
the ticket-02 solved smoke design, `projects/readout_probe.aedt`; original
untouched; no solves ran). Evidence: `src/probe_*.py` ×5, `evidence/run*.txt`
×5 + exported artifacts (`rubar_full.csv/.tab/.jpg`, `rubar_s11.csv`,
`rubar_probe.csv`), `summary.md`.

**Verdict: route-around validated; scripted readout WORKS on this box with
1.3.0's own accessors — one import-time alias + accessor correction.**

1. *The client bug is real but latent on the normal flow.* Reproduction
   (offline, deterministic): `HFSSDesignSolution(None, DesignType.HFSS,
   "2024.1").solution_type` → `AttributeError: type object 'HfssConstants' has
   no attribute 'default_solution'` (installed 1.3.0 pairs
   `design_solutions.py:218/220/249/251` `default_solution` references with a
   constants class that only defines `solution_default`). pyaedt main
   (2026-08-07) still mixes both names — it is current-release state, not an
   install defect. On the live box, open+readout never reaches it (design
   attached → `GetSolutionType()` over gRPC works, getter returns 'Modal' in
   all 5 sessions); it fires only in odesign-less paths or when
   `GetSolutionType()` raises (gRPC surface does flake — run4 4b hit
   `GrpcApiError: ... OpenProject` mid-session, cf. EC#3).
   **Route-around (validated):** `HfssConstants.default_solution =
   HfssConstants.solution_default` before app creation — the
   previously-crashing paths then return `'HFSS Terminal Network'` (run5 5a
   before/after, run2 offline annex); no behavior change on the working path.
   Apply defensively in every scripted flow.

2. *Readout shapes that return real data (fresh attach, solved copy,
   3 independent sessions):* `post.get_solution_data("dB(S(1,1))")` —
   no context; with the actual auto-sweep `setup_sweep_name="Setup1 :
   Sweep_MM13NY"` (filled 101×2, 2.0–3.0 GHz; per EC#6 the suffix is
   random per project — always read `existing_analysis_sweeps` first);
   `"Setup1 : LastAdaptive"` (1×2 @2.4 GHz). Exports: `post.create_report`
   + `post.export_report_to_file(csv/tab)` (102-line files with real
   values), `SolutionData.export_data_to_csv` (101-row sweep dump),
   `post.export_report_to_jpg`. S11 sweeps −0.038 → −0.054 dB.

3. *Refined negative route (why EC#6 looked flaky):* `SolutionData.data_real`
   does **not exist in pyAEDT 1.3.0** (zero occurrences in the wheel). The
   prior-art readers (`diag_readout*.py`, `s11_readout.py`) judged fill via
   `hasattr(data, "data_real")` → always "unfilled" on 1.3.0; and
   `diag_solve_status.py` polled `hfss.results.*`, which is also absent on
   1.3.0 (`AttributeError: 'Hfss' object has no attribute 'results'`, run2
   shape G). Correct 1.3.0 accessors: `full_matrix_real_imag` /
   `get_expression_data(expr, "real")` + `primary_sweep_values`. The
   one historical positive (fresh attach, 0.47 dB) is the pattern that today
   also fills 3/3 sessions. Today no solve-free run reproduced genuine
   server-empty data; the in-session-after-analyze / reopen emptiness stays
   untested by design (no solves per ticket).

**Proposed environment-compat amendment (ADR 0002 — approval required;
`knowledge/playbook/environment-compat.md` left untouched until then):**

Replace matrix item 6 with:

> ### 6. Reading results (`post.get_solution_data`) — WORKS on solved projects; use 1.3.0's accessors (verified 2026-08-07, ticket 16)
> Fresh attach to a solved project + `post.get_solution_data(expressions=..., setup_sweep_name=<actual sweep from existing_analysis_sweeps>)` returns a solution data object filled with the whole sweep (verified 3/3 sessions; e.g. 101 points 2–3 GHz). `setup_sweep_name` must be the *actual* sweep name (auto-generated random suffix, e.g. `Setup1 : Sweep_MM13NY`).
> **Accessor correction:** `SolutionData` on 1.3.0 has **no `data_real`**; prior probes' `hasattr(data,"data_real")` always read "unfilled" — that was an accessor artifact, not evidence of empty server data. Read values via `data.full_matrix_real_imag` or `data.get_expression_data(expr, formula="real")` + `data.primary_sweep_values`.
> `hfss.results.*` does not exist on Hfss in 1.3.0 — use `hfss.post.get_solution_data`.
> Export shapes verified: `post.create_report`, `post.export_report_to_file(csv|tab)`, `SolutionData.export_data_to_csv`, `post.export_report_to_jpg`.
> Residual: in-session-after-solve / reopen emptiness not re-exercised (needs a solve; ticket 16 ran solve-free by design). Artifacts: `workspaces/readout-route-around/evidence/run*.txt`.

And add matrix item 14:

> ### 14. `HfssConstants.default_solution` MISSING on 1.3.0 — apply one-line alias defensively
> Installed 1.3.0 wheel references `_design_type.default_solution` in `application/design_solutions.py` (fallbacks when no design is attached or `GetSolutionType()` fails) but `HfssConstants` defines only `solution_default` → `AttributeError` on those paths (reproduced offline; pyaedt main still mixes both names). Latent on this box's normal open+readout flow (`GetSolutionType` succeeds over gRPC on attach).
> **Route-around:** at process start, `HfssConstants.default_solution = HfssConstants.solution_default` (i.e. `"HFSS Terminal Network"`); validated in both directions, no behavior change on the working path. Artifact: `workspaces/readout-route-around/src/probe_stock3.py`, `evidence/run5_stock_trap_before_after.txt`.

Acceptance checkboxes done; evidence in the probe workspace; amendment
awaiting human approval.
