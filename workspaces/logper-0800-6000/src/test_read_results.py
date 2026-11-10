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
    def __init__(self, sweeps, post, odesign=None):
        self.existing_analysis_sweeps = sweeps
        self.post = post
        # Attached only when given, so the default fake has NO `odesign` at
        # all — which is what a design the report route cannot reach looks
        # like, and the AttributeError it raises is a real failure mode.
        if odesign is not None:
            self.odesign = odesign


# Distinguishes "the fake was not told what to return" from "the fake was
# told to return None", which is a real distinction here: a
# pyaedt_function_handler-wrapped export returns False, not None.
_UNSET = object()

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
        """The enumeration is written out longhand on purpose: a route added to
        VERDICTS without a deliberate decision about its wording fails here.

        Grew from four tokens to six on 2026-09-01, when the report-export
        route was added. The assertions are unchanged — every token distinct,
        every token carries a verdict, no verdict is a stub — only the list of
        tokens they are applied to."""
        routes = (read_results.ROUTE_LIVE, read_results.ROUTE_FRESH,
                  read_results.ROUTE_EXPORT, read_results.ROUTE_EXPORT_FRESH,
                  read_results.ROUTE_BOTH_FAILED, read_results.ROUTE_UNTESTED)
        self.assertEqual(len(set(routes)), 6)
        self.assertEqual(set(read_results.VERDICTS), set(routes))
        for route in routes:
            self.assertTrue(len(read_results.VERDICTS[route]) > 20, route)

    def test_every_mechanism_and_process_pair_maps_to_a_route(self):
        """A read that produced numbers must always have a token: a missing
        pair would be a KeyError in `ReadoutSession.read` at the exact moment
        a run finally had its results."""
        for mechanism in (read_results.MECH_API, read_results.MECH_EXPORT):
            for fresh in (False, True):
                route = read_results.ROUTE_BY_MECHANISM[(mechanism, fresh)]
                self.assertIn(route, read_results.VERDICTS)
        self.assertEqual(len(set(read_results.ROUTE_BY_MECHANISM.values())), 4)

    def test_a_verdict_names_the_route_that_produced_the_numbers(self):
        """The point of splitting the tokens: a reader must not have to guess
        whether a number came out of the API or out of an exported CSV."""
        for route in (read_results.ROUTE_LIVE, read_results.ROUTE_FRESH):
            self.assertIn("get_solution_data", read_results.VERDICTS[route])
        for route in (read_results.ROUTE_EXPORT, read_results.ROUTE_EXPORT_FRESH):
            self.assertIn("export", read_results.VERDICTS[route])
        for route in (read_results.ROUTE_FRESH, read_results.ROUTE_EXPORT_FRESH):
            self.assertIn("fresh", read_results.VERDICTS[route])

    def test_no_verdict_claims_a_cause_it_cannot_support(self):
        """The module was corrected once for saying 'SYSTEMATIC on this
        pairing' on evidence that could not carry it (env-compat #6 records the
        same call working on the same pairing). No verdict may say it again.

        The ban is on the word, not on the subject: ROUTE_UNTESTED's verdict
        does mention the pairing, and should - it names the pairing as the
        question still OPEN, which is the opposite of a claim about it."""
        for route, verdict in read_results.VERDICTS.items():
            self.assertNotIn("SYSTEMATIC", verdict, route)
            self.assertNotIn("systematic", verdict, route)
        self.assertIn("nothing here says", read_results.VERDICTS[read_results.ROUTE_UNTESTED])

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
        """Unchanged assertion, moved target: the alias body was extracted into
        `_alias_default_solution` on 2026-09-01 when `apply_route_arounds`
        became two route-arounds rather than one. Same claim, same order."""
        import inspect
        source = inspect.getsource(read_results._alias_default_solution)
        self.assertIn("generic.aedt_constants", source)
        self.assertIn("application.design_solutions", source)
        self.assertLess(source.index("generic.aedt_constants"),
                        source.index("application.design_solutions"),
                        "the module that actually has HfssConstants on 1.3.0 must be tried first")

    def test_settings_homes_are_tried_in_order(self):
        """Same claim for the second route-around: 1.3.0's home first."""
        import inspect
        source = inspect.getsource(read_results._disable_release_on_exception)
        self.assertIn("ansys.aedt.core.generic.settings", source)
        self.assertIn("pyaedt", source)
        self.assertLess(source.index("ansys.aedt.core.generic.settings"),
                        source.index('"pyaedt"'),
                        "the module that actually has settings on 1.3.0 must be tried first")


