"""Unit tests for scripts/run_trace.py (feature hfss-agent-run-logging,
ticket 04).

Both backends must produce the same `steps.jsonl` shape, count usage once
per request, and link subagents to their parent. Ground truth is the
captured corpus under scripts/fixtures/ (docs/agents/fixture-fidelity.md):

- `claude-code/f0c832a3-...jsonl`: a real Claude Code session with 15 tool
  calls and 8 thinking blocks, sliced by `claude_transcript.capture` with
  tool names, byte sizes and is_error kept;
- `claude-code/a0e9c38f-...` + its `subagents/`: a real session with two
  subagent transcripts (captured by another ticket's tree capture, content
  blocks not kept), used here for what it does hold: the on-disk layout,
  the parent link and the usage totals;
- `opencode/ses_fe9ae6dd3ffe2a8knbeE1b4yrr.jsonl`: the Aug 18 solve session
  `neon-eagle` (patch-array-5800) with its two subagents `cosmic-knight`
  and `hidden-falcon`, captured by `run_trace.capture_opencode`.

The one synthetic artifact, a SQLite database materialized FROM the real
opencode slice, exists so the database code path and the capture refusal
can run without the 11 GB store; a test asserts it traces identically to
the slice it came from (rule 3). Expected literals below (10 requests, 15
tool calls, 254 opencode calls, ...) were read off the real stores at
capture time.

Usage: python scripts/test_run_trace.py
"""

import contextlib
import io
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import claude_transcript  # noqa: E402
import run_trace  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"
CC_DIR = FIXTURES / "claude-code"
OC_DIR = FIXTURES / "opencode"
CC_SESSION = "f0c832a3-cb36-4168-ac07-70c2793c74a2"
CC_TRANSCRIPT = CC_DIR / f"{CC_SESSION}.jsonl"
CC_PARENT = "a0e9c38f-3117-4d93-8086-9b4f16ee0d52"
CC_PARENT_TRANSCRIPT = CC_DIR / f"{CC_PARENT}.jsonl"
CC_AGENTS = ("agent-a7c9f335c3a8f10e1", "agent-aee86fa4fd776a43f")
OC_SESSION = "ses_fe9ae6dd3ffe2a8knbeE1b4yrr"
OC_SLICE = OC_DIR / f"{OC_SESSION}.jsonl"
OC_CHILDREN = ("ses_fe964cc55ffeHbmOUhRVH9huBi", "ses_fe8c117fdffeX8Q8m5QQ6By5Cz")

TOKEN_KEYS = run_trace.TOKEN_KEYS


def cc_index():
    return json.loads((CC_DIR / claude_transcript.INDEX_FILE).read_text(encoding="utf-8"))


def oc_index():
    return json.loads((OC_DIR / run_trace.INDEX_FILE).read_text(encoding="utf-8"))


def card_tokens(card):
    return {k: card[k] for k in TOKEN_KEYS}


def step_tokens(steps):
    return {k: run_trace.totals(steps)[k] for k in TOKEN_KEYS}


# -- a database materialized from the real slice (synthetic, rule 3) --------

SCHEMA = """
CREATE TABLE project (id TEXT PRIMARY KEY, worktree TEXT NOT NULL);
CREATE TABLE session (
  id TEXT PRIMARY KEY, project_id TEXT NOT NULL, parent_id TEXT, slug TEXT NOT NULL,
  title TEXT NOT NULL, tokens_input INTEGER NOT NULL DEFAULT 0,
  tokens_output INTEGER NOT NULL DEFAULT 0, tokens_reasoning INTEGER NOT NULL DEFAULT 0,
  tokens_cache_read INTEGER NOT NULL DEFAULT 0, tokens_cache_write INTEGER NOT NULL DEFAULT 0,
  time_created INTEGER NOT NULL, time_updated INTEGER NOT NULL);
CREATE TABLE message (id TEXT PRIMARY KEY, session_id TEXT NOT NULL,
  time_created INTEGER NOT NULL, time_updated INTEGER NOT NULL, data TEXT NOT NULL);
CREATE TABLE part (id TEXT PRIMARY KEY, message_id TEXT NOT NULL, session_id TEXT NOT NULL,
  time_created INTEGER NOT NULL, time_updated INTEGER NOT NULL, data TEXT NOT NULL);
CREATE INDEX session_parent_idx ON session(parent_id);
CREATE INDEX message_session_idx ON message(session_id);
CREATE INDEX part_session_idx ON part(session_id);
"""


