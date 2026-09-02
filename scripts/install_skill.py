"""Install the hfss-agent skill for every harness on this box, as links not copies.

The skill lives at `skill/hfss-agent/` and must stay ONE artifact. This repo
has already paid three times for duplicated sources drifting apart: ticket
01's two profile parsers, SKILL.md drifting from the amended ADR 0006 for a
week, and — found while arming ticket 06 — the opencode skill copy under
`~/.agents/skills/hfss-agent` sitting four files and eight edits behind the
repo, still carrying both P0 bugs. A run launched against that copy would
have measured the pre-ticket-01 tooling. So every install is a link — a
directory junction on Windows, a symlink elsewhere — and never a copy.

Three targets, because the two harnesses read from different roots and one
of them needs a second skill:

- **Claude Code** loads project skills from `.claude/skills/<name>/SKILL.md`,
  inside the repo. Always installed; the link is gitignored, and a clone
  re-creates it by running this script.
- **opencode** loads them from the user-level `~/.agents/skills/<name>/`.
  Installed only when that root already exists, so a clone on a box that
  does not use opencode neither creates it nor fails its check.
- **analyze-papers for Claude Code** — the skill the Clarification step runs
  on user PDFs is a global skill that lives in opencode's root
  (`~/.agents/skills/analyze-papers`). Claude Code reads personal skills from
  `~/.claude/skills/`, so that root gets a link to the opencode copy —
  again a link, so the two hosts can never see different versions.
  Installed only when the opencode copy exists.

Run it from the MAIN checkout. From a git worktree (`.claude/worktrees/<name>`)
the in-repo Claude Code link is still made — each worktree needs its own — but
the user-level opencode link is only inspected, never re-pointed: it is shared
by every checkout and a worktree is deleted when its session ends.

A fourth thing is not a link: the Claude Code tool hooks (run logging,
ticket 08). `.claude/settings.json` gets a `PreToolUse`, a `PostToolUse` and
a `PostToolUseFailure` entry running `scripts/hook_log.py`, which appends
one line per tool call to the active workspace's `results/state/tools.jsonl`.
They are MERGED into the file — the `permissions` block and any hook that is
not ours are kept byte-for-byte in meaning — and removed the same way.
The file is tracked, so a clone carries them; the install is idempotent and
`--check` reports whether all three are present.

Usage:
    python scripts/install_skill.py            # install links + hooks (idempotent)
    python scripts/install_skill.py --check    # report status, change nothing
    python scripts/install_skill.py --remove   # links and hooks
    python scripts/install_skill.py --hooks          # hooks only
    python scripts/install_skill.py --remove-hooks   # hooks only
"""

import argparse
import json
import os
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(REPO, "skill", "hfss-agent")
AGENTS_SKILLS = os.path.join(os.path.expanduser("~"), ".agents", "skills")
CLAUDE_SKILLS = os.path.join(os.path.expanduser("~"), ".claude", "skills")
ANALYZE_PAPERS = os.path.join(AGENTS_SKILLS, "analyze-papers")

SKIPPED = "skipped"

# -- the tool hooks (ticket 08) ----------------------------------------------

SETTINGS = os.path.join(REPO, ".claude", "settings.json")
HOOK_SCRIPT = "scripts/hook_log.py"
HOOK_EVENTS = ("PreToolUse", "PostToolUse", "PostToolUseFailure")
HOOK_MATCHER = "*"                       # every tool; "" / omitted / "*" all mean that
HOOK_TIMEOUT_S = 5                       # the hook's own budget is ~50 ms
# Runs under the shell Claude Code gives hooks (Git Bash on Windows when it
# is installed, which the sandboxed Bash tool needs anyway). `-I -S` keeps
# the interpreter start-up under the budget; `${CLAUDE_PROJECT_DIR}` is the
# checkout the session started in, so the command does not depend on the
# session's cwd; `|| exit 0` means a missing python or script can never
# return 2, the one exit code that would block the tool call.
HOOK_COMMAND = 'python -I -S "${CLAUDE_PROJECT_DIR}/%s" || exit 0' % HOOK_SCRIPT


def hook_entry():
    return {"matcher": HOOK_MATCHER,
            "hooks": [{"type": "command", "command": HOOK_COMMAND,
                       "timeout": HOOK_TIMEOUT_S}]}


