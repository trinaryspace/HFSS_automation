"""Shared readout: fetch S11 data with a short retry window for solve-data lag."""

import time


def fetch_s11_db(hfss, timeout=60):
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        sweeps = list(hfss.existing_analysis_sweeps) or ["nominal_adaptive"]
        for name in sweeps:
            try:
                data = hfss.post.get_solution_data(expressions="dB(S(1,1))", setup_sweep_name=name)
                if data is not None and not isinstance(data, bool) and hasattr(data, "data_real"):
                    try:
                        if data.data_real():
                            return data
                    except Exception:  # noqa: BLE001
                        pass
            except Exception as e:  # noqa: BLE001
                last = e
        time.sleep(5)
    return last if last is not None else RuntimeError("no data within timeout")


def s11_summary(data):
    freqs = [float(f) for f in data.primary_sweep_values]
    vals = data.data_real()
    idx_2p4 = min(range(len(freqs)), key=lambda i: abs(freqs[i] - 2.4))
    return round(min(vals), 2), round(vals[idx_2p4], 2)
