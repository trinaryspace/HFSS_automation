"""Step trace extractor over both harness session stores (run-logging, 04).

Every number in docs/hfss-agent-performance-analysis.md section 2 (which
parts were reasoning, which tool outputs sat in context, how many calls of
which tool) was measured with throwaway probes over the harness stores.
This is the checked-in version: it reads either store and writes one
`steps.jsonl` per session, one record per step, in one host-neutral shape,
so the pain-point classifiers never touch a store.

The step record (every key present, None where not applicable):

    ts                  epoch ms of the step
    session_id          the session the step belongs to (a subagent's own id)
    host                "claude-code" | "opencode"
    parent_session_id   the spawning session for a subagent, else None
    seq                 0-based position within the session, in ts order
    role                "user" | "assistant" | "tool_result"
    kind                "text" | "reasoning" | "tool_use" | "tool_result"
    tool                tool name (on the tool_use and copied onto its result)
    tool_use_id         the call id joining a tool_use to its tool_result
    command             the bash command / file path / pattern / agent prompt
                        the call acted on, whole (capped at
                        claude_transcript.COMMAND_CHARS = 8192; copied onto
                        the result too)
    input_head          tool_use of an edit / write only: the first
                        HEAD_CHARS (2048) of the content written, or
                        {"old", "new"} heads of an edit's two strings;
                        None on every other step
    in_bytes            bytes handed in: a tool call's input, a user's text
    out_bytes           bytes produced: a tool's output, the model's text or
                        reasoning
    output_head         tool_result only: the first HEAD_CHARS of the
                        result's text (the error text when the call failed
                        with no output); None elsewhere
    is_error            tool_result only: the harness flagged the call failed
    request_id          the API request (Claude Code requestId / opencode
                        assistant message id) the step was generated in
    tokens_input, tokens_output, tokens_cache_read, tokens_cache_write,
    tokens_reasoning    set on the FIRST step of a request, None on the
                        rest, so summing a column gives the session's usage
    latency_ms          ts of the next step in the session minus this ts;
                        None on the last step

Byte sizes are UTF-8 lengths of the text, or of the JSON of a non-text
value (`claude_transcript.byte_size`). Steps are sorted by ts (stable),
and `seq` / `latency_ms` follow that order.

Claude Code (`~/.claude/projects/<encoded cwd>/<session-id>.jsonl`):

- `assistant` records: one per content block, all blocks of one API
  response sharing a `requestId` and the same `message.usage`. `thinking`
  -> reasoning (out_bytes = the thinking's size -- 0 on this host, where
  Claude Code writes the block with an empty text and only its signature,
  so `tokens_reasoning` is the measure of reasoning there), `text` ->
  text, `tool_use` (`id`, `name`, `input`) -> tool_use (in_bytes = the
  input's JSON size). Usage is taken ONCE per requestId -- the
  multi-record trap `claude_transcript.py` documents -- keyed exactly as
  `load_card` keys it, and lands on the request's first step. The records
  of one request do not all carry the same usage: on 2.1.258 the early
  ones hold a running count and the LAST holds the final numbers (the
  a0e9c38f fixture shows output 36 -> 2356 within one request), so the
  last record's usage wins, as in `load_card`.
- `user` records: `tool_result` blocks (`tool_use_id`, `content`,
  `is_error`) -> tool_result with role tool_result (output_head = the head
  of the content string, or of its `text` blocks joined); text blocks or a
  plain string content -> text with role user.
- every other record type (attachment, mode, system, titles, file-history)
  is bookkeeping, not a step.
- subagents: `<session-id>/subagents/agent-<id>.jsonl` beside the file.
  Their records carry the parent's `sessionId`, an `agentId` and
  `isSidechain: true`; they are traced as session `agent-<id>` (the file
  stem, one level deep as on disk today) with `parent_session_id` = the
  parent.
- a fixture slice from `claude_transcript.capture` carries `*_bytes` in
  place of content and traces identically; `capture_claude` refuses one
  that does not.

opencode (`~/.local/share/opencode/opencode.db`, opened read-only through
`run_card.connect`; every query is per session id and indexed, so the
11 GB `part` table is never scanned):

- `message` rows (`data` JSON): `role`, `time.created` and, on assistant
  messages, `tokens {input, output, reasoning, cache {read, write}}` --
  the usage, one per assistant message, summing to the `session` row's
  totals (the `step-finish` parts repeat the same numbers and are not
  counted). request_id = the message id.
- `part` rows (`data` JSON, keyed by `type`): `text` -> text (role from
  its message), `reasoning` -> reasoning, `tool` -> TWO steps: a tool_use
  at the part row's `time_created` (`tool`, `callID`, in_bytes =
  `state.input`'s JSON size, command and input_head from the input) and,
  once `state.status` is completed or error, a tool_result at
  `state.time.end` (out_bytes = the size of `state.output`, or of
  `state.error` when the output is null, output_head = its head, is_error
  = status == "error"). The row's `time_created` is when the model emitted
  the call; `state.time.start` is written when the call completes, ~30 ms
  before `state.time.end` (the `Start-Sleep -Seconds 240` call in
  neon-eagle reads 32 ms start-to-end and 241 s created-to-end), so a
  call's wall is only real from `time_created`. `step-start`,
  `step-finish`, `patch` and the like are not steps. A text or reasoning
  part's ts is its `time.start`, else the row's time_created.
- a message with usage but no step (an aborted turn) gets one empty text
  step so its tokens are never dropped.
- subagents: `session.parent_id` (the `task` tool's `state.metadata`
  names the same child `sessionId`), followed recursively.
- fixture slices (`capture_opencode`, `scripts/fixtures/opencode/`): one
  JSONL of the family's session / message / part rows with content
  replaced by sizes and heads (`text_bytes`; `input_bytes` + `command` +
  `input_head`; `output_bytes` + `output_head`), read back by
  `SliceStore`, and written only if it traces identically to the database.

Usage:
    python scripts/run_trace.py --workspace W [--out DIR]
        # every session in results/state/sessions.jsonl (ticket 01), with
        # subagents, to W/results/state/trace/<session-id>.steps.jsonl
    python scripts/run_trace.py --session-id ID [--host H] [--out DIR]
    python scripts/run_trace.py --slug SLUG [--host H] [--out DIR]
    python scripts/run_trace.py --transcript PATH.jsonl [--out DIR]
    python scripts/run_trace.py --slice PATH.jsonl [--out DIR]  # opencode fixture
    python scripts/run_trace.py ... --top N     # print the N heaviest tool
        # outputs and reasoning blocks (analysis doc section 2), write nothing
    python scripts/run_trace.py --capture ID --out DIR   # verified fixture slice

A session id starting with `ses_` is opencode; anything else is Claude Code
unless --host says otherwise. Stdlib only, Python 3.10 compatible.
"""

