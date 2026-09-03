"""Record a Review-gate verdict the moment the user gives it.

    python scripts/record_gate.py --workspace workspaces/<name> \
        --gate 1 --verdict fixes --note "notches in 1 of 4 patches; ports in yz"
    python scripts/record_gate.py --workspace workspaces/<name> --gate 1 --verdict pass

Appends one line to `results/state/review_gate.txt`:

    ts=<epoch seconds> gate=<n> verdict=<pass|fixes> note=<one line>

The file is append-only — a gate that took three fix rounds has three
`fixes` lines and one `pass` line, so the run report can attribute the wait
and the rebuilds to that gate instead of reading them out of the ledger's
prose. `read_gates()` parses the file back for the report.

One `PASS:` line on success; a `FAIL:` line and exit 1 on malformed input,
with nothing appended.
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
from hfss_spec import events  # noqa: E402

GATE_FILE = "review_gate.txt"
VERDICT_PASS = "pass"
VERDICT_FIXES = "fixes"
VERDICTS = (VERDICT_PASS, VERDICT_FIXES)

_LINE = re.compile(r"^ts=(?P<ts>\S+) gate=(?P<gate>\d+) verdict=(?P<verdict>\S+)"
                   r"(?: note=(?P<note>.*))?$")


def fail(message):
    print(f"FAIL: record_gate {message}")
    return 1


def render(gate, verdict, note="", ts=None):
    """One record line, note last so it may contain spaces."""
    line = f"ts={time.time() if ts is None else ts} gate={gate} verdict={verdict}"
    if note:
        line += f" note={note}"
    return line + "\n"


def gate_path(workspace):
    return Path(workspace) / "results" / "state" / GATE_FILE


def read_gates(path):
    """Every recorded verdict, oldest first; a line that does not parse is skipped."""
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError:
        return []
    records = []
    for line in text.splitlines():
        m = _LINE.match(line.strip())
        if m is None:
            continue
        try:
            ts = float(m.group("ts"))
        except ValueError:
            continue
        records.append({"ts": ts, "gate": int(m.group("gate")),
                        "verdict": m.group("verdict"), "note": m.group("note") or ""})
    return records


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspace", help="workspace dir; the file lands in results/state/")
    parser.add_argument("--gate", help="which Review gate, counting from 1")
    parser.add_argument("--verdict", help="one of: " + ", ".join(VERDICTS))
    parser.add_argument("--note", default="", help="one line: what the user asked for")
    args = parser.parse_args(argv)

    if not args.workspace:
        return fail("needs --workspace")
    workspace = Path(args.workspace)
    if not workspace.is_dir():
        return fail(f"workspace is not a directory: {workspace}")
    try:
        gate = int(str(args.gate).strip())
    except (TypeError, ValueError):
        return fail(f"gate must be a positive integer, got {args.gate!r}")
    if gate < 1:
        return fail(f"gate must be a positive integer, got {gate}")
    verdict = (args.verdict or "").strip()
    if verdict not in VERDICTS:
        return fail(f"verdict must be one of {', '.join(VERDICTS)}; got {args.verdict!r}")
    note = args.note.strip()
    if "\n" in note or "\r" in note:
        return fail("note must be one line")

    target = gate_path(workspace)
    os.makedirs(target.parent, exist_ok=True)
    with open(target, "a", encoding="utf-8") as handle:
        handle.write(render(gate, verdict, note))
    recorded = len(read_gates(target))
    line = f"PASS: record_gate gate={gate} verdict={verdict} recorded={recorded} file={target}"
    print(line)
    events.emit(target.parent, "gate.recorded", verdict=line,
                detail=f"gate={gate} verdict={verdict} note={note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
