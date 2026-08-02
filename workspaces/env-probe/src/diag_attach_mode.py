"""Diagnostic: does ATTACH mode (new_desktop=False) survive design-open?

Requires a stock ansysedt.exe already running (e.g. Project12 from a
manual launch). Tests the same InsertDesign -> GetActiveDesign sequence
through the attach path.
"""

import os
import sys
import threading
import time
import traceback

from ansys.aedt.core import Desktop


class Watchdog:
    def __init__(self, delays):
        self._delays = list(delays)
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        for d in self._delays:
            time.sleep(d)
            print(f"=== STALL DUMP t={d}s ===", flush=True)
            main_id = threading.main_thread().ident
            for tid, frame in sys._current_frames().items():
                if tid == main_id:
                    traceback.print_stack(frame)
            print("=== /STALL DUMP ===", flush=True)


def main() -> int:
    Watchdog([45, 90, 150])
    print("step A: attaching to running desktop (new_desktop=False)...", flush=True)
    d = Desktop(version="2024.1", new_desktop=False, non_graphical=False)
    print("step B: attached, version", d.aedt_version, flush=True)
    print("step C: active project name:", d.odesktop.GetActiveProjectName(), flush=True)
    oproject = d.odesktop.GetActiveProject()
    print("step D: project obj:", oproject.GetName(), flush=True)
    print("step E: InsertDesign HFSS...", flush=True)
    oproject.InsertDesign("HFSS", "attach_probe_design", "HFSS Modal Network", "")
    print("step F: InsertDesign returned", flush=True)
    print("step G: GetActiveDesign...", flush=True)
    od = oproject.GetActiveDesign()
    print("step H: GetActiveDesign returned:", repr(od), flush=True)
    if od is not None:
        print("step I: childnames:", od.GetChildNames(), flush=True)
    print("ATTACH DIAG COMPLETE", flush=True)
    d.release_desktop(close_projects=False)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
