"""Detached stage-aware solve watchdog (ADR 0006, amended) — no LLM babysits.

`08_solve.py` submits `analyze(..., blocking=False)` and launches THIS
script detached (`subprocess.Popen(DETACHED_PROCESS)`), then exits. Every
~20 s the watchdog reads two INDEPENDENT observables under
`<project>.aedtresults/`:

  * stage-family artifact growth — `*.imesh` / `*.cmesh` (initial meshing),
    `*_ADP<pass>_*` (adaptive meshing), `*_F<point>_SU.txt` (frequency
    sweep), plus the legacy `.sd` / file / byte counters;
  * the NEWEST `*.profile`'s stage ledger — the ordered
    `Initial Meshing` -> `Adaptive Meshing` -> `Frequency Sweep` groups with
    per-stage elapsed time and adaptive-pass count — and its terminal
    `Status` footnote (a `ProfileFootnote(... 'Status', ...)` line; the
    profile may hold several Solution Process groups, the LAST one counts).

Each tick appends ONE line to `results/state/solve_progress.txt` carrying
stage + evidence (stage-ledger extract, elapsed, family counts). Terminal
states are evidenced before claiming, never guessed:

  complete (exit 0): profile `Status: Normal Completion`, the profile was
    written during THIS watchdog session (freshness guards against a stale
    profile claiming done), and the result tree settled.
  stalled  (exit 2): no growth in the current stage past its window — the
    stage is named in the evidence (catches stuck-at-mesh, stuck-in-adaptive,
    a sweep plateau, and a completion write that never lands).
  aborted  (exit 3): the profile's terminal status is anything other than
    "Normal Completion" — appended VERBATIM to the evidence, and such a
    profile is never claimed complete — or the in-flight semaphores are
    gone with no completion and the solver process is dead (engine death /
    memory exhaustion with no profile to record it).

The sweep-count guess parameter (EXPECTED_SD) is removed entirely —
completion never depends on a predicted output count. This module imports
nothing from pyAEDT and no other workspace module: filesystem + process
observation only (stdlib; psutil IS optional and used solely for the
solver-death probe). It never attaches to a desktop and never kills
anything. On startup it guarantees the `aedt_port.txt` /
`aedt_process_id.txt` files exist (filling "0" only if the launching
session left none — it never overwrites live values) and records its own
pid in `solve_watchdog_pid.txt`.
"""

import os
import re
import sys
import time

import profile_evidence

SLEEP_SECONDS = 20
SETTLE_TICKS = 3          # unchanged ticks after the completion evidence => complete
STALL_TICKS = 30          # default unchanged-tick budget; per-stage below wins
START_TICKS = 45          # no growth at all from the start within this => stalled
DEAD_TICKS = 1            # grown, markers gone, solver dead this many ticks => aborted

# Per-stage stall budgets, in ~20 s ticks (ticket 02). A stage that is
# legitimately quiet for a long time must not be scored against a stage
# that never is: initial meshing on a large model can write nothing for
# many minutes, while sweep points land steadily and the completion write
# follows the last sweep output within seconds. The pilot's false stall
# came from one global window applied to every stage.
STALL_TICKS_BY_STAGE = {
    "initial_meshing": 60,    # ~20 min — meshing is the long quiet one
    "adaptive_meshing": 45,   # ~15 min
    "frequency_sweep": 30,    # ~10 min
    "finalizing": 9,          # ~3 min — the profile lands seconds after the sweep
}

STATUS_RUNNING = "running"
STATUS_COMPLETE = "complete"
STATUS_STALLED = "stalled"
STATUS_ABORTED = "aborted"

STAGE_MESH = "initial_meshing"
STAGE_ADAPTIVE = "adaptive_meshing"
STAGE_SWEEP = "frequency_sweep"
STAGE_FINAL = "finalizing"
STAGE_DONE = "done"

NORMAL_STATUS = profile_evidence.NORMAL_STATUS