def inflate_input(size, command):
    """A tool input dict of exactly `size` JSON bytes whose command is `command`."""
    if command is None:
        if size == 2:
            return {}
        if size >= 8:
            return {"k": "x" * (size - 8)}
        raise ValueError(f"cannot inflate a {size}-byte input without a command")
    escaped = len(json.dumps(command, ensure_ascii=False).encode("utf-8")) - 2
    for key in claude_transcript.COMMAND_KEYS:
        if len(key) + 8 + escaped == size:
            return {key: command}
    pad = size - (24 + escaped)
    if pad >= 0:
        return {"command": command, "_": "x" * pad}
    raise ValueError(f"cannot inflate a {size}-byte input for {command!r}")


def inflate_part(data):
    ptype = data.get("type")
    if ptype in ("text", "reasoning"):
        out = {"type": ptype, "text": "x" * int(data.get("text_bytes") or 0)}
        if "time" in data:
            out["time"] = data["time"]
        return out
    if ptype == "tool":
        state = data.get("state") or {}
        full = {"status": state.get("status"),
                "input": inflate_input(int(state["input_bytes"]), state.get("command"))}
        if "output_bytes" in state:
            full["output"] = "x" * int(state["output_bytes"])
        if "time" in state:
            full["time"] = state["time"]
        return {"type": ptype, "tool": data.get("tool"), "callID": data.get("callID"),
                "state": full}
    return {"type": ptype}


def materialize_db(slice_path, db_path):
    """A SQLite database in the opencode shape, inflated from a slice."""
    store = run_trace.SliceStore(slice_path)
    con = sqlite3.connect(db_path)
    con.executescript(SCHEMA)
    con.execute("INSERT INTO project VALUES (?, ?)",
                ("prj", "C:/Users/me/Repos/HFSS_automation"))
    for sid, row in store._sessions.items():
        con.execute("INSERT INTO session VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (sid, "prj", row.get("parent_id"), row["slug"], row.get("title") or "",
                     row["tokens_input"], row["tokens_output"], row["tokens_reasoning"],
                     row["tokens_cache_read"], row["tokens_cache_write"],
                     row["time_created"], row["time_updated"]))
        for m in store.messages(sid):
            con.execute("INSERT INTO message VALUES (?,?,?,?,?)",
                        (m["id"], sid, m["time_created"], m["time_updated"],
                         json.dumps(m["data"])))
        for p in store.parts(sid):
            con.execute("INSERT INTO part VALUES (?,?,?,?,?,?)",
                        (p["id"], p["message_id"], sid, p["time_created"],
                         p["time_updated"], json.dumps(inflate_part(p["data"]))))
    con.commit()
    con.close()
    return db_path


def synthetic_transcript(session_id, agent_id=None):
    """A Claude Code transcript in the real fixture's shape: one request
    written as three assistant records sharing requestId and usage."""
    usage = {"input_tokens": 3, "output_tokens": 40, "cache_read_input_tokens": 500,
             "cache_creation_input_tokens": 20, "output_tokens_details": {"thinking_tokens": 7}}
    top = {"sessionId": session_id, "isSidechain": agent_id is not None}
    if agent_id:
        top["agentId"] = agent_id
    lines = [
        {"type": "ai-title", "aiTitle": "synthetic", "sessionId": session_id},
        dict(top, type="user", uuid="u0", timestamp="2026-08-15T00:00:01.000Z",
             message={"role": "user", "content": "hello"}),
        dict(top, type="assistant", uuid="a0", requestId="req_0",
             timestamp="2026-08-15T00:00:02.000Z",
             message={"id": "msg_0", "role": "assistant", "usage": usage,
                      "content": [{"type": "thinking", "thinking": "", "signature": "s"}]}),
        dict(top, type="assistant", uuid="a1", requestId="req_0",
             timestamp="2026-08-15T00:00:03.000Z",
             message={"id": "msg_0", "role": "assistant", "usage": usage,
                      "content": [{"type": "text", "text": "Running it."}]}),
        dict(top, type="assistant", uuid="a2", requestId="req_0",
             timestamp="2026-08-15T00:00:04.000Z",
             message={"id": "msg_0", "role": "assistant", "usage": usage,
                      "content": [{"type": "tool_use", "id": "toolu_1", "name": "Bash",
                                   "input": {"command": "ls -la", "timeout": 5}}]}),
        dict(top, type="user", uuid="u1", timestamp="2026-08-15T00:00:06.000Z",
             message={"role": "user", "content": [
                 {"type": "tool_result", "tool_use_id": "toolu_1",
                  "content": "total 0\n", "is_error": True}]}),
    ]
    return "\n".join(json.dumps(l) for l in lines) + "\n"


