"""Post-solve confirm (ADR 0006 amendment): bank the completed solve.

Reads the newest solve profile's terminal `Status` and the sweep-point
count from the project results tree, then writes the solved marker to the
machine state (`results/state/solved.txt`: status, sweep_points, banked_at).
Teardown refuses to close a solved workspace's desktop without this marker
(bank-before-teardown, pilot retrospective P-B3/P-E2).

Filesystem-only: imports nothing from pyAEDT and no other workspace
module, so it runs in any Python with no desktop — the solve evidence is
read from disk after the watchdog's terminal line, before any release.

Run:  python src/confirm_solve.py [<project>.aedt]
Project resolution: argv[1] > SOLVE_PROJECT env > the single .aedt in the
workspace dir (the poll_solve contract).

Evidence rules (ground truth: the pilot's `Bowtie3501.results` tree):
- Terminal status: the newest `*.profile` carries the 'Stop Time'
  ProfileFootnote with `'Status', '<value>'`. Mid-run, crashed, or
  never-run trees have no such footnote. Non-"Normal Completion" terminal
  values (e.g. 'Engine Detected Error') ARE banked — the marker's status
  field carries them, and teardown must keep those results too.
- Sweep-point count: `*_SU.txt` files beside the profile sharing its
  `DV<id>` prefix (per-sweep-point outputs; a stale family from an earlier
  solve in the same results dir is excluded).
- In flight: any `*.semaphore` touched AFTER the newest terminal profile
  means a new solve started after that completion — nothing is banked
  then. Semaphores left behind by a kill-based release are older than
  their profile and ignored.

Exit: 0 banked; 2 nothing banked (abort line explains why).
"""

import os
import re
import sys
import time

import profile_evidence

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(WORKSPACE, "results", "state")

# Profile evidence has exactly one parser (ticket 01). This module used to
# carry its own regex, which omitted the escaped quotes AEDT writes and so
# reported "no terminal profile" for every real solve — nothing was ever
# banked, and the teardown guard fell through to purging solved results.
project_results_dir = profile_evidence.project_results_dir
find_profiles = profile_evidence.find_profiles
terminal_status = profile_evidence.terminal_status
newest_terminal_profile = profile_evidence.newest_terminal_profile


def _semaphore_paths(results_root):
    if not os.path.isdir(results_root):
        return []
    found = []
    for dirpath, dirnames, filenames in os.walk(results_root):
        for name in filenames:
            if name.endswith(".semaphore"):
                found.append(os.path.join(dirpath, name))
    return found


def in_flight_semaphores(results_root, newest_terminal_profile_path):
    """`*.semaphore` newer than the newest terminal profile, or [].

    A semaphore touched AFTER the last completion means a new solve
    started afterwards and may still be running. Semaphores older than
    their completion were left by that solve's kill-based release and are
    ignored.
    """
    if not newest_terminal_profile_path:
        return []
    reference = os.path.getmtime(newest_terminal_profile_path)
    live = []
    for path in _semaphore_paths(results_root):
        try:
            if os.path.getmtime(path) > reference:
                live.append(path)
        except OSError:
            pass
    return live


def sweep_point_count(profile_path):
    """`*_SU.txt` beside the profile sharing its `DV<id>` prefix.

    The profile stem carries the run's design id (`DV<digits>_...`); the
    per-point outputs are `DV<id>_<setup>_V<var>_F####_SU.txt` in the same
    results dir. A stale family from an earlier solve carries a different
    DV id and is excluded. Profiles without a DV prefix count every
    `*_SU.txt` in the dir.
    """
    results_dir = os.path.dirname(profile_path)
    stem = os.path.basename(profile_path)
    m = re.match(r"(DV\d+)_", stem)
    prefix = m.group(1) if m else None
    count = 0
    try:
        names = os.listdir(results_dir)
    except OSError:
        return 0
    for name in names:
        if not name.endswith("_SU.txt"):
            continue
        if prefix is None or name.startswith(prefix):
            count += 1
    return count


def confirm(project_path, state_dir=None, now=None):
    """Bank the solve evidence; returns (exit_code, printed_lines).

    `state_dir` and `now` default to the module's state dir and the wall
    clock; both are explicit so the runner tests can drive fixture state.
    """
    root = project_results_dir(project_path)
    lines = []
    profile = newest_terminal_profile(root)
    if profile is None:
        lines.append(
            "confirm_solve aborted: no terminal solve profile under %s — "
            "the solve never ran or is still in flight; nothing banked" % root)
        return 2, lines
    live = in_flight_semaphores(root, profile)
    if live:
        lines.append(
            "confirm_solve aborted: in-flight solve markers under %s are "
            "newer than the last completion — wait for the watchdog's "
            "terminal line; nothing banked" % root)
        return 2, lines
    status = terminal_status(profile)
    sweep_points = sweep_point_count(profile)
    banked_at = int(now if now is not None else time.time())
    state_dir = state_dir or STATE
    os.makedirs(state_dir, exist_ok=True)
    with open(os.path.join(state_dir, "solved.txt"), "w") as f:
        f.write("status=%s\n" % status)
        f.write("sweep_points=%d\n" % sweep_points)
        f.write("banked_at=%d\n" % banked_at)
    lines.append("PASS: confirm_solve banked status=%s sweep_points=%d banked_at=%d"
                 % (status, sweep_points, banked_at))
    if status != "Normal Completion":
        lines.append("! confirm_solve: solve status is NOT 'Normal Completion' (%s) — "
                     "results are banked; escalate per resolve-once" % status)
    return 0, lines


def resolve_project(argv=None):
    """The `.aedt` project path: argv[1] > SOLVE_PROJECT env > one in the workspace."""
    argv = argv if argv is not None else sys.argv
    if len(argv) > 1:
        return os.path.abspath(argv[1])
    env = os.environ.get("SOLVE_PROJECT")
    if env:
        return os.path.abspath(env)
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    matches = [os.path.join(parent, f) for f in os.listdir(parent)
               if f.endswith(".aedt") and not f.endswith(".aedt.lock")]
    if len(matches) == 1:
        return matches[0]
    return None


def main(argv=None):
    argv = argv if argv is not None else sys.argv
    project = resolve_project(argv)
    if not project:
        print("confirm_solve aborted: no project path (pass <project>.aedt or set SOLVE_PROJECT)",
              flush=True)
        return 3
    rc, lines = confirm(project)
    for line in lines:
        print(line, flush=True)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
