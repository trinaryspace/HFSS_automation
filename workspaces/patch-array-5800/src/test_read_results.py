"""Tier 0 tests for the readout module. No AEDT, no license, milliseconds.

The bug being locked down: a fill-state check written against `data_real` — an
attribute pyAEDT 1.3.0 does not have — reports "unfilled" on every good fetch,
so a working readout is discarded before anyone sees it. It survived two pilots
because nothing tested it offline. These fakes mimic the accessor surface of
1.3.0 exactly, so the regression cannot come back quietly.

The second bug locked down here is a reasoning failure rather than a call-shape
one, and it cost a whole run's results (patch-array-5800): two `GrpcApiError`s
on generic desktop calls were written up as "scripted readouts fail
systematically over this pairing" although the retry had reconnected to the
same degraded desktop process, and the same run's ledger recorded that
recycling the desktop had already cured that error class once. `ReadoutSession`
must escalate to a genuinely fresh process and must label the three outcomes
apart; a fake recycler stands in for the launch, so the whole decision is
testable with no AEDT.
"""

import os
import shutil
import sys
import tempfile
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


class FakeRecycler:
    """Stands in for `ws_common.recycle_desktop`: returns `(hfss, note)`.

    A recycle is a process launch on the live box; here it is a counter and a
    replacement fake, which is all the escalation logic can observe anyway.
    """

    def __init__(self, replacement, raises=None):
        self.replacement = replacement
        self.raises = raises
        self.calls = 0

    def __call__(self):
        self.calls += 1
        if self.raises:
            raise self.raises
        return self.replacement, "recycled desktop: fresh desktop pinned at port 61234"


def healthy_hfss():
    return FakeHfss(SWEEPS, FakePost(FakeSolution(sweep=FREQS, values=FILLED)))


def sick_hfss():
    """A desktop whose channel raises the run's actual error class."""
    return FakeHfss(SWEEPS, FakePost(raises=RuntimeError(
        "GrpcApiError: GetVariables failed")))


class TestReadoutSessionRoutes(unittest.TestCase):
    """The three outcomes must be distinguishable, because the run that could
    not distinguish them wrote an untested hypothesis into the playbook."""

    def test_live_read_never_escalates(self):
        recycler = FakeRecycler(healthy_hfss())
        session = read_results.ReadoutSession(healthy_hfss(), recycle=recycler)
        out = session.read("dB(S(1,1))")
        self.assertEqual(out.y, FILLED)
        self.assertEqual(out.route, read_results.ROUTE_LIVE)
        self.assertEqual(recycler.calls, 0)
        self.assertFalse(session.escalated)

    def test_fresh_process_success_is_the_confirmed_verdict(self):
        """The hypothesis the 2026-08-18 run assumed false, actually tested."""
        fresh = healthy_hfss()
        recycler = FakeRecycler(fresh)
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        out = session.read("dB(S(1,1))")
        self.assertEqual(out.y, FILLED)
        self.assertEqual(out.route, read_results.ROUTE_FRESH)
        self.assertEqual(recycler.calls, 1)
        self.assertIs(session.hfss, fresh)          # later signals use the fresh one
        self.assertIn("GetVariables", out.note)     # what the live channel did
        self.assertIn("fresh process:", out.note)   # and what the fresh one did
        self.assertIn("CONFIRMED", read_results.verdict_line("s11", out))

    def test_failure_on_both_rules_out_the_channel_without_naming_a_cause(self):
        """Both arms failing narrows the cause; it does not identify one.

        This assertion was inverted on 2026-09-01. It used to require the word
        SYSTEMATIC, which the verdict string duly supplied - and the 2026-08-18
        run's conclusion ("systematic over this pairing") is exactly the
        overclaim that sent it to the wrong answer. Two failures rule out the
        channel's age and nothing more: environment-compat #6 records the same
        call working on the same pairing, and the experiment later traced the
        real cause to pyAEDT releasing its own session mid-read. The verdict
        must now say what was tried and explicitly disclaim the cause.
        """
        recycler = FakeRecycler(sick_hfss())
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        out = session.read("dB(S(1,1))")
        self.assertEqual(out.y, [])
        self.assertEqual(out.route, read_results.ROUTE_BOTH_FAILED)
        self.assertEqual(recycler.calls, 1)
        line = read_results.verdict_line("s11", out)
        self.assertIn("BOTH", line)
        self.assertIn("not the channel's age", line)
        self.assertIn("NOT established by this run alone", line)
        self.assertNotIn("SYSTEMATIC", line)

    def test_no_recycler_is_untested_and_never_reads_as_systematic(self):
        """The defect verbatim: no fresh process ran, so nothing was proved."""
        session = read_results.ReadoutSession(sick_hfss())
        out = session.read("dB(S(1,1))")
        self.assertEqual(out.route, read_results.ROUTE_UNTESTED)
        line = read_results.verdict_line("s11", out)
        self.assertIn("UNTESTED", line)
        self.assertNotIn("SYSTEMATIC", line)

    def test_a_raising_recycle_is_untested_not_systematic(self):
        recycler = FakeRecycler(None, raises=RuntimeError("launch refused"))
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        out = session.read("dB(S(1,1))")
        self.assertEqual(out.route, read_results.ROUTE_UNTESTED)
        self.assertIn("launch refused", out.note)
        self.assertNotIn("SYSTEMATIC", read_results.verdict_line("s11", out))


