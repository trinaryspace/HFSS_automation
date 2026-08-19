"""Tier 0 tests for the relational checks. No AEDT, no license, milliseconds.

These lock down two rules written against real defects, so the tests are stated
in terms of those defects rather than in the abstract. The regression they guard
is not "the code runs" — it is "the check still fires on the spec it was written
for, and still stays quiet on the five the maintainer passed."

Each check also has a false-positive test, because a warning that cries wolf on a
correct design gets ignored, and an ignored gate is the failure mode cell S11
demonstrated.
"""

import math
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hfss_spec.loader import load_spec_text          # noqa: E402
from hfss_spec.validate import validate              # noqa: E402

C0 = 299792458.0
LAMBDA_2G4 = C0 / 2.4e9


def spec_text(air_pad_mm, port_w_mm=1.0, wire_d_mm=1.0, gap_mm=2.0):
    """A dipole with a radiation box, parameterised on the two things tested."""
    return f"""
spec_version: 1
name: probe
recipe: half-wave-dipole
solution_type: Modal
provenance:
  source: "test fixture for hfss_spec/test_model_checks.py"
  canonical_reading: closed-form
target: {{quantity: resonant_frequency, value: 2.4GHz, tolerance_pct: 5}}
variables:
  f0: 2.4GHz
  L_arm: 28mm
  Gap: {gap_mm}mm
  WireD: {wire_d_mm}mm
  PortW: {port_w_mm}mm
  Pad: {air_pad_mm}mm
materials:
  metal: {{library: pec}}
  air: {{library: air}}
geometry:
  - op: cylinder
    name: ArmLo
    material: metal
    origin: ["0mm", "0mm", "-L_arm - Gap/2"]
    radius: WireD/2
    height: L_arm
    axis: z
  - op: cylinder
    name: ArmHi
    material: metal
    origin: ["0mm", "0mm", "Gap/2"]
    radius: WireD/2
    height: L_arm
    axis: z
  - op: sheet
    name: PortSheet
    plane: xz
    origin: ["-PortW/2", "0mm", "-Gap/2"]
    size: [PortW, Gap]
  - op: box
    name: AirBox
    material: air
    origin: ["-WireD/2 - Pad", "-WireD/2 - Pad", "-L_arm - Gap/2 - Pad"]
    size: ["WireD + 2*Pad", "WireD + 2*Pad", "2*L_arm + Gap + 2*Pad"]
excitations:
  - name: "1"
    type: lumped_port
    "on": {{object: PortSheet}}
    integration_line:
      from: {{point: ["0mm", "0mm", "-Gap/2"]}}
      to: {{point: ["0mm", "0mm", "Gap/2"]}}
    impedance: 50ohm
boundaries:
  - name: Rad
    type: radiation
    "on": {{outer_faces: AirBox}}
setup:
  name: Setup1
  solution_frequency: f0
  sweep: {{name: Sweep1, type: interpolating, start: 2.0GHz, stop: 3.0GHz, count: 101}}
qa_signals: [convergence, ports_excited, in_band_resonance]
"""


def warnings_for(**kwargs):
    report = validate(load_spec_text(spec_text(**kwargs)))
    return [f.message for f in report.warnings]


def clearance_warnings(**kwargs):
    return [m for m in warnings_for(**kwargs) if "radiation boundary" in m]


def port_warnings(**kwargs):
    return [m for m in warnings_for(**kwargs) if "lumped port sheet" in m]


