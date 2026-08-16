"""Stage-script skeleton — the verification contract, spelled out.

One Stage = one script = one Run. A real stage script is this skeleton's
shape, with the `<PLACEHOLDER>`s replaced by the stage's actual work:

1. Attach (or, rarely, launch) through ws_common — the puck is port-pinned.
2. DELETE-THEN-CREATE (ADR 0008): delete every object, boundary,
   excitation, mesh operation, and sweep this stage (re)creates BEFORE
   creating it, so re-running the stage in place always converges (never
   wipe-and-rebuild; that is an explicit escalation only).
3. Do the stage work; write one machine-state file per completion signal
   via `write_state`.
4. End with exactly ONE Verification line of the form
   `PASS: <stage> <assertions>` plus `exit_keep_alive()` (desktop stays
   alive for the next stage). On failure: `STAGE_FAILED` + the exception.
5. The static gate (`00_static_gate.py`) must run clean before any AEDT
   launch: py_compile + import-check of every src/*.py.

This file itself is runnable (it exercises the attach + Verification-line
contract) but is not part of any replay set.
"""

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    # delete-then-create (ADR 0008): delete the objects this stage makes,
    # then create them; never build on a dirty project.
    write_state("stage_<name>", "done")
    assertions = "<objects exist | bbox sane | validate_simple()>"
    print("PASS: <stage> " + assertions, flush=True)
    return hfss is not None and 0 or 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
