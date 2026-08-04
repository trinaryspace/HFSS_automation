# 01 — Measurement harness + baseline

**What to build:** the run-card machinery. A small script (proposed path `scripts/run_card.py`, new dir) that reads the opencode DB (`~/.local/share/opencode/opencode.db`, path overridable) and, for a given session slug (or the latest session of the HFSS project), prints the run card: slug, created/updated, `tokens_input`, `tokens_output`, `tokens_reasoning`, `tokens_cache_read/write`, billed sum, part count, conversation store bytes, and a one-line duration. It also appends a `## Run card` section to `workspaces/<name>/summary.md` (or drafts it for the agent to paste). Baseline run: capture the numbers for `silent-engine` and record them in this ticket's resolution. The SQL in `docs/hfss-agent-performance-analysis.md` §10 is the reference.

**Status:** ready-for-agent
**Blocked by:** none (independent of the rest; do first so the pilot has a measuring stick)

- [x] `scripts/run_card.py` prints the run card for a named session slug
- [x] Baseline for `silent-engine` captured and recorded below
- [ ] Run-card section template lands in the workspace summary skeleton (with ticket 04)
- [x] Script tolerates a locked/WAL DB (it is read while opencode runs)

## Comments

- 2026-08-04: Created in the grill-with-docs session; acceptance thresholds are 01 + 06's contract (≥50% tokens, ≥40% parts, ≥40% wall excl. solve vs the baseline below).
- 2026-08-04: Ticket 01 implemented — `scripts/run_card.py` (new `scripts/` dir), `scripts/test_run_card.py` (10/10 pass). Usage: `python scripts/run_card.py --slug <slug>` or `--latest` (latest HFSS-project session); `--summary <path>` appends/replaces an idempotent `## Run card` section in `summary.md`; DB path via `--db` flag > `OPENCODE_DB` env var > `~/.local/share/opencode/opencode.db`, opened read-only (`file:...?mode=ro`, 30 s busy timeout) so it works while opencode holds the DB in WAL. Baseline captured with the reference SQL of analysis §10:

  ```
  slug: silent-engine
  created: 2026-08-03T04:43:14Z
  updated: 2026-08-03T06:07:12Z
  duration: 1 h 23 min 58 s
  tokens_input: 329760
  tokens_output: 68370
  tokens_reasoning: 0
  tokens_cache_read: 9186701
  tokens_cache_write: 0
  billed: 398130
  parts: 424
  store_bytes: 1082759
  ```

  vs analysis §1: input 329,760 / output 68,370 / cache-read 9,186,701 / billed 398,130 — all exact. Two notes for the record: (1) measured wall time is 1 h 24 min; the doc's "~1.6 h" was an eyeball estimate (its other row, `playful-river`, measures 4 h 49 min vs "~2.3 h"). (2) `tokens_reasoning` and `tokens_cache_write` are 0 in this DB version — reasoning volume was originally derived from part payloads (§2), not this column; if reasoning tracking matters for the pilot comparison, use the part-payload method, not this column.
