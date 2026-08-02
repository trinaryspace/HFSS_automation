# 02 — Smoke-test matrix + environment-compat entry

**What to build:** the playbook store exists with its environment-compat entry, populated with one recorded outcome per probe of the one-time smoke-test matrix run against the live 2024 R1 backend: attach-onto-running-desktop semantics, `analyze(blocking=False)` non-blocking behavior, and the RCS/SBR+ data surface (`get_rcs_data`, `MonostaticRCSExporter` — expected to fail per ADR 0004), plus any additional APIs the scaffold needs as they surface. After this ticket, the skill's promise surface — which APIs may be promised vs routed around — is decidable from a single source of truth.

**Blocked by:** 01 (repair + trivial launch must work so probes can run)

**Status:** ready-for-agent

- [ ] Every matrix probe runs once against the live backend; each outcome (works / broken / behavior notes) is recorded in the environment-compat entry
- [ ] The environment-compat entry is the single accumulation point for backend-compat facts (ADR 0004)
- [ ] Probes that solve (e.g. `analyze`) run only on throwaway designs in the Workspace, never on anything the user cares about
- [ ] No playbook content beyond the environment-compat entry is added (ADR 0002 — growth only via approved amendments)
- [ ] Each recorded outcome is detailed enough that a skill-generated route-around decision can be made from it blind
