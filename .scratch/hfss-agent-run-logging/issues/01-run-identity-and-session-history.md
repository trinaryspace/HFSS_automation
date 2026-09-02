# 01 — Run identity and phase-session history

**What to build:** A run is one workspace and three phase sessions plus their
subagents, and the workspace must be able to name all of them after the fact.
Today `scripts/session.py --phase` calls `hfss_spec.session.start`, which
overwrites `results/state/session.json` on every declaration; the last run's
file now describes a readout experiment and carries no `host` or
`host_session_id`, so the run's own sessions cannot be found from the
workspace. Fix by making the history append-only and the identity explicit.

- `hfss_spec/session.py`: `start()` also appends one line to
  `results/state/sessions.jsonl` — `{ts, phase, name, host, host_session_id,
  cwd, worktree, skill_commit, pid}`. `session.json` stays as the *current*
  session for the phase gate; the JSONL is the record. Re-declaring the same
  phase appends, never replaces.
- `results/state/run.json`, written on the first declaration and never
  rewritten: `{run_id, workspace, created_ts, task_doc}`. `run_id` is
  `<workspace-name>-<created date>`; a workspace copied for a second run gets
  a new one.
- `skill_commit` is `git rev-parse --short HEAD` of the checkout that owns the
  installed skill link, so a later report can say which skill text ran. The
  campaign log already records this by hand.
- `scripts/run_card.py` and `scripts/claude_transcript.select` accept the
  JSONL: a workspace with three declared sessions cards all three (one card
  each, plus a run total) instead of "the declared session".
- Subagent sessions are discovered from the parent: Claude Code keeps them in
  `<session-id>/` beside the transcript; opencode links them through the
  `session.parent_id` column. Record both mappings in the harness table in
  `skill/hfss-agent/reference/execution.md`.

**Blocked by:** None. Land before the next Tier-2 run.

**Status:** ready-for-agent

- [ ] `sessions.jsonl` appended by every `--phase` declaration; `session.json` unchanged in role
- [ ] `run.json` written once; a tier-0 test proves a second declaration does not rewrite it
- [ ] `run_card.py --workspace` prints one card per declared session and a `## Run total` block
- [ ] Subagent transcripts of a Claude Code session are enumerated (test on a captured fixture)
- [ ] Harness table row added for session history and subagent discovery
