"""Stage 6: setup + sweep — delete-then-create (ADR 0008).

Setup1: adaptive at 3.5 GHz, MaxPasses 15, MaxDeltaS 0.02 (paper baseline
resonance 3.46-3.55 GHz). Linear-count discrete sweep 3.2-4.2 GHz, 201
points (the proven sweep shape, EC#6 — sweep names auto-suffix; read the
real names back from existing_analysis_sweeps).
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    sweeps = list(hfss.existing_analysis_sweeps)
    print("existing sweeps (pre):", sweeps, flush=True)

    # delete-then-create (ADR 0008): drop the setup and its sweeps.
    existing_setups = list(hfss.setups)
    for st in existing_setups:
        for sw in list(st.sweeps):
            print("deleting sweep:", st.name, sw.name, flush=True)
            st.delete_sweep(str(sw.name))
        hfss.delete_setup(st.name)
        print("deleted setup:", st.name, flush=True)

    setup = hfss.create_setup("Setup1")
    setup.props["Frequency"] = "3.5GHz"
    setup.props["MaxPasses"] = 15
    setup.props["MaxDeltaS"] = 0.02
    setup.update()
    print(
        "setup:", setup.name, setup.props.get("Frequency"),
        setup.props.get("MaxPasses"), flush=True,
    )

    hfss.create_linear_count_sweep(
        setup=setup.name, unit="GHz", start_frequency=3.2,
        stop_frequency=4.2, num_of_freq_points=201,
    )
    sweeps = list(hfss.existing_analysis_sweeps)
    print("existing_analysis_sweeps (post):", sweeps, flush=True)
    write_state("sweeps", ",".join(sweeps))
    assert sweeps, "no sweep visible after create"
    assert any("Setup1" in s for s in sweeps), "Setup1 sweep missing: %r" % sweeps
    print(
        "PASS: setup Setup1 3.5GHz/15pass/dS0.02, sweeps %s" % ", ".join(sweeps),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