_STAGE_NAMES = profile_evidence.STAGE_NAMES
_STAGE_RANK = profile_evidence.STAGE_RANK

# Profile parsing lives in exactly one place (ticket 01). These aliases
# keep the watchdog's own call sites readable and let callers that used to
# reach for `poll_solve.parse_profile` keep working.
project_results_dir = profile_evidence.project_results_dir
parse_profile = profile_evidence.parse_profile
newest_profile = profile_evidence.newest_profile


def family_regexes():
    """(mesh, adp, fsu) name patterns for the stage families."""
    return (re.compile(r"\.imesh$|\.cmesh$"),
            re.compile(r"_ADP\d+"),
            re.compile(r"_F\d+_SU\.txt$"))


def scan_results(root):
    """Stage-family growth under an `.aedtresults` tree.

    One os.walk — no recursive listings ever land in the agent's context.
    Returns a dict with, per family, a (count, bytes) tuple:
      mesh: `*.imesh` / `*.cmesh` files (initial meshing);
      adp:  `*_ADP<pass>_*` entries (adaptive meshing);
      fsu:  `*_F<point>_SU.txt` files (frequency sweep); the bare
            `*_F<point>` dirs co-occur with the SU.txt files in the pilot
            artifacts, so the SU.txt file family is the sweep signal;
      sd:   everything ending `.sd` — directories AND files (HFSS writes
            per-pass `.sd` files and some derived results as dirs).
    Plus `semaphores` (count of `*.semaphore` in-flight markers such as
    `.Design.asol.semaphore` / `.Design.asol_priv.semaphore`), the total
    `files` count and summed `bytes_total`.
    """
    mesh_re, adp_re, fsu_re = family_regexes()
    fam = {"mesh": [0, 0], "adp": [0, 0], "fsu": [0, 0], "sd": [0, 0]}
    semaphores = 0
    files = 0
    bytes_total = 0
    if not os.path.isdir(root):
        return _scan_shape(fam, semaphores, files, bytes_total)
    for dirpath, dirnames, filenames in os.walk(root):
        for name in dirnames:
            # Directory-form artifacts (ticket 02). On this box `.imesh`,
            # `.cmesh` and `_ADP*` are ALWAYS directories — verified across
            # every workspace — so applying the family patterns to files
            # only left `mesh` and `adp` permanently zero and the watchdog
            # blind to stage until sweep files appeared. Directories count
            # once and contribute no bytes of their own; growth inside them
            # still lands in the `files` / `bytes_total` counters.
            for key, rx in (("mesh", mesh_re), ("adp", adp_re), ("fsu", fsu_re)):
                if rx.search(name):
                    fam[key][0] += 1
            if name.endswith(".sd"):
                fam["sd"][0] += 1
        for name in filenames:
            full = os.path.join(dirpath, name)
            try:
                size = os.path.getsize(full)
            except OSError:
                size = 0
            files += 1
            bytes_total += size
            if name.endswith(".semaphore"):
                semaphores += 1
            for key, rx in (("mesh", mesh_re), ("adp", adp_re), ("fsu", fsu_re)):
                if rx.search(name):
                    fam[key][0] += 1
                    fam[key][1] += size
            if name.endswith(".sd"):
                fam["sd"][0] += 1
                fam["sd"][1] += size
    return _scan_shape(fam, semaphores, files, bytes_total)


def _scan_shape(fam, semaphores, files, bytes_total):
    return {"mesh": tuple(fam["mesh"]), "adp": tuple(fam["adp"]),
            "fsu": tuple(fam["fsu"]), "sd": tuple(fam["sd"]),
            "semaphores": semaphores, "files": files, "bytes_total": bytes_total}


