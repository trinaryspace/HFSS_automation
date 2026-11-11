"""Route-B add-on: a resistive termination across the feed line at the base.

Why: the redesign's remaining S11 spikes sit at about twice the half-wave
resonance of the two largest elements. Energy that gets past the active
region runs to the open base end of the feed line, reflects, and re-excites
the big elements at their full-wave frequency - the classic log-periodic
anomaly. A matched resistor across the two feed strips at the base absorbs
that leftover wave instead of reflecting it.

Model: a small vertical sheet inside the substrate joining the bottom strip
(z = 0) to the top strip (z = h), carrying a lumped RLC boundary of R ohm.
As built that is a plated via plus a chip resistor in series on one layer;
the via's inductance and the resistor's parasitics are NOT modelled.

Does nothing unless LOGPER_TERM_R is set, so designs without a termination
replay unchanged.

Usage (workspace root):
    set HFSS_WS_DESIGN=LogPer_RO4350B_v4
    set LOGPER_TERM_R=50
    python src/23_base_termination.py
Prints one Verification line:  PASS: base_termination ...

API, from the installed pyAEDT 1.3.0 (hfss.py):
    assign_lumped_rlc_to_sheet(assignment, start_direction=0, name=None,
        rlc_type="Parallel", resistance=None, inductance=None,
        capacitance=None) -> BoundaryObject | bool
"""

import os

import ws_common

SHEET = "TermR"
BOUNDARY = "TermR_RLC"
TOL = 0.01  # mm


def main():
    value = os.environ.get("LOGPER_TERM_R")
    if not value:
        print("PASS: base_termination skipped - LOGPER_TERM_R not set", flush=True)
        return
    resistance = float(value)
    hfss = ws_common.attach()
    m = hfss.modeler

    for boundary in list(hfss.boundaries or []):       # delete-then-create
        if boundary.name == BOUNDARY:
            boundary.delete()
    if SHEET in m.object_names:
        m.delete(SHEET)

    # Parametric: position and size are design variables.
    hfss["term_x"] = "0.5mm"      # distance of the resistor from the base edge
    hfss["term_w"] = "0.5mm"      # resistor footprint along the board
    hfss["term_y"] = "0.4mm"      # off the centreline, still inside both strips

    # create_rectangle("XZ") takes sizes as [z, x] on 2024 R1 (measured on the
    # patch-2400 run), so the bounding box is checked rather than trusted.
    sheet = m.create_rectangle("XZ", ["term_x", "term_y", "0mm"], ["h", "term_w"],
                               name=SHEET)
    if not sheet or SHEET not in m.object_names:
        raise RuntimeError("could not create the termination sheet")
    box = [float(v) for v in m[SHEET].bounding_box]
    sub = [float(v) for v in m["Substrate"].bounding_box]
    want = [0.5, 0.4, 0.0, 1.0, 0.4, sub[5]]
    if max(abs(a - b) for a, b in zip(box, want)) > TOL:
        raise RuntimeError("termination sheet bbox %s != expected %s" % (box, want))

    mid_x = (box[0] + box[3]) / 2.0
    line = [[mid_x, box[1], box[2]], [mid_x, box[1], box[5]]]   # bottom strip -> top strip
    rlc = hfss.assign_lumped_rlc_to_sheet(SHEET, start_direction=line, name=BOUNDARY,
                                          rlc_type="Parallel", resistance=resistance)
    if not rlc:
        raise RuntimeError("assign_lumped_rlc_to_sheet reported failure")
    names = [b.name for b in hfss.boundaries]
    if BOUNDARY not in names:
        raise RuntimeError("termination boundary missing after assignment: %s" % names)
    if not bool(hfss.validate_simple()):
        raise RuntimeError("validate_simple() returned False with the termination")

    hfss.save_project()
    ws_common.write_state("stage_base_termination", "R=%s" % resistance)
    print("PASS: base_termination R=%.1fohm sheet_bbox=%s boundary=%s validate_simple=True"
          % (resistance, [round(v, 3) for v in box], BOUNDARY), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