class TestRadiationClearance(unittest.TestCase):
    def test_lambda_over_ten_is_flagged(self):
        """X0a's defect: 15 mm side pad at 2.4 GHz, where lambda0/3 is 41.6."""
        found = clearance_warnings(air_pad_mm=15.0)
        self.assertTrue(found, "a lambda0/8 pad must be flagged")
        self.assertIn("lambda0/3", found[0])

    def test_lambda_over_four_is_flagged(self):
        """The commonly-copied value. Four of six reviewed specs chose it."""
        self.assertTrue(clearance_warnings(air_pad_mm=LAMBDA_2G4 * 1e3 / 4))

    def test_exactly_lambda_over_three_is_clean(self):
        """A spec written as c0/(3*f0) lands here; a strict `<` would misfire."""
        self.assertEqual(clearance_warnings(air_pad_mm=LAMBDA_2G4 * 1e3 / 3), [])

    def test_generous_pad_is_clean(self):
        self.assertEqual(clearance_warnings(air_pad_mm=60.0), [])

    def test_the_message_carries_numbers_a_human_can_act_on(self):
        message = clearance_warnings(air_pad_mm=15.0)[0]
        for token in ("mm", "lambda0/3", "GHz"):
            self.assertIn(token, message)


class TestPortGeometry(unittest.TestCase):
    def test_four_times_the_conductor_is_flagged(self):
        """S4's defect verbatim: a 4 mm ribbon on a 1 mm wire."""
        found = port_warnings(air_pad_mm=60.0, port_w_mm=4.0, wire_d_mm=1.0)
        self.assertTrue(found)
        self.assertIn("4.0x", found[0])

    def test_matching_the_conductor_is_clean(self):
        self.assertEqual(
            port_warnings(air_pad_mm=60.0, port_w_mm=1.0, wire_d_mm=1.0), [])

    def test_a_gap_wider_than_the_wire_is_not_a_width(self):
        """The port must span the gap along the current; that extent is not a
        width. Judging the largest extent flagged a correctly-sized port."""
        self.assertEqual(
            port_warnings(air_pad_mm=60.0, port_w_mm=1.0, wire_d_mm=1.0,
                          gap_mm=6.0), [])

    def test_modest_flare_is_tolerated(self):
        self.assertEqual(
            port_warnings(air_pad_mm=60.0, port_w_mm=1.4, wire_d_mm=1.0), [])


class TestFlushFaces(unittest.TestCase):
    """A flush boundary face is only legitimate under a wave port.

    Caught at a Review gate 2026-08-17: a four-lumped-port array was built with
    its -y face flush, copied from a wave-port design. Every automated gate
    passed it - including this one, which excused any flush face on the
    assumption a wave port explained it, and never checked.
    """

    def test_a_flush_face_on_a_lumped_port_design_is_flagged(self):
        # The dipole fixture uses a lumped port; pull the airbox flush in -x by
        # placing it exactly on the wire surface.
        text = spec_text(air_pad_mm=60.0).replace(
            'origin: ["-WireD/2 - Pad", "-WireD/2 - Pad", "-L_arm - Gap/2 - Pad"]',
            'origin: ["-WireD/2", "-WireD/2 - Pad", "-L_arm - Gap/2 - Pad"]')
        report = validate(load_spec_text(text))
        flagged = [f.message for f in report.warnings
                   if "radiation boundary" in f.message]
        self.assertTrue(flagged, "a lumped-port design gets no flush-face pass")

    def test_the_rule_is_about_the_port_type_not_the_geometry(self):
        """Same geometry, wave port instead: flush is then legitimate."""
        text = spec_text(air_pad_mm=60.0).replace(
            'origin: ["-WireD/2 - Pad", "-WireD/2 - Pad", "-L_arm - Gap/2 - Pad"]',
            'origin: ["-WireD/2", "-WireD/2 - Pad", "-L_arm - Gap/2 - Pad"]')
        text = text.replace("type: lumped_port", "type: wave_port")
        report = validate(load_spec_text(text))
        flagged = [f.message for f in report.warnings
                   if "radiation boundary" in f.message]
        self.assertEqual(flagged, [])