# ---------------------------------------------------------------------------
# The report-export route.
#
# FIXTURE PROVENANCE (docs/agents/fixture-fidelity.md: no fixture from memory).
# The two blobs below are verbatim lines out of CSVs that this route exported
# on this box on 2026-09-01 — the run that produced the first scripted S11 this
# project has ever yielded:
#
#   workspaces/patch-array-5800/results/s11_fed_2026-09-01.csv
#       3623 bytes, CRLF, 1 header + 151 data rows, 5.00-6.50 GHz in 0.01 GHz
#       steps. Minimum -7.36862380345162 dB at 5.66 GHz, which independently
#       reproduced the maintainer's UI read of the same solve.
#   workspaces/patch-array-5800/results/gain_pattern_5p66GHz_2026-09-01.csv
#       CRLF, 1 header + 181 data rows. Freq and Phi are constant down the
#       whole file; Theta runs -180..180 in 2 deg steps. FOUR columns — the
#       shape a two-column parser reads Phi from and reports as gain.
#
# These are real lines lifted from those files — the header row, the first data
# rows, the extreme row, the last row — not a re-typed shape. The CRLF endings,
# the quoted header cells and the full float precision are the artifacts' own,
# and CRLF in particular is load-bearing: a parser that splits on "\n" carries
# a stray "\r" into the last field of every row. Row parsing is independent of
# row count, so a slice exercises the parser exactly as the whole file does.
# ---------------------------------------------------------------------------

REAL_S11_CSV = (b'"Freq [GHz]","dB(S(1,1)) []"\r\n'
                b'5,-0.971789418833437\r\n'
                b'5.01,-0.99572380927031\r\n'
                b'5.02,-1.02038237259029\r\n'
                b'5.66,-7.36862380345162\r\n'
                b'6.5,-1.00875846279887\r\n')

REAL_FARFIELD_CSV = (b'"Freq [GHz]","Phi [deg]","Theta [deg]","dB(GainTotal) []"\r\n'
                     b'5.66,0,-180,-17.060163588662\r\n'
                     b'5.66,0,-178,-17.3918938333137\r\n'
                     b'5.66,0,-176,-17.7292431059142\r\n'
                     b'5.66,0,180,-17.060163588662\r\n')


class FakeReportModule:
    """`odesign.GetModule("ReportSetup")` — the calls the export route makes.

    It counts them, because "was the report module touched at all?" is the
    question that pins the route ORDER: a run whose API read succeeded must
    not have created anything in the user's project.
    """

    def __init__(self, existing=(), create_raises=None, list_raises=None):
        self.existing = list(existing)
        self.created = []
        self.deleted = []
        self.listed = 0
        self.create_raises = create_raises
        self.list_raises = list_raises

    def GetAllReportNames(self):
        self.listed += 1
        if self.list_raises:
            raise self.list_raises
        return list(self.existing)

    def CreateReport(self, name, category, display, setup_sweep, context, families,
                     components, extra):
        if self.create_raises:
            raise self.create_raises
        self.created.append({"name": name, "category": category, "display": display,
                             "sweep": setup_sweep, "context": context,
                             "families": families, "components": components})
        self.existing.append(name)

    def DeleteReports(self, names):        # never called by this module, asserted below
        self.deleted.extend(names)


