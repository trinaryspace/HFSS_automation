"""The one parser for Claude Code session transcripts (run-card backend).

opencode keeps its sessions in a SQLite database; Claude Code keeps each
session as a JSONL transcript under `~/.claude/projects/<encoded cwd>/
<session-id>.jsonl`. `scripts/run_card.py` reads either, and this module is
the whole of the Claude Code side: locate a transcript, reduce it to the
same card dict the opencode SQL produces, and capture a verified fixture
slice from a real transcript for the tests.

What the card's numbers mean on this host (the opencode column is the
reference the card was designed around; the mapping is stated here so a
reader never has to guess):

- `tokens_input` / `tokens_output` / `tokens_cache_read` /
  `tokens_cache_write`: summed over the session's API requests from each
  assistant record's `message.usage`. One API response is written as
  several `assistant` records (one per content block) that all carry the
  same `requestId`, so usage is counted **once per requestId**, never once
  per record -- and the LAST record's usage is the one kept: on 2.1.258 the
  earlier records of a request hold a running count (output 36 on the
  first record, 2356 on the last, in the a0e9c38f fixture).
- `tokens_reasoning`: the summed `output_tokens_details.thinking_tokens`
  when the record carries it; otherwise 0, exactly as opencode reports 0
  for providers that do not break it out.
- `billed`: `tokens_input + tokens_output`, the same definition as the SQL.
- `parts`: the count of `user` + `assistant` records — one content block
  or tool result per record, which is what an opencode `part` row is.
- `storesize`: the transcript's size in bytes (opencode: sum of part data).
- `slug`: the session's title — a `/rename` custom title if one was set,
  else the AI-generated title, else the session id. The named phase
  sessions the skill asks for (`<name>-clarify` …) are set with `/rename`
  on this host.
- `time_created` / `time_updated`: the first and last **message** record
  timestamps (user or assistant). Attachment, mode and file-history records
  also carry timestamps but are bookkeeping, not the session's span.

Subagent transcripts (the `<session-id>/` directory beside the file) are
**not** folded in, matching opencode where subagent sessions are their own
rows and the card reads only the parent.

Usage:
    python scripts/claude_transcript.py --session-id <id>        # print the card
    python scripts/claude_transcript.py --latest                  # newest HFSS session
    python scripts/claude_transcript.py --capture <id> --out DIR  # fixture slice

Fixture capture writes `<id>.jsonl` plus `index.json` holding the card
computed from the FULL original. The slice keeps every user/assistant
record's bookkeeping (ids, timestamps, requestId, the usage keys the card
reads) and the title records, and reduces each content block to its
evidence with the content itself dropped:

- `thinking`    -> `{"type": "thinking", "thinking_bytes": N}`
- `text`        -> `{"type": "text", "text_bytes": N}`
- `tool_use`    -> `{"type": "tool_use", "id", "name", "input_bytes": N,
                     "command": <first 200 chars of the command / path>}`
- `tool_result` -> `{"type": "tool_result", "tool_use_id", "is_error",
                     "content_bytes": N}`
- a string `content` -> `"content_bytes": N` on the message

`N` is the UTF-8 byte length of the text, or of the block's JSON for
non-text values (`byte_size`). `scripts/run_trace.py` reads either form,
so a slice traces exactly like its source. The slice is written only if it
reduces to the same card (`storesize` aside, which is the slice's own size
by construction) and passes the caller's extra `verify` check, so a fixture
can never drift from the artifact it stands for
(docs/agents/fixture-fidelity.md). Subagent transcripts beside the source
(`<id>/subagents/agent-*.jsonl`) are sliced the same way into the same
layout under the fixture dir, each verified against its own card.
Stdlib only, Python 3.10 compatible.
"""

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECTS_DIR = Path.home() / ".claude" / "projects"
ENV_SESSION_ID = "CLAUDE_CODE_SESSION_ID"
ENV_PROJECTS_DIR = "CLAUDE_PROJECTS_DIR"
PROJECT_MARKER = "HFSS_automation"
HOST = "claude-code"

