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


def real_setup_props(case="patch-10GHZ-probe-fed"):
    """A real captured setup-properties block, straight off this box.

    `docs/agents/fixture-fidelity.md`: what a setup looks like when the model
    reports it is read from the corpus, never recalled. It matters here because
    the read-back check has to pick `MaximumPasses` out of a block that also
    carries `MaxPass` — a different property with a similar name — and a
    hand-written fixture would very likely have carried only one of them.
    """
    snapshot = json.loads((SNAPSHOTS / f"{case}.json").read_text(encoding="utf-8-sig"))
    (block,) = list(snapshot["setups"].values())[:1] or [{}]
    return dict(block)


class FakeSetup:
    """A setup that keeps the model's own copy apart from the write.

    `props` is pyAEDT's copy of the arg it sent; `properties` is what the model
    reports back when asked. They are separate dicts on purpose — the P0 the
    read-back exists for is exactly the run where the two disagreed and only
    the first one was ever looked at.

    `rejects` names the keys this model silently declines to take, which is the
    live failure reproduced: AEDT kept its own `Frequency` and raised nothing.
    """

    def __init__(self, name, owner, reported=None, rejects=()):
        self.name = name
        self.props = {}
        self.properties = dict(real_setup_props() if reported is None else reported)
        self._rejects = tuple(rejects)
        self._owner = owner

    def update(self, properties=None):
        if properties:
            self.props.update(properties)
        for key, value in self.props.items():
            if key not in self._rejects:
                self.properties[key] = value
        self._owner.calls.append(("setup.update", dict(self.props)))
        return True


class WriteThroughOnlySetup:
    """A setup with no object-oriented view — `properties` is simply absent.

    pyAEDT builds that view from the setup's child object, and it is empty
    whenever the tree node did not initialise. The compiler then has nothing
    left but its own copy of the arg it sent, and has to say so.
    """

    def __init__(self, inner):
        self._inner = inner

    @property
    def name(self):
        return self._inner.name

    @property
    def props(self):
        return self._inner.props

    def update(self, properties=None):
        return self._inner.update(properties)


class FakeHfss:
    """Records every call the compiler makes. No AEDT anywhere near it."""

    def __init__(self, valid=True, setup_rejects=(), setup_reported=None,
                 setup_rename=None):
        self.calls = []
        self.modeler = FakeModeler(self)
        self.boundaries = []
        self.setup_names = []
        self.variables = {}
        self._solution_type = None
        self._valid = valid
        self._setup_rejects = setup_rejects
        self._setup_reported = setup_reported
        self._setup_rename = setup_rename
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
        # pyAEDT runs the name through `generate_unique_setup_name`, so a setup
        # that survived the delete makes the new one come back renamed.
        name = self._setup_rename or name
        self.setup_names.append(name)
        return FakeSetup(name, self, reported=self._setup_reported,
                         rejects=self._setup_rejects)

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
        # `solution_frequency: f0` reaches AEDT as the literal 2.4GHz, never as
        # the name `f0` — see TestSetupFrequency for why that distinction is
        # the whole P0.
        self.assertEqual(props["Frequency"], "2.4GHz")
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


