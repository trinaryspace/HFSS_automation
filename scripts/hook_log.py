"""Claude Code tool hook: append one line per tool call to the active
workspace's `results/state/tools.jsonl` (run logging, ticket 08).

Installed into `.claude/settings.json` by `scripts/install_skill.py`
(merged into the file, removed by `--remove-hooks`) as a `PreToolUse`, a
`PostToolUse` and a `PostToolUseFailure` command hook on every tool.
Claude Code runs it with the hook payload on stdin — JSON with
`session_id`, `hook_event_name`, `tool_name`, `tool_input`, `tool_use_id`
and, after the call, `tool_response` or `error` — and it must return
within ~50 ms and never block a tool: it appends and exits, parses no
command, and exits 0 on every malformed input (a hook that exits 2 would
block the call; anything else is noise in the transcript).

The workspace a session belongs to is looked up in
`~/.hfss-agent/sessions.json`, written by `scripts/session.py --phase`
(session id -> {workspace, phase}; `hfss_spec.session.register_session`).
A session with no entry is not a run and logs nothing. The file lives
outside every checkout on purpose: one hook, however many worktrees.

    PreToolUse       writes a start stamp, `~/.hfss-agent/pending/<key>`,
                     keyed by session id + tool_use_id (falling back to the
                     tool name when a payload has no id)
    PostToolUse      reads and deletes the stamp, appends the line
    PostToolUseFailure  same, with `is_error` true (Claude Code fires this
                     instead of PostToolUse when the tool itself failed)

The line: `{ts, session_id, phase, tool, command, exit_code, duration_ms,
exec_ms, tool_use_id, is_error}` — `ts` epoch ms of the completion,
`command` the tool input's command / path / pattern whole (capped, never
parsed), `duration_ms` the wall from the stamp to the completion (what the
model waited, permission prompt included) or null when the start was not
seen, `exec_ms` the harness's own `duration_ms` (execution only, per its
description) or null. `scripts/run_trace.py` merges the file into the
step trace: `is_error` from the exit code, `latency_ms` of the tool_use
from `duration_ms`.

What the payloads look like on Claude Code 2.1.258, captured from a real
headless session in this checkout (`scripts/fixtures/hooks/`, four raw
payloads kept byte-for-byte by `--capture`): every event carries
`session_id`, `transcript_path`, `cwd`, `prompt_id`, `permission_mode`,
`effort`, `hook_event_name`, `tool_name`, `tool_input`, `tool_use_id`. A
successful Bash call's `PostToolUse` adds `tool_response` =
`{stdout, stderr, interrupted, isImage, noOutputExpected}` — **no exit
code**: a non-zero exit is not a PostToolUse at all but a
`PostToolUseFailure` whose `error` is `"Exit code 3"` (the code on the
first line, stderr and stdout after it) with `is_interrupt`. Both carry
the harness's `duration_ms`. So `exit_code` is 0 on a PostToolUse of a
Bash call, the number on the error's first line on a failure, and null
for every other tool (they have no exit code). `cwd` is the session's
working directory (the worktree root for a worktree session); hooks run
there.

Usage:
    python -I -S scripts/hook_log.py               # stdin: the hook payload
    python -I -S scripts/hook_log.py --capture DIR # also keep the raw stdin
                                                   # as DIR/<event>.<id>.json
                                                   # (fixture capture)

`HFSS_AGENT_HOME` overrides `~/.hfss-agent` (tests, and `hfss_spec.session`
honours the same variable). Stdlib only; `-I -S` keeps the interpreter's
start-up under the budget, so the script must not need site-packages.
"""

import json
import os
import sys
import time

ENV_HOME = "HFSS_AGENT_HOME"
HOME_DIRNAME = ".hfss-agent"
SESSIONS_MAP = "sessions.json"
PENDING_DIR = "pending"
LOG_FILE = "tools.jsonl"                     # under <workspace>/results/state/
STATE_SUBDIR = ("results", "state")

