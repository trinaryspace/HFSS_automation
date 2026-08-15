"""Diagnose the solve outcome left by stage 08's poll timeout.

The .sd/.SU sweep files live one level below the top of the results dir, so
the stage-08 poll (non-recursive glob) could not see them and timed out at
45 min even though the solver finished/stopped ~2.5 min after submission.
This probe re-attaches and reads the authoritative surfaces: adaptive
convergence and the S11 readout.
"""

import sys
import time

from ws_common import attach, exit_keep_alive, read_state


def main() -> int:
    hfss = attach(launch=False)
    setup = hfss.setups[0]
    print("setup name:", setup.name, flush=True)
    try:
        conv = setup.get_convergence()
        print("convergence entries:", len(conv), flush=True)
        for c in conv[-8:]:
            print("  ", c, flush=True)
    except Exception as e:  # noqa: BLE001
        print("get_convergence failed:", type(e).__name__, str(e)[:200], flush=True)

    sweeps = (read_state("sweeps") or "").split(",")
    sweep = next((s for s in sweeps if "Sweep" in s), None)
    print("sweep:", sweep, flush=True)

    data = None
    for i in range(4):
        try:
            data = hfss.post.get_solution_data(expressions="dB(S(P1WavePort,P1WavePort))", setup_sweep_name=sweep)
        except Exception as e:  # noqa: BLE001
            print(f"  try {i+1} readout exception: {type(e).__name__} {str(e)[:120]}", flush=True)
            data = None
        if data is not None and data.data_real() is not None and len(data.data_real()) > 0:
            break
        print(f"  try {i+1}: unfilled; wait 10s", flush=True)
        time.sleep(10)
    if data is not None and data.data_real() is not None and len(data.data_real()) > 0:
        xs = list(data.primary_sweep_values)
        ys = list(data.data_real())
        print("S11 READOUT OK points =", len(xs), flush=True)
        print("S11 min =", min(ys), "at", xs[ys.index(min(ys))], flush=True)
    else:
        print("S11 READOUT UNFILLED (flaky, EC#6)", flush=True)
    print("DONE probe", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
