"""Tests for the template runner scripts at the no-AEDT seams.

Covers poll_solve (scan + state machine + progress line), capture_state
(shape extraction + normalization), 12_verify_sync (diff, replay
selection, copy hygiene), 00_static_gate (compile/import gate on
throwaway trees), confirm_solve (terminal profile parse + sweep count +
in-flight test + banking), and the guarded teardown decision
(banked / unbanked-with-evidence / neither) on fixture state, and the
stale-pin attach route (bounded connect: a dead pinned desktop fails fast
as `stale pin — re-pinning`, never a hanging attach — the timeout path is
simulated at the socket seam with the AEDT entry points stood in by
fakes). No AEDT, no license, no desktop: every module under test imports
nothing beyond the standard library, except ws_common which imports pyAEDT
classes but never launches or attaches (the static gate's own
import-check doctrine).

Run:  python -m unittest src.test_template_runners -v
   or: python src/test_template_runners.py
"""

import contextlib
import importlib.util
import io
import json
import os
import shutil
import socket
import sys
import tempfile
import time
import unittest
from unittest import mock

SRC = os.path.dirname(os.path.abspath(__file__))
if SRC not in sys.path:
    # The runners import `profile_evidence` (the single profile parser,
    # ticket 01) by name, so the source dir must be importable however the
    # suite was invoked.
    sys.path.insert(0, SRC)

import real_fixtures  # noqa: E402  (needs SRC on the path)


