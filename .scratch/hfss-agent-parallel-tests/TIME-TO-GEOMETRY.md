# Time to geometry — making the agent faster, and the bugs in the way

*2026-08-19. Follows `RUN-2x2-POSTMORTEM.md`. Written against a different
objective from the post-mortem's: not tokens, but **wall-clock from the
Clarification gate to usable simulation geometry in front of the maintainer**.*

The post-mortem measured cost. The maintainer's response reframed it:

> *Like it's able to get there eventually. Maybe I'm not as much concerned with
> sheer token cost as the time it takes for it to physically go from prompt (or
> really the clarification gate) to actual usable simulation geometry in front
> of me.*

That is a different metric and it ranks the backlog differently. Tokens and
minutes correlate loosely at best: the 2x2 run spent 2.2 M tokens over 4.4
hours, and the expensive parts were not the same as the slow parts.

---

## 1. Where the 4.4 hours actually went

No per-seam timing exists (ticket 14 would give it), so this is reconstructed
from the run's artifacts and narration. The units are minutes, and they sort
very differently from the token attribution in the post-mortem.

| phase | ~wall | is it EM work? |
|---|---|---|
| Read-first protocol (ADRs, CONTEXT, playbook, execution ref, compiler internals) | 15–30 min | no |
| Clarification + synthesis by hand (Balanis, Hammerstad, feed arithmetic) | 30–45 min | **yes** |
| Schema archaeology — deriving the YZ sheet-size convention | 10–20 min | no, and it was already known |
| First build + compile + AEDT launch | 10–15 min | partly |
| **4 x Review-gate defect repair, each a full edit → recompile → relaunch → look** | **60–90 min** | no |
| Geometry bug hunt (the open T2 junctions) | 20–30 min | **yes** |
| Readout archaeology (3 scripts chasing a gRPC fault) | 30–45 min | no |
| Solves | ~25 min | unavoidable |

**The dominant term is the Review-gate repair loop**, and it is almost entirely
overhead. Each round costs a license check, an AEDT launch, a compile, a window,
and a human's attention — for a defect that a drawing would have shown in a
second. Four rounds, because the defects were found one or two at a time by eye.

Second-largest is **re-derivation of things the repo already knows**. Third is
the readout, which cost the run its primary result.

So the levers, in order of minutes returned:

1. **Fewer Review-gate rounds** — catch relational defects before the desktop.
2. **Cheaper Review-gate rounds** — don't relaunch AEDT to look at geometry.
3. **Don't re-derive** — write down what runs keep paying to rediscover.
4. **Don't hand-synthesise** — a function is faster and cannot fumble arithmetic.

---

## 2. What was built today

Everything in this section is implemented, tested and on
`worktree-flush-face-fix`. It is the first three levers.

### 2.1 `scripts/preview_spec.py` — see the model in ~1 second, no license

```
python scripts/preview_spec.py workspaces/<name>/design.yaml
```

Three orthographic views straight off the bounding boxes `model_checks` already
computes, plus a findings footer. No AEDT, no license, no pyAEDT.

This is the single largest wall-clock lever available, because it attacks both
of the top two terms at once:

- **The agent looks at its own model before anyone else does.** It can read the
  PNG back. A defect found here costs one edit; the same defect found at the
  AEDT gate costs a launch, a compile, a human, and a round trip.
- **Correction rounds stop costing a relaunch.** Edit, re-render, look.

Of the four defects the maintainer caught by eye on 2026-08-18, **three are
visible in this drawing** and the fourth is in its footer. Rendering the shipped
S7 spec prints, in one line each:

```
P1  17.268 x 13.624 mm  cuts=8      <- eight notches
P2  17.268 x 13.624 mm  cuts=0      <- and none on the other three
clearance -y  0.00 mm  wave-port face
```

It never pretends. Ops whose bounds cannot be resolved offline (polylines,
lofts, sweeps) are listed under **not drawn** by name, because a preview that
silently omits geometry would be the exact confident-but-wrong failure this repo
keeps paying for.

