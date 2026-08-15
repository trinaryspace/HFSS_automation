"""Stage 6: excitations / boundaries.

Waveport per Ports.pdf: on an external boundary (airbox +X face, flush with
the substrate +X edge), at the microstrip cross-section where only the
quasi-TEM mode propagates, sized 3*FeedW (small enough to avoid higher
waveguide modes, still >= 6h), 50 ohm, renormalized. Assignment via the
sheet's face object (EC#7); sheet on the boundary face is the shape that
validated and solved in the bowtie-3670 session (EC#8 route-around).

Radiation boundary on AirBox (HFSS-manual standard open region; gap 25mm,
>= lambda/4 at 3.5 GHz).
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler

    # port sheet: YZ plane at x=SubW/2 (feed/edge intersection), 3*FeedW square
    sheet = m.create_rectangle(
        "YZ",
        ["SubW/2", "-PortW/2", "-CuT"],
        ["PortW", "PortH"],
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
    # keep the objects record current (stage 02 recorded pre-port objects)
    write_state("objects", ",".join(sorted(m.object_names)))
    hit = any("1" == n for n in names) and any("Rad" in n for n in names)
    print("STAGE_OK excitations" if hit and port else "STAGE_FAILED excitations", flush=True)
    return 0 if hit and port else 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
