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

Usage:
    python scripts/install_skill.py            # install (idempotent)
    python scripts/install_skill.py --check    # report status, change nothing
    python scripts/install_skill.py --remove
"""

import argparse
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
    return _summary(failed)


def check():
    failed = []
    for target in TARGETS:
        state, detail = status(target)
        label = SKIPPED if state is SKIPPED else ("ok" if state else "FAILED")
        print("  %-14s %-8s %s" % (target.name, label, detail))
        if state is not SKIPPED and not state:
            failed.append(target.name)
    return _summary(failed)


def _summary(failed):
    live = [target.name for target in TARGETS if status(target)[0] is not SKIPPED]
    if failed:
        print("FAIL: install_skill targets=%d failed=%d (%s)"
              % (len(live), len(failed), ",".join(failed)))
        return 1
    print("PASS: install_skill targets=%d failed=0" % len(live))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--remove", action="store_true")
    args = parser.parse_args(argv)

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
        if not removed:
            print("nothing to remove")
        return 0
    if args.check:
        return check()
    return install()


if __name__ == "__main__":
    raise SystemExit(main())
