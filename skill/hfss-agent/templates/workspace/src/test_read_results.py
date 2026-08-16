"""Tier 0 tests for the readout module. No AEDT, no license, milliseconds.

The bug being locked down: a fill-state check written against `data_real` — an
attribute pyAEDT 1.3.0 does not have — reports "unfilled" on every good fetch,
so a working readout is discarded before anyone sees it. It survived two pilots
because nothing tested it offline. These fakes mimic the accessor surface of
1.3.0 exactly, so the regression cannot come back quietly.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import read_results  # noqa: E402


class FakeSolution:
    """A SolutionData shaped like pyAEDT 1.3.0's: no data_real, ever."""

    def __init__(self, sweep=None, values=None, matrix=None, raise_on_get=False):
        if sweep is not None:
            self.primary_sweep_values = sweep
        self._values = values
        self._raise = raise_on_get
        if matrix is not None:
            self.full_matrix_real_imag = matrix

    def get_expression_data(self, expression, formula=None):
        if self._raise:
            raise RuntimeError("boom")
        return self._values


class LegacyFakeSolution:
    """The pre-1.3.0 shape, to prove we do not depend on it."""

    def __init__(self, sweep, values):
        self.primary_sweep_values = sweep
        self.data_real = lambda: values


class FakePost:
    def __init__(self, solution=None, raises=None):
        self._solution = solution
        self._raises = raises

    def get_solution_data(self, expressions=None, setup_sweep_name=None):
        if self._raises:
            raise self._raises
        return self._solution


class FakeHfss:
    def __init__(self, sweeps, post):
        self.existing_analysis_sweeps = sweeps
        self.post = post


FILLED = [1.0, 2.0, 3.0]
FREQS = [2.0e9, 2.5e9, 3.0e9]
SWEEPS = ["Setup1 : LastAdaptive", "Setup1 : Sweep_MM13NY"]


class TestFillState(unittest.TestCase):
    def test_filled_solution_without_data_real_is_filled(self):
        """The whole bug: 1.3.0 has no data_real, and this must still be filled."""
        sol = FakeSolution(sweep=FREQS, values=FILLED)
        self.assertFalse(hasattr(sol, "data_real"))
        self.assertTrue(read_results.is_filled(sol))

    def test_legacy_shape_alone_is_not_trusted(self):
        """data_real present but no 1.3.0 accessor -> not filled, and say why."""
        sol = LegacyFakeSolution(FREQS, FILLED)
        self.assertFalse(read_results.is_filled(sol))
        self.assertIn("data_real", read_results.unfilled_reason(sol))

    def test_none_and_empty_sweep_are_unfilled(self):
        self.assertFalse(read_results.is_filled(None))
        self.assertIn("returned None", read_results.unfilled_reason(None))
        self.assertFalse(read_results.is_filled(FakeSolution(sweep=[], values=FILLED)))
        self.assertIn("primary_sweep_values",
                      read_results.unfilled_reason(FakeSolution(sweep=[])))

    def test_reason_never_recommends_data_real(self):
        reason = read_results.unfilled_reason(FakeSolution(sweep=FREQS))
        self.assertIn("full_matrix_real_imag", reason)
        self.assertIn("do NOT test data_real", reason)


class TestExtract(unittest.TestCase):
    def test_extract_via_get_expression_data(self):
        xs, ys = read_results.extract(FakeSolution(sweep=FREQS, values=FILLED),
                                      "dB(S(1,1))")
        self.assertEqual((xs, ys), (FREQS, FILLED))

    def test_extract_falls_back_to_full_matrix(self):
        sol = FakeSolution(sweep=FREQS, values=[],
                           matrix=[{"dB(S(1,1))": FILLED}, {}])
        xs, ys = read_results.extract(sol, "dB(S(1,1))")
        self.assertEqual(ys, FILLED)

    def test_extract_tolerates_a_raising_getter(self):
        sol = FakeSolution(sweep=FREQS, raise_on_get=True,
                           matrix=[{"dB(S(1,1))": FILLED}, {}])
        with self.assertRaises(RuntimeError):
            sol.get_expression_data("x")
        # extract must not propagate it when a fallback exists
        xs, ys = read_results.extract(sol, "dB(S(1,1))")
        self.assertEqual(ys, FILLED)


