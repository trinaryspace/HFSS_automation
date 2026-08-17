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
