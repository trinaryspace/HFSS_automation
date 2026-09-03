"""Tier 0 tests for scripts/fixtures/backfill.py and capture_state.py (run
logging, ticket 10).

Ground truth, all real (docs/agents/fixture-fidelity.md):

- `scripts/fixtures/opencode/ses_fe9ae6dd3ffe2a8knbeE1b4yrr.jsonl` — the
  Aug 18 patch-array-5800 run (`neon-eagle`), whose seven `session.py
  --phase` calls are the instants the backfilled lines must carry.
- `scripts/fixtures/<workspace>/state/` — the captured machine state of the
  three backfilled workspaces; `sessions.jsonl` there is the backfill's
  committed copy and must equal what the script writes today.
- `scripts/fixtures/patch-array-5800/state/session.json` — the readout
  experiment's overwrite, whose `started_ms` is the eighth line's instant.

What is asserted: every line has ticket 01's keys plus `backfilled: true`;
`ts` is `ts_ms` in UTC; the seven Aug 18 lines are the trace's declaration
steps to the millisecond and in trace order, all in one opencode session;
the committed copies are reproducible and the script is byte-stable;
`hfss_spec.session.history` reads the lines like any other; `capture_state`
refuses a workspace without state and captures a real one byte for byte.

Run: `python scripts/test_backfill.py`
"""

import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
for entry in (str(REPO), str(REPO / "scripts"), str(REPO / "scripts" / "fixtures")):
    if entry not in sys.path:
        sys.path.insert(0, entry)

import backfill  # noqa: E402
import capture_state  # noqa: E402
import run_trace  # noqa: E402
from hfss_spec import painpoints, session as phase_session  # noqa: E402

FIXTURES = REPO / "scripts" / "fixtures"
OC_SLICE = FIXTURES / "opencode" / "ses_fe9ae6dd3ffe2a8knbeE1b4yrr.jsonl"
NEON = backfill.NEON
TICKET_01_KEYS = {"ts", "ts_ms", "phase", "name", "host", "host_session_id", "cwd", "worktree",
                  "skill_commit", "pid"}
BACKFILL_KEYS = TICKET_01_KEYS | {"backfilled", "backfill_source", "declared_by_run"}
# The seven declarations, by the seq of the `session.py --phase` call in
# the recaptured neon-eagle slice (hfss_spec/test_painpoints.py's hand count).
DECLARATION_SEQS = (149, 243, 473, 536, 652, 740, 822)


def neon_main_steps():
    family = run_trace.trace_opencode_family(run_trace.SliceStore(OC_SLICE), NEON)
    return family[NEON]


class TestFixturesArePresent(unittest.TestCase):
    def test_corpus(self):
        self.assertTrue(OC_SLICE.is_file())
        for name in backfill.RECORDS:
            self.assertTrue((FIXTURES / name / "state" / "sessions.jsonl").is_file(), name)
            self.assertTrue((FIXTURES / name / "backfill.json").is_file(), name)
            self.assertTrue((FIXTURES / name / "index.json").is_file(), name)


