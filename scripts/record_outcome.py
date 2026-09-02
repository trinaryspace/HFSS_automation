"""Record what the run delivered, in the form the run card can read.

    python scripts/record_outcome.py --workspace workspaces/<name> \
        --outcome completed --completions 2 --note "tuning issue, not a feed defeat"

Writes `results/state/outcome.txt` as key=value lines — `outcome=`,
`completions=`, optionally `escape_hatch_scripts=` and `note=`, plus
`recorded_at=` (epoch seconds) — which is exactly what `scripts/run_card.py`'s
`Outcome` parses. The last run wrote this file by hand as free text
(`completed - user verdict: ...`) and the card read it as `unrecorded`; this
script is the writer that cannot get the form wrong, and it refuses anything
that is not one of the three outcome words.

Outcome words: `completed` (something solved and was read), `escalated` (the
run stopped on a question the user has to answer), `abandoned` (nothing
delivered). `completions` is how many simulations the run actually delivered
(default 1 when completed, else 0); a completed run with none is refused as a
contradiction. Re-recording replaces the file — the outcome is the run's final
verdict, not a log.

One `PASS:` line on success; a `FAIL:` line and exit 1 on malformed input,
with nothing written.
"""

import argparse
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_card import OUTCOME_COMPLETED, OUTCOME_FILE, OUTCOMES  # noqa: E402


def fail(message):
    print(f"FAIL: record_outcome {message}")
    return 1


def _int(raw, name):
    """A non-negative int, or a FAIL message."""
    try:
        value = int(str(raw).strip())
    except (TypeError, ValueError):
        return None, f"{name} must be an integer, got {raw!r}"
    if value < 0:
        return None, f"{name} must not be negative, got {value}"
    return value, None


def render(outcome, completions, escape_hatch=None, note="", recorded_at=None):
    """The key=value text; validated before it is written."""
    lines = [f"outcome={outcome}", f"completions={completions}"]
    if escape_hatch is not None:
        lines.append(f"escape_hatch_scripts={escape_hatch}")
    if note:
        lines.append(f"note={note}")
    lines.append(f"recorded_at={time.time() if recorded_at is None else recorded_at}")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspace", help="workspace dir; the file lands in results/state/")
    parser.add_argument("--outcome", help="one of: " + ", ".join(OUTCOMES))
    parser.add_argument("--completions", help="simulations actually delivered "
                                              "(default 1 when completed, else 0)")
    parser.add_argument("--escape-hatch", dest="escape_hatch",
                        help="stage scripts written outside the compiler")
    parser.add_argument("--note", default="", help="one line, the user's verdict verbatim")
    args = parser.parse_args(argv)

    if not args.workspace:
        return fail("needs --workspace")
    workspace = Path(args.workspace)
    if not workspace.is_dir():
        return fail(f"workspace is not a directory: {workspace}")
    outcome = (args.outcome or "").strip()
    if outcome not in OUTCOMES:
        return fail(f"outcome must be one of {', '.join(OUTCOMES)}; got {args.outcome!r}")
    if args.completions is None:
        completions = 1 if outcome == OUTCOME_COMPLETED else 0
    else:
        completions, error = _int(args.completions, "completions")
        if error:
            return fail(error)
    if outcome == OUTCOME_COMPLETED and completions == 0:
        return fail("outcome=completed with completions=0 is a contradiction; "
                    "record escalated or abandoned, or say how many completed")
    escape_hatch = None
    if args.escape_hatch is not None:
        escape_hatch, error = _int(args.escape_hatch, "escape-hatch")
        if error:
            return fail(error)
    note = args.note.strip()
    if "\n" in note or "\r" in note:
        return fail("note must be one line")

    state = workspace / "results" / "state"
    os.makedirs(state, exist_ok=True)
    target = state / OUTCOME_FILE
    target.write_text(render(outcome, completions, escape_hatch, note), encoding="utf-8")
    print(f"PASS: record_outcome outcome={outcome} completions={completions} "
          f"file={target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
