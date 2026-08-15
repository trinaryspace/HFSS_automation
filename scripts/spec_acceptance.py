"""Compiler acceptance against a stored snapshot. Ticket 11, Tier 1.

Compile a `design.yaml` onto a desktop, capture the result, and diff it against
the model the old path produced. No solve, so it runs in minutes.

    python scripts/spec_acceptance.py --workspace <dir> \
        --spec knowledge/cases/bowtie-3500/design.yaml \
        --reference workspaces/bowtie-3500-pilot/results/state/model_snapshot.json

`--offline` skips the desktop entirely and diffs two stored snapshots, which is
how the diff logic itself is regression-tested without a license.

Every residual difference is classified compiler bug / schema gap / capture gap
and printed, because an unclassified diff is not a finding.
"""

import argparse
import importlib.util
import json
import logging
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

os.environ.setdefault("PYAEDT_LOG_LEVEL", "WARNING")
logging.getLogger("Global").setLevel(logging.WARNING)

from hfss_spec import acceptance                                  # noqa: E402
from hfss_spec.compiler import BuildLog, CompileError, build      # noqa: E402
from hfss_spec.loader import SpecLoadError, load_spec             # noqa: E402


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--spec")
    parser.add_argument("--reference", required=True,
                        help="the model_snapshot.json the old path produced")
    parser.add_argument("--workspace")
    parser.add_argument("--offline", metavar="SNAPSHOT",
                        help="diff this stored snapshot instead of building")
    parser.add_argument("--bboxes", action="store_true",
                        help="also report per-object bbox deltas")
    args = parser.parse_args(argv)

    try:
        reference = json.loads(Path(args.reference).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"FAIL: spec_acceptance reference unreadable — {exc}")
        return 1

    if args.offline:
        built = json.loads(Path(args.offline).read_text(encoding="utf-8"))
    else:
        if not (args.spec and args.workspace):
            parser.error("give --spec and --workspace, or --offline SNAPSHOT")
        built = _build_and_capture(args)
        if built is None:
            return 1

    result = acceptance.compare(reference, built)
    sys.stdout.write(result.text())
    if args.bboxes:
        deltas = acceptance.bbox_deltas(reference, built)
        for name, delta in deltas.items():
            print(f"  bbox {name:<22} {delta}")
        print(f"  bbox objects differing: {len(deltas)}")
    return 0 if result.ok else 1


def _build_and_capture(args):
    workspace = Path(args.workspace)
    try:
        spec = load_spec(args.spec)
    except SpecLoadError as exc:
        sys.stdout.write(exc.report.text())
        return None

    ws = _load(workspace / "src" / "ws_common.py", "_ws_common")
    capture = _load(workspace / "src" / "capture_state.py", "_capture_state")
    hfss = ws.attach(launch=True)
    try:
        build(spec, hfss, BuildLog(emit=lambda line: print(line, flush=True)))
    except CompileError as exc:
        print(f"STAGE_FAILED: spec_acceptance {exc}")
        return None
    return capture.shape_from_model(hfss)


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    raise SystemExit(main())
