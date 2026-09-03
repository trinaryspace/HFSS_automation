"""Capture named steps of a real step trace as a fixture, line for line.

Run logging, ticket 10. A classifier rule that one real step proved wrong
(a `new_desktop=True` inside a heredoc the same command then runs; a
`GrpcApiError` mentioned in prose a `read` returned) needs that step in the
suite, and the session it came from — the 2026-09-01 readout experiment,
Claude Code `e5cdcdf5-…`, 3.6 MB captured with its eleven subagents — is
too large to ship whole. This copies the requested lines of a
`results/state/trace/<id>.steps.jsonl` byte for byte into
`scripts/fixtures/<host>/<id>.steps-slice.jsonl`, refuses a line that does
not re-read to the same step, and records each seq with its sha256 in
`<id>.steps-slice.json` (docs/agents/fixture-fidelity.md). Rerunning
against an unchanged trace is byte-stable.

    python scripts/fixtures/capture_steps.py --trace <ws>/results/state/trace/<id>.steps.jsonl \\
        --seq 765 810 187 483 721 --out scripts/fixtures/claude-code
"""

import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUFFIX = ".steps-slice.jsonl"
CAPTURED_ON = "2026-09-02"


def capture(trace_path, seqs, out_dir, captured=CAPTURED_ON):
    """Write the slice and its index; return the index."""
    wanted = set(int(s) for s in seqs)
    kept = []
    with open(trace_path, "rb") as fh:
        for raw in fh:
            line = raw.rstrip(b"\r\n")
            if not line:
                continue
            step = json.loads(line.decode("utf-8"))
            if step.get("seq") in wanted and step.get("parent_session_id") is None:
                kept.append((step["seq"], line, step))
    missing = wanted - {seq for seq, _, _ in kept}
    if missing:
        raise SystemExit("FAIL: capture_steps seq not in the trace: %s" % sorted(missing))
    kept.sort(key=lambda item: item[0])
    session_id = kept[0][2]["session_id"]
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, session_id + SUFFIX)
    with open(target, "wb") as fh:
        for _, line, _ in kept:
            fh.write(line + b"\n")
    with open(target, "rb") as fh:
        back = [json.loads(l) for l in fh.read().splitlines() if l]
    if back != [step for _, _, step in kept]:
        raise SystemExit("FAIL: capture_steps the slice does not re-read to the same steps")
    index = {
        "captured": captured,
        "captured_from": os.path.abspath(trace_path),
        "session_id": session_id,
        "note": __doc__.strip().splitlines()[0],
        "steps": {str(seq): {"kind": step.get("kind"), "tool": step.get("tool"),
                             "bytes": len(line), "sha256": hashlib.sha256(line).hexdigest()}
                  for seq, line, step in kept},
    }
    with open(target[: -len(".jsonl")] + ".json", "w", encoding="utf-8") as fh:
        json.dump(index, fh, indent=2)
        fh.write("\n")
    return index


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--trace", required=True, help="a <id>.steps.jsonl written by run_trace")
    parser.add_argument("--seq", required=True, nargs="+", type=int, help="the seqs to keep (main session)")
    parser.add_argument("--out", default=os.path.join(HERE, "claude-code"), help="fixture dir")
    args = parser.parse_args(argv)
    index = capture(args.trace, args.seq, args.out)
    print("PASS: capture_steps %s seqs=%s" % (index["session_id"], ",".join(sorted(index["steps"], key=int))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
