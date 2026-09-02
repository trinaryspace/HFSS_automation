"""Closed-form physics pre-check on a `design.yaml`. Ticket 09, offline.

    python scripts/precheck.py knowledge/cases/patch-2400/design.yaml

Prints the estimator's inputs, the target, the prediction and the signed
disagreement. It **never blocks**: the exit code is 0 even on an inconsistent
verdict, because the user arbitrates which reading is canonical and the choice
is recorded in the spec's `provenance.canonical_reading`. Use `--strict` when
you want a nonzero exit for scripting.

The verdict line (`PASS:` / `FAIL:` / `UNCHECKED:`) is also a `gate.precheck`
event in the workspace's `results/state/events.jsonl` (run logging, ticket
03); the workspace is `--workspace` or, by default, the spec's directory.
"""

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec import events, physics                      # noqa: E402
from hfss_spec.loader import SpecLoadError, load_spec      # noqa: E402


def state_dir_for(spec_path, workspace=None) -> Path:
    root = Path(workspace) if workspace else Path(spec_path).resolve().parent
    return root / "results" / "state"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("spec")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero on an inconsistent verdict")
    parser.add_argument("--workspace",
                        help="workspace whose results/state/events.jsonl records "
                             "the gate (default: the spec's directory)")
    args = parser.parse_args(argv)
    state_dir = state_dir_for(args.spec, args.workspace)

    try:
        spec = load_spec(args.spec)
    except SpecLoadError as exc:
        sys.stdout.write(exc.report.text())
        events.emit(state_dir, "gate.precheck", verdict=exc.report.summary(),
                    detail=f"spec={args.spec}")
        return 1
    except (OSError, ValueError) as exc:
        line = f"FAIL: precheck unreadable — {exc}"
        print(line)
        events.emit(state_dir, "gate.precheck", verdict=line, detail=f"spec={args.spec}")
        return 1

    result = physics.check(spec)
    text = result.text()
    sys.stdout.write("\n" + text)
    # The verdict is the text's last line — the one a reader greps for.
    events.emit(state_dir, "gate.precheck", verdict=text.strip().splitlines()[-1],
                detail=f"spec={spec.name} recipe={result.recipe} verdict={result.verdict}")
    if args.strict and result.verdict == "INCONSISTENT":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
