# 17 — Readout one-shot policy (post-analysis, deferred)

**What to build:** The scripted-readout archaeology ends: at most one scripted Readout attempt per session (one retry on a fresh attach), then the plot goes to the user via the UI — never the multi-shape exploration of the pilot. The execution text's current "re-attach and retry until it works" guidance is replaced by this one-shot policy. The ledger records the read route actually used per run (UI vs scripted) so the summary's Result QA section is honest. The policy is conditional: the scripted attempt runs only when the route-around (ticket 16) is in place; otherwise the first move is handing the plot to the user.

**Deferred:** this is the post-analysis correction — parked until the post-analysis phase is worked. Until then, behavior stays as today: everything post-solve goes to the user.

**Blocked by:** 16 — pyAEDT readout route-around (pre-work).

**Status:** ready-for-human

- [ ] Execution text states the one-shot policy (one attempt, one fresh-attach retry, then UI) and drops the archaeology guidance
- [ ] Policy conditional on the route-around: absent it, first move is the UI handoff
- [ ] Ledger records the read route actually used per run (UI vs scripted)
- [ ] Existing behavior unchanged while this ticket is parked
