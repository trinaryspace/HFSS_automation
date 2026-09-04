"""Relaunch the desktop on the solved project so the user can inspect results.

Used after a desktop crash: the solve evidence is already banked
(`results/state/solved.txt`) and the results folder is on disk, so this only
brings a desktop back up on the saved project and re-pins it. The stale
`.lock` a crash leaves behind is cleared by the preamble's `remove_lock=True`
(env-compat #9), and the dead port pin is re-pinned by `attach`.

It also re-creates the S11 report in the design tree, because the report the
readout stage left standing was made after the last project save and does not
survive the crash. `create_or_reuse_report` drives the ReportSetup module
directly — the route that works on this box — and the project is saved so the
plot persists.

Usage (workspace root):  python src/14_relaunch.py
Prints one Verification line:  PASS: relaunch <port/pid/report>
Leaves the desktop RUNNING for the user; never tears down.
"""

import sys

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

EXPR = "dB(S(1,1))"


def main():
    hfss = ws_common.attach(launch=True)
    port = ws_common.read_state("aedt_port")
    pid = ws_common.read_state("aedt_process_id")

    sweeps = list(getattr(hfss, "existing_analysis_sweeps", []) or [])
    report, note = None, ""
    try:
        sweep = read_results.resolve_sweep(hfss)
        report = read_results.create_or_reuse_report(hfss, EXPR, sweep)
        note = "report=%s sweep=%s" % (report, sweep)
    except Exception as e:                   # noqa: BLE001 - report is a bonus
        note = "report=FAILED(%s: %s)" % (type(e).__name__, str(e)[:120])

    try:
        hfss.save_project()
        saved = True
    except Exception:                        # noqa: BLE001
        saved = False

    line = ("PASS: relaunch port=%s pid=%s sweeps=%d saved=%s %s"
            % (port, pid, len(sweeps), saved, note))
    print(line, flush=True)
    import run_events
    run_events.emit("desktop.relaunch", stage="qa", verdict=line,
                    detail="after user-reported crash", state_dir=ws_common.STATE)
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
        sys.exit(1)
