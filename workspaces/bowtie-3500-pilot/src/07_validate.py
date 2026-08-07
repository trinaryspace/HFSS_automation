"""Stage 7: validation gate (EC#8) — validate_simple() must return True."""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    hfss.save_project()
    valid = bool(hfss.validate_simple())
    print("validate_simple:", valid, flush=True)
    write_state("validated", str(valid))
    assert valid, "validate_simple() is False — design invalid (EC#8)"
    print("PASS: validation validate_simple() returns True", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