def _is_ours(hook):
    return isinstance(hook, dict) and HOOK_SCRIPT in str(hook.get("command", ""))


def read_settings(path=SETTINGS):
    """(settings dict, error) — ({}, None) for a missing file."""
    if not os.path.exists(path):
        return {}, None
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError) as exc:
        return None, "cannot read %s: %s" % (_short(path), exc)
    if not isinstance(data, dict):
        return None, "%s is not a JSON object" % _short(path)
    return data, None


def write_settings(data, path=SETTINGS):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def hooks_present(settings):
    """The events that carry our hook, and the ones that do not."""
    hooks = settings.get("hooks") if isinstance(settings, dict) else None
    hooks = hooks if isinstance(hooks, dict) else {}
    present, missing = [], []
    for event in HOOK_EVENTS:
        entries = hooks.get(event)
        found = any(isinstance(e, dict) and any(_is_ours(h) for h in (e.get("hooks") or []))
                    for e in (entries if isinstance(entries, list) else []))
        (present if found else missing).append(event)
    return present, missing


def merge_hooks(settings):
    """Return a copy of the settings with our three hooks present, adding
    only what is missing; every other key and hook is left as it was."""
    out = dict(settings)
    hooks = dict(out.get("hooks") or {}) if isinstance(out.get("hooks"), dict) else {}
    for event in HOOK_EVENTS:
        entries = list(hooks.get(event) or []) if isinstance(hooks.get(event), list) else []
        if not any(isinstance(e, dict) and any(_is_ours(h) for h in (e.get("hooks") or []))
                   for e in entries):
            entries.append(hook_entry())
        hooks[event] = entries
    out["hooks"] = hooks
    return out


def strip_hooks(settings):
    """Return a copy with our hooks removed; an event or the `hooks` block
    left empty by that is dropped, anything else is kept."""
    out = dict(settings)
    hooks = out.get("hooks")
    if not isinstance(hooks, dict):
        return out
    kept = {}
    for event, entries in hooks.items():
        if not isinstance(entries, list):
            kept[event] = entries
            continue
        new_entries = []
        for entry in entries:
            if not isinstance(entry, dict):
                new_entries.append(entry)
                continue
            remaining = [h for h in (entry.get("hooks") or []) if not _is_ours(h)]
            if remaining or not entry.get("hooks"):
                new_entries.append(dict(entry, hooks=remaining) if entry.get("hooks") else entry)
        if new_entries:
            kept[event] = new_entries
    if kept:
        out["hooks"] = kept
    else:
        out.pop("hooks", None)
    return out


def hooks_status(path=SETTINGS):
    """(state, detail) like `status()`: True when all three are present."""
    settings, error = read_settings(path)
    if error:
        return False, error
    present, missing = hooks_present(settings)
    if not missing:
        return True, "%s -> %s in %s" % ("/".join(present), HOOK_SCRIPT, _short(path))
    return False, "missing %s in %s (run install_skill.py)" % ("/".join(missing), _short(path))


def install_hooks(path=SETTINGS):
    """Merge the hooks in; returns (ok, detail)."""
    settings, error = read_settings(path)
    if error:
        return False, error
    if not hooks_present(settings)[1]:
        return True, "already installed"
    write_settings(merge_hooks(settings), path)
    state, detail = hooks_status(path)
    return state, detail


def remove_hooks(path=SETTINGS):
    """Strip the hooks; returns (removed, detail)."""
    settings, error = read_settings(path)
    if error:
        return False, error
    if not hooks_present(settings)[0]:
        return False, "no hooks to remove"
    write_settings(strip_hooks(settings), path)
    return True, "removed %s from %s" % (HOOK_SCRIPT, _short(path))


