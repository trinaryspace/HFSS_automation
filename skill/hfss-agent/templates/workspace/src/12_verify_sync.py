"""Read-back sync verifier (ADR 0005): replay the amended scripts and diff.

Run from the live workspace (Build session, after the Review gate is
passed with tweaks): the amended staged scripts are replayed top-to-bottom
on a FRESH COPY of the workspace on a port-pinned SECOND desktop, the same
model shape is captured there, and the result is diffed against
`results/state/model_snapshot.json` (written by `capture_state.py` against
the live model). The read-back sync contract (ADR 0005) is then verified
mechanically: replaying the scripts reproduces the delivered model.

Output contract: exactly ONE terminal verdict line —
    PASS: sync replay matches snapshot
    FAIL: sync mismatch — <differing keys or reason>

Safety: teardown is port-pinned to the COPY's recorded port/pid (the copy
lives under `results/state/verify/` inside this workspace) and runs as a
subprocess of the copy's own ws_common — the user's desktop and the live
session desktop can never be touched, and the process that prints the
verdict is never killed by that teardown's os._exit.

Replay set (default): the numbered stage scripts NN_*.py that build the
model before the solve — anything whose basename suggests solve/plots/QA
is skipped, as are the infra scripts. Pass explicit script names (relative
to src/) to replay a different set.

Usage:  python src/12_verify_sync.py [workspace] [script ...]
Exit: 0 on PASS, 1 on FAIL (scripts always get their port-pinned teardown).
"""

import json
import os
import shutil
import subprocess
import sys
import time

INFRA = {"ws_common", "poll_solve", "capture_state", "12_verify_sync",
         "00_static_gate", "stage_skeleton"}
SOLVE_LIKE = ("solve", "qa", "plot")
SCRIPT_TIMEOUT_S = int(os.environ.get("VERIFY_SCRIPT_TIMEOUT_S", "900"))


def workspace_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def select_replay_scripts(src_dir, explicit=None):
    """The scripts to replay: explicit names, else build-stage NN_*.py."""
    if explicit:
        return [os.path.join(src_dir, name) for name in explicit]
    picked = []
    for name in sorted(os.listdir(src_dir)):
        if not name.endswith(".py") or not name[:2].isdigit():
            continue
        stem = name[:-3]
        if stem in INFRA:
            continue
        if any(mark in stem.lower() for mark in SOLVE_LIKE):
            continue
        if 1 <= int(name[:2]) <= 10:
            picked.append(os.path.join(src_dir, name))
    return picked


def make_copy(workspace):
    """Fresh copy of src/ + docs under `results/state/verify/<stamp>/copy`.

    Nothing from results/, *.aedt, *.aedtresults, or lock files is copied,
    so the copy carries no live-session desktop state: its scripts launch
    and pin their own second desktop.
    """
    stamp = time.strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(workspace, "results", "state", "verify", stamp, "copy")
    src_dir = os.path.join(workspace, "src")
    os.makedirs(dest, exist_ok=True)
    for name in os.listdir(src_dir):
        if name.endswith(".py"):
            shutil.copy2(os.path.join(src_dir, name), os.path.join(dest, name))
    for name in ("README.md", "state.md", "summary.md"):
        path = os.path.join(workspace, name)
        if os.path.isfile(path):
            shutil.copy2(path, os.path.join(dest, name))
    return dest