import argparse
import json
import os
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import claude_transcript  # noqa: E402
import run_card  # noqa: E402

HOST_CLAUDE = claude_transcript.HOST
HOST_OPENCODE = run_card.HOST_OPENCODE
HOSTS = (HOST_OPENCODE, HOST_CLAUDE)

STEP_KEYS = ("ts", "session_id", "host", "parent_session_id", "seq", "role",
             "kind", "tool", "tool_use_id", "command", "input_head", "in_bytes",
             "out_bytes", "output_head", "is_error", "request_id", "tokens_input",
             "tokens_output", "tokens_cache_read", "tokens_cache_write",
             "tokens_reasoning", "latency_ms")
COMMAND_CHARS = claude_transcript.COMMAND_CHARS
HEAD_CHARS = claude_transcript.HEAD_CHARS
TOKEN_KEYS = ("tokens_input", "tokens_output", "tokens_cache_read",
              "tokens_cache_write", "tokens_reasoning")
KINDS = ("text", "reasoning", "tool_use", "tool_result")
ROLES = ("user", "assistant", "tool_result")
ROLE_TOOL_RESULT = "tool_result"

SESSIONS_FILE = "sessions.jsonl"          # ticket 01, results/state/
TRACE_DIR = os.path.join("results", "state", "trace")
STEPS_SUFFIX = ".steps.jsonl"
INDEX_FILE = claude_transcript.INDEX_FILE
CARD_KEYS = claude_transcript.CARD_KEYS
OPENCODE_ID_PREFIX = "ses_"
FINISHED_STATUSES = ("completed", "error")
STEP_PART_TYPES = ("text", "reasoning", "tool")
KB = 1024.0

byte_size = claude_transcript.byte_size
command_of = claude_transcript.command_of
head_of = claude_transcript.head_of
input_head_of = claude_transcript.input_head_of
result_text = claude_transcript.result_text


def _step(**fields):
    step = dict.fromkeys(STEP_KEYS)
    step.update(fields)
    return step


