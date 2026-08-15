"""Tier 0 suite for the Design Spec — seconds, no AEDT, no license.

Tickets 07/08/10/12a. The point of the whole phase-2 bet is that the build
path becomes checkable without license-hours, so this file is the evidence for
that claim: a recorder stands in for the desktop and the compiler's call
sequence is asserted exactly.

Two rules this suite enforces about itself:

- **Fixture fidelity** (`docs/agents/fixture-fidelity.md`). The reducer tests
  run against the five real captured snapshots in `knowledge/cases/_snapshots/`
  and the pilot's own `model_snapshot.json`, not against hand-written JSON. Two
  P0 bugs already reached production behind hand-written fixtures.
- **Import layering.** Every module except `compiler` must import with no
  pyAEDT anywhere, and a test asserts it.

Run: `python hfss_spec/test_hfss_spec.py`
"""

import json
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from hfss_spec import compiler, snapshot_to_spec                    # noqa: E402
from hfss_spec.expressions import ExpressionError, resolve_all      # noqa: E402
from hfss_spec.loader import SpecLoadError, dump_spec, load_spec, spec_from_dict  # noqa: E402
from hfss_spec.schema import DesignSpec, json_schema                # noqa: E402
from hfss_spec.units import UnitError, parse_quantity               # noqa: E402
from hfss_spec.validate import SpecNotValidated, validate           # noqa: E402

CASES = REPO / "knowledge" / "cases"
SNAPSHOTS = CASES / "_snapshots"
PILOT_SNAPSHOT = (REPO / "workspaces" / "bowtie-3500-pilot" / "results" / "state"
                  / "model_snapshot.json")
PATCH_SPEC = CASES / "patch-2400" / "design.yaml"


# --- a desktop that only records -------------------------------------------


class FakeFace:
    def __init__(self, center, area, fid):
        self.center = center
        self.area = area
        self.id = fid


class FakeObject:
    def __init__(self, name, bbox=(0, 0, 0, 1, 1, 1), faces=()):
        self.name = name
        self.bounding_box = list(bbox)
        self.faces = list(faces)
        self.material_name = ""


class FakeBoundary:
    def __init__(self, name, owner):
        self.name = name
        self._owner = owner

    def delete(self):
        self._owner.calls.append(("boundary.delete", self.name))
        self._owner.boundaries = [b for b in self._owner.boundaries if b is not self]


class FakeModeler:
    def __init__(self, owner):
        self._owner = owner
        self.object_names = []
        self.objects = {}

    def __getitem__(self, name):
        return self.objects.get(name)

    def _record(self, op, **kwargs):
        self._owner.calls.append((op, kwargs))

    def _add(self, name):
        if name not in self.object_names:
            self.object_names.append(name)
        self.objects.setdefault(name, FakeObject(name))

    def delete(self, name):
        self._record("delete", name=name)
        self.object_names = [n for n in self.object_names if n != name]

    def create_box(self, origin, sizes, name, material=None):
        self._record("create_box", origin=origin, sizes=sizes, name=name,
                     material=material)
        self._add(name)

    def create_rectangle(self, orientation, origin, sizes, name, material=None):
        self._record("create_rectangle", orientation=orientation, origin=origin,
                     sizes=sizes, name=name, material=material)
        self._add(name)

    def create_cylinder(self, orientation, origin, radius, height, name, material=None):
        self._record("create_cylinder", orientation=orientation, origin=origin,
                     radius=radius, height=height, name=name, material=material)
        self._add(name)

    def unite(self, assignment):
        self._record("unite", assignment=assignment)

    def subtract(self, blank, tools, keep_originals):
        self._record("subtract", blank=blank, tools=tools,
                     keep_originals=keep_originals)

    def sweep_along_vector(self, assignment, sweep_vector, draft_angle, draft_type):
        self._record("sweep_along_vector", assignment=assignment,
                     sweep_vector=sweep_vector, draft_angle=draft_angle,
                     draft_type=draft_type)

    def connect(self, assignment):
        self._record("connect", assignment=assignment)


class FakeSetup:
    def __init__(self, name, owner):
        self.name = name
        self.props = {}
        self._owner = owner

    def update(self):
        self._owner.calls.append(("setup.update", dict(self.props)))


