"""Closed-form physics pre-check on a `design.yaml`. Ticket 09, offline.

    python scripts/precheck.py knowledge/cases/patch-2400/design.yaml

Prints the estimator's inputs, the target, the prediction and the signed
disagreement. It **never blocks**: the exit code is 0 even on an inconsistent
verdict, because the user arbitrates which reading is canonical and the choice
is recorded in the spec's `provenance.canonical_reading`. Use `--strict` when
you want a nonzero exit for scripting.
"""

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec import physics                              # noqa: E402
from hfss_spec.loader import SpecLoadError, load_spec      # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("spec")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero on an inconsistent verdict")
    args = parser.parse_args(argv)

    try:
        spec = load_spec(args.spec)
    except SpecLoadError as exc:
        sys.stdout.write(exc.report.text())
        return 1
    except (OSError, ValueError) as exc:
        print(f"FAIL: precheck unreadable — {exc}")
        return 1

    result = physics.check(spec)
    sys.stdout.write("\n" + result.text())
    if args.strict and result.verdict == "INCONSISTENT":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
