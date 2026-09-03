"""Subagent transcripts of a Claude Code session: discovery and capture.

A Claude Code session spawns subagents (the Agent tool), and each one is its
own transcript. Looked at on disk (2026-09-02, `~/.claude/projects/`), the
layout beside a parent transcript `<project>/<session-id>.jsonl` is:

    <project>/<session-id>/subagents/agent-<agentId>.jsonl
    <project>/<session-id>/subagents/agent-<agentId>.meta.json
    <project>/<session-id>/tool-results/<id>.txt

The `.meta.json` is one line — `{"agentType", "description", "toolUseId",
"spawnDepth"}` — and the transcript's records carry `isSidechain: true`,
`agentId`, and the **parent's** `sessionId`, not their own. Two consequences
this module is built around:

- discovery walks `<session-id>/subagents/` (and tolerates `.jsonl` files
  directly under `<session-id>/`, the shape the ticket described), keyed by
  the `agent-<id>` filename because that is the only place the agent's own id
  survives a slice;
- `claude_transcript.capture` names its slice after the card's `session_id`,
  which for a subagent is the parent's, so `capture_tree` places each slice
  by filename and records the cards in a `subagents/index.json` of its own.

The card of a subagent is `claude_transcript.load_card` unchanged (usage once
per requestId, parts = user + assistant records), annotated with `agent_id`,
`agent_type`, `description` and `parent_session_id`; its `slug` is the
description the parent gave it, since a subagent never has a title record.

Usage:
    python scripts/claude_subagents.py --session-id <id>             # list cards
    python scripts/claude_subagents.py --capture <id> --out DIR      # fixture tree

Stdlib only, Python 3.10 compatible. Lives here rather than in
`claude_transcript.py` only because that file is under someone else's edit;
it can move.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import claude_transcript  # noqa: E402

SUBAGENTS_DIR = "subagents"
META_SUFFIX = ".meta.json"
AGENT_PREFIX = "agent-"
INDEX_FILE = "index.json"


def session_dir(transcript):
    """`<session-id>/` beside the transcript (may not exist)."""
    transcript = Path(transcript)
    return transcript.parent / transcript.stem


def subagent_transcripts(transcript):
    """The subagent .jsonl files of a parent transcript, sorted by name."""
    root = session_dir(transcript)
    if not root.is_dir():
        return []
    found = []
    for folder in (root / SUBAGENTS_DIR, root):
        if not folder.is_dir():
            continue
        for path in folder.iterdir():
            if path.is_file() and path.suffix == ".jsonl":
                found.append(path)
    return sorted(set(found), key=lambda p: p.name)


def agent_id_of(path):
    """`agent-a7c9f335c3a8f10e1.jsonl` -> `a7c9f335c3a8f10e1`; else the stem."""
    stem = Path(path).stem
    return stem[len(AGENT_PREFIX):] if stem.startswith(AGENT_PREFIX) else stem


def read_meta(path):
    """The `.meta.json` beside a subagent transcript, or {} when absent."""
    meta = Path(path).with_name(Path(path).stem + META_SUFFIX)
    try:
        data = json.loads(meta.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def load_subagent_card(path, parent_session_id=None):
    """The run-card dict of one subagent transcript, or None if empty."""
    path = Path(path)
    card = claude_transcript.load_card(path)
    if card is None:
        return None
    meta = read_meta(path)
    agent_id = agent_id_of(path)
    card["agent_id"] = agent_id
    card["agent_type"] = str(meta.get("agentType") or "")
    card["description"] = str(meta.get("description") or "")
    # The records carry the parent's sessionId; keep that fact visible.
    card["parent_session_id"] = parent_session_id or card["session_id"]
    card["slug"] = card["description"] or f"{AGENT_PREFIX}{agent_id}"
    return card


def discover(transcript):
    """Every subagent card of a parent transcript, in filename order."""
    transcript = Path(transcript)
    cards = []
    for path in subagent_transcripts(transcript):
        card = load_subagent_card(path, parent_session_id=transcript.stem)
        if card is not None:
            cards.append(card)
    return cards


# -- fixture capture ---------------------------------------------------------

def capture_tree(transcript, out_dir):
    """Capture the parent slice and every subagent slice, same tree shape.

    Each slice goes through `claude_transcript.capture` (which refuses a
    slice that reduces to a different card) into a scratch dir, then is
    placed at `<out>/<session-id>/subagents/agent-<id>.jsonl`; the
    `.meta.json` is copied byte-for-byte, being real and tiny. The cards of
    the FULL originals land in `<out>/<session-id>/subagents/index.json`,
    keyed by agent id, so a test can assert the slice still agrees.
    """
    transcript = Path(transcript)
    out_dir = Path(out_dir)
    parent = claude_transcript.capture(transcript, out_dir)
    target_dir = out_dir / transcript.stem / SUBAGENTS_DIR
    scratch = out_dir / transcript.stem / ".capture"
    index = {}
    written = []
    for source in subagent_transcripts(transcript):
        full = load_subagent_card(source, parent_session_id=transcript.stem)
        if full is None:
            continue
        scratch.mkdir(parents=True, exist_ok=True)
        sliced = claude_transcript.capture(source, scratch)
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / source.name
        target.write_bytes(sliced.read_bytes())
        sliced.unlink()
        meta = source.with_name(source.stem + META_SUFFIX)
        if meta.is_file():
            (target_dir / meta.name).write_bytes(meta.read_bytes())
        index[full["agent_id"]] = {
            "captured_from": source.name,
            "captured_from_dir": f"{source.parent.parent.name}/{source.parent.name}",
            "meta": read_meta(source),
            "card": {k: full[k] for k in claude_transcript.CARD_KEYS},
        }
        written.append(target)
    for leftover in (scratch / claude_transcript.INDEX_FILE,):
        if leftover.is_file():
            leftover.unlink()
    if scratch.is_dir():
        scratch.rmdir()
    if written:
        (target_dir / INDEX_FILE).write_text(
            json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return parent, written


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--session-id", help="list the subagent cards of this session")
    parser.add_argument("--transcript", help="parent transcript path (instead of --session-id)")
    parser.add_argument("--projects-dir", help="override ~/.claude/projects")
    parser.add_argument("--capture", metavar="SESSION_ID",
                        help="write verified fixture slices of the session and its subagents")
    parser.add_argument("--out", help="fixture directory for --capture")
    args = parser.parse_args(argv)

    if args.capture:
        if not args.out:
            parser.error("--capture needs --out DIR")
        source = claude_transcript.find_transcript(args.capture, args.projects_dir)
        if source is None:
            print(f"error: no transcript for session {args.capture}", file=sys.stderr)
            return 1
        try:
            parent, written = capture_tree(source, args.out)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        print(f"PASS: claude_subagents captured {parent.name} + {len(written)} "
              f"subagent slice(s) from {source.parent.name}")
        return 0

    if args.transcript:
        transcript = Path(args.transcript)
    elif args.session_id:
        transcript = claude_transcript.find_transcript(args.session_id, args.projects_dir)
    else:
        parser.error("give --session-id, --transcript, or --capture")
    if transcript is None or not transcript.is_file():
        print("error: no transcript found", file=sys.stderr)
        return 1
    cards = discover(transcript)
    for card in cards:
        print(f"{card['agent_id']}  {card['agent_type'] or '-':<16} "
              f"billed={card['billed']:<8} parts={card['parts']:<5} "
              f"requests={card['requests']:<4} {card['description']}")
    print(f"PASS: claude_subagents session={transcript.stem} subagents={len(cards)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
