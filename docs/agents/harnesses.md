# Harnesses

The `hfss-agent` skill runs under two agent harnesses, **opencode** and
**Claude Code**, from one source tree. Nothing in the skill is forked per
host; the differences are confined to where each harness looks for things,
and every one of those places is either a link or a checked copy.

## The rule

**One skill, two link roots, zero copies.** Anything a harness must read from
its own location is a link to the repo (`scripts/install_skill.py`), and the
one thing that cannot be linked — the subagent prompts, because the two
frontmatter formats are incompatible — exists twice under a tier-0 check
that fails when the copies differ (`scripts/verify_agents.py`).

| What | opencode | Claude Code | Kept in step by |
|---|---|---|---|
| Skill | `~/.agents/skills/hfss-agent` | `.claude/skills/hfss-agent` | both are links; `install_skill.py --check` in tier 0 |
| Project instructions | `AGENTS.md` | `CLAUDE.md` → `@AGENTS.md` | an import, not a copy |
| Subagents `kb-lookup`, `runcard` | `opencode.json` `agent:` | `.claude/agents/*.md` | `verify_agents.py` in tier 0 (prompts verbatim, tool surfaces agree) |
| `analyze-papers` skill | `~/.agents/skills/analyze-papers` | `~/.claude/skills/analyze-papers` | a link the installer makes when the source exists |
| Session store (run card) | `opencode.db` | `~/.claude/projects/*/<id>.jsonl` | `scripts/run_card.py` reads both; `claude_transcript.py` is the one parser for the second, with a real captured fixture |
| Session identity | slug `<name>-<phase>` | `/rename`, plus `CLAUDE_CODE_SESSION_ID` recorded by `scripts/session.py` | `results/state/session.json` carries `host` + `host_session_id` |
| Permissions | per-agent `permission` maps | `.claude/settings.json` allow-list, per-agent `tools:` | — |

The per-host table the *agent* reads at run time lives in the skill itself:
`skill/hfss-agent/reference/execution.md`, "Harness notes". This page is the
maintainer's view of the same thing.

## When you touch one side

- Edited a subagent prompt? Edit it in both `opencode.json` and
  `.claude/agents/<name>.md`, then run `python scripts/verify_agents.py`.
- Changed what the skill needs from the host (a new tool, a new global
  skill)? Add a row to the "Harness notes" table in `execution.md` and, if
  it is a location, a `Target` in `install_skill.py`.
- Changed a run-card metric? The mapping for the Claude Code side is stated
  in `scripts/claude_transcript.py`'s docstring; keep the two definitions
  the same and recapture the fixture
  (`python scripts/claude_transcript.py --capture <id> --out scripts/fixtures/claude-code`),
  which refuses a slice that parses differently from its original.

## Why not a plugin, or a shared agent file

Claude Code can bundle skills and agents as a plugin, and both harnesses can
read agent definitions from markdown with frontmatter. Neither helps here:
the repo-local `.claude/` layout is already a supported install, and the two
frontmatter dialects disagree on the `tools` and `model` keys, so a single
file would have to be wrong for one host. The verbatim check is smaller and
cannot be silently wrong.
