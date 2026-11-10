"""Route-B add-on: the centre conductor's bend at the board tip.

Schema v1 has no circle primitive and no swept arc, so `design.yaml` builds
the straight `InnerCond` (inside the coax) and the vertical `WireLeg` (on the
tip edge) and this stage joins them with the 90 degree, `bend_R`-radius bend
the CST model has (CST STEP: bend radius 1.5 mm, wire radius 0.255 mm).

It then notches the substrate with the finished wire, because the inside of
the bend grazes the board's top tip corner (CST's PCB solid carries the same
notch).

Run AFTER `compile_spec` (which recreates InnerCond and WireLeg). Re-running
it on an already-joined wire verifies and passes without touching the model.

Usage (workspace root):  python src/20_feed_bend.py
Prints one Verification line:  PASS: feed_bend ...

API, quoted from the KB:
  Modeler3D.create_polyline(points, segment_type=None, cover_surface=False,
      close_surface=False, name=None, material=None, xsection_type=None,
      xsection_orient=None, xsection_width=1, xsection_topwidth=1,
      xsection_height=1, xsection_num_seg=0, xsection_bend_type=None,
      non_model=False) -> Polyline
      (xsection_type "Circle": xsection_width is the DIAMETER; three points
       with segment_type "Arc" are a three-point arc)
  Modeler3D.unite(assignment, purge=False, keep_originals=False) -> str | bool
  Modeler3D.subtract(blank_list, tool_list, keep_originals=True) -> bool
"""

import math

import ws_common

BEND = "WireBend"
TOL = 0.02  # mm


def _box(hfss, name):
    return [float(v) for v in hfss.modeler[name].bounding_box]


def _worst(box, want):
    return max(abs(a - b) for a, b in zip(box, want))


def main():
    hfss = ws_common.attach()
    m = hfss.modeler
    names = set(m.object_names)

    if "InnerCond" not in names:
        raise RuntimeError("InnerCond missing - run compile_spec first")

    if "WireLeg" not in names and BEND not in names:
        # Joined on an earlier run: the wire must reach from the coax base to
        # the tip edge and below the far copper.
        box = _box(hfss, "InnerCond")
        sub = _box(hfss, "Substrate")
        if box[0] > TOL or box[3] < sub[3] or box[2] > -TOL:
            raise RuntimeError("InnerCond is not the joined wire: bbox %s" % box)
        print("PASS: feed_bend already joined, bbox=%s"
              % [round(v, 3) for v in box], flush=True)
        return

    if BEND in names:                       # delete-then-create (ADR 0008)
        m.delete(BEND)

    # Dimensions are read from the two objects the spec built. Evaluating the
    # design variables instead (`variable_manager[...].numeric_value`) raises
    # an AEDT API error over gRPC on this box (measured on this run).
    inner, leg = _box(hfss, "InnerCond"), _box(hfss, "WireLeg")
    r_in = (inner[4] - inner[1]) / 2.0
    coax_l, zc = inner[3], (inner[2] + inner[5]) / 2.0
    bend_r = (leg[0] + leg[3]) / 2.0 - coax_l
    if abs((zc - bend_r) - leg[5]) > TOL or bend_r <= r_in:
        raise RuntimeError("InnerCond and WireLeg do not meet through a "
                           "quarter bend: inner %s leg %s" % (inner, leg))

    k = math.sqrt(0.5)
    # Parametric: the three arc points are expressions over design variables.
    points = [
        ["coax_L", "0mm", "zc"],
        ["coax_L + bend_R*%.12f" % k, "0mm", "zc - bend_R + bend_R*%.12f" % k],
        ["coax_L + bend_R", "0mm", "zc - bend_R"],
    ]
    bend = m.create_polyline(
        points,
        segment_type="Arc",
        name=BEND,
        material="cu_pure",
        xsection_type="Circle",
        xsection_width="2*r_in",
        xsection_bend_type="Curved",
    )
    if not bend or BEND not in m.object_names:
        raise RuntimeError("create_polyline did not produce %r" % BEND)
    box = _box(hfss, BEND)
    want = [coax_l, -r_in, zc - bend_r, coax_l + bend_r + r_in, r_in, zc + r_in]
    if _worst(box, want) > TOL:
        raise RuntimeError("bend bbox %s != expected %s"
                           % ([round(v, 4) for v in box], [round(v, 4) for v in want]))

    before = len(m.object_names)
    m.unite(["InnerCond", BEND, "WireLeg"])
    after = len(m.object_names)
    # env-compat #14: a unite can fail silently - judge it by the object count.
    if before - after != 2 or "InnerCond" not in m.object_names:
        raise RuntimeError("unite did not consume 2 objects (%d -> %d)" % (before, after))
    joined = _box(hfss, "InnerCond")
    joined_want = [0.0, -r_in, leg[2], leg[3], r_in, inner[5]]
    if _worst(joined, joined_want) > TOL:
        raise RuntimeError("joined wire bbox %s != expected %s"
                           % ([round(v, 4) for v in joined],
                              [round(v, 4) for v in joined_want]))

    if not m.subtract("Substrate", ["InnerCond"], keep_originals=True):
        raise RuntimeError("subtract Substrate - InnerCond failed")
    if "InnerCond" not in m.object_names:
        raise RuntimeError("InnerCond was consumed by the substrate notch")

    hfss.save_project()
    ws_common.write_state("stage_feed_bend", "done")
    print("PASS: feed_bend bend_R=%.3fmm r_in=%.3fmm bend_bbox_ok united=3->1 "
          "substrate_notched InnerCond_bbox=%s"
          % (bend_r, r_in, [round(v, 3) for v in joined]), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