def process_alive_default(pid):
    """psutil liveness probe; on ANY doubt report alive (fail closed:
    the watchdog never claims engine death without a reliable answer)."""
    try:
        import psutil
    except ImportError:
        return True
    try:
        proc = psutil.Process(pid)
        return proc.is_running() and proc.status() not in (psutil.STATUS_ZOMBIE,
                                                           psutil.STATUS_DEAD)
    except psutil.Error:
        return False


def solver_alive(state_dir, process_alive=None):
    """The solver process recorded by the launching session, or None if
    the pid file is absent / empty (unknown != dead)."""
    if process_alive is None:
        process_alive = process_alive_default
    path = os.path.join(state_dir, "aedt_process_id.txt")
    try:
        with open(path) as f:
            pid = int(f.read().strip() or "0")
    except (OSError, ValueError):
        return None
    if pid <= 0:
        return None
    try:
        return bool(process_alive(pid))
    except Exception:
        return True


def observe(root, state_dir, process_alive=None):
    """One scan's observation: family counts + newest profile + solver.

    `process_alive(pid)` is injectable so the no-AEDT tests can drive the
    engine-death path without any real process.
    """
    obs = dict(scan_results(root))
    pair = newest_profile(root)
    profile_path, profile_mtime = pair if pair else (None, None)
    stages, status, stop = parse_profile(profile_path) if profile_path else ([], None, None)
    obs.update({"profile_path": profile_path, "profile_mtime": profile_mtime,
                "profile_stages": stages, "profile_status": status,
                "profile_stop": stop,
                "solver_alive": solver_alive(state_dir, process_alive)})
    return obs


def _growth_tuple(obs):
    return (obs["mesh"], obs["adp"], obs["fsu"], obs["sd"],
            obs["files"], obs["bytes_total"])


def _anything_written(obs):
    written = (obs["mesh"][0] + obs["mesh"][1] + obs["adp"][0] + obs["adp"][1] +
               obs["fsu"][0] + obs["fsu"][1] + obs["sd"][0] + obs["sd"][1] +
               obs["files"])
    return written > 0 or obs["profile_mtime"] is not None


def stage_floor(cur):
    """Best-evidenced stage rank 0..2 from families + profile ledger."""
    rank = 0
    if cur["adp"][0] > 0:
        rank = max(rank, 1)
    if cur["fsu"][0] > 0:
        rank = max(rank, 2)
    for name, _elapsed, _passes in cur["profile_stages"]:
        rank = max(rank, _STAGE_RANK.get(name, 0))
    return rank


def stage_token(floor):
    if floor >= 2:
        return STAGE_SWEEP
    if floor >= 1:
        return STAGE_ADAPTIVE
    return STAGE_MESH


def format_stage_ledger(stages):
    """The stage ledger extract for the progress line, e.g.
    `Initial_Meshing:00:00:02,Adaptive_Meshing:00:00:15:6p,Frequency_Sweep:00:03:58`
    (name:elapsed[:Np for adaptive passes]); `-` when no profile yet."""
    tokens = []
    for name, elapsed, passes in stages:
        token = name.replace(" ", "_")
        if elapsed:
            token += ":" + elapsed
        if passes:
            token += ":%dp" % passes
        tokens.append(token)
    return ",".join(tokens) if tokens else "-"


def profile_status_token(status):
    """Machine token for the profile's terminal status line."""
    if not status:
        return "-"
    if status == NORMAL_STATUS:
        return "normal_completion"
    return re.sub(r"[^A-Za-z0-9]+", "_", status.lower()).strip("_")


