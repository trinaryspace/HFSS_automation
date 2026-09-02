"""Declare or inspect a phase session (ticket 14 boundary).

A phase session that has not declared itself is unguarded — `hfss_spec.session`
permits everything, deliberately, so the boundary could land without breaking
workspaces that predate it. Declaring is therefore the step that turns the
boundary on, and it is one command at the top of each session:

    python scripts/session.py --workspace workspaces/<name> --phase clarify
    python scripts/session.py --workspace workspaces/<name> --phase build
    python scripts/session.py --workspace workspaces/<name> --phase solve

With no `--phase` it reports the current session and its budget, which is what a
resuming session or a human wants:

    python scripts/session.py --workspace workspaces/<name>

Once declared, the repo's own entry points refuse out-of-phase work: a clarify
session cannot `compile_spec --launch`, and only a solve session may solve.
"""

import argparse
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec.session import (                        # noqa: E402
    DEFAULT_CALL_BUDGET, HOST_CLAUDE_CODE, HOST_OPENCODE, PHASES, Session,
    detect_host, start,
)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspace", required=True,
                        help="workspace dir; state lands in results/state/")
    parser.add_argument("--phase", choices=PHASES,
                        help="declare this phase; omit to report the current one")
    parser.add_argument("--name", default="",
                        help="run name, for the record")
    parser.add_argument("--budget", type=int, default=DEFAULT_CALL_BUDGET,
                        help=f"call budget before escalating (default {DEFAULT_CALL_BUDGET}; 0 disables)")
    parser.add_argument("--note-calls", type=int, default=0, metavar="N",
                        help="add N to the call count and re-report the verdict")
    parser.add_argument("--host", choices=(HOST_CLAUDE_CODE, HOST_OPENCODE),
                        help="harness this session runs under (default: detected "
                             "from the environment; Claude Code exports its id)")
    parser.add_argument("--session-id",
                        help="the harness's own id or slug for this session, so "
                             "scripts/run_card.py can find it later")
    args = parser.parse_args(argv)

    state_dir = Path(args.workspace) / "results" / "state"

    if args.phase:
        host, host_id = detect_host()
        if args.host:
            host = args.host
        if args.session_id:
            host_id = args.session_id
        session = start(args.phase, name=args.name, state_dir=state_dir,
                        call_budget=args.budget, host=host,
                        host_session_id=host_id)
        print(f"PASS: session declared phase={session.phase} "
              f"name={session.name or '-'} budget={session.call_budget} "
              f"host={session.host or '-'} "
              f"session_id={session.host_session_id or '-'}")
        return 0

    session = Session.load(state_dir)
    if session is None:
        print(f"FAIL: session none declared in {state_dir} — "
              f"this workspace is UNGUARDED; declare a phase to enforce the "
              f"boundary")
        return 1

    if args.note_calls:
        session.note_call(args.note_calls)
        session.save(state_dir)

    print(f"  phase   {session.phase}")
    print(f"  name    {session.name or '-'}")
    print(f"  calls   {session.calls}/{session.call_budget}")
    verdict = session.budget_verdict()
    print(verdict if verdict.startswith("ESCALATE") else f"PASS: {verdict}")
    return 2 if session.over_budget else 0


if __name__ == "__main__":
    raise SystemExit(main())
