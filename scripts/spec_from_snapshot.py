"""Reduce a captured `model_snapshot.json` to a `design.yaml`. Ticket 12a.

Two jobs. It shapes the schema against real models rather than guesswork (Q7),
and it is the Re-entry mechanism (Q8): a project we did not build gets a spec
by reduction instead of by archaeology, which is what ADR 0001's copy-first
ceremony has been missing.

    copy the project (ADR 0001) -> capture_state -> spec_from_snapshot
        -> the spec IS the model card

The output is deliberately incomplete where the input is: geometry ops the
snapshot cannot name come out as `op: unknown` carrying their bounding box, and
`validate_spec` will refuse to compile them. That is the honest answer, not a
failure — a bounding box is a consequence of a construction op, not a
restatement of it.

Usage:
    python scripts/spec_from_snapshot.py <snapshot.json> [-o design.yaml]
                                         [--name NAME] [--recipe RECIPE]
    python scripts/spec_from_snapshot.py --workspace workspaces/<name>
"""

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec.snapshot_to_spec import (                    # noqa: E402
    load_snapshot, reduce_snapshot, to_yaml,
)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("snapshot", nargs="?", help="path to model_snapshot.json")
    parser.add_argument("--workspace", help="workspace dir holding results/state/")
    parser.add_argument("-o", "--out", help="write the spec here (default: stdout)")
    parser.add_argument("--name", default="", help="spec name")
    parser.add_argument("--recipe", default="", help="recipe name")
    parser.add_argument("--report", action="store_true",
                        help="print the exact/approximate/missing breakdown")
    args = parser.parse_args(argv)

    path = _resolve(args, parser)
    try:
        snapshot = load_snapshot(path)
    except (OSError, ValueError) as exc:
        print(f"FAIL: spec_from_snapshot unreadable — {exc}")
        return 1

    reduction = reduce_snapshot(snapshot, name=args.name, recipe=args.recipe)
    text = to_yaml(reduction.spec)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)

    if args.report:
        for label, entries in (("exact", reduction.exact),
                               ("approximate", reduction.approximate),
                               ("missing", reduction.missing),
                               ("notes", reduction.notes)):
            if entries:
                sys.stderr.write(f"\n  {label}:\n")
                for entry in entries:
                    sys.stderr.write(f"    - {entry}\n")
        sys.stderr.write("\n")

    verdict = "PASS" if not reduction.missing else "PARTIAL"
    sys.stderr.write(f"{verdict}: spec_from_snapshot {reduction.summary}\n")
    return 0


def _resolve(args, parser) -> Path:
    if args.workspace:
        return Path(args.workspace) / "results" / "state" / "model_snapshot.json"
    if args.snapshot:
        return Path(args.snapshot)
    parser.error("give a snapshot path or --workspace")


if __name__ == "__main__":
    raise SystemExit(main())