PRE = "PreToolUse"
POST = "PostToolUse"
POST_FAILURE = "PostToolUseFailure"
EVENTS = (PRE, POST, POST_FAILURE)

COMMAND_KEYS = ("command", "file_path", "filePath", "pattern", "prompt", "url")
COMMAND_CHARS = 8192                         # claude_transcript.COMMAND_CHARS
LINE_KEYS = ("ts", "session_id", "phase", "tool", "command", "exit_code",
             "duration_ms", "exec_ms", "tool_use_id", "is_error")
SAFE_CHARS = frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.")


def home_dir(environ=None):
    env = os.environ if environ is None else environ
    override = env.get(ENV_HOME)
    if override:
        return override
    return os.path.join(os.path.expanduser("~"), HOME_DIRNAME)


def sessions_map_path(environ=None):
    return os.path.join(home_dir(environ), SESSIONS_MAP)


def pending_dir(environ=None):
    return os.path.join(home_dir(environ), PENDING_DIR)


def log_path(workspace):
    return os.path.join(workspace, *STATE_SUBDIR, LOG_FILE)


def now_ms():
    return int(time.time() * 1000)


# -- the lookup --------------------------------------------------------------

def load_sessions(path):
    """The session map, or {} for a missing or unreadable file."""
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def lookup(sessions, session_id):
    """(workspace, phase) for a session, or (None, None).

    An entry is `{"workspace": ..., "phase": ...}`; a bare string value is
    taken as the workspace, so a hand-written map still resolves.
    """
    entry = sessions.get(session_id) if isinstance(session_id, str) else None
    if isinstance(entry, str):
        return (entry or None), None
    if isinstance(entry, dict):
        workspace = entry.get("workspace")
        if isinstance(workspace, str) and workspace:
            phase = entry.get("phase")
            return workspace, (phase if isinstance(phase, str) else None)
    return None, None


# -- the payload -------------------------------------------------------------

def parse(raw):
    """The payload as a dict, or None for anything that is not one."""
    try:
        data = json.loads(raw)
    except (TypeError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def stamp_key(session_id, tool_use_id, tool):
    """The pending-file name: session id + tool_use_id, else + tool name."""
    tail = tool_use_id if isinstance(tool_use_id, str) and tool_use_id else tool
    raw = "%s.%s" % (session_id, tail if isinstance(tail, str) and tail else "tool")
    return "".join(c if c in SAFE_CHARS else "_" for c in raw)[:200]


def command_of(tool_input):
    """The command / path / pattern of a tool input, whole and unparsed."""
    if not isinstance(tool_input, dict):
        return None
    for key in COMMAND_KEYS:
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            return value[:COMMAND_CHARS]
    return None


def exit_code_of(payload):
    """The exit code of the call a payload reports, else None.

    PostToolUseFailure: the integer after `Exit code ` on the error's
    first line (Claude Code's Bash tool raises `Exit code N` + stderr +
    stdout for a non-zero exit); None when the error is something else (a
    timeout, a sandbox refusal, an interrupt). PostToolUse: 0 when the
    response is a Bash response (`stdout` and `stderr` strings), else the
    integer under an `exit_code` / `exitCode` / `code` key when a response
    carries one, else None. Never raises.
    """
    if not isinstance(payload, dict):
        return None
    if payload.get("hook_event_name") == POST_FAILURE:
        return _exit_code_in_text(payload.get("error"))
    response = payload.get("tool_response")
    if response is None:
        response = payload.get("tool_result")
    if not isinstance(response, dict):
        return None
    for key in ("exit_code", "exitCode", "code", "returncode", "returnCode"):
        value = response.get(key)
        if isinstance(value, int) and not isinstance(value, bool):
            return value
        if isinstance(value, str) and value.lstrip("-").isdigit():
            return int(value)
    if isinstance(response.get("stdout"), str) and isinstance(response.get("stderr"), str):
        return 0
    return None


def _exit_code_in_text(text):
    """`Exit code N` at the head of a tool's error text, else None."""
    if not isinstance(text, str):
        return None
    head = text.lstrip()[:64]
    marker = "Exit code "
    if not head.startswith(marker):
        return None
    digits = ""
    for ch in head[len(marker):]:
        if ch.isdigit() or (ch == "-" and not digits):
            digits += ch
        else:
            break
    try:
        return int(digits)
    except ValueError:
        return None


def line_for(payload, phase, started_ms, ended_ms):
    """The tools.jsonl record for one completed call."""
    failed = payload.get("hook_event_name") == POST_FAILURE
    code = exit_code_of(payload)
    exec_ms = payload.get("duration_ms")
    if isinstance(exec_ms, bool) or not isinstance(exec_ms, (int, float)):
        exec_ms = None
    tool_use_id = payload.get("tool_use_id")
    return {
        "ts": ended_ms,
        "session_id": payload.get("session_id"),
        "phase": phase,
        "tool": payload.get("tool_name"),
        "command": command_of(payload.get("tool_input")),
        "exit_code": code,
        "duration_ms": None if started_ms is None else max(0, ended_ms - started_ms),
        "exec_ms": None if exec_ms is None else int(exec_ms),
        "tool_use_id": tool_use_id if isinstance(tool_use_id, str) else None,
        "is_error": bool(failed or (code is not None and code != 0)),
    }


# -- the two halves ----------------------------------------------------------

def write_stamp(pending, key, ts):
    try:
        os.makedirs(pending, exist_ok=True)
        with open(os.path.join(pending, key), "w", encoding="utf-8") as fh:
            fh.write(str(ts))
    except OSError:
        pass


def take_stamp(pending, key):
    """The start ms the stamp holds (the file is removed), or None."""
    path = os.path.join(pending, key)
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read().strip()
    except OSError:
        return None
    try:
        os.remove(path)
    except OSError:
        pass
    try:
        return int(text)
    except ValueError:
        return None


def append_line(path, record):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, separators=(",", ":")) + "\n")
    except (OSError, TypeError, ValueError):
        return False
    return True