class FakeHfss:
    """Records every call the compiler makes. No AEDT anywhere near it."""

    def __init__(self, valid=True):
        self.calls = []
        self.modeler = FakeModeler(self)
        self.boundaries = []
        self.setup_names = []
        self.variables = {}
        self._solution_type = None
        self._valid = valid
        self.materials = self

    # solution type
    @property
    def solution_type(self):
        return self._solution_type

    @solution_type.setter
    def solution_type(self, value):
        self._solution_type = value
        self.calls.append(("solution_type", value))

    # variables
    def __setitem__(self, name, expression):
        self.variables[name] = expression
        self.calls.append(("variable", name, expression))

    # materials surface
    def checkifmaterialexists(self, name):
        return False

    def add_material(self, name):
        self.calls.append(("add_material", name))
        return type("M", (), {})()

    # ports and boundaries
    def lumped_port(self, **kwargs):
        self.calls.append(("lumped_port", kwargs))
        self.boundaries.append(FakeBoundary(kwargs["name"], self))

    def wave_port(self, **kwargs):
        self.calls.append(("wave_port", kwargs))
        self.boundaries.append(FakeBoundary(kwargs["name"], self))

    def assign_radiation_boundary_to_objects(self, target, name):
        self.calls.append(("radiation", target, name))
        self.boundaries.append(FakeBoundary(name, self))

    def assign_perfecte_to_sheets(self, target, name):
        self.calls.append(("perfect_e", target, name))
        self.boundaries.append(FakeBoundary(name, self))

    # setup
    def delete_setup(self, name):
        self.calls.append(("delete_setup", name))
        self.setup_names = [s for s in self.setup_names if s != name]

    def create_setup(self, name):
        self.calls.append(("create_setup", name))
        self.setup_names.append(name)
        return FakeSetup(name, self)

    def create_linear_count_sweep(self, **kwargs):
        self.calls.append(("sweep", kwargs))

    def validate_simple(self):
        return self._valid

    def ops(self, kind):
        return [c for c in self.calls if c[0] == kind]


# --- units and expressions --------------------------------------------------


class TestUnits(unittest.TestCase):
    def test_literal_with_unit(self):
        self.assertEqual(parse_quantity("52.64mm").si, 0.05264)
        self.assertEqual(parse_quantity("2.4GHz").si, 2.4e9)
        self.assertEqual(parse_quantity(4.4).unit, "")

    def test_unknown_unit_is_an_error(self):
        with self.assertRaises(UnitError):
            parse_quantity("5furlongs")

    def test_aedt_spellings_round_trip(self):
        for raw, si in (("1in", 0.0254), ("1mil", 2.54e-5), ("1cm", 0.01)):
            self.assertAlmostEqual(parse_quantity(raw).si, si)


class TestExpressions(unittest.TestCase):
    def test_variable_reference_and_arithmetic(self):
        scope = resolve_all({"h": "1.6mm", "sub": "h*6"})
        self.assertAlmostEqual(scope["sub"].si, 0.0096)

    def test_unit_literal_inside_an_expression(self):
        """AEDT writes `patch_L + 2mm` routinely; it is not valid Python."""
        scope = resolve_all({"patch_L": "29.4216mm", "pad": "patch_L + 2mm"})
        self.assertAlmostEqual(scope["pad"].si, 0.0314216)

    def test_wavelength_from_c0(self):
        scope = resolve_all({"f0": "2.4GHz", "lam": "c0/f0"})
        self.assertAlmostEqual(scope["lam"].si, 0.1249135, places=6)
        self.assertEqual(str(scope["lam"].dimension), "length")

    def test_adding_a_frequency_to_a_length_is_an_error(self):
        with self.assertRaises(ExpressionError) as caught:
            resolve_all({"f": "2.4GHz", "L": "1mm", "bad": "f+L"})
        self.assertIn("cannot add", str(caught.exception))

    def test_cycle_names_the_ring(self):
        with self.assertRaises(ExpressionError) as caught:
            resolve_all({"a": "b+1", "b": "a+1"})
        self.assertIn("a -> b -> a", str(caught.exception))


# --- schema -----------------------------------------------------------------


def minimal_spec(**overrides) -> dict:
    data = {
        "spec_version": 1,
        "name": "t",
        "recipe": "r",
        "provenance": {"source": "test", "canonical_reading": "closed-form"},
        "variables": {"f0": "2.4GHz", "w": "10mm"},
        "geometry": [
            {"op": "box", "name": "Sub", "origin": ["0mm", "0mm", "0mm"],
             "size": ["w", "w", "1.6mm"]},
        ],
        "excitations": [
            {"name": "P1", "type": "wave_port", "on": {"object": "Sub"}},
        ],
        "boundaries": [
            {"name": "Rad", "type": "radiation", "on": {"outer_faces": "Sub"}},
        ],
        "setup": {"name": "Setup1", "solution_frequency": "f0"},
        "qa_signals": ["convergence"],
    }
    data.update(overrides)
    return data


