"""Stage 8 (ver.2): setup + sweep — interpolating sweep (antenna standard).

Run #1 used a 201-point DISCRETE sweep; the solver stalled repeatedly after
adaptivity (melded 201 points, wrote zero sweep .sd — three freezes at the
same plateau). Interpolating sweeps solve a handful of points and interpolate
the band — the standard choice for antenna S11 curves.
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

    # remove any prior (discrete) sweep so the record is single-sweep
    for sname in list(hfss.existing_analysis_sweeps):
        if "Sweep" in sname:
            setup.delete_sweep(sname.split(":")[-1].strip())
            print("deleted old sweep:", sname, flush=True)

    hfss.create_linear_count_sweep(
        setup=setup.name,
        unit="GHz",
        start_frequency=3.2,
        stop_frequency=4.2,
        num_of_freq_points=201,
        sweep_type="Interpolating",
        interpolation_tol=0.5,
        interpolation_max_solutions=50,
        save_fields=False,
    )
    sweeps = list(hfss.existing_analysis_sweeps)
    print("existing_analysis_sweeps:", sweeps, flush=True)
    write_state("sweeps", ",".join(sweeps))
    assert any("Sweep" in s for s in sweeps), "no sweep visible"
    print("STAGE_OK setup+interpolating sweep", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