`SKILL.md` now names it as the third offline gate, before `compile --dry-run`,
with an instruction to *read the image back*.

### 2.2 Two new relational checks — R1 and R2 from the post-mortem

Both warn rather than block, for the reason `model_checks` already documents: a
heuristic that can block a correct design is worse than one that misses.

**`conductor_connectivity`** — union-find over conductor bounding boxes, per
metal layer. Pointed at the S7 spec as shipped, it prints:

```
5 conductor(s) in the same metal layer are not connected to the rest of it:
ArmL, ArmR, InLine, Xfmr1, Xfmr2R; closest approach 0.58285 mm between
'ArmL' and 'Xfmr2L'
```

That is the exact defect, to five decimal places, from a check that takes
milliseconds and no license. It is the check the post-mortem called "the highest
value single check available", and it catches the class where a model is
**silently disconnected and still validates, still solves, and still reports
numbers**.

Layering matters and cost two iterations to get right: a global pass reports
every microstrip ground plane as an island, which is how a check gets ignored.
Layers are sets of conductors whose extents overlap on the stacking axis — which
also handles finite-thickness metal, where a first attempt keyed on
zero-thickness sheets did not.

**`element_symmetry`** — groups objects by extent and compares their boolean
counts:

```
4 identically sized objects (17.000 x 14.000 x 0.000 mm) carry different
numbers of boolean operations: P1=8, P2=0, P3=0, P4=0
```

That is the missing-notches defect, stated as a number.

Both stay silent on all four canonical cases, and a test asserts that.

### 2.3 The physics gaps that were costing solves

**Dispersion.** `effective_permittivity` was quasi-static — the f → 0 limit —
and `patch_resonance` used the same static value, so **the pre-check confirmed
its own assumption** and reported a perfect zero disagreement on a patch that
would resonate low. Added `microstrip_dispersion` (Kirschning–Jansen 1982),
`patch_resonance_dispersive`, and switched the patch estimator to predict what
the solver will actually find.

The bias has one sign and it is measurable on the stacks this tool has shipped:

| stack | shortfall from missing dispersion |
|---|---|
| RO4350B, er 3.48, h 0.762 mm @ 5.8 GHz (the 2x2 array) | **−1.16 %** |
| FR4, er 4.4, h 1.6 mm @ 5.8 GHz | **−2.83 %** |
| FR4, er 4.4, h 1.6 mm @ 2.4 GHz (`patch-2400`) | −1.27 % |

The 2x2 run measured **−3.4 %**, identically in both designs. So dispersion is
about a third of that error and is the part that is a **code defect** rather
than a modelling choice. It is not the whole story — see BF-9 and §3 — but it
was invisible, systematic, and free to fix.

**Inset synthesis, which did not exist at all.** The string `inset` appeared only
in comments; there was no way to compute an inset depth, which is why the 2x2
spec carried it as "the match tuner, expected to move ±2 mm in the build". Added
`slot_conductance` (14-12), `mutual_conductance` (14-18a, Simpson + a stdlib
Bessel J0), `patch_edge_resistance` (14-17) and `inset_depth` (14-20a inverted).

Validated against Balanis Example 14.1, a published worked example with every
intermediate printed:

| quantity | Balanis | computed |
|---|---|---|
| G1 | 1.57e-3 S | **1.5728e-3 S** |
| G12 | 6.1683e-4 S | **6.1683e-4 S** |
| Rin(0) | 228.3508 Ω | **228.3508 Ω** |
| y0 for 50 Ω | 0.3126 cm | **0.3126 cm** |

Note G1: the familiar `(1/90)(W/λ0)²` is an *asymptote*, and on this patch it is
11 % high, which propagates straight into the inset depth. The integral form is
now the default and the approximation is opt-in.

**`synthesize_rectangular_patch`** — `(f0, er, h) → the patch`, dispersion
included, with a closure check. Every array run so far has re-derived these four
relations by hand in conversation. Hand-arithmetic is also where the shipped
defects came from: the 0.58285 mm open circuit was me offsetting each sheet by
half of *its own* width.

