"""One-shot delivered plots for the fed array (solve #2's readouts).

Policy (SKILL.md): one scripted attempt per signal, then ONE escalation per
run to a genuinely fresh desktop PROCESS, then UI arbitration.

The retry has to be a fresh process, not a fresh attach. `attach()`
reconnects by the pinned port, and the bounded connect clears the pin only
for a desktop that is *dead* — a degraded-but-still-answering desktop passes
it, so the retry lands back on the same sick channel and the channel-lifetime
question is never actually asked. That is how this run's first pass concluded
"scripted readouts fail systematically over this pairing" from two
`GrpcApiError`s on `GetVariables` / `GetPropValue`, while its own ledger
recorded that recycling the desktop had already cured that exact error class
earlier the same day. `ws_common.recycle_desktop` is the escalation;
`read_results.ReadoutSession` spends it exactly once per run.

Deliverables:
    results/s11_fed.csv         F, dB(S(1,1))
    results/s11_fed.png         (best effort; requires matplotlib)
    results/state/readouts.txt  one verdict line per signal, carrying the
                                route token that separates the outcomes:
                                `live-channel` (read on the channel the run
                                had), `fresh-process` (channel degradation
                                CONFIRMED), `both-failed` (systematic on
                                this pairing), `untested` (no fresh process
                                ran, so nothing was proved either way).
"""

import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(HERE))))

from ws_common import RESULTS, STATE, attach, exit_keep_alive, recycle_desktop  # noqa: E402
import read_results  # noqa: E402


def main():
    read_results.apply_route_arounds()
    hfss = attach(launch=False)
    try:
        print("design:", hfss.design_name, flush=True)
    except Exception as exc:  # noqa: BLE001 - a design-name read is not the readout
        # `design_name` is a generic desktop call, the same class as the
        # GetVariables / GetPropValue failures this stage exists to diagnose.
        # Letting it kill the script here would end the run before the
        # escalation that answers the question.
        print("design: unreadable on this channel (%s) - continuing to the readout"
              % type(exc).__name__, flush=True)

    session = read_results.ReadoutSession(hfss, recycle=recycle_desktop)
    s11 = session.read("dB(S(1,1))", setup="Setup1")
    verdicts = [read_results.verdict_line("s11", s11)]

    if s11.y:
        path = os.path.join(RESULTS, "s11_fed.csv")
        fx = []
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["freq_GHz", "dB_S11"])
            for x, y in zip(s11.x, s11.y):
                try:
                    ghz = float(x) / 1e9 if abs(float(x)) > 1e6 else float(x)
                except (ValueError, TypeError):
                    w.writerow([x, y])
                    continue
                fx.append(ghz)
                w.writerow([ghz, y])
        # best-effort PNG
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(fx, s11.y, "-o", markersize=3)
            ax.set_xlabel("freq (GHz)"); ax.set_ylabel("dB(S(1,1))")
            ax.axvline(5.8, color="red", ls="--", lw=0.8)
            ax.set_title("patch-array-5800 - fed array S11 (solve #2)")
            ax.grid(True)
            fig.savefig(os.path.join(RESULTS, "s11_fed.png"), dpi=120)
            plt.close(fig)
        except Exception as exc:  # noqa: BLE001 - png is best-effort
            print("png skipped:", type(exc).__name__, flush=True)
        # resonance + depth from the data
        if fx:
            best = min(range(len(s11.y)), key=lambda k: s11.y[k])
            verdicts.append("s11_dip: %.2f GHz at %.2f dB (%d points, read by the "
                            "route above)" % (fx[best], s11.y[best], len(s11.y)))
        print("PASS: s11_fed readout -> %s" % path, flush=True)

    read_results.write_readouts(STATE, verdicts)
    return 0


if __name__ == "__main__":
    main()
    exit_keep_alive()