class TestSchema(unittest.TestCase):
    def test_no_field_accepts_a_face_id(self):
        """Symbolic selectors are a type, not a convention (env-compat #7/#8)."""
        text = json.dumps(json_schema())
        for banned in ('"face_id"', '"faceid"', '"edge_id"', '"edgeid"'):
            self.assertNotIn(banned, text.lower())

    def test_unknown_field_is_rejected(self):
        with self.assertRaises(SpecLoadError) as caught:
            spec_from_dict(minimal_spec(colour="red"))
        self.assertIn("colour", caught.exception.report.text())

    def test_missing_required_op_field_names_the_op(self):
        broken = minimal_spec(geometry=[{"op": "box", "name": "Sub"}])
        with self.assertRaises(SpecLoadError) as caught:
            spec_from_dict(broken)
        self.assertIn("origin", caught.exception.report.text())

    def test_lumped_port_without_an_integration_line_is_rejected(self):
        """pyAEDT 1.3.0 rejects a bare face — measured on the patch-2400 run."""
        broken = minimal_spec(excitations=[
            {"name": "P1", "type": "lumped_port", "on": {"object": "Sub"}}])
        with self.assertRaises(SpecLoadError) as caught:
            spec_from_dict(broken)
        self.assertIn("integration_line", caught.exception.report.text())

    def test_project_variables_keep_their_own_namespace(self):
        with self.assertRaises(SpecLoadError):
            spec_from_dict(minimal_spec(variables={"$losstan": "0"}))
        spec = spec_from_dict(minimal_spec(project_variables={"$losstan": "0"}))
        self.assertEqual(spec.project_variables, {"$losstan": "0"})

    def test_ambiguity_tiebreaks_are_mutually_exclusive(self):
        broken = minimal_spec(excitations=[{
            "name": "P1", "type": "wave_port",
            "on": {"face_of": "Sub", "direction": "-y",
                   "pick": "largest_area", "nearest": ["0mm", "0mm", "0mm"]}}])
        with self.assertRaises(SpecLoadError):
            spec_from_dict(broken)

    def test_json_schema_exports_from_the_same_models(self):
        schema = json_schema()
        self.assertEqual(schema["title"], "DesignSpec")
        self.assertIn("GeometryOp", schema["$defs"])


class TestRoundTrip(unittest.TestCase):
    def test_load_dump_load_is_stable(self):
        spec = load_spec(PATCH_SPEC)
        once = dump_spec(spec)
        twice = dump_spec(spec_from_dict(__import__("yaml").safe_load(once)))
        self.assertEqual(once, twice)


# --- validator (ticket 08) ---------------------------------------------------


class TestValidator(unittest.TestCase):
    def test_the_real_patch_spec_validates(self):
        report = validate(load_spec(PATCH_SPEC))
        self.assertTrue(report.ok, report.text())

    def test_reference_resolution_catches_a_typo(self):
        broken = minimal_spec(boundaries=[
            {"name": "Rad", "type": "radiation", "on": {"outer_faces": "Sbu"}}])
        report = validate(spec_from_dict(broken))
        self.assertFalse(report.ok)
        self.assertIn("did you mean 'Sub'", report.text())

    def test_boolean_operand_must_already_exist(self):
        broken = minimal_spec(geometry=[
            {"op": "box", "name": "Sub", "origin": ["0mm"] * 3,
             "size": ["w", "w", "1mm"]},
            {"op": "subtract", "name": "Sub", "tools": ["Slot"]},
        ])
        report = validate(spec_from_dict(broken))
        self.assertIn("'Slot'", report.text())

    def test_dimensional_mismatch_in_geometry(self):
        broken = minimal_spec(geometry=[
            {"op": "box", "name": "Sub", "origin": ["0mm"] * 3,
             "size": ["w", "w", "f0"]}])
        report = validate(spec_from_dict(broken))
        self.assertIn("must be length", report.text())

    def test_zero_extent_is_an_error(self):
        broken = minimal_spec(geometry=[
            {"op": "box", "name": "Sub", "origin": ["0mm"] * 3,
             "size": ["w", "w", "0mm"]}])
        report = validate(spec_from_dict(broken))
        self.assertIn("must be positive", report.text())

    def test_sweep_must_bracket_the_target(self):
        """The pilot's own failure mode: a resonance outside the swept band."""
        broken = minimal_spec(
            target={"quantity": "resonant_frequency", "value": "3.9GHz",
                    "tolerance_pct": 5},
            setup={"name": "Setup1", "solution_frequency": "f0",
                   "sweep": {"name": "S", "start": "2.0GHz", "stop": "3.0GHz",
                             "count": 101}})
        report = validate(spec_from_dict(broken))
        self.assertFalse(report.ok)
        self.assertIn("does not contain the target", report.text())

    def test_a_narrow_bracket_warns_but_passes(self):
        spec = spec_from_dict(minimal_spec(
            setup={"name": "Setup1", "solution_frequency": "f0",
                   "sweep": {"name": "S", "start": "2.0GHz", "stop": "3.0GHz",
                             "count": 101}}))
        report = validate(spec)
        self.assertTrue(report.ok)
        self.assertTrue(any("near side" in w.message for w in report.warnings))

    def test_recipe_completeness_needs_an_excitation(self):
        report = validate(spec_from_dict(minimal_spec(excitations=[])))
        self.assertIn("nothing drives the model", report.text())

    def test_qa_signal_without_its_evidence(self):
        report = validate(spec_from_dict(
            minimal_spec(qa_signals=["in_band_resonance"])))
        self.assertIn("in_band_resonance cannot be reported", report.text())

    def test_reducer_placeholders_are_refused(self):
        broken = minimal_spec(geometry=[
            {"op": "unknown", "name": "Sub", "bbox": [0, 0, 0, 1, 1, 1]}])
        report = validate(spec_from_dict(broken))
        self.assertFalse(report.ok)
        self.assertIn("op: unknown", report.text())

    def test_findings_carry_a_spec_path(self):
        broken = minimal_spec(geometry=[
            {"op": "box", "name": "Sub", "origin": ["0mm"] * 3,
             "size": ["w", "w", "f0"]}])
        report = validate(spec_from_dict(broken))
        self.assertTrue(any(f.path.startswith("geometry[0].size[")
                            for f in report.errors), report.text())


