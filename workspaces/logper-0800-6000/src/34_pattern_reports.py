"""Add radiation-pattern plots to the design in HFSS_WS_DESIGN, for the user
to open in the AEDT Results tree.

Creates (delete-then-create, ADR 0008):
  Pattern_Eplane_dBi   polar cut in the board plane (theta = 90), all field
                       frequencies as traces
  Pattern_Hplane_dBi   polar cut normal to the board through the board axis
                       (phi = 0 and 180), all field frequencies
  Pattern_3D_<f>GHz    3D polar plot of total directivity at each field
                       frequency

Frame: +x runs base -> tip, so the beam should point along +x (phi = 0,
theta = 90).

These are far-field reports and AEDT recomputes them whenever a field point
is re-solved. On the 5-degree sphere that is cheap; on a 2-degree sphere it
cost ~35 minutes per point (2026-11-12), so this stage refuses a sphere finer
than 4 degrees. Delete them (`24_delete_report.py` only handles
AgentReadout_*; these are removed by re-running with --remove) before a long
solve if they get in the way.

Usage (workspace root):
    set HFSS_WS_DESIGN=LogPer_RO4350B_v3
    python src/34_pattern_reports.py            # create
    python src/34_pattern_reports.py --remove   # delete them again
Prints one Verification line:  PASS: pattern_reports ...
"""

import sys

import read_results

read_results.apply_route_arounds()          # must precede Hfss construction

import ws_common                             # noqa: E402

SWEEP = "Setup1 : FieldPts"
SPHERE = "FF_Sphere"
EXPR = "dB(DirTotal)"
FREQS = ["1GHz", "2GHz", "3GHz", "4GHz", "5GHz", "6GHz"]
PREFIX = "Pattern_"


def main(argv):
    remove_only = "--remove" in argv
    hfss = ws_common.attach()
    module = hfss.odesign.GetModule("ReportSetup")
    existing = [str(n) for n in (module.GetAllReportNames() or [])]
    ours = [n for n in existing if n.startswith(PREFIX)]
    if ours:
        module.DeleteReports(ours)
    if remove_only:
        hfss.save_project()
        print("PASS: pattern_reports removed=%s" % ours, flush=True)
        return

    step = None
    for field_setup in hfss.field_setups or []:
        if field_setup.name == SPHERE:
            props = dict(field_setup.props)
            step = float(str(props.get("ThetaStep", "0")).replace("deg", ""))
    if step is None:
        raise RuntimeError("far-field sphere %s not found - run 22_setup_extras.py "
                           "without LOGPER_TUNING" % SPHERE)
    if step < 4.0:
        raise RuntimeError("sphere step is %.1f deg; refusing to add live far-field "
                           "reports on a sphere finer than 4 deg" % step)

    created = []
    module.CreateReport(
        PREFIX + "Eplane_dBi", "Far Fields", "Radiation Pattern", SWEEP,
        ["Context:=", SPHERE],
        ["Phi:=", ["All"], "Theta:=", ["90deg"], "Freq:=", ["All"]],
        ["Ang Component:=", "Phi", "Mag Component:=", [EXPR]], [])
    created.append(PREFIX + "Eplane_dBi")
    module.CreateReport(
        PREFIX + "Hplane_dBi", "Far Fields", "Radiation Pattern", SWEEP,
        ["Context:=", SPHERE],
        ["Theta:=", ["All"], "Phi:=", ["0deg", "180deg"], "Freq:=", ["All"]],
        ["Ang Component:=", "Theta", "Mag Component:=", [EXPR]], [])
    created.append(PREFIX + "Hplane_dBi")
    for freq in FREQS:
        name = PREFIX + "3D_" + freq
        module.CreateReport(
            name, "Far Fields", "3D Polar Plot", SWEEP,
            ["Context:=", SPHERE],
            ["Phi:=", ["All"], "Theta:=", ["All"], "Freq:=", [freq]],
            ["Phi Component:=", "Phi", "Theta Component:=", "Theta",
             "Mag Component:=", [EXPR]], [])
        created.append(name)

    after = [str(n) for n in (module.GetAllReportNames() or [])]
    missing = [n for n in created if n not in after]
    if missing:
        raise RuntimeError("reports missing after creation: %s" % missing)
    hfss.save_project()
    print("PASS: pattern_reports design=%s sphere_step=%.0fdeg created=%d %s saved=True"
          % (ws_common.DESIGN, step, len(created), created), flush=True)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
