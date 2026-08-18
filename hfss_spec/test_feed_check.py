"""Tier 0 tests for the feed-network walk. No AEDT, no license, milliseconds.

The regression these guard is not that the algebra works, but that the gate still
catches S7 and still accepts every legitimate feed. A checker that rejected the
200 ohm halving design would be worse than no checker, because it would push
designers toward the one topology it happened to know.
"""

import math
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hfss_spec.loader import load_spec_text        # noqa: E402
from hfss_spec.validate import validate            # noqa: E402
from hfss_spec import physics as P                 # noqa: E402

ER, H, F0 = 3.48, 0.762e-3, 5.8e9
LONG = 10e-3          # a plain line's length does not enter the walk


def width_for(z):
    lo, hi = 0.02e-3, 20e-3
    for _ in range(200):
        mid = (lo + hi) / 2
        if P.microstrip_impedance(mid, H, ER)[0] > z:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def quarter_for(z):
    _, eeff = P.microstrip_impedance(width_for(z), H, ER)
    return P.guide_wavelength(F0, eeff) / 4.0


HEAD = """
spec_version: 1
name: feedprobe
recipe: corporate-patch-array
solution_type: Modal
provenance: {source: "test fixture", canonical_reading: closed-form}
target: {quantity: resonant_frequency, value: 5.8GHz, tolerance_pct: 5}
variables:
  f0: 5.8GHz
  h: 0.762mm
  er: 3.48
materials:
  ro: {permittivity: 3.48, loss_tangent: 0.0037}
  metal: {library: pec}
geometry:
  - op: box
    name: Sub
    material: ro
    origin: ["-40mm", "-40mm", "0mm"]
    size: ["80mm", "80mm", "0.762mm"]
"""

TAIL = """
excitations:
  - name: "1"
    type: lumped_port
    "on": {object: Trunk}
    integration_line:
      from: {point: ["0mm", "0mm", "0mm"]}
      to: {point: ["0mm", "0mm", "0.762mm"]}
    impedance: 50ohm
boundaries: []
setup:
  name: Setup1
  solution_frequency: f0
  sweep: {name: Sweep1, type: interpolating, start: 5.0GHz, stop: 6.5GHz, count: 101}
qa_signals: [convergence, ports_excited]
"""


def spec_with(lines, chain, element_z, include_feed=True):
    """A board carrying `lines` (name -> (Z_ohm, length_m)) plus a feed chain."""
    parts = [HEAD]
    for name, (z, length) in lines.items():
        w = width_for(z)
        parts.append("  - op: sheet\n    name: %s\n    material: metal\n"
                     "    plane: xy\n    origin: [\"0mm\", \"0mm\", \"0.762mm\"]\n"
                     "    size: [\"%.6fmm\", \"%.6fmm\"]\n"
                     % (name, w * 1e3, length * 1e3))
    parts.append(TAIL)
    if include_feed:
        parts.append("feed_network:\n  element_impedance: %s\n  chain:\n" % element_z)
        for stage in chain:
            parts.append("    - {%s}\n" % stage)
    return "".join(parts)


def feed_errors(text):
    report = validate(load_spec_text(text))
    return [f.message for f in report.errors if f.path.startswith("feed_network")]


class TestLegitimateTopologies(unittest.TestCase):
    """All three must pass. This is the whole point of the design."""

    def test_a_fifty_ohm_elements_with_quarter_wave_junction_sections(self):
        x = 50 / math.sqrt(2)
        lines = {"Elem": (50, LONG), "X2": (x, quarter_for(x)),
                 "Arm": (50, LONG), "X1": (x, quarter_for(x)),
                 "Trunk": (50, LONG)}
        chain = ["line: Elem", "junction: 2", "quarter_wave: X2",
                 "line: Arm", "junction: 2", "quarter_wave: X1", "line: Trunk"]
        self.assertEqual(feed_errors(spec_with(lines, chain, "50ohm")), [])

    def test_canonical_fifty_ohm_patches_six_transformers(self):
        """The canonical 50-ohm-patch corporate feed, and the one to compare
        against: 50 trunk -> T -> two 100 ohm branches -> lambda/4 @ 70.71 to 50
        -> T -> four 100 ohm lines -> lambda/4 @ 70.71 to each 50 ohm patch.
        Six transformers, and nothing ever leaves 50 or 100 ohm. 70.71 is
        sqrt(50*100), the classic quarter-wave value, and its line is 0.946 mm
        against the 2.908 mm a 35.36 ohm section needs.
        """
        x = math.sqrt(50 * 100)
        lines = {"XP": (x, quarter_for(x)), "El": (100, LONG),
                 "Br": (50, LONG), "XB": (x, quarter_for(x)),
                 "Bo": (100, LONG), "Trunk": (50, LONG)}
        chain = ["quarter_wave: XP", "line: El", "junction: 2",
                 "line: Br", "quarter_wave: XB", "line: Bo", "junction: 2",
                 "line: Trunk"]
        self.assertEqual(feed_errors(spec_with(lines, chain, "50ohm")), [])

    def test_b_two_hundred_ohm_elements_pure_halving_no_sections(self):
        """The elegant one: 200 is 4x a 50 ohm input, so two parallel
        combinations land on it with no matching sections at all. Written with the
        pair junction at the element edge, so no unmakeable 200 ohm line exists.
        """
        lines = {"Arm": (100, LONG), "Trunk": (50, LONG)}
        chain = ["junction: 2", "line: Arm", "junction: 2", "line: Trunk"]
        self.assertEqual(feed_errors(spec_with(lines, chain, "200ohm")), [])

    def test_c_two_hundred_ohm_elements_stepped_down_by_quarter_wave(self):
        zx = math.sqrt(200 * 100)
        x = 50 / math.sqrt(2)
        lines = {"XE": (zx, quarter_for(zx)), "Elem": (100, LONG),
                 "Arm": (50, LONG), "X1": (x, quarter_for(x)),
                 "Trunk": (50, LONG)}
        chain = ["quarter_wave: XE", "line: Elem", "junction: 2",
                 "line: Arm", "junction: 2", "quarter_wave: X1", "line: Trunk"]
        self.assertEqual(feed_errors(spec_with(lines, chain, "200ohm")), [])


