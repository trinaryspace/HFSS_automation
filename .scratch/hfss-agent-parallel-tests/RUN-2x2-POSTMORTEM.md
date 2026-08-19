# Post-mortem — the 2x2 array run, 2026-08-18

Session `neon-eagle` + subagents. **~2,220,000 billed, ~1,225 parts, 4.4 hours,
three solves.** Measured against the vision in `PLAN.md` — *"a complete HFSS
project out of a single conversation"* — and the spec's phase-2 acceptance of
**<=80,000 billed and <=60 parts**.

This is the most expensive run in the project's history. It cost **more than
`shiny-canyon`** (1,579,333 / 1,392), the run the whole spec-driven effort was
written to prevent. It also produced more real engineering than any previous run.
Both things are true and the tension between them is the finding.

| run | billed | parts | wall | outcome |
|---|---|---|---|---|
| `silent-engine` baseline | 398,130 | 424 | 1.6 h | completed |
| `kind-rocket` (best) | 346,993 | 477 | 0.7 h | completed |
| `shiny-canyon` (the disaster) | 1,579,333 | 1,392 | 25 h | abandoned |
| **this run** | **~2,220,000** | **~1,225** | **4.4 h** | completed, primary question unanswered |
| acceptance target | <=80,000 | <=60 | — | — |

**27x the token target. 20x the parts target.**

## What the run was for, and whether it answered

The task was to **falsify the feed**: does the corrected corporate network
actually match the elements at lambda/2 coupling? The method was two solves —
extract the active element impedance from a 4-port elements-only model, then
synthesise the feed to that measured value.

**It did not answer.** Stage 1's readout failed (gRPC), the extraction was parked,
and the feed was built against an *assumed* 50 ohm. So the -7 dB result cannot be
attributed: it is consistent with an untuned inset, with the unmeasured active
impedance, or with a feed defect. The falsification test came back inconclusive.

That distinction matters and the summary blurs it. "Not outright failure, a tuning
issue" is right about the **resonance**; it is not established about the **feed**,
because the measurement that would establish it never happened.

## Results, read honestly

| signal | result | what it means |
|---|---|---|
| resonance | **5.6 GHz in BOTH designs** | -3.4%. Identical in elements-only and fed array, so the error is **element-level, not the feed**. The two-solve method earned its keep here even though stage 1's readout failed. |
| dip depth | **~-7 dB** | \|gamma\| 0.45, VSWR ~2.6 — *worse* than the -9.5 dB 2:1 signature the brief named as the defect shape |
| convergence / ports / energy | PASS | 10 and 14 adaptive passes, Normal Completion, banked |
| gain, element balance | not read | UI reads pending |
| **feed verdict** | **inconclusive** | stage 1 parked |

The resonance finding is genuinely valuable: because both designs shifted
identically, the element synthesis is implicated and the feed is exonerated *for
that error*. That is exactly the diagnostic the two-solve design was for.

## The defect the run found in my work

**Both stage-2 transformers were disconnected from their arms by 0.58285 mm.**
Verified independently:

```
ArmL   spans x = -6.1379 .. -0.8713
Xfmr2L spans x = -14.3763 .. -6.7207
gap = 0.58285 mm  =  (xfmr_W - feed50_W)/2   ->  OPEN CIRCUIT
```

I wrote those origins, offsetting each sheet by half of **its own** width, so the
2.9 mm transformer and the 1.7 mm arm centred on different lines. Both T2
junctions were open air. The agent found it at build time and fixed it.

**And every gate I built passed it.** `feed_check` walks impedances and never asks
whether the objects touch. A completely disconnected feed validates clean. That is
the single most important gap this run exposed.

## Scoring the four Review-gate defects

The maintainer caught four defects by eye on a model that had passed
`validate_spec`, `precheck`, `compile --dry-run`, snapshot verification and
`validate_simple=True`:

| defect | any gate catch it? |
|---|---|
| notches missing on 3 of 4 patches | no — nothing checks repeated elements are identical |
| ports in yz, should be xz | no — nothing relates port plane to feed direction |
| rectangles not assigned pec | no — a sheet with no material is legal |
| airbox flush with lumped ports | **should have — my bug**, now fixed on `worktree-flush-face-fix` |

