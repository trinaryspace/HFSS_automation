"""Design-spec-route sync verifier (ADR 0005) — workspace-local.

`12_verify_sync.py` replays numbered staged scripts, which the design-spec
route does not have; this driver replays the route's actual artifact — the
`design*.yaml` specs — with the same contract:

1. Copy src/ + docs + the two specs into a fresh stamp under
   `results/state/verify/<stamp>/copy` (no project, no results, no locks:
   the copy carries no live-session state).
2. On the COPY, port-pinned: compile the spec(s) with `compile_spec.py
   --launch`, capture the model, diff its snapshot against the LIVE
   workspace's `results/state/model_snapshot.json`.
3. Teardown is the copy's own `ws_common.teardown()` (kills only the copy's
   desktop — the live pinned desktop is never touched).
4. Exactly one terminal verdict line:
       PASS: sync replay matches snapshot
       FAIL: sync mismatch — <differing keys>

Usage:  python src/verify_spec_replay.py [--spec SPEC_OR_SPECS ...]
Unsafe only in that it launches a second AEDT desktop (a license seat) —
that is the point: the replay must not touch the live desktop.

Canonicalization and diff reuse `12_verify_sync`'s (imported, not copied).
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time

import importlib.util

import ws_common

_VERIFIER = os.path.join(ws_common.WORKSPACE, "src", "12_verify_sync.py")
_spec = importlib.util.spec_from_file_location("_verify_sync", _VERIFIER)
_verify_sync = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_verify_sync)
canon = _verify_sync.canon
diff_shapes = _verify_sync.diff_shapes


def stamp_copy():
    stamp = time.strftime("%Y%m%d_%H%M%S")
    while True:
        dest = os.path.join(ws_common.WORKSPACE, "results", "state", "verify",
                            stamp, "copy")
        try:
            os.makedirs(dest, exist_ok=False)
            break
        except FileExistsError:
            stamp = time.strftime("%Y%m%d_%H%M%S_%f")
    src_dir = os.path.join(ws_common.WORKSPACE, "src")
    os.makedirs(os.path.join(dest, "src"), exist_ok=True)
    for name in os.listdir(src_dir):
        if name.endswith(".py") and not name.startswith("twelve_compat"):
            shutil.copy2(os.path.join(src_dir, name), os.path.join(dest, "src", name))
    for name in ("README.md", "state.md", "summary.md"):
        path = os.path.join(ws_common.WORKSPACE, name)
        if os.path.isfile(path):
            shutil.copy2(path, os.path.join(dest, name))
    for name in ("design.yaml", "design_elements.yaml"):
        path = os.path.join(ws_common.WORKSPACE, name)
        if os.path.isfile(path):
            shutil.copy2(path, os.path.join(dest, name))
    return dest


def run(python, args, cwd, timeout=1200):
    try:
        proc = subprocess.run([python] + args, cwd=cwd, capture_output=True,
                              text=True, timeout=timeout)
        return proc.returncode, proc.stdout or "", proc.stderr or ""
    except subprocess.TimeoutExpired as exc:
        return -1, exc.stdout or "", "TIMED OUT after %ds" % timeout


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--spec", action="append", default=None,
                        help="spec basenames to replay; default: design.yaml, "
                             "design_elements.yaml (those present in the copy)")
    args = parser.parse_args(argv)
    python = sys.executable
    live_snapshot = os.path.join(ws_common.WORKSPACE, "results", "state",
                                 "model_snapshot.json")
    if not os.path.isfile(live_snapshot):
        print("FAIL: sync mismatch — no live model_snapshot.json (run capture_state.py first)", flush=True)
        return 1
    copy = stamp_copy()
    print("copy:", copy, flush=True)
    specs = args.spec or ["design.yaml", "design_elements.yaml"]
    missing = [s for s in specs if not os.path.isfile(os.path.join(copy, s))]
    if missing:
        print("FAIL: sync mismatch — specs missing from copy: %s" % ", ".join(missing), flush=True)
        return 1
    failed = []
    for spec in specs:
        rc, out, err = run(python, [os.path.join(ws_common.WORKSPACE, "..", "..", "scripts", "compile_spec.py"),
                                    "--workspace", copy,
                                    "--spec", os.path.join(copy, spec),
                                    "--launch"],
                           cwd=os.path.join(copy, "src"))
        for line in (out or "").strip().splitlines()[-4:] + (err or "").strip().splitlines()[-3:]:
            print("  | " + line, flush=True)
        if rc != 0 or "STAGE_FAILED" in out:
            failed.append(spec)
    if not failed:
        rc, out, err = run(python, [os.path.join(copy, "src", "capture_state.py")],
                           cwd=os.path.join(copy, "src"))
        for line in (out or "").strip().splitlines()[-3:]:
            print("  | " + line, flush=True)
        replay_snapshot = os.path.join(copy, "results", "state", "model_snapshot.json")
        if rc != 0 or not os.path.isfile(replay_snapshot):
            failed.append("capture_state")
        else:
            live = json.load(open(live_snapshot, encoding="utf-8"))
            replay = json.load(open(replay_snapshot, encoding="utf-8"))
            diffs = diff_shapes(live, replay)
            if diffs:
                failed.append("snapshot: " + " | ".join(diffs[:8]))
    teardown = subprocess.run(
        [python, "-c",
         "import sys;sys.path.insert(0,%r);from ws_common import teardown;teardown()"
         % os.path.join(copy, "src")],
        capture_output=True, text=True, timeout=180,
    )
    for line in (teardown.stdout or "").strip().splitlines()[-2:]:
        print("  teardown | " + line, flush=True)
    if failed:
        print("FAIL: sync mismatch — %s" % "; ".join(failed), flush=True)
        return 1
    print("PASS: sync replay matches snapshot", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
