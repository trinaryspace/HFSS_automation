# 04 — hfss-agent skill scaffold + workspace template

**What to build:** the skill text that a conversation reads to run the whole pipeline, encoding the full conversation contract, plus the per-conversation Workspace template. The skill covers: the one solution-type-agnostic Spine (interpret → clarify → solution type → design → geometry → materials → excitations → mesh → setup/sweep → solve → post-process → reports); the single Clarification block that proposes or derives the Recipe, states gaps as explicit Assumptions, and proposes the Result QA signals for approval; staged scripts (one Stage = one script = one Run) with the standard attach-or-launch preamble, session state living in the AEDT project never in a Python process; full parameterization of geometry via design variables; the visual review gate (ADR 0003); read-back sync that introspects the live model after user UI tweaks and amends the owning stage's script, recording the delta in the summary (ADR 0005); background solves with short status polls; self-correction capped at 3 consecutive failed Runs per Stage with the message manager read after every Run; Result QA against the approved signals; the three learning-loop triggers (generalizing user tweak, backend-compat discovery, generalizable QA anomaly); and the rule to consult the environment-compat entry before promising any API and route around unsupported ones (ADR 0004). The Workspace template holds the staged scripts, the project file, results, and the summary, gitignored as outputs.

**Blocked by:** 02 (the environment-compat entry must exist for the skill to cite as its promise-surface authority)

**Status:** ready-for-agent

- [ ] Skill text covers every contract element in the listing above, using the glossary's vocabulary
- [ ] Skill text is consistent with ADRs 0001–0005 (no review gate via scripts, sync before a gate closes, playbook via approved amendments only)
- [ ] Skill text explicitly directs the agent to the environment-compat entry before promising an API and to route around unsupported ones
- [ ] Workspace template exists and is gitignored as output (tool and knowledge directories stay clean)
- [ ] The Workspace template matches the agreed shape (staged script directory, project file, results, summary)
