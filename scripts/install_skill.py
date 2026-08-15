"""Install the hfss-agent skill for every harness on this box, as links not copies.

The skill lives at `skill/hfss-agent/` and must stay ONE artifact. This repo
has already paid three times for duplicated sources drifting apart: ticket
01's two profile parsers, SKILL.md drifting from the amended ADR 0006 for a
week, and — found while arming ticket 06 — the opencode skill copy under
`~/.agents/skills/hfss-agent` sitting four files and eight edits behind the
repo, still carrying both P0 bugs. A run launched against that copy would
have measured the pre-ticket-01 tooling. So every install is a link — a
directory junction on Windows, a symlink elsewhere — and never a copy.

Two targets, because the two harnesses read from different roots:

- **Claude Code** loads project skills from `.claude/skills/<name>/SKILL.md`,
  inside the repo. Always installed; the link is gitignored, and a clone
  re-creates it by running this script.
- **opencode** loads them from the user-level `~/.agents/skills/<name>/`.
  Installed only when that root already exists, so a clone on a box that
  does not use opencode neither creates it nor fails its check.

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

# (name, link path, required) — an optional target whose parent root is
# absent is reported as skipped rather than failed.
TARGETS = [
    ("claude-code", os.path.join(REPO, ".claude", "skills", "hfss-agent"), True),
    ("opencode", os.path.join(AGENTS_SKILLS, "hfss-agent"), False),
]

SKIPPED = "skipped"


def resolved(path):
    try:
        return os.path.realpath(path)
    except OSError:
        return None


def _is_junction(path):
    if os.name != "nt":
        return False
    try:
        return bool(os.readlink(path))
    except OSError:
        return False


def status(link, required):
    """(state, detail) — state is True, False, or SKIPPED.

    SKIPPED means an optional target whose skills root does not exist on
    this box; it is not a failure and never blocks the tier-0 gate.
    """
    if not required and not os.path.isdir(os.path.dirname(link)):
        return SKIPPED, "no %s on this box" % _short(os.path.dirname(link))
    if not os.path.exists(link):
        return False, "not installed"
    target = resolved(link)
    if target != resolved(SOURCE):
        return False, "points at %s, expected %s" % (target, resolved(SOURCE))
    if not os.path.isfile(os.path.join(link, "SKILL.md")):
        return False, "link resolves but has no SKILL.md"
    if not os.path.islink(link) and not _is_junction(link):
        return False, ("it is a COPY, not a link — delete it and re-run, or "
                       "it will drift from skill/hfss-agent")
    return True, "linked -> skill/hfss-agent"


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


def link_one(link):
    """Create the link, replacing whatever is there. Returns (ok, detail)."""
    if os.path.exists(link):
        remove_link(link)
    os.makedirs(os.path.dirname(link), exist_ok=True)
    if os.name == "nt":
        # Directory junction: works without administrator rights, unlike a
        # true symlink on Windows.
        result = subprocess.run(["cmd", "/c", "mklink", "/J", link, SOURCE],
                                capture_output=True, text=True)
        if result.returncode != 0:
            return False, "mklink failed: %s" % (result.stderr or result.stdout).strip()
    else:
        os.symlink(SOURCE, link, target_is_directory=True)
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
    for name, link, required in TARGETS:
        state, detail = status(link, required)
        if state is SKIPPED:
            print("  %-12s %s: %s" % (name, SKIPPED, detail))
            continue
        if state:
            print("  %-12s already installed: %s" % (name, detail))
            continue
        print("  %-12s installing over %s (%s)" % (name, _short(link), detail))
        ok, why = link_one(link)
        if not ok:
            print("  %-12s FAILED: %s" % (name, why))
            failed.append(name)
            continue
        state, detail = status(link, required)
        print("  %-12s %s" % (name, detail if state else "FAILED: " + detail))
        if not state:
            failed.append(name)
    return _summary(failed)


def check():
    failed = []
    for name, link, required in TARGETS:
        state, detail = status(link, required)
        label = SKIPPED if state is SKIPPED else ("ok" if state else "FAILED")
        print("  %-12s %-8s %s" % (name, label, detail))
        if state is not SKIPPED and not state:
            failed.append(name)
    return _summary(failed)


def _summary(failed):
    live = [name for name, link, required in TARGETS
            if status(link, required)[0] is not SKIPPED]
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
        for name, link, _required in TARGETS:
            if os.path.exists(link):
                remove_link(link)
                print("removed %s (%s)" % (_short(link), name))
                removed += 1
        if not removed:
            print("nothing to remove")
        return 0
    if args.check:
        return check()
    return install()


if __name__ == "__main__":
    raise SystemExit(main())
