"""Stage 8: setup + sweep.

Setup1: adaptive at 3.5 GHz (paper baseline resonance ~3.46-3.55 GHz),
MaxPasses 15, MaxDeltaS 0.02. Linear-count sweep 3.2-4.2 GHz, 201 points,
discrete (the proven sweep shape, EC#6).
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    setup = hfss.create_setup("Setup1")
    setup.props["Frequency"] = "3.5GHz"
    setup.props["MaxPasses"] = 15
    setup.props["MaxDeltaS"] = 0.02
    setup.update()
    print("setup:", setup.name, setup.props.get("Frequency"), setup.props.get("MaxPasses"), flush=True)

    hfss.create_linear_count_sweep(
        setup=setup.name, unit="GHz", start_frequency=3.2, stop_frequency=4.2, num_of_freq_points=201
    )
    sweeps = list(hfss.existing_analysis_sweeps)
    print("existing_analysis_sweeps:", sweeps, flush=True)
    write_state("sweeps", ",".join(sweeps))
    assert sweeps, "no sweep visible"
    print("STAGE_OK setup+sweep", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
