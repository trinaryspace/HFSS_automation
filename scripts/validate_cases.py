"""Validate every canonical case that has a `design.yaml`. Tier 0.

The regression set exists so acceptance is not N=1 (ticket 05), and this is the
cheap tier of it: every spec in `knowledge/cases/*/design.yaml` must load and
validate clean, in milliseconds, with no license. A case with no spec yet is
reported rather than skipped silently — the count of cases still lacking one is
how far phase 2 has actually got.

Usage:
    python scripts/validate_cases.py [--verbose]
"""

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec.loader import SpecLoadError, load_spec       # noqa: E402
from hfss_spec.validate import validate                     # noqa: E402

CASES = REPO / "knowledge" / "cases"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    if not CASES.is_dir():
        print("FAIL: validate_cases no knowledge/cases directory")
        return 1

    directories = sorted(p for p in CASES.iterdir()
                         if p.is_dir() and not p.name.startswith("_"))
    failed, without, warnings = [], [], 0
    for directory in directories:
        path = directory / "design.yaml"
        if not path.exists():
            without.append(directory.name)
            continue
        try:
            spec = load_spec(path)
        except SpecLoadError as exc:
            failed.append(directory.name)
            print(f"  {directory.name}: does not load")
            if args.verbose:
                print(exc.report.text())
            continue
        except (OSError, ValueError) as exc:
            failed.append(directory.name)
            print(f"  {directory.name}: unreadable — {exc}")
            continue
        report = validate(spec)
        warnings += len(report.warnings)
        status = "ok" if report.ok else "FAILED"
        if not report.ok:
            failed.append(directory.name)
        if args.verbose or not report.ok:
            print(f"  {directory.name:<22} {status:<8} "
                  f"errors={len(report.errors)} warnings={len(report.warnings)}")
            if not report.ok:
                print(report.text())

    if without:
        # Not a failure: the schema is still growing into the case set, and
        # saying which cases lack a spec is the honest progress metric.
        print(f"  no design.yaml yet: {', '.join(without)}")
    total = len(directories) - len(without)
    verdict = "FAIL" if failed else "PASS"
    print(f"{verdict}: validate_cases specs={total} failed={len(failed)} "
          f"warnings={warnings} without_spec={len(without)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
