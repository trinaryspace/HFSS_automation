# 06 — Proof 1 re-runnability: replay top-to-bottom reproduces the delivered model

**What to build:** the "re-runnable record" property of the staged scripts is proven, not claimed. The final staged scripts from Proof 1 (ticket 05) are replayed in a fresh Workspace — no user interaction — and must reproduce the delivered model: same parameterized geometry, variables, boundaries, excitations, setups, and mesh operations as the conversation delivered, including the read-back-synced state after the review-gate UI tweak. Divergence is a failure of the record: any delta is diagnosed, the owning stage's script is amended so the replay is faithful (or escalated with the evidence if it cannot be made faithful), and the delta feeds the learning loop per the ceremony.

**Blocked by:** 05 (delivered scripts and model are this ticket's input)

**Status:** ready-for-agent

- [ ] Replaying the staged scripts top-to-bottom in a fresh Workspace produces a model whose enumerable state (design variables, boundaries, excitations, setups, mesh operations) matches the delivered model
- [ ] A divergence, if any, is either fixed by amending the owning stage's script and re-replaying to a match, or escalated with the divergence evidence and the script state
- [ ] Any post-tweak sync state (ticket 05) is reproduced by the replay — the sync survived the round trip
- [ ] The replay delta or its absence is recorded in the summary and offered to the learning loop per its triggers (ADR 0002 respected — no playbook auto-append)
