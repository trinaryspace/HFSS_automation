"""The single parser for AEDT solve-profile evidence (ticket 01).

Every consumer of profile evidence imports this module — the watchdog
(`poll_solve`), the post-solve bank (`confirm_solve`), and the teardown
guard (`ws_common`). Before this module existed there were two parsers
with different regexes, and they disagreed on 9 of 9 real profiles on this
box: `confirm_solve`'s omitted the escaped quotes AEDT actually writes, so
it returned `None` for every completed solve, `guard_verdict()` fell
through to `proceed`, and teardown purged solved results. Solve evidence
now means the same thing to every consumer because there is only one
implementation of what it means.

Ground truth (pinned by `fixtures/real/`, captured from this box):

- Footnote strings serialize with **escaped quotes** and land at the
  Solution Process level after the stage groups have closed:
  `ProfileFootnote('I(2, 1, \\'Stop Time\\', \\'..\\', 1, \\'Status\\', \\'..\\')', 0)`.
  The regexes here tolerate both the escaped and the bare form.
- A profile file may hold **several `Solution Process` groups** (an engine
  error followed by a re-run of the same variation). The LAST group is
  terminal: entering a new one resets the accumulated evidence.
- Group nesting is driven only by `ProfileGroup` blocks. `StartInfo` and
  `TotalInfo` are different block types and never affect depth.
- The profile is written at the END of a solve, not per stage, so a
  profile's presence is terminal evidence, not progress evidence.

Stdlib only: no pyAEDT import, no desktop attach, no side effects.
"""

import os
import re

NORMAL_STATUS = "Normal Completion"

STAGE_NAMES = ("Initial Meshing", "Adaptive Meshing", "Frequency Sweep")
STAGE_RANK = {"Initial Meshing": 0, "Adaptive Meshing": 1, "Frequency Sweep": 2}

_SOLUTION_GROUP = "Solution Process"

_NAME_RE = re.compile(r"Name='([^']+)'")
_ELAPSED_RE = re.compile(r"\\?'Elapsed Time\\?'\s*,\s*\\?'([^'\\]+)")
# `\\?'` tolerates both `'Status'` and the escaped `\'Status\'` AEDT writes.
_STATUS_RE = re.compile(r"\\?'Status\\?'\s*,\s*\\?'([^'\\]+)")
_STOP_RE = re.compile(r"\\?'Stop Time\\?'\s*,\s*\\?'([^'\\]+)")


def parse_profile(path):
    """`(stages, status, stop)` for the LAST Solution Process group.

    `stages` is the ordered list of `(name, elapsed, passes)` for the stage
    groups that CLOSED inside that group — a stage still being written is
    not reported, which is correct: the profile only exists once the solve
    has ended. `status` / `stop` are the terminal footnote values, or None
    when the profile carries none (mid-write or crashed).
    """
    stages = []
    status = None
    stop = None
    stack = []
    solution_depth = None
    stage_depth = None
    stage_name = None
    elapsed = None
    passes = 0
    if not path or not os.path.isfile(path):
        return stages, status, stop
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if "$begin 'ProfileGroup'" in line:
                stack.append(None)
                continue
            if "$end 'ProfileGroup'" in line and stack:
                closed = stack.pop()
                if closed == _SOLUTION_GROUP:
                    solution_depth = None
                    stage_depth = None
                    stage_name = None
                    elapsed = None
                    passes = 0
                elif closed in STAGE_NAMES:
                    stages.append((stage_name, elapsed, passes))
                    stage_depth = None
                    stage_name = None
                    elapsed = None
                    passes = 0
                continue
            if stack and stack[-1] is None:
                match = _NAME_RE.search(line)
                if match:
                    name = match.group(1)
                    stack[-1] = name
                    if name == _SOLUTION_GROUP:
                        # A later Solution Process group supersedes earlier
                        # ones: the engine-error-then-rerun case.
                        stages = []
                        status = None
                        stop = None
                        solution_depth = len(stack)
                        stage_depth = None
                        stage_name = None
                        elapsed = None
                        passes = 0
                    elif solution_depth is not None:
                        if name in STAGE_NAMES:
                            stage_depth = len(stack)
                            stage_name = name
                            elapsed = None
                            passes = 0
                        elif name.startswith("Adaptive Pass"):
                            passes += 1
                    continue
            if solution_depth is not None:
                if stage_depth is not None:
                    match = _ELAPSED_RE.search(line)
                    if match:
                        elapsed = match.group(1)
                match = _STATUS_RE.search(line)
                if match:
                    status = match.group(1).strip()
                match = _STOP_RE.search(line)
                if match:
                    stop = match.group(1).strip()
    return stages, status, stop


def terminal_status(path):
    """The profile's terminal Status value, or None when unfinished."""
    _stages, status, _stop = parse_profile(path)
    return status


def is_normal_completion(path):
    """True only for a profile whose terminal Status is Normal Completion."""
    return terminal_status(path) == NORMAL_STATUS


def find_profiles(results_root):
    """All `*.profile` under the tree, newest mtime first."""
    found = []
    if not results_root or not os.path.isdir(results_root):
        return found
    for dirpath, _dirnames, filenames in os.walk(results_root):
        for name in filenames:
            if name.endswith(".profile"):
                full = os.path.join(dirpath, name)
                try:
                    found.append((os.path.getmtime(full), full))
                except OSError:
                    continue
    found.sort(reverse=True)
    return [path for (_mtime, path) in found]


def newest_profile(results_root):
    """`(path, mtime)` of the newest profile under the tree, else None."""
    paths = find_profiles(results_root)
    if not paths:
        return None
    try:
        return paths[0], os.path.getmtime(paths[0])
    except OSError:
        return None


def newest_terminal_profile(results_root):
    """Newest profile carrying a terminal Status, else None.

    A mid-write or crashed newest profile is skipped in favour of the
    newest one that did finish: an older completion is still solve
    evidence, and the teardown guard must protect those results.
    """
    for path in find_profiles(results_root):
        if terminal_status(path) is not None:
            return path
    return None


def project_results_dir(project_path):
    """AEDT results folder for a project: `<project>.aedtresults`."""
    return project_path + "results"
