# 17 — Re-pilot acceptance on the canonical set

**What to build:** The acceptance run for the whole feature. One greenfield
build through the spec-driven path on a vetted canonical case, measured against
both prior baselines under the ticket-04 metric, plus a full Tier 1 pass over the
canonical set. Thresholds: **≤80,000 billed tokens and ≤60 parts** for a clean
greenfield run (against `silent-engine`'s 398,130 / 424), **zero escape-hatch
stage scripts** on the canonical set, and a delivered `.aedt` that validates with
the expected in-band resonance. Stretch: ≤50,000 tokens.

Two lessons from the `shiny-canyon` pilot are binding here. First, the case must
come from a **self-consistent source** — the previous pilot's paper was
internally inconsistent and the resulting entanglement made the run
uninterpretable; ticket 09's closed-form check now runs before the build as
insurance. Second, the **readout path is locked in Clarification** (UI read is
authoritative, scripted readout is a bonus, never a blocker) so no run can stall
on retrieval again — the failure that consumed roughly eight attempts and
ultimately ended the pilot.

Record the calibration findings the same way the pilot did, and write an honest
go/no-go: if the thresholds miss, the retrospective must say which layer was
responsible rather than which model was used.

**Blocked by:** 04, 05, 09, 10, 11, 12, 13, 14, 15 — and a maintainer-vetted
self-consistent source for the case.

**Status:** needs-triage

- [ ] Tier 1 pass over the full canonical set before the acceptance run starts
- [ ] One greenfield run on a vetted case, user in the loop only at Clarification and the Review gate
- [ ] Run card records tokens, parts, wall time, outcome, escape-hatch count, cost per completed simulation, and per-seam token breakdown
- [ ] Thresholds met, or a retrospective naming the responsible layer
- [ ] Delivered `.aedt` validates and shows the expected in-band resonance
- [ ] Go/no-go on ticket 16 and on any v2 schema expansion recorded in Comments
