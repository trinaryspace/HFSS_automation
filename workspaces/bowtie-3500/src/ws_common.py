"""Shared constants, state file, and attach/launch preamble for staged scripts."""

import os

from ansys.aedt.core import Desktop, Hfss

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT = os.path.join(WORKSPACE, "bowtie_3500.aedt")
RESULTS = os.path.join(WORKSPACE, "results")
STATE = os.path.join(RESULTS, "state")  # gitignored via workspaces/*/results/

DESIGN = "Bowtie3500"
SOLUTION_TYPE = "Modal"  # explicit, never the default (EC#11)
AEDT_VERSION = "2024.1"

os.makedirs(RESULTS, exist_ok=True)


def write_state(key, value):
    with open(os.path.join(STATE, key + ".txt"), "w") as f:
        f.write(str(value))


def read_state(key):
    try:
        with open(os.path.join(STATE, key + ".txt")) as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def attach(launch=False):
    """Attach to the running desktop, or launch a fresh one (first stage).

    Returns the Hfss handle with the active design open.
    """
    os.makedirs(STATE, exist_ok=True)
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
        port = getattr(hfss.desktop_class, "port", 0)
    else:
        port = _session_port()
        if port:
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
            Desktop(version=AEDT_VERSION, new_desktop=False)
            hfss = Hfss(
                project=PROJECT,
                design=DESIGN,
                solution_type=SOLUTION_TYPE,
                new_desktop=False,
                remove_lock=True,
            )
    write_state("aedt_port", str(port))
    write_state("aedt_process_id", getattr(hfss.desktop_class, "aedt_process_id", "0"))
    return hfss


def _session_port():
    try:
        return int(read_state("aedt_port") or 0)
    except ValueError:
        return 0


def exit_keep_alive():
    """End a staged script leaving the desktop (and its project) alive."""
    import sys

    sys.stdout.flush()
    os._exit(0)


def teardown():
    """End of session: release desktop, kill server process until gone (EC#10)."""
    import sys
    import time

    import psutil

    pid = read_state("aedt_process_id")
    try:
        from ansys.aedt.core import Desktop

        d = Desktop(version=AEDT_VERSION, new_desktop=False)
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