# Record types that carry a session title, in precedence order.
TITLE_KEYS = (
    ("custom-title", "customTitle"),   # /rename
    ("ai-title", "aiTitle"),           # generated
    ("agent-name", "agentName"),       # the session's display name
)
PART_TYPES = ("user", "assistant")
CARD_KEYS = ("slug", "time_created", "time_updated", "tokens_input",
             "tokens_output", "tokens_reasoning", "tokens_cache_read",
             "tokens_cache_write", "billed", "parts", "storesize")
INDEX_FILE = "index.json"


def encoded_marker(marker=PROJECT_MARKER):
    """Claude Code names a project dir by its cwd with every non-alphanumeric
    character turned into `-` (`C:\\Users\\me\\Repos\\HFSS_automation` ->
    `C--Users-me-Repos-HFSS-automation`)."""
    return re.sub(r"[^A-Za-z0-9]", "-", marker)


def projects_dir(override=None):
    return Path(override or os.environ.get(ENV_PROJECTS_DIR) or PROJECTS_DIR)


def project_transcripts(root=None, marker=PROJECT_MARKER, worktree=None):
    """Transcript paths for the HFSS project, newest-modified first.

    Every worktree gets its own project dir, so the marker matches them all
    (a parallel campaign runs cells from several worktrees, exactly as the
    opencode backend's `IN (SELECT ... LIKE marker)` does). `worktree`
    narrows to one exact cwd.
    """
    root = projects_dir(root)
    if not root.is_dir():
        return []
    wanted = encoded_marker(worktree) if worktree else None
    found = []
    for project in root.iterdir():
        if not project.is_dir():
            continue
        if wanted is not None:
            if project.name != wanted:
                continue
        elif encoded_marker(marker) not in project.name:
            continue
        found.extend(p for p in project.glob("*.jsonl") if p.is_file())
    found.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return found


def find_transcript(session_id, root=None):
    """The transcript for a session id, searched across every project dir."""
    root = projects_dir(root)
    if not root.is_dir():
        return None
    for project in root.iterdir():
        candidate = project / f"{session_id}.jsonl"
        if candidate.is_file():
            return candidate
    return None


