# 09 — Paper dimension gate in Clarification

**What to build:** When the Recipe comes from an academic paper, the Clarification block must surface the paper's own consistency before anything builds. The agent numerically cross-checks the paper's equations against its Table and Figure readings for the key dimensions (base/height/feed), prints a verdict in the Clarification block ("dims cross-check: consistent" or "⚠ Table says 46×23, Figure says 52.64×26.32"), and the user arbitrates which reading is canonical. No build starts until those locked with the canonical source recorded in the State ledger. Clarification also records the results-path note (S11 will be read via the UI on this box; a scripted Readout is a bonus, never a blocker) so no run can stall on retrieval discovery later.

This is the front-gate for the Astuti failure class: the paper was internally inconsistent and the discrepancy survived until the user caught it at the results read ~20 h in.

**Blocked by:** None — can start immediately.

**Status:** ready-for-human

- [x] Paper-recipe Clarification includes the consistency verdict line with the actual disagreeing numbers
- [x] Non-consistent paper → user arbitrates (canonical reading locked, or paper rejected); build does not start before arbitration; the ledger records the canonical source (Table / Figure / equations)
- [x] Clarification block includes the results-path note (UI default read route)
- [x] Non-paper recipes see no Clarification behavior change
