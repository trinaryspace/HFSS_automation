"""Tier 1: build a workspace on the live desktop, but never solve it.

Between Tier 0 (seconds, no license) and Tier 2 (hours, full solve) sits
the question most regressions actually live in: does the model still
*build*? The pilot answered that by replaying eight staged scripts on a
port-pinned second desktop and then solving — roughly eight minutes a
round, six rounds. Most of that cost bought nothing, because the bugs it
found were build-stage bugs.

Tier 1 runs a workspace's build stages in order, stops dead before the
solve, and captures the model snapshot. It is deliberately incapable of
solving: any stage numbered 08 or above is refused, not skipped quietly,
so this runner can never consume solver time or license-hours by accident.

Preconditions are the skill's own (env-compat "Standing prerequisites"):
VPN up so the license server is reachable, AEDT 2024 R1 launchable. When
they are not met this exits non-zero with the evidence rather than
working around it.

Once the spec compiler lands (phase 2, ticket 10) this grows a `--spec`
mode that compiles a `design.yaml` instead of running staged scripts; the
stage-script mode stays as the escape-hatch path.

Usage:
    python scripts/tier1.py --workspace workspaces/<name>
    python scripts/tier1.py --workspace workspaces/<name> --dry-run
"""

import argparse
import os
import re
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

from hfss_spec import events  # noqa: E402

SOLVE_STAGE = 8
STAGE_RE = re.compile(r"^(\d{2})_.*\.py$")
PASS_RE = re.compile(r"^PASS:\s*(.+)$", re.MULTILINE)
FAIL_MARKERS = ("STAGE_FAILED", "Traceback (most recent call last)")


def build_stages(src_dir):
    """Ordered `NN_*.py` build stages: every stage BELOW the solve stage."""
    stages = []
    for name in sorted(os.listdir(src_dir)):
        match = STAGE_RE.match(name)
        if not match:
            continue
        number = int(match.group(1))
        if number >= SOLVE_STAGE:
            continue
        stages.append((number, name))
    return stages


def refused_stages(src_dir):
    """Solve-and-beyond stages, listed so the refusal is explicit."""
    refused = []
    for name in sorted(os.listdir(src_dir)):
        match = STAGE_RE.match(name)
        if match and int(match.group(1)) >= SOLVE_STAGE:
            refused.append(name)
    return refused


def run_stage(src_dir, name, timeout):
    """Run one staged script; return (ok, verification_line, tail)."""
    started = time.time()
    env = dict(os.environ)
    # Context hygiene: staged scripts must not spray pyAEDT INFO into the
    # runner's output. The verification line is the contract, not the log.
    env.setdefault("PYAEDT_LOG_LEVEL", "WARNING")
    try:
        proc = subprocess.run([sys.executable, name], cwd=src_dir, env=env,
                              capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, None, "timed out after %ds" % timeout
    output = (proc.stdout or "") + (proc.stderr or "")
    elapsed = time.time() - started
    verification = None
    match = PASS_RE.search(output)
    if match:
        verification = match.group(1).strip()
    failed = (proc.returncode != 0
              or verification is None
              or any(marker in output for marker in FAIL_MARKERS))
    tail = "\n".join(output.strip().splitlines()[-12:])
    return (not failed), verification, tail if failed else "%.1fs" % elapsed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspace", required=True,
                        help="workspace directory holding src/ and results/")
    parser.add_argument("--dry-run", action="store_true",
                        help="list what would run; touches no desktop")
    parser.add_argument("--timeout", type=int, default=900,
                        help="per-stage timeout in seconds (default 900)")
    parser.add_argument("--no-snapshot", action="store_true",
                        help="skip the capture_state snapshot")
    args = parser.parse_args(argv)

    workspace = os.path.abspath(os.path.join(REPO, args.workspace))
    src_dir = os.path.join(workspace, "src")
    state_dir = os.path.join(workspace, "results", "state")
    if not os.path.isdir(src_dir):
        print("FAIL: tier1 no src/ under %s" % workspace)
        return 2

    stages = build_stages(src_dir)
    refused = refused_stages(src_dir)
    if not stages:
        line = ("FAIL: tier1 no build stages (NN_*.py below %02d) in %s"
                % (SOLVE_STAGE, src_dir))
        print(line)
        events.emit(state_dir, "gate.tier1", verdict=line)
        return 2

    print("  workspace: %s" % os.path.relpath(workspace, REPO).replace(os.sep, "/"))
    print("  build stages: %s" % ", ".join(name for _n, name in stages))
    if refused:
        print("  refused (solve and beyond, never run here): %s" % ", ".join(refused))

    if args.dry_run:
        line = "PASS: tier1 dry-run stages=%d refused=%d" % (len(stages), len(refused))
        print(line)
        events.emit(state_dir, "gate.tier1", verdict=line,
                    detail="stages=%s" % ",".join(name for _n, name in stages))
        return 0

    started = time.time()
    failures = []
    for _number, name in stages:
        # Each staged script is a Spine stage; its Verification line is the
        # stage's verdict, so the boundary and the verdict land as one
        # stage.start / stage.end pair (run logging, ticket 03).
        events.emit(state_dir, "stage.start", stage=name)
        stage_started = time.time()
        ok, verification, detail = run_stage(src_dir, name, args.timeout)
        if ok:
            print("  %-34s ok    %s" % (name, verification or ""))
            events.emit(state_dir, "stage.end", stage=name,
                        verdict="PASS: %s" % verification,
                        duration_ms=(time.time() - stage_started) * 1000)
        else:
            print("  %-34s FAIL" % name)
            for line in detail.splitlines():
                print("      | %s" % line)
            events.emit(state_dir, "stage.end", stage=name,
                        verdict="FAIL: %s %s" % (name, detail.strip().splitlines()[-1]
                                                 if detail.strip() else "no output"),
                        duration_ms=(time.time() - stage_started) * 1000)
            failures.append(name)
            break  # a failed stage invalidates everything after it

    snapshot = None
    if not failures and not args.no_snapshot:
        capture = os.path.join(src_dir, "capture_state.py")
        if os.path.isfile(capture):
            ok, verification, detail = run_stage(src_dir, "capture_state.py",
                                                 args.timeout)
            if ok:
                snapshot = os.path.join(workspace, "results", "state",
                                        "model_snapshot.json")
                print("  %-34s ok    %s" % ("capture_state.py", verification or ""))
            else:
                print("  %-34s FAIL" % "capture_state.py")
                for line in detail.splitlines():
                    print("      | %s" % line)
                failures.append("capture_state.py")

    elapsed = time.time() - started
    if failures:
        line = ("FAIL: tier1 stages=%d failed=%s elapsed=%.1fs"
                % (len(stages), ",".join(failures), elapsed))
    else:
        line = ("PASS: tier1 stages=%d solved=no snapshot=%s elapsed=%.1fs"
                % (len(stages),
                   "yes" if snapshot and os.path.isfile(snapshot) else "no",
                   elapsed))
    print(line)
    events.emit(state_dir, "gate.tier1", verdict=line,
                detail="failed=%s" % (",".join(failures) or "-"),
                duration_ms=elapsed * 1000)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
