# 02 — Smoke-test matrix + environment-compat entry

**What to build:** the playbook store exists with its environment-compat entry, populated with one recorded outcome per probe of the one-time smoke-test matrix run against the live 2024 R1 backend: attach-onto-running-desktop semantics, `analyze(blocking=False)` non-blocking behavior, and the RCS/SBR+ data surface (`get_rcs_data`, `MonostaticRCSExporter` — expected to fail per ADR 0004), plus any additional APIs the scaffold needs as they surface. After this ticket, the skill's promise surface — which APIs may be promised vs routed around — is decidable from a single source of truth.

**Blocked by:** 01 (repair + trivial launch must work so probes can run)

**Status:** ready-for-agent

- [x] Every matrix probe runs once against the live backend; each outcome (works / broken / behavior notes) is recorded in the environment-compat entry
- [x] The environment-compat entry is the single accumulation point for backend-compat facts (ADR 0004)
- [x] Probes that solve (e.g. `analyze`) run only on throwaway designs in the Workspace, never on anything the user cares about
- [x] No playbook content beyond the environment-compat entry is added (ADR 0002 — growth only via approved amendments)
- [x] Each recorded outcome is detailed enough that a skill-generated route-around decision can be made from it blind

## Comments

- 2026-08-02: **DONE.** Entry lives at `knowledge/playbook/environment-compat.md`; probes in `workspaces/smoke-matrix/src/`; workspace summary in `workspaces/smoke-matrix/summary.md`.
- Headline outcomes: launch+attach work (cross-process attach verified, including reading launcher-written state); blocking solve True @ ~147 s; `analyze(blocking=False)` returns in ~3 s and the solve completes in background; raw COM surface partly broken over gRPC (route around via high-level API); result readout `post.get_solution_data` works-but-flaky (unfilled SolutionData; retry/re-attach pattern); `get_rcs_data`/`MonostaticRCSExporter` present but unusable on this box (optional deps + no SBR+ license — matches ADR 0004); `Hfss()` defaults new designs to Terminal (Modal must be explicit).
- Operating notes added: UM VPN is a standing prerequisite for the license server; crashed runs leave lock files + server processes (use `remove_lock=True` and kill-until-gone); pandas 2.3.3 installed as part of the RCS chain evidence.
