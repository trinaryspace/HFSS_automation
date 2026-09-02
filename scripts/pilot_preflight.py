"""Pilot hygiene pre-flight: prove a cell is uncontaminated before it runs.

`swift-otter` (2026-08-16) measured nothing because a spec that "was supposed to
be moved aside and was not" stayed in place, and because a sibling workspace full
of working staged scripts sat where the agent could copy it. Nine of its twelve
staged scripts came out byte-identical to the previous run's. Neither fact was
checked before launch and both were only discovered afterwards, by which point
the tokens were spent.

This is that check. It asserts nothing about the tool — only about the *cell*:
that the workspace is empty, that the specs on disk are the ones you intended,
and that the skill every worktree shares is the one you froze. It runs offline in
about a second, needs no license and no desktop, and prints a block meant to be
pasted verbatim into the cell record. If it did not print, it did not happen.

Deliberately NOT `tier0.py`: that suite fails in a fresh worktree by design (its
snapshot corpus lives under `workspaces/*/results/`, which is gitignored) and
takes ~290 s. Run tier0 once per campaign branch in the main checkout; run this
once per cell.

Usage:
    python scripts/pilot_preflight.py --cell S1
    python scripts/pilot_preflight.py --cell X0a --expect-missing patch-2400
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CASES = REPO / "knowledge" / "cases"
WORKSPACES = REPO / "workspaces"
SKILL = REPO / "skill" / "hfss-agent"
OPENCODE_SKILL = Path.home() / ".agents" / "skills" / "hfss-agent"
CLAUDE_SKILL = REPO / ".claude" / "skills" / "hfss-agent"


def git(*argv):
    """Run a git command in the repo; return stripped stdout, or None."""
    try:
        out = subprocess.run(["git", "-C", str(REPO), *argv],
                             capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def resolve_link(path):
    """Where a junction/symlink actually points, or None when it is not one."""
    if not path.exists():
        return "absent"
    try:
        target = os.path.normcase(os.path.realpath(path))
    except OSError:
        return "unresolvable"
    # Compare against the UNresolved absolute path: `path.resolve()` follows
    # the link too, so comparing the two resolved forms always said "not a
    # link", for junctions and symlinks alike.
    if target == os.path.normcase(os.path.abspath(str(path))):
        return "not a link"
    return os.path.realpath(path)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--cell", required=True, help="cell id, e.g. S1 or X0a")
    parser.add_argument("--expect-missing", action="append", default=[],
                        metavar="CASE",
                        help="a case whose design.yaml this cell moved aside; "
                             "its presence is a FAIL, its absence is expected")
    parser.add_argument("--allow-workspaces", action="store_true",
                        help="permit a non-empty workspaces/ (D1-B only, where "
                             "a copyable predecessor is the experiment)")
    args = parser.parse_args(argv)

    failures = []
    print(f"preflight cell={args.cell}")

    # 1. Which tree is this, exactly.
    head = git("rev-parse", "HEAD")
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    print(f"  cwd           {REPO}")
    print(f"  branch        {branch or 'UNKNOWN'}")
    print(f"  head          {head or 'UNKNOWN'}")
    if head is None:
        failures.append("not a git checkout (or git unavailable)")

    # 2. No predecessor workspace to copy. This is the swift-otter check.
    present = sorted(p.name for p in WORKSPACES.iterdir()
                     if p.is_dir()) if WORKSPACES.is_dir() else []
    print(f"  workspaces    {len(present)}"
          + (f" - {', '.join(present)}" if present else " (empty)"))
    if present and not args.allow_workspaces:
        failures.append(
            f"workspaces/ is not empty ({', '.join(present)}) - the agent can "
            "copy these. A fresh worktree ships 152 tracked files here, "
            "patch-2400/src included, so this fails BY DEFAULT: clean-room the "
            "cell with `git rm -r -q workspaces` first, or pass "
            "--allow-workspaces if a copyable predecessor is the experiment")

    # 3. Exactly which specs are on disk.
    with_spec, without_spec = [], []
    if CASES.is_dir():
        for directory in sorted(p for p in CASES.iterdir()
                                if p.is_dir() and not p.name.startswith("_")):
            (with_spec if (directory / "design.yaml").exists()
             else without_spec).append(directory.name)
    else:
        failures.append("knowledge/cases is missing")
    print(f"  specs present {len(with_spec)}"
          + (f" - {', '.join(with_spec)}" if with_spec else ""))
    if without_spec:
        print(f"  specs absent  {', '.join(without_spec)}")
    # A case's design.yaml is NOT the only copy of its answer. case.json carries
    # key_dimensions (patch_width_mm, ereff, fringing dL, patch_length_mm) and
    # notes.md carries the Balanis derivation. Cell X0a proved this the
    # expensive way: with only design.yaml removed, the agent read notes.md and
    # case.json, and its "closed form agrees to -0.00%" was four numbers read
    # off the answer key rather than derived. A blind authoring cell needs the
    # WHOLE case directory gone.
    for case in args.expect_missing:
        directory = CASES / case
        if directory.exists():
            leftovers = ", ".join(sorted(p.name for p in directory.iterdir()))
            failures.append(
                f"'{case}' case directory still exists ({leftovers}) - this cell "
                "expects it gone. Removing design.yaml alone is not enough: "
                "case.json holds key_dimensions and notes.md holds the "
                "derivation, so the agent reads the answer instead of deriving "
                "it (measured on cell X0a)")

    # 4. The skill is shared across every worktree; record which one.
    skill_commit = git("log", "-1", "--format=%h %s", "--", "skill/hfss-agent")
    print(f"  skill commit  {skill_commit or 'UNKNOWN'}")
    print(f"  opencode link {resolve_link(OPENCODE_SKILL)}")
    print(f"  claude link   {resolve_link(CLAUDE_SKILL)}")
    if not SKILL.is_dir():
        failures.append("skill/hfss-agent is missing from this worktree")

    # 5. The canonical specs still load. Milliseconds, and it catches a
    #    half-finished spec move.
    try:
        out = subprocess.run([sys.executable,
                              str(REPO / "scripts" / "validate_cases.py")],
                             capture_output=True, text=True, timeout=120)
        line = next((ln for ln in reversed(out.stdout.splitlines())
                     if ln.startswith(("PASS:", "FAIL:"))), "no summary line")
        print(f"  validate_cases {line}")
        if out.returncode != 0:
            failures.append(f"validate_cases failed: {line}")
    except (OSError, subprocess.SubprocessError) as exc:
        failures.append(f"validate_cases did not run: {exc}")

    if failures:
        for reason in failures:
            print(f"  ! {reason}")
        print(f"FAIL: preflight cell={args.cell} problems={len(failures)}")
        return 1
    print(f"PASS: preflight cell={args.cell} workspaces={len(present)} "
          f"specs={len(with_spec)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
