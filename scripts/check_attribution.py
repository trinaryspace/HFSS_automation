"""Does opencode register a `project` row per worktree? (campaign task W0-5)

`run_card.py` scopes sessions to the HFSS project by matching PROJECT_MARKER
against `project.worktree`. Whether a parallel campaign can attribute tokens at
all depends on a fact nobody has needed until now: when opencode starts in a git
worktree, does it create a *new* project row for that directory, or resolve to
the main checkout?

Measured 2026-08-16, before any worktree session existed: exactly one row
(`C:/Users/afpim/Repos/HFSS_automation`, 52 sessions). `load_card` has since been
changed from `= (SELECT id ...)` to `IN (SELECT id ...)`, so several matching
rows no longer collapse to one arbitrary row and the answer is no longer
load-bearing. It still decides whether cells should be carded with `--worktree`.

Run this after starting one throwaway opencode session from a worktree.

Usage:
    python scripts/check_attribution.py
    python scripts/check_attribution.py --slug <probe-session-slug>
"""

import argparse
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_card import DEFAULT_DB, ENV_DB, PROJECT_MARKER, connect  # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--db", help="path to opencode.db")
    parser.add_argument("--slug", help="probe session slug, to prove it is reachable")
    args = parser.parse_args(argv)

    import os
    db_path = args.db or os.environ.get(ENV_DB) or DEFAULT_DB
    if not Path(db_path).is_file():
        print(f"FAIL: check_attribution database not found: {db_path}")
        return 1
    con = connect(db_path)
    try:
        rows = con.execute(
            "SELECT id, worktree FROM project WHERE worktree LIKE '%' || ? || '%'"
            " ORDER BY worktree", (PROJECT_MARKER,)).fetchall()
        print(f"project rows matching {PROJECT_MARKER!r}: {len(rows)}")
        for pid, worktree in rows:
            count = con.execute("SELECT COUNT(*) FROM session WHERE project_id=?",
                                (pid,)).fetchone()[0]
            print(f"  {count:5d} sessions  {worktree}")

        if args.slug:
            found = con.execute(
                "SELECT p.worktree FROM session s JOIN project p"
                " ON p.id = s.project_id WHERE s.slug = ?"
                " ORDER BY s.time_created DESC LIMIT 1", (args.slug,)).fetchone()
            print(f"  slug {args.slug!r} lives in: "
                  f"{found[0] if found else 'NOT FOUND ANYWHERE'}")
    finally:
        con.close()

    if len(rows) <= 1:
        print("verdict: one project row - opencode resolves worktrees to the "
              "main project. `--slug` alone is sufficient.")
    else:
        print("verdict: several project rows - opencode registers one per "
              "worktree. Pass `--worktree <cell path>` when carding a cell, and "
              "note that the pre-patch scalar subquery would have hidden "
              f"{len(rows) - 1} of these {len(rows)} projects entirely.")
    print(f"PASS: check_attribution project_rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