# --- compiler (ticket 10) ----------------------------------------------------


class TestCompilerGolden(unittest.TestCase):
    def build(self, spec=None):
        spec = spec or load_spec(PATCH_SPEC)
        hfss = FakeHfss()
        log = compiler.build(spec, hfss)
        return hfss, log

    def test_the_validator_is_a_hard_gate(self):
        broken = spec_from_dict(minimal_spec(excitations=[]))
        with self.assertRaises(SpecNotValidated):
            compiler.build(broken, FakeHfss())

    def test_spine_order_and_one_line_per_stage(self):
        _hfss, log = self.build()
        self.assertEqual([r.stage for r in log.results], list(compiler.STAGES))
        for line in log.lines:
            self.assertTrue(line.startswith("PASS: "), line)
            self.assertEqual(len(line.splitlines()), 1)

    def test_solution_type_is_explicit(self):
        """AEDT defaults to Terminal; Modal must be stated (env-compat #11)."""
        hfss, _log = self.build()
        self.assertEqual(hfss.solution_type, "Modal")

    def test_every_variable_reaches_aedt_with_its_expression_intact(self):
        hfss, _log = self.build()
        self.assertEqual(hfss.variables["sub_W"], "80mm")
        self.assertEqual(hfss.variables["feed_run"], "sub_L/2 - patch_L/2")

    def test_geometry_call_sequence(self):
        hfss, _log = self.build()
        sequence = [c[0] for c in hfss.calls
                    if c[0] in ("create_box", "create_rectangle", "subtract", "unite")]
        self.assertEqual(sequence, [
            "create_box",        # Substrate
            "create_rectangle",  # GroundPlane
            "create_rectangle",  # Patch
            "create_rectangle",  # InsetL
            "create_rectangle",  # InsetR
            "subtract",
            "create_rectangle",  # Feed
            "unite",
            "create_box",        # AirBox
        ])

    def test_xz_rectangle_sizes_are_swapped_once_by_the_compiler(self):
        """`create_rectangle("XZ")` maps sizes to [z, x] on 2024 R1.

        Measured on the patch-2400 run, where a transposed sheet was caught by
        its bounding box. The spec always states sizes in axis order and the
        compiler does the swap, so no author has to remember it.
        """
        spec = spec_from_dict(minimal_spec(geometry=[
            {"op": "sheet", "name": "Port", "plane": "xz",
             "origin": ["0mm"] * 3, "size": ["3mm", "9mm"]},
        ], excitations=[{"name": "P1", "type": "wave_port",
                         "on": {"object": "Port"}}],
            boundaries=[]))
        hfss = FakeHfss()
        compiler.build(spec, hfss)
        call = hfss.ops("create_rectangle")[0][1]
        self.assertEqual(call["orientation"], "XZ")
        self.assertEqual(call["sizes"], ["9mm", "3mm"])

    def test_xy_rectangle_sizes_are_not_swapped(self):
        hfss, _log = self.build()
        ground = [c[1] for c in hfss.ops("create_rectangle")
                  if c[1]["name"] == "GroundPlane"][0]
        self.assertEqual(ground["sizes"], ["sub_W", "sub_L"])

    def test_idempotent_by_construction(self):
        """Re-running a stage in place converges — asserted, not doctrine."""
        spec = load_spec(PATCH_SPEC)
        hfss = FakeHfss()
        compiler.build(spec, hfss)
        first = len(hfss.modeler.object_names)
        hfss.calls.clear()
        compiler.build(spec, hfss)
        self.assertEqual(len(hfss.modeler.object_names), first)
        deleted = {c[1]["name"] for c in hfss.calls if c[0] == "delete"}
        self.assertIn("Substrate", deleted)
        self.assertIn("AirBox", deleted)

    def test_lumped_port_is_given_a_name_not_a_face(self):
        """The defect the patch-2400 run paid for, absorbed as library code."""
        hfss, _log = self.build()
        call = hfss.ops("lumped_port")[0][1]
        self.assertEqual(call["assignment"], "Substrate")
        self.assertEqual(call["impedance"], 50.0)
        self.assertEqual(len(call["integration_line"]), 2)

    def test_setup_and_sweep_carry_the_spec_values(self):
        hfss, _log = self.build()
        props = hfss.ops("setup.update")[0][1]
        self.assertEqual(props["MaximumPasses"], 15)
        self.assertEqual(props["MaxDeltaS"], 0.02)
        sweep = hfss.ops("sweep")[0][1]
        self.assertEqual(sweep["num_of_freq_points"], 201)
        self.assertEqual(sweep["sweep_type"], "Discrete")
        # `unit` is singular and the endpoints are bare floats in it -- the
        # first live acceptance run rejected `units=` plus unit-carrying
        # strings. The authored unit is preserved so the UI reads GHz.
        self.assertEqual(sweep["unit"], "GHz")
        self.assertEqual((sweep["start_frequency"], sweep["stop_frequency"]),
                         (2.0, 3.0))

    def test_validate_simple_failure_stops_the_build(self):
        with self.assertRaises(compiler.CompileError):
            compiler.build(load_spec(PATCH_SPEC), FakeHfss(valid=False))

    def test_no_pyaedt_import_at_module_import_time(self):
        self.assertNotIn("ansys.aedt.core", sys.modules)