def array_text(offset_mm, notch_all=True):
    """A two-element strip array whose second transformer can be nudged off.

    `offset_mm` is the sliver between `Xfmr` and `Arm`: 0 means they touch,
    0.58285 reproduces the exact open circuit shipped on 2026-08-18.
    `notch_all` cuts a notch from both patches or from only the first, which
    reproduces the missing-notches defect from the same run.
    """
    second_cut = ("""
  - op: subtract
    name: P2
    tools: [N2]
""" if notch_all else "")
    return f"""
spec_version: 1
name: array-probe
recipe: inset-fed-rectangular-patch
solution_type: Modal
provenance:
  source: "test fixture for hfss_spec/test_model_checks.py"
  canonical_reading: closed-form
target: {{quantity: resonant_frequency, value: 5.8GHz, tolerance_pct: 5}}
variables:
  f0: 5.8GHz
  Off: {offset_mm}mm
materials:
  metal: {{library: pec}}
  sub: {{permittivity: 3.48}}
  air: {{library: air}}
geometry:
  - op: box
    name: Substrate
    material: sub
    origin: ["-40mm", "-30mm", "0mm"]
    size: ["80mm", "60mm", "0.762mm"]
  - op: sheet
    name: Ground
    material: metal
    plane: xy
    origin: ["-40mm", "-30mm", "0mm"]
    size: ["80mm", "60mm"]
  # The feed chain: InLine -> Xfmr -> Bus -> {{P1, P2}}. `Off` is the sliver
  # between InLine and Xfmr, and it is the only joint that can be broken.
  - op: sheet
    name: Arm
    material: metal
    plane: xy
    origin: ["-20mm", "-1mm", "0.762mm"]
    size: ["10mm", "2mm"]
  - op: sheet
    name: Xfmr
    material: metal
    plane: xy
    origin: ["-10mm + Off", "-1.5mm", "0.762mm"]
    size: ["8mm", "3mm"]
  - op: sheet
    name: Bus
    material: metal
    plane: xy
    origin: ["-2mm + Off", "-14mm", "0.762mm"]
    size: ["2mm", "28mm"]
  - op: sheet
    name: P1
    material: metal
    plane: xy
    origin: ["0mm + Off", "-1mm", "0.762mm"]
    size: ["17mm", "14mm"]
  - op: sheet
    name: P2
    material: metal
    plane: xy
    origin: ["0mm + Off", "-15mm", "0.762mm"]
    size: ["17mm", "14mm"]
  - op: sheet
    name: N1
    plane: xy
    origin: ["5mm + Off", "0mm", "0.762mm"]
    size: ["1mm", "2mm"]
  - op: sheet
    name: N2
    plane: xy
    origin: ["5mm + Off", "-14mm", "0.762mm"]
    size: ["1mm", "2mm"]
  - op: subtract
    name: P1
    tools: [N1]{second_cut}
  # A DEDICATED port sheet. The port must not sit on `Arm` itself: an object
  # named by `{{object: ...}}` is treated as an excitation surface and excluded
  # from the conductor graph, which would hide the very break under test.
  - op: sheet
    name: PortSheet
    plane: yz
    origin: ["-20mm", "-1mm", "0mm"]
    size: ["2mm", "0.762mm"]
  - op: box
    name: AirBox
    material: air
    origin: ["-60mm", "-50mm", "-20mm"]
    size: ["120mm", "100mm", "40mm"]
excitations:
  - name: "1"
    type: lumped_port
    impedance: 50ohm
    "on": {{object: PortSheet}}
    integration_line:
      from: {{point: ["-20mm", "0mm", "0mm"]}}
      to: {{point: ["-20mm", "0mm", "0.762mm"]}}
boundaries:
  - name: Rad
    type: radiation
    "on": {{outer_faces: AirBox}}
setup:
  name: Setup1
  solution_frequency: f0
  sweep: {{name: Sweep1, type: interpolating, start: 5.0GHz, stop: 6.6GHz, count: 101}}
qa_signals: [convergence]
"""


def array_warnings(**kwargs):
    findings = validate(load_spec_text(array_text(**kwargs))).findings
    return [f for f in findings if f.path == "geometry"]


