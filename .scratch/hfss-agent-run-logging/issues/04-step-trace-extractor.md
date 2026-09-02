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

**Status:** ready-for-human

- [x] Both backends produce the same `steps.jsonl` shape; a tier-0 test asserts the schema on both fixtures
- [x] Usage counted once per request on Claude Code (the multi-record trap `claude_transcript.py` documents)
- [x] Subagent sessions extracted with `parent_session_id`; totals with and without subagents agree with `run_card`
- [x] `--top` reproduces the analysis doc's section 2 on the captured fixture (heaviest outputs and reasoning blocks)
- [x] Capture refuses a slice whose card differs from the source

## Comments

### 2026-09-02 — landed

- `scripts/run_trace.py`: the extractor. `DbStore` (opencode, read-only URI
  via `run_card.connect`; every query per session id and indexed, verified
  with `explain query plan` — `part` is never scanned) and `SliceStore`
  (a captured family) feed one `trace_opencode`; `trace_transcript` /
  `trace_claude` read a Claude Code transcript and its
  `<id>/subagents/agent-*.jsonl`. Mapping stated in the module docstring.
  CLI: `--workspace` (reads ticket 01's `results/state/sessions.jsonl`,
  falls back to `session.json`, tolerant of both absent), `--session-id`,
  `--slug`, `--transcript`, `--slice`, `--out`, `--top N`, `--no-subagents`,
  `--capture ID --out DIR` for either host.
- `scripts/claude_transcript.py`: the slice now keeps tool names, byte
  sizes, `is_error` and thinking sizes (content dropped, usage trimmed to
  the five keys the card reads), slices subagent transcripts into the same
  layout, still refuses on a card mismatch, and takes a `verify` hook that
  `run_trace.capture_claude` uses to refuse a slice that traces differently.
- Fixtures: `scripts/fixtures/claude-code/f0c832a3-…` recaptured (same
  card, now with tool blocks); `scripts/fixtures/opencode/ses_fe9ae6dd3ffe…`
  = `neon-eagle`, the Aug 18 patch-array-5800 solve session, with its
  subagents `cosmic-knight` and `hidden-falcon` (484 KB). Both captures are
  byte-stable on rerun.
- `scripts/test_run_trace.py` (31 tests) registered in tier 0 as `run-trace`.
  The opencode database path is tested on a SQLite file materialized FROM
  the real slice, with a test asserting it traces identically (rule 3).
- Two things the real fixtures taught: Claude Code stores thinking blocks
  with an empty text (signature only), so reasoning bytes are 0 there and
  `tokens_reasoning` is the measure; and on 2.1.258 the records of one
  request carry a running usage — the last record has the final numbers
  (output 36 -> 2356 in one request of a0e9c38f). `run_trace` keeps the
  last, as `load_card` does; my first draft kept the first and the fixture
  caught it.

Verification lines, verbatim:

    PASS: run_trace tests=31 failed=0
    ALL PASS                                   (skill/hfss-agent/verify_skill.py)
      run-trace          ok      2.7s
    FAIL: tier0 suites=16 failed=1 (run-card) elapsed=21.2s

The one tier-0 failure is `test_three_declared_sessions_card_three_times_plus_a_total`
in ticket 01's in-flight `TestRunFromHistory` (`scripts/test_run_card.py`,
active wall vs a fixed 2026-08-05 gate), which is not mine to edit; every
other suite, including the pre-existing run-card tests over the recaptured
f0c832a3 slice, passes.

Not done / for the reviewer:

- The Claude Code subagent check runs on ticket 01's
  `claude-code/a0e9c38f-…` capture (made with the old slicer through their
  `scripts/claude_subagents.py`, so it holds usage and layout but no tool
  blocks). I used it read-only rather than overwrite a parallel agent's
  files; recapturing it with the merged slicer (`run_trace.py --capture
  a0e9c38f-… --out scripts/fixtures/claude-code`) would give the subagent
  slices tool steps too. `claude_transcript.capture`'s subagent slicing and
  `claude_subagents.capture_tree` overlap; one should go after the merge.
- `--top` reproduces section 2's shape (tool-call histogram, reasoning
  share, heaviest outputs and reasoning blocks) on `neon-eagle`; the doc's
  literal numbers are from `silent-engine`, which was not captured.
