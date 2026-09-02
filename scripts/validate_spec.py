"""Validate a `design.yaml` offline. No AEDT, no license, milliseconds.

Ticket 08's entry point. The economic argument in one command: the errors this
catches are the ones that otherwise cost a desktop launch, a failed stage, a
traceback read and a self-correction round.

Usage:
    python scripts/validate_spec.py knowledge/cases/patch-2400/design.yaml
    python scripts/validate_spec.py <spec> --schema        # dump JSON Schema
    python scripts/validate_spec.py <spec> --quiet         # summary line only

Exit code is 0 only when there are no errors, so it is usable as a gate.

The summary line is also a `gate.validate_spec` event in the workspace's
`results/state/events.jsonl` (run logging, ticket 03). The workspace is
`--workspace`, or by default the spec's own directory — a spec that lives
in a workspace is logged there; a spec under `knowledge/cases/` has no
state dir, so nothing is written.
"""

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec import events                                # noqa: E402
from hfss_spec.loader import SpecLoadError, load_spec       # noqa: E402
from hfss_spec.schema import json_schema_text               # noqa: E402
from hfss_spec.validate import validate                     # noqa: E402


def state_dir_for(spec_path, workspace=None) -> Path:
    """`<workspace>/results/state`, the workspace defaulting to the spec's dir."""
    root = Path(workspace) if workspace else Path(spec_path).resolve().parent
    return root / "results" / "state"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("spec", nargs="?", help="path to a design.yaml")
    parser.add_argument("--schema", action="store_true",
                        help="print the JSON Schema and exit")
    parser.add_argument("--quiet", action="store_true",
                        help="print only the summary line")
    parser.add_argument("--workspace",
                        help="workspace whose results/state/events.jsonl records "
                             "the gate (default: the spec's directory)")
    args = parser.parse_args(argv)

    if args.schema:
        sys.stdout.write(json_schema_text())
        return 0
    if not args.spec:
        parser.error("give a spec path, or --schema")
    state_dir = state_dir_for(args.spec, args.workspace)

    try:
        spec = load_spec(args.spec)
    except SpecLoadError as exc:
        # A spec that does not fit the schema never reaches the other checks;
        # reporting both would just be noise on top of a shape error.
        sys.stdout.write(exc.report.summary() + "\n" if args.quiet
                         else exc.report.text())
        events.emit(state_dir, "gate.validate_spec", verdict=exc.report.summary(),
                    detail=f"spec={args.spec}")
        return 1
    except (OSError, ValueError) as exc:
        line = f"FAIL: validate_spec unreadable — {exc}"
        print(line)
        events.emit(state_dir, "gate.validate_spec", verdict=line,
                    detail=f"spec={args.spec}")
        return 1

    report = validate(spec)
    sys.stdout.write(report.summary() + "\n" if args.quiet else report.text())
    events.emit(state_dir, "gate.validate_spec", verdict=report.summary(),
                detail=f"spec={spec.name}")
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
