"""Export model pictures of the built design for the Review gate.

The gate is visual (ADR 0003) and the user may be reviewing from another
device, so this writes JPGs of the as-built model beside the other
deliverables instead of relying on the operator being at the desktop.

Pure post-processing: it reads the live model, writes image files, and
changes nothing. Keeps the desktop alive.

Usage (workspace root):  python src/13_model_picture.py
Prints one Verification line:  PASS: model_picture <counts>

API (quoted from the KB, `postprocessing/ansys.aedt.core.visualization.post.
post_common_3d.PostProcessor3D.export_model_picture.md`):
    export_model_picture(full_name=None, show_axis=True, show_grid=True,
        show_ruler=True, show_region='Default', selections=None,
        field_selections=None, orientation='isometric', width=0, height=0) -> str
and `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.fit_all.md`:
    fit_all() -> None
"""

import os
import sys

import ws_common

RESULTS = ws_common.RESULTS
# Views worth having at the gate: the top view is the one that shows the
# bow-tie outlines and alternation, which no bounding box can evidence.
VIEWS = ("top", "bottom", "isometric")


def main():
    hfss = ws_common.attach()
    os.makedirs(RESULTS, exist_ok=True)
    hfss.modeler.fit_all()
    written = []
    for orientation in VIEWS:
        out = os.path.join(RESULTS, "model_%s.jpg" % orientation)
        if os.path.exists(out):
            os.remove(out)                      # delete-then-create (ADR 0008)
        hfss.post.export_model_picture(
            full_name=out,
            show_axis=False,
            show_grid=False,
            show_ruler=False,
            orientation=orientation,
            width=1600,
            height=1200,
        )
        if os.path.exists(out) and os.path.getsize(out) > 0:
            written.append((orientation, os.path.getsize(out)))
        else:
            raise RuntimeError("export_model_picture wrote nothing for %r" % orientation)

    detail = " ".join("%s=%dB" % kv for kv in written)
    line = "PASS: model_picture views=%d %s" % (len(written), detail)
    print(line, flush=True)
    import run_events

    run_events.emit("gate.picture", stage="review_gate", verdict=line,
                    detail="dir=%s" % RESULTS, state_dir=ws_common.STATE)
    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
        sys.exit(1)