def _usage(tokens_input, tokens_output, cache_read, cache_write, reasoning):
    return {"tokens_input": int(tokens_input or 0),
            "tokens_output": int(tokens_output or 0),
            "tokens_cache_read": int(cache_read or 0),
            "tokens_cache_write": int(cache_write or 0),
            "tokens_reasoning": int(reasoning or 0)}


def _finish(steps):
    """Order by ts (stable), then number the steps and fill latency_ms."""
    steps.sort(key=lambda s: -1 if s["ts"] is None else s["ts"])
    for i, step in enumerate(steps):
        step["seq"] = i
        nxt = steps[i + 1]["ts"] if i + 1 < len(steps) else None
        step["latency_ms"] = (None if nxt is None or step["ts"] is None
                              else nxt - step["ts"])
    return steps


def totals(steps):
    """Summed usage over the steps, plus the request and step counts."""
    out = dict.fromkeys(TOKEN_KEYS, 0)
    requests = 0
    for step in steps:
        if step["tokens_input"] is None:
            continue
        requests += 1
        for key in TOKEN_KEYS:
            out[key] += step[key]
    out["billed"] = out["tokens_input"] + out["tokens_output"]
    out["requests"] = requests
    out["steps"] = len(steps)
    return out


def family_totals(family):
    """`totals` over every session of a `{session_id: steps}` family."""
    return totals([s for steps in family.values() for s in steps])


# -- Claude Code -------------------------------------------------------------

def _size(block, key):
    """A block's content size, from the content or from a slice's `*_bytes`."""
    if key in block:
        return byte_size(block[key])
    value = block.get(key + "_bytes")
    return int(value) if value is not None else None


def _block_steps(block, rtype, base, tools):
    """The step for one content block; None for a block that is not one."""
    if not isinstance(block, dict):
        return _step(kind="text", role=rtype, in_bytes=byte_size(block), **base)
    btype = block.get("type")
    if btype == "thinking":
        return _step(kind="reasoning", role="assistant",
                     out_bytes=_size(block, "thinking"), **base)
    if btype == "text":
        size = _size(block, "text")
        if rtype == "assistant":
            return _step(kind="text", role="assistant", out_bytes=size, **base)
        return _step(kind="text", role="user", in_bytes=size, **base)
    if btype == "tool_use":
        if "input" in block:
            command = command_of(block.get("input"))
            input_head = input_head_of(block.get("input"))
        else:                                   # a slice: already reduced
            command = block.get("command")
            input_head = block.get("input_head")
        tools[block.get("id")] = (block.get("name"), command)
        return _step(kind="tool_use", role="assistant", tool=block.get("name"),
                     tool_use_id=block.get("id"), command=command,
                     input_head=input_head, in_bytes=_size(block, "input"), **base)
    if btype == "tool_result":
        tool, command = tools.get(block.get("tool_use_id"), (None, None))
        head = (head_of(result_text(block.get("content"))) if "content" in block
                else block.get("content_head"))
        return _step(kind="tool_result", role=ROLE_TOOL_RESULT, tool=tool,
                     tool_use_id=block.get("tool_use_id"), command=command,
                     out_bytes=_size(block, "content"), output_head=head,
                     is_error=bool(block.get("is_error", False)), **base)
    return None


def claude_session_id(path):
    """The session id a transcript names, else its file stem."""
    for record in claude_transcript._records(path):
        if record.get("sessionId"):
            return record["sessionId"]
    return Path(path).stem


def trace_transcript(path, session_id=None, parent_session_id=None):
    """The steps of one Claude Code transcript (main or subagent)."""
    path = Path(path)
    session_id = session_id or claude_session_id(path)
    steps = []
    first_of_request = {}
    tools = {}
    for index, record in enumerate(claude_transcript._records(path)):
        rtype = record.get("type")
        if rtype not in claude_transcript.PART_TYPES:
            continue
        message = record.get("message") if isinstance(record.get("message"), dict) else {}
        request_id = record.get("requestId") if rtype == "assistant" else None
        base = {"ts": claude_transcript._iso_to_ms(record.get("timestamp")),
                "session_id": session_id, "host": HOST_CLAUDE,
                "parent_session_id": parent_session_id, "request_id": request_id}
        new = []
        content = message.get("content")
        if isinstance(content, list):
            for block in content:
                step = _block_steps(block, rtype, base, tools)
                if step is not None:
                    new.append(step)
        elif isinstance(content, str) or "content_bytes" in message:
            size = (byte_size(content) if isinstance(content, str)
                    else int(message["content_bytes"]))
            if rtype == "assistant":
                new.append(_step(kind="text", role="assistant", out_bytes=size, **base))
            else:
                new.append(_step(kind="text", role="user", in_bytes=size, **base))
        usage = claude_transcript._usage_of(record) if rtype == "assistant" else None
        if usage is not None:
            key = request_id or message.get("id") or f"record-{index}"
            if key not in first_of_request:
                if not new:
                    new.append(_step(kind="text", role="assistant", out_bytes=0, **base))
                first_of_request[key] = new[0]
            details = usage.get("output_tokens_details")
            thinking = details.get("thinking_tokens") if isinstance(details, dict) else 0
            # The last record of a request carries its final usage (earlier
            # ones hold the running count); overwrite, as load_card does.
            first_of_request[key].update(
                _usage(usage.get("input_tokens"), usage.get("output_tokens"),
                       usage.get("cache_read_input_tokens"),
                       usage.get("cache_creation_input_tokens"), thinking))
        steps.extend(new)
    return _finish(steps)