class TestSelectors(unittest.TestCase):
    def selector(self, **kwargs):
        from hfss_spec.schema import FaceOf
        return FaceOf(**kwargs)

    def hfss_with(self, faces):
        hfss = FakeHfss()
        hfss.modeler.objects["Sub"] = FakeObject("Sub", faces=faces)
        return hfss

    def test_unique_face_resolves(self):
        faces = [FakeFace((0, -5, 0), 10.0, 1), FakeFace((0, 5, 0), 10.0, 2)]
        face = compiler.resolve_face(self.hfss_with(faces),
                                     self.selector(face_of="Sub", direction="-y"), None)
        self.assertEqual(face.id, 1)

    def test_ambiguity_is_an_error_by_default(self):
        """Q3: silently picking the wrong face builds a model that simulates
        nonsense, which is the worst failure class this tool has."""
        faces = [FakeFace((0, -5, 0), 10.0, 1), FakeFace((0, -5, 3), 2.0, 2)]
        with self.assertRaises(compiler.SelectorError) as caught:
            compiler.resolve_face(self.hfss_with(faces),
                                  self.selector(face_of="Sub", direction="-y"), None)
        self.assertIn("pick: largest_area", str(caught.exception))

    def test_explicit_pick_opts_in(self):
        faces = [FakeFace((0, -5, 0), 10.0, 1), FakeFace((0, -5, 3), 2.0, 2)]
        face = compiler.resolve_face(
            self.hfss_with(faces),
            self.selector(face_of="Sub", direction="-y", pick="largest_area"), None)
        self.assertEqual(face.id, 1)


# --- reducer (ticket 12a) ----------------------------------------------------


