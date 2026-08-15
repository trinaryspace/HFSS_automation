"""Stage 4 (SYNCED, ver.2): geometry — one concave polygon for the whole trace.

User-corrected live model reproduces the PEC trace as a SINGLE outline:
  base_lo_left -> base_lo_right -> feed_lo_left -> edge_lo -> edge_hi
  -> feed_hi_left -> base_hi_right -> base_hi_left -> waist_left
(read back from live faces, Aug 2026). The feed line runs along +X from the
substrate +X edge (x=SubW/2) to the bowtie waist (x=FeedTipX*), sitting
BETWEEN the two triangle patches; AirBox +X face is flush with the port
plane at x=SubW/2. All coordinates are variable expressions.
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler
    wns = write_state

    v = {
        "PatchW": "26.3269mm",   # triangle base width (paper Table I)
        "PatchL": "20.2168mm",   # triangle length
        "SubW": "90mm",          # substrate width
        "SubL": "80mm",          # substrate length
        "SubH": "1.6mm",         # substrate thickness
        "CuT": "0.1mm",          # copper thickness
        "FeedW": "3.1118mm",     # 50-ohm feed line width
        "FeedL": "45mm",         # paper feed-line length (reference value)
        "AirGap": "25mm",        # radiation airbox gap (>= lambda/4 = 20.5mm @3.67GHz)
        # ---- position arguments (user-corrected in the UI) ----
        "WaistY": "5mm",         # y of the bowtie waist / feed centerline
        "FeedTipXlo": "2.417mm", # feed bottom-left x
        "FeedTipXhi": "2.481mm", # feed top-left x
        "FeedTipYlo": "3.5mm",   # feed bottom y
        "FeedTipYhi": "6.612mm", # feed top y
        "PortH": "4*FeedW",      # port height variable (user's value; live sheet is 3*FeedW)
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

    # 1. substrate
    m.create_box(["-SubW/2", "-SubL/2", "0"], ["SubW", "SubL", "SubH"], "Substrate", "FR4_43")
    # 2. ground plane
    m.create_box(["-SubW/2", "-SubL/2", "-CuT"], ["SubW", "SubL", "CuT"], "Ground", "pec")

    # 3. whole PEC trace as ONE concave polygon (live outline, CCW), thickened up
    pts = [
        ["-PatchW/2", "WaistY - PatchL", "SubH"],
        ["PatchW/2", "WaistY - PatchL", "SubH"],
        ["FeedTipXlo", "FeedTipYlo", "SubH"],
        ["SubW/2", "FeedTipYlo", "SubH"],
        ["SubW/2", "FeedTipYhi", "SubH"],
        ["FeedTipXhi", "FeedTipYhi", "SubH"],
        ["PatchW/2", "WaistY + PatchL", "SubH"],
        ["-PatchW/2", "WaistY + PatchL", "SubH"],
        ["-FeedW/2", "WaistY", "SubH"],
    ]
    poly = m.create_polyline(pts, cover_surface=True, close_surface=True, name="PatchBowtie", material="pec")
    hfss.modeler.thicken_sheet(poly.name, "CuT", both_sides=False)

    # 4. radiation airbox — +X face flush with the port plane (x=SubW/2)
    m.create_box(
        ["-SubW/2 - AirGap", "-SubL/2 - AirGap", "-CuT - AirGap"],
        ["SubW + AirGap", "SubL + 2*AirGap", "SubH + CuT + 2*AirGap"],
        "AirBox",
        "air",
    )

    objs = list(m.object_names)
    print("objects:", objs, flush=True)
    for o in objs:
        print(f"  {o}: bb={m.objects_by_name[o].bounding_box}", flush=True)
    wns("objects", ",".join(sorted(objs)))
    hfss.save_project()
    print("STAGE_OK geometry solids + variables (synced layout v2)", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
