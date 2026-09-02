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


class TestHistory(unittest.TestCase):
    """The record (run logging, ticket 01): `sessions.jsonl` is append-only,
    `run.json` is written once, `session.json` keeps its role.

    Written against `patch-array-5800`, whose session.json was overwritten by
    a later readout experiment; the run's own three sessions were no longer
    findable from the workspace."""

    def _state_dir(self, tmp):
        return os.path.join(tmp, "patch-array-5800", "results", "state")

    def test_every_declaration_appends_and_none_replaces(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = self._state_dir(tmp)
            S.start(S.CLARIFY, name="patch", state_dir=state, host="claude-code",
                    host_session_id="id-clarify")
            S.start(S.BUILD, name="patch", state_dir=state, host="claude-code",
                    host_session_id="id-build")
            # The readout experiment: the same phase declared again, later.
            S.start(S.SOLVE, name="patch", state_dir=state, host="claude-code",
                    host_session_id="id-solve")
            S.start(S.SOLVE, name="readout-experiment", state_dir=state,
                    host="claude-code", host_session_id="id-readout")
            records = S.history(state)
        self.assertEqual([r["phase"] for r in records],
                         [S.CLARIFY, S.BUILD, S.SOLVE, S.SOLVE])
        self.assertEqual([r["host_session_id"] for r in records],
                         ["id-clarify", "id-build", "id-solve", "id-readout"])
        for key in ("ts", "phase", "name", "host", "host_session_id", "cwd",
                    "worktree", "skill_commit", "pid"):
            self.assertTrue(all(key in r for r in records), key)

    def test_session_json_is_still_the_current_session(self):
        """The phase gate reads one file and gets the latest declaration;
        the history is beside it, not instead of it."""
        with tempfile.TemporaryDirectory() as tmp:
            state = self._state_dir(tmp)
            S.start(S.CLARIFY, name="patch", state_dir=state)
            S.start(S.BUILD, name="patch", state_dir=state)
            current = S.Session.load(state)
            with open(S.Session.path_for(state), encoding="utf-8") as fh:
                keys = set(json.load(fh))
        self.assertEqual(current.phase, S.BUILD)
        self.assertEqual(keys, set(S.Session.__dataclass_fields__))

    def test_run_json_is_written_once_and_never_rewritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = self._state_dir(tmp)
            S.start(S.CLARIFY, name="patch", state_dir=state, task_doc="task.md")
            with open(S.run_path(state), "rb") as fh:
                first = fh.read()
            run = S.run_info(state)
            # A later declaration with different everything must not touch it.
            S.start(S.SOLVE, name="readout-experiment", state_dir=state,
                    task_doc="other.md")
            with open(S.run_path(state), "rb") as fh:
                second = fh.read()
        self.assertEqual(first, second)
        self.assertEqual(run["task_doc"], "task.md")
        self.assertEqual(run["run_id"],
                         "patch-array-5800-" + run["created_ts"][:10])
        self.assertEqual(os.path.basename(run["workspace"]), "patch-array-5800")

    def test_a_copied_workspace_gets_its_own_run(self):
        """`results/` is gitignored, so a copy starts without run.json and
        is named for itself, never for the workspace it was copied from."""
        with tempfile.TemporaryDirectory() as tmp:
            a = S.ensure_run(self._state_dir(tmp), now_ms=1_756_800_000_000)
            copy = os.path.join(tmp, "patch-array-5800 - Copy", "results", "state")
            b = S.ensure_run(copy, now_ms=1_756_900_000_000)
        self.assertNotEqual(a["run_id"], b["run_id"])
        self.assertTrue(b["run_id"].startswith("patch-array-5800 - Copy-"))

    def test_skill_commit_is_recorded_and_tolerates_a_missing_git(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = self._state_dir(tmp)
            S.start(S.CLARIFY, state_dir=state)
            record = S.history(state)[0]
        self.assertEqual(record["skill_commit"], S.skill_commit())
        original = S.subprocess.run
        S.subprocess.run = lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError("git"))
        try:
            self.assertEqual(S.skill_commit(), "")
            self.assertEqual(S.worktree_of(tempfile.gettempdir()), "")
        finally:
            S.subprocess.run = original

    def test_a_torn_history_line_is_skipped_not_fatal(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = self._state_dir(tmp)
            S.start(S.CLARIFY, state_dir=state)
            with open(S.history_path(state), "a", encoding="utf-8") as fh:
                fh.write('{"phase": "build", "na')
            self.assertEqual(len(S.history(state)), 1)


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


class TestTraceBudget(unittest.TestCase):
    """The budget counts real tool calls from the step trace (ticket 02/04).

    The last run's card read `calls: 0` against a budget of 60 because the
    count was whatever `note_call` had been told, which was nothing. The
    count now comes from `results/state/trace/*.steps.jsonl`, and a session
    with no trace is reported as unaccounted rather than as zero.
    """

    def _trace(self, tmp, name, steps):
        os.makedirs(S.trace_dir(tmp), exist_ok=True)
        with open(os.path.join(S.trace_dir(tmp), name), "w", encoding="utf-8") as fh:
            for step in steps:
                fh.write(step if isinstance(step, str) else json.dumps(step))
                fh.write("\n")

    def test_no_trace_is_none_and_the_verdict_says_unaccounted(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(S.trace_calls(tmp))
            os.makedirs(S.trace_dir(tmp))
            self.assertIsNone(S.trace_calls(tmp))              # a dir with no trace
            self._trace(tmp, "notes.txt", ["not a trace"])
            self.assertIsNone(S.trace_calls(tmp))
        verdict = S.Session(phase=S.SOLVE).budget_verdict(trace_calls=None)
        self.assertTrue(verdict.startswith("ok:"))
        self.assertIn("calls unaccounted (no trace)", verdict)
        self.assertNotIn("calls=0", verdict)

    def test_tool_use_lines_are_counted_across_every_trace_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._trace(tmp, "id-build.steps.jsonl", [
                {"kind": "tool_use", "name": "Bash"},
                {"kind": "tool_result"},
                {"kind": "assistant_text"},
                {"kind": "tool_use", "name": "Read"},
            ])
            self._trace(tmp, "id-solve.steps.jsonl", [
                {"kind": "tool_use"},
                "",
                '{"kind": "tool_use", "na',                     # torn tail line
                "[1, 2]",                                        # foreign line
            ])
            self.assertEqual(S.trace_calls(tmp), 3)

    def test_the_trace_count_drives_the_verdict_and_the_breach(self):
        s = S.Session(phase=S.BUILD)
        self.assertTrue(s.budget_verdict(trace_calls=12).startswith("ok:"))
        self.assertIn("calls=12/60 (trace)", s.budget_verdict(trace_calls=12))
        self.assertFalse(s.exceeds(12))
        verdict = s.budget_verdict(trace_calls=250)                # S11's measured parts
        self.assertTrue(verdict.startswith("ESCALATE:"))
        self.assertIn("(trace)", verdict)
        self.assertTrue(s.exceeds(250))
        self.assertFalse(s.exceeds(None))

    def test_the_trace_beats_a_hand_count(self):
        s = S.Session(phase=S.BUILD)
        s.note_call(5)
        self.assertIn("calls=40/60 (trace)", s.budget_verdict(trace_calls=40))
        self.assertIn("calls=5/60 (note_call)", s.budget_verdict())


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: session "
          f"tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