def _run_py(python, args, cwd, ok_exit_codes=(0,)):
    """Run python<args>; return (exit_code, stdout, stderr)."""
    try:
        proc = subprocess.run(
            [python] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=SCRIPT_TIMEOUT_S,
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        return -1, (exc.stdout or ""), "TIMED OUT after %ds" % SCRIPT_TIMEOUT_S


def diff_shapes(live, replay, prefix=()):
    """Deep-diff two snapshots; sorted list of differing path strings."""
    diffs = []
    live_keys = set(live or {})
    replay_keys = set(replay or {})
    for key in sorted(live_keys | replay_keys):
        path = prefix + (key,)
        if key not in live_keys:
            diffs.append(".".join(path) + ": only in replay")
        elif key not in replay_keys:
            diffs.append(".".join(path) + ": only in live")
        elif isinstance(live[key], dict) and isinstance(replay[key], dict):
            diffs.extend(diff_shapes(live[key], replay[key], path))
        else:
            sub1 = json.dumps(live[key], sort_keys=True, default=str)
            sub2 = json.dumps(replay[key], sort_keys=True, default=str)
            if sub1 != sub2:
                elided1 = sub1[:160] if len(sub1) > 160 else sub1
                elided2 = sub2[:160] if len(sub2) > 160 else sub2
                diffs.append("%s: %r <-> %r" % (".".join(path), elided1, elided2))
    return diffs


def main(argv=None):
    argv = argv if argv is not None else sys.argv
    workspace = os.path.abspath(argv[1]) if len(argv) > 1 else workspace_root()
    explicit = argv[2:]
    python = sys.executable
    src_dir = os.path.join(workspace, "src")
    live_snapshot = os.path.join(workspace, "results", "state", "model_snapshot.json")
    if not os.path.isfile(live_snapshot):
        print("FAIL: sync mismatch — no live model_snapshot.json (run capture_state.py first)",
              flush=True)
        return 1

    scripts = select_replay_scripts(src_dir, explicit)
    if not scripts:
        print("FAIL: sync mismatch — no replay scripts found in src/", flush=True)
        return 1
    print("verify_sync replay count =", len(scripts), flush=True)
    for s in scripts:
        print("  replay:", os.path.relpath(s, src_dir), flush=True)

    copy = make_copy(workspace)
    print("copy:", copy, flush=True)

    failed = []
    for script in scripts:
        rc, stdout, stderr = _run_py(python, [script], cwd=os.path.dirname(script))
        tail = (stdout or "").strip().splitlines()[-6:]
        if stderr:
            tail.extend(("stderr: " + line) for line in stderr.strip().splitlines()[-3:])
        for line in tail:
            print("  |", line, flush=True)
        if rc != 0:
            failed.append(os.path.basename(script))
    if failed:
        print("FAIL: sync mismatch — replay scripts failed: " + ", ".join(failed), flush=True)
        _teardown_copy(python, copy)
        return 1

    cap_script = os.path.join(copy, "capture_state.py")
    rc, stdout, stderr = _run_py(python, [cap_script], cwd=os.path.dirname(cap_script))
    for line in (stdout or "").strip().splitlines()[-4:]:
        print("  |", line, flush=True)
    replay_snapshot = os.path.join(copy, "results", "state", "model_snapshot.json")
    if rc != 0 or not os.path.isfile(replay_snapshot):
        print("FAIL: sync mismatch — capture_state on the replay copy failed", flush=True)
        _teardown_copy(python, copy)
        return 1

    live = _load_json(live_snapshot) or {}
    replay = _load_json(replay_snapshot) or {}
    diffs = diff_shapes(live, replay)
    _teardown_copy(python, copy)
    if diffs:
        shown = diffs[:8]
        print("FAIL: sync mismatch — differing keys: " + " | ".join(shown), flush=True)
        if len(diffs) > len(shown):
            print("%d more differences" % (len(diffs) - len(shown)), flush=True)
        return 1
    print("PASS: sync replay matches snapshot", flush=True)
    return 0


def _load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _teardown_copy(python, copy):
    """Port-pinned teardown of the SECOND desktop, from the COPY's state.

    Runs as a fresh subprocess importing the copy's own ws_common, so the
    teardown acts only on the copy's recorded port/pid and its os._exit
    cannot kill this verdict-printing process.
    """
    expr = "import sys;sys.path.insert(0,%r);from ws_common import teardown;teardown()" % copy
    try:
        proc = subprocess.run([python, "-c", expr], capture_output=True, text=True, timeout=120)
        for line in (proc.stdout or "").strip().splitlines()[-3:]:
            print("  teardown |", line, flush=True)
    except Exception as exc:  # noqa: BLE001 - best effort
        print("  teardown | exception:", type(exc).__name__, str(exc)[:160], flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