class Target:
    """One link to maintain: `link` -> `source`.

    `skip_unless` is a path that must exist for the target to apply on this
    box; when it is absent the target is reported as skipped, never failed,
    so a clone on a box without opencode passes tier 0 unchanged.
    """

    def __init__(self, name, source, link, skip_unless=None):
        self.name = name
        self.source = source
        self.link = link
        self.skip_unless = skip_unless

    def skip_reason(self):
        if self.skip_unless is not None and not os.path.isdir(self.skip_unless):
            return "no %s on this box" % _short(self.skip_unless)
        return None

    @property
    def user_level_repo_link(self):
        """A link outside the repo that points into it — the opencode target.

        Such a link is shared by every checkout on the box, so it must point
        at the MAIN checkout. Run from a worktree (`.claude/worktrees/<name>`,
        deleted when its session ends) this script must leave it alone: it
        once re-pointed `~/.agents/skills/hfss-agent` at a worktree, and the
        next opencode session would have read a skill directory that no
        longer existed.
        """
        return (_under(self.source, REPO) and not _under(self.link, REPO))


TARGETS = [
    Target("claude-code", SOURCE, os.path.join(REPO, ".claude", "skills", "hfss-agent")),
    Target("opencode", SOURCE, os.path.join(AGENTS_SKILLS, "hfss-agent"),
           skip_unless=AGENTS_SKILLS),
    Target("analyze-papers", ANALYZE_PAPERS, os.path.join(CLAUDE_SKILLS, "analyze-papers"),
           skip_unless=ANALYZE_PAPERS),
]


def resolved(path):
    try:
        return os.path.realpath(path)
    except OSError:
        return None


def _under(path, root):
    path, root = os.path.normcase(os.path.abspath(path)), os.path.normcase(os.path.abspath(root))
    return path == root or path.startswith(root + os.sep)


_IN_WORKTREE = None


def in_worktree():
    """True when this checkout is a linked git worktree, not the main one."""
    global _IN_WORKTREE
    if _IN_WORKTREE is None:
        _IN_WORKTREE = _detect_worktree()
    return _IN_WORKTREE