### 2.4 Evidence: run-card defect D1, fixed and verified

`--latest` meant "the newest session", and the command is run by the `runcard`
**subagent**, whose session is by definition newer than the run. Confirmed in
the database — `hidden-falcon` (subagent) → `cosmic-knight` → `neon-eagle` (the
run). `--latest` now restricts to `parent_id IS NULL`, and a recursive CTE rolls
subagent tokens into the run's totals.

| | before | after |
|---|---|---|
| slug | `hidden-falcon` | **`neon-eagle`** |
| billed | 29,419 | **2,220,863** |
| parts | 26 | **1,225** |
| duration | 20 s | **4 h 20 min 32 s** |

The card now matches the post-mortem's hand-derived figures exactly. It also
reports `subagents`, `billed_own_session` and `parts_own_session`, so a run whose
cost sits in its children is visible as such.

### 2.5 A bug found while building the above: YAML 1.1 eats variable names

YAML 1.1 resolves bare `on`, `off`, `yes`, `no`, `y`, `n` to booleans **as
mapping keys**. The loader already mapped them back for the `on:` selector — but
that same mapping **silently renamed design variables**:

```yaml
variables:
  Off: 1mm     ->  off      # every expression using `Off` fails
  On:  4mm     ->  on       # and then
  Yes: 5mm     ->  on       # this one overwrites it, with nothing reported
```

Five declared variables became four and one value was lost, in silence. The
error surfaces as `unknown name 'Off'` pointing at the *geometry*, not at the
declaration. **`N` is the case that matters**: an array spec writing `N: 4` for
its element count is entirely normal, and `n` is false in YAML 1.1.

Fixed: the loader now reads YAML 1.2 core booleans, where only `true`/`false`
are boolean. `on:` still works unquoted as a selector.

### 2.6 A latent false negative in the existing clearance check

`radiation_clearance` excluded *every* object named by an excitation from the
model extent. For a port written `{object: PortSheet}` that is correct. For one
written `{face_of: Substrate}` it excluded **the substrate** — a real body, often
the largest thing inside the boundary. Harmless on `patch-2400` only because the
ground plane shares the substrate's footprint. Now narrowed to dedicated port
sheets via `model_checks.port_sheets`.

---

## 3. Reference material worth adding before the next run

Dropped into `knowledge/reference-papers/`, these are read by `analyze-papers`
before Clarification. Ranked by the specific failures they would have prevented,
not by general merit. The repo currently has Balanis ch. 14, an HFSS intro, a
ports note, and a bow-tie paper.

### Tier 1 — would have changed the 2x2 run's outcome

**1. Balanis, *Antenna Theory*, Chapter 6 — Arrays.**
Array factor, element spacing, grating lobes, and the λ/2 trade-off the
maintainer named as the standing constraint. The repo has ch. 14 and nothing on
arrays, so every array run reasons about spacing from scratch. *Also check
whether the existing `Chapter_14.pdf` includes §14.8 (coupling) and the array
feeding sections — if it stops before them, that is the gap to close first.*

**2. Ramesh, Yip et al., "Design formula for inset-fed microstrip patch
antenna."**
The closed form for inset depth vs input impedance, and — importantly — the
inset notch's own effect on resonant frequency. The tool now has the Balanis
`cos²` relation (§2.3), but the notch's *frequency* pull is not modelled at all,
and it is a live candidate for the ~2 % of the 2x2's −3.4 % that dispersion does
not explain. This is the highest-value single paper on the list.

**3. Pozar, *Microwave Engineering*, ch. 7 §7.2 (T-junction power dividers) and
ch. 5 §5.5–5.7 (quarter-wave and multisection transformers).**
The corporate feed from first principles. Every array run so far has re-derived
this topology in conversation, at ~30–45 min each. This is the reading that
converts it into recall.

