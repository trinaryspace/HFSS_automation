# 04 — hfss-agent skill scaffold + workspace template

**What to build:** the skill text that a conversation reads to run the whole pipeline, encoding the full conversation contract, plus the per-conversation Workspace template. The skill covers: the one solution-type-agnostic Spine (interpret → clarify → solution type → design → geometry → materials → excitations → mesh → setup/sweep → solve → post-process → reports); the single Clarification block that proposes or derives the Recipe, states gaps as explicit Assumptions, and proposes the Result QA signals for approval; staged scripts (one Stage = one script = one Run) with the standard attach-or-launch preamble, session state living in the AEDT project never in a Python process; full parameterization of geometry via design variables; the visual review gate (ADR 0003); read-back sync that introspects the live model after user UI tweaks and amends the owning stage's script, recording the delta in the summary (ADR 0005); background solves with short status polls; self-correction capped at 3 consecutive failed Runs per Stage with the message manager read after every Run; Result QA against the approved signals; the three learning-loop triggers (generalizing user tweak, backend-compat discovery, generalizable QA anomaly); and the rule to consult the environment-compat entry before promising any API and route around unsupported ones (ADR 0004). The Workspace template holds the staged scripts, the project file, results, and the summary, gitignored as outputs.

**Blocked by:** 02 (the environment-compat entry must exist for the skill to cite as its promise-surface authority)

**Status:** ready-for-agent

- [x] Skill text covers every contract element in the listing above, using the glossary's vocabulary — verified by `skill/hfss-agent/verify_skill.py` (26/26 PASS)
- [x] Skill text is consistent with ADRs 0001–0005 (no review gate via scripts, sync before a gate closes, playbook via approved amendments only)
- [x] Skill text explicitly directs the agent to the environment-compat entry before promising an API and to route around unsupported ones
- [x] Workspace template exists and is gitignored as output (tool and knowledge directories stay clean) — `.gitignore` now covers conversation-workspace outputs (`*.aedt`, `*.aedtresults/`, `results/`, `*.lock`)
- [x] The Workspace template matches the agreed shape (staged script directory, project file, results, summary)

## Comments

- 2026-08-02: **DONE.** Deliverables: `skill/hfss-agent/SKILL.md` (model-invoked skill, brace flow with per-stage completion criteria), `skill/hfss-agent/reference/execution.md` (attach-or-launch preamble, per-stage checklist, read-back sync, self-correction, learning loop), `skill/hfss-agent/templates/workspace/` (README + summary skeleton + empty `src/`), and `skill/hfss-agent/verify_skill.py` as the structural test seam (red→green; runs without AEDT/license).
- Env-compat facts wired into the skill where they change behaviour: high-level-API-only rule (EC#3), solve submission ≠ completion and readout flakiness (EC#5/#6), face-object port assignment (EC#7), validation gate (EC#8), `remove_lock=True` (EC#9), release/kill hygiene (EC#10), explicit Modal (EC#11), RCS route-around (EC#12).
- NOT in scope (pending): wiring the skill into the agent's skills directory (e.g. `~/.agents/skills/hfss-agent/`) — needed before the user's manual check conversation can invoke it. Deployment decision deferred to the user.