Four for four missed by machine, four for four caught by eye. The Review gate
(ADR 0003) is carrying the correctness of this tool almost single-handedly.

## Where the 2.2 M went

No token-by-seam breakdown exists (ticket 14 would give one), but the run's own
narration and the artifacts locate it:

1. **Read-first protocol** — ADRs, CONTEXT, playbook, execution reference,
   compiler internals. Wave A measured this at 109-301 parts *before any output*;
   this run is consistent with the high end.
2. **Schema archaeology** — it spent calls deriving the YZ sheet size convention
   because `design-spec.md` documents the XZ swap and says nothing about XY or YZ.
   The answer was already in `bowtie-3500`, hardware-verified. Undocumented
   knowledge is re-derived at full price, every run.
3. **Four Review-gate defect repairs**, each a diagnose-fix-rebuild cycle.
4. **A geometry bug hunt** (the open T2 junctions) — valuable, and expensive.
5. **Readout archaeology, again.** Scripted readout failed systematically; the
   run wrote `extract_active_z.py`, `extract_active_z_export.py` and
   `11_plots_s11.py` chasing it.
6. **A degraded gRPC channel** mid-session, recovered by recycling the desktop.

Only item 4 is irreducible engineering. Items 1, 2 and 5 are the tool paying
repeatedly for knowledge it already has.

## Three claims of mine this run refutes

**1. "The readout flakiness was mostly our own reader."** Landed in env-compat #6
under ADR 0002. Fault A (`data_real`) was real and is fixed. **Fault B — the
genuine gRPC raise — is alive**, hit `GetPropValue` and `GetVariables`
systematically over this pairing, and is what parked stage 1 and cost the run its
primary result. The amendment overstated the case and should be corrected.

**2. The session budget works.** It is decorative. 60-call budget, **1,179 parts**,
zero escalations. It binds whoever calls `note_call`, and nothing did.

**3. The run card is trustworthy.** `summary.md` reports **29,419 billed / 26
parts / 20 seconds** — that is `hidden-falcon`, the `runcard` subagent carding
*itself*. The delivered summary understates the run by roughly **74x**. This is
ticket-06 defect D1, documented 2026-08-15, never fixed, and it has now silently
mis-stated the most expensive run in the project's history.

## What went right, and should be protected

- **The phase boundary worked on its first live run.** It declared itself
  unprompted (`phase: clarify`, `patch-array-5800-clarify`). The SKILL.md
  instruction landed.
- **The two-solve methodology paid off** even with stage 1 crippled: identical
  resonance in both designs localised the error to the elements.
- **Idempotent recovery held.** A degraded gRPC channel was survived by recycling
  the desktop with `close_projects=False`; nothing was lost.
- **Sync-verify replayed to a zero-diff model.**
- **Real environment discoveries**: `unite` silently no-ops on mixed box/sheet
  sets; 2D sheets expose no Material property in the 2024 R1 GUI while the model
  DB carries `MaterialValue='"pec"'`.
- **It extended `feed_check`** to read in-plane width on 3D strips, 20 tests.
- **It refused to fake the parked extraction** and said so.

---

# Recommendations

Ordered by expected value against the vision — *a complete, correct HFSS project
out of one conversation, at <=80,000 tokens and <=60 parts*. Each says which of
the three gaps it closes: **correctness** (the tool ships wrong models),
**cost** (27x/20x over target), or **evidence** (we cannot tell what happened).

## Tier 1 — the tool currently ships wrong models

**R1. Connectivity check in `feed_check`.** *(correctness)*
Objects in a declared chain must physically touch. My open-circuit transformers
passed every gate. This is the highest-value single check available: it catches a
class where the model is *silently disconnected* and still validates, solves and
reports numbers. Bounding-box adjacency within a tolerance is enough; no topology
engine needed.

**R2. Element-repetition symmetry check.** *(correctness)*
In an array, the N elements must have identical op patterns. "Notches missing on
3 of 4 patches" is exactly this check firing. Derivable from the geometry: group
ops by their role and compare counts and dimensions across elements.

**R3. Port-plane vs feed-direction check.** *(correctness)*
A port sheet must be perpendicular to the line it terminates. Derivable from the
integration line and the adjoining conductor. Catches the yz/xz defect, which is
the most dangerous of the four because a wrongly-oriented port still validates,
still solves, and reports an impedance that is not the antenna's.