class TestLineShape(unittest.TestCase):
    def test_every_line_is_ticket_01s_plus_the_backfill_marks(self):
        for name, records in backfill.RECORDS.items():
            self.assertTrue(records, name)
            for record in records:
                self.assertEqual(set(record), BACKFILL_KEYS, name)
                self.assertIs(record["backfilled"], True)
                self.assertIn(record["declared_by_run"], (True, False))
                self.assertIn(record["phase"], phase_session.PHASES)
                self.assertIn(record["host"], (backfill.OPENCODE, backfill.CLAUDE))
                self.assertTrue(record["host_session_id"])
                self.assertTrue(record["backfill_source"])
                self.assertIsNone(record["pid"])
                iso = datetime.fromtimestamp(record["ts_ms"] / 1000.0, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                self.assertEqual(record["ts"], iso)

    def test_lines_are_sorted_key_json_one_per_line(self):
        for name in backfill.RECORDS:
            text = backfill.lines(name)
            self.assertTrue(text.endswith("\n"))
            self.assertNotIn("\r", text)
            for line in text.splitlines():
                self.assertEqual(line, json.dumps(json.loads(line), sort_keys=True))

    def test_history_reads_the_lines_like_the_runs_own(self):
        tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        for name in backfill.RECORDS:
            state = Path(tmp) / name
            state.mkdir()
            (state / "sessions.jsonl").write_text(backfill.lines(name), encoding="utf-8")
            records = phase_session.history(state)
            self.assertEqual(len(records), len(backfill.RECORDS[name]), name)
            self.assertEqual([r["phase"] for r in records], [r["phase"] for r in backfill.RECORDS[name]])
            self.assertTrue(all(r["backfilled"] for r in records))


class TestPatchArrayLinesAreTheTracesDeclarations(unittest.TestCase):
    def test_seven_aug_18_lines_are_the_declaration_steps_to_the_millisecond(self):
        steps = neon_main_steps()
        by_seq = {s["seq"]: s for s in steps}
        aug = [r for r in backfill.RECORDS["patch-array-5800"] if r["host_session_id"] == NEON]
        self.assertEqual(len(aug), 7)
        for record, seq in zip(aug, DECLARATION_SEQS):
            step = by_seq[seq]
            self.assertEqual(step["kind"], "tool_use")
            m = painpoints.DECLARE_RE.search(step["command"])
            self.assertIsNotNone(m, seq)
            self.assertEqual(record["phase"], m.group(1))
            self.assertEqual(record["name"], painpoints.DECLARE_NAME_RE.search(step["command"]).group(1))
            self.assertEqual(record["ts_ms"], step["ts"], seq)
            self.assertIn(f"seq {seq}:", record["backfill_source"])
            self.assertIs(record["declared_by_run"], True)
            self.assertEqual(record["skill_commit"], backfill.S7SIM_SKILL_COMMIT)
        self.assertEqual([r["ts_ms"] for r in aug], sorted(r["ts_ms"] for r in aug))

    def test_the_backfilled_history_attributes_exactly_as_the_trace_does(self):
        # The lines carry no information the trace lacks: attribution from
        # the history alone (commands blanked) equals attribution from the
        # trace's own declaration commands.
        steps = neon_main_steps()
        from_trace = painpoints.attribute([dict(s) for s in steps])
        blanked = [dict(s, command="") if painpoints.DECLARE_RE.search(s.get("command") or "") else dict(s)
                   for s in steps]
        history = [r for r in backfill.RECORDS["patch-array-5800"] if r["host_session_id"] == NEON]
        from_history = painpoints.attribute(blanked, [], history)
        self.assertEqual([(s["phase"], s["phase_index"]) for s in from_trace],
                         [(s["phase"], s["phase_index"]) for s in from_history])

    def test_the_eighth_line_is_the_readout_experiments_session_json(self):
        text = (FIXTURES / "patch-array-5800" / "state" / "session.json").read_text(encoding="utf-8-sig")
        current = json.loads(text)
        last = backfill.RECORDS["patch-array-5800"][-1]
        self.assertEqual((last["name"], last["phase"], last["ts_ms"]),
                         (current["name"], current["phase"], current["started_ms"]))
        self.assertEqual((last["host"], last["host_session_id"]), (backfill.CLAUDE, backfill.READOUT))
        # The file itself carries neither key, which is what the report classifies.
        self.assertFalse(current.get("host") or current.get("host_session_id"))

    def test_the_pilot_and_patch_2400_lines_are_not_the_runs_own(self):
        for name, sid in (("bowtie-3500-pilot", backfill.CANYON), ("patch-2400", backfill.ROCKET)):
            records = backfill.RECORDS[name]
            self.assertEqual([r["phase"] for r in records], ["clarify", "build", "solve"])
            self.assertTrue(all(r["host_session_id"] == sid and r["declared_by_run"] is False
                                and r["name"] == "" for r in records))


class TestBackfillScript(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.fixtures = Path(self.tmp) / "fixtures"
        self.workspaces = Path(self.tmp) / "workspaces"

    def test_committed_copies_are_what_the_script_writes(self):
        for name in backfill.RECORDS:
            text = backfill.lines(name)
            self.assertEqual((FIXTURES / name / "state" / "sessions.jsonl").read_bytes(), text.encode("utf-8"))
            index = json.loads((FIXTURES / name / "backfill.json").read_text(encoding="utf-8"))
            self.assertEqual(index["lines"], len(backfill.RECORDS[name]))
            self.assertEqual(index["sha256"], hashlib.sha256(text.encode("utf-8")).hexdigest())

    def test_writes_both_copies_byte_identical_and_is_byte_stable(self):
        (self.workspaces / "patch-2400").mkdir(parents=True)
        (self.fixtures / "patch-2400" / "state").mkdir(parents=True)
        (self.fixtures / "patch-2400" / "state" / "solved.txt").write_bytes(b"status=x\n")
        for name in backfill.RECORDS:
            (self.fixtures / name).mkdir(exist_ok=True)
        summary = backfill.backfill(str(self.workspaces), fixtures_root=str(self.fixtures))
        self.assertEqual(summary["patch-2400"], {"lines": 3, "materialized": ["solved.txt"]})
        self.assertEqual(summary["bowtie-3500-pilot"]["materialized"], [])   # no such workspace dir
        ws_copy = self.workspaces / "patch-2400" / "results" / "state" / "sessions.jsonl"
        fx_copy = self.fixtures / "patch-2400" / "state" / "sessions.jsonl"
        self.assertEqual(ws_copy.read_bytes(), fx_copy.read_bytes())
        self.assertEqual(ws_copy.read_bytes(), backfill.lines("patch-2400").encode("utf-8"))
        self.assertEqual((self.workspaces / "patch-2400" / "results" / "state" / "solved.txt").read_bytes(),
                         b"status=x\n")
        before = {p: p.read_bytes() for p in Path(self.tmp).rglob("*") if p.is_file()}
        mtimes = {p: p.stat().st_mtime_ns for p in before}
        summary = backfill.backfill(str(self.workspaces), fixtures_root=str(self.fixtures))
        self.assertEqual(summary["patch-2400"]["materialized"], [])           # never over an existing file
        after = {p: p.read_bytes() for p in Path(self.tmp).rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertEqual(mtimes[ws_copy], ws_copy.stat().st_mtime_ns)      # unchanged: not rewritten

    def test_never_overwrites_a_workspace_state_file(self):
        target = self.workspaces / "patch-2400" / "results" / "state"
        target.mkdir(parents=True)
        (target / "solved.txt").write_bytes(b"the workspace's own\n")
        (self.fixtures / "patch-2400" / "state").mkdir(parents=True)
        (self.fixtures / "patch-2400" / "state" / "solved.txt").write_bytes(b"captured\n")
        for name in backfill.RECORDS:
            (self.fixtures / name).mkdir(exist_ok=True)
        backfill.backfill(str(self.workspaces), fixtures_root=str(self.fixtures))
        self.assertEqual((target / "solved.txt").read_bytes(), b"the workspace's own\n")

    def test_summary_counts_every_workspace(self):
        # `main` writes into this checkout's fixture dir, so the throwaway
        # root drives `backfill` directly; the counts are the PASS line's.
        for name in backfill.RECORDS:
            (self.fixtures / name).mkdir(parents=True)
        summary = backfill.backfill(str(self.workspaces), fixtures_root=str(self.fixtures))
        parts = " ".join(f"{n}={s['lines']}" for n, s in summary.items())
        self.assertEqual(parts, "patch-array-5800=8 bowtie-3500-pilot=3 patch-2400=3")


class TestCaptureState(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_refuses_a_workspace_without_state(self):
        with self.assertRaises(SystemExit) as ctx:
            capture_state.capture("nope", self.tmp, out_root=self.tmp)
        self.assertIn("no results/state", str(ctx.exception))

    def test_captures_the_shipped_state_byte_for_byte_and_skips_the_tooling_files(self):
        # Round trip: a workspace built from the committed patch-2400 capture
        # captures back to the same bytes and the same index entries.
        src = Path(self.tmp) / "ws" / "results" / "state"
        src.mkdir(parents=True)
        for name in os.listdir(FIXTURES / "patch-2400" / "state"):
            shutil.copy(FIXTURES / "patch-2400" / "state" / name, src / name)
        (src / "events.jsonl").write_text("{}\n", encoding="utf-8")
        (src / "run.json").write_text("{}\n", encoding="utf-8")
        (src / "trace").mkdir()
        out = Path(self.tmp) / "out"
        index = capture_state.capture("patch-2400", str(src.parent.parent), out_root=str(out))
        shipped = json.loads((FIXTURES / "patch-2400" / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(index["files"], shipped["files"])
        self.assertNotIn("state/sessions.jsonl", index["files"])
        self.assertNotIn("state/events.jsonl", index["files"])
        for rel in index["files"]:
            self.assertEqual((out / "patch-2400" / rel).read_bytes(), (FIXTURES / "patch-2400" / rel).read_bytes())


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: backfill tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
