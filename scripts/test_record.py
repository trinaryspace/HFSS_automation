"""Tier 0 tests for the two run-record writers (run logging, ticket 02).

`record_outcome.py` writes `results/state/outcome.txt` in the key=value form
the run card parses; `record_gate.py` appends Review-gate verdicts to
`results/state/review_gate.txt`. Both print one `PASS:` line, refuse
malformed input with a `FAIL:` line and exit 1, and write nothing when they
refuse. The reader under test for the outcome is the real one:
`run_card.Outcome`.

Usage: python scripts/test_record.py
"""

import contextlib
import io
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import record_gate  # noqa: E402
import record_outcome  # noqa: E402
import run_card  # noqa: E402


def run(main, args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(args)
    return code, out.getvalue(), err.getvalue()


class RecordBase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.ws = Path(self.tmp) / "ws"
        self.ws.mkdir()
        self.state = self.ws / "results" / "state"


class TestRecordOutcome(RecordBase):
    def test_writes_key_value_the_card_reads_and_prints_one_pass_line(self):
        code, out, _ = run(record_outcome.main, [
            "--workspace", str(self.ws), "--outcome", "completed",
            "--completions", "2", "--note", "tuning issue, not a feed defeat"])
        self.assertEqual(code, 0, out)
        self.assertEqual(out.count("PASS:"), 1)
        self.assertTrue(out.startswith("PASS: record_outcome outcome=completed completions=2"))
        text = (self.state / run_card.OUTCOME_FILE).read_text(encoding="utf-8")
        self.assertIn("outcome=completed\n", text)
        self.assertIn("completions=2\n", text)
        self.assertIn("note=tuning issue, not a feed defeat\n", text)
        self.assertIn("recorded_at=", text)
        outcome = run_card.Outcome(self.ws)
        self.assertIsNone(outcome.warning)
        self.assertEqual(outcome.outcome, "completed")
        self.assertEqual(outcome.completions, 2)
        self.assertEqual(outcome.label, "completed (tuning issue, not a feed defeat)")
        self.assertTrue(outcome.cost_label(200).startswith("100"))

    def test_completions_default_from_the_outcome_word(self):
        run(record_outcome.main, ["--workspace", str(self.ws), "--outcome", "completed"])
        self.assertEqual(run_card.Outcome(self.ws).completions, 1)
        run(record_outcome.main, ["--workspace", str(self.ws), "--outcome", "abandoned"])
        outcome = run_card.Outcome(self.ws)
        self.assertEqual(outcome.completions, 0)
        self.assertIn("infinite", outcome.cost_label(100))

    def test_escape_hatch_is_carried(self):
        run(record_outcome.main, ["--workspace", str(self.ws), "--outcome", "escalated",
                                  "--escape-hatch", "2"])
        self.assertEqual(run_card.Outcome(self.ws).escape_hatch_label, "2")

    def test_re_recording_replaces_rather_than_appends(self):
        run(record_outcome.main, ["--workspace", str(self.ws), "--outcome", "escalated"])
        run(record_outcome.main, ["--workspace", str(self.ws), "--outcome", "completed"])
        text = (self.state / run_card.OUTCOME_FILE).read_text(encoding="utf-8")
        self.assertEqual(text.count("outcome="), 1)
        self.assertEqual(run_card.Outcome(self.ws).outcome, "completed")

    def _refused(self, args):
        code, out, _ = run(record_outcome.main, ["--workspace", str(self.ws)] + args)
        self.assertEqual(code, 1, out)
        self.assertTrue(out.startswith("FAIL: record_outcome"), out)
        self.assertEqual(out.count("FAIL:"), 1)
        self.assertFalse((self.state / run_card.OUTCOME_FILE).exists(),
                         "a refused record must write nothing")
        return out

    def test_refuses_the_free_text_the_last_run_wrote(self):
        out = self._refused(["--outcome", "completed - user verdict: tuning issue"])
        self.assertIn("outcome must be one of completed, escalated, abandoned", out)

    def test_refuses_an_unknown_word_and_a_missing_one(self):
        self._refused(["--outcome", "done"])
        self._refused([])

    def test_refuses_a_completed_run_with_no_completions(self):
        out = self._refused(["--outcome", "completed", "--completions", "0"])
        self.assertIn("contradiction", out)

    def test_refuses_bad_counts(self):
        self._refused(["--outcome", "completed", "--completions", "two"])
        self._refused(["--outcome", "completed", "--completions", "-1"])
        self._refused(["--outcome", "completed", "--escape-hatch", "x"])

    def test_refuses_a_multi_line_note(self):
        self._refused(["--outcome", "completed", "--note", "line one\nline two"])

    def test_refuses_a_missing_workspace(self):
        code, out, _ = run(record_outcome.main, [
            "--workspace", str(self.ws / "nope"), "--outcome", "completed"])
        self.assertEqual(code, 1)
        self.assertIn("FAIL: record_outcome workspace is not a directory", out)


class TestRecordGate(RecordBase):
    def _record(self, *args):
        return run(record_gate.main, ["--workspace", str(self.ws)] + list(args))

    def test_appends_one_line_per_verdict_and_reads_them_back(self):
        code, out, _ = self._record("--gate", "1", "--verdict", "fixes",
                                    "--note", "notches in 1 of 4 patches; ports in yz")
        self.assertEqual(code, 0, out)
        self.assertEqual(out.count("PASS:"), 1)
        self.assertTrue(out.startswith("PASS: record_gate gate=1 verdict=fixes recorded=1"))
        code, out, _ = self._record("--gate", "1", "--verdict", "pass")
        self.assertEqual(code, 0, out)
        self.assertIn("recorded=2", out)
        code, out, _ = self._record("--gate", "2", "--verdict", "pass", "--note", "fed array")
        self.assertIn("recorded=3", out)
        path = record_gate.gate_path(self.ws)
        lines = path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 3)
        self.assertTrue(lines[0].startswith("ts="))
        self.assertIn(" gate=1 verdict=fixes note=notches in 1 of 4 patches; ports in yz",
                      lines[0])
        records = record_gate.read_gates(path)
        self.assertEqual([(r["gate"], r["verdict"]) for r in records],
                         [(1, "fixes"), (1, "pass"), (2, "pass")])
        self.assertEqual(records[0]["note"], "notches in 1 of 4 patches; ports in yz")
        self.assertEqual(records[1]["note"], "")
        self.assertLessEqual(records[0]["ts"], records[1]["ts"])
        self.assertLessEqual(records[1]["ts"], records[2]["ts"])

    def test_the_file_is_append_only(self):
        self._record("--gate", "1", "--verdict", "fixes", "--note", "first")
        before = record_gate.gate_path(self.ws).read_text(encoding="utf-8")
        self._record("--gate", "1", "--verdict", "pass")
        after = record_gate.gate_path(self.ws).read_text(encoding="utf-8")
        self.assertTrue(after.startswith(before))

    def _refused(self, args, expect):
        self._record("--gate", "1", "--verdict", "fixes")
        before = record_gate.gate_path(self.ws).read_text(encoding="utf-8")
        code, out, _ = self._record(*args)
        self.assertEqual(code, 1, out)
        self.assertTrue(out.startswith("FAIL: record_gate"), out)
        self.assertEqual(out.count("FAIL:"), 1)
        self.assertIn(expect, out)
        self.assertEqual(record_gate.gate_path(self.ws).read_text(encoding="utf-8"), before,
                         "a refused record must append nothing")

    def test_refuses_an_unknown_verdict(self):
        self._refused(["--gate", "1", "--verdict", "maybe"], "verdict must be one of pass, fixes")

    def test_refuses_a_bad_gate_number(self):
        self._refused(["--gate", "0", "--verdict", "pass"], "positive integer")
        self._refused(["--gate", "one", "--verdict", "pass"], "positive integer")
        self._refused(["--verdict", "pass"], "positive integer")

    def test_refuses_a_multi_line_note(self):
        self._refused(["--gate", "1", "--verdict", "pass", "--note", "a\nb"], "one line")

    def test_refuses_a_missing_workspace(self):
        code, out, _ = run(record_gate.main, [
            "--workspace", str(self.ws / "nope"), "--gate", "1", "--verdict", "pass"])
        self.assertEqual(code, 1)
        self.assertIn("workspace is not a directory", out)

    def test_a_torn_line_is_skipped_on_read(self):
        self._record("--gate", "1", "--verdict", "pass")
        with open(record_gate.gate_path(self.ws), "a", encoding="utf-8") as handle:
            handle.write("ts=17 gate=")
        self.assertEqual(len(record_gate.read_gates(record_gate.gate_path(self.ws))), 1)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: record tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
