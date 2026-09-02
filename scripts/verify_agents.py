"""Check that the skill's subagents are defined identically for both harnesses.

The skill names two subagents — `kb-lookup` and `runcard` — and expects the
host to route to them. Each harness discovers subagents from its own place:

- **opencode** reads the `agent:` map in `opencode.json` (inline `prompt`,
  `permission` map, provider-aliased `model`).
- **Claude Code** reads `.claude/agents/<name>.md` (YAML frontmatter with
  `name` / `description` / `tools` / `model`, prompt as the body).

Neither format can be pointed at the other, so the prompt text exists twice.
This check is what keeps the two copies one artifact: the prompt bodies must
match verbatim, the agent sets must match, the tool surfaces must agree with
the opencode permission map, and every subagent the skill text names must be
defined for both hosts. It runs in tier 0, so a one-sided edit fails the gate
before it can ship. Stdlib only, no harness needed.

Usage: python scripts/verify_agents.py
"""

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPENCODE_JSON = os.path.join(REPO, "opencode.json")
CLAUDE_AGENTS = os.path.join(REPO, ".claude", "agents")
SKILL_TEXTS = [
    os.path.join(REPO, "skill", "hfss-agent", "SKILL.md"),
    os.path.join(REPO, "skill", "hfss-agent", "reference", "execution.md"),
]

# Claude Code tool names that the opencode permission keys stand for.
EDIT_TOOLS = {"Write", "Edit", "NotebookEdit"}
BASH_TOOLS = {"Bash", "PowerShell"}
SPAWN_TOOLS = {"Agent", "Task"}


def load_jsonc(path):
    """opencode.json carries `//` comment lines; json.loads does not."""
    with open(path, encoding="utf-8") as fh:
        lines = [line for line in fh
                 if not line.lstrip().startswith("//")]
    return json.loads("".join(lines))


def opencode_subagents(config):
    return {name: spec for name, spec in config.get("agent", {}).items()
            if spec.get("mode") == "subagent"}


def parse_frontmatter(text):
    """Return (fields, body) for a `---` fenced markdown file."""
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.S)
    if not match:
        return None, text
    fields = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, match.group(2)


def claude_subagents():
    agents = {}
    if not os.path.isdir(CLAUDE_AGENTS):
        return agents
    for entry in sorted(os.listdir(CLAUDE_AGENTS)):
        if not entry.endswith(".md"):
            continue
        with open(os.path.join(CLAUDE_AGENTS, entry), encoding="utf-8") as fh:
            fields, body = parse_frontmatter(fh.read())
        agents[entry[:-3]] = {"fields": fields or {}, "body": body}
    return agents


def normalize(text):
    return " ".join(text.split())


def claude_tools(fields):
    raw = fields.get("tools", "")
    return {tool.strip() for tool in raw.split(",") if tool.strip()}


def permission_state(spec, key):
    """Collapse opencode's per-key permission (string or glob map) to a verdict."""
    value = spec.get("permission", {}).get(key, "allow")
    if isinstance(value, dict):
        return "allow" if any(v == "allow" for v in value.values()) else "deny"
    return value


def named_in_skill():
    """Subagent names the skill text refers to as `<name>` subagent."""
    names = set()
    pattern = re.compile(r"`([a-z][a-z0-9-]*)`\s+subagent")
    for path in SKILL_TEXTS:
        with open(path, encoding="utf-8") as fh:
            names.update(pattern.findall(fh.read()))
    return names


def check(label, ok, detail=""):
    print("  %-52s %s%s" % (label, "ok" if ok else "FAIL",
                             (" — " + detail) if detail and not ok else ""))
    return ok


def main():
    config = load_jsonc(OPENCODE_JSON)
    oc = opencode_subagents(config)
    cc = claude_subagents()
    failures = 0

    failures += not check("opencode defines subagents", bool(oc))
    failures += not check("claude code defines subagents (.claude/agents)", bool(cc))
    failures += not check(
        "same subagent set on both hosts", set(oc) == set(cc),
        "opencode=%s claude=%s" % (sorted(oc), sorted(cc)))

    for name in sorted(set(oc) & set(cc)):
        spec, agent = oc[name], cc[name]
        fields, body = agent["fields"], agent["body"]
        failures += not check(
            "%s: frontmatter name matches filename" % name,
            fields.get("name") == name, "name=%r" % fields.get("name"))
        failures += not check(
            "%s: description present on both hosts" % name,
            bool(fields.get("description")) and bool(spec.get("description")))
        failures += not check(
            "%s: model pinned for claude code" % name, bool(fields.get("model")),
            "set `model:` in .claude/agents/%s.md (the cheap tier)" % name)
        failures += not check(
            "%s: prompt identical on both hosts" % name,
            normalize(spec.get("prompt", "")) == normalize(body),
            "opencode.json prompt and .claude/agents/%s.md body differ" % name)
        tools = claude_tools(fields)
        failures += not check(
            "%s: claude tools listed explicitly" % name, bool(tools))
        if permission_state(spec, "edit") == "deny":
            failures += not check(
                "%s: edit denied on both hosts" % name, not (tools & EDIT_TOOLS),
                "claude tools carry %s" % sorted(tools & EDIT_TOOLS))
        if permission_state(spec, "bash") == "deny":
            failures += not check(
                "%s: bash denied on both hosts" % name, not (tools & BASH_TOOLS),
                "claude tools carry %s" % sorted(tools & BASH_TOOLS))
        if permission_state(spec, "task") == "deny":
            failures += not check(
                "%s: spawning denied on both hosts" % name, not (tools & SPAWN_TOOLS),
                "claude tools carry %s" % sorted(tools & SPAWN_TOOLS))

    referenced = named_in_skill()
    failures += not check("skill text names at least one subagent", bool(referenced))
    missing = sorted(referenced - (set(oc) & set(cc)))
    failures += not check(
        "every subagent the skill names is defined on both hosts", not missing,
        "undefined: %s" % missing)

    agents = len(set(oc) | set(cc))
    if failures:
        print("FAIL: verify_agents agents=%d failed=%d" % (agents, failures))
        return 1
    print("PASS: verify_agents agents=%d failed=0" % agents)
    return 0


if __name__ == "__main__":
    sys.exit(main())