def watchdog_tick(prev, cur, state, cfg):
    """One ~20 s decision step; pure.

    `cur` is an observation dict from `observe()`; `cfg` may override the
    windows (settle_ticks / stall_ticks / start_ticks / dead_ticks).
    Returns (status, stage, evidence, state):
      status:  running | complete | stalled | aborted
      stage:   initial_meshing | adaptive_meshing | frequency_sweep |
               finalizing | done
      evidence: free text appended to the progress line — the profile's
               verbatim Status footnote on any terminal claim, the stuck
               stage on a stall, the death cause on an abort (None while
               simply running).
    """
    settle = cfg.get("settle_ticks", SETTLE_TICKS)
    start = cfg.get("start_ticks", START_TICKS)
    dead = cfg.get("dead_ticks", DEAD_TICKS)
    stage_windows = dict(STALL_TICKS_BY_STAGE)
    stage_windows.update(cfg.get("stall_ticks_by_stage", {}))
    default_stall = cfg.get("stall_ticks", STALL_TICKS)

    ps = cur["profile_status"]
    # Baseline = the newest profile's mtime at watchdog start (None if no
    # profile existed then). Locked once: a profile that appears later was
    # written THIS session; a rewrite bumps the mtime and is also fresh.
    if "profile_baseline" not in state:
        state["profile_baseline"] = cur["profile_mtime"]
    baseline = state["profile_baseline"]
    fresh = cur["profile_mtime"] is not None and (
        baseline is None or cur["profile_mtime"] > baseline)

    # Terminal claim 1 — engine / solver error recorded in the profile.
    # The moment a non-Normal terminal Status appears (fresh profile write)
    # the solve is over and it is NOT complete; append the status verbatim.
    if ps is not None and ps != NORMAL_STATUS and fresh:
        return (STATUS_ABORTED, STAGE_DONE,
                "profile status: %s (non-Normal; never complete)" % ps, state)

    changed = prev is None or _growth_tuple(cur) != _growth_tuple(prev)
    if changed:
        state["unchanged"] = 0
        if prev is not None or _anything_written(cur):
            state["grown"] = True
    else:
        state["unchanged"] += 1

    if cur["semaphores"] > 0:
        state["sem_ever"] = True
    sem_gone = state.get("sem_ever") and cur["semaphores"] == 0

    floor = stage_floor(cur)
    stage = stage_token(floor)
    # Sweep outputs done and the completion write not yet observed: the
    # pilot's profile lands ~seconds after the last sweep file, so one
    # quiet tick with sweep evidence is already "finalizing".
    if floor >= 2 and state.get("grown") and state["unchanged"] >= 1 \
            and ps is None:
        stage = STAGE_FINAL

    # Terminal claim 2 — completion: profile says Normal Completion, the
    # profile was written this session, and the tree settled.
    if (ps == NORMAL_STATUS and fresh and state.get("grown") and
            state["unchanged"] >= settle):
        evidence = ("profile status: %s (stop %s)" %
                    (ps, cur.get("profile_stop") or "?"))
        return STATUS_COMPLETE, STAGE_DONE, evidence, state

    # Terminal claim 3 — never grew: submit never picked up, or the engine
    # died before writing a single output.
    if not state.get("grown") and state["unchanged"] >= start:
        if cur["solver_alive"] is False:
            return (STATUS_ABORTED, STAGE_DONE,
                    "solver process dead, no in-flight markers, no "
                    "completion (never grew)", state)
        return (STATUS_STALLED, stage,
                "no growth since watchdog start for %d ticks (window %d) in "
                "stage %s — submit never picked up or meshing stuck before "
                "the first output" % (state["unchanged"], start, stage), state)

    # Terminal claim 4 — engine death mid-solve: in-flight markers gone,
    # no completion, solver process dead. A Normal Completion profile wins
    # over this branch even before its settle window elapses.
    if (state.get("grown") and state["unchanged"] >= dead and
            ps != NORMAL_STATUS and cur["solver_alive"] is False and sem_gone):
        return (STATUS_ABORTED, stage,
                "solver process dead, in-flight markers gone, no completion "
                "— aborted while in stage %s" % stage, state)

    # Terminal claim 5 — stall: no growth in the current stage past its
    # window; the stage is named so a mesh stuck forever and a running
    # sweep never look alike. A FRESH Normal Completion write awaits its
    # settle instead; a stale one (not written this session) may stall.
    # The window is the CURRENT stage's budget (ticket 02). An explicit
    # `stall_ticks` in cfg is a blanket override, which is how the tests
    # drive short windows.
    stall = (cfg["stall_ticks"] if "stall_ticks" in cfg
             else stage_windows.get(stage, default_stall))
    if state.get("grown") and \
            not (ps == NORMAL_STATUS and fresh) and \
            state["unchanged"] >= stall:
        return (STATUS_STALLED, stage,
                "no growth for %d unchanged ticks (window %d) in stage %s — "
                "not complete" % (state["unchanged"], stall, stage), state)

    return STATUS_RUNNING, stage, None, state


