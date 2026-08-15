"""Stage-aware watchdog tests at the no-AEDT seam (ticket 14).

Synthetic result trees drive `observe()` + `watchdog_tick()` through every
stage sequence and each documented terminal path:

  * full run: initial_meshing -> adaptive_meshing -> frequency_sweep ->
    finalizing -> done (complete, exit 0 semantics)
  * engine-error profile: aborted, status appended verbatim — NEVER complete
  * error-then-rerun profile (two Solution Process groups): last group wins
  * stuck-at-mesh / stuck-in-adaptive: stalled with the stage in evidence
  * engine death mid-sweep: in-flight markers gone + no completion + solver
    process dead => aborted
  * never-grew paths: solver alive => stalled, solver dead => aborted
  * stale profile freshness: a profile not written this session never claims
    completion

No pyAEDT, no license, no desktop: the module under test imports only the
standard library (psutil optional).

Run:  python src/test_poll_solve_stages.py
"""

import importlib.util
import os
import shutil
import sys
import tempfile
import time
import unittest

SRC = os.path.dirname(os.path.abspath(__file__))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

import real_fixtures  # noqa: E402  (needs SRC on the path)


def load(name):
    spec = importlib.util.spec_from_file_location("t14_" + name, os.path.join(SRC, name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def solution_group(stages, status=None, stop=None):
    """A `Solution Process` group chunk: stages are (name, elapsed, kids)."""
    lines = ["\t$begin 'ProfileGroup'",
             "\t\tMajorVer=2024",
             "\t\tMinorVer=1",
             "\t\tName='Solution Process'",
             "\t\t$begin 'StartInfo'",
             "\t\t\tI(1, 'Start Time', '08/07/2026 00:44:07')",
             "\t\t$end 'StartInfo'",
             "\t\t$begin 'TotalInfo'",
             "\t\t\tI(1, 'Elapsed Time', '00:04:17')",
             "\t\t$end 'TotalInfo'"]
    for name, elapsed, kids in stages:
        lines.append("\t\t$begin 'ProfileGroup'")
        lines.append("\t\t\tMajorVer=2024")
        lines.append("\t\t\tName='%s'" % name)
        lines.append("\t\t\t$begin 'StartInfo'")
        lines.append("\t\t\t\tI(1, 'Time', '08/07/2026 00:44:09')")
        lines.append("\t\t\t$end 'StartInfo'")
        lines.append("\t\t\t$begin 'TotalInfo'")
        lines.append("\t\t\t\tI(1, 'Elapsed Time', '%s')" % elapsed)
        lines.append("\t\t\t$end 'TotalInfo'")
        for kid in kids:
            lines.append("\t\t\t$begin 'ProfileGroup'")
            lines.append("\t\t\t\tMajorVer=2024")
            lines.append("\t\t\t\tName='%s'" % kid)
            lines.append("\t\t\t$end 'ProfileGroup'")
        lines.append("\t\t$end 'ProfileGroup'")
    if status:
        # HFSS serializes footnote strings with escaped quotes and puts the
        # terminal Status at the Solution Process level, after the stages.
        lines.append("\t\tProfileFootnote('I(2, 1, \\'Stop Time\\', \\'%s\\', "
                     "1, \\'Status\\', \\'%s\\')', 0)" % (stop, status))
    lines.append("\t$end 'ProfileGroup'")
    return "\n".join(lines)


def profile_text(groups):
    """One `.profile` file text; `groups` is a list of solution_group texts."""
    return "$begin 'Profile'\n" + "\n".join(groups) + "\n$end 'Profile'"


FULL_STAGES = [
    ("Initial Meshing", "00:00:02", ["Mesh", "Port Adapt"]),
    ("Adaptive Meshing", "00:00:17",
     ["Adaptive Pass 1", "Adaptive Pass 2", "Adaptive Pass 3",
      "Adaptive Pass 4", "Adaptive Pass 5", "Adaptive Pass 6"]),
    ("Frequency Sweep", "00:03:58",
     ["Solution - Sweep_3U94XF", "Frequency - 4.2GHz"]),
]


class StageFixture(object):
    """A synthetic `.aedtresults` tree + state dir + fake process probe."""

    def __init__(self, tmp):
        self.tmp = tmp
        self.root = os.path.join(tmp, "probe.aedtresults")
        self.state_dir = os.path.join(tmp, "results", "state")
        os.makedirs(self.root)
        os.makedirs(self.state_dir)
        with open(os.path.join(self.state_dir, "aedt_process_id.txt"), "w") as f:
            f.write("9999")
        self.alive = [True]

    def probe(self, pid):
        return self.alive[0]

    def write(self, name, body="x"):
        with open(os.path.join(self.root, name), "w") as f:
            f.write(body)

    def write_profile(self, name, groups):
        with open(os.path.join(self.root, name), "w") as f:
            f.write(profile_text(groups))

    def write_dir(self, name, inner=None, body="x"):
        """A directory-form artifact, as AEDT actually writes them.

        `.imesh` / `.cmesh` / `_ADP*` are directories on this box, each
        holding its own payload files (`current.ngmesh`, `native.adp`, ...).
        Growth therefore shows up as new directories AND as bytes inside
        them — writing these as flat files, as this fixture used to, made
        the ticket-02 bug invisible.
        """
        path = os.path.join(self.root, name)
        os.makedirs(path, exist_ok=True)
        if inner:
            with open(os.path.join(path, inner), "w") as handle:
                handle.write(body)
        return path

    def add_mesh(self, variant="V1"):
        self.write_dir("DV3019_V%s.imesh" % variant, inner="current.ngmesh")
        self.write_dir("DV3019_S1911_V%s.cmesh" % variant, inner="current.stats")

    def add_adp(self, pass_no, variant="V2"):
        self.write_dir("DV3019_S1911_ADP%d_V%s.sd" % (pass_no, variant),
                       inner="native.adp", body="a" * (1 + pass_no))

    def add_fsu(self, point, variant="V3"):
        self.write("DV3019_S1918_V%s_F%d_SU.txt" % (variant, point),
                   body="s" * point)

    def add_sd(self, name):
        self.write(name, body="d")

    def add_semaphore(self, design="DV3019"):
        self.write(".%s.asol.semaphore" % design)

    def observe(self):
        return poll_solve.observe(self.root, self.state_dir, self.probe)


poll_solve = load("poll_solve")


def tick(cur, prev=None, state=None, **cfg):
    defaults = {"settle_ticks": 2, "stall_ticks": 5, "start_ticks": 5,
                "dead_ticks": 1}
    defaults.update(cfg)
    state = state if state is not None else {"grown": False, "unchanged": 0,
                                             "sem_ever": False}
    return poll_solve.watchdog_tick(prev, cur, state, defaults)


class TestStageSequenceFromSyntheticTree(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.fx = StageFixture(self.tmp)
        self.prev = None
        self.state = {"grown": False, "unchanged": 0, "sem_ever": False}
        self.lines = []

    def step(self, mutate=None):
        if mutate:
            mutate()
        cur = self.fx.observe()
        status, stage, evidence, self.state = tick(
            cur, self.prev, self.state)
        self.lines.append((status, stage, evidence))
        self.prev = cur
        return status, stage, evidence

    def test_full_sequence_to_complete(self):
        stages_seen = []
        for status, stage, _ in [
                self.step(lambda: self.fx.add_mesh()),
                self.step(lambda: self.fx.add_mesh("V1b")),
                self.step(lambda: self.fx.add_adp(1)),
                self.step(lambda: self.fx.add_adp(6, "V2b")),
                self.step(lambda: self.fx.add_fsu(2885)),
                self.step(lambda: self.fx.add_fsu(2886)),
        ]:
            stages_seen.append(stage)
        self.assertEqual(stages_seen,
                         ["initial_meshing", "initial_meshing",
                          "adaptive_meshing", "adaptive_meshing",
                          "frequency_sweep", "frequency_sweep"])
        status, stage, evidence = self.step()            # sweep quiet 1
        self.assertEqual(status, "running")
        self.assertEqual(stage, "finalizing")
        self.step(lambda: self.fx.write_profile(          # completion write
            "DV3019_S1911_V1.profile",
            [solution_group(FULL_STAGES, "Normal Completion",
                            "08/07/2026 00:48:26")]))
        self.step()
        status, stage, evidence = self.step()            # settle done
        self.assertEqual(status, "complete")
        self.assertEqual(stage, "done")
        self.assertIn("Normal Completion", evidence)
        self.assertNotIn("stalled", [l[0] for l in self.lines])
        self.assertNotIn("aborted", [l[0] for l in self.lines])

    def test_progress_lines_carry_stage_and_evidence(self):
        self.step(lambda: self.fx.add_mesh())
        self.step(lambda: self.fx.add_adp(3))
        for status, stage, evidence in self.lines:
            self.assertIn(stage, ("initial_meshing", "adaptive_meshing"))
            self.assertIsNone(evidence)

    def test_engine_error_profile_never_complete(self):
        for _ in range(4):
            self.step(lambda: self.fx.add_fsu(1, "E%d" % _))
        self.step(lambda: self.fx.write_profile(
            "DV3019_S1911_VErr.profile",
            [solution_group([], "Engine Detected Error", "08/07/2026 00:37:53")]))
        status, stage, evidence = self.step()
        self.assertEqual(status, "aborted")
        self.assertIn("Engine Detected Error", evidence)
        self.assertIn("never complete", evidence)
        self.assertTrue(all(st != "complete" for st, _, _ in self.lines))

    def test_error_then_rerun_profile_last_group_wins(self):
        self.step(lambda: self.fx.add_fsu(2885))
        self.step(lambda: self.fx.write_profile(
            "DV3019_S1911_V1.profile",
            [solution_group([], "Engine Detected Error", "08/07/2026 00:37:53"),
             solution_group(FULL_STAGES, "Normal Completion",
                            "08/07/2026 00:43:14")]))
        self.step()
        self.step()
        status, stage, evidence = self.step()
        self.assertEqual(status, "complete")
        self.assertIn("Normal Completion", evidence)

    def test_stuck_at_mesh_stalls_with_stage_in_evidence(self):
        self.step(lambda: self.fx.add_mesh())
        self.step(lambda: self.fx.add_mesh())          # growth then stall
        for _ in range(8):
            self.step()
        status, stage, evidence = self.lines[-1]
        self.assertEqual(status, "stalled")
        self.assertEqual(stage, "initial_meshing")
        self.assertIn("initial_meshing", evidence)

    def test_stuck_in_adaptive_stalls_with_stage_in_evidence(self):
        self.step(lambda: self.fx.add_mesh())
        self.step(lambda: self.fx.add_adp(2))
        for _ in range(8):
            self.step()
        status, stage, evidence = self.lines[-1]
        self.assertEqual(status, "stalled")
        self.assertEqual(stage, "adaptive_meshing")
        self.assertIn("adaptive_meshing", evidence)

    def test_engine_death_mid_sweep_aborts(self):
        self.step(lambda: (self.fx.add_semaphore(),
                           self.fx.add_mesh("D1")))
        self.step(lambda: self.fx.add_adp(4, "D2"))
        self.step(lambda: self.fx.add_fsu(2885, "D3"))
        self.step(lambda: self.fx.add_fsu(2886, "D3"))
        self.step(lambda: self.fx.add_sd("DV3019_SOL1_M1_V4.sd"))
        self.fx.alive[0] = False                       # engine dies
        for name in os.listdir(self.fx.root):
            if name.endswith(".semaphore"):
                os.remove(os.path.join(self.fx.root, name))
        status, stage, evidence = self.step()          # removal is itself a
        self.assertEqual(status, "running")            # tree change: 1st quiet
        status, stage, evidence = self.step()          # tick then confirms death
        self.assertEqual(status, "aborted")
        self.assertNotEqual(stage, "done")
        self.assertIn("solver process dead", evidence)
        self.assertIn("in-flight", evidence)
        self.assertIn("while in stage", evidence)
        self.assertNotEqual(status, "stalled")
        self.assertNotEqual(status, "complete")

    def test_dead_solver_before_any_output_aborts(self):
        self.fx.alive[0] = False
        for _ in range(7):
            self.step()
        status, stage, evidence = self.lines[-1]
        self.assertEqual(status, "aborted")
        self.assertIn("solver process dead", evidence)

    def test_alive_solver_with_no_output_stalls(self):
        for _ in range(7):
            self.step()
        status, stage, evidence = self.lines[-1]
        self.assertEqual(status, "stalled")
        self.assertEqual(stage, "initial_meshing")
        self.assertIn("submit never picked up", evidence)

    def test_stale_profile_from_previous_run_never_completes(self):
        self.fx.write_profile(
            "DV3019_S1911_VOld.profile",
            [solution_group(FULL_STAGES, "Normal Completion",
                            "08/07/2026 00:43:14")])
        for m in range(3):
            self.step(lambda: self.fx.add_fsu(2885 + m))  # new solve grows
        for _ in range(5):
            self.step()
        status, stage, evidence = self.lines[-1]
        # profile mtime == baseline (written before the watchdog started) =>
        # never fresh => never complete; the stall names the stage honestly
        self.assertEqual(status, "stalled")
        self.assertNotEqual(stage, "done")

    def test_families_match_pilot_artifact_names(self):
        """Entity type is part of the artifact, not an implementation detail.

        `.imesh`, `.cmesh` and `_ADP*` are DIRECTORIES on this box. The
        earlier version of this test wrote all of these names as files,
        which is why `mesh`/`adp` could read (0,0) against every real tree
        while the suite stayed green (ticket 02).
        """
        dirs = ["DV3019_S1911_ADP6_V2681.sd",
                "DV3019_S1911_V2578.cmesh",
                "DV3019_V2573.imesh"]
        files = ["DV3019_S1918_V2657_F3092_SU.txt",
                 "DV3019_SOL1912_M1_V2664.sd",
                 ".Bowtie3501.asol.semaphore",
                 "DV3019_S1911_SD1_V2667.su",
                 "DV3019_S1911_SD6_V2682.su"]
        for name in dirs:
            os.makedirs(os.path.join(self.fx.root, name))
        for name in files:
            self.fx.write(name)
        s = poll_solve.scan_results(self.fx.root)
        self.assertEqual(s["mesh"], (2, 0), "imesh/cmesh dirs must count")
        self.assertEqual(s["adp"], (1, 0), "_ADP dirs must count")
        self.assertEqual(s["fsu"], (1, 1))
        # the _ADP dir and the plain .sd file both belong to the sd family
        self.assertEqual(s["sd"], (2, 1))
        self.assertEqual(s["semaphores"], 1)

    def test_real_solved_trees_show_mesh_and_adaptive_evidence(self):
        """Against captured real trees, every stage family must be visible.

        This is the regression that the directory bug would fail: all three
        captured solves completed initial meshing and six adaptive passes,
        so a scan reporting zero for those families is wrong by inspection.
        """
        for case in real_fixtures.cases():
            dest = os.path.join(self.fx.tmp, "real-" + case)
            real_fixtures.materialize(case, dest)
            scan = poll_solve.scan_results(dest)
            self.assertGreater(scan["mesh"][0], 0, "%s: no mesh evidence" % case)
            self.assertGreater(scan["adp"][0], 0, "%s: no adaptive evidence" % case)
            self.assertGreater(scan["fsu"][0], 0, "%s: no sweep evidence" % case)
            total_files, _total_bytes = real_fixtures.expected_totals(case)
            self.assertEqual(scan["files"], total_files,
                             "%s: materialized tree must match the real one" % case)

    def test_stage_floor_reaches_adaptive_without_a_profile(self):
        """Mid-solve there is no profile at all — the profile is written at
        the END of a solve. Adaptive evidence must therefore come from
        artifacts alone, or the watchdog cannot tell meshing from adapting.
        """
        self.fx.add_mesh()
        self.fx.add_adp(1)
        scan = dict(poll_solve.scan_results(self.fx.root), profile_stages=[])
        self.assertEqual(poll_solve.stage_token(poll_solve.stage_floor(scan)),
                         "adaptive_meshing")


class TestParseProfile(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.path = os.path.join(self.tmp, "x.profile")

    def _parse(self, text=None):
        if text is None:
            text = profile_text([solution_group(
                FULL_STAGES, "Normal Completion", "08/07/2026 00:48:26")])
        with open(self.path, "w") as f:
            f.write(text)
        return poll_solve.parse_profile(self.path)

    def test_stage_ledger_and_terminal_status(self):
        stages, status, stop = self._parse()
        self.assertEqual([s for s, _, _ in stages],
                         ["Initial Meshing", "Adaptive Meshing", "Frequency Sweep"])
        self.assertEqual(stages[0][1], "00:00:02")
        self.assertEqual(stages[1][2], 6)          # adaptive passes counted
        self.assertEqual(stages[2][1], "00:03:58")
        self.assertEqual(status, "Normal Completion")
        self.assertEqual(stop, "08/07/2026 00:48:26")

    def test_engine_error_at_validation(self):
        stages, status, stop = self._parse(profile_text(
            [solution_group([], "Engine Detected Error", "08/07/2026 00:37:53")]))
        self.assertEqual(stages, [])
        self.assertEqual(status, "Engine Detected Error")

    def test_last_solution_group_wins(self):
        _, status, stop = self._parse(profile_text(
            [solution_group([], "Engine Detected Error", "08/07/2026 00:37:53"),
             solution_group(FULL_STAGES, "Normal Completion",
                            "08/07/2026 00:43:14")]))
        self.assertEqual(status, "Normal Completion")
        self.assertEqual(stop, "08/07/2026 00:43:14")

    def test_missing_file(self):
        self.assertEqual(poll_solve.parse_profile(os.path.join(
            self.tmp, "nope.profile")), ([], None, None))

    def test_ledger_token_shape(self):
        stages, _, _ = self._parse()
        token = poll_solve.format_stage_ledger(stages)
        self.assertEqual(
            token,
            "Initial_Meshing:00:00:02,Adaptive_Meshing:00:00:17:6p,"
            "Frequency_Sweep:00:03:58")
        self.assertNotIn(" ", token)

    def test_pilot_profile_is_ground_truth(self):
        # walk up to the repo root (workspaces/bowtie-3500-pilot lives there)
        # whether the module runs from the pilot WS or the template copy
        here = os.path.abspath(os.path.dirname(__file__))
        frontier = here
        while os.path.dirname(frontier) != frontier:
            probe = os.path.join(frontier, "workspaces", "bowtie-3500-pilot")
            if os.path.isdir(probe):
                break
            frontier = os.path.dirname(frontier)
        pilot = os.path.join(frontier, "workspaces", "bowtie-3500-pilot",
                             "bowtie_3500_pilot.aedtresults",
                             "Bowtie3501.results", "DV3019_S1911_V2586.profile")
        if not os.path.isfile(pilot):
            self.skipTest("pilot artifacts not present")
        stages, status, stop = poll_solve.parse_profile(pilot)
        self.assertEqual([s for s, _, _ in stages],
                         ["Initial Meshing", "Adaptive Meshing", "Frequency Sweep"])
        self.assertEqual(stages[1][2], 6)
        self.assertEqual(status, "Normal Completion")
        self.assertIn("00:48:26", stop or "")

    def test_terminal_lines_format_with_evidence_tail(self):
        cur = dict(poll_solve.observe(os.path.join(self.tmp, "nope"), self.tmp,
                                      lambda pid: True))
        cur = dict(cur)
        cur["profile_status"] = "Normal Completion"
        line = poll_solve.format_progress(
            9, "complete", "done", cur,
            "profile status: Normal Completion (stop 08/07/2026 00:48:26)",
            3, 183, 1000)
        self.assertTrue(line.endswith(
            "evidence=profile status: Normal Completion (stop 08/07/2026 00:48:26)"))
        self.assertNotIn("expected_sd", line)
        self.assertIn("stage=done", line)
        self.assertIn("unchanged_ticks=3", line)


if __name__ == "__main__":
    unittest.main()
