# 04 — Step trace extractor over both stores

**What to build:** `scripts/run_trace.py`, the checked-in version of the
throwaway probes that produced `docs/hfss-agent-performance-analysis.md`.
It reads either harness store and writes one `steps.jsonl` per session with
one record per step:

```
{ts, session_id, host, parent_session_id, seq, role,      # user | assistant | tool_result
 kind,                                                    # text | reasoning | tool_use | tool_result
 tool, tool_use_id, command,                              # command: first 200 chars of the bash command / file path
 in_bytes, out_bytes, is_error,
 request_id, tokens_input, tokens_output, tokens_cache_read, tokens_cache_write, tokens_reasoning,
 latency_ms}                                              # ts of this step -> ts of the next
```

Sources and the mapping, stated in the module docstring the way
`claude_transcript.py` does:

- **Claude Code**: `assistant` records with `content[].type == tool_use`
  (`name`, `input`, `id`) and `user` records with `tool_result`
  (`tool_use_id`, `content`, `is_error`); usage once per `requestId`;
  thinking blocks are `kind=reasoning` with their byte size. Subagent
  transcripts under `<session-id>/` are extracted with `parent_session_id`
  set.
- **opencode**: the `part` table has only `id, message_id, session_id,
  time_created, time_updated, data`; the part type (tool / text /
  reasoning), tool name, input and output all live inside the `data` JSON.
  `session.parent_id` links subagent sessions (84 such rows exist today);
  token usage comes from the assistant message parts.

Usage: `run_trace.py --workspace W` (every session in `sessions.jsonl`, ticket
01), `--session-id`, `--slug`, `--transcript`, `--out DIR`. Default output is
`results/state/trace/<session-id>.steps.jsonl`. A `--top N` mode prints the N
heaviest outputs and reasoning blocks as a quick look without the report.

Fixtures: extend `claude_transcript.capture` so the slice keeps tool names,
byte sizes, `is_error` and thinking sizes, drops content, and is still
refused when it reduces to a different card. Capture one real Claude Code
session and one real opencode session (`hidden-falcon` or the Aug 18 solve
session) under `scripts/fixtures/`.

**Blocked by:** None.

**Status:** ready-for-agent

- [ ] Both backends produce the same `steps.jsonl` shape; a tier-0 test asserts the schema on both fixtures
- [ ] Usage counted once per request on Claude Code (the multi-record trap `claude_transcript.py` documents)
- [ ] Subagent sessions extracted with `parent_session_id`; totals with and without subagents agree with `run_card`
- [ ] `--top` reproduces the analysis doc's section 2 on the captured fixture (heaviest outputs and reasoning blocks)
- [ ] Capture refuses a slice whose card differs from the source
