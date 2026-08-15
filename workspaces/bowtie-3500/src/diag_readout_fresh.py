"""Fresh-session readout attempt (EC#6 route-around: re-attach (fresh
session) for reads; the solving session's readout is unreliable)."""

import sys
import time

from ws_common import PROJECT, DESIGN, attach, exit_keep_alive, read_state


def main() -> int:
    from ansys.aedt.core import Desktop

    Desktop(version="2024.1", new_desktop=False, port=int(read_state("aedt_port")))

    hfss = attach(launch=False)  # fresh python process -> fresh client session
    try:
        print("setups:", [s.name for s in hfss.setups], flush=True)
    except Exception as e:  # noqa: BLE001
        print("setups read failed:", type(e).__name__, str(e)[:200], flush=True)

    sweeps = (read_state("sweeps") or "").split(",")
    sweep = next((s for s in sweeps if "Sweep" in s), None)
    print("sweep:", sweep, flush=True)

    for expr in ["dB(S(P1WavePort,P1WavePort))", "S(P1WavePort,P1WavePort)", "VSWR(P1WavePort)"]:
        data = None
        for i in range(3):
            try:
                data = hfss.post.get_solution_data(expressions=expr, setup_sweep_name=sweep)
            except Exception as e:  # noqa: BLE001
                print(f"  {expr}: try {i+1} exception {type(e).__name__} {str(e)[:120]}", flush=True)
                data = None
            if data is not None and data.data_real() is not None and len(data.data_real()) > 0:
                break
            time.sleep(8)
        if data is not None and data.data_real() is not None and len(data.data_real()) > 0:
            xs = list(data.primary_sweep_values)
            ys = list(data.data_real())
            print(f"{expr}: OK points={len(xs)} min={min(ys):.3f} @ {xs[ys.index(min(ys))]}", flush=True)
        else:
            print(f"{expr}: UNFILLED", flush=True)
    print("DONE fresh-session probe", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
