"""Diagnostic: separate 'GetActiveDesign broken universally' from 'HFSS-specific'.

Control sequence on one live desktop:
  C. GetActiveDesign on an empty project (no design exists)
  D. InsertDesign of a CIRCUIT design
  E. GetActiveDesign (Circuit) -> GetChildNames
  F. InsertDesign of an HFSS design
  G. GetActiveDesign (HFSS) -> GetChildNames
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
    print("step A: creating Desktop session...", flush=True)
    d = Desktop(version="2024.1", new_desktop=True, non_graphical=False)
    print("step B: desktop up, version", d.aedt_version, flush=True)
    d.odesktop.NewProject()
    print("step C: GetActiveDesign on empty project...", flush=True)
    od = d.odesktop.GetActiveDesign()
    print("step C2: empty-project GetActiveDesign returned:", repr(od), flush=True)
    oproject = d.odesktop.GetActiveProject()
    print("step D: InsertDesign CIRCUIT...", flush=True)
    oproject.InsertDesign("CIRCUIT", "circuit_probe", "None", "")
    print("step D2: InsertDesign CIRCUIT returned", flush=True)
    od = d.odesktop.GetActiveDesign()
    print("step E: circuit GetActiveDesign returned:", repr(od), flush=True)
    if od is not None:
        print("step E2: circuit childnames:", od.GetChildNames(), flush=True)
    oproject.InsertDesign("HFSS", "hfss_probe", "HFSS Modal Network", "")
    print("step F2: InsertDesign HFSS returned", flush=True)
    od = d.odesktop.GetActiveDesign()
    print("step G: hfss GetActiveDesign returned:", repr(od), flush=True)
    if od is not None:
        print("step G2: hfss childnames:", od.GetChildNames(), flush=True)
    print("DIAG COMPLETE", flush=True)
    d.release_desktop(close_projects=True, close_desktop=True)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
