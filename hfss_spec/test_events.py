"""Tier 0 tests for the event log (run logging, ticket 03). No AEDT, seconds.

Three things are asserted here, in the order the ticket lists them:

1. `hfss_spec/events.py` itself — append-only, never raises, a no-op without
   a state dir, one line per `detail`, `run_id` from `run.json` (ticket 01)
   or null.
2. The repo's own scripts emit their events: the session boundary
   (`phase.declared`, `phase.refused`, `budget.escalate`), the compiler (one
   `stage.start` / `stage.end` pair per Spine stage, its `PASS:` line as the
   verdict), `compile_spec` end to end with the desktop stood in by the
   golden tests' recorder (`FakeHfss`), and the offline gates and recorders.
3. The Tier-1 shape — a compile of a canonical case leaves one pair per
   stage — proven offline against `FakeHfss` over the real `patch-2400`
   spec, the same way `test_hfss_spec` proves the compiler's call sequence.
   The live Tier-1 run is still owed a desktop; this is the part of it that
   needs none.

Run: `python hfss_spec/test_events.py`
"""

import contextlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

REPO = Path(__file__).resolve().parent.parent
for entry in (str(REPO), str(REPO / "scripts")):
    if entry not in sys.path:
        sys.path.insert(0, entry)

from hfss_spec import compiler, events                     # noqa: E402
from hfss_spec import session as S                         # noqa: E402
from hfss_spec.loader import load_spec                     # noqa: E402
from hfss_spec.test_hfss_spec import PATCH_SPEC, FakeHfss  # noqa: E402

import compile_spec                                        # noqa: E402
import precheck                                            # noqa: E402
import record_gate                                         # noqa: E402
import record_outcome                                      # noqa: E402
import run_card                                            # noqa: E402
import tier0                                               # noqa: E402
import tier1                                               # noqa: E402
import validate_spec                                       # noqa: E402

ISO_MS = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")
# A real Claude Code transcript slice (ticket 04's capture), enough to card.
CLAUDE_SLICE = (REPO / "scripts" / "fixtures" / "claude-code"
                / "f0c832a3-cb36-4168-ac07-70c2793c74a2.jsonl")


