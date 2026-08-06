# 07 — Publish docs: ADRs 0006–0008 + glossary terms

**What to build:** publish and validate the documentation decisions of the refactor:

- **ADRs** (drafts already written in the 2026-08-04 grill-with-docs session; this ticket reviews, adjusts if needed, and confirms they match the implemented behavior):
  - `docs/adr/0006-solves-run-under-a-detached-watchdog.md`
  - `docs/adr/0007-phase-sessions-bound-by-state-ledger.md`
  - `docs/adr/0008-idempotent-stage-scripts.md`
- **Glossary:** CONTEXT.md gains three terms (drafts exist from the session): **State ledger** (the per-Workspace file carrying stage progress, variables, and pitfalls between phase sessions), **Run card** (the per-run token/step/wall-time record appended to summary.md by the harness), **Verification line** (the single machine-parseable `PASS:` line each staged script emits).
- Cross-link: ADR 0006 cited from SKILL.md's solve stage; 0007 from the run structure; 0008 from the build doctrine (done in ticket 03 — checked here).

**Status:** ready-for-agent
**Blocked by:** none (drafts exist; finalize after 03/04 land so citations match reality)

- [x] ADRs 0006–0008 present, one-paragraph house style, numbered after 0005
- [x] CONTEXT.md carries the three terms in house format (definition + _Avoid_)
- [x] Skill text cites the new ADRs/terms consistently (cross-checked with 03)

## Comments

- 2026-08-04: Written by the grilling session — see `docs/adr/` and CONTEXT.md for the drafts.
- 2026-08-06: Finalized after tickets 03 (e9dfdb1) and 04 (75d6527/f6cfc7f) landed. Validation against the landed implementation:
  - **ADR 0006** adjusted to match `poll_solve.py`'s actual exit semantics (completion **or stall** — exit 0/2); everything else already matched the landed watchdog flow.
  - **ADR 0007** and **ADR 0008** verified verbatim against SKILL.md/execution.md and the template runners — no changes needed.
  - **ADR 0008's** consequence claim "the environment-compat EC#8 route-around is rewritten to match" was FALSE in the tree (environment-compat.md untouched since f6c3aa3, still advised wipe-as-default) — rewrote the EC#8 route-around to the delete-then-create doctrine (probes still wipe). Heading untouched, spine-api anchors intact.
  - **CONTEXT.md** three terms already in house format (definition + _Avoid_); wording cross-checked against execution.md (ledger contents, `PASS:` contract, run card harness).
  - **Cross-links verified**: ADR 0006 cited from SKILL.md's solve stage (hard rule 8 + Solve step), 0007 from the run structure (session block), 0008 from the build doctrine (hard rule 7 + idle Geometry/Validation steps); execution.md titles its sections with the ADR numbers; workspace template files carry the citations; `verify_skill.py` ADRS dict checks all three (0006 watchdog/solve_progress.txt, 0007 state.md/ledger, 0008 delete-then-create/idempotent) — 58/58 ALL PASS.
  - Full suite green: `verify_skill.py` 58/58, `test_template_runners.py` 24/24, `test_run_card.py` 10/10, `scraping/verify_kb.py` all pass.
  - Installed skill copy (`~/.agents/skills/hfss-agent`) verified in sync with the repo (deployed by the parallel agent, 2026-08-06).

**Status:** ready-for-human
