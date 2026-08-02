"""Matrix probe: RCS/SBR+ surface availability on AEDT 2024 R1.

Records whether the client surface exists and what calling it on a plain
Modal design does (expected per ADR 0004: unavailable on this backend).
"""

import os
import sys

from ansys.aedt.core import Hfss

from aedt_helpers import AEDT_VERSION, kill_aedt_tree

PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects")
PROJECT = os.path.join(PROJECT_DIR, "smoke_solve.aedt")


def main() -> int:
    lingering_pid = [None]
    print("Hfss.get_rcs_data present:", hasattr(Hfss, "get_rcs_data"), flush=True)
    try:
        from ansys.aedt.core.visualization.post.rcs_exporter import MonostaticRCSExporter

        print("MonostaticRCSExporter import: OK", flush=True)
    except Exception as e:
        print("MonostaticRCSExporter import: FAIL", type(e).__name__, str(e)[:120], flush=True)
        sys.stdout.flush()
        os._exit(0)
    try:
        with Hfss(
            version=AEDT_VERSION,
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design="solve_design",
            solution_type="Modal",
            remove_lock=True,
            close_on_exit=True,
        ) as hfss:
            lingering_pid[0] = hfss.desktop_class.aedt_process_id
            try:
                rv = hfss.get_rcs_data(frequencies=[2.4], setup="Setup1")
                print("get_rcs_data on Modal design ->", rv, flush=True)
            except Exception as e:
                print("get_rcs_data on Modal design:", type(e).__name__, str(e)[:160], flush=True)
    finally:
        kill_aedt_tree(lingering_pid[0])
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