class TestSetupFrequency(unittest.TestCase):
    """The P0 of 2026-09-01, and the check that would have caught it.

    `patch-array-5800` declared `solution_frequency: f0` with `f0: 5.8GHz` and
    solved with `Frequency='5GHz'` in both designs — pyAEDT's HFSSDrivenDefault
    template value, i.e. the compiler's write never reached AEDT. `EditSetup`
    raised nothing, and `MaximumPasses=15` in the same call landed, so every
    gate the run passed stayed green while the mesh adapted at the bottom edge
    of the 5.0-6.5GHz sweep. Two things are asserted here: the frequency is
    resolved to a literal before it is written, and the model is asked what it
    actually holds afterwards.
    """

    def spec(self, **setup):
        base = {"name": "Setup1", "solution_frequency": "f0"}
        base.update(setup)
        return spec_from_dict(minimal_spec(setup=base))

    def test_a_variable_reference_is_resolved_before_it_is_written(self):
        """AEDT's `Frequency` is a literal field, not an expression slot."""
        hfss = FakeHfss()
        compiler.build(self.spec(), hfss)
        props = hfss.ops("setup.update")[0][1]
        self.assertEqual(props["Frequency"], "2.4GHz")
        self.assertNotIn("f0", str(props["Frequency"]))

    def test_a_literal_keeps_the_unit_it_was_authored_in(self):
        hfss = FakeHfss()
        compiler.build(self.spec(solution_frequency="3.5GHz"), hfss)
        self.assertEqual(hfss.ops("setup.update")[0][1]["Frequency"], "3.5GHz")

    def test_an_expression_resolves_and_falls_back_to_hz(self):
        """The same fallback `_frequency_pair` makes: no authored unit to keep."""
        hfss = FakeHfss()
        compiler.build(self.spec(solution_frequency="f0 * 1.25"), hfss)
        self.assertEqual(hfss.ops("setup.update")[0][1]["Frequency"], "3000000000Hz")

    def test_a_solution_frequency_that_is_not_a_frequency_is_refused(self):
        """The validator gets there first; the compiler keeps its own guard.

        Called directly, because a spec this wrong cannot reach `build()` —
        which is the point: the guard is the last line, not the only one.
        """
        with self.assertRaises(SpecNotValidated):
            compiler.build(self.spec(solution_frequency="w"), FakeHfss())
        with self.assertRaises(compiler.CompileError) as caught:
            compiler._solution_frequency(self.spec(solution_frequency="w"))
        self.assertIn("not a frequency", str(caught.exception))

    # --- the read-back ------------------------------------------------------

    def rejecting_model(self):
        """The live failure, rebuilt: a model that keeps its own `Frequency`.

        The reported block is the real captured one with a single field varied
        to pyAEDT's template default — the synthetic-alongside-real shape
        `docs/agents/fixture-fidelity.md` allows, and asserted as such below.
        """
        reported = real_setup_props()
        reported["Frequency"] = "5GHz"
        return FakeHfss(setup_rejects=("Frequency",), setup_reported=reported)

    def test_the_reported_block_is_the_real_one_with_one_field_varied(self):
        real = real_setup_props()
        synthetic = real_setup_props()
        synthetic["Frequency"] = "5GHz"
        self.assertEqual(set(real), set(synthetic))
        self.assertEqual({k for k in real if real[k] != synthetic[k]}, {"Frequency"})
        # The decoy the alias list must not read as the pass ceiling.
        self.assertIn("MaximumPasses", real)
        self.assertIn("MaxPass", real)
        self.assertNotEqual(real["MaximumPasses"], real["MaxPass"])

    def test_a_frequency_the_model_did_not_take_stops_the_build(self):
        with self.assertRaises(compiler.CompileError) as caught:
            compiler.build(self.spec(), self.rejecting_model())
        message = str(caught.exception)
        self.assertIn("2.4GHz", message)       # what the spec asked for
        self.assertIn("5GHz", message)         # what the model reports
        self.assertIn("Setup1", message)

    def test_the_build_stops_at_the_setup_and_does_not_reach_validate(self):
        hfss = self.rejecting_model()
        with self.assertRaises(compiler.CompileError):
            compiler.build(self.spec(), hfss)
        self.assertEqual([c for c in hfss.calls if c[0] == "sweep"], [])

    def test_a_max_passes_the_model_did_not_take_stops_the_build(self):
        """The captured block reports 15; the spec asks for 9."""
        hfss = FakeHfss(setup_rejects=("MaximumPasses",))
        with self.assertRaises(compiler.CompileError) as caught:
            compiler.build(self.spec(max_passes=9), hfss)
        self.assertIn("max_passes", str(caught.exception))

    def test_the_verification_line_names_the_view_that_answered(self):
        hfss = FakeHfss()
        log = compiler.build(self.spec(), hfss)
        line = [r for r in log.results if r.stage == "setup_sweep"][0]
        self.assertEqual(line.assertions["frequency"], "2.4GHz")
        self.assertEqual(line.assertions["read_back"], "properties")

    def test_the_weak_view_is_used_only_as_a_fallback_and_says_so(self):
        """`props` is pyAEDT's copy of its own arg, so it can only ever agree.

        It stays in the ladder because it is the one view that always answers,
        but the Verification line has to show when a run leaned on it.
        """
        hfss = FakeHfss()
        original = hfss.create_setup
        hfss.create_setup = lambda name: WriteThroughOnlySetup(original(name))
        log = compiler.build(self.spec(), hfss)
        line = [r for r in log.results if r.stage == "setup_sweep"][0]
        self.assertEqual(line.assertions["read_back"], "props")

    def test_an_unreadable_view_falls_through_to_one_that_can_answer(self):
        """A view that answers in nothing usable must not fail a good build.

        Only the file-shaped `Frequency` spelling is corpus-verified; the
        object-oriented view's is a guess, so a value it reports that does not
        read as a frequency sends the check to the next view rather than
        stopping a build that was, in fact, written correctly.
        """
        reported = real_setup_props()
        reported["Frequency"] = "f0"
        hfss = FakeHfss(setup_rejects=("Frequency",), setup_reported=reported)
        log = compiler.build(self.spec(), hfss)
        line = [r for r in log.results if r.stage == "setup_sweep"][0]
        self.assertEqual(line.assertions["read_back"], "props")

    def test_a_frequency_no_view_can_read_stops_the_build(self):
        hfss = FakeHfss()
        original = hfss.create_setup

        def unreadable(name):
            setup = original(name)
            written = setup.update

            def update(properties=None):
                result = written(properties)
                # Both views left holding a variable name — what AEDT would
                # report if it had ever accepted the unresolved `f0`.
                setup.props["Frequency"] = "f0"
                setup.properties["Frequency"] = "f0"
                return result

            setup.update = update
            return setup

        hfss.create_setup = unreadable
        with self.assertRaises(compiler.CompileError) as caught:
            compiler.build(self.spec(), hfss)
        self.assertIn("does not read as a frequency", str(caught.exception))

    def test_a_model_that_will_not_report_its_frequency_stops_the_build(self):
        hfss = FakeHfss()
        original = hfss.create_setup

        def mute(name):
            setup = original(name)
            setup.properties = {"IsEnabled": True}
            setup.update = lambda properties=None: True   # writes nothing back
            return setup

        hfss.create_setup = mute
        with self.assertRaises(compiler.CompileError) as caught:
            compiler.build(self.spec(), hfss)
        self.assertIn("would not report", str(caught.exception))

    def test_a_renamed_setup_stops_the_build(self):
        """`create_setup` renames rather than fails when the name is taken."""
        with self.assertRaises(compiler.CompileError) as caught:
            compiler.build(self.spec(), FakeHfss(setup_rename="Setup2"))
        self.assertIn("Setup2", str(caught.exception))


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

    def test_circular_patch_reproduces_balanis_example_14_4(self):
        """er 2.32, h 0.1588 cm, a 0.529 cm, designed for 10 GHz.

        Landed 2026-08-17 from cell S6, which was asked for a circular patch,
        found no registered estimator, and proposed this rather than relabelling
        the recipe to borrow the rectangular one.
        """
        from hfss_spec import physics
        f = physics.circular_patch_resonance(a=0.529e-2, h=0.1588e-2, er=2.32)
        self.assertAlmostEqual(f / 1e9, 10.0, delta=0.5)   # -3.7%, inside 5%

    def test_circular_patch_fringing_always_lowers_the_frequency(self):
        """The disc looks electrically larger than it is, so ae > a and f falls.
        A sign error here would read as a plausible number in the wrong
        direction, which is the class of defect this whole gate exists for."""
        import math
        from hfss_spec import physics
        a, h, er = 10e-3, 1.6e-3, 4.4
        ae = physics.circular_patch_effective_radius(a, h, er)
        self.assertGreater(ae, a)
        naive = 1.8412 * physics.C0 / (2 * math.pi * a * math.sqrt(er))
        self.assertLess(physics.circular_patch_resonance(a, h, er), naive)

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