def handle(raw, environ=None, clock=now_ms):
    """Process one payload. Returns what was done, for tests: "ignored"
    (not a payload, or not a run's session), "stamped", "logged" or
    "unwritten" (the append failed)."""
    payload = parse(raw)
    if payload is None:
        return "ignored"
    session_id = payload.get("session_id")
    event = payload.get("hook_event_name")
    if not isinstance(session_id, str) or event not in EVENTS:
        return "ignored"
    workspace, phase = lookup(load_sessions(sessions_map_path(environ)), session_id)
    if workspace is None:
        return "ignored"
    key = stamp_key(session_id, payload.get("tool_use_id"), payload.get("tool_name"))
    pending = pending_dir(environ)
    if event == PRE:
        write_stamp(pending, key, clock())
        return "stamped"
    started = take_stamp(pending, key)
    record = line_for(payload, phase, started, clock())
    return "logged" if append_line(log_path(workspace), record) else "unwritten"


def capture(raw, out_dir):
    """Keep the raw stdin as a fixture: `<event>.<tool_use_id>.json`, or
    `malformed.<ms>.json` when it does not parse. Byte-for-byte."""
    payload = parse(raw)
    if payload is None:
        name = "malformed.%d.json" % now_ms()
    else:
        name = "%s.%s.json" % (payload.get("hook_event_name") or "unknown",
                               payload.get("tool_use_id") or now_ms())
    name = "".join(c if c in SAFE_CHARS else "_" for c in name)
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, name), "wb") as fh:
            fh.write(raw if isinstance(raw, bytes) else raw.encode("utf-8"))
    except OSError:
        pass


def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    out_dir = None
    if len(argv) >= 2 and argv[0] == "--capture":
        out_dir = argv[1]
    try:
        raw = sys.stdin.buffer.read()
    except Exception:                                   # noqa: BLE001
        return 0
    if out_dir is not None:
        try:
            capture(raw, out_dir)
        except Exception:                               # noqa: BLE001
            pass
    try:
        handle(raw)
    except Exception:                                   # noqa: BLE001
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
