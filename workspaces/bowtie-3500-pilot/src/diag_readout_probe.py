"""DIAGNOSTIC (not a stage): readout probe kept for EC#6 archaeology.

Not part of the replay set (no NN_ prefix). Retry-shaped readout used to
characterize the flaky solution-data surface during the pilot; the pilot's
README readout policy is now single-shot-then-UI, so this is reference
material only. Ends with a DONE line, not a PASS line — it is not a stage.
"""

import sys
import time

sys.path.insert(0, "src")
from ws_common import attach, exit_keep_alive, read_state


def main():
    hfss = attach(launch=False)
    sweeps = (read_state("sweeps") or "").split(",")
    sweep = next((s for s in sweeps if "Sweep" in s), None)
    print("sweep:", sweep, flush=True)
    exprs = ["dB(S(1,1))", "S(1,1)", "dB(S('1','1'))", "VSWR(1)"]
    for expr in exprs:
        data = None
        for i in range(3):
            try:
                data = hfss.post.get_solution_data(expressions=expr, setup_sweep_name=sweep)
            except Exception as e:  # noqa: BLE001
                print("  %s try %d exception %s %s" % (expr, i + 1, type(e).__name__, str(e)[:110]), flush=True)
                data = None
            if data is not None:
                dr = getattr(data, "data_real", None)
                if dr is not None and len(list(dr or [])) and len(list(dr[0] or [])):
                    break
                print("  %s unfilled data" % expr, flush=True)
            time.sleep(8)
        if data is not None:
            dr = getattr(data, "data_real", None)
            if dr is not None and len(list(dr or [])) and len(list(dr[0] or [])):
                xs = list(getattr(data, "primary_sweep_values") or [])
                ys = [float(v) for v in dr[0]]
                imin = ys.index(min(ys))
                print("OK %s points=%d min=%.3f @ %.4f GHz" % (expr, len(xs), ys[imin], xs[imin]), flush=True)
                with open("results/s11_raw.txt", "w") as f:
                    for x, y in zip(xs, ys):
                        f.write("%.9f %.9f\n" % (x, y))
                continue
        print("%s: UNFILLED" % expr, flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
