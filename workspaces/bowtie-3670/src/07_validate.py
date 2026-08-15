"""Stage 9: validation gate (EC#8) — validate_simple() must return True."""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    hfss.save_project()
    valid = bool(hfss.validate_simple())
    print("validate_simple:", valid, flush=True)
    write_state("validated", str(valid))
    print("STAGE_OK validation" if valid else "STAGE_FAILED validation", flush=True)
    return 0 if valid else 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