def run_main(argv):
    out = io.StringIO()
    err = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = run_trace.main(argv)
    return code, out.getvalue(), err.getvalue()


class TestCorpus(unittest.TestCase):
    def test_both_fixtures_are_present(self):
        self.assertTrue(CC_TRANSCRIPT.is_file(), CC_TRANSCRIPT)
        self.assertTrue(OC_SLICE.is_file(), OC_SLICE)
        self.assertIn(CC_SESSION, cc_index())
        self.assertIn(OC_SESSION, oc_index())
        for agent in CC_AGENTS:
            path = CC_DIR / CC_PARENT / claude_transcript.SUBAGENTS_DIR / f"{agent}.jsonl"
            self.assertTrue(path.is_file(), path)


class TestSchema(unittest.TestCase):
    """Both backends emit the same record shape."""

    def families(self):
        return [(run_trace.HOST_CLAUDE, run_trace.trace_claude(CC_TRANSCRIPT)),
                (run_trace.HOST_OPENCODE,
                 run_trace.trace_opencode_family(run_trace.SliceStore(OC_SLICE), OC_SESSION))]

    def test_every_step_has_exactly_the_schema_keys(self):
        for host, family in self.families():
            for sid, steps in family.items():
                self.assertTrue(steps, sid)
                for step in steps:
                    self.assertEqual(tuple(step), run_trace.STEP_KEYS)
                    self.assertEqual(step["host"], host)
                    self.assertEqual(step["session_id"], sid)
                    self.assertIn(step["kind"], run_trace.KINDS)
                    self.assertIn(step["role"], run_trace.ROLES)
                    self.assertIsInstance(step["ts"], int)
                    if step["kind"] == "tool_use":
                        self.assertIsInstance(step["tool"], str)
                        self.assertIsInstance(step["in_bytes"], int)
                        self.assertEqual(step["role"], "assistant")
                    if step["kind"] == "tool_result":
                        self.assertIsInstance(step["is_error"], bool)
                        self.assertEqual(step["role"], "tool_result")
                    if step["kind"] == "reasoning":
                        self.assertIsInstance(step["out_bytes"], int)

    def test_seq_and_latency_follow_ts_order(self):
        for _, family in self.families():
            for steps in family.values():
                for i, step in enumerate(steps):
                    self.assertEqual(step["seq"], i)
                    if i + 1 < len(steps):
                        self.assertLessEqual(step["ts"], steps[i + 1]["ts"])
                        self.assertEqual(step["latency_ms"], steps[i + 1]["ts"] - step["ts"])
                    else:
                        self.assertIsNone(step["latency_ms"])

    def test_tokens_sit_on_one_step_per_request(self):
        for _, family in self.families():
            for steps in family.values():
                seen = set()
                for step in steps:
                    has = step["tokens_input"] is not None
                    if has:
                        self.assertNotIn(step["request_id"], seen)
                        seen.add(step["request_id"])
                        for key in TOKEN_KEYS:
                            self.assertIsInstance(step[key], int)
                    else:
                        for key in TOKEN_KEYS:
                            self.assertIsNone(step[key])

    def test_results_join_their_calls(self):
        for _, family in self.families():
            for steps in family.values():
                calls = {s["tool_use_id"]: s for s in steps if s["kind"] == "tool_use"}
                for step in steps:
                    if step["kind"] == "tool_result":
                        self.assertIn(step["tool_use_id"], calls)
                        self.assertEqual(step["tool"], calls[step["tool_use_id"]]["tool"])
                        self.assertEqual(step["command"], calls[step["tool_use_id"]]["command"])


