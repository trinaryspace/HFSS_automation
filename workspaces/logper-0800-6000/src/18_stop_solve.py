"""Stop the running solve on the pinned desktop. An emergency brake.

Used when the machine is about to run out of disk or memory: a solve that
dies because the system disk filled can take the project down with it, so a
deliberate stop is the safer failure. Never run it on a healthy solve.

    python src/18_stop_solve.py            # clean stop: finish the current step
    python src/18_stop_solve.py --abort    # stop immediately

Prints one Verification line:  PASS: stop_solve clean_stop=<bool> returned=<...>

API, from the installed pyAEDT 1.3.0 (application/analysis.py):
    stop_simulations(self, clean_stop: bool = True) -> str
"""

import sys

import ws_common


def main(argv):
    clean = "--abort" not in argv
    hfss = ws_common.attach()
    returned = hfss.stop_simulations(clean_stop=clean)
    import run_events
    line = "PASS: stop_solve clean_stop=%s returned=%r" % (clean, returned)
    print(line, flush=True)
    run_events.emit("solve.stopped", stage="solve", verdict=line,
                    state_dir=ws_common.STATE)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