class TestSnapshotToSpec(unittest.TestCase):
    """Against real captured snapshots only — see the fixture-fidelity rule."""

    def snapshots(self):
        return sorted(SNAPSHOTS.glob("*.json"))

    def test_corpus_is_present(self):
        self.assertGreaterEqual(len(self.snapshots()), 5)
        self.assertTrue(PILOT_SNAPSHOT.exists())

    def test_every_real_snapshot_reduces(self):
        for path in self.snapshots() + [PILOT_SNAPSHOT]:
            with self.subTest(path.name):
                reduction = snapshot_to_spec.reduce_snapshot(
                    snapshot_to_spec.load_snapshot(path))
                self.assertIn("variables", reduction.spec)
                self.assertIn("setup", reduction.spec)

    def test_port_counts_match_the_verified_numbers(self):
        """coplanar 2, bandpass 2, probe-fed patch 1, horn 1, parabolic 1.

        Terminals are port-typed too, and every snapshot captured before the
        terminal-suffix rule stored them as ports — so the reducer recomputes
        from raw boundaries instead of trusting the stored section.
        """
        expected = {"coplanar-wg-3ghz": 2, "bandpass-1p5ghz": 2,
                    "patch-10GHZ-probe-fed": 1, "horn-10ghz": 1,
                    "parabolic-10ghz": 1}
        for path in self.snapshots():
            with self.subTest(path.stem):
                reduction = snapshot_to_spec.reduce_snapshot(
                    snapshot_to_spec.load_snapshot(path))
                self.assertEqual(len(reduction.spec["excitations"]),
                                 expected[path.stem])

    def test_project_scope_is_kept_separate(self):
        """`$losstan` is a different AEDT namespace; flattening writes back wrong."""
        reduction = snapshot_to_spec.reduce_snapshot(
            snapshot_to_spec.load_snapshot(SNAPSHOTS / "coplanar-wg-3ghz.json"))
        self.assertIn("$losstan", reduction.spec["project_variables"])
        self.assertNotIn("$losstan", reduction.spec["variables"])

    def test_variable_expressions_are_verbatim(self):
        raw = snapshot_to_spec.load_snapshot(SNAPSHOTS / "horn-10ghz.json")
        reduction = snapshot_to_spec.reduce_snapshot(raw)
        for name, expression in raw["variables"].items():
            if not name.startswith("$"):
                self.assertEqual(reduction.spec["variables"][name], str(expression))

    def test_parametric_variation_strings_are_not_read_as_sweeps(self):
        """Real `sweeps` lists mix genuine sweeps with parametric tables."""
        raw = snapshot_to_spec.load_snapshot(SNAPSHOTS / "coplanar-wg-3ghz.json")
        real, variations = snapshot_to_spec._split_sweeps(raw["sweeps"])
        self.assertTrue(variations)
        self.assertTrue(all("='" not in s for s in real))

    def test_geometry_is_unknown_without_object_kinds(self):
        """A bbox is a consequence of a construction op, not a restatement."""
        reduction = snapshot_to_spec.reduce_snapshot(
            snapshot_to_spec.load_snapshot(SNAPSHOTS / "parabolic-10ghz.json"))
        self.assertEqual(reduction.unknown_geometry,
                         len(reduction.spec["geometry"]))
        self.assertTrue(any("object_kinds" in m for m in reduction.missing))

    def test_object_kinds_promote_a_planar_sheet(self):
        raw = snapshot_to_spec.load_snapshot(SNAPSHOTS / "horn-10ghz.json")
        name = raw["objects"][0]
        raw["object_kinds"] = {name: "sheet"}
        raw["bboxes"][name] = [0.0, 0.0, 0.0, 2.0, 3.0, 0.0]
        reduction = snapshot_to_spec.reduce_snapshot(raw)
        entry = [g for g in reduction.spec["geometry"] if g["name"] == name][0]
        self.assertEqual(entry["op"], "sheet")
        self.assertEqual(entry["plane"], "xy")
        self.assertEqual(entry["size"], ["2in", "3in"])

    def test_pilot_snapshot_reports_its_missing_setup_properties(self):
        """The pilot's snapshot recorded `{}` for its setup — the v1 defect."""
        reduction = snapshot_to_spec.reduce_snapshot(
            snapshot_to_spec.load_snapshot(PILOT_SNAPSHOT))
        self.assertTrue(any("setup properties" in m for m in reduction.missing))
        self.assertTrue(any("model_units" in m for m in reduction.missing))

    def test_a_reduced_spec_loads_into_the_schema(self):
        """Reduction output must be schema-shaped even when incomplete."""
        reduction = snapshot_to_spec.reduce_snapshot(
            snapshot_to_spec.load_snapshot(SNAPSHOTS / "horn-10ghz.json"))
        spec = spec_from_dict(reduction.spec)
        self.assertEqual(spec.spec_version, 1)
        # ...and the validator must then refuse to compile it.
        self.assertFalse(validate(spec).ok)