def _records(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except ValueError:
                continue                # a torn tail line while the session is live


def _iso_to_ms(raw):
    if not isinstance(raw, str):
        return None
    try:
        dt = datetime.strptime(raw, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        try:
            dt = datetime.strptime(raw, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            return None
    return int(dt.replace(tzinfo=timezone.utc).timestamp() * 1000)


def _usage_of(record):
    message = record.get("message")
    if not isinstance(message, dict):
        return None
    usage = message.get("usage")
    return usage if isinstance(usage, dict) else None


def load_card(path):
    """Reduce one transcript to the run-card dict; None if it has no session."""
    path = Path(path)
    usage_by_request = {}
    titles = {}
    parts = 0
    first_ms = last_ms = None
    session_id = None
    for record in _records(path):
        rtype = record.get("type")
        session_id = session_id or record.get("sessionId")
        for title_type, key in TITLE_KEYS:
            if rtype == title_type and record.get(key):
                titles[title_type] = record[key]
        if rtype in PART_TYPES:
            parts += 1
            ts = _iso_to_ms(record.get("timestamp"))
            if ts is not None:
                first_ms = ts if first_ms is None else min(first_ms, ts)
                last_ms = ts if last_ms is None else max(last_ms, ts)
        if rtype == "assistant":
            usage = _usage_of(record)
            if usage is not None:
                key = record.get("requestId") or record["message"].get("id") \
                    or f"record-{parts}"
                usage_by_request[key] = usage
    if session_id is None and not usage_by_request and parts == 0:
        return None
    totals = {"tokens_input": 0, "tokens_output": 0, "tokens_reasoning": 0,
              "tokens_cache_read": 0, "tokens_cache_write": 0}
    for usage in usage_by_request.values():
        totals["tokens_input"] += int(usage.get("input_tokens") or 0)
        totals["tokens_output"] += int(usage.get("output_tokens") or 0)
        totals["tokens_cache_read"] += int(usage.get("cache_read_input_tokens") or 0)
        totals["tokens_cache_write"] += int(usage.get("cache_creation_input_tokens") or 0)
        details = usage.get("output_tokens_details")
        if isinstance(details, dict):
            totals["tokens_reasoning"] += int(details.get("thinking_tokens") or 0)
    slug = next((titles[t] for t, _ in TITLE_KEYS if t in titles),
                session_id or path.stem)
    card = dict(totals)
    card.update({
        "slug": slug,
        "session_id": session_id or path.stem,
        "host": HOST,
        "transcript": str(path),
        "time_created": first_ms,
        "time_updated": last_ms,
        "billed": totals["tokens_input"] + totals["tokens_output"],
        "parts": parts,
        "storesize": path.stat().st_size,
        "requests": len(usage_by_request),
    })
    card["duration_ms"] = (None if first_ms is None or last_ms is None
                           else last_ms - first_ms)
    return card


def select(session_id=None, slug=None, latest=False, root=None, worktree=None):
    """Resolve a card the way run_card's CLI asks for one, or None."""
    if session_id:
        path = find_transcript(session_id, root)
        return load_card(path) if path else None
    candidates = project_transcripts(root, worktree=worktree)
    if latest:
        for path in candidates:
            card = load_card(path)
            if card is not None:
                return card
        return None
    if slug:
        for path in candidates:
            card = load_card(path)
            if card is not None and card["slug"] == slug:
                return card
    return None


# -- fixture capture ---------------------------------------------------------

KEEP_TOP = ("type", "uuid", "parentUuid", "timestamp", "sessionId",
            "requestId", "cwd", "version", "isSidechain", "agentId")
KEEP_MESSAGE = ("id", "model", "role")
# The usage keys the card reads; the rest (iterations, cache_creation,
# server_tool_use, ...) is dropped, which the capture check proves is safe.
KEEP_USAGE = ("input_tokens", "output_tokens", "cache_read_input_tokens",
              "cache_creation_input_tokens", "output_tokens_details")
SUBAGENTS_DIR = "subagents"
SUBAGENT_GLOB = "agent-*.jsonl"
COMMAND_CHARS = 200
# The tool_use input key that names what the call acted on, in precedence
# order: a shell command, a file path, a search pattern, an agent prompt.
COMMAND_KEYS = ("command", "file_path", "filePath", "notebook_path", "pattern",
                "path", "url", "skill", "query", "description", "prompt")


def byte_size(value):
    """UTF-8 length of a text, or of the JSON of anything else."""
    if isinstance(value, str):
        return len(value.encode("utf-8"))
    return len(json.dumps(value, ensure_ascii=False).encode("utf-8"))


def command_of(tool_input):
    """The first 200 chars of what a tool call acted on, or None."""
    if not isinstance(tool_input, dict):
        return None
    for key in COMMAND_KEYS:
        value = tool_input.get(key)
        if isinstance(value, str) and value.strip():
            return value[:COMMAND_CHARS]
    return None


def slice_block(block):
    """A content block reduced to its evidence (see the module docstring)."""
    if not isinstance(block, dict):
        return {"type": "text", "text_bytes": byte_size(block)}
    if any(k.endswith("_bytes") for k in block):
        return dict(block)              # already reduced: a slice re-slices to itself
    btype = block.get("type")
    if btype == "thinking":
        return {"type": btype, "thinking_bytes": byte_size(block.get("thinking", ""))}
    if btype == "text":
        return {"type": btype, "text_bytes": byte_size(block.get("text", ""))}
    if btype == "tool_use":
        out = {"type": btype, "id": block.get("id"), "name": block.get("name"),
               "input_bytes": byte_size(block.get("input", {}))}
        command = command_of(block.get("input"))
        if command is not None:
            out["command"] = command
        return out
    if btype == "tool_result":
        return {"type": btype, "tool_use_id": block.get("tool_use_id"),
                "is_error": bool(block.get("is_error", False)),
                "content_bytes": byte_size(block.get("content", ""))}
    return {"type": btype}


def slice_record(record):
    """The record with everything but its evidence removed; None to drop it."""
    rtype = record.get("type")
    if rtype in PART_TYPES:
        out = {k: record[k] for k in KEEP_TOP if k in record}
        message = record.get("message")
        if isinstance(message, dict):
            kept = {k: message[k] for k in KEEP_MESSAGE if k in message}
            usage = message.get("usage")
            if isinstance(usage, dict):
                kept["usage"] = {k: usage[k] for k in KEEP_USAGE if k in usage}
            content = message.get("content")
            if isinstance(content, list):
                kept["content"] = [slice_block(b) for b in content]
            elif isinstance(content, str):
                kept["content_bytes"] = byte_size(content)
            elif "content_bytes" in message:            # already reduced
                kept["content_bytes"] = message["content_bytes"]
            out["message"] = kept
        return out
    for title_type, key in TITLE_KEYS:
        if rtype == title_type:
            return {k: record[k] for k in ("type", key, "sessionId") if k in record}
    return None


def comparable(card):
    """The card fields a slice must reproduce (storesize is the file's own)."""
    return {k: card[k] for k in CARD_KEYS if k != "storesize"}


def subagent_transcripts(path):
    """The subagent transcripts Claude Code keeps beside a session file, in
    `<session-id>/subagents/agent-<id>.jsonl` (a `.meta.json` sits next to
    each, naming the agent type and the spawning tool_use). Sorted by name."""
    path = Path(path)
    folder = path.parent / path.stem / SUBAGENTS_DIR
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.glob(SUBAGENT_GLOB) if p.is_file())


def _write_slice(source, target):
    """Slice `source` into `target`; refuse (and unlink) on a card mismatch."""
    full = load_card(source)
    if full is None:
        raise ValueError(f"{source} holds no session")
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for record in _records(source):
        kept = slice_record(record)
        if kept is not None:
            lines.append(json.dumps(kept, sort_keys=True, separators=(",", ":")))
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    sliced = load_card(target)
    if sliced is None or comparable(sliced) != comparable(full):
        target.unlink()
        raise ValueError("slice of %s does not reduce to the same card as the "
                         "original; not written" % source.name)
    return full


def _discard(target):
    """Remove a refused slice and its subagent slices."""
    if target.is_file():
        target.unlink()
    shutil.rmtree(target.parent / target.stem, ignore_errors=True)


def capture(source, out_dir, verify=None):
    """Write `<id>.jsonl` (+ its subagent slices) and the index entry;
    refuse a slice that parses differently.

    `verify(source, target)` is an extra check run after the slices are
    written and before the index is; it raises ValueError to refuse
    (`run_trace.capture_claude` uses it to demand an identical trace).
    """
    source = Path(source)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    full = load_card(source)
    if full is None:
        raise ValueError(f"{source} holds no session")
    target = out_dir / f"{full['session_id']}.jsonl"
    _write_slice(source, target)
    subagents = {}
    try:
        for agent in subagent_transcripts(source):
            agent_target = out_dir / full["session_id"] / SUBAGENTS_DIR / agent.name
            agent_card = _write_slice(agent, agent_target)
            subagents[agent.stem] = {k: agent_card[k] for k in CARD_KEYS}
        if verify is not None:
            verify(source, target)
    except ValueError:
        _discard(target)
        raise
    index_path = out_dir / INDEX_FILE
    index = {}
    if index_path.is_file():
        index = json.loads(index_path.read_text(encoding="utf-8"))
    entry = {
        "captured_from": source.name,
        "captured_from_dir": source.parent.name,
        "card": {k: full[k] for k in CARD_KEYS},
    }
    if subagents:
        entry["subagents"] = subagents
    index[full["session_id"]] = entry
    index_path.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")
    return target


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--session-id", help="card this session id")
    parser.add_argument("--latest", action="store_true",
                        help="card the newest HFSS-project transcript")
    parser.add_argument("--projects-dir", help="override ~/.claude/projects")
    parser.add_argument("--capture", metavar="SESSION_ID",
                        help="write a verified fixture slice of this session")
    parser.add_argument("--out", help="fixture directory for --capture")
    args = parser.parse_args(argv)

    if args.capture:
        if not args.out:
            parser.error("--capture needs --out DIR")
        source = find_transcript(args.capture, args.projects_dir)
        if source is None:
            print(f"error: no transcript for session {args.capture}", file=sys.stderr)
            return 1
        try:
            target = capture(source, args.out)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        print(f"PASS: claude_transcript captured {target.name} from {source.parent.name}")
        return 0

    card = select(session_id=args.session_id, latest=args.latest,
                  root=args.projects_dir)
    if card is None:
        print("error: no transcript found", file=sys.stderr)
        return 1
    for key in ("host", "session_id", "transcript", "requests") + CARD_KEYS:
        print(f"{key}: {card[key]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
