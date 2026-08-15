"""Stage 6: setup + sweep.

Setup1: adaptive at 2.4 GHz (the Recipe target), MaxPasses 15, MaxDeltaS
0.02. Linear-count DISCRETE sweep 2.0-3.0 GHz, 201 points (the proven
sweep shape, EC#6). create_linear_count_sweep auto-suffixes the real sweep
name — read back from existing_analysis_sweeps before any report uses it.
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)

    # delete-then-create (ADR 0008): drop the sweeps and setups we (re)create.
    for s in list(hfss.existing_analysis_sweeps or []):
        if ":" not in s:
            continue
        setup_name, sweep_name = (p.strip() for p in s.split(":", 1))
        setup = next((st for st in (hfss.setups or []) if st.name == setup_name), None)
        if setup is not None:
            setup.delete_sweep(sweep_name)
            print("deleted sweep:", s, flush=True)
    for setup in list(hfss.setups or []):
        hfss.delete_setup(setup.name)
        print("deleted setup:", setup.name, flush=True)

    setup = hfss.create_setup("Setup1")
    setup.props["Frequency"] = "2.4GHz"
    setup.props["MaxPasses"] = 15
    setup.props["MaxDeltaS"] = 0.02
    setup.update()
    print("setup:", setup.name, setup.props.get("Frequency"),
          setup.props.get("MaxPasses"), setup.props.get("MaxDeltaS"), flush=True)

    hfss.create_linear_count_sweep(
        setup=setup.name, unit="GHz", start_frequency=2.0, stop_frequency=3.0,
        num_of_freq_points=201,
    )
    sweeps = list(hfss.existing_analysis_sweeps or [])
    print("existing_analysis_sweeps:", sweeps, flush=True)
    write_state("sweeps", ",".join(sweeps))
    assert any("Sweep" in s for s in sweeps), "no sweep visible"
    print("PASS: setup Setup1 2.4GHz/15pass/dS0.02, sweeps %s" % sweeps, flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
