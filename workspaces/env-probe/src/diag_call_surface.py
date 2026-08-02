"""Diagnostic: enumerate which design-object calls work on 2024.1.

Matches pyaedt's own internal sequence (desktop.py / aedt_objects.py):
C. oproject.SetActiveDesign (no design yet - expect fast error)
C2. oproject.GetDesignNames (name array)
D. InsertDesign CIRCUIT
E. oproject.GetActiveDesign  <- the pyaedt-critical call
E2. oproject.GetNumDesigns
F. oproject.GetChildNames
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


def call(label, fn):
    try:
        r = fn()
        print(f"{label}: returned {r!r}", flush=True)
        return r
    except Exception as e:
        print(f"{label}: EXCEPTION {type(e).__name__}: {e}", flush=True)
        return None


def main() -> int:
    Watchdog([40, 80, 140])
    d = Desktop(version="2024.1", new_desktop=True, non_graphical=False)
    print("step B: desktop up", flush=True)
    d.odesktop.NewProject()
    oproject = d.odesktop.GetActiveProject()
    print("step B2: active project OK", flush=True)
    call("step C  SetActiveDesign(none)", lambda: oproject.SetActiveDesign("missing"))
    call("step C2 GetDesignNames", lambda: oproject.GetDesignNames())
    call("step C3 GetNumDesigns", lambda: oproject.GetNumDesigns())
    call("step D  InsertDesign CIRCUIT", lambda: oproject.InsertDesign("CIRCUIT", "circuit_probe", "None", ""))
    call("step E  GetActiveDesign", lambda: oproject.GetActiveDesign())
    call("step E2 GetNumDesigns", lambda: oproject.GetNumDesigns())
    call("step F  GetChildNames", lambda: oproject.GetChildNames())
    call("step G  GetActiveProjectName", lambda: d.odesktop.GetActiveProjectName())
    print("DIAG COMPLETE", flush=True)
    d.release_desktop(close_projects=True, close_desktop=True)
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
