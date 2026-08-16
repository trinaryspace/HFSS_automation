"""Stage 4: excitations/boundaries — lumped port + radiation boundary.

Lumped port (Recipe: inset feed tuned for 50 ohm): the port sheet is the XZ
rectangle on the substrate -Y face spanning the trace width (x) and the
dielectric height (z in [0, SubH]) — the cross-section between ground top
and trace bottom. Assignment by FACE OBJECT on the sheet (EC#7; ids/edges
break on this pairing). Integration line is passed as an explicit 2-point
list derived from the sheet's own bounding box (bottom-center -> top-center,
the vertical ground-to-trace gap), never an EdgePrimitive (EC#7 crash).

Radiation boundary on AirBox (assign_radiation_boundary_to_objects).
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler

    # delete-then-create (ADR 0008): drop prior ports/boundaries created here.
    for b in list(hfss.boundaries):
        try:
            if b.name in ("1", "Rad1") or "Rad" in b.name or b.name == "1":
                b.delete()
                print("deleted boundary:", b.name, flush=True)
        except Exception as e:  # noqa: BLE001 - best effort, idempotent re-run
            print("boundary delete skip:", b.name, type(e).__name__, flush=True)

    sheet = m.objects_by_name.get("PortSheet")
    assert sheet is not None, "PortSheet missing (run stage 02 first)"
    bb = sheet.bounding_box
    print("PortSheet bbox:", bb, flush=True)
    # sanity: the XZ sheet must span FeedW in x and SubH in z (cf. stage 02 comment)
    assert abs((bb[3] - bb[0]) - 3.06) < 1e-6, "port sheet x span != FeedW: %r" % bb
    assert abs((bb[5] - bb[2]) - 1.6) < 1e-6, "port sheet z span != SubH: %r" % bb
    mid_x = (bb[0] + bb[3]) / 2.0
    y_plane = (bb[1] + bb[4]) / 2.0
    line = [[mid_x, y_plane, bb[2]], [mid_x, y_plane, bb[5]]]
    print("integration line (bottom->top):", line, flush=True)

    # pyAEDT 1.3.0 `lumped_port` defect (measured 2026-08-14): a FacePrimitive's
    # id is stringified into props["Objects"] and the macro layer rejects it
    # ("a geometry selection is required for assignment") — unlike wave_port,
    # which resolves face ids to object names. The working shape on this
    # pairing: the SHEET NAME (the stable geometry selection) + the explicit
    # 2-point integration line.
    port = hfss.lumped_port(
        "PortSheet",
        impedance=50,
        name="1",
        renormalize=True,
        integration_line=line,
    )
    print("lumped port:", port.name if port else None, flush=True)

    rad = hfss.assign_radiation_boundary_to_objects("AirBox", name="Rad1")
    print("radiation boundary:", rad.name if rad else None, flush=True)

    names = sorted(b.name for b in hfss.boundaries)
    print("boundaries:", names, flush=True)
    write_state("boundaries", ",".join(names))
    write_state("objects", ",".join(sorted(m.object_names)))
    hit = any(n == "1" for n in names) and any("Rad" in n for n in names)
    assert port is not None and hit, "port or radiation boundary missing"
    print("PASS: excitations lumped port '1' (50 ohm, integration line vertical) "
          "on PortSheet face, radiation boundary Rad1 on AirBox", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
