"""Shared constants, state files, and port-pinned attach/launch preamble.

Every staged script imports this module. Session state lives in the AEDT
project, never in a Python process; machine state that must survive between
phase sessions lives in `results/state/*.txt` (ADR 0007).

Port-pinning (ADR 0006/0008, seeded by the silent-engine run): the desktop
launched for this workspace records its gRPC port and process id in
`results/state/aedt_port.txt` / `aedt_process_id.txt`, and every later
attach AND every teardown reconnects by that recorded port. A teardown
without a recorded port refuses to act — it can never close or kill a
desktop it does not own (never the user's own desktop).

Fill PROJECT and DESIGN when the workspace is created (the template can't
know them). Keep all other script paths derived from this module.
"""

import os

from ansys.aedt.core import Desktop, Hfss

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TODO(workspace creation): fill in the project file name inside this workspace.
PROJECT = os.path.join(WORKSPACE, "<workspace_name>.aedt")
RESULTS = os.path.join(WORKSPACE, "results")
STATE = os.path.join(RESULTS, "state")  # gitignored via workspaces/*/results/

DESIGN = "<DesignName>"
SOLUTION_TYPE = "<Modal|Terminal|Transient|...>"  # explicit, never the default (env-compat #11)
AEDT_VERSION = "2024.1"

os.makedirs(RESULTS, exist_ok=True)


def write_state(key, value):
    """Write one machine-state file: `results/state/<key>.txt`."""
    with open(os.path.join(STATE, key + ".txt"), "w") as f:
        f.write(str(value))


def read_state(key):
    """Read one machine-state file; None when absent."""
    try:
        with open(os.path.join(STATE, key + ".txt")) as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def attach(launch=False):
    """Attach to the pinned workspace desktop, or launch a fresh one.

    Port-pinned: the recorded `aedt_port` is used both to attach and to
    record the writeback, so a session never drifts onto another desktop.
    """
    os.makedirs(STATE, exist_ok=True)
    port = _session_port()
    if launch:
        hfss = Hfss(
            version=AEDT_VERSION,
            new_desktop=True,
            non_graphical=False,
            project=PROJECT,
            design=DESIGN,
            solution_type=SOLUTION_TYPE,
            remove_lock=True,
        )
    elif port:
        Desktop(version=AEDT_VERSION, new_desktop=False, port=port)
        hfss = Hfss(
            project=PROJECT,
            design=DESIGN,
            solution_type=SOLUTION_TYPE,
            new_desktop=False,
            port=port,
            remove_lock=True,
        )
    else:
        # No pinned port recorded: attach wherever a desktop is listening.
        # Attaching is safe (read-only wrt other desktops); teardown is not.
        Desktop(version=AEDT_VERSION, new_desktop=False)
        hfss = Hfss(
            project=PROJECT,
            design=DESIGN,
            solution_type=SOLUTION_TYPE,
            new_desktop=False,
            remove_lock=True,
        )

    if launch:
        # A fresh desktop: its own port/pid is the truth, never a stale pin.
        live_port = getattr(hfss.desktop_class, "port", 0) or 0
        live_pid = str(getattr(hfss.desktop_class, "aedt_process_id", "0") or "0")
    else:
        live_port = getattr(hfss.desktop_class, "port", 0) or _session_port()
        live_pid = (
            getattr(hfss.desktop_class, "aedt_process_id", "0")
            or read_state("aedt_process_id")
            or "0"
        )
    write_state("aedt_port", str(live_port))
    write_state("aedt_process_id", str(live_pid))
    return hfss


def _session_port():
    try:
        return int(read_state("aedt_port") or 0)
    except ValueError:
        return 0


def exit_keep_alive():
    """End a staged script leaving the pinned desktop (and project) alive."""
    import sys

    sys.stdout.flush()
    os._exit(0)


def teardown():
    """End of session: release and reap the PINNED desktop only.

    Safety contract: without a recorded pinned port this refuses to touch
    any desktop — release is issued only through `Desktop(port=<pinned>)`,
    and the launched process is killed only by the recorded
    `aedt_process_id` of that pinned desktop. It can never close or kill
    the user's own desktop.
    """
    import sys
    import time

    import psutil

    pid = read_state("aedt_process_id")
    port = _session_port()
    if not port:
        print(
            "teardown aborted: no pinned aedt_port recorded — "
            "refusing to close any desktop",
            flush=True,
        )
        sys.stdout.flush()
        os._exit(0)
    try:
        from ansys.aedt.core import Desktop

        d = Desktop(version=AEDT_VERSION, new_desktop=False, port=port)
        d.release_desktop(close_projects=True, close_on_exit=True)
    except Exception as e:  # noqa: BLE001 - best effort
        print("release exception:", type(e).__name__, str(e)[:200], flush=True)
    if pid and pid != "0":
        deadline = time.time() + 30
        while time.time() < deadline:
            try:
                p = psutil.Process(int(pid))
            except (psutil.NoSuchProcess, ValueError):
                break
            try:
                p.kill()
            except psutil.AccessDenied:
                pass
            time.sleep(1)
    print("teardown: server process gone =", end=" ", flush=True)
    try:
        psutil.Process(int(pid)).status()
        print("False", flush=True)
    except (psutil.NoSuchProcess, ValueError):
        print("True", flush=True)
    sys.stdout.flush()
    os._exit(0)
