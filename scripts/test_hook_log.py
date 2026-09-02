"""Tests for scripts/hook_log.py, the hook install in scripts/install_skill.py
and the session map (feature hfss-agent-run-logging, ticket 08).

Ground truth is `scripts/fixtures/hooks/` (docs/agents/fixture-fidelity.md):
the four raw stdin payloads Claude Code 2.1.258 handed the hook during a
real headless session in this checkout (`echo hello`, then `exit 3`), kept
byte-for-byte by `hook_log.py --capture`, and the transcript of that same
session sliced by `run_trace.capture_claude`, so the hook lines and the
steps they must join come from one real run. Nothing here was typed from
memory: the field names (`tool_response`, not `tool_result`; a non-zero
exit arriving as `PostToolUseFailure` with `error: "Exit code 3"`; the
harness's own `duration_ms`) are asserted against those files.

Usage: python scripts/test_hook_log.py
"""

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO))
import hook_log  # noqa: E402
import install_skill  # noqa: E402
import run_trace  # noqa: E402
from hfss_spec import session as S  # noqa: E402

FIXTURES = HERE / "fixtures" / "hooks"
SESSION = "45641dd8-dbcc-4f08-8f92-90237c4a0f63"
TRANSCRIPT = FIXTURES / f"{SESSION}.jsonl"
OK_ID = "toolu_01UdH5CkY2L7G9fknFiuWwXg"          # echo hello
FAIL_ID = "toolu_01Wq4yd3xcssNi3976krgrPL"        # exit 3
PAYLOADS = (f"PreToolUse.{OK_ID}.json", f"PostToolUse.{OK_ID}.json",
            f"PreToolUse.{FAIL_ID}.json", f"PostToolUseFailure.{FAIL_ID}.json")
BUDGET_MS = 50


def raw(name):
    return (FIXTURES / name).read_bytes()


def payload(name):
    return json.loads(raw(name))


class Clock:
    """A clock the tests advance by hand."""

    def __init__(self, start=1_700_000_000_000):
        self.now = start

    def __call__(self):
        return self.now

    def tick(self, ms):
        self.now += ms