class TestAcceptance(unittest.TestCase):
    """Ticket 11's diff, exercised offline against the pilot's real snapshot."""

    def pilot(self):
        return json.loads(PILOT_SNAPSHOT.read_text(encoding="utf-8"))

    def test_a_snapshot_matches_itself(self):
        from hfss_spec import acceptance
        result = acceptance.compare(self.pilot(), self.pilot())
        self.assertTrue(result.ok, result.text())

    def test_random_suffixes_are_normalised_not_reported(self):
        """`Rad__M4WFEW` vs `Rad__QQ11ZZ` is AEDT noise, not a difference."""
        from hfss_spec import acceptance
        built = json.loads(json.dumps(self.pilot()))
        built["boundaries"] = {("Rad__QQ11ZZ" if k.startswith("Rad__") else k): v
                               for k, v in built["boundaries"].items()}
        result = acceptance.compare(self.pilot(), built)
        self.assertTrue(result.ok, result.text())

    def test_a_missing_object_is_a_compiler_bug(self):
        from hfss_spec import acceptance
        built = json.loads(json.dumps(self.pilot()))
        built["objects"] = [n for n in built["objects"] if n != "PatchBowtie"]
        result = acceptance.compare(self.pilot(), built)
        self.assertEqual([d.classification for d in result.differences],
                         [acceptance.COMPILER_BUG])

    def test_a_left_over_intermediate_is_a_schema_gap(self):
        from hfss_spec import acceptance
        built = json.loads(json.dumps(self.pilot()))
        built["objects"] = built["objects"] + ["PatchTriUp"]
        result = acceptance.compare(self.pilot(), built)
        self.assertEqual([d.classification for d in result.differences],
                         [acceptance.SCHEMA_GAP])

    def test_a_changed_variable_is_reported_with_both_values(self):
        from hfss_spec import acceptance
        built = json.loads(json.dumps(self.pilot()))
        built["variables"]["SubW"] = "91mm"
        result = acceptance.compare(self.pilot(), built)
        self.assertIn("variables.SubW", result.text())
        self.assertIn("90mm", result.text())
        self.assertIn("91mm", result.text())

    def test_bbox_deltas_are_a_magnitude_not_a_boolean(self):
        from hfss_spec import acceptance
        built = json.loads(json.dumps(self.pilot()))
        built["bboxes"]["Substrate"] = [x + 0.1 for x in built["bboxes"]["Substrate"]]
        deltas = acceptance.bbox_deltas(self.pilot(), built)
        self.assertEqual(set(deltas), {"Substrate"})
        self.assertAlmostEqual(deltas["Substrate"][0], 0.1)

    def test_the_bowtie_spec_declares_the_pilot_objects(self):
        """The acceptance target is reachable: the spec names what was built."""
        spec = load_spec(CASES / "bowtie-3500" / "design.yaml")
        self.assertTrue(validate(spec).ok)
        built_by_spec = set(spec.declared_objects)
        for name in self.pilot()["objects"]:
            self.assertIn(name, built_by_spec)

    def test_the_bowtie_spec_carries_every_pilot_variable(self):
        spec = load_spec(CASES / "bowtie-3500" / "design.yaml")
        for name, expression in self.pilot()["variables"].items():
            self.assertEqual(spec.variables.get(name), expression, name)


class TestPhysicsEstimators(unittest.TestCase):
    """Ticket 09. Each estimator against a worked example computed elsewhere.

    The reference numbers come from `knowledge/cases/*/case.json`, where they
    were recomputed from the textbook relations rather than copied out of a
    paper — which is the whole point, given that a paper disagreeing with
    itself is the failure this check exists to catch.
    """

    def test_effective_permittivity_balanis_14_1(self):
        from hfss_spec import physics
        ereff = physics.effective_permittivity(er=4.4, h=1.6e-3, w=38.0100e-3)
        self.assertAlmostEqual(ereff, 4.0857, places=4)

    def test_fringing_extension_balanis_14_2(self):
        from hfss_spec import physics
        dl = physics.fringing_extension(ereff=4.0857, h=1.6e-3, w=38.0100e-3)
        self.assertAlmostEqual(dl * 1e3, 0.7388, places=4)

    def test_patch_resonance_returns_the_frequency_it_was_synthesised_for(self):
        from hfss_spec import physics
        f = physics.patch_resonance(patch_l=29.4216e-3, patch_w=38.0100e-3,
                                    h=1.6e-3, er=4.4)
        self.assertAlmostEqual(f / 1e9, 2.4, places=3)

    def test_hammerstad_reproduces_the_50_ohm_synthesis(self):
        from hfss_spec import physics
        z0, ereff = physics.microstrip_impedance(w=3.0829e-3, h=1.6e-3, er=4.4)
        self.assertAlmostEqual(ereff, 3.3323, places=4)
        self.assertAlmostEqual(z0, 50.0, places=1)

    def test_guide_wavelength_matches_the_case(self):
        from hfss_spec import physics
        lam = physics.guide_wavelength(2.4e9, 3.3323)
        self.assertAlmostEqual(lam * 1e3, 68.4282, places=3)

    def test_wr90_te10_cutoff(self):
        from hfss_spec import physics
        f = physics.rectangular_waveguide_cutoff(a=0.9 * 25.4e-3)
        self.assertAlmostEqual(f / 1e9, 6.5571, places=4)

    def test_bowtie_estimator_against_the_MEASURED_pilot_resonance(self):
        """The honesty test the ticket asks for.

        The pilot's delivered geometry measured 3.85 GHz. If the estimator
        cannot get near that, it has no business flagging anyone's paper.
        """
        from hfss_spec import physics
        f = physics.bowtie_resonance(side=26.3269e-3, base=20.2168e-3,
                                     h=1.6e-3, er=4.3)
        error_pct = 100.0 * (f - 3.85e9) / 3.85e9
        self.assertLess(abs(error_pct), 2.0,
                        f"predicted {f/1e9:.4f} GHz against a measured 3.85 GHz "
                        f"({error_pct:+.2f}%)")


