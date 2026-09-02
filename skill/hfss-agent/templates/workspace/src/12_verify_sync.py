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

The verdict line is also a `sync.verify` event in the live workspace's
`results/state/events.jsonl` (run logging, ticket 03).
"""

import json
import os
import re
import shutil
import subprocess
import sys
import time

try:
    import run_events
except ImportError:
    # Loaded by file path with src/ off sys.path (`hfss_spec.acceptance`
    # borrows `canon` / `diff_shapes` that way): take the sibling by path.
    import importlib.util as _importlib_util

    _spec = _importlib_util.spec_from_file_location(
        "run_events", os.path.join(os.path.dirname(os.path.abspath(__file__)), "run_events.py"))
    run_events = _importlib_util.module_from_spec(_spec)
    _spec.loader.exec_module(run_events)

INFRA = {"ws_common", "poll_solve", "capture_state", "12_verify_sync",
         "00_static_gate", "stage_skeleton", "run_events"}
SOLVE_LIKE = ("solve", "qa", "plot")
try:
    SCRIPT_TIMEOUT_S = int(os.environ.get("VERIFY_SCRIPT_TIMEOUT_S", "900"))
except ValueError:
    SCRIPT_TIMEOUT_S = 900


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
    and pin their own second desktop. Scripts land in the copy's `src/`
    (the template layout) so ws_common's WORKSPACE derivation — parent of
    the script's parent directory — resolves to the COPY root, not the
    stamp dir.
    """
    stamp = time.strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(workspace, "results", "state", "verify", stamp, "copy")
    src_dir = os.path.join(workspace, "src")
    os.makedirs(os.path.join(dest, "src"), exist_ok=True)
    for name in os.listdir(src_dir):
        if name.endswith(".py"):
            shutil.copy2(os.path.join(src_dir, name), os.path.join(dest, "src", name))
    for name in ("README.md", "state.md", "summary.md"):
        path = os.path.join(workspace, name)
        if os.path.isfile(path):
            shutil.copy2(path, os.path.join(dest, name))
    return dest


def _run_py(python, args, cwd):
    """Run python<args>; return (exit_code, stdout, stderr), timeout-guarded."""
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


RAND_SUFFIX = re.compile(r"(Sweep_|Rad__)[A-Z0-9]{6}")  # AEDT auto-suffixes (EC#6)


def canon(val):
    """Normalize AEDT random auto-suffixes (sweep/radiation names) before diff.

    Dict keys are the danger: two raw keys with DIFFERENT random suffixes
    must not collapse onto one canonical key, or a count drift (a replay
    gaining a second same-class entry) would vanish from the diff. Keys
    within one dict that map to the same canonical form are therefore
    numbered: `Rad__<RND>#1`, `#2`, ... so both sides keep their counts.
    """

    def canon_key(k, seen):
        out = RAND_SUFFIX.sub(r"\1<RND>", str(k))
        if out != str(k):
            n = seen.get(out, 0) + 1
            seen[out] = n
            if n > 1:
                out = "%s#%d" % (out, n)
        return out

    if isinstance(val, dict):
        seen = {}
        return {canon_key(k, seen): canon(v) for k, v in sorted(val.items(), key=lambda kv: str(kv[0]))}
    if isinstance(val, list):
        return [canon(v) for v in val]
    if isinstance(val, tuple):
        return tuple(canon(v) for v in val)
    if isinstance(val, str):
        return RAND_SUFFIX.sub(r"\1<RND>", val)
    return val


def diff_shapes(live, replay, prefix=()):
    """Deep-diff two canonicalized snapshots; sorted list of differing paths."""
    diffs = []
    live = canon(live or {})
    replay = canon(replay or {})
    live_keys = set(live)
    replay_keys = set(replay)
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


