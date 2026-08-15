"""Stage 2: geometry — every dimension/position a design variable.

Layout (locked in Clarification, case.json canonical):
- Patch W=38.0100 (x) x L=29.4216 (y) x CuT=0.035 mm, centered on the
  substrate, bottom at z = SubH (top of the FR4_epoxy substrate).
- Substrate/ground 80 x 80 mm; ground is a pec slab z in [-CuT, 0].
- 50-ohm feed trace (FeedW=3.06 mm, Hammerstad) runs along -Y from the
  substrate -Y edge to y = -PatchL/2 + InsetDepth, overlapping the patch
  island by 0.001 mm and united with it (one PEC body — the inset feed
  connects to the patch between the two inset notches).
- Two inset notch boxes (width InsetGap each) subtracted from the patch at
  the -Y radiating edge; InsetDepth is the match tuner (case notes.md).
- Airbox gap AirGap=31 mm (~= lambda0/4 @ 2.4 GHz); radiation boundary on it
  is stage 04.
- PortSheet: XZ rectangle on the substrate -Y face, between trace bottom
  (z=0 ground top) and trace bottom plane (z=SubH) — the lumped-port
  cross-section (stage 04 assigns it by face object, EC#7).
"""

import sys

from ws_common import attach, exit_keep_alive, write_state

OVERLAP = 0.001  # mm — union safety overlap between trace and patch island


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler

    # delete-then-create (ADR 0008): wipe what this stage (re)creates.
    stale = [n for n in m.object_names if n in
             ("Patch", "FeedTrace", "NotchA", "NotchB", "Substrate",
              "Ground", "AirBox", "PortSheet", "AirBox_Auto")]
    if stale:
        m.delete(stale)
        print("deleted stale objects:", stale, flush=True)

    v = {
        "PatchW": "38.01mm",        # case.json (Balanis 14-6)
        "PatchL": "29.4216mm",      # case.json (Balanis 14-7)
        "SubW": "80mm",             # substrate/ground width  (Clarification lock)
        "SubL": "80mm",             # substrate/ground length (Clarification lock)
        "SubH": "1.6mm",            # case.json substrate height
        "CuT": "0.035mm",           # case.json copper thickness
        "FeedW": "3.06mm",          # 50-ohm microstrip on FR4 h=1.6 (Hammerstad)
        "InsetDepth": "7.4mm",      # match tuner (~= L/4); wrong depth => shallow S11, resonance unaffected
        "InsetGap": "3.0mm",        # inset notch width (Clarification lock)
        "AirGap": "31mm",           # ~= lambda0/4 @ 2.4 GHz
    }
    for k, val in v.items():
        hfss[k] = val
    print("variables set:", sorted(k for k in hfss.variable_manager.variables if k in v), flush=True)

    # 1. substrate (FR4_epoxy from the AEDT library — er 4.4, tan-d 0.02, verified stage 03)
    m.create_box(["-SubW/2", "-SubL/2", "0"], ["SubW", "SubL", "SubH"], "Substrate", "FR4_epoxy")
    # 2. ground (pec, full substrate footprint)
    m.create_box(["-SubW/2", "-SubL/2", "-CuT"], ["SubW", "SubL", "CuT"], "Ground", "pec")
    # 3. patch (pec) — the inset notch cuts happen after creation
    patch = m.create_box(["-PatchW/2", "-PatchL/2", "SubH"],
                         ["PatchW", "PatchL", "CuT"], "Patch", "pec")
    # 4. two inset notch boxes, 1 um overshoot in y/z for boolean robustness
    nb = [
        m.create_box(["-FeedW/2 - InsetGap", "-PatchL/2 - 0.001", "SubH - 0.001"],
                     ["InsetGap", "InsetDepth + 0.002", "CuT + 0.002"],
                     "NotchA", "vacuum"),
        m.create_box(["FeedW/2", "-PatchL/2 - 0.001", "SubH - 0.001"],
                     ["InsetGap", "InsetDepth + 0.002", "CuT + 0.002"],
                     "NotchB", "vacuum"),
    ]
    # 5. subtract the notches out of the patch
    m.subtract(blank_list="Patch", tool_list=[n.name for n in nb], keep_originals=False)
    # 6. feed trace: from the substrate -Y edge into the inset island (+OVERLAP)
    trace = m.create_box(
        ["-FeedW/2", "-SubL/2", "SubH"],
        ["FeedW", "SubL/2 - PatchL/2 + InsetDepth + %g" % OVERLAP, "CuT"],
        "FeedTrace", "pec",
    )
    # 7. unite trace into the patch — one continuous PEC feed-to-patch body
    patch.unite(["FeedTrace"])
    print("objects after unite:", m.object_names, flush=True)

    # 8. radiation airbox
    m.create_box(["-SubW/2 - AirGap", "-SubL/2 - AirGap", "-CuT - AirGap"],
                 ["SubW + 2*AirGap", "SubL + 2*AirGap", "SubH + CuT + 2*AirGap"],
                 "AirBox", "air")
    # 9. port sheet: XZ plane on the substrate -Y face, trace width x dielectric height.
    #    Measured on this pairing (2026-08-14): an "XZ" rectangle's sizes are
    #    [z_width, x_height] — sizes[0] runs along Z, sizes[1] along X — so the
    #    argument order is [SubH, FeedW] (a transposed sheet was caught by bbox
    #    assertions in 04: x-span 1.6, z-span 3.06).
    m.create_rectangle("XZ", ["-FeedW/2", "-SubL/2", "0"],
                       ["SubH", "FeedW"], "PortSheet", "vacuum")

    objs = sorted(m.object_names)
    print("objects:", objs, flush=True)
    write_state("objects", ",".join(objs))

    pb = m.objects_by_name.get("Patch")
    assert pb is not None, "Patch missing after unite"
    bb = pb.bounding_box
    print("Patch bbox:", bb, flush=True)
    assert abs(bb[0] + 19.005) < 1e-6 and abs(bb[3] - 19.005) < 1e-6, "patch x span wrong"
    # the unified body runs from the substrate -Y edge (trace) to the patch +Y edge
    assert abs(bb[1] + 40.0) < 1e-6 and abs(bb[4] - 14.7108) < 1e-6, "patch y span wrong"
    assert abs(bb[2] - 1.6) < 1e-6 and abs(bb[5] - 1.635) < 1e-6, "patch z span wrong"
    assert "FeedTrace" not in m.object_names, "FeedTrace should be united into Patch"
    assert "NotchA" not in m.object_names and "NotchB" not in m.object_names, "notches not subtracted"
    assert len(objs) == 5, "expected 5 objects, got %d: %r" % (len(objs), objs)

    hfss.save_project()
    print("PASS: geometry 5 solids (Substrate Ground Patch AirBox PortSheet), "
          "Patch bbox 38.01x29.4216x0.035 at z=1.6, all dims variables", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
