"""Stage 4: geometry — every dimension/position a design variable.

Layout (user-confirmed Clarification):
- Substrate 90 (X) x 80 (Y) x 1.6 mm, FR4_43 (er 4.3, tan-d 0.02).
- Ground plane on the bottom (z = -CuT..0).
- Bow-tie waist at the substrate center (0, 0): two triangle petals with
  their bases along X at y = +/-PatchL, tips touching the feed stub start.
- 50-ohm feed stub (Table I: Wz=3.1118, Lz=45) runs along +X from the
  waist to the substrate +X edge (x = +SubW/2) — Lz = half the PCB width,
  per the paper text.
- Waveport plane flush at x = SubW/2 (stage 04), airbox +X face flush with
  it (port on the external boundary, Ports.pdf).
- NO DGS (user decision: baseline reference antenna).
"""

import os
import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler

    # deterministic rebuild: wipe any solids from previous Runs (EC#8 — same-name
    # rebuilds duplicate silently and invalidate; never start from a dirty design)
    stale = list(m.object_names)
    if stale:
        m.delete(stale)
        print("wiped previous objects:", stale, flush=True)

    v = {
        "PatchW": "26.3269mm",  # triangle base width (paper Table I: W)
        "PatchL": "20.2168mm",  # triangle length (paper Table I: L)
        "SubW": "90mm",         # substrate width  (paper Table I: Wg)
        "SubL": "80mm",         # substrate length (paper Table I: Lg)
        "SubH": "1.6mm",        # substrate thickness (paper Table I: h)
        "CuT": "0.1mm",         # copper thickness (paper Table I: t)
        "FeedW": "3.1118mm",    # 50-ohm feed line width (paper Table I: Wz)
        "FeedL": "45mm",        # feed line length (paper Table I: Lz = Wg/2)
        "AirGap": "25mm",       # radiation airbox gap >= lambda/4 (21.4mm @3.5GHz)
        "PortW": "3*FeedW",     # waveport width  (live-validated shape, EC#7/#8)
        "PortH": "3*FeedW",     # waveport height (ground bottom up ~5.8h)
    }
    for k, val in v.items():
        hfss[k] = val
    print("variables set:", sorted(k for k in hfss.variable_manager.variables if k in v), flush=True)

    mat = hfss.materials.material_keys.get("FR4_43")
    if mat is None:
        mat = hfss.materials.add_material("FR4_43")
    mat.permittivity.value = 4.3
    mat.dielectric_loss_tangent.value = 0.02
    mat.update()
    print("material FR4_43 permittivity =", mat.permittivity.evaluated_value, flush=True)

    # 1. substrate
    m.create_box(["-SubW/2", "-SubL/2", "0"], ["SubW", "SubL", "SubH"], "Substrate", "FR4_43")
    # 2. ground plane (no DGS — clean, per user decision)
    m.create_box(["-SubW/2", "-SubL/2", "-CuT"], ["SubW", "SubL", "CuT"], "Ground", "pec")

    # 3. lower triangle: base along X at y=-PatchL, tip at the waist (0,0).
    #    The tip lands inside the feed stub footprint (x>=0), so the petal
    #    OVERLAPS the stub by area — point-contact petals fail to unite.
    #    CCW winding -> +Z sheet normal -> thicken_sheet extrudes upward.
    p_lo = m.create_polyline(
        [
            ["-PatchW/2", "-PatchL", "SubH"],
            ["PatchW/2", "-PatchL", "SubH"],
            ["0", "0", "SubH"],
        ],
        cover_surface=True,
        close_surface=True,
        name="PatchBowtie",
        material="pec",
    )

    # 4. upper triangle: mirrored, tip also at the waist (0,0). Vertex order
    #    REVERSED vs the lower petal so the normal still points +Z.
    p_hi = m.create_polyline(
        [
            ["-PatchW/2", "PatchL", "SubH"],
            ["0", "0", "SubH"],
            ["PatchW/2", "PatchL", "SubH"],
        ],
        cover_surface=True,
        close_surface=True,
        name="PatchTriUp",
        material="pec",
    )

    # 5. feed stub: from the waist (x=0) to the substrate +X edge
    m.create_box(["0", "-FeedW/2", "SubH"], ["FeedL", "FeedW", "CuT"], "FeedLine", "pec")

    for p in (p_lo, p_hi):
        hfss.modeler.thicken_sheet(p.name, "CuT", both_sides=False)
    # unite all three PEC pieces into one solid named PatchBowtie
    p_lo.unite(["PatchTriUp", "FeedLine"])

    # 6. radiation airbox — +X face flush with the port plane (x=SubW/2)
    m.create_box(
        ["-SubW/2 - AirGap", "-SubL/2 - AirGap", "-CuT - AirGap"],
        ["SubW + AirGap", "SubL + 2*AirGap", "SubH + CuT + 2*AirGap"],
        "AirBox",
        "air",
    )

    objs = list(m.object_names)
    print("objects:", objs, flush=True)
    write_state("objects", ",".join(sorted(objs)))
    for o in objs:
        print(f"  {o}: bb={m.objects_by_name[o].bounding_box}", flush=True)
    pb = m.objects_by_name.get("PatchBowtie")
    assert pb is not None, "PatchBowtie union missing"
    bb = pb.bounding_box
    assert abs(bb[2] - 1.6) < 1e-9 and abs(bb[5] - 1.7) < 1e-9, f"PatchBowtie z range wrong: {bb}"
    hfss.save_project()
    print("STAGE_OK geometry solids (no DGS) + variables", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