class TestPrecheck(unittest.TestCase):
    def test_patch_spec_is_consistent(self):
        from hfss_spec import physics
        result = physics.check(load_spec(PATCH_SPEC))
        self.assertEqual(result.verdict, "consistent", result.text())
        self.assertLess(abs(result.prediction.delta_pct), 1.0)

    def test_the_pilot_bowtie_is_flagged_against_its_own_target(self):
        """The Astuti failure class, caught in microseconds.

        The delivered geometry resonates at 3.85 GHz against a 3.5 GHz target.
        That is a real disagreement, it survived four solves and twenty hours,
        and the estimator sees it before anything is built.
        """
        from hfss_spec import physics
        result = physics.check(load_spec(CASES / "bowtie-3500" / "design.yaml"))
        self.assertEqual(result.verdict, "INCONSISTENT", result.text())
        self.assertGreater(result.prediction.delta_pct, 8.0)

    def test_astuti_table_reading_is_flagged_harder(self):
        """Astuti et al. 2022's Table I, as a fixture.

        Table I reads 46 x 23 mm where the figure and the equations give
        52.64 x 26.32. Building the Table reading would have put the resonance
        ~24% above the stated 3.5 GHz target.
        """
        from hfss_spec import physics
        table = physics.bowtie_resonance(side=23.0e-3, base=46.0e-3,
                                         h=1.6e-3, er=4.3)
        figure = physics.bowtie_resonance(side=26.32e-3, base=52.64e-3,
                                          h=1.6e-3, er=4.3)
        self.assertGreater(100.0 * (table - 3.5e9) / 3.5e9, 15.0)
        self.assertNotAlmostEqual(table / 1e9, figure / 1e9, places=1)

    def test_tolerances_come_from_the_playbook_not_the_code(self):
        from hfss_spec import physics
        source = (REPO / "hfss_spec" / "physics.py").read_text(encoding="utf-8")
        recipes = physics.load_tolerances()
        self.assertIn("bow-tie-patch", recipes)
        for entry in recipes.values():
            self.assertIn("tolerance_pct", entry)
        # No recipe's tolerance is hard-coded next to its estimator.
        self.assertNotIn("tolerance_pct = 8", source)

    def test_an_unknown_recipe_reports_rather_than_raising(self):
        from hfss_spec import physics
        spec = spec_from_dict(minimal_spec(recipe="not-a-recipe"))
        result = physics.check(spec)
        self.assertEqual(result.verdict, "no-estimator")

    def test_the_check_never_blocks(self):
        """Exit code 0 even on INCONSISTENT — the user arbitrates."""
        import subprocess
        out = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "precheck.py"),
             str(CASES / "bowtie-3500" / "design.yaml")],
            capture_output=True, text=True)
        self.assertEqual(out.returncode, 0)
        self.assertIn("INCONSISTENT", out.stdout)


class TestImportLayering(unittest.TestCase):
    def test_tier0_modules_do_not_mention_pyaedt(self):
        for name in ("units", "expressions", "schema", "validate",
                     "snapshot_to_spec", "loader", "physics", "acceptance"):
            source = (REPO / "hfss_spec" / f"{name}.py").read_text(encoding="utf-8")
            with self.subTest(name):
                self.assertNotIn("ansys.aedt", source)
                self.assertNotIn("import pyaedt", source)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: hfss_spec tests={total} failed={failed}")
    sys.exit(1 if failed else 0)