class FakeDesign:
    def __init__(self, module, get_module_raises=None):
        self._module = module
        self._raises = get_module_raises

    def GetModule(self, name):
        if self._raises:
            raise self._raises
        assert name == "ReportSetup", name
        return self._module


class FakeExportPost(FakePost):
    """A post object that writes what a real export writes, where it writes it.

    pyAEDT 1.3.0 builds the path as `<out_dir>/<plot_name>.csv` and returns it
    (visualization/post/common.py:1111), so the fake does the same. `returns`
    forces the `False` a `pyaedt_function_handler`-wrapped call gives back when
    the error handler swallows an exception.
    """

    def __init__(self, solution=None, raises=None, payload=None, returns=_UNSET,
                 export_raises=None, write=True):
        FakePost.__init__(self, solution=solution, raises=raises)
        self.payload = payload
        self.returns = returns
        self.export_raises = export_raises
        self.write = write
        self.exports = []

    def export_report_to_file(self, out_dir, plot_name, extension):
        self.exports.append((out_dir, plot_name, extension))
        if self.export_raises:
            raise self.export_raises
        path = os.path.join(out_dir, plot_name + extension)
        if self.write:
            with open(path, "wb") as handle:
                handle.write(self.payload if self.payload is not None else REAL_S11_CSV)
        return path if self.returns is _UNSET else self.returns


def export_hfss(payload=REAL_S11_CSV, existing=(), solution=None, sol_raises=None,
                **kwargs):
    """A design whose API read fails and whose report route works."""
    module = FakeReportModule(existing=existing)
    post = FakeExportPost(solution=solution,
                          raises=sol_raises if sol_raises is not None else RuntimeError(
                              "GrpcApiError: GetVariables failed"),
                          payload=payload, **kwargs)
    return FakeHfss(SWEEPS, post, odesign=FakeDesign(module)), module, post


class TestReportShapes(unittest.TestCase):
    def test_report_name_is_distinctive_deterministic_and_a_legal_filename(self):
        name = read_results.report_name_for("dB(S(1,1))")
        self.assertEqual(name, "AgentReadout_dB_S_1_1")
        self.assertEqual(name, read_results.report_name_for("dB(S(1,1))"))
        self.assertTrue(name.startswith(read_results.REPORT_NAME_PREFIX))
        # export_report_to_file joins this straight onto a directory path.
        self.assertFalse(set(name) & set('\\/:*?"<>|'))

    def test_far_field_spec_differs_on_every_axis_that_matters(self):
        """Four columns come back because it is a Data Table over a sphere, not
        a rectangular plot of a sweep. Each of these was wrong once."""
        modal = read_results.report_spec("dB(S(1,1))")
        far = read_results.report_spec("dB(GainTotal)", sphere="Sphere1")
        self.assertEqual(modal.category, "Modal Solution Data")
        self.assertEqual(modal.display, "Rectangular Plot")
        self.assertEqual(modal.context, ["Domain:=", "Sweep"])
        self.assertEqual(far.category, "Far Fields")
        self.assertEqual(far.display, "Data Table")
        self.assertEqual(far.context, ["Context:=", "Sphere1"])
        self.assertIn("Theta:=", far.families)
        self.assertIn("dB(GainTotal)", far.components[-1])