def load(name):
    spec = importlib.util.spec_from_file_location("tp_" + name, os.path.join(SRC, name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def obs(**kw):
    """A bare observation dict for pure watchdog_tick tests."""
    base = {"mesh": (0, 0), "adp": (0, 0), "fsu": (0, 0), "sd": (0, 0),
            "semaphores": 0, "files": 0, "bytes_total": 0,
            "profile_mtime": None, "profile_stages": [], "profile_status": None,
            "profile_stop": None, "solver_alive": True}
    base.update(kw)
    return base


class TestPollSolveScan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pollsolve = load("poll_solve")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _results(self):
        root = os.path.join(self.tmp, "probe.aedtresults")
        os.makedirs(os.path.join(root, "F1.sd"), exist_ok=True)
        names = {
            "DV3019_V1.imesh": "m" * 3,
            "DV3019_S1_V2.cmesh": "m" * 4,
            "DV3019_S1_ADP6_V3.sd": "a",
            "DV3019_S1_V4_F2885_SU.txt": "s" * 6,
            "DV3019_SOL1_M1_V5.sd": "d" * 7,
            ".DV3019.asol.semaphore": "",
            "top.bin": "y" * 5,
        }
        for name, body in names.items():
            with open(os.path.join(root, name), "w") as f:
                f.write(body)
        return root

    def test_scan_counts_each_stage_family(self):
        s = self.pollsolve.scan_results(self._results())
        self.assertEqual(s["mesh"], (2, 7))      # imesh + cmesh (bytes 3+4)
        self.assertEqual(s["adp"], (1, 1))       # _ADP6_ entry
        self.assertEqual(s["fsu"], (1, 6))       # F2885_SU.txt
        self.assertEqual(s["sd"], (3, 8))        # dir F1.sd + ADP/SOL sd files
        self.assertEqual(s["semaphores"], 1)
        self.assertEqual((s["files"], s["bytes_total"]), (7, 26))

    def test_scan_missing_dir_is_zero(self):
        s = self.pollsolve.scan_results(
            os.path.join(self.tmp, "nope.aedtresults"))
        self.assertEqual((s["mesh"], s["adp"], s["fsu"]), ((0, 0), (0, 0), (0, 0)))
        self.assertEqual((s["files"], s["bytes_total"]), (0, 0))

    def test_project_results_dir(self):
        self.assertEqual(self.pollsolve.project_results_dir(r"C:\x\m.aedt"),
                         r"C:\x\m.aedtresults")


class TestPollSolveStateMachine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pollsolve = load("poll_solve")

    def _tick(self, cfg, cur, prev=None, state=None):
        state = state if state is not None else {"grown": False, "unchanged": 0,
                                                 "sem_ever": False}
        return self.pollsolve.watchdog_tick(prev, cur, state, cfg)

    def test_never_grew_stalls_after_start_ticks(self):
        zm = obs()
        cfg = {"start_ticks": 3, "stall_ticks": 9, "settle_ticks": 9}
        state = {"grown": False, "unchanged": 0, "sem_ever": False}
        prev = None
        seen = []
        for _ in range(4):
            status, stage, evidence, state = self._tick(cfg, zm, prev, state)
            seen.append(status)
            prev = zm
        self.assertEqual(seen[:3], ["running", "running", "running"])
        self.assertEqual(seen[3], "stalled")
        self.assertEqual(stage, "initial_meshing")

    def test_complete_after_growth_and_fresh_normal_profile(self):
        cfg = {"settle_ticks": 2}
        mtime = time.time()
        grew = obs(mesh=(1, 5), profile_stages=[
            ("Initial Meshing", "00:00:01", 0),
            ("Adaptive Meshing", "00:00:15", 6)])
        done = obs(mesh=(1, 5), profile_mtime=mtime,
                   profile_status="Normal Completion",
                   profile_stop="08/07/2026 00:48:26", profile_stages=[
                       ("Initial Meshing", "00:00:01", 0),
                       ("Adaptive Meshing", "00:00:15", 6),
                       ("Frequency Sweep", "00:03:58", 0)])
        state = {"grown": False, "unchanged": 0, "sem_ever": False}
        status, stage, ev, state = self._tick(cfg, grew, None, state)
        self.assertEqual((status, stage), ("running", "adaptive_meshing"))
        prev = grew
        s2, stage2, ev2, state = self._tick(cfg, done, prev, state)
        self.assertEqual((s2, stage2), ("running", "frequency_sweep"))
        s3, _, ev3, state = self._tick(cfg, done, done, state)
        s4, stage4, ev4, state = self._tick(cfg, done, done, state)
        self.assertEqual((s4, stage4), ("complete", "done"))
        self.assertIn("Normal Completion", ev4)

    def test_engine_error_profile_is_aborted_never_complete(self):
        cfg = {"settle_ticks": 2, "stall_ticks": 9, "start_ticks": 9}
        grew = obs(fsu=(1, 5))
        err = obs(fsu=(1, 5), profile_mtime=time.time(),
                  profile_status="Engine Detected Error",
                  profile_stop="08/07/2026 00:37:53")
        status, stage, ev, state = self._tick(cfg, grew, None,
                                              {"grown": False, "unchanged": 0,
                                               "sem_ever": False})
        self.assertEqual((status, stage), ("running", "frequency_sweep"))
        status, stage, ev, state = self._tick(cfg, err, grew, state)
        self.assertEqual((status, stage), ("aborted", "done"))
        self.assertIn("Engine Detected Error", ev)
        for _ in range(12):
            status, _, _, state = self._tick(cfg, err, err, state)
        # the engine-error profile must never flip to complete later
        self.assertEqual(status, "aborted")

    def test_stale_normal_profile_is_not_complete(self):
        cfg = {"settle_ticks": 2, "stall_ticks": 4, "start_ticks": 9}
        mtime = time.time()
        stale = obs(fsu=(1, 5), profile_mtime=mtime,
                    profile_status="Normal Completion")
        state = {"grown": False, "unchanged": 0, "sem_ever": False}
        prev = None
        status = stage = None
        for _ in range(6):
            status, stage, _, state = self._tick(cfg, stale, prev, state)
            prev = stale
        # same mtime from tick 0 => not written this session => stall, not done
        self.assertEqual(status, "stalled")
        self.assertNotEqual(stage, "done")
        self.assertNotIn("complete", status)

    def test_stuck_at_mesh_stalls_with_stage_in_evidence(self):
        cfg = {"settle_ticks": 9, "stall_ticks": 3}
        mesh = obs(mesh=(2, 9))
        state = {"grown": False, "unchanged": 0, "sem_ever": False}
        prev = None
        last_ev = None
        for _ in range(5):
            status, stage, ev, state = self._tick(cfg, mesh, prev, state)
            prev = mesh
            last_ev = ev
        self.assertEqual(status, "stalled")
        self.assertEqual(stage, "initial_meshing")
        self.assertIn("initial_meshing", last_ev)

    def test_engine_death_mid_solve_aborts(self):
        cfg = {"settle_ticks": 9, "stall_ticks": 9, "dead_ticks": 1}
        live = obs(fsu=(1, 5), semaphores=1, solver_alive=True)
        dead = obs(fsu=(1, 5), semaphores=0, solver_alive=False)
        state = {"grown": False, "unchanged": 0, "sem_ever": False}
        status, stage, ev, state = self._tick(cfg, live, None, state)
        self.assertEqual(status, "running")
        status, stage, ev, state = self._tick(cfg, dead, live, state)
        self.assertEqual((status, stage), ("aborted", "finalizing"))
        self.assertIn("solver process dead", ev)

    def test_never_grew_with_dead_solver_aborts(self):
        cfg = {"start_ticks": 2}
        zm = obs(solver_alive=False)
        state = {"grown": False, "unchanged": 0, "sem_ever": False}
        prev = None
        status = None
        for _ in range(3):
            status, _, _, state = self._tick(cfg, zm, prev, state)
            prev = zm
        self.assertEqual(status, "aborted")

    def test_progress_line_has_stage_and_no_expected_sd(self):
        cur = obs(mesh=(2, 7), adp=(1, 1), fsu=(1, 6), sd=(2, 8), files=7,
                  bytes_total=26, semaphores=1, profile_status="Normal Completion")
        line = self.pollsolve.format_progress(
            3, "complete", "done", cur,
            "profile status: Normal Completion (stop 08/07/2026 00:48:26)",
            1, 61, 1000)
        for token in ("tick=3", "status=complete", "stage=done", "elapsed_s=61",
                      "mesh=2", "adp=1", "fsu=1", "sd=2", "files=7",
                      "semaphores=1", "profile_status=normal_completion",
                      "evidence=profile status: Normal Completion"):
            self.assertIn(token, line)
        self.assertNotIn("expected_sd", line)

    def test_resolve_project_from_argv(self):
        self.assertEqual(
            self.pollsolve.resolve_project(["poll_solve.py", r"C:\w\m.aedt"]),
            r"C:\w\m.aedt")

    def test_resolve_project_none_when_ambiguous(self):
        # the real parent of poll_solve.py holds many non-.aedt files and no
        # exactly-one .aedt, so the argv-less fallback must return None here.
        self.assertIsNone(self.pollsolve.resolve_project(["poll_solve.py"]))


class TestCaptureState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.capture = load("capture_state")

    def test_rounded_normalizes_floats(self):
        r = self.capture._rounded
        self.assertEqual(r(0.10000000000000001), 0.1)
        self.assertEqual(r([1.5, "x", None]), [1.5, "x", None])
        self.assertEqual(r((1, 2.0)), [1, 2.0])
        self.assertEqual(r({"a": 1.2300000001}), {"a": 1.23})
        self.assertEqual(r(7), 7)

    def test_shape_from_fake_model(self):
        events = {}

        class FakeObj:
            def __init__(self, name, material="pec"):
                self.name = name
                self.material_name = material
                self.bounding_box = [0.5, 0.0, 0.0, 2.0, 1.0, 1.0000000009]

        class FakeSetup:
            def __init__(self, name, props):
                self.name = name
                self._props = props

            def get_properties(self):
                return self._props

        class FakeModeler:
            object_names = ["Sub", "Patch"]

            def get_object_bounding_box(self, name):
                return {"Sub": [0.0, 0.0, 0.0, 80.0, 90.0, 1.6],
                        "Patch": None}[name]

            def __getitem__(self, name):
                if name == "Patch":
                    return FakeObj("Patch", "pec")
                return FakeObj("Sub", "FR4_epoxy")

        class FakeModel:
            modeler = FakeModeler()
            boundaries = [type("B", (), {"name": "Rad1", "type": "Radiation"})()]
            excitations = [type("E", (), {"name": "P1WavePort", "type": "WavePort"})()]
            setups = [FakeSetup("Setup1", {"Frequency": 2.45, "MaxPasses": 9})]
            existing_analysis_sweeps = ["Setup1 : LastAdaptive", "Setup1 : SweepX : Table"]
            variables = {"w": "2mm", "PatchW": "100mm"}

        shape = self.capture.shape_from_model(FakeModel())
        self.assertEqual(shape["objects"], ["Patch", "Sub"])
        self.assertEqual(shape["bboxes"]["Sub"], [0.0, 0.0, 0.0, 80.0, 90.0, 1.6])
        # get_object_bounding_box returned None; the per-object fallback won
        self.assertEqual(shape["bboxes"]["Patch"], [0.5, 0.0, 0.0, 2.0, 1.0, 1.000000001])
        self.assertEqual(shape["materials"], {"Patch": "pec", "Sub": "FR4_epoxy"})
        self.assertEqual(shape["boundaries"], {"Rad1": "Radiation"})
        self.assertEqual(shape["excitations"], {"P1WavePort": "WavePort"})
        self.assertEqual(shape["setups"]["Setup1"]["Frequency"], 2.45)
        self.assertEqual(shape["sweeps"], ["Setup1 : LastAdaptive", "Setup1 : SweepX : Table"])
        self.assertEqual(list(shape["variables"]), ["PatchW", "w"])
        json.dumps(shape, sort_keys=True)  # must be JSON-native

    def test_shape_section_keys_stable(self):
        self.assertEqual(
            list(load("capture_state").shape_from_model(
                type("M", (), {"modeler": type("Mdl", (), {"object_names": ["A"]})(),
                               "boundaries": [], "excitations": [],
                               "setups": [], "existing_analysis_sweeps": [],
                               "variables": {}})()).keys()),
            ["snapshot_version", "model_units", "objects", "object_kinds",
             "bboxes", "materials", "boundaries", "excitations", "ports",
             "terminals", "setups", "sweeps", "variables"])

    def test_object_kinds_split_by_modeler_lists(self):
        """solid/sheet/line, the one thing a bbox cannot tell the reducer.

        Added for ticket 12a: without it every reduced object falls back to
        `op: unknown`, because a bounding box is a consequence of a
        construction op rather than a restatement of it.
        """
        modeler = type("Mdl", (), {"object_names": ["Sub", "Patch", "Path"],
                                   "solid_names": ["Sub"],
                                   "sheet_names": ["Patch"],
                                   "line_names": ["Path"]})()
        shape = load("capture_state").shape_from_model(
            type("M", (), {"modeler": modeler, "boundaries": [], "excitations": [],
                           "setups": [], "existing_analysis_sweeps": [],
                           "variables": {}})())
        self.assertEqual(shape["object_kinds"],
                         {"Patch": "sheet", "Path": "line", "Sub": "solid"})
        self.assertEqual(shape["snapshot_version"], 3)

    def test_setup_properties_are_actually_captured(self):
        """pyAEDT 1.3.0's Setup has `props`, NOT `get_properties()`.

        The original probe was `hasattr(setup, "get_properties")`, which is
        always False on this version, so every snapshot recorded `{}` for
        every setup — on both sides of any comparison, making a changed
        max-pass indistinguishable from an unchanged one.
        """
        setup = type("S", (), {"name": "Setup1",
                               "props": {"Frequency": "10GHz",
                                         "MaximumPasses": 6,
                                         "MaxDeltaS": 0.02}})()
        shape = load("capture_state").shape_from_model(
            type("M", (), {"modeler": type("Mdl", (), {"object_names": [],
                                                       "model_units": "cm"})(),
                           "boundaries": [], "excitations": [],
                           "setups": [setup], "existing_analysis_sweeps": [],
                           "variables": {}})())
        self.assertEqual(shape["setups"]["Setup1"]["MaximumPasses"], 6)
        self.assertEqual(shape["setups"]["Setup1"]["Frequency"], "10GHz")
        self.assertEqual(shape["model_units"], "cm")

    def test_ports_are_derived_from_boundaries(self):
        """Ports appear in `boundaries`; `excitations` came back empty on
        every real model captured (Modal and Terminal, wave and lumped)."""
        entity = lambda n, t: type("B", (), {"name": n, "type": t})()
        shape = load("capture_state").shape_from_model(
            type("M", (), {"modeler": type("Mdl", (), {"object_names": []})(),
                           "boundaries": [entity("1", "Wave Port"),
                                          entity("AutoOpen1", "Radiation"),
                                          entity("antennaMetal", "Perfect E")],
                           "excitations": [], "setups": [],
                           "existing_analysis_sweeps": [], "variables": {}})())
        self.assertEqual(shape["ports"], {"1": "Wave Port"})
        self.assertEqual(shape["excitations"], {})
        self.assertIn("antennaMetal", shape["boundaries"])

    def test_terminals_are_not_counted_as_ports(self):
        """A 2-port coplanar waveguide lists SIX port-typed boundaries.

        Terminal-solution designs add one `<name>_T<n>` terminal per
        conductor per port, and they carry the same `Wave Port` type, so
        counting everything port-typed reports six ports for a two-port
        line. Real shapes, from the captured coplanar model.
        """
        entity = lambda n, t: type("B", (), {"name": n, "type": t})()
        names = ["1", "1_T1", "1_T2", "2", "2_T1", "2_T2"]
        shape = load("capture_state").shape_from_model(
            type("M", (), {"modeler": type("Mdl", (), {"object_names": []})(),
                           "boundaries": [entity(n, "Wave Port") for n in names]
                                         + [entity("Rad1", "Radiation")],
                           "excitations": [], "setups": [],
                           "existing_analysis_sweeps": [], "variables": {}})())
        self.assertEqual(sorted(shape["ports"]), ["1", "2"])
        self.assertEqual(sorted(shape["terminals"]),
                         ["1_T1", "1_T2", "2_T1", "2_T2"])


class TestVerifySync(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.verify = load("12_verify_sync")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_diff_equal_close(self):
        snap = {"objects": ["A"], "bboxes": {"A": [0, 0, 0, 1, 1, 1]},
                "variables": {"w": "2mm"}}
        self.assertEqual(self.verify.diff_shapes(snap, json.loads(json.dumps(snap))), [])

    def test_diff_catches_nested_leaf(self):
        live = {"objects": ["A"], "bboxes": {"A": [0, 0, 0, 1, 1, 1]},
                "variables": {"w": "2mm"}}
        replay = {"objects": ["A"], "bboxes": {"A": [0, 0, 0, 1, 1, 2]},
                  "variables": {"w": "2mm"}}
        diffs = self.verify.diff_shapes(live, replay)
        self.assertEqual(len(diffs), 1)
        self.assertIn("bboxes.A", diffs[0])

    def test_diff_missing_sections(self):
        diffs = self.verify.diff_shapes({"objects": ["A"]}, {"objects": ["A"], "sweeps": []})
        self.assertEqual(len(diffs), 1)
        self.assertIn("sweeps: only in replay", diffs[0])

    def test_diff_canon_matches_same_random_suffixes(self):
        live = {"boundaries": {"1": "Wave Port", "Rad__AAAA00": "Radiation"}}
        replay = {"boundaries": {"1": "Wave Port", "Rad__BBBB11": "Radiation"}}
        self.assertEqual(self.verify.diff_shapes(live, replay), [])

    def test_diff_canon_preserves_random_suffix_counts(self):
        # a second same-class entry in replay must NOT vanish via key collapse
        live = {"boundaries": {"Rad__AAAA00": "Radiation"}}
        replay = {"boundaries": {"Rad__AAAA00": "Radiation", "Rad__BBBB11": "Radiation"}}
        diffs = self.verify.diff_shapes(live, replay)
        self.assertEqual(len(diffs), 1)
        self.assertIn("only in replay", diffs[0])

    def test_replay_selection_defaults(self):
        src = os.path.join(self.tmp, "src")
        os.makedirs(src)
        names = ["01_solution_type_and_design.py", "02_geometry.py", "03_materials.py",
                 "04_excitations.py", "05_mesh.py", "06_setup_sweep.py", "07_validate.py",
                 "08_solve.py", "09_plots.py", "10_qa.py", "12_verify_sync.py",
                 "00_static_gate.py", "ws_common.py", "poll_solve.py", "stage_skeleton.py"]
        for n in names:
            with open(os.path.join(src, n), "w") as f:
                f.write("# x\n")
        picked = [os.path.basename(p) for p in self.verify.select_replay_scripts(src)]
        self.assertEqual(picked, ["01_solution_type_and_design.py", "02_geometry.py",
                                  "03_materials.py", "04_excitations.py", "05_mesh.py",
                                  "06_setup_sweep.py", "07_validate.py"])

    def test_replay_selection_explicit(self):
        picked = self.verify.select_replay_scripts("src", ["02_geometry.py"])
        self.assertEqual(picked, [os.path.join("src", "02_geometry.py")])

    def test_replay_paths_map_into_copy(self):
        ws = os.path.join(self.tmp, "ws")
        os.makedirs(os.path.join(ws, "src"))
        for name in ("01_build.py", "04_excitations.py", "08_solve.py", "ws_common.py"):
            with open(os.path.join(ws, "src", name), "w") as f:
                f.write("# x\n")
        copied = self.verify.make_copy(ws)
        scripts = self.verify.select_replay_scripts(os.path.join(ws, "src"))
        replays = [os.path.join(copied, "src", os.path.basename(s)) for s in scripts]
        self.assertEqual([os.path.basename(p) for p in replays],
                         ["01_build.py", "04_excitations.py"])
        for path in replays:
            self.assertTrue(os.path.isfile(path))
            self.assertTrue(os.path.commonpath([copied, path]) == os.path.normpath(copied))

    def test_make_copy_is_hygienic(self):
        ws = os.path.join(self.tmp, "ws")
        os.makedirs(os.path.join(ws, "src"))
        os.makedirs(os.path.join(ws, "results", "state"))
        os.makedirs(os.path.join(ws, "results", "plots"))
        for name in ("01_a.py", "ws_common.py", "00_static_gate.py"):
            with open(os.path.join(ws, "src", name), "w") as f:
                f.write("pass\n")
        for name in ("m.aedt", "m.aedt.lock", "summary.md", "state.md", "README.md"):
            with open(os.path.join(ws, name), "w") as f:
                f.write("x")
        os.makedirs(os.path.join(ws, "m.aedtresults"))
        with open(os.path.join(ws, "results", "state", "aedt_port.txt"), "w") as f:
            f.write("12345")

        copy = self.verify.make_copy(ws)
        copied = os.listdir(copy)
        copied_src = os.listdir(os.path.join(copy, "src"))
        self.assertIn("01_a.py", copied_src)
        self.assertIn("ws_common.py", copied_src)
        self.assertIn("summary.md", copied)
        self.assertIn("state.md", copied)
        for banned in ("m.aedt", "m.aedt.lock", "m.aedtresults", "results"):
            self.assertNotIn(banned, copied)
        self.assertTrue(os.path.isdir(os.path.join(copy, "src")))


class TestStaticGate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gate = load("00_static_gate")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, name, body):
        with open(os.path.join(self.tmp, name), "w") as f:
            f.write(body)

    def test_gate_clean_tree(self):
        self._write("00_static_gate.py", "import os\n")
        self._write("ok_mod.py", "x = 1\n")
        ok, lines, compiled, imported = self.gate.run_gate(self.tmp)
        self.assertTrue(ok)
        self.assertEqual(compiled, 2)
        self.assertEqual(imported, 1)

    def test_gate_catches_syntax_error(self):
        self._write("bad.py", "def (:\n")
        ok, lines, _, _ = self.gate.run_gate(self.tmp)
        self.assertFalse(ok)
        self.assertTrue(any("compile FAIL" in l for l in lines))

    def test_gate_catches_import_error(self):
        self._write("needs.py", "import definitely_not_a_module_xyz\n")
        ok, lines, _, imported = self.gate.run_gate(self.tmp)
        self.assertFalse(ok)
        self.assertEqual(imported, 0)
        self.assertTrue(any("import FAIL" in l for l in lines))


class TestConfirmSolve(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.confirm = load("confirm_solve")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _profile_text(self, status=None, stop="08/07/2026 00:43:14", groups=1):
        """A profile in the shape AEDT actually writes.

        Structurally faithful on the two points that matter and that the
        previous hand-written fixture got wrong: the stage groups live
        inside a named `Solution Process` group, and the terminal footnote
        escapes its quotes. `test_synthetic_profile_matches_real_shape`
        pins this against a captured artifact.
        """
        text = "$begin 'Profile'\n"
        for index in range(groups):
            text += ("\t$begin 'ProfileGroup'\n"
                     "\t\tName='Solution Process'\n"
                     "\t\t$begin 'ProfileGroup'\n"
                     "\t\t\tName='Frequency Sweep'\n"
                     "\t\t\t$begin 'TotalInfo'\n"
                     "\t\t\t\tI(1, 'Elapsed Time', '00:01:00')\n"
                     "\t\t\t$end 'TotalInfo'\n"
                     "\t\t$end 'ProfileGroup'\n")
            if status is not None:
                value = status[index] if isinstance(status, (list, tuple)) else status
                text += ("\t\tProfileFootnote('I(2, 1, \\'Stop Time\\', \\'%s\\', 1, "
                         "\\'Status\\', \\'%s\\')', 0)\n" % (stop, value))
            text += "\t$end 'ProfileGroup'\n"
        return text + "$end 'Profile'\n"

    def _results_dir(self, name="probe"):
        project = os.path.join(self.tmp, name + ".aedt")
        root = project + "results"
        results_dir = os.path.join(root, name + ".results")
        os.makedirs(results_dir)
        return project, root, results_dir

    def _profile(self, results_dir, stem, mtime, status="Normal Completion"):
        path = os.path.join(results_dir, stem + ".profile")
        with open(path, "w") as f:
            f.write(self._profile_text(status))
        os.utime(path, (mtime, mtime))
        return path

    def test_terminal_status_parsed(self):
        _, _, d = self._results_dir()
        p = self._profile(d, "DV3019_S1_V1", 1000)
        self.assertEqual(self.confirm.terminal_status(p), "Normal Completion")

    def test_terminal_status_none_without_footnote(self):
        _, _, d = self._results_dir()
        p = self._profile(d, "DV3019_S1_V1", 1000, status=None)
        self.assertIsNone(self.confirm.terminal_status(p))
        self.assertIsNone(self.confirm.terminal_status(os.path.join(self.tmp, "missing.profile")))

    def test_terminal_status_last_solution_group_wins(self):
        """An error session followed by a re-run: the LAST group is terminal."""
        _, _, d = self._results_dir()
        path = os.path.join(d, "DV3019_S1_V1.profile")
        with open(path, "w") as handle:
            handle.write(self._profile_text(
                status=["Engine Detected Error", "Normal Completion"], groups=2))
        self.assertEqual(self.confirm.terminal_status(path), "Normal Completion")

    def test_terminal_status_escaped_quotes_is_the_real_form(self):
        """The bug of 2026-08-14: the bare form is not what AEDT writes.

        A parser that only accepts `'Status', 'X'` reports None for every
        real solve, which silently turned the teardown guard off.
        """
        _, _, d = self._results_dir()
        path = os.path.join(d, "DV1_S1_V1.profile")
        with open(path, "w") as handle:
            handle.write(
                "$begin 'Profile'\n\t$begin 'ProfileGroup'\n"
                "\t\tName='Solution Process'\n"
                "\t\tProfileFootnote('I(2, 1, \\'Stop Time\\', \\'08/07/2026 00:43:14\\', "
                "1, \\'Status\\', \\'Normal Completion\\')', 0)\n"
                "\t$end 'ProfileGroup'\n$end 'Profile'\n")
        self.assertEqual(self.confirm.terminal_status(path), "Normal Completion")

    def test_synthetic_profile_matches_real_shape(self):
        """The synthetic builder is only valid while it agrees with a real artifact."""
        case = "pilot-normal"
        name = "DV3019_S1911_V2586.profile"
        real = real_fixtures.profile_path(case, name)
        expected = real_fixtures.meta(case)["profiles"][name]
        self.assertEqual(self.confirm.terminal_status(real), expected["status"])

        _, _, d = self._results_dir("synthetic")
        synthetic = os.path.join(d, "DV1_S1_V1.profile")
        with open(synthetic, "w") as handle:
            handle.write(self._profile_text(status=expected["status"],
                                            stop=expected["stop"]))
        self.assertEqual(self.confirm.terminal_status(synthetic), expected["status"])

    def test_newest_terminal_profile_skips_unfinished_newer(self):
        _, root, d = self._results_dir()
        old_ok = self._profile(d, "DV3019_S1_V1", 1000)
        self._profile(d, "DV3019_S1_V2", 2000, status=None)
        self.assertEqual(self.confirm.newest_terminal_profile(root), old_ok)

    def test_sweep_count_attributed_by_dv_prefix(self):
        _, _, d = self._results_dir()
        p = self._profile(d, "DV3019_S1_V1", 2000)
        for i in range(5):
            with open(os.path.join(d, "DV3019_S1_V9_F%04d_SU.txt" % i), "w") as f:
                f.write("x")
        for i in range(3):
            with open(os.path.join(d, "DV2569_S1_V9_F%04d_SU.txt" % i), "w") as f:
                f.write("x")
        self.assertEqual(self.confirm.sweep_point_count(p), 5)

    def test_sweep_count_falls_back_to_all_without_dv_prefix(self):
        _, _, d = self._results_dir()
        p = self._profile(d, "TOPNON_DV1", 2000)
        for i in range(2):
            with open(os.path.join(d, "DV3019_S1_V9_F%04d_SU.txt" % i), "w") as f:
                f.write("x")
        self.assertEqual(self.confirm.sweep_point_count(p), 2)

    def test_in_flight_semaphore_newer_than_profile(self):
        _, root, d = self._results_dir()
        p = self._profile(d, "DV3019_S1_V1", 2000)
        sem = os.path.join(root, ".probe.asol.semaphore")
        with open(sem, "w") as f:
            f.write("")
        os.utime(sem, (3000, 3000))
        self.assertEqual(len(self.confirm.in_flight_semaphores(root, p)), 1)

    def test_stale_semaphore_from_completed_solve_ignored(self):
        _, root, d = self._results_dir()
        p = self._profile(d, "DV3019_S1_V1", 2000)
        sem = os.path.join(root, ".probe.asol.semaphore")
        with open(sem, "w") as f:
            f.write("")
        os.utime(sem, (1500, 1500))
        self.assertEqual(self.confirm.in_flight_semaphores(root, p), [])

    def test_confirm_banks_terminal_profile(self):
        project, _, d = self._results_dir()
        self._profile(d, "DV3019_S1_V1", 2000)
        for i in range(4):
            with open(os.path.join(d, "DV3019_S1_V9_F%04d_SU.txt" % i), "w") as f:
                f.write("x")
        st = os.path.join(self.tmp, "results", "state")
        rc, lines = self.confirm.confirm(project, state_dir=st, now=1234567890)
        self.assertEqual(rc, 0)
        self.assertTrue(any(l.startswith("PASS: confirm_solve banked") for l in lines))
        with open(os.path.join(st, "solved.txt")) as f:
            content = f.read()
        self.assertIn("status=Normal Completion", content)
        self.assertIn("sweep_points=4", content)
        self.assertIn("banked_at=1234567890", content)

    def test_confirm_banks_non_normal_status_with_warning(self):
        project, _, d = self._results_dir()
        self._profile(d, "DV3019_S1_V1", 2000, status="Engine Detected Error")
        st = os.path.join(self.tmp, "results", "state")
        rc, lines = self.confirm.confirm(project, state_dir=st, now=1234567890)
        self.assertEqual(rc, 0)
        with open(os.path.join(st, "solved.txt")) as f:
            self.assertIn("status=Engine Detected Error", f.read())
        self.assertTrue(any("NOT 'Normal Completion'" in l for l in lines))

    def test_confirm_refuses_without_terminal_profile(self):
        project, _, d = self._results_dir()
        self._profile(d, "DV3019_S1_V1", 2000, status=None)
        st = os.path.join(self.tmp, "results", "state")
        rc, lines = self.confirm.confirm(project, state_dir=st, now=1234567890)
        self.assertEqual(rc, 2)
        self.assertFalse(os.path.isfile(os.path.join(st, "solved.txt")))
        self.assertTrue(any("aborted" in l for l in lines))

    def test_confirm_refuses_in_flight_solve(self):
        project, root, d = self._results_dir()
        self._profile(d, "DV3019_S1_V1", 2000)
        sem = os.path.join(root, ".probe.asol.semaphore")
        with open(sem, "w") as f:
            f.write("")
        os.utime(sem, (3000, 3000))
        st = os.path.join(self.tmp, "results", "state")
        rc, lines = self.confirm.confirm(project, state_dir=st, now=1234567890)
        self.assertEqual(rc, 2)
        self.assertFalse(os.path.isfile(os.path.join(st, "solved.txt")))
        self.assertTrue(any("in-flight" in l for l in lines))


class TestGuardedTeardown(unittest.TestCase):
    """The teardown guard's three-way decision on fixture state."""

    @classmethod
    def setUpClass(cls):
        cls.common = load("ws_common")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _state_dir(self):
        st = os.path.join(self.tmp, "results", "state")
        os.makedirs(st)
        return st

    def _project_and_results(self):
        project = os.path.join(self.tmp, "probe.aedt")
        d = os.path.join(project + "results", "probe.results")
        os.makedirs(d)
        return project, d

    def _banked(self, st):
        with open(os.path.join(st, "solved.txt"), "w") as f:
            f.write("status=Normal Completion\nsweep_points=4\nbanked_at=1\n")

    def _terminal_profile(self, d, mtime=2000):
        """A terminal profile in AEDT's real shape: named Solution Process
        group, escaped-quote footnote. The previous fixture had neither, so
        the guard tested green while being inert on every real solve."""
        path = os.path.join(d, "DV3019_S1_V1.profile")
        with open(path, "w") as f:
            f.write("$begin 'Profile'\n\t$begin 'ProfileGroup'\n"
                    "\t\tName='Solution Process'\n"
                    "\t\tProfileFootnote('I(2, 1, \\'Stop Time\\', "
                    "\\'08/07/2026 00:43:14\\', 1, \\'Status\\', "
                    "\\'Normal Completion\\')', 0)\n"
                    "\t$end 'ProfileGroup'\n$end 'Profile'\n")
        os.utime(path, (mtime, mtime))
        return path

    def _unfinished_profile(self, d, mtime=2000):
        path = os.path.join(d, "DV3019_S1_V1.profile")
        with open(path, "w") as f:
            f.write("$begin 'Profile'\nProfileItem('Frequency Sweep', 0, 0, 0, 0, 0, "
                    "'I(5, 1, 'Elapsed Time', '00:01:00', 1, 'Total Memory', '325 MB', "
                    "false)', false, true)\n$end 'Profile'\n")
        os.utime(path, (mtime, mtime))
        return path

    def _semaphore(self, root, mtime):
        sem = os.path.join(root, ".probe.asol.semaphore")
        with open(sem, "w") as f:
            f.write("")
        os.utime(sem, (mtime, mtime))

    def test_banked_workspace_verdict(self):
        st = self._state_dir()
        project, d = self._project_and_results()
        self._banked(st)
        self._terminal_profile(d, mtime=2000)
        self.assertEqual(self.common.guard_verdict(project, state_dir=st),
                         self.common.GUARD_BANKED)

    def test_banked_workspace_without_results_dir_verdict(self):
        st = self._state_dir()
        self._banked(st)
        self.assertEqual(
            self.common.guard_verdict(os.path.join(self.tmp, "probe.aedt"), state_dir=st),
            self.common.GUARD_BANKED)

    def test_unbanked_with_evidence_refuses(self):
        st = self._state_dir()
        project, d = self._project_and_results()
        self._terminal_profile(d, mtime=2000)
        self._semaphore(project + "results", mtime=1500)
        self.assertEqual(self.common.guard_verdict(project, state_dir=st),
                         self.common.GUARD_REFUSE)

    def test_unbanked_never_solved_proceeds(self):
        st = self._state_dir()
        project = os.path.join(self.tmp, "probe.aedt")
        self.assertEqual(self.common.guard_verdict(project, state_dir=st),
                         self.common.GUARD_PROCEED)

    def test_unbanked_unfinished_profile_proceeds(self):
        st = self._state_dir()
        project, d = self._project_and_results()
        self._unfinished_profile(d)
        self.assertEqual(self.common.guard_verdict(project, state_dir=st),
                         self.common.GUARD_PROCEED)

    def test_unbanked_in_flight_semaphore_proceeds(self):
        st = self._state_dir()
        project, d = self._project_and_results()
        self._terminal_profile(d, mtime=2000)
        self._semaphore(project + "results", mtime=3000)
        self.assertEqual(self.common.guard_verdict(project, state_dir=st),
                         self.common.GUARD_PROCEED)

    def test_guard_constants_distinct(self):
        self.assertEqual(len({self.common.GUARD_BANKED, self.common.GUARD_REFUSE,
                              self.common.GUARD_PROCEED}), 3)


class TestStalePin(unittest.TestCase):
    """Attach routing on the pinned port: bounded connect, stale-pin verdict.

    The dead-pin path is a unit simulation: the probe is injected (the
    socket connect would hang until `STALE_PIN_TIMEOUT`; it never answers)
    and the AEDT entry points (Hfss/Desktop) are fakes, so the route
    decision, the verdict print, the pin clear, and the re-pin run with no
    AEDT, no license, no desktop — the same no-AEDT seam the other suites
    use. ws_common.STATE is redirected to a throwaway tree so no checked-in
    state file is ever written.
    """

    @classmethod
    def setUpClass(cls):
        cls.common = load("ws_common")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self._state = os.path.join(self.tmp, "results", "state")
        os.makedirs(self._state)
        self.launched = []
        self.attached = []
        self._orig = (self.common.STATE, self.common.Hfss, self.common.Desktop)
        self.common.STATE = self._state
        self.addCleanup(self._restore)

        class FakeDesktop:
            port = 0
            aedt_process_id = 0

        class LaunchedHfss:
            """A fresh desktop: its own port/pid is the truth."""

            def __init__(self):
                fd = FakeDesktop()
                fd.port = 61234
                fd.aedt_process_id = 4242
                self.desktop_class = fd

        class AttachedHfss:
            """An attach: pinned port stays the source of truth."""

            def __init__(self):
                self.desktop_class = FakeDesktop()

        def fake_hfss(**kw):
            if kw.get("new_desktop"):
                self.launched.append(kw)
                return LaunchedHfss()
            self.attached.append(kw)
            return AttachedHfss()

        def fake_desktop(**kw):
            self.attached.append(kw)
            return FakeDesktop()

        self.common.Hfss = fake_hfss
        self.common.Desktop = fake_desktop

    def _restore(self):
        self.common.STATE, self.common.Hfss, self.common.Desktop = self._orig

    def _pin(self, port, pid="9999"):
        with open(os.path.join(self._state, "aedt_port.txt"), "w") as f:
            f.write(str(port))
        if pid is not None:
            with open(os.path.join(self._state, "aedt_process_id.txt"), "w") as f:
                f.write(str(pid))

    def _stale_probe(self, port):
        """The time-out path of the bounded connect: never answers."""
        return False

    def test_dead_pin_fails_fast_as_stale_and_repins(self):
        self._pin(60123)
        with contextlib.redirect_stdout(io.StringIO()) as out:
            hfss = self.common.attach(probe=self._stale_probe)
        msg = out.getvalue()
        self.assertIn("stale pin", msg)
        self.assertIn("re-pinning", msg)
        self.assertIn("no hanging attach", msg)
        self.assertEqual(len(self.attached), 0)    # stale pin never attached against
        self.assertEqual(len(self.launched), 1)    # fresh desktop launched instead
        self.assertEqual(self.common.read_state("aedt_port"), "61234")  # re-pinned
        self.assertEqual(self.common.read_state("aedt_process_id"), "4242")
        self.assertIsNotNone(hfss)

    def test_live_pin_attaches_pinned_and_never_launches(self):
        self._pin(60123)
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.common.attach(probe=lambda port: True)
        self.assertNotIn("stale pin", out.getvalue())
        self.assertEqual(len(self.launched), 0)
        self.assertEqual(len(self.attached), 2)   # Desktop(port) + Hfss(port)
        self.assertEqual(self.attached[0].get("port"), 60123)
        self.assertEqual(self.attached[1].get("port"), 60123)
        self.assertEqual(self.common.read_state("aedt_port"), "60123")  # pin untouched

    def test_no_pin_skips_probe_and_attaches_anywhere(self):
        probe = mock.Mock(return_value=True)
        with contextlib.redirect_stdout(io.StringIO()):
            self.common.attach(probe=probe)
        probe.assert_not_called()
        self.assertEqual(len(self.attached), 2)   # Desktop + Hfss, no port kw
        self.assertIsNone(self.attached[0].get("port"))
        self.assertEqual(len(self.launched), 0)

    def test_explicit_launch_skips_probe_and_repins(self):
        self._pin(60123)
        probe = mock.Mock(side_effect=AssertionError("launch must not probe"))
        with contextlib.redirect_stdout(io.StringIO()):
            self.common.attach(launch=True, probe=probe)
        probe.assert_not_called()
        self.assertEqual(len(self.launched), 1)
        self.assertEqual(self.attached, [])
        self.assertEqual(self.common.read_state("aedt_port"), "61234")

    def test_pin_probe_applies_bound_and_simulated_timeout_is_dead(self):
        with mock.patch.object(self.common.socket, "socket") as sock:
            s = sock.return_value.__enter__.return_value
            s.connect.side_effect = socket.timeout(
                "simulated: connect would hang past the bound")
            self.assertFalse(self.common._pin_probe(60123))
            s.settimeout.assert_called_once_with(self.common.STALE_PIN_TIMEOUT)
            s.connect.assert_called_once_with(("127.0.0.1", 60123))

    def test_pin_probe_refused_is_dead_and_connect_succeeds_alive(self):
        with mock.patch.object(self.common.socket, "socket") as sock:
            s = sock.return_value.__enter__.return_value
            s.connect.side_effect = ConnectionRefusedError("no listener on the pin")
            self.assertFalse(self.common._pin_probe(60123))
        with mock.patch.object(self.common.socket, "socket") as sock:
            s = sock.return_value.__enter__.return_value
            self.assertTrue(self.common._pin_probe(60123))

    def test_pin_probe_zero_is_dead_without_any_socket_call(self):
        with mock.patch.object(self.common.socket, "socket") as sock:
            self.assertFalse(self.common._pin_probe(0))
            sock.assert_not_called()


if __name__ == "__main__":
    unittest.main()
