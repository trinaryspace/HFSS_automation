"""Stage 2: geometry — every dimension a design variable, delete-then-create.

Recipe (locked in Clarification): paper-exact plain bowtie, NO DGS.
- Substrate 90 (X) x 80 (Y) x 1.6 mm; ground PEC on z=-CuT..0.
- Bow-tie waist at (0,0): two triangle petals, bases along X at y=+/-PatchL,
  tips meeting at the waist OVERLAPPING the feed-stub footprint (point-contact
  petals fail to unite — prior-art pitfall, feed-location discipline).
- Feed stub (FeedW x FeedL) runs along +X from the waist to the substrate +X
  edge (x = +FeedL = +SubW/2): the port plane sits flush there (user steering
  note: "the feed location was one of the main issues").
- Airbox: lambda/4 gap (25 mm >= 21.4 mm @ 3.5 GHz), +X face flush with the
  port plane at x = +SubW/2.
"""

import sys

from ws_common import attach, exit_keep_alive, write_state

PARAMS = {
    # User-corrected reading of paper Fig 1 (2026-08-05 pilot QA): the
    # isosceles triangle's BASE — the edge farthest from the feed — is the
    # paper's L; the two LEGS pointing inward toward the feed are the
    # paper's W. First build had them swapped (resonated 3.85 GHz, -4 dB);
    # corrected: base = 20.2168, leg = 26.3269, height derived.
    "PatchBase": "20.2168mm",  # triangle base (paper Table I: L)
    "PatchLeg": "26.3269mm",   # triangle legs toward the feed (paper Table I: W)
    "PatchH": "24.3094mm",     # derived height: sqrt(W^2 - (L/2)^2)
    "SubW": "90mm",            # substrate width (paper Table I: Wg)
    "SubL": "80mm",            # substrate length (paper Table I: Lg)
    "SubH": "1.6mm",           # substrate thickness (paper Table I: h)
    "CuT": "0.1mm",            # copper thickness (paper Table I: t)
    "FeedW": "3.1118mm",       # 50-ohm feed line width (paper Table I: Wz)
    "FeedL": "45mm",           # feed line length (paper Table I: Lz = Wg/2)
    "AirGap": "25mm",          # airbox gap >= lambda/4 @ 3.5 GHz (21.4 mm)
    "PortW": "3*FeedW",        # waveport width (proven shape, EC#7/#8)
    "PortH": "3*FeedW",        # waveport height
}

