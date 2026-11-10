"""Read the two QA signals the S11 stage does not: convergence and port Z0.

Read-only apart from the reused `AgentReadout_*` report (see read_results).
Both reads are best-effort and reported as unreadable rather than raised.

Usage (workspace root):  python src/10_convergence_port.py
Prints one Verification line:  PASS: convergence_port ...
"""

import os

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

RESULTS = ws_common.RESULTS
SETUP = "Setup1"


def main():
    hfss = ws_common.attach()
    os.makedirs(RESULTS, exist_ok=True)

    conv_note = "unreadable"
    out = os.path.join(RESULTS, "convergence.txt")
    try:
        written = hfss.export_convergence(SETUP, output_file=out)
        path = written if isinstance(written, str) and os.path.isfile(written) else out
        if os.path.isfile(path):
            text = open(path, encoding="utf-8", errors="replace").read()
            rows = [l for l in text.splitlines() if l.strip()]
            print("convergence table (%s):" % os.path.basename(path), flush=True)
            for line in rows[-14:]:
                print("   " + line[:160], flush=True)
            conv_note = "exported rows=%d" % len(rows)
    except Exception as exc:                 # noqa: BLE001 - reported, not raised
        conv_note = "unreadable: %s: %s" % (type(exc).__name__, str(exc)[:160])

    z_note = "unreadable"
    try:
        x, y, note = read_results.read_via_report(
            hfss, "re(Zo(P1))", sweep="Setup1 : Sweep1", export_dir=RESULTS)
        if y:
            pick = {}
            for f, v in zip(x, y):
                for target in (1.0, 3.0, 6.0):
                    if abs(f - target) < 0.006:
                        pick[target] = v
            z_note = " ".join("%.0fGHz=%.2fohm" % kv for kv in sorted(pick.items()))
            z_note += " min=%.2f max=%.2f" % (min(y), max(y))
        else:
            z_note = "unreadable: %s" % note[:200]
    except Exception as exc:                 # noqa: BLE001 - reported, not raised
        z_note = "unreadable: %s: %s" % (type(exc).__name__, str(exc)[:160])

    print("PASS: convergence_port convergence=[%s] port_Zo=[%s]" % (conv_note, z_note),
          flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
