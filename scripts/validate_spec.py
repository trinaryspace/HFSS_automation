"""Validate a `design.yaml` offline. No AEDT, no license, milliseconds.

Ticket 08's entry point. The economic argument in one command: the errors this
catches are the ones that otherwise cost a desktop launch, a failed stage, a
traceback read and a self-correction round.

Usage:
    python scripts/validate_spec.py knowledge/cases/patch-2400/design.yaml
    python scripts/validate_spec.py <spec> --schema        # dump JSON Schema
    python scripts/validate_spec.py <spec> --quiet         # summary line only

Exit code is 0 only when there are no errors, so it is usable as a gate.
"""

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec.loader import SpecLoadError, load_spec       # noqa: E402
from hfss_spec.schema import json_schema_text               # noqa: E402
from hfss_spec.validate import validate                     # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("spec", nargs="?", help="path to a design.yaml")
    parser.add_argument("--schema", action="store_true",
                        help="print the JSON Schema and exit")
    parser.add_argument("--quiet", action="store_true",
                        help="print only the summary line")
    args = parser.parse_args(argv)

    if args.schema:
        sys.stdout.write(json_schema_text())
        return 0
    if not args.spec:
        parser.error("give a spec path, or --schema")

    try:
        spec = load_spec(args.spec)
    except SpecLoadError as exc:
        # A spec that does not fit the schema never reaches the other checks;
        # reporting both would just be noise on top of a shape error.
        sys.stdout.write(exc.report.summary() + "\n" if args.quiet
                         else exc.report.text())
        return 1
    except (OSError, ValueError) as exc:
        print(f"FAIL: validate_spec unreadable — {exc}")
        return 1

    report = validate(spec)
    sys.stdout.write(report.summary() + "\n" if args.quiet else report.text())
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