def verdict(workspace, line, rc):
    """Print the one terminal verdict line and record it as `sync.verify`."""
    print(line, flush=True)
    run_events.emit("sync.verify", stage="sync", verdict=line,
                    state_dir=os.path.join(workspace, "results", "state"))
    return rc


def main(argv=None):
    argv = argv if argv is not None else sys.argv
    workspace = os.path.abspath(argv[1]) if len(argv) > 1 else workspace_root()
    explicit = argv[2:]
    python = sys.executable
    src_dir = os.path.join(workspace, "src")
    live_snapshot = os.path.join(workspace, "results", "state", "model_snapshot.json")
    if not os.path.isfile(live_snapshot):
        return verdict(workspace, "FAIL: sync mismatch — no live model_snapshot.json "
                                  "(run capture_state.py first)", 1)

    scripts = select_replay_scripts(src_dir, explicit)
    if not scripts:
        return verdict(workspace, "FAIL: sync mismatch — no replay scripts found in src/", 1)
    print("verify_sync replay count =", len(scripts), flush=True)
    for s in scripts:
        print("  replay:", os.path.relpath(s, src_dir), flush=True)

    copy = make_copy(workspace)
    print("copy:", copy, flush=True)
    # The replay runs the COPIED scripts (paths inside the fresh copy), never
    # the live ones: their ws_common derives paths from the copy, so the
    # second desktop, its port pin, and the delete-then-create runs all act
    # on the copy — the live workspace is untouched.
    replays = [os.path.join(copy, "src", os.path.basename(s)) for s in scripts]

    failed = []
    for script in replays:
        rc, stdout, stderr = _run_py(python, [script], cwd=os.path.dirname(script))
        tail = (stdout or "").strip().splitlines()[-6:]
        if stderr:
            tail.extend(("stderr: " + line) for line in stderr.strip().splitlines()[-3:])
        for line in tail:
            print("  |", line, flush=True)
        # os._exit(0) hides a failed replay's exit code (the staged-script
        # pattern), so failure means: nonzero rc OR any STAGE_FAILED line.
        if rc != 0 or "STAGE_FAILED" in (stdout or ""):
            failed.append(os.path.basename(script))
    if failed:
        _teardown_copy(python, copy)
        return verdict(workspace, "FAIL: sync mismatch — replay scripts failed: "
                                  + ", ".join(failed), 1)

    cap_script = os.path.join(copy, "src", "capture_state.py")
    rc, stdout, stderr = _run_py(python, [cap_script], cwd=os.path.dirname(cap_script))
    for line in (stdout or "").strip().splitlines()[-4:]:
        print("  |", line, flush=True)
    replay_snapshot = os.path.join(copy, "results", "state", "model_snapshot.json")
    if rc != 0 or not os.path.isfile(replay_snapshot):
        _teardown_copy(python, copy)
        return verdict(workspace, "FAIL: sync mismatch — capture_state on the replay "
                                  "copy failed", 1)

    live = _load_json(live_snapshot) or {}
    replay = _load_json(replay_snapshot) or {}
    diffs = diff_shapes(live, replay)
    _teardown_copy(python, copy)
    if diffs:
        shown = diffs[:8]
        if len(diffs) > len(shown):
            print("%d more differences" % (len(diffs) - len(shown)), flush=True)
        return verdict(workspace, "FAIL: sync mismatch — differing keys: "
                                  + " | ".join(shown), 1)
    return verdict(workspace, "PASS: sync replay matches snapshot", 0)


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
    expr = ("import sys;sys.path.insert(0,%r);from ws_common import teardown;teardown()" %
            os.path.join(copy, "src"))
    try:
        proc = subprocess.run([python, "-c", expr], capture_output=True, text=True, timeout=120)
        for line in (proc.stdout or "").strip().splitlines()[-3:]:
            print("  teardown |", line, flush=True)
    except Exception as exc:  # noqa: BLE001 - best effort
        print("  teardown | exception:", type(exc).__name__, str(exc)[:160], flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
