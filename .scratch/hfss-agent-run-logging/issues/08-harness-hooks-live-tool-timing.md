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

**Status:** needs-triage

- [ ] Hook installed by `scripts/install_skill.py` (settings merge, not overwrite) and removable
- [ ] `hook_log.py` appends in under 50 ms and exits 0 on every malformed input
- [ ] `run_trace.py` merges `tools.jsonl` when present, preferring its exit codes and durations
- [ ] Harness table row for hooks, with the opencode plugin follow-up named