class TestParseRealExportCsv(unittest.TestCase):
    """Against the captured artifacts above. See the provenance block."""

    def write(self, blob, name="export.csv"):
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        path = os.path.join(tmp, name)
        with open(path, "wb") as handle:
            handle.write(blob)
        return path

    def test_two_column_rectangular_export(self):
        xs, ys, note = read_results.parse_report_csv(self.write(REAL_S11_CSV),
                                                     expect="dB(S(1,1))")
        self.assertEqual(xs, [5.0, 5.01, 5.02, 5.66, 6.5])
        self.assertEqual(ys[0], -0.971789418833437)
        self.assertEqual(min(ys), -7.36862380345162)
        self.assertEqual(xs[ys.index(min(ys))], 5.66)   # the UI-corroborated point
        self.assertIn("parsed 5 rows", note)

    def test_four_column_far_field_export_takes_the_last_column(self):
        """A two-column assumption reads Phi (0.0) as the gain and says so
        cheerfully. The value is the LAST column, always."""
        xs, ys, note = read_results.parse_report_csv(self.write(REAL_FARFIELD_CSV),
                                                     expect="dB(GainTotal)")
        self.assertEqual(ys, [-17.060163588662, -17.3918938333137,
                              -17.7292431059142, -17.060163588662])
        self.assertNotIn(0.0, ys)
        self.assertEqual(xs, [-180.0, -178.0, -176.0, 180.0])   # Theta, not Freq
        self.assertIn("Theta", note)

    def test_crlf_does_not_leak_into_the_last_field(self):
        """The artifacts are CRLF. Splitting on '\\n' puts a '\\r' on every
        row's final value, which then either raises or silently truncates."""
        self.assertIn(b"\r\n", REAL_S11_CSV)
        _, ys, _ = read_results.parse_report_csv(self.write(REAL_S11_CSV))
        self.assertTrue(all(isinstance(v, float) for v in ys))

    def test_x_column_can_be_forced(self):
        xs, _, _ = read_results.parse_report_csv(self.write(REAL_FARFIELD_CSV),
                                                 x_column=0)
        self.assertEqual(xs, [5.66, 5.66, 5.66, 5.66])

    def test_a_missing_file_and_an_empty_file_are_different_outcomes(self):
        """Distinct because they mean different things: nothing was exported,
        versus something was exported and had nothing in it."""
        _, ys, missing = read_results.parse_report_csv(
            os.path.join(tempfile.gettempdir(), "no_such_readout_export.csv"))
        self.assertEqual(ys, [])
        self.assertIn("no file at", missing)
        _, ys, empty = read_results.parse_report_csv(self.write(b""))
        self.assertEqual(ys, [])
        self.assertIn("empty", empty)
        self.assertNotEqual(missing, empty)

    def test_a_header_with_no_rows_is_its_own_outcome(self):
        _, ys, note = read_results.parse_report_csv(
            self.write(REAL_S11_CSV.split(b"\r\n")[0] + b"\r\n"))
        self.assertEqual(ys, [])
        self.assertIn("no parseable numeric rows", note)

    def test_an_unrecognised_header_is_refused_not_guessed(self):
        """Synthetic by necessity — there is no captured artifact of a
        malformed export. It defines nothing about the real shape; it only
        pins what happens when the file is not one."""
        _, ys, note = read_results.parse_report_csv(self.write(b"nonsense\r\n1\r\n2\r\n"))
        self.assertEqual(ys, [])
        self.assertIn("unrecognised header", note)

    def test_a_report_of_another_signal_is_refused(self):
        """The guard against exporting somebody else's report of our name: the
        header does not carry the expression that was asked for."""
        _, ys, note = read_results.parse_report_csv(self.write(REAL_S11_CSV),
                                                    expect="dB(GainTotal)")
        self.assertEqual(ys, [])
        self.assertIn("not this signal's export", note)
        self.assertIn("dB(GainTotal)", note)

    def test_malformed_rows_are_counted_in_the_note_not_hidden(self):
        blob = REAL_S11_CSV + b'5.67,not-a-number\r\n5.68\r\n'
        xs, ys, note = read_results.parse_report_csv(self.write(blob))
        self.assertEqual(len(ys), 5)
        self.assertIn("2 unparseable row(s) skipped", note)