def trace_claude(path, subagents=True):
    """`{session_id: steps}` for a transcript and (by default) its subagents,
    the parent first."""
    path = Path(path)
    parent_id = claude_session_id(path)
    family = {parent_id: trace_transcript(path, parent_id)}
    if subagents:
        for agent in claude_transcript.subagent_transcripts(path):
            family[agent.stem] = trace_transcript(agent, agent.stem,
                                                  parent_session_id=parent_id)
    return family


def capture_claude(source, out_dir):
    """`claude_transcript.capture`, refusing a slice that traces differently."""
    def verify(src, target):
        if trace_claude(src) != trace_claude(target):
            raise ValueError("slice of %s does not trace like the original; "
                             "not written" % Path(src).name)
    return claude_transcript.capture(source, out_dir, verify=verify)


# -- opencode ----------------------------------------------------------------

SESSION_COLUMNS = ("id", "parent_id", "slug", "title", "time_created",
                   "time_updated", "tokens_input", "tokens_output",
                   "tokens_reasoning", "tokens_cache_read", "tokens_cache_write")
# The run card's reference SQL (run_card.REFERENCE_SQL), by session id.
SESSION_SQL = ("SELECT " + ", ".join("s." + c for c in SESSION_COLUMNS) + ", "
               "s.tokens_input + s.tokens_output AS billed, "
               "(SELECT count(*) FROM part p WHERE p.session_id = s.id) AS parts, "
               "(SELECT sum(length(data)) FROM part p2 WHERE p2.session_id = s.id) "
               "AS storesize FROM session s WHERE s.id = ?")
CHILDREN_SQL = "SELECT id FROM session WHERE parent_id = ? ORDER BY time_created, id"
MESSAGES_SQL = ("SELECT id, session_id, time_created, time_updated, data "
                "FROM message WHERE session_id = ? ORDER BY time_created, id")
PARTS_SQL = ("SELECT id, message_id, session_id, time_created, time_updated, data "
             "FROM part WHERE session_id = ? ORDER BY time_created, id")
SLUG_SQL = ("SELECT id FROM session s WHERE s.slug = ? AND s.project_id IN "
            "(SELECT id FROM project WHERE worktree LIKE '%' || ? || '%') "
            "ORDER BY s.time_created DESC LIMIT 1")
ROW_KEYS = ("id", "message_id", "session_id", "time_created", "time_updated")


class DbStore:
    """The opencode database, per-session and read-only."""

    def __init__(self, con, name="opencode.db"):
        self.con = con
        self.name = name

    def session(self, session_id):
        row = self.con.execute(SESSION_SQL, (session_id,)).fetchone()
        return dict(row) if row is not None else None

    def children(self, session_id):
        return [r["id"] for r in self.con.execute(CHILDREN_SQL, (session_id,))]

    def messages(self, session_id):
        return [self._row(r) for r in self.con.execute(MESSAGES_SQL, (session_id,))]

    def parts(self, session_id):
        return [self._row(r) for r in self.con.execute(PARTS_SQL, (session_id,))]

    def find_slug(self, slug, marker=run_card.PROJECT_MARKER):
        row = self.con.execute(SLUG_SQL, (slug, marker)).fetchone()
        return row["id"] if row is not None else None

    @staticmethod
    def _row(row):
        out = {k: row[k] for k in row.keys() if k != "data"}
        try:
            out["data"] = json.loads(row["data"])
        except (TypeError, ValueError):
            out["data"] = {}
        return out