SOLIDS = ["Substrate", "Ground", "PatchBowtie", "PatchTriUp", "FeedLine", "AirBox"]


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler

    # delete-then-create (ADR 0008): re-running this stage in place converges.
    stale = [n for n in SOLIDS if n in m.object_names]
    if stale:
        m.delete(stale)
        print("deleted stale solids:", stale, flush=True)

    for key, val in PARAMS.items():
        hfss[key] = val
    # delete-then-create for variables too (ADR 0008): variables this stage
    # no longer defines (parameterization changes) are removed so a re-run
    # in place converges — orphaned variables also leak into the sweep
    # variation table.
    vm = hfss.variable_manager
    for stale in [n for n in list(vm.variables) if n not in PARAMS]:
        print("deleting stale variable:", stale, flush=True)
        vm.delete_variable(stale)
    print("variables set:", sorted(PARAMS), flush=True)

    # FR4_43: er 4.3, tan-d 0.02 (paper states er; tan-d is the standard value).
    # Lookup by indexing (material_keys is a cold index; getitem returns None —
    # not an exception — when the material is absent from the project library).
    mat = hfss.materials["FR4_43"]
    if mat is None:
        mat = hfss.materials.add_material("FR4_43")
    mat.permittivity.value = 4.3
    mat.dielectric_loss_tangent.value = 0.02
    mat.update()

    m.create_box(["-SubW/2", "-SubL/2", "0"], ["SubW", "SubL", "SubH"], "Substrate", "FR4_43")
    m.create_box(["-SubW/2", "-SubL/2", "-CuT"], ["SubW", "SubL", "CuT"], "Ground", "pec")

    # lower petal: base along X at y=-PatchH (base = PatchBase, the edge
    # farthest from the feed), legs of length PatchLeg meeting at the waist
    # (0,0) — the user-corrected Fig-1 reading. CCW winding -> +Z normal ->
    # thicken_sheet extrudes upward. Tip overlaps the stub footprint.
    p_lo = m.create_polyline(
        [
            ["-PatchBase/2", "-PatchH", "SubH"],
            ["PatchBase/2", "-PatchH", "SubH"],
            ["0", "0", "SubH"],
        ],
        cover_surface=True,
        close_surface=True,
        name="PatchBowtie",
        material="pec",
    )
    p_hi = m.create_polyline(
        [
            ["-PatchBase/2", "PatchH", "SubH"],
            ["0", "0", "SubH"],
            ["PatchBase/2", "PatchH", "SubH"],
        ],
        cover_surface=True,
        close_surface=True,
        name="PatchTriUp",
        material="pec",
    )
    m.create_box(["0", "-FeedW/2", "SubH"], ["FeedL", "FeedW", "CuT"], "FeedLine", "pec")

    for p in (p_lo, p_hi):
        m.thicken_sheet(p.name, "CuT", both_sides=False)
    # unite all three PEC pieces into one solid named PatchBowtie (the
    # united solid keeps the first operand's name)
    p_lo.unite(["PatchTriUp", "FeedLine"])
    print("after unite:", m.object_names, flush=True)

    # airbox: +X face flush with the port plane at x = +SubW/2
    m.create_box(
        ["-SubW/2 - AirGap", "-SubL/2 - AirGap", "-CuT - AirGap"],
        ["SubW + AirGap", "SubL + 2*AirGap", "SubH + CuT + 2*AirGap"],
        "AirBox",
        "air",
    )

    objs = sorted(m.object_names)
    print("objects:", objs, flush=True)
    write_state("objects", ",".join(objs))

    # FEED-LOCATION assertions (user steering note): feed stub reaches exactly
    # the +X substrate edge x=+SubW/2; the airbox +X face is flush with it;
    # petals sit between y=-PatchL..+PatchL with tips at the waist.
    pb = m.objects_by_name["PatchBowtie"]
    bb = pb.bounding_box
    print("PatchBowtie bbox:", bb, flush=True)
    xmin, xmax = bb[0], bb[3]
    assert abs(xmax - 45.0) < 1e-6, "feed does not reach +X edge: xmax=%r" % xmax
    assert abs(xmin + 10.1084) < 3e-3, "petal base half-width wrong: xmin=%r" % xmin
    assert abs(bb[1] + 24.3094) < 3e-3 and abs(bb[4] - 24.3094) < 3e-3, (
        "petal span wrong: %r" % (bb[1], bb[4])
    )
    # leg check: distance (base corner -> waist) must be PatchLeg (paper W)
    leg = ((bb[0] - 0.0) ** 2 + (bb[4] - 0.0) ** 2) ** 0.5
    assert abs(leg - 26.3269) < 5e-3, "petal leg != paper W: %r" % leg
    assert abs(bb[2] - 1.6) < 1e-9 and abs(bb[5] - 1.7) < 1e-9, (
        "thickness range wrong: %r" % (bb[2], bb[5])
    )
    ab = m.objects_by_name["AirBox"]
    abb = ab.bounding_box
    assert abs(abb[3] - 45.0) < 1e-6, "airbox +X face not flush at x=+SubW/2: %r" % abb[3]

    hfss.save_project()
    print(
        "PASS: geometry %d solids, feed xmax==+SubW/2, airbox flush, "
        "base=PatchBase, leg=PatchLeg, span y in [-PatchH,+PatchH], "
        "z in [SubH,SubH+CuT]" % len(objs),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
