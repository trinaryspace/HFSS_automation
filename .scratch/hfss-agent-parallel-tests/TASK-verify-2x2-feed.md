# Task — synthesise and simulate the 2x2 array, to falsify the feed

Status: ready-to-run
Written 2026-08-17. Hand this to the hfss-agent when the VPN is up.

**The point of this task is to break the feed, not to confirm it.** The corporate
feed in `cells/fixed/S7.design.yaml` was designed by an agent, corrected once by
the maintainer, and has never been simulated. Nobody involved is confident in it.
A run that reports "looks good" without having tried to falsify it has failed.

## Why the feed is suspect

The array's element geometry is well grounded: Balanis 14-6/14-7 recomputed for
5.8 GHz on RO4350B 0.762 mm, closing at 5.8000 GHz, and the same numbers appear in
the single-element S1 spec. **The feed is the unverified part.** Its history:

1. As authored: every line width individually correct, network internally
   self-consistent, and terminating four 100 ohm lines into patches inset-matched
   to 50 ohm — a 2:1 mismatch on every element, past three green gates.
2. Corrected once to all-50-ohm lines with three lambda/4 sections at 35.36 ohm.
3. Then found to be unconventional: the canonical 50-ohm-patch feed uses **six**
   transformers at 70.71 ohm and never leaves 50/100 ohm.
4. And the canonical form **does not fit** at lambda/2 spacing: the element run is
   6.110 mm and a 70.71 ohm lambda/4 is 7.984 mm.

So there are three candidate feeds, all of which close arithmetically. The
simulation decides between them.

## Locked design constraints — do not trade these away

- **Element spacing stays at S = lambda0/2 = 25.844 mm.** Wider invites grating
  lobes; narrower increases mutual coupling. lambda/2 is the standard compromise
  and the array's pattern is the product, so **the feed adapts to the array, not
  the other way round.** Creative feed routing is encouraged; moving the elements
  is not.
- Stack: RO4350B, er 3.48, tand 0.0037, h 0.762 mm, copper 0.035 mm.
- Elements: patch_W 17.2679 mm, patch_L 13.6238 mm. Do not re-synthesise these.
- Single 50 ohm input.
- Airbox lambda0/3 = 17.2295 mm on all six sides.

## The three candidate feeds

Pick one, state why in the ledger, and record the impedance chain in the spec's
`feed_network` block so `validate_spec` checks it. All three satisfy the only
invariant that matters: **the 50 ohm input must see 50 ohms, and a Z1 patch must
be fed Z1.**

**Candidate 1 — as it stands now (3 transformers, 50 ohm patches).**
`patch 50 | 50 ohm line | T: ||2 -> 25 | lam/4 @ 35.36 -> 50 | 50 ohm arm |
T: ||2 -> 25 | lam/4 @ 35.36 -> 50 | 50 ohm trunk`
Fits at lambda/2 because the transformers sit in the arm direction. Unconventional:
it creates 25 ohm nodes, and a 2.908 mm transformer butts a 1.743 mm line, which is
a large width discontinuity with real junction parasitics.

**Candidate 2 — canonical (6 transformers, 50 ohm patches).**
`patch 50 | lam/4 @ 70.71 -> 100 | 100 ohm line | T: ||2 -> 50 | 50 ohm branch |
lam/4 @ 70.71 -> 100 | 100 ohm branch | T: ||2 -> 50 | 50 ohm trunk`
Never leaves 50/100 ohm; 70.71 ohm line is 0.946 mm. **Needs 7.984 mm in the
element run and only 6.110 mm exists**, so it requires creative routing — meander
the element transformer, or bring the element feed in from the outside of the
array rather than through the inter-patch gap. Either is legitimate; say which.

**Candidate 3 — 100 ohm patches (1 transformer).**
`patch 100 | 100 ohm line (matched, no transformer) | T: ||2 -> 50 | 50 ohm arm |
T: ||2 -> 25 | lam/4 @ 35.36 -> 50 | 50 ohm trunk`
Uses the fact that a patch need not present 50 ohm: inset-match the elements to
100 ohm (a shallower inset than for 50) and the element lines need no transformer
at all. Fits at lambda/2 with room to spare. Fewest discontinuities.
**Recommended starting point** — but the inset depth for a 100 ohm match is a
tuned parameter, so expect to move it.

## The methodology — two solves, in this order

**Do not match the feed to the isolated patch impedance.** At lambda/2 the
elements couple, so what a feed actually sees is the *active* impedance - what an
element presents while its neighbours are driven. Matching to the isolated value
leaves a mismatch no amount of correct feed arithmetic removes, because the
arithmetic was solved against the wrong load.

**Stage 1 - characterise the elements, no feed network.**
Build the four patches at S = lambda0/2 with an individual lumped port at each
intended feed point. No corporate feed, no transformers. Solve, and export the
full 4x4 S-matrix.

Then compute the active impedance for uniform broadside excitation:

    gamma_act,i = sum_j S_ij * (a_j / a_i)      with all a_j equal
    Z_act,i     = Z0 * (1 + gamma_act,i) / (1 - gamma_act,i)

`hfss_spec.physics.active_impedance(s_row)` does exactly this - use it rather
than re-deriving.

**A 2x2 is the easy case**: by symmetry every element has one neighbour in x, one
in y and one on the diagonal, so all four active impedances are identical. One
number to match to. (Larger arrays differ by edge/corner/interior and need each.)