class TestCatchesS7(unittest.TestCase):
    def test_hundred_ohm_lines_into_fifty_ohm_elements_is_caught(self):
        """S7's defect exactly: correct widths, a network built for 100 ohm
        elements, and elements inset-matched to 50."""
        lines = {"Elem": (100, LONG), "Arm": (100, LONG), "Trunk": (50, LONG)}
        chain = ["line: Elem", "junction: 2", "line: Arm",
                 "junction: 2", "line: Trunk"]
        errors = feed_errors(spec_with(lines, chain, "50ohm"))
        self.assertTrue(errors)
        self.assertIn("2.00:1", errors[0])

    def test_the_same_network_closes_if_the_elements_really_are_200(self):
        """The network was never wrong in isolation - it was wrong for its
        elements. That is why the gate checks a relationship, not a shape."""
        lines = {"Arm": (100, LONG), "Trunk": (50, LONG)}
        chain = ["junction: 2", "line: Arm", "junction: 2", "line: Trunk"]
        self.assertEqual(feed_errors(spec_with(lines, chain, "200ohm")), [])

    def test_a_chain_that_misses_the_port_impedance_is_reported(self):
        lines = {"Elem": (100, LONG), "Trunk": (100, LONG)}
        chain = ["line: Elem", "line: Trunk"]
        errors = feed_errors(spec_with(lines, chain, "100ohm"))
        self.assertTrue(any("does not close" in e for e in errors))


class TestHonestLimits(unittest.TestCase):
    def test_an_unmakeable_line_is_refused_not_guessed(self):
        """A 200 ohm line is 0.038 mm on this stack, past Hammerstad's range.
        Reporting a confident number there is the failure this gate exists for."""
        lines = {"Elem": (200, LONG), "Trunk": (50, LONG)}
        chain = ["line: Elem", "junction: 2", "junction: 2", "line: Trunk"]
        errors = feed_errors(spec_with(lines, chain, "200ohm"))
        self.assertTrue(any("Hammerstad" in e for e in errors))

    def test_a_transformer_of_the_wrong_length_is_reported(self):
        x = 50 / math.sqrt(2)
        lines = {"Elem": (50, LONG), "X2": (x, quarter_for(x) * 1.5),
                 "Arm": (50, LONG), "X1": (x, quarter_for(x)),
                 "Trunk": (50, LONG)}
        chain = ["line: Elem", "junction: 2", "quarter_wave: X2",
                 "line: Arm", "junction: 2", "quarter_wave: X1", "line: Trunk"]
        errors = feed_errors(spec_with(lines, chain, "50ohm"))
        self.assertTrue(any("quarter-wave" in e for e in errors))

    def test_a_misspelled_object_is_named_not_ignored(self):
        errors = feed_errors(spec_with({"Trunk": (50, LONG)}, ["line: Trnuk"], "50ohm"))
        self.assertTrue(any("not a geometry object" in e for e in errors))

    def test_no_feed_network_block_means_no_findings(self):
        """Optional by design: every spec written before this must still pass."""
        text = spec_with({"Trunk": (50, LONG)}, ["line: Trunk"], "50ohm",
                         include_feed=False)
        self.assertEqual(feed_errors(text), [])


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print("%s: feed_check tests=%d failed=%d"
          % ("PASS" if not failed else "FAIL", result.testsRun, failed))
    raise SystemExit(1 if failed else 0)
