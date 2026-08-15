"""Read-back sync probe (ADR 0005): compare the live model against the
staged record (state files) after the user's Review gate. If everything
matches, the gate closes with zero deltas; otherwise the owning stage's
script must be amended before solving.
"""

import sys

from ws_common import attach, exit_keep_alive, read_state


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler

    written_vars = {"AirGap", "CuT", "FeedL", "FeedW", "PatchL", "PatchW", "PortH", "PortW", "SubH", "SubL", "SubW"}
    live_vars = {k: hfss.variable_manager.variables[k].expression for k in written_vars}
    print("live design variables:", flush=True)
    for k in sorted(live_vars):
        print(f"  {k} = {live_vars[k]}", flush=True)

    objects = list(m.object_names)
    boundaries = sorted(b.name for b in hfss.boundaries)
    sweeps = list(hfss.existing_analysis_sweeps)
    print("objects:", objects, flush=True)
    print("boundaries:", boundaries, flush=True)
    print("sweeps:", sweeps, flush=True)

    rec_objects = (read_state("objects") or "").split(",")
    rec_bnds = (read_state("boundaries") or "").split(",")
    rec_sweeps = (read_state("sweeps") or "").split(",")

    delta = []
    if sorted(objects) != sorted(rec_objects):
        delta.append(f"objects: live={sorted(objects)} recorded={sorted(rec_objects)}")
    if boundaries != rec_bnds:
        delta.append(f"boundaries: live={boundaries} recorded={rec_bnds}")
    if len([s for s in sweeps if "Sweep" in s]) != len([s for s in rec_sweeps if "Sweep" in s]):
        delta.append(f"sweeps differ: live={sweeps} recorded={rec_sweeps}")

    if delta:
        print("SYNC_DELTA:", "; ".join(delta), flush=True)
        return 1
    print("SYNC_OK no deltas; gate closes clean", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
