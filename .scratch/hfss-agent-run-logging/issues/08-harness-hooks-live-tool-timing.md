# 08 — Harness hooks for live tool timing (optional)

**What to build:** A workspace-local tool log written *during* the run by
the harness, for the two things the transcript does not carry well: the
bash exit code, and wall time that is unaffected by how the transcript
batches records. Only Claude Code has hooks in this repo today;
`.claude/settings.json` holds a permission allow-list and nothing else.

- `scripts/hook_log.py`, invoked by `PreToolUse` and `PostToolUse` hooks in
  `.claude/settings.json`, reads the hook JSON on stdin and appends
  `{ts, session_id, phase, tool, command, exit_code, duration_ms}` to
  `results/state/tools.jsonl` of the active workspace.
- The active workspace is resolved from the session id through
  `~/.hfss-agent/sessions.json`, which `scripts/session.py --phase` writes
  (session id → workspace path). Gitignored, per-machine. A session with no
  entry logs nothing and never errors.
- The hook must return within ~50 ms and never block a tool call: append
  and exit, no parsing of the command.
- opencode: its plugin API exposes `tool.execute.before/after`; note the
  equivalent as a follow-up in the harness table rather than building it
  here.

Why optional: ticket 04 derives tool, bytes, error flag and inter-step
latency from the transcript already. This ticket adds exit codes and
tighter timing, and a live file a maintainer can tail during a run. Decide
after ticket 06 shows whether the transcript-derived timing is good enough.

**Blocked by:** 01.

**Status:** ready-for-human

- [x] Hook installed by `scripts/install_skill.py` (settings merge, not overwrite) and removable
- [x] `hook_log.py` appends in under 50 ms and exits 0 on every malformed input
- [x] `run_trace.py` merges `tools.jsonl` when present, preferring its exit codes and durations
- [x] Harness table row for hooks, with the opencode plugin follow-up named

## Comments

### 2026-09-02 — landed

