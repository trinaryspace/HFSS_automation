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

**Status:** ready-for-human

- [x] `sessions.jsonl` appended by every `--phase` declaration; `session.json` unchanged in role
- [x] `run.json` written once; a tier-0 test proves a second declaration does not rewrite it
- [x] `run_card.py --workspace` prints one card per declared session and a `## Run total` block
- [x] Subagent transcripts of a Claude Code session are enumerated (test on a captured fixture)
- [x] Harness table row added for session history and subagent discovery

## Comments

### 2026-09-02 — landed

What landed, by file:

- `hfss_spec/session.py`: `start()` now also appends one line to
  `results/state/sessions.jsonl` (`ts`, `ts_ms`, `phase`, `name`, `host`,
  `host_session_id`, `cwd`, `worktree`, `skill_commit`, `pid`) and writes
  `results/state/run.json` once (`run_id`, `workspace`, `created_ts`,
  `created_ms`, `task_doc`). `session.json` is written exactly as before,
  same keys. `skill_commit` is `git rev-parse --short HEAD` in the checkout
  that holds `hfss_spec/` (the installed skill links back into it); `""`
  when git is absent. New helpers: `history()`, `run_info()`,
  `ensure_run()`, `skill_commit()`, `worktree_of()`.
- `hfss_spec/test_session.py`: `TestHistory` — four declarations append
  four lines (a re-declared phase appends); `session.json` still the
  current session with its original key set; `run.json` bytes identical
  after a second declaration with a different name and `task_doc`; a
  copied workspace gets its own `run_id`; `skill_commit` recorded and `""`
  under a missing git; a torn history line is skipped.
- `scripts/session.py`: `--task-doc`; the PASS line carries `run=<run_id>
  declared=<n>`; the report mode lists the history.
- `scripts/claude_subagents.py` (new, small; can move into
  `claude_transcript.py` once that file is free): `discover(transcript)`
  and `capture_tree(transcript, out)`. **The real shape is one level deeper
  than this ticket's prose**: `<project>/<session-id>/subagents/
  agent-<agentId>.jsonl` with an `agent-<agentId>.meta.json` beside each
  (`agentType`, `description`, `toolUseId`, `spawnDepth`), and the records
  carry the *parent's* `sessionId`, so the agent id survives only in the
  filename. `claude_transcript.capture` therefore names every subagent
  slice after the parent; `capture_tree` places each verified slice by
  filename and writes a `subagents/index.json` with the cards of the full
  originals.
- Fixture: this box did have subagent directories (three HFSS sessions).
  Captured `a0e9c38f-3117-4d93-8086-9b4f16ee0d52` — the parent slice via
  `claude_transcript.capture` and its two real subagents via
  `capture_tree` — into `scripts/fixtures/claude-code/`, meta files copied
  byte-for-byte. Every slice reduced to the same card as its original.
- `scripts/run_card.py`: `--workspace` / `--summary` with no explicit
  selection and a `sessions.jsonl` present cards **every** declared
  session from its own host's store (one card each, `## <phase> — <slug>`),
  folds each Claude Code session's subagents in (listed per session, summed
  as `billed_subagents`), and ends with `## Run total` (`run_id`,
  `skill_commit`, sessions, unresolved, span, wall axis, summed tokens,
  outcome, cost per completion). A session declared with no id is printed
  as `unresolved`, never dropped. In `summary.md` the whole run sits under
  one `## Run card` heading with `###` sub-blocks so the upsert stays
  idempotent. A workspace with only the old `session.json` behaves exactly
  as before (all previous tests untouched).
- `skill/hfss-agent/reference/execution.md`: two harness rows — session
  history / run identity, and subagent discovery (opencode:
  `session.parent_id`; Claude Code: the `subagents/` tree above).

Not done, stated plainly: opencode subagent sessions are documented
(`parent_id`) but not folded into the run total; the opencode entry in a
history resolves by slug only. `docs/agents/harnesses.md` was not touched
(outside this ticket's file list).

Verification, verbatim:

- `PASS: tier0 suites=15 failed=0 elapsed=20.6s`
- `python skill/hfss-agent/verify_skill.py` → `ALL PASS`
- `python scripts/test_run_card.py` → `Ran 62 tests in 2.781s` / `OK`
- `python hfss_spec/test_session.py` → `PASS: session tests=23 failed=0`

Two worktree-environment gaps had to be closed before tier0 could run
here, neither a code change: the gitignored real artifact
`workspaces/bowtie-3500-pilot/results/state/model_snapshot.json` was
copied byte-for-byte from the main checkout, and
`python scripts/install_skill.py` was run to make the `.claude/skills/`
link. Both live in gitignored paths.