class SliceStore:
    """A captured opencode family (`capture_opencode`), same interface."""

    def __init__(self, path):
        self.path = Path(path)
        self.name = self.path.name
        self._sessions = {}
        self._messages = {}
        self._parts = {}
        with open(self.path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                table = row.pop("table", None)
                if table == "session":
                    self._sessions[row["id"]] = row
                elif table == "message":
                    self._messages.setdefault(row["session_id"], []).append(row)
                elif table == "part":
                    self._parts.setdefault(row["session_id"], []).append(row)

    def roots(self):
        """Session ids whose parent is not in the slice, in file order."""
        return [sid for sid, row in self._sessions.items()
                if row.get("parent_id") not in self._sessions]

    def session(self, session_id):
        return self._sessions.get(session_id)

    def children(self, session_id):
        rows = [r for r in self._sessions.values() if r.get("parent_id") == session_id]
        rows.sort(key=lambda r: (r.get("time_created") or 0, r["id"]))
        return [r["id"] for r in rows]

    def messages(self, session_id):
        return list(self._messages.get(session_id, []))

    def parts(self, session_id):
        return list(self._parts.get(session_id, []))

    def find_slug(self, slug, marker=None):
        rows = [r for r in self._sessions.values() if r.get("slug") == slug]
        rows.sort(key=lambda r: r.get("time_created") or 0, reverse=True)
        return rows[0]["id"] if rows else None


def open_db(db_path=None):
    """A `DbStore` over the opencode database (read-only URI, as run_card)."""
    db_path = Path(db_path or os.environ.get(run_card.ENV_DB) or run_card.DEFAULT_DB)
    if not db_path.is_file():
        raise FileNotFoundError(f"database not found: {db_path}")
    return DbStore(run_card.connect(db_path), db_path.name)


def _text_size(data):
    if "text" in data:
        return byte_size(data["text"])
    value = data.get("text_bytes")
    return int(value) if value is not None else None


def _tool_output_size(state):
    """Size of what the model saw back: the output, or the error when the
    output is null (a failed call); from a slice, the recorded size."""
    if "input_bytes" in state:
        value = state.get("output_bytes")
        return int(value) if value is not None else None
    output = state.get("output")
    if output is None:
        output = state.get("error")
    return byte_size(output) if output is not None else None


def _tool_output_head(state):
    """The head of what the model saw back (output, else the error); from
    a slice, the recorded head."""
    if "input_bytes" in state:
        return state.get("output_head")
    output = state.get("output")
    if output is None:
        output = state.get("error")
    return head_of(output)


def _part_steps(row, role, base):
    """The steps one part row yields (0, 1 or 2)."""
    data = row.get("data") or {}
    ptype = data.get("type")
    if ptype in ("text", "reasoning"):
        size = _text_size(data)
        ts = (data.get("time") or {}).get("start") or row.get("time_created")
        if ptype == "reasoning":
            return [_step(ts=ts, kind="reasoning", role="assistant", out_bytes=size, **base)]
        if role == "user":
            return [_step(ts=ts, kind="text", role="user", in_bytes=size, **base)]
        return [_step(ts=ts, kind="text", role="assistant", out_bytes=size, **base)]
    if ptype == "tool":
        state = data.get("state") or {}
        time = state.get("time") or {}
        if "input_bytes" in state:
            in_bytes, command = int(state["input_bytes"]), state.get("command")
            input_head = state.get("input_head")
        else:
            in_bytes = byte_size(state.get("input", {}))
            command = command_of(state.get("input"))
            input_head = input_head_of(state.get("input"))
        tool, call_id = data.get("tool"), data.get("callID")
        # The row's time_created is the call's real start (see the module
        # docstring); state.time.start is stamped at completion.
        steps = [_step(ts=row.get("time_created") or time.get("start"), kind="tool_use",
                       role="assistant", tool=tool, tool_use_id=call_id,
                       command=command, input_head=input_head, in_bytes=in_bytes, **base)]
        status = state.get("status")
        if status in FINISHED_STATUSES:
            steps.append(_step(ts=time.get("end") or row.get("time_updated"),
                               kind="tool_result", role=ROLE_TOOL_RESULT, tool=tool,
                               tool_use_id=call_id, command=command,
                               out_bytes=_tool_output_size(state),
                               output_head=_tool_output_head(state),
                               is_error=(status == "error"), **base))
        return steps
    return []


def _opencode_usage(tokens):
    cache = tokens.get("cache") if isinstance(tokens.get("cache"), dict) else {}
    return _usage(tokens.get("input"), tokens.get("output"), cache.get("read"),
                  cache.get("write"), tokens.get("reasoning"))


def trace_opencode(store, session_id, parent_session_id=None):
    """The steps of one opencode session."""
    messages = store.messages(session_id)
    roles = {}
    for row in messages:
        roles[row["id"]] = (row.get("data") or {}).get("role")
    by_message = {}
    steps = []
    for row in store.parts(session_id):
        mid = row.get("message_id")
        role = roles.get(mid) or "assistant"
        base = {"session_id": session_id, "host": HOST_OPENCODE,
                "parent_session_id": parent_session_id,
                "request_id": mid if role == "assistant" else None}
        new = _part_steps(row, role, base)
        by_message.setdefault(mid, []).extend(new)
        steps.extend(new)
    for row in messages:
        data = row.get("data") or {}
        tokens = data.get("tokens")
        if data.get("role") != "assistant" or not isinstance(tokens, dict):
            continue
        mine = by_message.get(row["id"]) or []
        if not mine:
            created = (data.get("time") or {}).get("created") or row.get("time_created")
            empty = _step(ts=created, kind="text", role="assistant", out_bytes=0,
                          session_id=session_id, host=HOST_OPENCODE,
                          parent_session_id=parent_session_id, request_id=row["id"])
            steps.append(empty)
            mine = [empty]
        first = min(mine, key=lambda s: -1 if s["ts"] is None else s["ts"])
        first.update(_opencode_usage(tokens))
    return _finish(steps)


def trace_opencode_family(store, session_id, parent_session_id=None):
    """`{session_id: steps}` for a session and its subagents, parent first."""
    family = {session_id: trace_opencode(store, session_id, parent_session_id)}
    for child in store.children(session_id):
        family.update(trace_opencode_family(store, child, session_id))
    return family


def slice_message_data(data):
    """A message's data reduced to role, time, usage and error name."""
    out = {}
    for key in ("role", "time", "tokens"):
        if key in data:
            out[key] = data[key]
    error = data.get("error")
    if isinstance(error, dict) and error.get("name"):
        out["error"] = {"name": error["name"]}
    return out


def slice_part_data(data):
    """A part's data reduced to its evidence (see the module docstring)."""
    ptype = data.get("type")
    out = {"type": ptype}
    if ptype in ("text", "reasoning"):
        out["text_bytes"] = _text_size(data)
        if "time" in data:
            out["time"] = data["time"]
    elif ptype == "tool":
        state = data.get("state") or {}
        kept = {"status": state.get("status"),
                "input_bytes": byte_size(state.get("input", {}))}
        command = command_of(state.get("input"))
        if command is not None:
            kept["command"] = command
        input_head = input_head_of(state.get("input"))
        if input_head is not None:
            kept["input_head"] = input_head
        size = _tool_output_size(state)
        if size is not None:
            kept["output_bytes"] = size
        head = _tool_output_head(state)
        if head is not None:
            kept["output_head"] = head
        if "time" in state:
            kept["time"] = state["time"]
        out.update({"tool": data.get("tool"), "callID": data.get("callID"),
                    "state": kept})
    return out


def _family_ids(store, session_id):
    ids = [session_id]
    for child in store.children(session_id):
        ids.extend(_family_ids(store, child))
    return ids


def capture_opencode(store, session_id, out_dir):
    """Write `<id>.jsonl` (the family's rows, content dropped) + the index
    entry; refuse a slice that traces differently from the store."""
    if store.session(session_id) is None:
        raise ValueError(f"no session {session_id} in {store.name}")
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{session_id}.jsonl"
    lines = []
    cards = {}
    for sid in _family_ids(store, session_id):
        session = dict(store.session(sid))
        cards[sid] = session
        lines.append(dict(table="session", **session))
        for row in store.messages(sid):
            kept = {k: row[k] for k in ROW_KEYS if k in row}
            kept["data"] = slice_message_data(row.get("data") or {})
            lines.append(dict(table="message", **kept))
        for row in store.parts(sid):
            kept = {k: row[k] for k in ROW_KEYS if k in row}
            kept["data"] = slice_part_data(row.get("data") or {})
            lines.append(dict(table="part", **kept))
    target.write_text("\n".join(json.dumps(l, sort_keys=True, separators=(",", ":"))
                                for l in lines) + "\n", encoding="utf-8")
    if trace_opencode_family(SliceStore(target), session_id) != \
            trace_opencode_family(store, session_id):
        target.unlink()
        raise ValueError("slice of %s does not trace like %s; not written"
                         % (session_id, store.name))
    index_path = out_dir / INDEX_FILE
    index = {}
    if index_path.is_file():
        index = json.loads(index_path.read_text(encoding="utf-8"))
    entry = {"captured_from": store.name,
             "card": {k: cards[session_id][k] for k in CARD_KEYS}}
    children = {sid: {k: card[k] for k in CARD_KEYS}
                for sid, card in cards.items() if sid != session_id}
    if children:
        entry["subagents"] = children
    index[session_id] = entry
    index_path.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")
    return target


# -- workspace, output, --top ------------------------------------------------

def host_of(session_id, host=None):
    """opencode for a `ses_` id, else Claude Code, unless told otherwise."""
    if host:
        return host
    return HOST_OPENCODE if str(session_id).startswith(OPENCODE_ID_PREFIX) else HOST_CLAUDE


def workspace_sessions(workspace):
    """`[(host, session_id)]` the workspace declared, in order, unique.

    Read from results/state/sessions.jsonl (ticket 01: one line per phase
    declaration with ts, phase, name, host, host_session_id). When that file
    is absent, the single session results/state/session.json declares is
    used, so an older workspace still traces.
    """
    path = Path(workspace) / "results" / "state" / SESSIONS_FILE
    found = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if not isinstance(row, dict):
            continue
        sid = str(row.get("host_session_id") or "")
        if not sid:
            continue
        pair = (host_of(sid, row.get("host") or None), sid)
        if pair not in found:
            found.append(pair)
    if not found:
        host, sid = run_card.declared_session(workspace)
        if sid:
            found.append((host_of(sid, host or None), sid))
    return found


def write_steps(steps, out_dir, session_id):
    """`<out_dir>/<session_id>.steps.jsonl`, one step per line."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{session_id}{STEPS_SUFFIX}"
    with open(target, "w", encoding="utf-8") as fh:
        for step in steps:
            fh.write(json.dumps(step, separators=(",", ":")) + "\n")
    return target


def read_steps(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _iso(ms):
    if ms is None:
        return "n/a"
    return datetime.fromtimestamp(ms / 1000.0, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _kb(n):
    return "%.1f KB" % ((n or 0) / KB)


def top_report(session_id, host, steps, n=10):
    """Section 2 of the analysis doc for one session: what the bytes were.

    Reasoning share, persisted tool outputs, and the tool-call histogram,
    then the N heaviest tool outputs and reasoning blocks.
    """
    reasoning = [s for s in steps if s["kind"] == "reasoning"]
    results = [s for s in steps if s["kind"] == "tool_result"]
    calls = [s for s in steps if s["kind"] == "tool_use"]
    usage = totals(steps)
    lines = ["== %s (%s): steps=%d requests=%d billed=%s"
             % (session_id, host, len(steps), usage["requests"], f"{usage['billed']:,}")]
    hist = Counter(s["tool"] or "?" for s in calls)
    lines.append("tool calls: %d -- %s" % (
        len(calls), ", ".join(f"{k} {v}" for k, v in hist.most_common()) or "none"))
    lines.append("reasoning: %d blocks, %s" % (
        len(reasoning), _kb(sum(s["out_bytes"] or 0 for s in reasoning))))
    lines.append("tool outputs: %d results, %s (%d errors)" % (
        len(results), _kb(sum(s["out_bytes"] or 0 for s in results)),
        sum(1 for s in results if s["is_error"])))
    lines.append("heaviest tool outputs:")
    for s in sorted(results, key=lambda s: s["out_bytes"] or 0, reverse=True)[:n]:
        lines.append("  %9s  %-12s %s  %s%s" % (
            _kb(s["out_bytes"]), s["tool"] or "?", _iso(s["ts"]),
            (s["command"] or "")[:80].replace("\n", " "), "  [error]" if s["is_error"] else ""))
    lines.append("heaviest reasoning blocks:")
    for s in sorted(reasoning, key=lambda s: s["out_bytes"] or 0, reverse=True)[:n]:
        lines.append("  %9s  %s" % (_kb(s["out_bytes"]), _iso(s["ts"])))
    return "\n".join(lines)


def _families(args):
    """`[(host, {session_id: steps})]` for what the CLI asked for."""
    if args.transcript:
        path = Path(args.transcript)
        if not path.is_file():
            raise FileNotFoundError(f"transcript not found: {path}")
        return [(HOST_CLAUDE, trace_claude(path))]
    if args.slice:
        store = SliceStore(args.slice)
        roots = [args.session_id] if args.session_id else store.roots()
        if not roots:
            raise ValueError(f"no session in slice {args.slice}")
        return [(HOST_OPENCODE, trace_opencode_family(store, sid)) for sid in roots]
    wanted = []
    if args.workspace:
        wanted = workspace_sessions(args.workspace)
        if not wanted:
            raise ValueError("no sessions declared in %s (results/state/%s or "
                             "session.json)" % (args.workspace, SESSIONS_FILE))
    elif args.session_id:
        wanted = [(host_of(args.session_id, args.host), args.session_id)]
    elif args.slug:
        host = args.host or HOST_OPENCODE
        if host == HOST_OPENCODE:
            store = open_db(args.db)
            sid = store.find_slug(args.slug)
            if sid is None:
                raise ValueError(f"no opencode session with slug {args.slug!r} "
                                 f"in the {run_card.PROJECT_MARKER} project")
            return [(HOST_OPENCODE, trace_opencode_family(store, sid))]
        card = claude_transcript.select(slug=args.slug, root=args.projects_dir)
        if card is None:
            raise ValueError(f"no Claude Code transcript titled {args.slug!r}")
        return [(HOST_CLAUDE, trace_claude(card["transcript"]))]
    else:
        raise ValueError("give one of --workspace, --session-id, --slug, "
                         "--transcript or --slice")
    families = []
    db = None
    for host, sid in wanted:
        if host == HOST_OPENCODE:
            db = db or open_db(args.db)
            if db.session(sid) is None:
                raise ValueError(f"no opencode session {sid}")
            families.append((host, trace_opencode_family(db, sid)))
        else:
            path = claude_transcript.find_transcript(sid, args.projects_dir)
            if path is None:
                raise ValueError(f"no Claude Code transcript for session {sid} under "
                                 f"{claude_transcript.projects_dir(args.projects_dir)}")
            families.append((host, trace_claude(path)))
    return families


def _capture(args):
    host = host_of(args.capture, args.host)
    if host == HOST_OPENCODE:
        store = open_db(args.db)
        target = capture_opencode(store, args.capture, args.out)
        print(f"PASS: run_trace captured {target.name} from {store.name}")
        return 0
    source = claude_transcript.find_transcript(args.capture, args.projects_dir)
    if source is None:
        raise ValueError(f"no transcript for session {args.capture}")
    target = capture_claude(source, args.out)
    print(f"PASS: run_trace captured {target.name} from {source.parent.name}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspace", help="trace every session the workspace declared")
    parser.add_argument("--session-id", help="one session (ses_... is opencode)")
    parser.add_argument("--slug", help="opencode slug, or Claude Code title with --host")
    parser.add_argument("--host", choices=HOSTS, help="force the store to read")
    parser.add_argument("--transcript", help="a Claude Code transcript .jsonl")
    parser.add_argument("--slice", help="a captured opencode fixture .jsonl")
    parser.add_argument("--db", help="opencode.db path (default: $OPENCODE_DB or ~/.local/share/opencode/opencode.db)")
    parser.add_argument("--projects-dir", help="Claude Code projects dir (default: ~/.claude/projects)")
    parser.add_argument("--out", help="output dir (default: <workspace>/%s)" % TRACE_DIR)
    parser.add_argument("--top", type=int, metavar="N",
                        help="print the N heaviest outputs and reasoning blocks; write nothing")
    parser.add_argument("--no-subagents", action="store_true",
                        help="leave subagent sessions out")
    parser.add_argument("--capture", metavar="SESSION_ID",
                        help="write a verified fixture slice of this session to --out")
    args = parser.parse_args(argv)

    try:
        if args.capture:
            if not args.out:
                parser.error("--capture needs --out DIR")
            return _capture(args)
        families = _families(args)
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.no_subagents:                 # a family lists its parent first
        families = [(host, dict(list(fam.items())[:1])) for host, fam in families]
    if args.top is not None:
        for host, family in families:
            for sid, steps in family.items():
                print(top_report(sid, host, steps, args.top))
        return 0
    out_dir = Path(args.out) if args.out else Path(args.workspace or ".") / TRACE_DIR
    written = 0
    steps_total = 0
    for host, family in families:
        for sid, steps in family.items():
            write_steps(steps, out_dir, sid)
            written += 1
            steps_total += len(steps)
    print(f"PASS: run_trace sessions={written} steps={steps_total} dir={out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