**4. Edwards & Steer, *Foundations for Microstrip Circuit Design*, the
discontinuities chapter.**
Mitred bends, T-junction reference planes, step-change-in-width. The 2x2 feed is
full of right-angle bends and T-junctions modelled as ideal. At 5.8 GHz the
uncompensated bend reactance is not negligible, and **nothing in this repo knows
these discontinuities exist** — the impedance walk in `feed_check` treats every
junction as a perfect node.

### Tier 2 — the array methodology the maintainer specified

**5. Pozar, "Input impedance and mutual coupling of rectangular microstrip
antennas," *IEEE TAP* 30(6), 1982.**
The canonical treatment of exactly the two-solve method the maintainer
prescribed: simulate the elements without the feed, extract the active
impedances, match to those. `physics.active_impedance` implements the algebra;
this is the paper that says when it is valid and how far coupling moves the
answer at λ/2.

**6. Pozar, "The active element pattern," *IEEE TAP* 42(8), 1994.**
Short, and it is the argument for why active impedance is the right quantity to
match rather than the isolated one.

**7. Garg, Bhartia, Bahl & Ittipiboon, *Microstrip Antenna Design Handbook*.**
The omnibus. If only one book is added, this is arguably it: feed networks,
insets, arrays, and coupling, all with closed forms in a form that can be turned
directly into estimators.

### Tier 3 — closes named holes in the tooling

**8. Kirschning & Jansen, *Electronics Letters* 18(6), 1982.**
One page; the dispersion model implemented today. Worth having on disk as the
citation for the estimator.

**9. Hammerstad & Jensen, "Accurate models for microstrip computer-aided
design," 1980.**
Carries the **thickness correction** (deferred R13) and, more usefully, the
**stated validity range**. The 2x2 patch has W/h = 22.7, and the repo's own
tolerance file claims ~1 % accuracy "for W/h in 0.1–10". Nothing checks that.

**10. Anything with even/odd-mode coupled-line synthesis** (Pozar ch. 8, or
Matthaei–Young–Jones).
The standing example in hard rule 8. Cell S11 burned 51 minutes and 151,526
tokens writing a field solver because this was missing. It is the one gap where
supplying the reference converts a hard escalation into a buildable recipe.

**A note on how these get used.** Papers are context, not playbook (ADR 0002).
The step that would make them pay is turning #2, #3 and #7 into *registered
estimators* with tolerances — the same route `circular_patch_resonance` took.
A PDF the agent reads is worth minutes; an estimator it calls is worth the
minutes plus the arithmetic errors.

---

## 4. Bugfix register

Status is honest: **fixed** means implemented and tested on this branch.

