"""Tests for the template runner scripts at the no-AEDT seams.

Covers poll_solve (scan + state machine + progress line), capture_state
(shape extraction + normalization), 12_verify_sync (diff, replay
selection, copy hygiene), and 00_static_gate (compile/import gate on
throwaway trees). No AEDT, no license, no desktop: every module under
test imports only the standard library at module level.

Run:  python -m unittest src.test_template_runners -v
   or: python src/test_template_runners.py
"""

import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest

SRC = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location("tp_" + name, os.path.join(SRC, name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestPollSolveScan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pollsolve = load("poll_solve")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _results(self):
        root = os.path.join(self.tmp, "probe.aedtresults")
        os.makedirs(os.path.join(root, "Adaptive.asol"), exist_ok=True)
        os.makedirs(os.path.join(root, "Sweep", "F199.sd"), exist_ok=True)
        os.makedirs(os.path.join(root, "F1.sd"), exist_ok=True)
        with open(os.path.join(root, "F1.sd", "native.adp"), "w") as f:
            f.write("x" * 13)
        with open(os.path.join(root, "top.bin"), "w") as f:
            f.write("y" * 7)
        return root

    def test_scan_counts_recursive_growth(self):
        (a, s, n, b) = self.pollsolve.scan_results(self._results())
        self.assertEqual((a, s), (1, 2))
        self.assertEqual((n, b), (2, 20))

    def test_scan_missing_dir_is_zero(self):
        self.assertEqual(self.pollsolve.scan_results(
            os.path.join(self.tmp, "nope.aedtresults")), (0, 0, 0, 0))

    def test_project_results_dir(self):
        self.assertEqual(self.pollsolve.project_results_dir(r"C:\x\m.aedt"),
                         r"C:\x\m.aedtresults")


class TestPollSolveStateMachine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pollsolve = load("poll_solve")

    def _tick(self, cfg, metrics, prev, state):
        return self.pollsolve.watchdog_tick(prev, metrics, state, cfg)

    def test_never_grew_stalls_after_start_ticks(self):
        zm = (0, 0, 0, 0)
        cfg = {"start_ticks": 3}
        state = {"grown": False, "unchanged": 0}
        prev = None
        seen = []
        for _ in range(4):
            status, state = self._tick(cfg, zm, prev, state)
            seen.append(status)
            prev = zm
        self.assertEqual(seen[:3], ["running", "running", "running"])
        self.assertEqual(seen[3], "stalled")

    def test_completion_with_expected_sd_after_settle(self):
        cfg = {"expected_sd": 2, "settle_ticks": 2, "stall_ticks": 9}
        cur = (1, 2, 5, 100)  # already >= expected on the first sample
        state = {"grown": False, "unchanged": 0}
        prev = None
        statuses = []
        for _ in range(4):
            status, state = self._tick(cfg, cur, prev, state)
            statuses.append(status)
            prev = cur
        self.assertEqual(statuses, ["settling", "settling", "complete", "complete"])

    def test_completion_without_expected_after_growth_settle(self):
        cfg = {"settle_ticks": 2}
        cur = (1, 2, 5, 100)
        state = {"grown": False, "unchanged": 0}
        prev = None
        s1, state = self._tick(cfg, cur, prev, state)
        prev = cur
        s2, state = self._tick(cfg, cur, prev, state)
        s3, state = self._tick(cfg, cur, prev, state)
        self.assertEqual([s1, s2, s3], ["settling", "settling", "complete"])

    def test_plateau_after_growth_marks_stalled(self):
        cfg = {"settle_ticks": 5, "stall_ticks": 2}
        cur = (1, 2, 5, 100)
        state = {"grown": False, "unchanged": 0}
        prev = None
        self._tick(cfg, cur, prev, state)
        prev = cur
        s2, state = self._tick(cfg, cur, prev, state)
        s3, state = self._tick(cfg, cur, prev, state)
        self.assertEqual(s2, "settling")
        self.assertEqual(s3, "stalled")

    def test_regrowth_resets_the_settle_counter(self):
        cfg = {"settle_ticks": 3}
        state = {"grown": False, "unchanged": 0}
        prev = None
        grow = (1, 2, 5, 100)
        self._tick(cfg, grow, prev, state)
        prev = grow
        for _ in range(2):
            _, state = self._tick(cfg, grow, prev, state)
        self.assertEqual(state["unchanged"], 2)
        bigger = (1, 3, 6, 150)
        s, state = self._tick(cfg, bigger, prev, state)
        self.assertTrue(state["grown"])
        self.assertEqual(state["unchanged"], 0)
        self.assertEqual(s, "settling")

    def test_progress_line_shape(self):
        line = self.pollsolve.format_progress(
            3, "settling", (1, 2, 5, 100), {"unchanged": 1}, {"expected_sd": 2},
            61, 1000)
        for token in ("tick=3", "status=settling", "asol=1", "sd=2",
                      "bytes=100", "expected_sd=2", "elapsed_s=61"):
            self.assertIn(token, line)

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
            ["objects", "bboxes", "materials", "boundaries", "excitations",
             "setups", "sweeps", "variables"])


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


if __name__ == "__main__":
    unittest.main()
