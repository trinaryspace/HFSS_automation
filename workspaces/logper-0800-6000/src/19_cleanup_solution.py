"""Delete the solution data of the design selected by HFSS_WS_DESIGN.

For a design whose stored solution is useless and in the way: a solve that
was stopped part-way leaves gigabytes of partial data and a report that
plots numbers nobody should read. Geometry, setups and variables are kept.

REFUSES the FR-4 replica design, whose banked results are a deliverable.

Usage (workspace root):
    set HFSS_WS_DESIGN=LogPer_RO4350B_20mil
    python src/19_cleanup_solution.py
Prints one Verification line:  PASS: cleanup_solution design=<name> ...

API (spine-api.md):
    Hfss.cleanup_solution(variations='All', entire_solution=True, field=True,
        mesh=True, linked_data=True) -> bool
"""

import ws_common

PROTECTED = {"LogPer_CoaxFeed_NoCase"}


def main():
    if ws_common.DESIGN in PROTECTED:
        raise RuntimeError("%s holds banked deliverable results - refusing"
                           % ws_common.DESIGN)
    hfss = ws_common.attach()
    done = hfss.cleanup_solution(entire_solution=True, field=True, mesh=True)
    hfss.save_project()
    print("PASS: cleanup_solution design=%s returned=%s" % (ws_common.DESIGN, done),
          flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
