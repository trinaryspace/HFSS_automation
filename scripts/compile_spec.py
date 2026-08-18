"""Compile a `design.yaml` onto the live AEDT desktop. Ticket 10, Tier 1.

Build only — this script never solves. Solve submission stays imperative under
the detached watchdog (ADR 0006), which is deliberate: the watchdog, the
banking rule and the Review gate are the parts of the old path that worked, and
phase 2 keeps them in full.

    python scripts/compile_spec.py --workspace workspaces/patch-2400 \
                                   --spec knowledge/cases/patch-2400/design.yaml

The validator is a hard gate inside `compiler.build`, so an incoherent spec
fails here in milliseconds without ever launching a desktop. Nothing about the
spec is re-derived at run time.

Output is one `PASS:` line per Spine stage plus a final summary line, and
pyAEDT's INFO chatter is suppressed — a full build should cost the caller ten
lines of context, not a thousand.
"""

import argparse
import importlib.util
import logging
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

# Before pyAEDT is imported anywhere: INFO logs are the single largest source
# of junk context in the old path (retrospective section D).
os.environ.setdefault("PYAEDT_LOG_LEVEL", "WARNING")
logging.getLogger("Global").setLevel(logging.WARNING)
logging.getLogger("pyaedt").setLevel(logging.WARNING)

from hfss_spec.compiler import BuildLog, CompileError, build      # noqa: E402
from hfss_spec.loader import SpecLoadError, load_spec             # noqa: E402
from hfss_spec.validate import SpecNotValidated                   # noqa: E402


def load_ws_common(workspace: Path):
    """The workspace's own attach-or-launch preamble, not a second copy of it."""
    path = workspace / "src" / "ws_common.py"
    if not path.exists():
        raise FileNotFoundError(f"no ws_common at {path}")
    spec = importlib.util.spec_from_file_location("_ws_common", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["_ws_common"] = module
    spec.loader.exec_module(module)
    return module


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--spec", required=True)
    parser.add_argument("--launch", action="store_true",
                        help="launch a desktop instead of attaching to one")
    parser.add_argument("--dry-run", action="store_true",
                        help="validate and report the plan; touch no desktop")
    args = parser.parse_args(argv)

    workspace = Path(args.workspace)
    try:
        spec = load_spec(args.spec)
    except SpecLoadError as exc:
        sys.stdout.write(exc.report.text())
        return 1

    if args.dry_run:
        from hfss_spec.compiler import STAGES
        from hfss_spec.validate import validate
        report = validate(spec)
        sys.stdout.write(report.text())
        if not report.ok:
            return 1
        print(f"  plan: {len(STAGES)} stages, {len(spec.geometry)} geometry ops, "
              f"{len(spec.excitations)} port(s), {len(spec.boundaries)} boundary(ies)")
        print(f"PASS: compile_spec dry-run spec={spec.name} "
              f"escape_hatch={spec.escape_hatch_count}")
        return 0

    # The phase boundary (ticket 14). Launching a desktop costs a licence seat
    # and compiling geometry mutates a live model; neither belongs to a
    # Clarification session. An undeclared session is unguarded - see
    # hfss_spec.session.require - so this changes nothing for existing
    # workspaces and refuses only where a phase has actually been declared.
    from hfss_spec.session import PhaseViolation, require as require_phase
    state_dir = workspace / "results" / "state"
    try:
        if args.launch:
            require_phase("launch_desktop", state_dir)
        require_phase("compile_model", state_dir)
    except PhaseViolation as exc:
        print(f"FAIL: compile_spec phase-boundary - {exc}")
        return 1

    ws = load_ws_common(workspace)
    hfss = ws.attach(launch=args.launch)
    log = BuildLog(emit=lambda line: print(line, flush=True))
    try:
        build(spec, hfss, log)
    except SpecNotValidated as exc:
        sys.stdout.write(str(exc))
        return _leave(ws, 1)
    except CompileError as exc:
        print(f"STAGE_FAILED: compile_spec {exc}")
        return _leave(ws, 1)

    print(f"PASS: compile_spec spec={spec.name} stages={len(log.results)}")
    return _leave(ws, 0)


def _leave(ws, code: int):
    """Leave the pinned desktop and its project alive, whatever happened.

    `ws.exit_keep_alive()` is `os._exit(0)` — it never returns and always
    reports success, so calling it on a failure path would hide the failure.
    Both paths still bypass the interpreter's normal shutdown, because gRPC
    teardown hangs otherwise (env-compat #10); only the code differs. Nothing
    here ever closes a project: a workspace holding solve evidence must be
    banked first (ADR 0006 amendment).
    """
    sys.stdout.flush()
    if code == 0:
        ws.exit_keep_alive()        # does not return
    os._exit(code)


if __name__ == "__main__":
    raise SystemExit(main())