class TestHornSynthesis(unittest.TestCase):
    """The horn's dimensions are computed, not sourced, so they get checked."""

    def test_synthesis_closes_on_the_requested_gain(self):
        from hfss_spec import physics
        lam = physics.C0 / 10e9
        h = physics.optimum_pyramidal_horn(15.0, 22.86e-3, 10.16e-3, lam)
        self.assertAlmostEqual(h["gain_dbi"], 15.0, delta=0.05)

    def test_pyramidal_condition_is_satisfied(self):
        """pe == ph, or the two flares do not meet the feed at one station."""
        from hfss_spec import physics
        lam = physics.C0 / 10e9
        h = physics.optimum_pyramidal_horn(15.0, 22.86e-3, 10.16e-3, lam)
        self.assertLess(abs(h["pe"] - h["ph"]), 1e-6)

    def test_reproduces_the_textbook_worked_example(self):
        """Balanis's 22.6 dB / 11 GHz WR-90 horn: a1 16.36 cm, b1 12.85 cm."""
        from hfss_spec import physics
        h = physics.optimum_pyramidal_horn(22.6, 22.86e-3, 10.16e-3,
                                           physics.C0 / 11e9)
        self.assertAlmostEqual(h["a1"] * 1e2, 16.36, places=1)
        self.assertAlmostEqual(h["b1"] * 1e2, 12.85, places=1)

    def test_the_root_is_below_balanis_trial_value(self):
        """Why the solver scans instead of iterating upward.

        At 15 dBi on WR-90 the classic starting value G0/(2*pi*sqrt(2*pi))
        is 2.008 and the root is 1.817 — an upward search never brackets it,
        and higher-gain horns hide the problem.
        """
        import math
        from hfss_spec import physics
        lam = physics.C0 / 10e9
        h = physics.optimum_pyramidal_horn(15.0, 22.86e-3, 10.16e-3, lam)
        g0 = 10 ** 1.5
        trial = g0 / (2 * math.pi * math.sqrt(2 * math.pi))
        self.assertLess(h["chi"], trial)

    def test_the_horn_spec_needs_no_escape_hatch(self):
        """The Q1c decision, tested: a horn is a first-class spec."""
        spec = load_spec(CASES / "horn-10ghz" / "design.yaml")
        self.assertEqual(spec.escape_hatch_count, 0)
        self.assertTrue(any(op.op == "connect" for op in spec.geometry))
        self.assertTrue(validate(spec).ok)


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