def _detect_worktree():
    try:
        result = subprocess.run(
            ["git", "-C", REPO, "rev-parse", "--git-dir", "--git-common-dir"],
            capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        result = None
    if result is not None and result.returncode == 0:
        dirs = result.stdout.split()
        if len(dirs) == 2:
            git_dir, common = (os.path.realpath(os.path.join(REPO, d)) for d in dirs)
            return os.path.normcase(git_dir) != os.path.normcase(common)
    # No git: fall back to where Claude Code puts its worktrees.
    return (os.sep + ".claude" + os.sep + "worktrees" + os.sep) in REPO + os.sep


def _is_junction(path):
    if os.name != "nt":
        return False
    try:
        return bool(os.readlink(path))
    except OSError:
        return False


def status(target):
    """(state, detail) — state is True, False, or SKIPPED.

    SKIPPED means an optional target whose prerequisite does not exist on
    this box; it is not a failure and never blocks the tier-0 gate.
    """
    reason = target.skip_reason()
    if reason is not None:
        return SKIPPED, reason
    link, source = target.link, target.source
    if target.user_level_repo_link and in_worktree():
        # Managed from the main checkout only (see Target.user_level_repo_link).
        if not os.path.exists(link):
            return SKIPPED, ("not installed; run install_skill.py from the main "
                             "checkout, never from a worktree")
        if not (os.path.islink(link) or _is_junction(link)):
            return False, ("it is a COPY, not a link — delete it and re-run from "
                           "the main checkout")
        if not os.path.isfile(os.path.join(link, "SKILL.md")):
            return False, "link resolves but has no SKILL.md"
        return True, ("linked -> %s (left alone: this is a worktree; the link "
                      "belongs to the main checkout)" % resolved(link))
    if not os.path.exists(link):
        return False, "not installed"
    resolved_link = resolved(link)
    if resolved_link != resolved(source):
        return False, "points at %s, expected %s" % (resolved_link, resolved(source))
    if not os.path.isfile(os.path.join(link, "SKILL.md")):
        return False, "link resolves but has no SKILL.md"
    if not os.path.islink(link) and not _is_junction(link):
        return False, ("it is a COPY, not a link — delete it and re-run, or "
                       "it will drift from %s" % _short(source))
    return True, "linked -> %s" % _short(source)


def _short(path):
    """Repo-relative where possible, ~-relative otherwise, forward slashes."""
    home = os.path.expanduser("~")
    for root, prefix in ((REPO, ""), (home, "~/")):
        try:
            rel = os.path.relpath(path, root)
        except ValueError:
            continue
        if not rel.startswith(".."):
            return prefix + rel.replace(os.sep, "/")
    return path.replace(os.sep, "/")


def link_one(link, source):
    """Create the link, replacing whatever is there. Returns (ok, detail)."""
    if os.path.exists(link):
        remove_link(link)
    os.makedirs(os.path.dirname(link), exist_ok=True)
    if os.name == "nt":
        # Directory junction: works without administrator rights, unlike a
        # true symlink on Windows.
        result = subprocess.run(["cmd", "/c", "mklink", "/J", link, source],
                                capture_output=True, text=True)
        if result.returncode != 0:
            return False, "mklink failed: %s" % (result.stderr or result.stdout).strip()
    else:
        os.symlink(source, link, target_is_directory=True)
    return True, None


def remove_link(path):
    if os.path.islink(path) or _is_junction(path):
        try:
            os.rmdir(path)          # junctions and dir symlinks unlink this way
            return
        except OSError:
            pass
    shutil.rmtree(path, ignore_errors=True)


def install():
    if not os.path.isdir(SOURCE):
        print("FAIL: install_skill no skill at %s" % SOURCE)
        return 1
    failed = []
    for target in TARGETS:
        state, detail = status(target)
        if state is SKIPPED:
            print("  %-14s %s: %s" % (target.name, SKIPPED, detail))
            continue
        if state:
            print("  %-14s already installed: %s" % (target.name, detail))
            continue
        print("  %-14s installing over %s (%s)" % (target.name, _short(target.link), detail))
        ok, why = link_one(target.link, target.source)
        if not ok:
            print("  %-14s FAILED: %s" % (target.name, why))
            failed.append(target.name)
            continue
        state, detail = status(target)
        print("  %-14s %s" % (target.name, detail if state else "FAILED: " + detail))
        if not state:
            failed.append(target.name)
    ok, detail = install_hooks()
    print("  %-14s %s" % ("hooks", detail if ok else "FAILED: " + detail))
    if not ok:
        failed.append("hooks")
    return _summary(failed)


def check():
    failed = []
    for target in TARGETS:
        state, detail = status(target)
        label = SKIPPED if state is SKIPPED else ("ok" if state else "FAILED")
        print("  %-14s %-8s %s" % (target.name, label, detail))
        if state is not SKIPPED and not state:
            failed.append(target.name)
    state, detail = hooks_status()
    print("  %-14s %-8s %s" % ("hooks", "ok" if state else "FAILED", detail))
    if not state:
        failed.append("hooks")
    return _summary(failed)


def _summary(failed):
    live = [target.name for target in TARGETS if status(target)[0] is not SKIPPED]
    hooks = len(hooks_present(read_settings()[0] or {})[0])
    if failed:
        print("FAIL: install_skill targets=%d hooks=%d/%d failed=%d (%s)"
              % (len(live), hooks, len(HOOK_EVENTS), len(failed), ",".join(failed)))
        return 1
    print("PASS: install_skill targets=%d hooks=%d/%d failed=0"
          % (len(live), hooks, len(HOOK_EVENTS)))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--remove", action="store_true",
                        help="remove the links and the hooks")
    parser.add_argument("--hooks", action="store_true",
                        help="install only the tool hooks into .claude/settings.json")
    parser.add_argument("--remove-hooks", action="store_true",
                        help="remove only the tool hooks from .claude/settings.json")
    args = parser.parse_args(argv)

    if args.hooks:
        ok, detail = install_hooks()
        print("  %-14s %s" % ("hooks", detail if ok else "FAILED: " + detail))
        return 0 if ok else 1
    if args.remove_hooks:
        removed, detail = remove_hooks()
        print(detail)
        return 0
    if args.remove:
        removed = 0
        for target in TARGETS:
            if target.user_level_repo_link and in_worktree():
                print("left %s alone (%s): remove it from the main checkout"
                      % (_short(target.link), target.name))
                continue
            if os.path.exists(target.link):
                remove_link(target.link)
                print("removed %s (%s)" % (_short(target.link), target.name))
                removed += 1
        gone, detail = remove_hooks()
        if gone:
            print(detail)
            removed += 1
        if not removed:
            print("nothing to remove")
        return 0
    if args.check:
        return check()
    return install()


if __name__ == "__main__":
    raise SystemExit(main())