**R4. Widen the relational-gate family and say so.** *(correctness)*
R1-R3 plus the two that exist are all instances of one thing: **properties of the
model as a whole**. Every defect found by human review in this campaign has been
relational, and every one passed field-wise validation. This is where checking
effort belongs, and the module should say that in one place so it is not
rediscovered.

## Tier 2 — we cannot tell what happened

**R5. Fix run-card defect D1.** *(evidence)*
The `runcard` subagent must card the **parent** session, never `--latest`. Two
options: pass `--slug` explicitly, or make `--latest` resolve to the top-level
session. Until this is fixed **every delivered summary is capable of understating
its own run by two orders of magnitude**, which makes the headline metric — cost
per completed simulation — unmeasurable in exactly the runs that matter most.

**R6. Correct the env-compat readout entry.** *(evidence)*
Fault B is not fixed. The entry currently reads as though the readout problem is
solved. It should record: Fault A fixed and tested; **Fault B live**, reproduced
2026-08-18 on `GetPropValue`/`GetVariables`, and it will park a run's primary
result. ADR 0002 amendment, needs approval.

**R7. Make the readout not a single point of failure.** *(correctness + evidence)*
The scripted readout has now blocked a real result. `read_results.py` already has
export fallbacks; they were not enough. Add: export-to-file as the **primary**
path rather than the fallback, and a `touchstone`/CSV export written at solve time
so the data exists on disk regardless of whether any later fetch works.

**R8. Per-seam token accounting.** *(cost)*
Nothing tells us where 2.2 M went. Ticket 14's run-card breakdown is the fix, and
without it every cost recommendation is inference from narration.

## Tier 3 — the cost gap is structural

**R9. Finish ticket 14's boundary with harness-level tool gating.** *(cost)*
The phase boundary works, and the budget does not, because one is enforced by
code and the other asks an agent to notice. 1,179 parts against a 60-call budget
with zero escalations is the whole argument. Per-phase tool restriction is what
makes it real.

**R10. Document what the run had to derive.** *(cost)*
`design-spec.md` documents the XZ sheet swap and is silent on XY and YZ, so the
silence reads as "unknown" and gets re-derived at full price. Add: the sheet-plane
convention for all three planes; the `unite` same-dimensionality rule; the 2D
sheet Material GUI quirk; the wave-port-flush vs lumped-port-clearance rule; and
the metal-modelling convention (zero-thickness PEC sheets are standard at these
frequencies — 1 oz copper is ~40 skin depths at 5.8 GHz, so thickness buys nothing
and costs a ~500:1 mesh aspect ratio). Each of these cost real tokens this run.

**R11. Ship a worked array case.** *(cost)*
Every array run so far has re-derived corporate-feed topology from scratch. A
canonical `patch-array-5800` case with its `feed_network` block, once it is
verified, converts that from reasoning into reading. This is the single largest
one-off cost reduction available for the array class.

**R12. Register the `corporate-patch-array` estimator.** *(correctness)*
The run's precheck was UNCHECKED. The element synthesis is just `patch_resonance`
on the element dims — the run verified it offline by hand. Cheap, and it closes a
no-estimator hole on the exact recipe we are now iterating on.

## Tier 4 — deferred, with reasons

**R13. Hammerstad thickness correction.** Deferred at the maintainer's direction.
`microstrip_impedance` is W/h only, so specifying 1 oz copper would change nothing
in the synthesised widths while changing the model. At t/h 4.6% the bias is ~1-2%
in one direction across every line. Revisit if a match comes in mysteriously low.

**R14. Junction symmetry / unequal splits.** `feed_check` assumes N identical
branches. Correct for symmetric corporate feeds, wrong for amplitude-tapered
arrays. Add when tapering is on the roadmap.

**R15. Tolerance tightening.** Line-vs-load is 5%; arithmetic over a declared
intent could justify 2%.

## The one-line version

The tool's **containment machinery works** — phase boundaries, idempotent
recovery, banking, sync-verify all held under a degraded channel. Its
**correctness checking does not**: every defect this campaign found was
relational, and every one passed the gates. And its **cost is diverging**, not
converging: 2.2 M against an 80 k target, with the accounting broken in a way
that hides it.

R1-R3 and R5 are days of work and address the two gaps that matter most.
