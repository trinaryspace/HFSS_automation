# 19 — Reconcile and commit the ADR 0006 amendment

**What to build:** ADR 0006's solve-lifecycle contract gains what the pilot proved necessary and the planning session settled: the stage-aware watchdog (stage/status model, evidence-before-claiming rules — complete / stalled / aborted), the banking contract (post-solve confirm writes the solved marker), and the teardown guard (banked → close_projects=False; unbanked-with-evidence → refused). A draft amendment from the planning session already sits in the tree, uncommitted; this ticket reconciles its wording against the code landed by tickets 13 and 14 (which must exist first) and commits the final text. Execution text cross-references are updated to point at the amended contract.

**Blocked by:** 13 — bank-before-teardown, 14 — stage-aware solve watchdog.

**Status:** ready-for-agent

- [ ] ADR 0006 amendment committed, wording matching the landed watchdog and teardown-guard behavior
- [ ] Cross-references in the execution text updated to the amended contract
- [ ] No other tickets' files bundled into the commit

## Comments

- 2026-08-14: **SKILL.md reconciled to the amended ADR 0006.** It carried the
  pre-amendment solve ceremony while `execution.md` carried the new one:
  `confirm_solve`, `solved.txt`, `banked` and `close_projects` appeared 0
  times in SKILL.md and once each in execution.md. The skill therefore told
  the agent to solve but never to bank, so a run would reach teardown
  unbanked. Not destructive any more — ticket 01's repaired guard now
  *refuses* that teardown rather than purging — but it would burn steps on a
  confused escalation, and it was about to do so on the ticket-06 run.
- Landed in SKILL.md: hard rule 8 rewritten (stage-aware watchdog, evidenced
  terminal states, no predicted output count, bank-before-teardown, and
  resolve-once after an anomaly); the Solve+QA section gained the
  skip-if-no-stale cleanup, the `Popen(DETACHED_PROCESS)` launcher, the
  0/2/3 exit semantics, an explicit bank step, and the one-shot readout
  policy; release hygiene now forbids reaping before `solved.txt` exists.
- **Root cause addressed, not just the instance.** Nothing checked SKILL.md
  against the amendment, which is why it drifted. `verify_skill.py` gained
  four marker groups — bank-before-teardown, stage-aware watchdog,
  resolve-once, readout-one-shot — plus `confirm_solve.py`,
  `profile_evidence.py` and `real_fixtures.py` in the template src list. Tier
  0 green.
- Still open in this ticket: committing the amended ADR 0006 text itself
  (currently uncommitted in the working tree).
