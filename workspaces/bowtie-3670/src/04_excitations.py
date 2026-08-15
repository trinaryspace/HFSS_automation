"""Stage 6 (SYNCED): excitations / boundaries.

User-corrected live model: wave port on a YZ-plane sheet at the substrate
+X edge (x=SubW/2), where the feed line meets the edge. Sheet is a
3*FeedW square from y=-FeedW, z=-CuT (measured live). Port named "1"
(live boundary name). Radiation boundary on AirBox (unchanged).
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler

    # port sheet: YZ plane at x=SubW/2 (feed/edge intersection), flush with
    # the airbox +X face. Delivered state: y from -FeedW to PortH (4*FeedW),
    # z from -CuT to PortH-FeedW (3*FeedW) — measured from the saved project.
    sheet = m.create_rectangle(
        "YZ",
        ["SubW/2", "-FeedW", "-CuT"],
        ["FeedW + PortH", "PortH - FeedW"],
        "PortSheet",
        "vacuum",
    )
    print("port sheet created:", sheet.name, "faces:", [f.id for f in sheet.faces], flush=True)
    face = sheet.faces[0]
    # default integration (explicit-line macro call errored; default works, EC#7)
    port = hfss.wave_port(
        face,
        impedance=50,
        name="1",
        renormalize=True,
    )
    print("wave port:", port.name if port else None, flush=True)

    rad = hfss.assign_radiation_boundary_to_objects("AirBox")
    print("radiation boundary:", rad.name if rad else None, flush=True)

    names = sorted(b.name for b in hfss.boundaries)
    print("boundaries:", names, flush=True)
    write_state("boundaries", ",".join(names))
    hit = any("1" == n for n in names) and any("Rad" in n for n in names)
    print("STAGE_OK excitations (synced)" if hit and port else "STAGE_FAILED excitations", flush=True)
    return 0 if hit and port else 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
