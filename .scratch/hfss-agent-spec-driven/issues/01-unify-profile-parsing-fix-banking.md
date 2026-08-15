# 01 — Unify profile-status parsing; repair the banking guard (P0, live bug)

**What to build:** One profile parser, imported by every consumer. Today there
are two: `poll_solve._PROFILE_STATUS` correctly tolerates AEDT's escaped-quote
serialization (`\'Status\', \'Normal Completion\'`), while
`confirm_solve.STATUS_TOKEN_RE` (`r"'Status'\s*,\s*'([^']+)'"`) does not — and
therefore returns `None` on **9 of 9** real profiles in this repo's workspaces.
The failure is silent and total: `newest_terminal_profile()` → `None` →
`ws_common.guard_verdict()` → `GUARD_PROCEED` → teardown with
`close_projects=True` → the solved results are purged. That is precisely the
incident ticket 13 was written to make structurally impossible, and it is fully
live today; measured on `bowtie-3500`, `bowtie-3500-pilot`, and `bowtie-3670`,
all three return `proceed`. Extract profile parsing (terminal status, stop time,
stage ledger) into a single module — `profile_evidence.py` — with `poll_solve`,
`confirm_solve`, and `ws_common` all importing it. Ticket 14's Comments already
document the escaped-quote quirk and the several-Solution-Process-groups quirk
correctly; the unified parser is where that knowledge now lives, not in a
comment thread.

**Blocked by:** None — can start immediately. Do this first: every downstream
measurement is untrustworthy while banking is broken.

**Status:** ready-for-human

- [x] Exactly one implementation of terminal-status / stop-time / stage-ledger parsing; `grep` shows no second regex for `Status` anywhere in `src/`
- [x] `terminal_status()` returns the correct value for all 9 real profiles under `workspaces/**` (including the `Engine Detected Error` one in `bowtie-3500`)
- [x] `guard_verdict()` returns `refuse` for the three solved-but-unbanked workspaces, and `banked` once `confirm_solve.py` has run
- [x] `confirm_solve.py` writes `results/state/solved.txt` (status + sweep-point count) against a real workspace and exits 0
- [x] Regression test asserts the escaped form specifically, driven from `fixtures/real/` (ticket 03), not a hand-written string
- [x] Template and pilot workspace copies synced; full suite green

## Comments

- 2026-08-14: **DONE.** New `profile_evidence.py` is the single parser;
  `poll_solve`, `confirm_solve` and `ws_common` (via `confirm_solve`) all
  import it, and their local copies are gone. The pattern now tolerates
  both the bare `'Status', 'X'` and the escaped `\'Status\', \'X\'` form
  by making the leading backslash optional at each quote, and Stop Time /
  Status are captured independently rather than requiring both on one line.
- **Measured before/after on the 9 real profiles.** Before: `confirm_solve`
  returned `None` on 9/9, so `guard_verdict()` said `proceed` for
  `bowtie-3500`, `bowtie-3500-pilot` and `bowtie-3670` — teardown would
  have purged all three. After: correct status on 9/9 (including
  `DV86_S83_V106.profile` -> `Engine Detected Error`), and all three
  workspaces now score `refuse` until banked.
- **Multi-group semantics preserved and now pinned.** `DV2487_S1911_V0.profile`
  holds two Solution Process groups (an error session and its rerun); the
  parser reports the LAST group, verified against the captured artifact.
  This is stricter than the old `confirm_solve`, which took the last Status
  anywhere in the file.
- **Banking verified without mutating the workspaces**, using
  `confirm(project, state_dir=<temp>)`: all three bank cleanly, exit 0, and
  the non-Normal one carries its escalation line. The real workspaces were
  left unbanked deliberately — writing `solved.txt` into them is the user's
  call, and the guard now protects them either way by refusing teardown.
- `verify_skill.py` gained a check that fails if any template `src/` module
  other than `profile_evidence.py` compiles its own `Status` pattern, so a
  second parser cannot reappear silently.
- Template and pilot workspace copies synced. Tier 0 green (7/7).
