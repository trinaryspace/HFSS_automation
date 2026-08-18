"""Tier 0 tests for the session boundary. No AEDT, no license, milliseconds.

Written against cell S11, which spent 51 minutes and 151,526 tokens writing a
field solver inside a Clarification block and delivered nothing. The tests are
stated in those terms rather than abstractly, because the regression that matters
is not "the state machine works" but "a clarify session still cannot reach a
licence, and existing workspaces still run".
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hfss_spec import session as S                     # noqa: E402


class TestBoundary(unittest.TestCase):
    def test_clarify_may_not_launch_a_desktop(self):
        """The S11 shape: a clarify session reaching for build-phase work."""
        with self.assertRaises(S.PhaseViolation) as caught:
            S.Session(phase=S.CLARIFY).require("launch_desktop")
        message = str(caught.exception)
        self.assertIn("clarify", message)
        self.assertIn("build", message)

    def test_clarify_may_not_compile_or_solve(self):
        clarify = S.Session(phase=S.CLARIFY)
        for action in ("compile_model", "solve"):
            with self.assertRaises(S.PhaseViolation):
                clarify.require(action)

    def test_build_may_not_solve(self):
        """Build owns geometry, not solver time. tier1 already refuses stage 08+;
        this makes the same boundary true for every path, not just that runner."""
        with self.assertRaises(S.PhaseViolation):
            S.Session(phase=S.BUILD).require("solve")

    def test_each_phase_can_do_its_own_work(self):
        S.Session(phase=S.BUILD).require("compile_model")
        S.Session(phase=S.BUILD).require("launch_desktop")
        S.Session(phase=S.SOLVE).require("solve")

    def test_authoring_and_gating_are_legal_everywhere(self):
        """Offline work is cheap and a build session re-gating its own spec is
        normal; the boundary is about licences and solver time, not about
        forbidding thought."""
        for phase in S.PHASES:
            S.Session(phase=phase).require("author_spec")
            S.Session(phase=phase).require("gate_spec")

    def test_the_refusal_says_what_to_do_instead(self):
        """A refusal that does not route the decision to the user invites a
        work-around, which is how S11 got past a documented limit."""
        try:
            S.Session(phase=S.CLARIFY).require("solve")
        except S.PhaseViolation as exc:
            self.assertIn("user", str(exc))
            self.assertIn("do not work around", str(exc))

    def test_an_unknown_action_is_never_silently_permitted(self):
        with self.assertRaises(S.UnknownAction):
            S.Session(phase=S.BUILD).require("lauch_desktop")   # typo on purpose


class TestPersistence(unittest.TestCase):
    def test_a_session_round_trips_through_the_state_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            started = S.start(S.BUILD, name="patch-2400", state_dir=tmp)
            loaded = S.Session.load(tmp)
            self.assertEqual(loaded.phase, S.BUILD)
            self.assertEqual(loaded.name, "patch-2400")
            self.assertEqual(loaded.call_budget, started.call_budget)

    def test_no_session_file_means_unguarded_not_broken(self):
        """The guard lands in a repo full of workspaces that predate it. A guard
        that broke every existing path on day one would be switched off."""
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(S.Session.load(tmp))
            S.require("solve", tmp)          # must not raise

    def test_a_corrupt_or_unknown_phase_is_treated_as_absent(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(S.Session.path_for(tmp), "w", encoding="utf-8") as fh:
                json.dump({"phase": "wishful"}, fh)
            self.assertIsNone(S.Session.load(tmp))
            with open(S.Session.path_for(tmp), "w", encoding="utf-8") as fh:
                fh.write("{not json")
            self.assertIsNone(S.Session.load(tmp))

    def test_a_declared_session_is_enforced_through_the_cli_helper(self):
        with tempfile.TemporaryDirectory() as tmp:
            S.start(S.CLARIFY, state_dir=tmp)
            with self.assertRaises(S.PhaseViolation):
                S.require("launch_desktop", tmp)
            S.require("author_spec", tmp)    # still fine

    def test_start_rejects_a_phase_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            S.start("clarrify")


class TestBudget(unittest.TestCase):
    def test_the_default_matches_the_documented_escalation(self):
        self.assertEqual(S.DEFAULT_CALL_BUDGET, 60)

    def test_a_session_under_budget_is_ok(self):
        s = S.Session(phase=S.CLARIFY)
        s.note_call(10)
        self.assertFalse(s.over_budget)
        self.assertTrue(s.budget_verdict().startswith("ok:"))

    def test_reaching_the_budget_escalates_with_the_reason(self):
        """S11's cost was not the wrong decision at call 20; it was the 200
        calls after it with nobody to notice."""
        s = S.Session(phase=S.CLARIFY)
        s.note_call(S.DEFAULT_CALL_BUDGET)
        self.assertTrue(s.over_budget)
        verdict = s.budget_verdict()
        self.assertTrue(verdict.startswith("ESCALATE:"))
        self.assertIn("looping", verdict)

    def test_s11_would_have_escalated_four_times_over(self):
        s = S.Session(phase=S.CLARIFY)
        s.note_call(250)                     # S11's measured parts
        self.assertTrue(s.over_budget)

    def test_a_zero_budget_disables_the_check(self):
        s = S.Session(phase=S.BUILD, call_budget=0)
        s.note_call(10_000)
        self.assertFalse(s.over_budget)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: session "
          f"tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
