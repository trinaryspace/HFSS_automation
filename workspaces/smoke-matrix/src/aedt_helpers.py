"""Shared helpers for the maintained matrix probes.

Constants, project-dir wiping, and kill-until-gone for the launched AEDT
process tree. Investigation-era scripts (src/diag_*.py) intentionally do
not use these — they are archival records.
"""

import os
import shutil
import time

import psutil

AEDT_VERSION = "2024.1"
PROBE_VALUE = "1.5mm"


def wipe_project_dir(project_dir):
    if os.path.isdir(project_dir):
        for leftover in os.listdir(project_dir):
            p = os.path.join(project_dir, leftover)
            if os.path.isdir(p):
                shutil.rmtree(p, ignore_errors=True)
            else:
                os.remove(p)


def kill_aedt_tree(pid, timeout=30, also_sweep_since=None):
    """Kill the launched AEDT process tree and wait until it is gone.

    Observed: release plus a pid-tree kill does not always reap the server
    process; the optional `also_sweep_since` fallback kills any ansysedt.exe
    spawned after that moment, guaranteeing a clean state."""
    if not pid:
        return
    deadline = time.time() + timeout
    first = True
    while time.time() < deadline:
        try:
            proc = psutil.Process(pid)
        except psutil.NoSuchProcess:
            return
        if first:
            for child in proc.children(recursive=True):
                try:
                    child.kill()
                except psutil.NoSuchProcess:
                    pass
            try:
                proc.kill()
            except psutil.NoSuchProcess:
                return
            except psutil.AccessDenied:
                pass
            first = False
        time.sleep(1)
    if also_sweep_since is not None:
        for p in psutil.process_iter(["pid", "name", "create_time"]):
            try:
                if p.info["name"] == "ansysedt.exe" and p.info["create_time"] > also_sweep_since:
                    p.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