def format_progress(tick_no, status, stage, cur, evidence, unchanged_ticks,
                    elapsed_s, started_at):
    """One `solve_progress.txt` line — the agent's only solve signal.
    Stage + evidence: stage-ledger extract, elapsed, family counts;
    terminal lines carry the evidence tail (profile Status verbatim)."""
    parts = [
        "tick=%d" % tick_no,
        "status=%s" % status,
        "stage=%s" % stage,
        "elapsed_s=%d" % int(elapsed_s),
        "mesh=%d" % cur["mesh"][0],
        "adp=%d" % cur["adp"][0],
        "fsu=%d" % cur["fsu"][0],
        "sd=%d" % cur["sd"][0],
        "files=%d" % cur["files"],
        "bytes=%d" % cur["bytes_total"],
        "unchanged_ticks=%d" % unchanged_ticks,
        "semaphores=%d" % cur["semaphores"],
        "stage_ledger=%s" % format_stage_ledger(cur["profile_stages"]),
        "profile_status=%s" % profile_status_token(cur["profile_status"]),
        "watchdog_started=%d" % int(started_at),
    ]
    if evidence:
        parts.append("evidence=%s" % evidence)
    return " ".join(parts)


def resolve_project(argv=None):
    """The `.aedt` project path: argv[1] > SOLVE_PROJECT env > one in parent dir."""
    argv = argv or sys.argv
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
        print("watchdog aborted: no project path (pass <project>.aedt or set SOLVE_PROJECT)", flush=True)
        return 3
    workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    state_dir = os.path.join(workspace, "results", "state")
    os.makedirs(state_dir, exist_ok=True)
    progress = os.path.join(state_dir, "solve_progress.txt")

    # State-file writebacks (ADR 0006): the watchdog's startup guarantees
    # the pinned-port/pid records EXIST for the solve session's attach and
    # teardown (08_solve wrote their live values before launching it; the
    # watchdog only fills in "0" if they are missing) and records its own
    # pid in solve_watchdog_pid.txt for whoever launched it.
    with open(os.path.join(state_dir, "solve_watchdog_pid.txt"), "w") as f:
        f.write(str(os.getpid()))
    for key in ("aedt_port", "aedt_process_id"):
        path = os.path.join(state_dir, key + ".txt")
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("0")

    started = time.time()
    prev = None
    state = {"grown": False, "unchanged": 0, "sem_ever": False}
    tick_no = 0
    status = STATUS_RUNNING
    stage = STAGE_MESH
    evidence = None
    while True:
        cur = observe(project_results_dir(project), state_dir)
        status, stage, evidence, state = watchdog_tick(prev, cur, state, {})
        line = format_progress(tick_no, status, stage, cur, evidence,
                               state.get("unchanged", 0),
                               time.time() - started, started)
        with open(progress, "a") as f:
            f.write(line + "\n")
        print(line, flush=True)
        if status != STATUS_RUNNING:
            print("watchdog exit:", status, flush=True)
            return {STATUS_COMPLETE: 0, STATUS_STALLED: 2, STATUS_ABORTED: 3}[status]
        prev = cur
        tick_no += 1
        time.sleep(SLEEP_SECONDS)


if __name__ == "__main__":
    raise SystemExit(main())