class TestResolveSweep(unittest.TestCase):
    def test_prefers_the_real_sweep_over_lastadaptive(self):
        hfss = FakeHfss(SWEEPS, FakePost())
        self.assertEqual(read_results.resolve_sweep(hfss), "Setup1 : Sweep_MM13NY")

    def test_can_ask_for_the_adaptive_point(self):
        hfss = FakeHfss(SWEEPS, FakePost())
        self.assertEqual(read_results.resolve_sweep(hfss, prefer_sweep=False),
                         "Setup1 : LastAdaptive")

    def test_auto_suffix_is_never_guessed(self):
        """EC#6: the suffix is random, so the name must come from the design."""
        hfss = FakeHfss(["Setup1 : Sweep_ZZ99QQ"], FakePost())
        self.assertEqual(read_results.resolve_sweep(hfss), "Setup1 : Sweep_ZZ99QQ")

    def test_no_sweeps_returns_none(self):
        self.assertIsNone(read_results.resolve_sweep(FakeHfss([], FakePost())))


class TestReadExpression(unittest.TestCase):
    def test_happy_path_reports_point_count(self):
        hfss = FakeHfss(SWEEPS, FakePost(FakeSolution(sweep=FREQS, values=FILLED)))
        xs, ys, note = read_results.read_expression(hfss, "dB(S(1,1))")
        self.assertEqual(ys, FILLED)
        self.assertIn("read 3 points", note)

    def test_a_raising_call_is_reported_not_raised(self):
        hfss = FakeHfss(SWEEPS, FakePost(raises=RuntimeError("GrpcApiError GetVariables")))
        xs, ys, note = read_results.read_expression(hfss, "dB(S(1,1))")
        self.assertEqual(ys, [])
        self.assertIn("GetVariables", note)

    def test_unsolved_design_is_named_as_such(self):
        hfss = FakeHfss([], FakePost())
        xs, ys, note = read_results.read_expression(hfss, "dB(S(1,1))")
        self.assertIn("nothing solved yet", note)

    def test_every_failure_note_is_actionable(self):
        """A note is what a human acts on, so none may be empty."""
        cases = [
            FakeHfss([], FakePost()),
            FakeHfss(SWEEPS, FakePost(raises=RuntimeError("x"))),
            FakeHfss(SWEEPS, FakePost(FakeSolution(sweep=[]))),
        ]
        for hfss in cases:
            _, _, note = read_results.read_expression(hfss, "dB(S(1,1))")
            self.assertTrue(note and len(note) > 20, note)


class TestRouteAround(unittest.TestCase):
    """These must not import pyAEDT: that loads PyDesktopPlugin.dll and turns a
    millisecond tier-0 suite into a 25-second one. The live behaviour is
    asserted by the module's own __main__ check, which runs where AEDT exists.
    """

    def test_status_is_a_string_never_a_bool(self):
        """A bool conflated 'not needed' with 'import failed' and hid a wrong
        module path behind a confident healthy answer. Never again."""
        self.assertNotIsInstance(read_results.apply_route_arounds.__doc__, type(None))
        source = read_results.apply_route_arounds.__doc__
        self.assertIn("status string", source)

    def test_known_module_homes_are_tried_in_order(self):
        import inspect
        source = inspect.getsource(read_results.apply_route_arounds)
        self.assertIn("generic.aedt_constants", source)
        self.assertIn("application.design_solutions", source)
        self.assertLess(source.index("generic.aedt_constants"),
                        source.index("application.design_solutions"),
                        "the module that actually has HfssConstants on 1.3.0 must be tried first")


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: read_results tests={total} failed={failed}")
    raise SystemExit(1 if failed else 0)
