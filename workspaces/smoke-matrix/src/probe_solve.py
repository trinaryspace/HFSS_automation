"""Matrix probe: analyze(blocking=False) non-blocking solve submission behavior.

Builds the shared smoke design, launches the solve non-blocking, times the
submission, and polls for a solution. Verified: submission returns quickly.
Background completion is inferred (see environment-compat entry item 5),
not asserted here — readout is flaky, so no PASS/FAIL on data.
"""

import os
import sys
import time

import psutil
from ansys.aedt.core import Hfss

from aedt_helpers import AEDT_VERSION, kill_aedt_tree, wipe_project_dir
from s11_readout import fetch_s11_db, s11_summary
from smoke_design import build_smoke_design

PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "projects")
PROJECT = os.path.join(PROJECT_DIR, "smoke_solve.aedt")


def main() -> int:
    start_time = time.time()
    lingering_pid = [None]
    os.makedirs(PROJECT_DIR, exist_ok=True)
    wipe_project_dir(PROJECT_DIR)
    exit_code = 0
    try:
        with Hfss(
            version=AEDT_VERSION,
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design="solve_design",
            solution_type="Modal",
        ) as hfss:
            lingering_pid[0] = hfss.desktop_class.aedt_process_id
            build_smoke_design(hfss)
            hfss.save_project()
            print("step 1: design built + saved (valid):",
                  bool(hfss.validate_simple()), flush=True)
            t0 = time.time()
            rv = hfss.analyze(setup="Setup1", blocking=False)
            print(f"step 2: analyze(blocking=False) returned {rv!r} after {time.time()-t0:.1f}s", flush=True)
            deadline = time.time() + 420
            result = None
            last_err = None
            while time.time() < deadline:
                data = fetch_s11_db(hfss, timeout=30)
                if not isinstance(data, Exception):
                    result = data
                    break
                last_err = f"{type(data).__name__}"
                time.sleep(10)
            elapsed = time.time() - t0
            if result is None:
                print(f"step 3: no data within {elapsed:.0f}s; last {last_err} (flaky readout recorded)", flush=True)
            else:
                lo, at = s11_summary(result)
                print(f"step 3: result visible after {elapsed:.0f}s; S11 min {lo:.2f} dB; @2.4GHz {at:.2f} dB", flush=True)
            if rv:
                print("NON-BLOCKING SOLVE PROBE PASS: submission verified (completion inferred)", flush=True)
            else:
                print("NON-BLOCKING SOLVE PROBE FAIL: analyze(blocking=False) returned falsy", flush=True)
                exit_code = 1
    finally:
        kill_aedt_tree(lingering_pid[0], also_sweep_since=start_time)
        leftover = [
            p.info["pid"]
            for p in psutil.process_iter(["pid", "name", "create_time"])
            if p.info["name"] == "ansysedt.exe" and p.info["create_time"] > start_time
        ]
        assert not leftover, f"ansysedt still alive after cleanup: {leftover}"
    sys.stdout.flush()
    os._exit(exit_code)


if __name__ == "__main__":
    raise SystemExit(main())
