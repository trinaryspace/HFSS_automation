"""Diagnostic: dump this process's visible windows around the design-open freeze.

Shows whether the AEDT GUI ever materializes (window classes/titles) in the
session this script runs in, and what window state exists right before the
GetActiveDesign call that freezes.
"""

import ctypes
import os
import sys
import time

from ansys.aedt.core import Desktop

user32 = ctypes.windll.user32
EnumWindows = user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
GetWindowThreadProcessId = user32.GetWindowThreadProcessId
GetWindowTextW = user32.GetWindowTextW
GetClassNameW = user32.GetClassNameW
IsWindowVisible = user32.IsWindowVisible

my_pid = os.getpid()


def dump_windows(label):
    titles = []

    def collector(hwnd, _):
        pid = ctypes.c_ulong()
        GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if pid.value == my_pid and IsWindowVisible(hwnd):
            buf = ctypes.create_unicode_buffer(512)
            GetWindowTextW(hwnd, buf, 512)
            cls = ctypes.create_unicode_buffer(256)
            GetClassNameW(hwnd, cls, 256)
            titles.append((cls.value, buf.value))
        return True

    print(f"--- windows of pid {my_pid} at {label} ---", flush=True)
    EnumWindows(EnumWindowsProc(collector), 0)
    if not titles:
        print("  (no visible top-level windows for this process)", flush=True)
    for t in titles:
        visible = "VISIBLE"
        print(f"  [{t[0]}] {t[1] or '(no title)'} ({visible})", flush=True)
    print(f"--- {len(titles)} windows ---", flush=True)


def main() -> int:
    d = Desktop(version="2024.1", new_desktop=True, non_graphical=False)
    dump_windows("after launch")
    d.odesktop.NewProject()
    oproject = d.odesktop.GetActiveProject()
    print("project:", oproject.GetName(), flush=True)
    dump_windows("after new project")
    print("InsertDesign...", flush=True)
    oproject.InsertDesign("HFSS", "probe_design", "HFSS Modal Network", "")
    print("InsertDesign returned", flush=True)
    print("sleeping 25s for design editor init...", flush=True)
    time.sleep(25)
    dump_windows("after InsertDesign+25s (right before GetActiveDesign)")
    print("DIAG COMPLETE - calling GetActiveDesign is NOT attempted (freezes)", flush=True)
    d.odesktop.QuitApplication()
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
