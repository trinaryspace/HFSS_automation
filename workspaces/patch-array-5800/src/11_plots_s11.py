"""One-shot delivered plots for the fed array (solve #2's readouts).

Policy (SKILL.md): one scripted attempt per signal + one retry on a fresh
attach, then UI arbitration. The channel was recycled (fresh desktop), so
the GetVariables flake of the old session may be gone; if it is not, the
verdicts here say "unreadable" and the user's UI numbers stand.

Deliverables:
    results/s11_fed.csv       F, dB(S(1,1))
    results/s11_fed.png       (best effort; requires matplotlib)
    results/state/readouts.txt  one line per signal verdict
"""

import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(HERE))))

from ws_common import RESULTS, STATE, attach, exit_keep_alive  # noqa: E402
import read_results  # noqa: E402


def main():
    verdicts = []
    hfss = attach(launch=False)
    print("design:", hfss.design_name, flush=True)
    sweep = read_results.resolve_sweep(hfss, setup="Setup1")
    if sweep is None:
        verdicts.append("s11: unreadable - no sweep on the design")
        _write_verdicts(verdicts)
        exit_keep_alive()

    xs, ys, note = read_results.read_expression(hfss, "dB(S(1,1))", sweep=sweep)
    if ys:
        path = os.path.join(RESULTS, "s11_fed.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["freq_GHz", "dB_S11"])
            for x, y in zip(xs, ys):
                try:
                    w.writerow([float(x) / 1e9 if abs(float(x)) > 1e6 else float(x), y])
                except (ValueError, TypeError):
                    w.writerow([x, y])
        # best-effort PNG
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(8, 5))
            fx = [float(x) / 1e9 if abs(float(x)) > 1e6 else float(x) for x in xs]
            ax.plot(fx, ys, "-o", markersize=3)
            ax.set_xlabel("freq (GHz)"); ax.set_ylabel("dB(S(1,1))")
            ax.axvline(5.8, color="red", ls="--", lw=0.8)
            ax.set_title("patch-array-5800 - fed array S11 (solve #2)")
            ax.grid(True)
            fig.savefig(os.path.join(RESULTS, "s11_fed.png"), dpi=120)
            plt.close(fig)
        except Exception as exc:  # noqa: BLE001 - png is best-effort
            print("png skipped:", type(exc).__name__, flush=True)
        # resonance + depth from the data
        try:
            best = min(range(len(ys)), key=lambda k: ys[k])
            res_f, depth = fx[best], ys[best]
        except Exception:  # noqa: BLE001
            res_f, depth = float("nan"), float("nan")
        verdicts.append("s11: read %d points; dip %.2f GHz at %.2f dB (note: %s)"
                        % (len(ys), res_f, depth, note))
        print("PASS: s11_fed readout -> %s" % path, flush=True)
    else:
        verdicts.append("s11: unreadable - %s" % note)

    _write_verdicts(verdicts)
    return 0


def _write_verdicts(verdicts):
    os.makedirs(STATE, exist_ok=True)
    with open(os.path.join(STATE, "readouts.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(verdicts) + "\n")
    for v in verdicts:
        print(v, flush=True)


if __name__ == "__main__":
    main()
    exit_keep_alive()