class HomeCase(unittest.TestCase):
    """A temp `HFSS_AGENT_HOME`, a workspace and a registered session."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.home = self.tmp / "home"
        self.env = {"HFSS_AGENT_HOME": str(self.home)}
        self.workspace = self.tmp / "ws"
        S.register_session(SESSION, self.workspace, "build", host="claude-code",
                           now_ms=1, environ=self.env)

    def handle(self, name, clock):
        return hook_log.handle(raw(name), environ=self.env, clock=clock)

    def lines(self):
        path = hook_log.log_path(str(self.workspace))
        if not os.path.exists(path):
            return []
        return [json.loads(l) for l in Path(path).read_text(encoding="utf-8").splitlines() if l]


class TestCorpus(unittest.TestCase):
    def test_the_real_payloads_and_transcript_are_present(self):
        for name in PAYLOADS:
            self.assertTrue((FIXTURES / name).is_file(), name)
        self.assertTrue(TRANSCRIPT.is_file(), TRANSCRIPT)
        index = json.loads((FIXTURES / run_trace.INDEX_FILE).read_text(encoding="utf-8"))
        self.assertIn(SESSION, index)

    def test_what_claude_code_actually_sends(self):
        """The contract, read off the captured files rather than the docs."""
        pre = payload(PAYLOADS[0])
        for key in ("session_id", "transcript_path", "cwd", "hook_event_name",
                    "tool_name", "tool_input", "tool_use_id"):
            self.assertIn(key, pre)
        self.assertEqual(pre["hook_event_name"], "PreToolUse")
        self.assertEqual(pre["session_id"], SESSION)
        self.assertEqual(pre["tool_input"]["command"], "echo hello")
        post = payload(PAYLOADS[1])
        self.assertEqual(post["hook_event_name"], "PostToolUse")
        self.assertIn("tool_response", post)
        self.assertNotIn("tool_result", post)
        self.assertEqual(set(post["tool_response"]),
                         {"stdout", "stderr", "interrupted", "isImage", "noOutputExpected"})
        self.assertIsInstance(post["duration_ms"], int)
        failure = payload(PAYLOADS[3])
        self.assertEqual(failure["hook_event_name"], "PostToolUseFailure")
        self.assertNotIn("tool_response", failure)
        self.assertEqual(failure["error"], "Exit code 3")
        self.assertFalse(failure["is_interrupt"])
        # The hook's cwd is the checkout the session ran in (a worktree here).
        self.assertTrue(pre["cwd"].replace("\\", "/").endswith("run-logging-plan"))

    def test_the_payloads_join_the_transcript(self):
        steps = run_trace.trace_transcript(TRANSCRIPT)
        uses = {s["tool_use_id"] for s in steps if s["kind"] == "tool_use"}
        self.assertEqual(uses, {OK_ID, FAIL_ID})
        self.assertEqual(steps[0]["session_id"], SESSION)


class TestLines(HomeCase):
    def test_pre_stamps_and_post_logs_one_line_per_call(self):
        clock = Clock()
        self.assertEqual(self.handle(PAYLOADS[0], clock), "stamped")
        self.assertEqual(self.lines(), [])
        clock.tick(3106)
        self.assertEqual(self.handle(PAYLOADS[1], clock), "logged")
        clock.tick(500)
        self.assertEqual(self.handle(PAYLOADS[2], clock), "stamped")
        clock.tick(332)
        self.assertEqual(self.handle(PAYLOADS[3], clock), "logged")
        ok, failed = self.lines()
        self.assertEqual(tuple(ok), hook_log.LINE_KEYS)
        self.assertEqual(ok, {
            "ts": clock.now - 832, "session_id": SESSION, "phase": "build",
            "tool": "Bash", "command": "echo hello", "exit_code": 0,
            "duration_ms": 3106, "exec_ms": 2884, "tool_use_id": OK_ID,
            "is_error": False})
        self.assertEqual(failed, {
            "ts": clock.now, "session_id": SESSION, "phase": "build",
            "tool": "Bash", "command": "exit 3", "exit_code": 3,
            "duration_ms": 332, "exec_ms": 96, "tool_use_id": FAIL_ID,
            "is_error": True})
        # The stamps are consumed.
        self.assertEqual(os.listdir(hook_log.pending_dir(self.env)), [])

    def test_a_post_without_its_pre_still_logs_with_no_duration(self):
        clock = Clock()
        self.assertEqual(self.handle(PAYLOADS[3], clock), "logged")
        (line,) = self.lines()
        self.assertIsNone(line["duration_ms"])
        self.assertEqual(line["exec_ms"], 96)
        self.assertEqual(line["exit_code"], 3)

    def test_the_phase_follows_a_redeclaration(self):
        S.register_session(SESSION, self.workspace, "solve", environ=self.env)
        self.handle(PAYLOADS[1], Clock())
        self.assertEqual(self.lines()[0]["phase"], "solve")

    def test_an_unregistered_session_logs_nothing(self):
        other = json.loads(raw(PAYLOADS[1]))
        other["session_id"] = "0000-not-a-run"
        self.assertEqual(hook_log.handle(json.dumps(other), environ=self.env, clock=Clock()),
                         "ignored")
        self.assertEqual(self.lines(), [])
        self.assertFalse(os.path.exists(hook_log.pending_dir(self.env)))

    def test_no_map_at_all_logs_nothing(self):
        env = {"HFSS_AGENT_HOME": str(self.tmp / "nowhere")}
        self.assertEqual(hook_log.handle(raw(PAYLOADS[1]), environ=env, clock=Clock()),
                         "ignored")

    def test_a_bare_string_entry_is_a_workspace(self):
        path = hook_log.sessions_map_path(self.env)
        Path(path).write_text(json.dumps({SESSION: str(self.workspace)}), encoding="utf-8")
        self.handle(PAYLOADS[1], Clock())
        (line,) = self.lines()
        self.assertIsNone(line["phase"])
        self.assertEqual(line["tool"], "Bash")

    def test_a_payload_without_tool_use_id_keys_the_stamp_by_tool(self):
        pre = payload(PAYLOADS[0])
        post = payload(PAYLOADS[1])
        del pre["tool_use_id"]
        del post["tool_use_id"]
        clock = Clock()
        hook_log.handle(json.dumps(pre), environ=self.env, clock=clock)
        self.assertEqual(os.listdir(hook_log.pending_dir(self.env)), [f"{SESSION}.Bash"])
        clock.tick(40)
        hook_log.handle(json.dumps(post), environ=self.env, clock=clock)
        (line,) = self.lines()
        self.assertEqual(line["duration_ms"], 40)
        self.assertIsNone(line["tool_use_id"])

    def test_other_tools_have_no_exit_code(self):
        post = payload(PAYLOADS[1])
        post.update(tool_name="Read", tool_input={"file_path": "C:/x/y.md"},
                    tool_response={"type": "text", "file": {"content": "..."}})
        hook_log.handle(json.dumps(post), environ=self.env, clock=Clock())
        (line,) = self.lines()
        self.assertEqual((line["tool"], line["command"], line["exit_code"], line["is_error"]),
                         ("Read", "C:/x/y.md", None, False))

    def test_a_failure_that_is_not_an_exit_code_is_still_an_error(self):
        failure = payload(PAYLOADS[3])
        failure["error"] = "Command timed out after 2m 0.0s"
        hook_log.handle(json.dumps(failure), environ=self.env, clock=Clock())
        (line,) = self.lines()
        self.assertIsNone(line["exit_code"])
        self.assertTrue(line["is_error"])

    def test_a_long_command_is_capped_not_parsed(self):
        post = payload(PAYLOADS[1])
        post["tool_input"] = {"command": "x" * 10_000}
        hook_log.handle(json.dumps(post), environ=self.env, clock=Clock())
        self.assertEqual(len(self.lines()[0]["command"]), hook_log.COMMAND_CHARS)


class TestMalformed(HomeCase):
    """Every bad input: exit 0, nothing written, and fast."""

    CASES = (
        b"", b"   ", b"{not json", b"[]", b"[1, 2]", b'"a string"', b"null", b"42",
        b"{}", b'{"session_id": 5}', b'{"session_id": "x"}',
        b'{"session_id": "x", "hook_event_name": "Stop"}',
        json.dumps({"session_id": SESSION, "hook_event_name": "PostToolUse"}).encode(),
        json.dumps({"session_id": SESSION, "hook_event_name": "PostToolUse",
                    "tool_name": 7, "tool_input": "nope", "tool_response": 3,
                    "duration_ms": "fast", "tool_use_id": ["x"]}).encode(),
        b"\xff\xfe\x00garbage", "{\"session_id\": \"\u00e9\"}".encode("utf-8"),
    )

    def test_every_malformed_input_is_handled_in_process_within_budget(self):
        for case in self.CASES:
            started = time.perf_counter()
            try:
                result = hook_log.handle(case, environ=self.env, clock=Clock())
            except Exception as exc:                      # noqa: BLE001
                self.fail(f"{case!r} raised {exc!r}")
            elapsed = (time.perf_counter() - started) * 1000
            self.assertLess(elapsed, BUDGET_MS, f"{case!r} took {elapsed:.1f} ms")
            self.assertIn(result, ("ignored", "logged", "stamped"), case)
        # The two dict cases with our session id are logged, the rest ignored.
        self.assertEqual(len(self.lines()), 2)
        for line in self.lines():
            self.assertEqual(tuple(line), hook_log.LINE_KEYS)

    def test_the_script_exits_zero_on_malformed_stdin(self):
        for case in (b"", b"{not json", b"[]", b"\xff\xfe"):
            proc = subprocess.run([sys.executable, "-I", "-S", str(HERE / "hook_log.py")],
                                  input=case, capture_output=True,
                                  env=dict(os.environ, **self.env), timeout=30)
            self.assertEqual(proc.returncode, 0, (case, proc.stderr))
            self.assertEqual(proc.stdout, b"")

    def test_main_never_raises_even_when_handle_does(self):
        original = hook_log.handle
        hook_log.handle = lambda raw: (_ for _ in ()).throw(RuntimeError("boom"))
        try:
            sys.stdin = io.TextIOWrapper(io.BytesIO(raw(PAYLOADS[1])))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(hook_log.main([]), 0)
        finally:
            hook_log.handle = original
            sys.stdin = sys.__stdin__

    def test_an_unwritable_workspace_is_unwritten_not_fatal(self):
        blocker = self.tmp / "ws" / "results"
        blocker.parent.mkdir(parents=True, exist_ok=True)
        blocker.write_text("a file where the dir should be", encoding="utf-8")
        result = hook_log.handle(raw(PAYLOADS[1]), environ=self.env, clock=Clock())
        self.assertEqual(result, "unwritten")


class TestBudget(HomeCase):
    """The in-process cost of a real Pre + Post pair, and the whole
    interpreter for information (Python's own start-up is ~30 ms here)."""

    def test_a_real_pair_is_handled_within_budget_in_process(self):
        clock = Clock()
        for name in (PAYLOADS[0], PAYLOADS[1]):
            started = time.perf_counter()
            self.handle(name, clock)
            elapsed = (time.perf_counter() - started) * 1000
            self.assertLess(elapsed, BUDGET_MS, f"{name} took {elapsed:.1f} ms")
        self.assertEqual(len(self.lines()), 1)

    def test_the_whole_process_timing_is_reported(self):
        env = dict(os.environ, **self.env)
        best = None
        for _ in range(3):
            started = time.perf_counter()
            proc = subprocess.run([sys.executable, "-I", "-S", str(HERE / "hook_log.py")],
                                  input=raw(PAYLOADS[1]), capture_output=True, env=env,
                                  timeout=30)
            elapsed = (time.perf_counter() - started) * 1000
            self.assertEqual(proc.returncode, 0, proc.stderr)
            best = elapsed if best is None else min(best, elapsed)
        print(f"  hook_log whole-process best of 3: {best:.0f} ms "
              f"(interpreter start-up included)", file=sys.stderr)
        self.assertLess(best, 1000)
        self.assertEqual(len(self.lines()), 3)


class TestCapture(HomeCase):
    def test_capture_keeps_the_raw_stdin_byte_for_byte(self):
        out = self.tmp / "cap"
        for name in PAYLOADS:
            hook_log.capture(raw(name), str(out))
        self.assertEqual(sorted(os.listdir(out)), sorted(PAYLOADS))
        for name in PAYLOADS:
            self.assertEqual((out / name).read_bytes(), raw(name))
        hook_log.capture(b"{not json", str(out))
        self.assertTrue(any(n.startswith("malformed.") for n in os.listdir(out)))

    def test_capture_flag_captures_and_still_logs(self):
        out = self.tmp / "cap"
        proc = subprocess.run([sys.executable, "-I", "-S", str(HERE / "hook_log.py"),
                               "--capture", str(out)], input=raw(PAYLOADS[1]),
                              capture_output=True, env=dict(os.environ, **self.env), timeout=30)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual((out / PAYLOADS[1]).read_bytes(), raw(PAYLOADS[1]))
        self.assertEqual(len(self.lines()), 1)


class TestSessionMap(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.env = {"HFSS_AGENT_HOME": str(self.tmp / "home")}

    def test_hook_and_session_agree_on_the_map_location(self):
        self.assertEqual(hook_log.sessions_map_path(self.env), S.sessions_map_path(self.env))
        self.assertEqual(hook_log.sessions_map_path({}), S.sessions_map_path({}))
        self.assertEqual(hook_log.ENV_HOME, S.ENV_AGENT_HOME)
        self.assertTrue(S.sessions_map_path({}).replace("\\", "/").endswith(
            "/.hfss-agent/sessions.json"))

    def test_session_cli_registers_the_declared_session(self):
        ws = self.tmp / "ws"
        env = dict(os.environ, **self.env)
        env.pop("CLAUDE_CODE_SESSION_ID", None)
        proc = subprocess.run([sys.executable, str(HERE / "session.py"), "--workspace", str(ws),
                               "--phase", "build", "--session-id", "sid-1", "--name", "t"],
                              capture_output=True, text=True, env=env, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("hook_map=registered", proc.stdout)
        data = json.loads(Path(S.sessions_map_path(self.env)).read_text(encoding="utf-8"))
        self.assertEqual(data["sid-1"]["phase"], "build")
        self.assertEqual(Path(data["sid-1"]["workspace"]).resolve(), ws.resolve())
        # Claude Code's exported id is picked up without --session-id.
        env["CLAUDE_CODE_SESSION_ID"] = "sid-env"
        proc = subprocess.run([sys.executable, str(HERE / "session.py"), "--workspace", str(ws),
                               "--phase", "solve"], capture_output=True, text=True, env=env,
                              timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(Path(S.sessions_map_path(self.env)).read_text(encoding="utf-8"))
        self.assertEqual(set(data), {"sid-1", "sid-env"})
        self.assertEqual(data["sid-env"]["host"], "claude-code")
        # No id: nothing to register, said so.
        env.pop("CLAUDE_CODE_SESSION_ID")
        proc = subprocess.run([sys.executable, str(HERE / "session.py"), "--workspace", str(ws),
                               "--phase", "solve"], capture_output=True, text=True, env=env,
                              timeout=60)
        self.assertIn("hook_map=unregistered", proc.stdout)
        self.assertEqual(set(json.loads(Path(S.sessions_map_path(self.env)).read_text(
            encoding="utf-8"))), {"sid-1", "sid-env"})


class TestInstall(unittest.TestCase):
    """The hooks are merged into settings.json, never clobbering it."""

    ORIGINAL = {
        "permissions": {"allow": ["Bash(python scripts/*)", "Bash(git status*)"]},
        "hooks": {"PostToolUse": [{"matcher": "Write|Edit",
                                   "hooks": [{"type": "command", "command": "prettier"}]}],
                  "Stop": [{"hooks": [{"type": "command", "command": "say done"}]}]},
        "env": {"X": "1"},
    }

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.path = self.tmp / ".claude" / "settings.json"
        self.path.parent.mkdir(parents=True)
        self.path.write_text(json.dumps(self.ORIGINAL, indent=2), encoding="utf-8")

    def read(self):
        return json.loads(self.path.read_text(encoding="utf-8"))

    def test_install_merges_and_remove_restores(self):
        self.assertEqual(install_skill.hooks_status(self.path)[0], False)
        ok, detail = install_skill.install_hooks(self.path)
        self.assertTrue(ok, detail)
        merged = self.read()
        self.assertEqual(merged["permissions"], self.ORIGINAL["permissions"])
        self.assertEqual(merged["env"], self.ORIGINAL["env"])
        self.assertEqual(merged["hooks"]["Stop"], self.ORIGINAL["hooks"]["Stop"])
        self.assertEqual(merged["hooks"]["PostToolUse"][0],
                         self.ORIGINAL["hooks"]["PostToolUse"][0])   # prettier kept, first
        for event in install_skill.HOOK_EVENTS:
            ours = [e for e in merged["hooks"][event]
                    if install_skill.HOOK_SCRIPT in e["hooks"][0]["command"]]
            self.assertEqual(len(ours), 1, event)
            self.assertEqual(ours[0]["matcher"], "*")
            self.assertEqual(ours[0]["hooks"][0]["timeout"], install_skill.HOOK_TIMEOUT_S)
        self.assertEqual(install_skill.hooks_status(self.path)[0], True)
        # Idempotent.
        before = self.path.read_bytes()
        self.assertEqual(install_skill.install_hooks(self.path), (True, "already installed"))
        self.assertEqual(self.path.read_bytes(), before)
        # Removal gives the original back, key for key.
        removed, _ = install_skill.remove_hooks(self.path)
        self.assertTrue(removed)
        self.assertEqual(self.read(), self.ORIGINAL)
        self.assertEqual(install_skill.remove_hooks(self.path)[0], False)

    def test_a_settings_file_with_no_hooks_block_gets_one_and_loses_it(self):
        self.path.write_text(json.dumps({"permissions": {"allow": ["Bash(rg *)"]}}),
                             encoding="utf-8")
        install_skill.install_hooks(self.path)
        self.assertEqual(set(self.read()), {"permissions", "hooks"})
        install_skill.remove_hooks(self.path)
        self.assertEqual(self.read(), {"permissions": {"allow": ["Bash(rg *)"]}})

    def test_a_missing_file_is_created_and_a_broken_one_refused(self):
        self.path.unlink()
        ok, _ = install_skill.install_hooks(self.path)
        self.assertTrue(ok)
        self.assertEqual(set(self.read()), {"hooks"})
        self.path.write_text("{broken", encoding="utf-8")
        ok, detail = install_skill.install_hooks(self.path)
        self.assertFalse(ok)
        self.assertIn("cannot read", detail)
        self.assertEqual(self.path.read_text(encoding="utf-8"), "{broken")

    def test_the_command_never_blocks_a_call_and_reaches_the_script(self):
        command = install_skill.HOOK_COMMAND
        self.assertIn("-I -S", command)
        self.assertIn("${CLAUDE_PROJECT_DIR}/" + install_skill.HOOK_SCRIPT, command)
        self.assertTrue(command.endswith("|| exit 0"))     # exit 2 would block the tool
        self.assertTrue((REPO / install_skill.HOOK_SCRIPT).is_file())

    def test_the_repo_settings_carry_the_hooks(self):
        state, detail = install_skill.hooks_status()
        self.assertTrue(state, detail)
        settings, _ = install_skill.read_settings()
        self.assertIn("Bash(python scripts/*)", settings["permissions"]["allow"])


class TestMerge(unittest.TestCase):
    """`run_trace.merge_tool_log` on the real transcript and real hook lines."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.env = {"HFSS_AGENT_HOME": str(self.tmp / "home")}
        self.workspace = self.tmp / "ws"
        S.register_session(SESSION, self.workspace, "build", environ=self.env)
        clock = Clock()
        for name, gap in zip(PAYLOADS, (0, 3106, 500, 332)):
            clock.tick(gap)
            hook_log.handle(raw(name), environ=self.env, clock=clock)
        self.tools = Path(hook_log.log_path(str(self.workspace)))
        self.entries = run_trace.read_tool_log(self.tools)

    def test_lines_join_the_calls_by_tool_use_id(self):
        steps = run_trace.trace_transcript(TRANSCRIPT)
        before = {s["tool_use_id"]: (s["latency_ms"], s["is_error"]) for s in steps
                  if s["kind"] == "tool_use"}
        self.assertEqual(run_trace.merge_tool_log(steps, self.entries), 2)
        uses = {s["tool_use_id"]: s for s in steps if s["kind"] == "tool_use"}
        results = {s["tool_use_id"]: s for s in steps if s["kind"] == "tool_result"}
        self.assertEqual(uses[OK_ID]["latency_ms"], 3106)
        self.assertEqual(uses[FAIL_ID]["latency_ms"], 332)
        self.assertFalse(results[OK_ID]["is_error"])
        self.assertTrue(results[FAIL_ID]["is_error"])
        self.assertNotEqual(before[OK_ID][0], None)
        for step in steps:                              # no key added or lost
            self.assertEqual(tuple(step), run_trace.STEP_KEYS)

    def test_the_hook_exit_code_beats_the_harness_flag(self):
        steps = run_trace.trace_transcript(TRANSCRIPT)
        entries = [dict(e) for e in self.entries]
        for e in entries:
            e["exit_code"] = 0 if e["tool_use_id"] == FAIL_ID else 1
        run_trace.merge_tool_log(steps, entries)
        results = {s["tool_use_id"]: s for s in steps if s["kind"] == "tool_result"}
        self.assertTrue(results[OK_ID]["is_error"])
        self.assertFalse(results[FAIL_ID]["is_error"])

    def test_a_line_without_an_id_joins_by_session_tool_and_command_once(self):
        steps = run_trace.trace_transcript(TRANSCRIPT)
        entries = [dict(e, tool_use_id=None) for e in self.entries] + [
            dict(self.entries[0], tool_use_id=None, duration_ms=9)]     # a third, unmatched
        self.assertEqual(run_trace.merge_tool_log(steps, entries), 2)
        uses = {s["tool_use_id"]: s for s in steps if s["kind"] == "tool_use"}
        self.assertEqual(uses[OK_ID]["latency_ms"], 3106)

    def test_lines_that_say_nothing_change_nothing(self):
        steps = run_trace.trace_transcript(TRANSCRIPT)
        original = [dict(s) for s in steps]
        self.assertEqual(run_trace.merge_tool_log(steps, []), 0)
        self.assertEqual(run_trace.merge_tool_log(
            steps, [{"tool": "Bash", "tool_use_id": "toolu_unknown", "exit_code": 9}]), 0)
        self.assertEqual(steps, original)
        self.assertEqual(run_trace.read_tool_log(self.tmp / "absent.jsonl"), [])

    def test_a_torn_line_is_skipped(self):
        with open(self.tools, "a", encoding="utf-8") as fh:
            fh.write('{"tool": "Bash", "tool_use_id": "tru')
        self.assertEqual(len(run_trace.read_tool_log(self.tools)), 2)

    def test_the_cli_merges_the_workspace_log(self):
        state = self.workspace / "results" / "state"
        (state / run_trace.SESSIONS_FILE).write_text(json.dumps(
            {"ts": 1, "phase": "build", "name": "x", "host": "claude-code",
             "host_session_id": SESSION}) + "\n", encoding="utf-8")
        projects = self.tmp / "projects" / "C--Users-me-Repos-HFSS-automation"
        projects.mkdir(parents=True)
        shutil.copy(TRANSCRIPT, projects / TRANSCRIPT.name)
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = run_trace.main(["--workspace", str(self.workspace),
                                   "--projects-dir", str(projects.parent)])
        self.assertEqual(code, 0, out.getvalue())
        self.assertIn("hooked=2", out.getvalue())
        steps = run_trace.read_steps(state / "trace" / f"{SESSION}{run_trace.STEPS_SUFFIX}")
        uses = {s["tool_use_id"]: s for s in steps if s["kind"] == "tool_use"}
        self.assertEqual(uses[OK_ID]["latency_ms"], 3106)
        # Without the log: nothing hooked, same steps otherwise.
        self.tools.unlink()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            run_trace.main(["--workspace", str(self.workspace),
                            "--projects-dir", str(projects.parent)])
        self.assertIn("hooked=0", out.getvalue())


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: hook_log tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
