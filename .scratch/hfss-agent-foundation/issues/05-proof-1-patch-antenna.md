# 05 — Proof 1: greenfield patch antenna end-to-end

**What to build:** the acceptance seam passes. One greenfield conversation produces a solved inset-fed rectangular patch antenna (~2.4 GHz, FR4, driven modal, radiation boundary) — Recipe #1 derived through the Clarification block of this very conversation per ADR 0002's approval ceremony. Every Spine stage is exercised against the live desktop: clarification → solution type → design → geometry → materials → excitations/boundaries → mesh → setup + sweep → background solve → post-process → reports/plots → Result QA → summary. One deliberate user UI tweak at the review gate demonstrates read-back sync: the owning stage's script is amended so the record matches the approved model (ADR 0003/0005). Result QA reports the approved signals, and the deliverables land: solved project, requested plots, and a summary of the acute design decisions. The learning-loop machinery is exercised at least once by the outcome.

**Blocked by:** 03 (KB must contain the post-processing surface for plot/report stages), 04 (the skill drives the whole conversation)

**Status:** ready-for-agent

- [ ] Result QA signals green and reported: S11 minimum in band at ~2.4 GHz within the agreed tolerance, driven-modal convergence, port excited, energy pass, plausibility vs the recipe
- [ ] Deliverables on disk: the solved project file, the requested plots, and the summary with the acute design decisions
- [ ] All geometry is parameterized with design variables (readable, tweakable, re-solvable)
- [ ] The injected user UI tweak at the review gate is followed by read-back sync amending the owning stage's script, with the delta recorded in the summary
- [ ] Recipe #1 is recorded through the Clarification ceremony with the user's approval of the proposed Result QA signals (no bypass of ADR 0002)
- [ ] The final staged scripts are left in the Workspace in the exact state produced by the conversation (the input for ticket 06)
