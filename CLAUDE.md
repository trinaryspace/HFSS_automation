@AGENTS.md

## Claude Code

The project instructions above are `AGENTS.md`, imported so this file never
becomes a second copy. What is specific to this harness:

- The `hfss-agent` skill is read from `.claude/skills/hfss-agent`, a link to
  `skill/hfss-agent/` made by `python scripts/install_skill.py`. Run that once
  after cloning (it also links the global `analyze-papers` skill into
  `~/.claude/skills/`). Never copy the skill directory; tier 0 fails on a copy.
- The skill's subagents are `.claude/agents/kb-lookup.md` and
  `.claude/agents/runcard.md`. Invoke them with the Agent tool
  (`subagent_type: kb-lookup` / `runcard`). Their prompts must stay verbatim
  identical to the `agent:` entries in `opencode.json` —
  `scripts/verify_agents.py` enforces it.
- Every per-host difference the skill cares about is one table:
  `skill/hfss-agent/reference/execution.md`, "Harness notes". The rest of the
  skill is host-neutral and must stay that way.
- The Bash tool's `timeout` caps at 10 minutes. A solve is never awaited in a
  bash call; it runs under the detached watchdog (ADR 0006).
- Name the three phase sessions with `/rename <name>-clarify` (`-build`,
  `-solve`); `scripts/session.py --phase` records this session's id so
  `scripts/run_card.py` can find the transcript afterwards.