class TestConductorConnectivity(unittest.TestCase):
    """R1 — the check that would have caught the defect this tool shipped."""

    def test_the_shipped_open_circuit_is_caught(self):
        found = [f for f in array_warnings(offset_mm=0.58285)
                 if "not connected" in f.message]
        self.assertTrue(found, "the 0.58285 mm open circuit was not reported")
        self.assertIn("0.58285", found[0].message)

    def test_touching_metal_is_clean(self):
        found = [f for f in array_warnings(offset_mm=0.0)
                 if "not connected" in f.message]
        self.assertEqual(found, [], [f.message for f in found])

    def test_the_ground_plane_is_never_an_island(self):
        """A microstrip ground is separate on purpose, on every planar design.

        Before layering, this fired on every correct spec in the repo, which is
        the way to make a check ignored.
        """
        for offset in (0.0, 0.58285):
            found = [f for f in array_warnings(offset_mm=offset)
                     if "Ground" in f.message]
            self.assertEqual(found, [], "ground plane reported as disconnected")

    def test_the_gap_is_in_the_message(self):
        """The number is what separates a bug from a deliberate coupling gap."""
        found = [f for f in array_warnings(offset_mm=0.58285)
                 if "not connected" in f.message]
        self.assertRegex(found[0].message, r"closest approach [\d.]+ mm")

    def test_it_is_a_warning_not_an_error(self):
        result = validate(load_spec_text(array_text(offset_mm=0.58285)))
        self.assertTrue(result.ok, "connectivity must not block a build")


class TestElementSymmetry(unittest.TestCase):
    """R2 — notches missing from three patches of four, caught by eye."""

    def test_uneven_cuts_across_identical_elements_are_caught(self):
        found = [f for f in array_warnings(offset_mm=0.0, notch_all=False)
                 if "boolean operations" in f.message]
        self.assertTrue(found, "uneven notching was not reported")
        self.assertIn("P1=1", found[0].message)
        self.assertIn("P2=0", found[0].message)

    def test_evenly_built_elements_are_clean(self):
        found = [f for f in array_warnings(offset_mm=0.0, notch_all=True)
                 if "boolean operations" in f.message]
        self.assertEqual(found, [], [f.message for f in found])

    def test_differently_sized_objects_are_not_compared(self):
        """Grouping is by extent: the substrate and a patch are not siblings."""
        found = [f for f in array_warnings(offset_mm=0.0, notch_all=True)
                 if "identically sized" in f.message]
        self.assertEqual(found, [])


class TestCanonicalCasesStayQuiet(unittest.TestCase):
    """The false-positive guard that matters most: the shipped cases.

    Both new checks warn rather than block, but a warning on a correct design
    still costs attention and teaches people to skim. These four specs are the
    repo's own reference models, one of which has been built and solved.
    """

    def test_no_new_geometry_warnings_on_the_canonical_specs(self):
        import pathlib
        cases = (pathlib.Path(__file__).resolve().parent.parent
                 / "knowledge" / "cases")
        checked = 0
        for design in sorted(cases.glob("*/design.yaml")):
            findings = validate(load_spec_text(design.read_text(
                encoding="utf-8"))).findings
            noisy = [f.message for f in findings
                     if f.path == "geometry"
                     and ("not connected" in f.message
                          or "boolean operations" in f.message)]
            self.assertEqual(noisy, [], f"{design.parent.name}: {noisy}")
            checked += 1
        self.assertGreaterEqual(checked, 4)


class TestSeverity(unittest.TestCase):
    def test_both_are_warnings_never_errors(self):
        """A heuristic must not block a design. Blocking a correct model on a
        rule of thumb is worse than missing a defect."""
        report = validate(load_spec_text(
            spec_text(air_pad_mm=15.0, port_w_mm=4.0)))
        self.assertEqual(report.errors, [])
        self.assertTrue(report.ok)
        self.assertGreaterEqual(len(report.warnings), 2)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: model_checks "
          f"tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