Two corrections to the ticket's premise, both read off Claude Code 2.1.258
itself (its schema in the binary, then a real capture): **a non-zero Bash
exit is not a `PostToolUse` at all** — the tool raises, and the harness
fires `PostToolUseFailure` with `error: "Exit code 3"` (code on the first
line, stderr and stdout after it) and `is_interrupt`; a successful call's
`tool_response` is `{stdout, stderr, interrupted, isImage, noOutputExpected}`
with no exit code in it. So the hook is installed on three events, not
two, and `exit_code` is 0 on a PostToolUse of a Bash call, the number on
the failure's first line, and null for tools that have no exit code. Also:
every payload carries `tool_use_id` (the stamp is keyed by it), and the
harness sends its own `duration_ms` ("tool execution time, excludes
permission-prompt and hook time"), kept as `exec_ms` beside the stamp wall.

**A real hook payload was captured.** Hooks are snapshotted when a session
starts, so an edit to `settings.json` could not fire in this session; a
headless `claude -p` session was run in this checkout instead (`echo
hello`, then `exit 3`) with the hook in `--capture` mode. The four raw
stdin payloads it received are `scripts/fixtures/hooks/{PreToolUse,
PostToolUse,PostToolUseFailure}.<tool_use_id>.json`, byte-for-byte, and
that same session's transcript is beside them as
`45641dd8-dbcc-4f08-8f92-90237c4a0f63.jsonl` (sliced by `run_trace.py
--capture`, which refuses a slice that traces differently), so the hook
lines and the steps they join come from one real run. A second headless
session with a preset `--session-id`, registered through `scripts/session.py
--phase build`, then ran under the **installed** settings and wrote both
lines to its workspace's `tools.jsonl` — the end-to-end path is proven, not
inferred.

What landed, by file:

- `scripts/hook_log.py` (new, stdlib, `python -I -S` so the interpreter
  starts in ~30 ms): `PreToolUse` writes `~/.hfss-agent/pending/<session>.<tool_use_id>`
  (falls back to `<session>.<tool>` when a payload has no id);
  `PostToolUse` / `PostToolUseFailure` consume it and append one line —
  `{ts, session_id, phase, tool, command, exit_code, duration_ms, exec_ms,
  tool_use_id, is_error}` (the ticket's seven keys plus the three named) —
  to `<workspace>/results/state/tools.jsonl`. The workspace and phase come
  from `~/.hfss-agent/sessions.json`; no entry, no map, or any malformed
  stdin → nothing written, exit 0, never an exception out of `main`.
  `--capture DIR` keeps the raw stdin as a fixture. `HFSS_AGENT_HOME`
  relocates the map (tests).
- `hfss_spec/session.py`: `agent_home`, `sessions_map_path`,
  `load_sessions_map`, `register_session` (entry `{workspace, phase, host,
  ts, ts_ms}`, other sessions kept, re-declaration overwrites, written via
  temp file + `os.replace`, never raises). **The CLI registers, not
  `start()`**: every suite in the repo declares sessions through `start()`
  and would otherwise map the live Claude Code session to a temp dir.
- `scripts/session.py --phase`: registers when the declaration has a
  session id (`CLAUDE_CODE_SESSION_ID` or `--session-id`); the PASS line
  gains `hook_map=registered|unregistered`.
- `scripts/install_skill.py`: `install()` also merges the three hooks into
  `.claude/settings.json` (only what is missing is added; `permissions`,
  other hooks, other keys untouched; idempotent, byte-stable on a second
  run); `--hooks` / `--remove-hooks` do only that; `--remove` strips them
  with the links; `--check` prints a `hooks` row and fails when one of the
  three is absent. The command is
  `python -I -S "${CLAUDE_PROJECT_DIR}/scripts/hook_log.py" || exit 0`,
  matcher `*`, timeout 5 s: `CLAUDE_PROJECT_DIR` makes it independent of the
  session's cwd, and `|| exit 0` means a missing python or script can never
  return 2 — the one exit code that would block a tool call. It runs under
  the shell Claude Code gives hooks (Git Bash on Windows when installed,
  which the sandboxed Bash tool needs anyway).
- `.claude/settings.json`: the merged result — the allow-list unchanged,
  the three hook entries after it. Tracked, so a clone carries them.
- `scripts/run_trace.py`: `read_tool_log`, `merge_tool_log`,
  `merge_tool_log_families`; `--workspace` merges
  `<ws>/results/state/tools.jsonl` when present (`--tools PATH` to point
  elsewhere); the PASS line gains `hooked=N`. A line joins its tool_use by
  `tool_use_id` (else the first unjoined call with the same session, tool
  and command); on a join the tool_result's `is_error` follows the hook's
  exit code (non-zero → error, zero → not, whatever the harness flagged)
  and the tool_use's `latency_ms` becomes the hook's `duration_ms`.
  **No key was added to `STEP_KEYS`** — `hfss_spec/test_painpoints.py`'s
  key-set assertion is untouched; the exit code itself stays in
  `tools.jsonl`, which sits beside the trace for anyone who wants the number.
- `scripts/test_hook_log.py` (34 tests, standalone, one PASS line; for
  tier 0 as `hook-log` — ticket 07 owns `tier0.py`): the contract asserted
  on the captured files; a Pre+Post pair and sixteen malformed inputs each
  handled in-process under 50 ms (measured, asserted); the script exits 0
  on malformed stdin; the whole process best-of-3 printed for information
  (46 ms here, interpreter included); capture byte-for-byte; the CLI
  registration; the settings merge / idempotence / removal restoring the
  original key for key; the merge on the real transcript. `hfss_spec/
  test_session.py` +5 (`TestSessionMap`), `scripts/test_run_trace.py` +2.
- `.gitignore`: nothing to add — the map is outside the repo and
  `tools.jsonl` lives under the already-ignored `workspaces/*/results/`.

**Harness-table row for `skill/hfss-agent/reference/execution.md`
(ticket 09 owns the file; add verbatim):**

`| Live tool log (exit codes, wall per call) | not wired: opencode's plugin API has `tool.execute.before` / `tool.execute.after`; a plugin appending the same `tools.jsonl` line is the follow-up (ticket 08 comment) | `PreToolUse` / `PostToolUse` / `PostToolUseFailure` hooks in `.claude/settings.json` (installed and checked by `python scripts/install_skill.py`) run `scripts/hook_log.py`, which appends `{ts, session_id, phase, tool, command, exit_code, duration_ms, …}` to `results/state/tools.jsonl` of the workspace that `scripts/session.py --phase` registered for this session in `~/.hfss-agent/sessions.json`; an undeclared session logs nothing. A non-zero Bash exit arrives as `PostToolUseFailure` (`error: "Exit code N"`), not as a PostToolUse. `scripts/run_trace.py --workspace` merges the file into the trace |`

**Follow-ups, named:**

- *opencode plugin* (`hfss-agent-tool-log`): a `.opencode/plugin/` module
  registering `tool.execute.before` (stamp) and `tool.execute.after`
  (append the same line shape, `exit_code` from the bash tool's result,
  `session_id` = the opencode session id, workspace from the same
  `~/.hfss-agent/sessions.json` — which needs `scripts/session.py --host
  opencode --session-id <ses_…>` to be given the real session id, not the
  slug). `run_trace.merge_tool_log` already joins by `tool_use_id`
  (`callID` there) and needs no change.
- `scripts/run_report.py` refreshes traces through `run_trace.trace_claude`
  + `write_steps` directly, so its own refresh does not merge `tools.jsonl`
  yet; one call to `run_trace.merge_tool_log(steps,
  run_trace.read_tool_log(<ws>/results/state/tools.jsonl))` before
  `write_steps` closes that (ticket 06/10's file).
- Stale stamps: a tool that never completes (session killed mid-call)
  leaves its file in `~/.hfss-agent/pending/`; harmless and tiny, not
  pruned (a directory listing is the one thing that could grow past the
  budget).

Verification, verbatim:

- `PASS: hook_log tests=34 failed=0`
- `PASS: session tests=32 failed=0`
- `PASS: run_trace tests=38 failed=0`
- `PASS: install_skill targets=3 hooks=3/3 failed=0`
- `PASS: painpoints tests=68 failed=0`, `PASS: run_report tests=29 failed=0`,
  `python scripts/test_run_card.py` → `Ran 80 tests` / `OK`,
  `python skill/hfss-agent/verify_skill.py` → `ALL PASS` (unchanged suites, run to confirm)
- `PASS: run_trace captured 45641dd8-dbcc-4f08-8f92-90237c4a0f63.jsonl from C--Users-afpim-Repos-HFSS-automation--claude-worktrees-run-logging-plan`
- end-to-end (installed settings, headless session `7b1c2d3e-…` registered with `--phase build`):
  `PASS: session declared phase=build name=e2e budget=60 host=claude-code session_id=7b1c2d3e-0808-4e2e-9a1b-0d0e0f101112 run=e2e-ws-2026-09-02 declared=1 hook_map=registered`, then
  `{"ts":1788388085844,…,"tool":"Bash","command":"echo hello","exit_code":0,"duration_ms":3252,"exec_ms":3114,…,"is_error":false}` and
  `{"ts":1788388088526,…,"command":"exit 3","exit_code":3,"duration_ms":236,"exec_ms":102,…,"is_error":true}` in `results/state/tools.jsonl`, both stamps consumed.