class TestClaudeCode(unittest.TestCase):
    def setUp(self):
        self.steps = run_trace.trace_transcript(CC_TRANSCRIPT)

    def test_usage_counted_once_per_request(self):
        # The real slice: 24 assistant records, 10 API requests (run_card's trap).
        self.assertEqual(run_trace.totals(self.steps)["requests"], 10)
        self.assertEqual(step_tokens(self.steps), card_tokens(cc_index()[CC_SESSION]["card"]))

    def test_tool_calls_results_and_errors(self):
        calls = [s for s in self.steps if s["kind"] == "tool_use"]
        results = [s for s in self.steps if s["kind"] == "tool_result"]
        self.assertEqual(len(calls), 15)
        self.assertEqual(len(results), 15)
        self.assertEqual({s["tool"] for s in calls}, {"Bash", "Read"})
        self.assertEqual(sum(1 for s in results if s["is_error"]), 1)
        self.assertTrue(all(s["command"] for s in calls))
        self.assertTrue(all(isinstance(s["out_bytes"], int) for s in results))

    def test_reasoning_blocks_are_steps(self):
        reasoning = [s for s in self.steps if s["kind"] == "reasoning"]
        self.assertEqual(len(reasoning), 8)
        # Claude Code stores thinking with an empty text on this host; the
        # cost is in tokens_reasoning, which the usage test above checks.
        self.assertTrue(all(s["out_bytes"] == 0 for s in reasoning))

    def test_user_prompt_is_a_text_step_with_in_bytes(self):
        first = self.steps[0]
        self.assertEqual((first["kind"], first["role"]), ("text", "user"))
        self.assertGreater(first["in_bytes"], 0)

    def test_subagents_link_to_parent_and_totals_agree_with_the_cards(self):
        family = run_trace.trace_claude(CC_PARENT_TRANSCRIPT)
        self.assertEqual(tuple(family), (CC_PARENT,) + CC_AGENTS)
        parent_card = cc_index()[CC_PARENT]["card"]
        agent_index = json.loads((CC_DIR / CC_PARENT / claude_transcript.SUBAGENTS_DIR
                                  / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(step_tokens(family[CC_PARENT]), card_tokens(parent_card))
        for agent in CC_AGENTS:
            steps = family[agent]
            self.assertTrue(all(s["parent_session_id"] == CC_PARENT for s in steps))
            self.assertEqual(step_tokens(steps),
                             card_tokens(agent_index[agent[len("agent-"):]]["card"]))
        self.assertTrue(all(s["parent_session_id"] is None for s in family[CC_PARENT]))
        with_agents = run_trace.family_totals(family)
        without = run_trace.totals(family[CC_PARENT])
        expected = parent_card["billed"] + sum(
            agent_index[a[len("agent-"):]]["card"]["billed"] for a in CC_AGENTS)
        self.assertEqual(without["billed"], parent_card["billed"])
        self.assertEqual(with_agents["billed"], expected)

    def test_no_subagents_where_none_exist(self):
        self.assertEqual(tuple(run_trace.trace_claude(CC_TRANSCRIPT)), (CC_SESSION,))


class TestOpencode(unittest.TestCase):
    def setUp(self):
        self.store = run_trace.SliceStore(OC_SLICE)
        self.family = run_trace.trace_opencode_family(self.store, OC_SESSION)

    def test_family_and_parent_links(self):
        self.assertEqual(tuple(self.family), (OC_SESSION,) + OC_CHILDREN)
        self.assertTrue(all(s["parent_session_id"] is None for s in self.family[OC_SESSION]))
        for child in OC_CHILDREN:
            self.assertTrue(all(s["parent_session_id"] == OC_SESSION
                                for s in self.family[child]))

    def test_totals_agree_with_the_run_card_per_session(self):
        entry = oc_index()[OC_SESSION]
        self.assertEqual(step_tokens(self.family[OC_SESSION]), card_tokens(entry["card"]))
        for child in OC_CHILDREN:
            self.assertEqual(step_tokens(self.family[child]),
                             card_tokens(entry["subagents"][child]))
        with_agents = run_trace.family_totals(self.family)["billed"]
        self.assertEqual(with_agents, entry["card"]["billed"]
                         + sum(c["billed"] for c in entry["subagents"].values()))
        self.assertEqual(run_trace.totals(self.family[OC_SESSION])["billed"],
                         entry["card"]["billed"])

    def test_usage_once_per_assistant_message(self):
        steps = self.family[OC_SESSION]
        assistant = [m for m in self.store.messages(OC_SESSION)
                     if m["data"].get("role") == "assistant"]
        self.assertEqual(run_trace.totals(steps)["requests"], len(assistant))
        self.assertEqual(len(assistant), 236)

    def test_every_tool_part_yields_a_call_and_a_result(self):
        steps = self.family[OC_SESSION]
        tool_parts = [p for p in self.store.parts(OC_SESSION) if p["data"]["type"] == "tool"]
        self.assertEqual(len(tool_parts), 254)
        self.assertEqual(sum(1 for s in steps if s["kind"] == "tool_use"), 254)
        self.assertEqual(sum(1 for s in steps if s["kind"] == "tool_result"), 254)
        self.assertEqual(sum(1 for s in steps if s["is_error"]), 4)
        self.assertEqual(sum(1 for s in steps if s["kind"] == "reasoning"), 151)
        self.assertEqual(oc_index()[OC_SESSION]["card"]["parts"],
                         len(self.store.parts(OC_SESSION)))

    def test_step_finish_parts_are_not_double_counted(self):
        # step-start / step-finish / patch rows exist in the slice but are not steps
        kinds = {p["data"]["type"] for p in self.store.parts(OC_SESSION)}
        self.assertIn("step-finish", kinds)
        self.assertNotIn("step-finish", {s["kind"] for s in self.family[OC_SESSION]})


class TestSyntheticDbMatchesRealSlice(unittest.TestCase):
    """Rule 3: the materialized database traces exactly like the real slice
    it was inflated from, so the database path and the capture refusal are
    tested against the real shape."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.db = materialize_db(OC_SLICE, os.path.join(self.tmp, "opencode.db"))
        self.store = run_trace.open_db(self.db)

    def test_database_traces_identically_to_the_slice(self):
        self.assertEqual(run_trace.trace_opencode_family(self.store, OC_SESSION),
                         run_trace.trace_opencode_family(run_trace.SliceStore(OC_SLICE),
                                                         OC_SESSION))

    def test_capture_reproduces_the_slice_rows(self):
        out = Path(self.tmp) / "out"
        target = run_trace.capture_opencode(self.store, OC_SESSION, out)
        real = [l for l in OC_SLICE.read_text(encoding="utf-8").splitlines()
                if '"table":"session"' not in l]
        mine = [l for l in target.read_text(encoding="utf-8").splitlines()
                if '"table":"session"' not in l]
        self.assertEqual(mine, real)
        index = json.loads((out / run_trace.INDEX_FILE).read_text(encoding="utf-8"))
        self.assertEqual(index[OC_SESSION]["card"]["billed"],
                         oc_index()[OC_SESSION]["card"]["billed"])
        self.assertEqual(set(index[OC_SESSION]["subagents"]), set(OC_CHILDREN))

    def test_capture_refuses_a_slice_that_traces_differently(self):
        original = run_trace.slice_part_data

        def broken(data):
            kept = original(data)
            if kept.get("type") == "tool":
                kept["state"].pop("output_bytes", None)
            return kept
        run_trace.slice_part_data = broken
        try:
            with self.assertRaises(ValueError):
                run_trace.capture_opencode(self.store, OC_SESSION, Path(self.tmp) / "bad")
        finally:
            run_trace.slice_part_data = original
        self.assertFalse((Path(self.tmp) / "bad" / f"{OC_SESSION}.jsonl").exists())

    def test_slug_lookup_is_scoped_to_the_project(self):
        self.assertEqual(self.store.find_slug("neon-eagle"), OC_SESSION)
        self.assertIsNone(self.store.find_slug("no-such-slug"))


class TestClaudeCapture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_real_slice_recaptures_to_itself(self):
        target = run_trace.capture_claude(CC_TRANSCRIPT, Path(self.tmp) / "out")
        self.assertEqual(target.read_text(encoding="utf-8"),
                         CC_TRANSCRIPT.read_text(encoding="utf-8"))

    def test_capture_refuses_a_slice_that_traces_differently(self):
        original = claude_transcript.slice_block

        def broken(block):
            kept = original(block)
            if kept.get("type") == "tool_use":
                kept["name"] = "Elsewhere"        # same card, different trace
            return kept
        src = Path(self.tmp) / "syn.jsonl"
        src.write_text(synthetic_transcript("syn"), encoding="utf-8")
        claude_transcript.slice_block = broken
        try:
            with self.assertRaises(ValueError):
                run_trace.capture_claude(src, Path(self.tmp) / "bad")
        finally:
            claude_transcript.slice_block = original
        self.assertFalse((Path(self.tmp) / "bad" / "syn.jsonl").exists())
        self.assertFalse((Path(self.tmp) / "bad" / run_trace.INDEX_FILE).exists())

    def test_synthetic_parses_like_the_real_shape(self):
        src = Path(self.tmp) / "syn.jsonl"
        src.write_text(synthetic_transcript("syn"), encoding="utf-8")
        steps = run_trace.trace_transcript(src)
        real = run_trace.trace_transcript(CC_TRANSCRIPT)
        self.assertEqual({tuple(s) for s in steps}, {tuple(s) for s in real})
        self.assertEqual([s["kind"] for s in steps],
                         ["text", "reasoning", "text", "tool_use", "tool_result"])
        self.assertEqual(run_trace.totals(steps)["requests"], 1)      # 3 records, 1 request
        self.assertEqual(run_trace.totals(steps)["tokens_reasoning"], 7)
        call, result = steps[3], steps[4]
        self.assertEqual(call["command"], "ls -la")
        self.assertEqual(call["in_bytes"], claude_transcript.byte_size(
            {"command": "ls -la", "timeout": 5}))
        self.assertTrue(result["is_error"])
        self.assertEqual(result["out_bytes"], len("total 0\n"))
        self.assertEqual(result["tool"], "Bash")
        # And the slice of it traces the same (the capture's own check).
        target = run_trace.capture_claude(src, Path(self.tmp) / "out")
        self.assertEqual(run_trace.trace_transcript(target), steps)

    def test_subagent_layout_is_captured_and_traced(self):
        src = Path(self.tmp) / "syn.jsonl"
        src.write_text(synthetic_transcript("syn"), encoding="utf-8")
        agents = Path(self.tmp) / "syn" / claude_transcript.SUBAGENTS_DIR
        agents.mkdir(parents=True)
        (agents / "agent-abc.jsonl").write_text(synthetic_transcript("syn", "abc"),
                                                encoding="utf-8")
        target = run_trace.capture_claude(src, Path(self.tmp) / "out")
        family = run_trace.trace_claude(target)
        self.assertEqual(tuple(family), ("syn", "agent-abc"))
        self.assertTrue(all(s["parent_session_id"] == "syn" for s in family["agent-abc"]))
        self.assertEqual(family, run_trace.trace_claude(src))
        index = json.loads((Path(self.tmp) / "out" / run_trace.INDEX_FILE).read_text())
        self.assertIn("agent-abc", index["syn"]["subagents"])


class TestCli(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.projects = Path(self.tmp) / "projects" / "C--Users-me-Repos-HFSS-automation"
        self.projects.mkdir(parents=True)
        shutil.copy(CC_TRANSCRIPT, self.projects / CC_TRANSCRIPT.name)
        self.db = materialize_db(OC_SLICE, os.path.join(self.tmp, "opencode.db"))
        self.workspace = Path(self.tmp) / "ws"
        (self.workspace / "results" / "state").mkdir(parents=True)

    def declare(self, rows):
        path = self.workspace / "results" / "state" / run_trace.SESSIONS_FILE
        path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")

    def test_host_of(self):
        self.assertEqual(run_trace.host_of("ses_abc"), "opencode")
        self.assertEqual(run_trace.host_of(CC_SESSION), "claude-code")
        self.assertEqual(run_trace.host_of("ses_abc", "claude-code"), "claude-code")

    def test_workspace_traces_every_declared_session_with_subagents(self):
        self.declare([
            {"ts": 1, "phase": "clarify", "name": "x-clarify", "host": "claude-code",
             "host_session_id": CC_SESSION},
            {"ts": 2, "phase": "build", "name": "x-build", "host": "opencode",
             "host_session_id": OC_SESSION},
            {"ts": 3, "phase": "build", "name": "x-build", "host": "opencode",
             "host_session_id": OC_SESSION},          # re-declared: traced once
        ])
        code, out, err = run_main(["--workspace", str(self.workspace),
                                   "--projects-dir", str(self.projects.parent),
                                   "--db", self.db])
        self.assertEqual(code, 0, err)
        self.assertIn("PASS: run_trace sessions=4", out)
        trace_dir = self.workspace / "results" / "state" / "trace"
        for sid in (CC_SESSION, OC_SESSION) + OC_CHILDREN:
            path = trace_dir / f"{sid}{run_trace.STEPS_SUFFIX}"
            self.assertTrue(path.is_file(), path)
        steps = run_trace.read_steps(trace_dir / f"{CC_SESSION}{run_trace.STEPS_SUFFIX}")
        self.assertEqual(steps, run_trace.trace_transcript(CC_TRANSCRIPT))
        self.assertEqual(len(run_trace.read_steps(
            trace_dir / f"{OC_SESSION}{run_trace.STEPS_SUFFIX}")), 908)

    def test_workspace_without_sessions_file_falls_back_to_session_json(self):
        (self.workspace / "results" / "state" / "session.json").write_text(
            json.dumps({"host": "claude-code", "host_session_id": CC_SESSION}),
            encoding="utf-8")
        code, out, _ = run_main(["--workspace", str(self.workspace),
                                 "--projects-dir", str(self.projects.parent)])
        self.assertEqual(code, 0)
        self.assertIn("sessions=1", out)

    def test_workspace_with_nothing_declared_fails_cleanly(self):
        code, _, err = run_main(["--workspace", str(self.workspace)])
        self.assertEqual(code, 1)
        self.assertIn(run_trace.SESSIONS_FILE, err)

    def test_top_reproduces_section_two_on_the_fixtures(self):
        code, out, _ = run_main(["--slice", str(OC_SLICE), "--top", "3", "--no-subagents"])
        self.assertEqual(code, 0)
        self.assertIn("tool calls: 254 -- bash 129, read 48, edit 44, write 23", out)
        self.assertIn("reasoning: 151 blocks, 531.7 KB", out)
        self.assertIn("59.2 KB", out)                      # the heaviest reasoning block
        self.assertNotIn(OC_CHILDREN[0], out)
        code, out, _ = run_main(["--transcript", str(CC_TRANSCRIPT), "--top", "3"])
        self.assertEqual(code, 0)
        self.assertIn("tool calls: 15 -- Bash 8, Read 7", out)
        self.assertIn("(1 errors)", out)

    def test_session_id_and_slug_select_the_opencode_family(self):
        out_dir = Path(self.tmp) / "out"
        code, out, err = run_main(["--session-id", OC_SESSION, "--db", self.db,
                                   "--out", str(out_dir)])
        self.assertEqual(code, 0, err)
        self.assertIn("sessions=3", out)
        code, out, err = run_main(["--slug", "neon-eagle", "--db", self.db,
                                   "--out", str(out_dir), "--no-subagents"])
        self.assertEqual(code, 0, err)
        self.assertIn("sessions=1", out)

    def test_missing_transcript_fails_cleanly(self):
        code, _, err = run_main(["--transcript", os.path.join(self.tmp, "nope.jsonl")])
        self.assertEqual(code, 1)
        self.assertIn("nope.jsonl", err)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    if result.wasSuccessful():
        print("PASS: run_trace tests=%d failed=0" % result.testsRun)
        raise SystemExit(0)
    print("FAIL: run_trace tests=%d failed=%d"
          % (result.testsRun, len(result.failures) + len(result.errors)))
    raise SystemExit(1)