| # | bug | status |
|---|---|---|
| BF-1 | `feed_check` never asks whether declared conductors touch — a fully disconnected feed validated clean, solved, and reported numbers | **fixed** (`conductor_connectivity`) |
| BF-2 | Nothing compares repeated array elements — 8 notches on one patch of four passed every gate | **fixed** (`element_symmetry`) |
| BF-3 | `run_card --latest` cards the `runcard` subagent, not the run; understated the most expensive run in the project by ~74x (defect D1, open since 2026-08-15) | **fixed + verified against the live DB** |
| BF-4 | Subagent tokens were never rolled into the run's cost, so "billed per completed sim" measured a fraction of the bill | **fixed** (recursive CTE) |
| BF-5 | `effective_permittivity` is quasi-static and `patch_resonance` shares the same blind spot, so the pre-check confirms its own error; every patch lands 1–3 % low | **fixed** (Kirschning–Jansen) |
| BF-6 | No inset-depth synthesis existed at all; the match was tuned by hand or by solve | **fixed** (Balanis 14-12/14-17/14-18a/14-20a, verified against Example 14.1) |
| BF-7 | `slot_conductance`'s closed form is an asymptote, 11 % high on a typical patch, biasing the inset depth | **fixed** (integral form is the default) |
| BF-8 | YAML 1.1 silently renames variables called `On`/`Off`/`Yes`/`No`/`Y`/`N`, and can silently merge two into one, losing a value | **fixed** (YAML 1.2 core booleans) |
| BF-9 | `radiation_clearance` excluded `face_of` port hosts from the model extent — a real body, often the largest one — reporting a clearance the model does not have | **fixed** (`port_sheets`) |
| BF-10 | No offline way to look at geometry; every visual check costs an AEDT launch | **fixed** (`preview_spec.py`) |
| BF-11 | **Fault B is live.** The gRPC readout raise on `GetPropValue`/`GetVariables` is not fixed, and env-compat #6 reads as though the readout problem is solved. It parked the 2x2's primary result | **open** — needs an ADR 0002 amendment, so it needs approval |
| BF-12 | Readout is a single point of failure. `read_results.py` has export fallbacks and they were not enough | **open** — R7: write Touchstone/CSV at solve time so data exists on disk regardless |
| BF-13 | The session call budget is decorative: it binds whoever calls `note_call`, and only `scripts/session.py --note-calls` does. 1,179 parts against a 60-call budget, zero escalations | **open** — needs harness-level tool gating (ticket 14) |
| BF-14 | Nothing checks Hammerstad–Jensen's validity range. The 2x2 patch is at W/h = 22.7 against a stated 0.1–10 | **open** — cheap: warn in `microstrip_impedance` |
| BF-15 | No `corporate-patch-array` estimator, so the 2x2's precheck was `UNCHECKED` on the exact recipe now being iterated | **open** — the element synthesis is just `patch_resonance` on the element dims |
| BF-16 | `design-spec.md` documents the XZ sheet-size swap and is silent on XY and YZ, so the silence reads as "unknown" and gets re-derived at full price | **open** — R10 |
| BF-17 | `feed_check` assumes N identical branches; wrong for amplitude-tapered arrays | **open**, deferred (R14) |
| BF-18 | `microstrip_impedance` is W/h only — no conductor thickness | **open**, deferred at the maintainer's direction (R13) |
| BF-19 | A lumped port written `{object: SomeRealConductor}` removes that conductor from the connectivity graph. Correct for a dedicated port sheet, a blind spot if a spec ports a real body directly | **open**, narrow — documented in `port_sheets` |
| BF-20 | Nothing models microstrip discontinuities (mitred bends, T-junction reference planes). `feed_check` treats every junction as a perfect node | **open** — needs reference #4 above |

---

## 5. What to do next, ordered by minutes returned

**1. Use the preview on the next run and measure the round count.** The claim
is that Review-gate rounds drop from four to one or two. That is a measurable
prediction and the next run should test it.

**2. Ship a worked `patch-array-5800` case** (R11), once the feed is actually
verified. Every array run has re-derived corporate-feed topology from scratch —
30–45 minutes each. A case converts that into reading. This is the largest
remaining one-off reduction for the array class.

**3. Write down what runs keep re-deriving** (R10 / BF-16): the sheet-plane
convention for all three planes, the `unite` same-dimensionality rule, the 2D
sheet Material GUI quirk, wave-port-flush vs lumped-port-clearance, and the
metal-modelling convention (zero-thickness PEC is standard here — 1 oz copper is
~40 skin depths at 5.8 GHz, so thickness buys nothing and costs a ~500:1 mesh
aspect ratio).

**4. Fix the readout properly** (BF-11/BF-12). It is the one failure that has
already cost a run its primary result, and it will do it again. Export at solve
time so the data is on disk before any fetch is attempted.

**5. Then ticket 14's harness-level tool gating** (BF-13). It is the structural
fix for cost and variance, and it is the largest piece of work here — which is
why it comes after the four cheap things above.

---

## 6. The honest caveat

Items 2.1–2.6 are tested offline and none has been through a live AEDT run. The
preview draws axis-aligned bounding boxes, so it is blind to rotation, lofts and
swept bodies — it names them rather than guessing, but a horn or a bow-tie is
substantially "not drawn". The connectivity check declines to report at all when
any conductor cannot be bounded offline, which is the right call and also means
it says nothing useful about `bowtie-3500`.

None of this replaces the visual Review gate (ADR 0003). The claim is narrower
and, I think, defensible: **the gate should be confirming a model the agent has
already looked at, rather than discovering one it has not.**
