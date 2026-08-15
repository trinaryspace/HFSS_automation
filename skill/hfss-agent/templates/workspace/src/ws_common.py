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

Resume discipline (ADR 0007, pilot retrospective B5): resumes attach by
the pinned port through a BOUNDED CONNECT (short timeout, never a hanging
attach). A pinned desktop that answers nothing is a stale pin: it is
cleared — never attached against, never probed onto — and a fresh desktop
is launched and re-pinned.

Fill PROJECT and DESIGN when the workspace is created (the template can't
know them). Keep all other script paths derived from this module.
"""

import os
import socket

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


STALE_PIN_TIMEOUT = 2.0  # bounded connect (seconds): a dead pin must fail fast, never hang


def _pin_probe(port, host="127.0.0.1", timeout=None):
    """Bounded liveness probe of the pinned gRPC port; pure socket, no AEDT.

    Returns True only when the pinned address accepts a TCP connect within
    the timeout (default `STALE_PIN_TIMEOUT`). A dead pinned desktop
    (connection refused, unrouteable, or silent to the timeout) returns
    False fast — the caller clears the pin instead of handing the stale
    port to a pyAEDT attach that could hang or spawn an unattended desktop.
    """
    if not port:
        return False
    if timeout is None:
        timeout = STALE_PIN_TIMEOUT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, int(port)))
        except OSError:
            return False
    return True


def attach(launch=False, probe=None):
    """Attach to the pinned workspace desktop, or launch a fresh one.

    Port-pinned: the recorded `aedt_port` is used both to attach and to
    record the writeback, so a session never drifts onto another desktop.

    Resume (pilot retrospective B5): an attach with a recorded pin first
    runs the bounded connect. A dead pin prints the `stale pin — re-pinning`
    verdict, is cleared (port and process id), and a fresh desktop is
    launched and re-pinned — a stale pin is never attached against, never
    probed, and the session never hangs on it. `probe` is injectable for
    tests; default is the socket probe above.
    """
    probe = probe or _pin_probe
    os.makedirs(STATE, exist_ok=True)
    port = _session_port()
    if not launch and port and not probe(port):
        print(
            "stale pin: aedt_port=%d has no live desktop (bounded connect "
            "timed out / refused) — clearing the pin and re-pinning "
            "(no hanging attach)" % port,
            flush=True,
        )
        write_state("aedt_port", "0")
        write_state("aedt_process_id", "0")
        port = 0
        launch = True
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


GUARD_BANKED = "banked"
GUARD_REFUSE = "refuse"
GUARD_PROCEED = "proceed"


def guard_verdict(project, state_dir=None):
    """Bank-before-teardown decision (ADR 0006 amendment); filesystem only.

        banked  — the solved marker (`results/state/solved.txt`) exists:
                  teardown keeps the project and results on disk
                  (`close_projects=False`) and still reaps the pinned
                  process.
        refuse  — unbanked but solve evidence on disk (the newest profile
                  carries a terminal Status and no in-flight semaphores):
                  teardown must not run until the post-solve confirm
                  banks it — releasing now would purge the solved results.
        proceed — neither: exactly today's teardown. Build-phase, verify-
                  copy, and mid-flight (fresh semaphores, no completion)
                  workspaces land here.

    Imported lazily so the verdict shares `confirm_solve`'s parsing — solve
    evidence means the same thing to the bank and to the guard.
    """
    state_dir = state_dir or STATE
    if os.path.isfile(os.path.join(state_dir, "solved.txt")):
        return GUARD_BANKED

    import confirm_solve

    root = confirm_solve.project_results_dir(project)
    if not os.path.isdir(root):
        return GUARD_PROCEED
    profile = confirm_solve.newest_terminal_profile(root)
    if profile is None:
        return GUARD_PROCEED
    if confirm_solve.in_flight_semaphores(root, profile):
        return GUARD_PROCEED
    return GUARD_REFUSE


def teardown():
    """End of session: guarded release and reap of the PINNED desktop only.

    Safety contract: without a recorded pinned port this refuses to touch
    any desktop — release is issued only through `Desktop(port=<pinned>)`,
    and the launched process is killed only by the recorded
    `aedt_process_id` of that pinned desktop. It can never close or kill
    the user's own desktop.

    Bank-before-teardown (ADR 0006 amendment): the verdict comes first.
    A banked workspace releases with `close_projects=False` (the project
    and its results stay on disk) and still reaps the pinned process; an
    unbanked workspace that shows solve evidence on disk is refused with
    the "bank it first" message and a non-zero exit WITHOUT touching the
    desktop — releasing would purge the solved results; anything else
    tears down exactly as today (`close_projects=True`).
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
    verdict = guard_verdict(PROJECT)
    if verdict == GUARD_REFUSE:
        print(
            "teardown refused: solve evidence on disk is NOT banked — "
            "tearing down would purge the solved results. Bank it first: "
            "python src/confirm_solve.py %s, then re-run teardown." % PROJECT,
            flush=True,
        )
        sys.stdout.flush()
        os._exit(2)
    close_projects = verdict != GUARD_BANKED
    if close_projects:
        print("teardown: unguarded release (close_projects=True)", flush=True)
    else:
        print("teardown: banked workspace — projects left on disk (close_projects=False)",
              flush=True)
    try:
        from ansys.aedt.core import Desktop

        d = Desktop(version=AEDT_VERSION, new_desktop=False, port=port)
        d.release_desktop(close_projects=close_projects, close_on_exit=True)
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
    # `pid` is None when no process id was ever recorded. `int(None)` raises
    # TypeError, which is not caught below, so the function used to die here
    # WITHOUT reaching os._exit(0) — and os._exit is the only reason gRPC
    # teardown does not hang. A missing pid is "nothing to reap", not a crash.
    print("teardown: server process gone =", end=" ", flush=True)
    if not pid or pid == "0":
        print("True (no server process was recorded)", flush=True)
    else:
        try:
            psutil.Process(int(pid)).status()
            print("False", flush=True)
        except (psutil.NoSuchProcess, ValueError, TypeError):
            print("True", flush=True)
    sys.stdout.flush()
    os._exit(0)
