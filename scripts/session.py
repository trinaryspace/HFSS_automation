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

The budget is judged against the actual tool-call count in the step trace
(`results/state/trace/*.steps.jsonl`, run logging ticket 04) when one has been
extracted, and reported as `calls unaccounted (no trace)` otherwise — never as
a count nobody measured.

Once declared, the repo's own entry points refuse out-of-phase work: a clarify
session cannot `compile_spec --launch`, and only a solve session may solve.

Every declaration is also recorded: one line appended to
`results/state/sessions.jsonl` (the run's session history, never rewritten)
and, on the first declaration, `results/state/run.json` naming the run. That
is how `scripts/run_card.py --workspace` finds all three phase sessions
afterwards. `--task-doc` records the request document the run answers.
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
    detect_host, history, run_info, start, trace_calls,
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
    parser.add_argument("--task-doc", default="",
                        help="the request document this run answers; recorded "
                             "in run.json on the first declaration only")
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
                        host_session_id=host_id, task_doc=args.task_doc)
        run = run_info(state_dir) or {}
        print(f"PASS: session declared phase={session.phase} "
              f"name={session.name or '-'} budget={session.call_budget} "
              f"host={session.host or '-'} "
              f"session_id={session.host_session_id or '-'} "
              f"run={run.get('run_id') or '-'} "
              f"declared={len(history(state_dir))}")
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

    run = run_info(state_dir) or {}
    traced = trace_calls(state_dir)
    if traced is not None:
        calls_line = f"{traced}/{session.call_budget} (trace)"
    elif session.calls:
        calls_line = f"{session.calls}/{session.call_budget} (note_call)"
    else:
        calls_line = f"unaccounted (no trace); budget {session.call_budget}"
    print(f"  run     {run.get('run_id') or '-'}")
    print(f"  phase   {session.phase}")
    print(f"  name    {session.name or '-'}")
    print(f"  calls   {calls_line}")
    for record in history(state_dir):
        print(f"  history {record['ts']} {record['phase']:<8} "
              f"{record.get('host') or '-'} {record.get('host_session_id') or '-'}")
    verdict = session.budget_verdict(trace_calls=traced)
    print(verdict if verdict.startswith("ESCALATE") else f"PASS: {verdict}")
    over = session.exceeds(traced) if traced is not None else session.over_budget
    return 2 if over else 0


if __name__ == "__main__":
    raise SystemExit(main())
