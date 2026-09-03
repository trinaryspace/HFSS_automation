"""Capture a workspace's `results/state/` files as fixtures, byte for byte.

Run logging, ticket 10. `scripts/fixtures/patch-array-5800/capture.py` did
this for one workspace (with its ledger slice besides); the two other runs
the acceptance grades — `patch-2400` (`kind-rocket`) and `bowtie-3500-pilot`
(`shiny-canyon`) — keep their real machine state only in the main
checkout's gitignored `results/state/`, which a worktree never sees. This
captures every top-level file of such a directory into
`scripts/fixtures/<workspace>/state/`, records size and sha256 in
`index.json`, and refuses a file that does not re-read identical
(docs/agents/fixture-fidelity.md). `scripts/fixtures/backfill.py` then
materializes the captured files into a checkout's workspace, so
`scripts/run_report.py --workspace workspaces/<name>` reads the run's real
watchdog log, bank and outcome wherever it runs.

Not captured: subdirectories (`verify/`, `trace/`, `zact_export/`) and the
files the tooling writes after the run — `events.jsonl` (the report's own
`report.written` lines), `tools.jsonl`, `sessions.jsonl` (the backfill's
own output) and `run.json`.

    python scripts/fixtures/capture_state.py --workspace patch-2400 \\
        --from C:/path/to/checkout/workspaces/patch-2400

Rerunning against an unchanged source is byte-stable.
"""

import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
STATE_SUBDIR = "state"
INDEX = "index.json"
NOT_CAPTURED = ("events.jsonl", "tools.jsonl", "sessions.jsonl", "run.json")
CAPTURED_ON = "2026-09-02"


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def capture(workspace_name, source_workspace, out_root=HERE, captured=CAPTURED_ON):
    """Write `<out_root>/<workspace_name>/state/<file>` for every top-level
    file of `<source_workspace>/results/state/` and the index; return it."""
    state_dir = os.path.join(source_workspace, "results", "state")
    if not os.path.isdir(state_dir):
        raise SystemExit("FAIL: capture_state no results/state under %s" % source_workspace)
    out_dir = os.path.join(out_root, workspace_name)
    os.makedirs(os.path.join(out_dir, STATE_SUBDIR), exist_ok=True)
    index = {
        "captured": captured,
        "captured_from_workspace": os.path.abspath(source_workspace),
        "note": __doc__.strip().splitlines()[0],
        "files": {},
    }
    for name in sorted(os.listdir(state_dir)):
        path = os.path.join(state_dir, name)
        if not os.path.isfile(path) or name in NOT_CAPTURED:
            continue
        with open(path, "rb") as handle:
            data = handle.read()
        target = os.path.join(out_dir, STATE_SUBDIR, name)
        with open(target, "wb") as handle:
            handle.write(data)
        with open(target, "rb") as handle:
            back = handle.read()
        if back != data:
            raise SystemExit("FAIL: capture_state %s does not re-read identical to its source" % name)
        index["files"][STATE_SUBDIR + "/" + name] = {
            "source": "results/state/" + name, "slice": "whole file",
            "bytes": len(data), "sha256": _sha(data)}
    with open(os.path.join(out_dir, INDEX), "w", encoding="utf-8") as handle:
        json.dump(index, handle, indent=2)
        handle.write("\n")
    return index


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspace", required=True, help="workspace name (fixture dir name)")
    parser.add_argument("--from", dest="source", help="workspace dir to read results/state/ from "
                                                       "(default: this checkout's workspaces/<name>)")
    args = parser.parse_args(argv)
    source = args.source or os.path.join(REPO, "workspaces", args.workspace)
    index = capture(args.workspace, source)
    sizes = " ".join("%s=%d" % (n.split("/", 1)[1], f["bytes"]) for n, f in index["files"].items())
    print("PASS: capture_state %s files=%d %s" % (args.workspace, len(index["files"]), sizes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
