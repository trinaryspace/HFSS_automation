#!/usr/bin/env python
"""Render a design.yaml to a PNG — no licence, no AEDT, about a second.

    python scripts/preview_spec.py workspaces/<name>/design.yaml
    python scripts/preview_spec.py <spec> -o preview.png --text

The point is wall-clock, not tokens. The Review gate is the check that actually
finds defects in this tool, and today the only way to reach it is a licence
check, an AEDT launch and a full compile — paid again on every correction round.
This puts the same geometry in front of a person, or in front of the agent, in
about a second.

Use it **before** `compile_spec --launch`, and again after every geometry edit.
It is not a substitute for the AEDT Review gate (ADR 0003): it draws axis-
aligned bounding boxes, so a rotated or lofted body is reported as undrawn
rather than guessed at. It is the cheap first look that makes the expensive one
a confirmation.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec import preview                                       # noqa: E402
from hfss_spec.loader import load_spec                              # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", type=Path, help="path to design.yaml")
    ap.add_argument("-o", "--out", type=Path, default=None,
                    help="output PNG (default: <spec dir>/preview.png)")
    ap.add_argument("--text", action="store_true",
                    help="also print the findings as text")
    ap.add_argument("--no-image", action="store_true",
                    help="skip the PNG; print the text report only")
    ap.add_argument("--dpi", type=int, default=130)
    args = ap.parse_args(argv)

    spec = load_spec(args.spec)
    scope = preview.resolve_scope(spec)

    if args.no_image:
        data = preview.collect(spec, scope)
    else:
        out = args.out or args.spec.parent / "preview.png"
        data = preview.render(spec, scope, out, dpi=args.dpi)
        print("wrote %s" % out)

    if args.text or args.no_image:
        print(preview.text_report(data))

    # Exit 0 always: this is a look, not a gate. The gates are validate_spec
    # and precheck, and a preview that could fail a build would start being
    # argued with instead of looked at.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
