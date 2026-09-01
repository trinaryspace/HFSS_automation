"""Design-spec-route sync verifier (ADR 0005) — the route's replay driver.

`12_verify_sync.py` replays numbered staged scripts, which the design-spec
route does not have; this driver replays the route's actual artifact — the
`design*.yaml` specs — with the same contract:

1. Copy src/ + docs + every `design*.yaml` into a fresh stamp under
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
       FAIL: no design*.yaml to replay — <copy>
       FAIL: named spec missing from copy: <names>

Usage:  python src/verify_spec_replay.py [--spec SPEC_OR_SPECS ...]
Unsafe only in that it launches a second AEDT desktop (a license seat) —
that is the point: the replay must not touch the live desktop.

Canonicalization and diff reuse `12_verify_sync`'s (imported, not copied).

**Why the spec set is discovered and not hard-coded.** This driver was
written inside patch-array-5800, which happened to carry two specs —
`design.yaml` for the fed array and `design_elements.yaml` for the
elements-only extraction design — so its default spec list was written as
that literal pair. On any ordinary single-spec workspace the default run
then printed `FAIL: sync mismatch` because `design_elements.yaml` did not
exist: a false FAIL, in a gate, caused by a file that was never supposed to
be there. Two places in this same file already had it right — `stamp_copy()`
copied each spec only `if os.path.isfile(...)`, and the `--spec` help text
already promised "those present in the copy" — so the defect was one check
disagreeing with the behaviour documented beside it. The set is now
`discover_specs()` over the copy, in both places.

**Absence is never a mismatch.** `sync mismatch` means the replayed model
differed from the live one; that is the verdict a reader acts on, and it
must never be spent on a file that was not there. So the two ways a spec
can be absent get their own lines:

- **Defaulted** (no `--spec`): the set is whatever `design*.yaml` the copy
  holds, so an absent file is not an error — it is simply not in the set.
  Finding none at all is `FAIL: no design*.yaml to replay`, which says
  nothing was verified — a different fact from "the model differed", and
  the one a reader needs in order to know the gate did not actually run.
- **Named** (`--spec NAME`): the caller asked for that spec by name, so its
  absence is a real error and still fails loudly — but as `named spec
  missing`, because it too says nothing about the model.

Discovery order is deliberate and stable: `design.yaml` first when present
(the route's principal artifact, and the specs compile into ONE design on
the copy in the order they are given), then the rest sorted. A gate verdict
must not depend on the order the filesystem happens to hand back names.
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

# The route's principal artifact. Replayed first when present, because the
# specs compile into one design on the copy in the order given.
PRIMARY_SPEC = "design.yaml"
SPEC_PREFIX = "design"
SPEC_SUFFIX = ".yaml"


def discover_specs(root):
    """The `design*.yaml` basenames actually present in `root`, in replay order.

    Pure filesystem work — no AEDT, no desktop — so the spec set a defaulted
    run will replay is checkable offline, which is how the hard-coded-pair
    defect is kept from coming back.

    Order: `design.yaml` first if present, then the remainder sorted. Plain
    `sorted()` would already put `design.yaml` first for every name this
    repo has produced ('.' sorts below every alnum and '_'), but not for a
    hypothetical `design-alt.yaml` ('-' sorts below '.'), and the principal
    spec leading is a property worth stating rather than inheriting from an
    ASCII accident. A missing or unreadable directory yields no specs, so a
    caller gets the "nothing to replay" verdict rather than a traceback.
    """
    try:
        names = os.listdir(root)
    except OSError:
        return []
    found = sorted(name for name in names
                   if name.startswith(SPEC_PREFIX) and name.endswith(SPEC_SUFFIX)
                   and os.path.isfile(os.path.join(root, name)))
    if PRIMARY_SPEC in found:
        found.remove(PRIMARY_SPEC)
        found.insert(0, PRIMARY_SPEC)
    return found


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
    # Every design*.yaml, not a hard-coded pair: a spec the copy does not
    # carry is a spec the replay cannot run, and `--spec` names are resolved
    # against the copy.
    for name in discover_specs(ws_common.WORKSPACE):
        shutil.copy2(os.path.join(ws_common.WORKSPACE, name),
                     os.path.join(dest, name))
    return dest


def resolve_specs(copy, named=None):
    """(specs, failure_line) for a replay over `copy`.

    Exactly one of the two is meaningful: a non-empty `specs` list, or a
    terminal FAIL line to print. The defaulted and the named cases fail
    differently on purpose — see the module docstring; neither borrows the
    `sync mismatch` verdict, which belongs to a model that differed.
    """
    if named:
        specs = list(named)
        missing = [s for s in specs
                   if not os.path.isfile(os.path.join(copy, s))]
        if missing:
            return [], ("FAIL: named spec missing from copy: %s"
                        % ", ".join(missing))
        return specs, None
    specs = discover_specs(copy)
    if not specs:
        return [], "FAIL: no design*.yaml to replay — %s" % copy
    return specs, None


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
                        help="spec basenames to replay, resolved against the "
                             "copy; a named spec that is missing is an error. "
                             "Default: every design*.yaml present in the copy, "
                             "design.yaml first.")
    args = parser.parse_args(argv)
    python = sys.executable
    live_snapshot = os.path.join(ws_common.WORKSPACE, "results", "state",
                                 "model_snapshot.json")
    if not os.path.isfile(live_snapshot):
        print("FAIL: sync mismatch — no live model_snapshot.json (run capture_state.py first)", flush=True)
        return 1
    copy = stamp_copy()
    print("copy:", copy, flush=True)
    specs, failure = resolve_specs(copy, args.spec)
    if failure:
        print(failure, flush=True)
        return 1
    for spec in specs:
        print("  replay:", spec, flush=True)
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