class Workspace(unittest.TestCase):
    """A throwaway workspace with an existing `results/state`."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.ws = self.tmp / "ws"
        self.state = self.ws / "results" / "state"
        self.state.mkdir(parents=True)

    def names(self):
        return events.names(self.state)

    def records(self):
        return events.read(self.state)

    @contextlib.contextmanager
    def quiet(self):
        with contextlib.redirect_stdout(io.StringIO()) as out, \
                contextlib.redirect_stderr(io.StringIO()):
            yield out


# --- the module ---------------------------------------------------------------


class TestEmit(Workspace):
    def test_append_only_with_the_documented_keys(self):
        self.assertTrue(events.emit(self.state, "a.first", stage="s", verdict="PASS: s x=1"))
        first = events.events_path(self.state)
        first_line = Path(first).read_text(encoding="utf-8")
        self.assertTrue(events.emit(self.state, "b.second"))
        text = Path(first).read_text(encoding="utf-8")
        self.assertTrue(text.startswith(first_line))          # the first line is untouched
        self.assertEqual(len(text.splitlines()), 2)
        record = json.loads(text.splitlines()[0])
        self.assertEqual(tuple(record), events.FIELDS)
        self.assertEqual(record["event"], "a.first")
        self.assertEqual(record["stage"], "s")
        self.assertEqual(record["verdict"], "PASS: s x=1")
        self.assertEqual(record["pid"], os.getpid())
        self.assertTrue(ISO_MS.match(record["ts"]), record["ts"])
        self.assertIsInstance(record["ts_ms"], int)
        self.assertIsNone(record["duration_ms"])
        self.assertIsNone(record["run_id"])                   # no run.json yet
        self.assertIsNone(record["phase"])                    # nothing declared

    def test_no_op_when_the_state_dir_does_not_exist(self):
        missing = self.tmp / "nope" / "results" / "state"
        self.assertFalse(events.emit(missing, "x"))
        self.assertFalse((self.tmp / "nope").exists())        # nothing was created
        self.assertFalse(events.emit(None, "x"))
        self.assertFalse(events.emit("", "x"))
        self.assertEqual(events.read(missing), [])

    def test_never_raises(self):
        # 1. the log file's name is taken by a directory
        os.makedirs(events.events_path(self.state))
        self.assertFalse(events.emit(self.state, "x"))
        shutil.rmtree(events.events_path(self.state))
        # 2. the filesystem refuses the append
        with mock.patch("builtins.open", side_effect=OSError("disk full")):
            self.assertFalse(events.emit(self.state, "x"))
        # 3. a detail that cannot even be turned into a string

        class Unprintable:
            def __str__(self):
                raise RuntimeError("no")

        self.assertFalse(events.emit(self.state, "x", detail=Unprintable()))
        # 4. a torn run.json is not a reason to lose the event
        (self.state / events.RUN_FILE).write_text("{not json", encoding="utf-8")
        self.assertTrue(events.emit(self.state, "y"))
        self.assertIsNone(self.records()[-1]["run_id"])

    def test_detail_and_verdict_are_one_line(self):
        events.emit(self.state, "x", verdict="PASS: a\nsecond line\n",
                    detail="first\nsecond")
        record = self.records()[0]
        self.assertEqual(record["verdict"], "PASS: a")
        self.assertEqual(record["detail"], "first")
        events.emit(self.state, "y", detail="z" * (events.MAX_LINE + 50))
        self.assertEqual(len(self.records()[1]["detail"]), events.MAX_LINE)
        events.emit(self.state, "w", detail=None, verdict=None)
        self.assertEqual(self.records()[2]["detail"], "")
        self.assertIsNone(self.records()[2]["verdict"])

    def test_run_id_comes_from_run_json(self):
        info = S.ensure_run(self.state, now_ms=1_755_000_000_000)
        events.emit(self.state, "x")
        self.assertEqual(self.records()[0]["run_id"], info["run_id"])
        self.assertTrue(info["run_id"].startswith("ws-"))

    def test_phase_defaults_to_the_current_session(self):
        with self.quiet():
            S.start("build", state_dir=self.state)              # itself an event
        events.emit(self.state, "x")
        events.emit(self.state, "y", phase="solve")
        phases = [r["phase"] for r in self.records()]
        self.assertEqual(phases, ["build", "build", "solve"])

    def test_read_skips_torn_lines(self):
        events.emit(self.state, "x")
        with open(events.events_path(self.state), "a", encoding="utf-8") as handle:
            handle.write('{"event": "half"')
        self.assertEqual(self.names(), ["x"])

    def test_duration_is_an_int_ms(self):
        events.emit(self.state, "x", duration_ms=12.7)
        self.assertEqual(self.records()[0]["duration_ms"], 12)


# --- the session boundary ------------------------------------------------------


class TestSessionEvents(Workspace):
    def test_declaration_is_an_event(self):
        with self.quiet():
            S.start("clarify", name="cell", state_dir=self.state, host="opencode",
                    host_session_id="quiet-owl")
        records = self.records()
        self.assertEqual([r["event"] for r in records], ["phase.declared"])
        self.assertEqual(records[0]["phase"], "clarify")
        self.assertIn("name=cell", records[0]["detail"])
        self.assertIn("session_id=quiet-owl", records[0]["detail"])
        self.assertEqual(records[0]["run_id"], S.run_info(self.state)["run_id"])

    def test_refusal_is_an_event_with_the_action(self):
        with self.quiet():
            S.start("clarify", state_dir=self.state)
        with self.assertRaises(S.PhaseViolation):
            S.require("compile_model", self.state)
        refused = self.records()[-1]
        self.assertEqual(refused["event"], "phase.refused")
        self.assertEqual(refused["phase"], "clarify")
        self.assertTrue(refused["detail"].startswith("action=compile_model:"))
        self.assertTrue(refused["verdict"].startswith("FAIL: phase-boundary"))

    def test_an_unguarded_workspace_records_no_refusal(self):
        S.require("solve", self.state)
        self.assertEqual(self.names(), [])

    def test_budget_escalation_is_an_event(self):
        session = S.Session(phase="build", call_budget=2)
        self.assertTrue(session.budget_verdict(trace_calls=1, state_dir=self.state)
                        .startswith("ok:"))
        self.assertEqual(self.names(), [])
        verdict = session.budget_verdict(trace_calls=5, state_dir=self.state)
        self.assertTrue(verdict.startswith("ESCALATE:"))
        escalated = self.records()[-1]
        self.assertEqual(escalated["event"], "budget.escalate")
        self.assertEqual(escalated["verdict"], verdict)
        self.assertIn("calls=5", escalated["detail"])


# --- the compiler ----------------------------------------------------------------


class TestCompilerEvents(Workspace):
    def test_one_pair_per_stage_with_the_pass_line_as_verdict(self):
        """The Tier-1 shape, offline: a compile of the canonical patch-2400
        case leaves exactly one stage.start / stage.end pair per Spine stage,
        in Spine order, each end carrying that stage's own PASS: line."""
        spec = load_spec(PATCH_SPEC)
        log = compiler.BuildLog(state_dir=str(self.state))
        compiler.build(spec, FakeHfss(), log)
        records = self.records()
        expected = []
        for stage in compiler.STAGES:
            expected += [("stage.start", stage), ("stage.end", stage)]
        self.assertEqual([(r["event"], r["stage"]) for r in records], expected)
        ends = [r for r in records if r["event"] == "stage.end"]
        self.assertEqual([r["verdict"] for r in ends], log.lines)
        for record in ends:
            self.assertTrue(record["verdict"].startswith("PASS: "))
            self.assertIsInstance(record["duration_ms"], int)
        for record in records:
            if record["event"] == "stage.start":
                self.assertIsNone(record["verdict"])

    def test_a_failing_stage_ends_with_a_fail_line_and_still_raises(self):
        spec = load_spec(PATCH_SPEC)
        log = compiler.BuildLog(state_dir=str(self.state))
        with self.assertRaises(compiler.CompileError):
            compiler.build(spec, FakeHfss(valid=False), log)
        records = self.records()
        self.assertEqual(records[-2]["event"], "stage.start")
        self.assertEqual(records[-1]["event"], "stage.end")
        self.assertEqual(records[-1]["stage"], "validate")
        self.assertTrue(records[-1]["verdict"].startswith("FAIL: validate CompileError:"))
        # every earlier stage still has its full pair
        self.assertEqual(len(records), 2 * len(compiler.STAGES))

    def test_no_state_dir_means_no_log_and_no_complaint(self):
        log = compiler.BuildLog()
        compiler.build(load_spec(PATCH_SPEC), FakeHfss(), log)
        self.assertEqual(len(log.results), len(compiler.STAGES))
        self.assertEqual(self.names(), [])


