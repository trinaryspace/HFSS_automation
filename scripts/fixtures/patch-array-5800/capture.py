"""Capture the patch-array-5800 run-record fixtures, byte for byte.

Run logging, ticket 02. Two artifacts from the last real run are the ground
truth for two parsers, and both were written by hand rather than by a script:

- `state.session1.md` — `state.md` from its first byte up to (not including)
  the `## Session 2` heading. Its `- Started:` line carries trailing text,
  which the strict ledger regex in `scripts/run_card.py` rejected, so the run's
  active wall read `unmeasurable`.
- `outcome.txt` — the whole `results/state/outcome.txt`: free text with a UTF-8
  BOM, which the key=value parser read as nothing, so the card said
  `unrecorded`.
- `state/*` — every top-level file of `results/state/` (run logging, ticket
  05): the watchdog tick log `solve_progress.txt` (three watchdog runs, all
  `complete`), `readouts.txt` (the `route=both-failed` line with its two
  `GrpcApiError ... GetVariables`, and the 2026-09-01 readout experiment's
  pin move), `z_act.txt`, the pinned `aedt_port.txt` / `aedt_process_id.txt`,
  the overwritten `session.json`, `solved.txt`, `solve_started.txt`,
  `solve_watchdog_pid.txt`, `completions.txt` and `model_snapshot.json`.
  The pain-point classifiers (`hfss_spec/painpoints.py`) take their machine
  state from these. Subdirectories (`verify/`, `zact_export/`) are not
  captured.

The workspace is gitignored, so the fixtures are committed here. Rerunning
this script against an unchanged workspace is byte-stable; a slice is written
only after it re-reads identical to the source bytes, and `index.json` carries
each file's size and sha256 so drift is visible.

    python scripts/fixtures/patch-array-5800/capture.py [<workspace dir>]
"""

import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WORKSPACE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(HERE))), "workspaces", "patch-array-5800")
SESSION2 = b"## Session 2"
STATE_SUBDIR = "state"          # <out_dir>/state/<file>, one per results/state/ file


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def capture(workspace, out_dir=HERE):
    ledger = open(os.path.join(workspace, "state.md"), "rb").read()
    cut = ledger.index(SESSION2)
    session1 = ledger[:cut]
    outcome = open(os.path.join(workspace, "results", "state", "outcome.txt"), "rb").read()
    files = {"state.session1.md": (session1, "state.md",
                                   "bytes [0, index of '## Session 2')"),
             "outcome.txt": (outcome, "results/state/outcome.txt", "whole file")}
    state_dir = os.path.join(workspace, "results", "state")
    for name in sorted(os.listdir(state_dir)):
        path = os.path.join(state_dir, name)
        if not os.path.isfile(path):
            continue                    # verify/, zact_export/: not machine state
        files[STATE_SUBDIR + "/" + name] = (open(path, "rb").read(),
                                            "results/state/" + name, "whole file")
    os.makedirs(os.path.join(out_dir, STATE_SUBDIR), exist_ok=True)
    index = {
        "captured": "2026-09-02",
        "captured_from_workspace": os.path.abspath(workspace),
        "note": __doc__.strip().splitlines()[0],
        "files": {},
    }
    for name, (data, source, slice_) in files.items():
        target = os.path.join(out_dir, name)
        with open(target, "wb") as handle:
            handle.write(data)
        if open(target, "rb").read() != data:
            raise SystemExit("FAIL: capture %s does not re-read identical to its source" % name)
        index["files"][name] = {"source": source, "slice": slice_,
                                "bytes": len(data), "sha256": _sha(data)}
    with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as handle:
        json.dump(index, handle, indent=2)
        handle.write("\n")
    return index


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    workspace = argv[0] if argv else DEFAULT_WORKSPACE
    index = capture(workspace)
    sizes = " ".join("%s=%d" % (n, f["bytes"]) for n, f in index["files"].items())
    print("PASS: capture patch-array-5800 fixtures %s" % sizes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