Record Z_act in the ledger. It is the real design target and the reason this
stage exists.

**Stage 2 - synthesise the feed to Z_act and solve the fed array.**
Set `element_impedance` to the measured value and
`element_impedance_source: active_measured`; the validator warns while it is
still marked `isolated` or `assumed`, which is the current state of
`cells/fixed/S7.design.yaml`. Then pick a candidate feed, route it, and solve.

Everything stays parameterised so the values can be tuned by hand afterwards -
that is the point of the spec route, and the inset depth in particular should be
expected to move.

## QA signals — with the numbers that decide it

One solve separates the element from the feed, which is the whole reason this is
worth running:

- **Resonance position tests the elements.** The S11 dip should sit at
  5.8 GHz +/-5% (5.51-6.09 GHz). If it lands there, the Balanis synthesis is
  vindicated and any remaining problem is the feed.
- **Dip depth tests the feed**, and the bands are now calibrated against how
  much coupling alone can cost:
  - **S11 < -25 dB**: matched to the active impedance. The stage-1 extraction
    was used and worked.
  - **around -20 dB**: the signature of a feed matched to the *isolated* 50 ohm
    while the elements actually present something else. A perfectly matched
    isolated element under modest lambda/2 coupling reads about 41 ohm active,
    a 17% error and roughly -20 dB. **This is the predicted outcome if stage 1
    is skipped** - "mostly matches", and solved against the wrong load.
  - **around -9 to -10 dB** with the dip in band: a 2:1 element mismatch
    (|gamma| = 1/3). The elements are fine and **the feed is wrong** - this is
    the original defect's exact signature, and finding it is a successful run.
  - **no dip in band**: the elements are wrong, not the feed. Report separately.
- **Broadside gain**: a 2x2 of ~7 dBi patches should reach roughly **12-13 dBi**.
  Materially less, with a good S11, points at unequal element excitation — the
  corporate feed's actual job.
- **Element balance**: the four patches must be excited equally. Check surface
  current or near field for symmetry. A corporate feed that matches at the input
  but feeds the elements unequally still fails, and S11 alone will not show it.
- **Convergence, ports excited, energy pass** as normal.

Sweep 5.0-6.5 GHz so both the in-band behaviour and any out-of-band resonance are
visible. Do not narrow it to flatter the result.

## Sequence

1. Preconditions: VPN up (license server reachable), AEDT 2024 R1 free, **zero
   stray `ansysedt.exe`**. Do not start otherwise.
2. `python scripts/pilot_preflight.py --cell S7SIM`
3. Declare the phase — this turns on the boundary, so a clarify session cannot
   reach the licence:
   `python scripts/session.py --workspace workspaces/<name> --phase clarify`
4. **Clarify**: choose a candidate, state why, write `design.yaml` with its
   `feed_network` block declared, and gate it offline:
   `validate_spec` then `precheck` then `compile_spec --dry-run`.
   The feed walk is an ERROR, so a chain that does not close will not compile.
5. Re-declare `--phase build`, then `compile_spec --launch`, then
   `capture_state.py`. **Review gate: the maintainer inspects the model in the
   UI.** Nothing solves before that.
6. Re-declare `--phase solve`, solve under the detached watchdog, bank with
   `confirm_solve.py`, then read results.
7. Readout: use `read_results.py` from the workspace template — it carries the
   working pyAEDT 1.3.0 accessors and the constants alias. **Do not hand-write a
   fill-state check**; every run that did tested `data_real`, which does not exist
   on 1.3.0, and threw away good data. One scripted attempt plus one retry on a
   fresh attach, then the UI arbitrates.
8. Record the run card by slug (never `--latest`), and write `summary.md`.

## What counts as success

A clear answer either way, with numbers. Specifically:

- the candidate chosen and why, including how it was routed to fit at lambda/2;
- S11 at f0 in dB, and the dip frequency;
- broadside gain;
- whether the four elements are excited equally;
- and an explicit verdict on **which of the three candidate feeds this run
  supports or rules out**.

**A run that reports the feed works without having stated what would have shown
it broken has not tested anything.** If the feed is mismatched, say so plainly —
that is the most valuable outcome available, because it is currently unknown.

## The prompt to paste

> I need a 2x2 array of rectangular microstrip patches at 5.8 GHz on 0.762 mm
> Rogers RO4350B, fed by a corporate microstrip feed network from a single 50 ohm
> input. Element spacing must stay at half a wavelength - I care about the pattern,
> so route the feed creatively rather than moving the elements. The element
> dimensions are already fixed at 17.2679 mm by 13.6238 mm; don't re-synthesise
> them. I am specifically unsure whether the feed network actually matches, so I
> want S11 across 5.0-6.5 GHz, the broadside gain, and a check that all four
> patches are excited equally. Tell me what would show the feed to be broken
> before you build it. There's a candidate design and the reasoning in
> .scratch/hfss-agent-parallel-tests/TASK-verify-2x2-feed.md - read it first.
>
> One thing I want done properly: don't match the feed to the isolated patch
> impedance. Simulate the four patches on their own first, with a port on each and
> no feed network, pull the active impedance out of the S-matrix, and match to
> that. At half-wave spacing they couple and the driven impedance won't be 50.
