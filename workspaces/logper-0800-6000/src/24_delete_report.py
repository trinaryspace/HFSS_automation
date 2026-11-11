"""Delete named `AgentReadout_*` reports from the design in HFSS_WS_DESIGN.

Why this exists: a report left in the design tree is recomputed by AEDT when
the project is reopened or another report is exported. The full-sphere
far-field table (`AgentReadout_dB_DirTotal`, 98,826 rows) takes over ten
minutes each time and made AEDT unresponsive after a restart. Its numbers
are already on disk as CSV, so the report itself is disposable.

Only reports whose name starts with `AgentReadout_` can be deleted here -
never a report the user made.

Usage (workspace root):
    python src/24_delete_report.py AgentReadout_dB_DirTotal [more names ...]
Prints one Verification line:  PASS: delete_report ...
"""

import sys

import ws_common

PREFIX = "AgentReadout_"


def main(names):
    if not names:
        raise SystemExit("usage: 24_delete_report.py <report name> [...]")
    foreign = [n for n in names if not n.startswith(PREFIX)]
    if foreign:
        raise RuntimeError("refusing to delete non-agent reports: %s" % foreign)
    hfss = ws_common.attach()
    module = hfss.odesign.GetModule("ReportSetup")
    before = [str(n) for n in (module.GetAllReportNames() or [])]
    present = [n for n in names if n in before]
    if present:
        module.DeleteReports(present)
    after = [str(n) for n in (module.GetAllReportNames() or [])]
    left = [n for n in names if n in after]
    if left:
        raise RuntimeError("still present after delete: %s" % left)
    hfss.save_project()
    print("PASS: delete_report design=%s deleted=%s absent=%s remaining=%s"
          % (ws_common.DESIGN, present, [n for n in names if n not in before], after),
          flush=True)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