class TestCompileSpecEvents(Workspace):
    """`scripts/compile_spec.py` end to end, the desktop stood in by the recorder.

    `load_ws_common` is replaced by a fake workspace module whose `attach`
    returns a `FakeHfss` and whose `exit_keep_alive` / `os._exit` raise
    `SystemExit` instead of ending the interpreter, so `_leave` is exercised
    without a desktop and without killing the test.
    """

    def setUp(self):
        super().setUp()
        self.attached = []
        suite = self

        def attach(launch=False):
            suite.attached.append(launch)
            return FakeHfss()

        def keep_alive():
            raise SystemExit(0)

        self.ws_module = SimpleNamespace(attach=attach, exit_keep_alive=keep_alive)

    def compile(self, *extra):
        argv = ["--workspace", str(self.ws), "--spec", str(PATCH_SPEC), *extra]
        with mock.patch.object(compile_spec, "load_ws_common", return_value=self.ws_module), \
                mock.patch.object(compile_spec.os, "_exit",
                                  side_effect=lambda code: (_ for _ in ()).throw(SystemExit(code))), \
                self.quiet() as out:
            try:
                code = compile_spec.main(argv)
            except SystemExit as exc:
                code = exc.code
        return code, out.getvalue()

    def test_compile_brackets_every_stage_and_ends_with_the_summary_line(self):
        code, out = self.compile()
        self.assertEqual(code, 0, out)
        self.assertEqual(self.attached, [False])
        names = self.names()
        self.assertEqual(names[0], "compile.start")
        self.assertEqual(names[-1], "compile.end")
        pairs = names[1:-1]
        self.assertEqual(pairs, ["stage.start", "stage.end"] * len(compiler.STAGES))
        end = self.records()[-1]
        self.assertTrue(end["verdict"].startswith("PASS: compile_spec spec="), end)
        self.assertTrue(end["verdict"].endswith(f"stages={len(compiler.STAGES)}"))
        self.assertIn(end["verdict"], out)                    # the same string was printed
        self.assertIsInstance(end["duration_ms"], int)

    def test_dry_run_records_its_gate_line(self):
        code, out = self.compile("--dry-run")
        self.assertEqual(code, 0, out)
        self.assertEqual(self.attached, [])
        self.assertEqual(self.names(), ["gate.compile_spec"])
        self.assertTrue(self.records()[0]["verdict"].startswith("PASS: compile_spec dry-run"))

    def test_a_clarify_session_is_refused_and_the_refusal_is_recorded(self):
        with self.quiet():
            S.start("clarify", state_dir=self.state)
        code, out = self.compile()
        self.assertEqual(code, 1)
        self.assertIn("FAIL: compile_spec phase-boundary", out)
        self.assertEqual(self.names(), ["phase.declared", "phase.refused"])
        self.assertEqual(self.attached, [])                     # never reached a desktop

    def test_a_build_session_stamps_run_id_and_phase_on_every_event(self):
        with self.quiet():
            S.start("build", state_dir=self.state)
        code, _ = self.compile()
        self.assertEqual(code, 0)
        run_id = S.run_info(self.state)["run_id"]
        for record in self.records():
            self.assertEqual(record["run_id"], run_id)
            self.assertEqual(record["phase"], "build")


