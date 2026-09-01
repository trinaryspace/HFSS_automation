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

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from hfss_spec import model_checks                   # noqa: E402
from hfss_spec.loader import load_spec, load_spec_text   # noqa: E402
from hfss_spec.validate import validate              # noqa: E402

C0 = 299792458.0
LAMBDA_2G4 = C0 / 2.4e9


TARGET_2G4 = "{quantity: resonant_frequency, value: 2.4GHz, tolerance_pct: 5}"


def spec_text(air_pad_mm, port_w_mm=1.0, wire_d_mm=1.0, gap_mm=2.0,
              target=TARGET_2G4, solution_frequency="f0"):
    """A dipole with a radiation box, parameterised on the things tested.

    `target` and `solution_frequency` are here because the clearance check has to
    find a frequency before it can measure anything, and the two ways it can find
    one need to be varied independently. Pass `target=None` to omit the key —
    `DesignSpec.target` is Optional, so a spec with no headline goal is a shape
    the schema really admits.
    """
    target_line = "" if target is None else f"target: {target}\n"
    return f"""
spec_version: 1
name: probe
recipe: half-wave-dipole
solution_type: Modal
provenance:
  source: "test fixture for hfss_spec/test_model_checks.py"
  canonical_reading: closed-form
{target_line}variables:
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
  solution_frequency: {solution_frequency}
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


class TestTargetFrequency(unittest.TestCase):
    """The clearance check measures nothing until it has a frequency.

    Until 2026-08-31 it usually did not have one. `_target_frequency` read
    `setup.frequency`, and `Setup`'s field is `solution_frequency` — a name that
    `extra="forbid"` guarantees no spec ever carried. So every spec whose target
    is not itself a frequency resolved None and `radiation_clearance` returned
    `[]` before looking at a single face. That is worse than a wrong answer: the
    report was clean because nothing ran, and `horn-10ghz`, `S3` and
    `microstrip-50r` went unmeasured for as long as the typo lived.

    These tests are written against the resolution step rather than the geometry,
    because the geometry was never the part that was broken.
    """

    def test_the_setup_carries_the_frequency_when_the_target_is_not_one(self):
        """The regression. A TEM line's target is an impedance, not a frequency,
        so the setup is the only place the frequency can come from."""
        found = clearance_warnings(
            air_pad_mm=12.0,
            target="{quantity: characteristic_impedance, value: 50ohm, "
                   "tolerance_pct: 5}")
        self.assertTrue(
            found,
            "a non-frequency target must fall back to setup.solution_frequency")
        self.assertIn("41.64 mm at 2.4 GHz", found[0])

    def test_the_fallback_reads_the_field_the_schema_actually_defines(self):
        """Named rather than implied: the whole defect was one wrong field name,
        and a test that only exercises the behaviour would not say which name."""
        from hfss_spec.schema import Setup
        self.assertIn("solution_frequency", Setup.model_fields)
        self.assertNotIn("frequency", Setup.model_fields)
        self.assertEqual(Setup.model_config.get("extra"), "forbid")

    def test_cutoff_frequency_is_not_a_quantity_the_schema_offers(self):
        """The other dead branch. It was matched against `Target.quantity` and is
        not one of its members, so it could never fire. If the schema ever grows
        it, this fails and the literal list here is due a revisit."""
        from hfss_spec.schema import Target
        import typing
        self.assertNotIn("cutoff_frequency",
                         typing.get_args(Target.model_fields["quantity"].annotation))

    def test_a_frequency_target_still_wins_over_the_setup(self):
        """A design solved at 6 GHz but targeted at 2.4 GHz is judged at 2.4 —
        the clearance is a near-field property of the design frequency, and the
        target is where the author stated it. Repairing the fallback must not
        quietly promote the setup over the target."""
        found = clearance_warnings(air_pad_mm=20.0, solution_frequency="6GHz")
        self.assertTrue(found)
        self.assertIn("41.64 mm at 2.4 GHz", found[0])
        self.assertNotIn("6 GHz", found[0])

    def test_no_resolvable_frequency_degrades_quietly(self):
        """Neither source resolves — no target, and a setup frequency naming a
        variable that does not exist. The check must return nothing rather than
        raise: an unreadable spec is `validate`'s problem to report, and a
        relational check that throws takes the whole report down with it."""
        text = spec_text(air_pad_mm=1.0, target=None,
                         solution_frequency="f_typo")
        spec = load_spec_text(text)
        self.assertIsNone(model_checks._target_frequency(spec))
        report = validate(spec)                        # must not raise
        self.assertEqual(
            [f.message for f in report.warnings if "radiation boundary" in f.message],
            [])

    def test_the_real_case_the_dead_fallback_was_hiding(self):
        """`microstrip-50r` is a spec in this repo, not a fixture: target
        `characteristic_impedance`, so it was unchecked, and it is under-padded.
        The warning is expected and wanted — whether a lambda0/3 radiation rule
        belongs on a non-radiating TEM line is a separate decision the maintainer
        is taking with the warning visible, not by suppressing it here."""
        path = os.path.join(REPO, "knowledge", "cases", "microstrip-50r",
                            "design.yaml")
        report = validate(load_spec(path))
        found = [f.message for f in report.warnings
                 if "radiation boundary" in f.message]
        self.assertTrue(found, "microstrip-50r must now be measured")
        self.assertIn("12.00 mm on +z", found[0])
        self.assertIn("41.64 mm at 2.4 GHz", found[0])
        self.assertEqual(report.errors, [])


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
