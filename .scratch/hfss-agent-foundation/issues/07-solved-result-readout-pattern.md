# 07 — Reliable solved-result readout pattern for Proof 1 Result QA

**What to build:** a trustworthy, repeatable way to read solved results (S-parameters over a sweep) from a solved Modal design on this backend, because the current `post.get_solution_data` path is flaky (environment-compat entry item 6: unfilled `SolutionData` with "No Data Available" on most attempts; one positive observation only). Proof 1's Result QA needs signals it can act on blind.

**Blocked by:** 02 (entry item 6 documents the flakiness this ticket targets)

**Status:** ready-for-agent

- [ ] Reproduce the current flaky path on the shared smoke design (re-open solved project, read `dB(S(1,1))`)
- [ ] Evaluate at least two alternative readout routes and pick one that succeeds reliably more than once: candidates — (a) fresh-attach readout pattern (new desktop session attached to the solved project, then `get_solution_data`), (b) direct parse of on-disk results (`.aedtresults/<design>.asol` / per-frequency `.sd` files), (c) `export_results`/`export_report` to CSV and read the file
- [ ] Encode the winning pattern as a helper in the smoke-matrix tooling and demonstrate ≥2 consecutive successful reads on the same solved project
- [ ] Update the environment-compat entry (item 6) with the new route-around, or record why the flakiness persists
- [ ] State, for the skill text (ticket 04), which readout call Proof 1 QA scripts should use