# --- gates and recorders -------------------------------------------------------


class TestScriptEvents(Workspace):
    def test_validate_spec_records_its_summary_line(self):
        with self.quiet() as out:
            code = validate_spec.main([str(PATCH_SPEC), "--workspace", str(self.ws), "--quiet"])
        self.assertEqual(code, 0)
        record = self.records()[0]
        self.assertEqual(record["event"], "gate.validate_spec")
        self.assertTrue(record["verdict"].startswith("PASS: validate_spec errors=0"))
        self.assertEqual(out.getvalue().strip(), record["verdict"])

    def test_validate_spec_defaults_to_the_specs_own_workspace(self):
        spec_copy = self.ws / "design.yaml"
        shutil.copy(PATCH_SPEC, spec_copy)
        with self.quiet():
            validate_spec.main([str(spec_copy), "--quiet"])
        self.assertEqual(self.names(), ["gate.validate_spec"])
        # a spec under knowledge/cases/ has no state dir: nothing is written
        with self.quiet():
            validate_spec.main([str(PATCH_SPEC), "--quiet"])
        self.assertFalse((PATCH_SPEC.parent / "results").exists())

    def test_precheck_records_the_verdict_line(self):
        with self.quiet():
            precheck.main([str(PATCH_SPEC), "--workspace", str(self.ws)])
        record = self.records()[0]
        self.assertEqual(record["event"], "gate.precheck")
        self.assertRegex(record["verdict"], r"^(PASS|FAIL|UNCHECKED): precheck recipe=")

    def test_record_outcome_and_record_gate(self):
        with self.quiet():
            self.assertEqual(record_outcome.main(
                ["--workspace", str(self.ws), "--outcome", "completed",
                 "--completions", "2", "--note", "user verdict"]), 0)
            self.assertEqual(record_gate.main(
                ["--workspace", str(self.ws), "--gate", "1", "--verdict", "fixes",
                 "--note", "notches"]), 0)
            self.assertEqual(record_outcome.main(
                ["--workspace", str(self.ws), "--outcome", "nonsense"]), 1)
        records = self.records()
        self.assertEqual([r["event"] for r in records], ["outcome.recorded", "gate.recorded"])
        self.assertTrue(records[0]["verdict"].startswith("PASS: record_outcome outcome=completed"))
        self.assertIn("note=user verdict", records[0]["detail"])
        self.assertTrue(records[1]["verdict"].startswith("PASS: record_gate gate=1 verdict=fixes"))

    def test_tier1_dry_run_records_its_gate(self):
        src = self.ws / "src"
        src.mkdir()
        (src / "01_stage.py").write_text("print('PASS: stage')\n", encoding="utf-8")
        (src / "08_solve.py").write_text("# never run here\n", encoding="utf-8")
        with self.quiet():
            code = tier1.main(["--workspace", str(self.ws), "--dry-run"])
        self.assertEqual(code, 0)
        record = self.records()[0]
        self.assertEqual(record["event"], "gate.tier1")
        self.assertEqual(record["verdict"], "PASS: tier1 dry-run stages=1 refused=1")

    def test_tier1_brackets_each_stage_script_with_its_verification_line(self):
        """The stage-script route: tier1 knows the boundary and the line."""
        src = self.ws / "src"
        src.mkdir()
        (src / "01_a.py").write_text("print('PASS: a objects == 1')\n", encoding="utf-8")
        (src / "02_b.py").write_text("print('no verification line here')\n", encoding="utf-8")
        with self.quiet():
            code = tier1.main(["--workspace", str(self.ws), "--no-snapshot", "--timeout", "60"])
        self.assertEqual(code, 1)
        records = self.records()
        self.assertEqual([(r["event"], r["stage"]) for r in records],
                         [("stage.start", "01_a.py"), ("stage.end", "01_a.py"),
                          ("stage.start", "02_b.py"), ("stage.end", "02_b.py"),
                          ("gate.tier1", None)])
        self.assertEqual(records[1]["verdict"], "PASS: a objects == 1")
        self.assertTrue(records[3]["verdict"].startswith("FAIL: 02_b.py"))
        self.assertTrue(records[4]["verdict"].startswith("FAIL: tier1 stages=2 failed=02_b.py"))

    def test_run_card_records_the_card_it_wrote(self):
        summary = self.ws / "summary.md"
        summary.write_text("# run\n", encoding="utf-8")
        with self.quiet():
            code = run_card.main(["--transcript", str(CLAUDE_SLICE),
                                  "--summary", str(summary)])
        self.assertEqual(code, 0)
        self.assertIn("## Run card", summary.read_text(encoding="utf-8"))
        record = self.records()[0]
        self.assertEqual(record["event"], "card.written")
        self.assertEqual(record["stage"], "summary")
        self.assertTrue(record["verdict"].startswith("PASS: run_card written summary="))
        self.assertIn("sessions=1", record["detail"])
        self.assertRegex(record["detail"], r"billed=\d+")

    def test_tier0_gate_lands_only_with_a_workspace(self):
        tier0.record_gate(None, "PASS: tier0 suites=1 failed=0 elapsed=0.1s", [], 0.1)
        self.assertEqual(self.names(), [])
        tier0.record_gate(str(self.ws), "PASS: tier0 suites=1 failed=0 elapsed=0.1s", [], 0.1)
        record = self.records()[0]
        self.assertEqual(record["event"], "gate.tier0")
        self.assertTrue(record["verdict"].startswith("PASS: tier0"))
        self.assertEqual(record["duration_ms"], 100)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: events tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