class TestReadoutSessionBudget(unittest.TestCase):
    """One escalation per run, spent once, never a loop."""

    def test_three_failing_signals_launch_exactly_one_desktop(self):
        recycler = FakeRecycler(sick_hfss())
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        routes = [session.read(e).route for e in ("dB(S(1,1))", "dB(S(2,1))", "GainTotal")]
        self.assertEqual(recycler.calls, 1)
        self.assertEqual(routes, [read_results.ROUTE_BOTH_FAILED] * 3)

    def test_a_failed_escalation_is_still_spent(self):
        recycler = FakeRecycler(None, raises=RuntimeError("launch refused"))
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        session.read("dB(S(1,1))")
        session.read("dB(S(2,1))")
        self.assertEqual(recycler.calls, 1)
        self.assertTrue(session.escalated)

    def test_signals_after_a_FAILED_escalation_stay_untested(self):
        """The budget being spent is not the same fact as a fresh process
        existing. Reporting `both-failed` here would claim a fresh process
        failed when none ever came up — the untested-hypothesis-as-finding
        move this whole class exists to prevent, and it was a live bug in
        the first cut of `read`."""
        recycler = FakeRecycler(None, raises=RuntimeError("launch refused"))
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        session.read("dB(S(1,1))")
        second = session.read("dB(S(2,1))")
        self.assertFalse(session.on_fresh_process)
        self.assertEqual(second.route, read_results.ROUTE_UNTESTED)
        self.assertNotIn("SYSTEMATIC", read_results.verdict_line("s21", second))
        self.assertIn("launch refused", second.note)

    def test_a_live_read_after_a_failed_escalation_is_still_the_live_channel(self):
        """No fresh process came up, so a later success is the live channel's
        — labelling it `fresh-process` would invent a desktop."""
        recycler = FakeRecycler(None, raises=RuntimeError("launch refused"))
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        session.read("dB(S(1,1))")
        session.hfss = healthy_hfss()          # the channel recovered on its own
        out = session.read("dB(S(2,1))")
        self.assertEqual(out.route, read_results.ROUTE_LIVE)

    def test_signals_after_a_successful_escalation_say_which_desktop_read_them(self):
        recycler = FakeRecycler(healthy_hfss())
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        session.read("dB(S(1,1))")
        second = session.read("dB(S(2,1))")
        self.assertEqual(second.route, read_results.ROUTE_FRESH)
        self.assertIn("already spent", second.note)
        self.assertEqual(recycler.calls, 1)


class TestVerdictRecord(unittest.TestCase):
    """What lands in `results/state/readouts.txt` is the evidence a later
    session reasons from, so its shape is part of the contract."""

    def test_every_route_has_a_verdict_and_the_tokens_are_distinct(self):
        routes = (read_results.ROUTE_LIVE, read_results.ROUTE_FRESH,
                  read_results.ROUTE_BOTH_FAILED, read_results.ROUTE_UNTESTED)
        self.assertEqual(len(set(routes)), 4)
        self.assertEqual(set(read_results.VERDICTS), set(routes))
        for route in routes:
            self.assertTrue(len(read_results.VERDICTS[route]) > 20, route)

    def test_line_carries_signal_route_verdict_and_trail(self):
        out = read_results.Readout(FREQS, FILLED, read_results.ROUTE_LIVE, "read 3 points")
        line = read_results.verdict_line("s11", out)
        self.assertTrue(line.startswith("s11: route=live-channel "))
        self.assertIn("| read 3 points", line)

    def test_written_file_is_greppable_by_route(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        recycler = FakeRecycler(healthy_hfss())
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler)
        line = read_results.verdict_line("s11", session.read("dB(S(1,1))"))
        path = read_results.write_readouts(tmp, [line])
        with open(path, encoding="utf-8") as f:
            written = f.read()
        self.assertIn("route=" + read_results.ROUTE_FRESH, written)
        self.assertTrue(written.endswith("\n"))


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
