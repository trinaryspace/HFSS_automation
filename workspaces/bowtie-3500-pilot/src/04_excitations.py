"""Stage 4: excitations / boundaries — port + radiation, delete-then-create.

Waveport per Ports.pdf: on an external boundary (airbox +X face, flush with
the substrate +X edge at x = +SubW/2), microstrip cross-section, sized
3*FeedW, 50 ohm, renormalized. Assignment via the sheet's FACE OBJECT — never
ids/edges (EC#7); default integration line (the explicit-line macro route
errored; default worked — EC#7 route-around). Radiation boundary on AirBox.

Delete-then-create (ADR 0008): the port boundary, its sheet, and the
radiation boundary are deleted before being re-created, so re-running this
stage in place converges.
"""

import sys
import re

from ws_common import attach, exit_keep_alive, write_state


def delete_boundaries(hfss, pattern):
    for b in list(hfss.boundaries):
        if re.match(pattern, str(b.name)):
            print("deleting boundary:", b.name, flush=True)
            b.delete()


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler

    # delete-then-create (ADR 0008)
    delete_boundaries(hfss, r"^1$")
    delete_boundaries(hfss, r"^Rad")
    if "PortSheet" in m.object_names:
        print("deleting stale PortSheet", flush=True)
        m.delete(["PortSheet"])

    # port sheet: YZ plane at x = +SubW/2 (feed/edge + airbox-face
    # intersection), 3*FeedW square, vacuum -> external boundary port.
    sheet = m.create_rectangle(
        "YZ",
        ["SubW/2", "-PortW/2", "-CuT"],
        ["PortW", "PortH"],
        "PortSheet",
        "vacuum",
    )
    print("port sheet:", sheet.name, "faces:", [f.id for f in sheet.faces], flush=True)
    face = sheet.faces[0]
    port = hfss.wave_port(
        face,
        impedance=50,
        name="1",
        renormalize=True,
    )
    print("wave port:", port.name if port else None, flush=True)

    rad = hfss.assign_radiation_boundary_to_objects("AirBox")
    print("radiation boundary:", rad.name if rad else None, flush=True)

    names = sorted(str(b.name) for b in hfss.boundaries)
    print("boundaries:", names, flush=True)
    write_state("boundaries", ",".join(names))
    write_state("objects", ",".join(sorted(m.object_names)))

    port_hit = any(n == "1" for n in names)
    rad_hit = any(n.startswith("Rad") for n in names)
    assert port_hit, "waveport boundary missing: %r" % names
    assert rad_hit, "radiation boundary missing: %r" % names
    print(
        "PASS: excitations waveport on %s face, boundaries %s (port + radiation)"
        % (sheet.name, ", ".join(names)),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