class TestExportRoute(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_the_route_reads_the_signal_end_to_end(self):
        hfss, module, post = export_hfss()
        xs, ys, note = read_results.read_via_report(hfss, "dB(S(1,1))",
                                                    export_dir=self.tmp)
        self.assertEqual(min(ys), -7.36862380345162)
        self.assertEqual(len(module.created), 1)
        self.assertIn("created report", note)
        self.assertIn("parsed 5 rows", note)

    def test_the_sweep_name_is_read_back_never_hardcoded(self):
        """EC#6: `Sweep_MM13NY`'s suffix is random. A hardcoded name misses."""
        hfss, module, _ = export_hfss()
        read_results.read_via_report(hfss, "dB(S(1,1))", export_dir=self.tmp)
        self.assertEqual(module.created[0]["sweep"], "Setup1 : Sweep_MM13NY")

    def test_an_existing_report_of_our_name_is_reused_not_duplicated(self):
        hfss, module, _ = export_hfss(existing=["AgentReadout_dB_S_1_1"])
        name, note = read_results.create_or_reuse_report(hfss, "dB(S(1,1))",
                                                         "Setup1 : Sweep_MM13NY")
        self.assertEqual(name, "AgentReadout_dB_S_1_1")
        self.assertEqual(module.created, [])
        self.assertIn("reused", note)

    def test_a_users_own_report_is_neither_reused_nor_touched(self):
        """Never silently clobber a report the user made. Ours is created
        alongside it; theirs is not read, renamed, or deleted."""
        hfss, module, _ = export_hfss(existing=["S Parameter Plot 1", "MyGain"])
        name, _ = read_results.create_or_reuse_report(hfss, "dB(S(1,1))",
                                                      "Setup1 : Sweep_MM13NY")
        self.assertEqual(name, "AgentReadout_dB_S_1_1")
        self.assertEqual([c["name"] for c in module.created], ["AgentReadout_dB_S_1_1"])
        self.assertIn("S Parameter Plot 1", module.existing)
        self.assertEqual(module.deleted, [])

    def test_the_report_is_left_in_the_project_on_purpose(self):
        """Documented decision, asserted so it cannot drift: deleting is a
        second mutation after the numbers are already in hand, and the report
        left standing is the plot the user's authoritative UI read opens."""
        hfss, module, _ = export_hfss()
        read_results.read_via_report(hfss, "dB(S(1,1))", export_dir=self.tmp)
        self.assertEqual(module.deleted, [])
        self.assertIn("AgentReadout_dB_S_1_1", module.existing)

    def test_a_second_signal_does_not_pile_up_reports(self):
        hfss, module, _ = export_hfss()
        read_results.read_via_report(hfss, "dB(S(1,1))", export_dir=self.tmp)
        read_results.read_via_report(hfss, "dB(S(1,1))", export_dir=self.tmp)
        self.assertEqual(len(module.created), 1)
        self.assertEqual(module.existing.count("AgentReadout_dB_S_1_1"), 1)

    def test_an_unreachable_report_module_is_reported_not_raised(self):
        hfss = sick_hfss()                       # no odesign at all
        _, ys, note = read_results.read_via_report(hfss, "dB(S(1,1))",
                                                   export_dir=self.tmp)
        self.assertEqual(ys, [])
        self.assertIn("ReportSetup", note)

    def test_a_failing_CreateReport_is_reported_not_raised(self):
        module = FakeReportModule(create_raises=RuntimeError("GrpcApiError: CreateReport"))
        hfss = FakeHfss(SWEEPS, FakeExportPost(raises=RuntimeError("boom")),
                        odesign=FakeDesign(module))
        _, ys, note = read_results.read_via_report(hfss, "dB(S(1,1))",
                                                   export_dir=self.tmp)
        self.assertEqual(ys, [])
        self.assertIn("CreateReport", note)
        self.assertIn("GrpcApiError", note)

    def test_an_unlistable_report_module_says_so_and_still_tries(self):
        """`GetAllReportNames` failing means existing reports are UNKNOWN, not
        absent — the note must not let a reader infer the design was empty."""
        module = FakeReportModule(list_raises=RuntimeError("GrpcApiError: GetAllReportNames"))
        hfss = FakeHfss(SWEEPS, FakeExportPost(raises=RuntimeError("boom")),
                        odesign=FakeDesign(module))
        _, ys, note = read_results.read_via_report(hfss, "dB(S(1,1))",
                                                   export_dir=self.tmp)
        self.assertEqual(min(ys), -7.36862380345162)
        self.assertIn("existing reports are unknown", note)
        self.assertEqual(len(module.created), 1)

    def test_a_wrapped_export_returning_False_is_not_mistaken_for_a_path(self):
        """`pyaedt_function_handler` returns False instead of raising. The file
        it would have written is still checked for, then reported missing."""
        hfss, _, post = export_hfss(returns=False, write=False)
        _, ys, note = read_results.read_via_report(hfss, "dB(S(1,1))",
                                                   export_dir=self.tmp)
        self.assertEqual(ys, [])
        self.assertIn("returned False", note)
        self.assertIn("no file is at", note)

    def test_an_export_that_returns_False_but_wrote_the_file_still_reads(self):
        hfss, _, _ = export_hfss(returns=False)
        _, ys, _ = read_results.read_via_report(hfss, "dB(S(1,1))", export_dir=self.tmp)
        self.assertEqual(len(ys), 5)

    def test_a_raising_export_is_reported_not_raised(self):
        hfss, _, _ = export_hfss(export_raises=RuntimeError("GrpcApiError: ExportToFile"))
        _, ys, note = read_results.read_via_report(hfss, "dB(S(1,1))",
                                                   export_dir=self.tmp)
        self.assertEqual(ys, [])
        self.assertIn("ExportToFile", note)

    def test_an_unsolved_design_never_creates_a_report(self):
        module = FakeReportModule()
        hfss = FakeHfss([], FakeExportPost(), odesign=FakeDesign(module))
        _, ys, note = read_results.read_via_report(hfss, "dB(S(1,1))",
                                                   export_dir=self.tmp)
        self.assertEqual(ys, [])
        self.assertIn("nothing solved yet", note)
        self.assertEqual(module.created, [])

    def test_the_far_field_route_carries_the_sphere_through(self):
        hfss, module, _ = export_hfss(payload=REAL_FARFIELD_CSV)
        xs, ys, _ = read_results.read_via_report(hfss, "dB(GainTotal)",
                                                 export_dir=self.tmp, sphere="Sphere1")
        self.assertEqual(module.created[0]["context"], ["Context:=", "Sphere1"])
        self.assertEqual(module.created[0]["category"], "Far Fields")
        self.assertEqual(len(ys), 4)
        self.assertEqual(xs[0], -180.0)


class TestRouteOrder(unittest.TestCase):
    """`get_solution_data` first, the report export second, on one process."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_a_working_api_read_never_touches_the_users_project(self):
        """The whole reason the API goes first: it has no side effects. If it
        answers, no report is created and the report module is never asked
        anything at all."""
        module = FakeReportModule()
        post = FakeExportPost(solution=FakeSolution(sweep=FREQS, values=FILLED))
        hfss = FakeHfss(SWEEPS, post, odesign=FakeDesign(module))
        xs, ys, mechanism, note = read_results.read_signal(hfss, "dB(S(1,1))",
                                                           export_dir=self.tmp)
        self.assertEqual(ys, FILLED)
        self.assertEqual(mechanism, read_results.MECH_API)
        self.assertEqual(module.created, [])
        self.assertEqual(module.listed, 0)
        self.assertEqual(post.exports, [])
        self.assertIn("read 3 points", note)

    def test_the_export_route_is_reached_automatically_when_the_api_fails(self):
        """No human in the loop: one call, and the route that works answers."""
        hfss, module, _ = export_hfss()
        xs, ys, mechanism, note = read_results.read_signal(hfss, "dB(S(1,1))",
                                                           export_dir=self.tmp)
        self.assertEqual(mechanism, read_results.MECH_EXPORT)
        self.assertEqual(min(ys), -7.36862380345162)
        self.assertEqual(len(module.created), 1)

    def test_the_note_carries_both_attempts_in_order(self):
        """The API attempt is the standing measurement of env-compat #6's
        claim that this call once worked here. It has to be legible in the
        trail even when the export route is what produced the numbers."""
        hfss, _, _ = export_hfss()
        _, _, _, note = read_results.read_signal(hfss, "dB(S(1,1))", export_dir=self.tmp)
        self.assertIn("GetVariables", note)
        self.assertLess(note.index(read_results.MECH_API),
                        note.index(read_results.MECH_EXPORT))

    def test_both_routes_failing_reports_no_mechanism(self):
        hfss = sick_hfss()
        xs, ys, mechanism, note = read_results.read_signal(hfss, "dB(S(1,1))",
                                                           export_dir=self.tmp)
        self.assertEqual(ys, [])
        self.assertIsNone(mechanism)
        self.assertIn("GetVariables", note)
        self.assertIn("ReportSetup", note)

    def test_the_default_export_dir_is_not_made_until_a_csv_is_due(self):
        """Offline, and on any run whose API read worked, no temp directory is
        created at all — the export route bails long before it needs one."""
        read_results._DEFAULT_EXPORT_DIR = None
        self.addCleanup(setattr, read_results, "_DEFAULT_EXPORT_DIR", None)
        read_results.read_signal(sick_hfss(), "dB(S(1,1))")
        self.assertIsNone(read_results._DEFAULT_EXPORT_DIR)


class TestReadoutSessionExportRoutes(unittest.TestCase):
    """The verdict has to name which route produced the numbers."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_export_on_the_live_channel_is_its_own_token(self):
        hfss, _, _ = export_hfss()
        recycler = FakeRecycler(healthy_hfss())
        session = read_results.ReadoutSession(hfss, recycle=recycler, export_dir=self.tmp)
        out = session.read("dB(S(1,1))")
        self.assertEqual(out.route, read_results.ROUTE_EXPORT)
        self.assertEqual(min(out.y), -7.36862380345162)
        self.assertEqual(recycler.calls, 0, "a working route must not spend the escalation")
        line = read_results.verdict_line("s11", out)
        self.assertIn("route=report-export ", line)
        self.assertIn("export", line)

    def test_export_after_an_escalation_says_both_facts(self):
        """Which route AND which process. Collapsing either loses evidence."""
        fresh, _, _ = export_hfss()
        recycler = FakeRecycler(fresh)
        session = read_results.ReadoutSession(sick_hfss(), recycle=recycler,
                                              export_dir=self.tmp)
        out = session.read("dB(S(1,1))")
        self.assertEqual(out.route, read_results.ROUTE_EXPORT_FRESH)
        self.assertEqual(recycler.calls, 1)
        line = read_results.verdict_line("s11", out)
        self.assertIn("fresh", line)
        self.assertIn("export", line)
        self.assertNotIn("SYSTEMATIC", line)

    def test_a_later_signal_on_the_recycled_desktop_keeps_the_export_token(self):
        fresh, _, _ = export_hfss()
        session = read_results.ReadoutSession(sick_hfss(), recycle=FakeRecycler(fresh),
                                              export_dir=self.tmp)
        session.read("dB(S(1,1))")
        second = session.read("dB(S(1,1))")
        self.assertEqual(second.route, read_results.ROUTE_EXPORT_FRESH)
        self.assertIn("already spent", second.note)

    def test_the_session_sphere_reaches_the_report(self):
        hfss, module, _ = export_hfss(payload=REAL_FARFIELD_CSV)
        session = read_results.ReadoutSession(hfss, export_dir=self.tmp,
                                              sphere="Sphere1")
        out = session.read("dB(GainTotal)")
        self.assertEqual(out.route, read_results.ROUTE_EXPORT)
        self.assertEqual(module.created[0]["display"], "Data Table")
        self.assertEqual(len(out.y), 4)

    def test_the_export_route_is_tried_before_the_escalation_is_spent(self):
        """A desktop launch costs a minute; the export costs a call. Spending
        the run's one escalation on a signal the live process could have
        exported is the budget wasted for nothing."""
        hfss, _, _ = export_hfss()
        recycler = FakeRecycler(healthy_hfss())
        session = read_results.ReadoutSession(hfss, recycle=recycler, export_dir=self.tmp)
        session.read("dB(S(1,1))")
        self.assertFalse(session.escalated)
        self.assertFalse(session.on_fresh_process)


class FakeSettings:
    """pyAEDT's `settings`, as far as this module is concerned.

    `release_on_exception` defaults True in 1.3.0
    (generic/settings.py:247) and is a property with a setter (:1011).
    """

    def __init__(self, value=True):
        self.release_on_exception = value


class StickyFakeSettings:
    """A settings object whose write is silently ignored."""

    @property
    def release_on_exception(self):
        return True

    @release_on_exception.setter
    def release_on_exception(self, value):
        pass


class TestReleaseOnExceptionRouteAround(unittest.TestCase):
    """`settings.release_on_exception` off, offline, against fake modules.

    This is the route-around that cost a month: with the flag on, one failed
    read released EVERY desktop session, so the next call raised `GrpcApiError`
    naming whatever it tried next and the fault read as a broken transport.
    Measured on 2026-09-01: with it off, three consecutive failed reads and the
    session still answered `design_name`.

    The fakes go into `sys.modules` under the real dotted names. `__import__`
    checks `sys.modules` for the full name before touching the filesystem, so
    the real pyAEDT is never imported here — that would load
    PyDesktopPlugin.dll and turn a millisecond suite into a 25-second one.
    """

    NAMES = ("ansys", "ansys.aedt", "ansys.aedt.core", "ansys.aedt.core.generic",
             "ansys.aedt.core.generic.settings", "ansys.aedt.core.generic.aedt_constants",
             "ansys.aedt.core.application", "ansys.aedt.core.application.design_solutions",
             "pyaedt")

    def stub(self, settings=None):
        import types
        saved = {name: sys.modules.get(name) for name in self.NAMES}

        def restore():
            for name, module in saved.items():
                if module is None:
                    sys.modules.pop(name, None)
                else:
                    sys.modules[name] = module
        self.addCleanup(restore)
        for name in self.NAMES:
            sys.modules[name] = types.ModuleType(name)
        if settings is not None:
            sys.modules["ansys.aedt.core.generic.settings"].settings = settings
        return settings

    def test_the_flag_is_turned_off(self):
        settings = self.stub(FakeSettings())
        self.assertTrue(settings.release_on_exception, "pyAEDT ships it ON")
        self.assertEqual(read_results._disable_release_on_exception(), "disabled")
        self.assertFalse(settings.release_on_exception)

    def test_an_already_disabled_flag_is_reported_as_such_not_as_a_no_op(self):
        self.stub(FakeSettings(value=False))
        self.assertEqual(read_results._disable_release_on_exception(), "already-disabled")

    def test_a_write_that_does_not_stick_is_never_reported_as_disabled(self):
        """The `data_real` failure shape: a check that reports healthy while
        doing nothing. Read it back, or do not claim it."""
        self.stub(StickyFakeSettings())
        status = read_results._disable_release_on_exception()
        self.assertIn("unavailable", status)
        self.assertIn("did not stick", status)

    def test_a_missing_settings_object_is_unavailable_not_silently_fine(self):
        self.stub(None)          # modules exist, none of them has `settings`
        status = read_results._disable_release_on_exception()
        self.assertTrue(status.startswith("unavailable:"), status)
        self.assertIn("ansys.aedt.core.generic.settings", status)

    def test_apply_route_arounds_reports_it_alongside_the_alias(self):
        settings = self.stub(FakeSettings())
        status = read_results.apply_route_arounds()
        self.assertIn("release_on_exception=disabled", status)
        self.assertIn("default_solution=", status)
        self.assertFalse(settings.release_on_exception)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: read_results tests={total} failed={failed}")
    raise SystemExit(1 if failed else 0)
