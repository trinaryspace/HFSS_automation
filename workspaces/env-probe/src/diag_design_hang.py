"""Diagnostic: find where design creation hangs behind Hfss().

Steps through desktop -> new project -> insert design at the COM level
with a watchdog that dumps the calling stack if anything stalls.
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
    Watchdog([60, 120, 180, 240])
    print("step A: creating Desktop session...", flush=True)
    d = Desktop(version="2024.1", new_desktop=True, non_graphical=False)
    print("step B: desktop up, version", d.aedt_version, flush=True)
    print("step C: NewProject...", flush=True)
    d.odesktop.NewProject()
    print("step D: NewProject returned", flush=True)
    oproject = d.odesktop.GetActiveProject()
    print("step E: active project", oproject.GetName(), flush=True)
    print("step F: InsertDesign('HFSS', 'probe_design', 'HFSS Modal Network', '')...", flush=True)
    oproject.InsertDesign("HFSS", "probe_design", "HFSS Modal Network", "")
    print("step G: InsertDesign returned (None expected over gRPC)", flush=True)
    odesign = d.odesktop.GetActiveDesign()
    print("step H: active design is", odesign.GetName(), flush=True)
    print("step I: GetChildNames on design...", flush=True)
    names = odesign.GetChildNames()
    print("step J: GetChildNames returned", len(names), "names", flush=True)
    print("DIAG COMPLETE", flush=True)
    d.release_desktop(close_projects=True, close_desktop=True)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
