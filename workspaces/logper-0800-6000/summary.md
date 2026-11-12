# Summary — logper-0800-6000

Written by the hfss-agent conversation at its end; appended to by read-back
sync deltas and learning-loop notes as they occur.

## What the Model is

- Design: `LogPer_CoaxFeed_NoCase` · Project: `logper-0800-6000.aedt` · Solution type: Modal
- Purpose / prompt: a faithful HFSS replica of the ByTechLab PCB log-periodic
  bow-tie array (0.8–6 GHz), originally simulated in CST. This is **Phase A**:
  CST model "2_WITH_FEED_COAX_FR4_V1", coax feed, no case. **Phase B** (the PLA
  case) is not done and needs its own Clarification.
- Geometry: trapezoidal FR-4 board 205 × 160→20 × 1.5 mm; two copper layers of
  15 bow-ties each (element n = element 0 scaled by 0.85ⁿ, alternating sides);
  a coax lying on one feed line whose centre conductor bends over the tip to
  the other layer; radiation box 93.7 mm clear on every side.

## Acute design decisions

- **Copper as zero-thickness finite-conductivity sheets** (σ 5.96e7 S/m)
  instead of CST's 35 µm solids. The foil is 15–40 skin depths thick over the
  band, which is the regime the boundary is built for; the user asked whether
  this was valid and standard, and kept it as built.
- **Shield trimmed flat at z = h.** CST sinks the shield 0.015 mm into its
  35 µm trace; with sheet copper that overlap would cut into the substrate, so
  the shield rests on the trace through the same 0.35 mm facet.
- **Capped wave port** on the coax dielectric's end face at the board base,
  backed by a 1 mm PEC cap and renormalised to 50 Ω. CST used a 50 Ω discrete
  port at the same place.
- **Dispersive FR-4** from CST's own fit (ε′ 4.81 → 4.65 over 0.8–6 GHz,
  tan δ 0.023–0.025), loaded as datasets from 60 rows of CST's export.
- **Radiation box at λ/4 of 0.8 GHz**, not of the adaptive frequency, because
  the lowest frequency is the one that needs the clearance.
- **Broadband adaptive solve** over 0.8–6 GHz: a log-periodic array is active
  in a different part of the board at each frequency.
- **Route A spec plus three Route-B add-on stages.** `design.yaml` (48
  geometry ops, 0 in-spec escape hatches) builds everything schema v1 can
  express. Three things it cannot: the centre conductor's 1.5 mm bend (no
  circle primitive or swept arc) — `src/20_feed_bend.py`; the FR-4 dispersion
  datasets — `src/21_fr4_dispersion.py`; broadband adaptive, a field sweep and
  the far-field sphere — `src/22_setup_extras.py`. Rebuild order is fixed:
  `compile_spec` → 20 → 21 → 22.
- **Parametric, not traced.** The bow-ties are built from the CST parameter
  set through chained scale variables; the rule reproduces all 128 KiCad
  copper vertices to 0.00 µm.

## Clarification record

- Recipe: `printed-log-periodic-bowtie-array` — new, no playbook entry; the
  as-built CST model is canonical, not the design paper. dims cross-check:
  consistent (CST parameter list = CST STEP export = KiCad copper). Precheck:
  UNCHECKED, no estimator for this recipe.
- Assumptions (all confirmed):
  1. Board copper = finite-conductivity sheets, σ 5.96e7; coax conductors 3D copper.
  2. Shield trimmed flat at z = h, resting on a 0.35 mm facet.
  3. Wave port on the coax end face, 1 mm PEC cap, renormalised to 50 Ω.
  4. FR-4 dispersive per CST's fit; PTFE 1.70 / 0.0002; copper 5.96e7.
  5. Radiation boundary at λ/4 of 0.8 GHz (93.7 mm) on all sides.
  6. Broadband adaptive 0.8–6 GHz, ≤ 12 passes, ΔS 0.02; interpolating sweep
     0.4–6.5 GHz (611 points); field points at 1…6 GHz.
  7. S11 read in the AEDT UI is authoritative; the scripted readout is a bonus.
- Approved Result QA signals: convergence; port; passivity; band edge within
  ±5 % of CST; per-GHz mean S11 within ±3 dB of CST and worst in-band ≤ −5 dB;
  radiation (indicative until Phase B).
- Clarification confirmed, verbatim (2026-11-10): "yep that sounds good, build it".
- Review gate 1 passed, verbatim (2026-11-10): "Ok that sounds good. Go for it".

## Read-back sync deltas

- None. `spec_acceptance` reported differences=0 against the as-built snapshot.
- `src/verify_spec_replay.py`: `PASS: sync replay matches snapshot`. In this
  workspace the verifier was extended to replay the add-on stages 20–22 and to
  carry `data/`, because the live model is the spec plus those stages.

Model shape record: `results/state/model_snapshot.json`, written by
`src/capture_state.py`.

## Results

- Outcome: completed, one solve. The user's verdict on the results has not
  been given yet.
- Solve #1: Normal Completion, banked (71 sweep points). Initial mesh 41 s,
  adaptive 6 passes in 6 min 21 s, sweeps 27 min 56 s.
- Readout route: report-export on the live channel (`get_solution_data` came
  back unfilled, as is usual on this box).

| # | Signal | Result | Verdict |
|---|--------|--------|---------|
| 1 | Convergence | ΔS 0.0154 ≤ 0.02 at pass 6 of 12; 121,574 elements; ΔS by pass 0.413, 0.152, 0.051, 0.039, 0.015 | PASS |
| 2 | Port | P1 excited, one mode. `re(Zo(P1))` reads 50.00 Ω, which is the renormalised value; the raw line impedance (expected 50.3 Ω) was **not read** | not verified |
| 3 | Passivity | max S11 −0.72 dB | PASS |
| 4 | Band edge (first −10 dB) | HFSS 0.808 GHz; CST 0.808 GHz (−0.1 %); measured 0.820 GHz | PASS |
| 5 | In-band S11 | see table below; worst in-band −6.32 dB at 5.80 GHz (CST −6.84, measured −5.21) | PASS |
| 6 | Radiation (indicative) | see table below; 4 GHz directivity is 0.08 dB under the 6–7 dBi range | marginal |

Per-GHz mean S11 (dB):

| Band (GHz) | HFSS | CST | Measured |
|---|---|---|---|
| 1–2 | −12.22 | −12.29 | −13.34 |
| 2–3 | −10.55 | −11.03 | −11.79 |
| 3–4 | −8.88 | −9.69 | −11.22 |
| 4–5 | −8.71 | −8.16 | −10.54 |
| 5–6 | −7.49 | −8.52 | −9.33 |

Radiation, bare board (HFSS) against CST's **with-case** model — indicative
only, since CST exported no far-field data for the no-case model:

| Freq (GHz) | HFSS peak directivity (dBi) | CST with case (dBi) | HFSS rad. efficiency | CST with case |
|---|---|---|---|---|
| 1 | 6.94 | 6.93 | 0.755 | 0.767 |
| 2 | 6.26 | 6.55 | 0.736 | 0.740 |
| 3 | 6.09 | 6.13 | 0.745 | 0.629 |
| 4 | 5.92 | 6.73 | 0.749 | 0.705 |
| 5 | 6.60 | 6.82 | 0.758 | 0.668 |
| 6 | 6.35 | 6.91 | 0.761 | 0.693 |

Deliverables in `results/`: `s11_vs_cst_meas.png`, `s11_comparison.csv`,
`AgentReadout_dB_S_1_1.csv`, `AgentReadout_AntennaParams.csv`,
`convergence.txt`, `model_top.jpg`, `model_bottom.jpg`, `model_isometric.jpg`.

## RO4350B redesign (2026-11-10 to 2026-11-12)

After the FR-4 replica, the user dropped the PLA case and asked for the same
antenna on 20 mil RO4350B, to be fabricated. Targets: 0.8–6 GHz, S11 below
−10 dB, one forward lobe, board short enough for a 300 mm coax pigtail; bands
that matter most: 900 MHz ISM, 1.8/1.9 GHz cell, 2.4 GHz ISM, 5.1–5.9 GHz
Wi-Fi, and other cell bands. The full solve-by-solve record is `state.md`.

**Candidate** — design `LogPer_RO4350B_v3` in the same project, spec
`design_ro4350b_final.yaml` (validated offline; the live design reached these
values by variable edits, and the spec has not been compiled against it):

- 20 mil RO4350B (Dk 3.66, Df 0.0037), 1 oz copper, board 264.1 × 202.7 mm
- 15 bow-ties per layer, element scale 1.356 on the FR-4 dimensions, scaling
  ratio 0.84; largest arm 81.4 mm, smallest 7.1 mm
- feed strips 1.6 mm on both layers, with a 3 × 3.7 mm matching pad at the tip
- coax: Taoglas CAB.01061 (1.37 mm micro-coax, jacket stripped, braid
  1.15 mm) along the top feed strip; centre conductor bent over the tip

**What each change does**

- Element scale: the thin board loads the elements less, so they must be
  larger for the same frequency; the scale also sets where the two largest
  elements' second harmonics (the remaining S11 spikes) fall.
- Scaling ratio 0.84 instead of 0.85: keeps the smallest element at its
  original size while the largest grow, so the upper band edge stays put.
- 1.6 mm feed strips: about 50 Ω on 0.508 mm (4 mm, as on FR-4, is about
  22 Ω and collapses the match).
- Tip pad: about 0.4 pF, cancelling about 1 nH of series inductance in the
  centre conductor's loop over the board tip.
- Thin coax: the shield must be no wider than the feed strip.

**Full-accuracy result** (`results/v3_k1356/`; converged at pass 8, ΔS
0.0186, 249,644 elements; 50 mm radiation box):

| Band (GHz) | Worst S11 (dB) | Mean S11 (dB) |
|---|---|---|
| 0.70–0.89 cell | −11.7 | −17.7 |
| 0.902–0.928 ISM | −14.7 | −14.8 |
| 1.71–1.99 cell | −13.2 | −16.2 |
| 2.11–2.20 cell | −17.0 | −18.0 |
| 2.30–2.40 cell | −13.4 | −13.6 |
| 2.40–2.4835 ISM | −13.8 | −14.8 |
| 2.5–2.69 cell | −15.1 | −18.6 |
| 3.3–3.8 cell | −12.6 | −15.6 |
| 5.15–5.895 Wi-Fi | −14.0 | −16.2 |

First −10 dB crossing 0.685 GHz; −11.6 dB at 6.00 GHz; 99 % of 1–6 GHz at or
below −10 dB. Above −10 dB inside 0.8–6 GHz only at 1.53 GHz (−9.8 dB) and
2.26–2.27 GHz (−9.5 dB). Band edges are the usual US allocations, chosen by
the agent, not given by the user.

| Freq (GHz) | Peak directivity (dBi) | Rad. efficiency | Peak realized gain (dBi) |
|---|---|---|---|
| 1 | 6.30 | 0.816 | 5.27 |
| 2 | 6.92 | 0.806 | 5.83 |
| 3 | 6.73 | 0.788 | 5.51 |
| 4 | 5.64 | 0.767 | 4.40 |
| 5 | 6.47 | 0.760 | 5.12 |
| 6 | 5.95 | 0.736 | 4.31 |

Beam: one main lobe at every frequency; straight off the tip at 1, 2, 3, 5
and 6 GHz; at 4 GHz a broad flat-topped beam whose peak sits 65° out of the
board plane, 0.85 dB above the value toward the tip.

**Tried and not kept**: identical copper on Rogers (match collapses); unequal
feed strips (standing wave); 50 Ω termination at the base (spikes unmoved,
efficiency lost); 19-element denser array (could not be converged on this
machine — untested, not disproven); a 16th tip element (the initial mesher
fails on it).

**Not done**: Review gate on the candidate; replay verification; a check with
a λ/4 radiation box (the mesher failed at every larger box tried); mounting
holes, stiffener and connector are not modelled.

**Fabrication package** (2026-11-12): `fab/` holds a KiCad project and board,
Gerbers, DXF, a bare-board STEP and an A3 mechanical drawing, generated from
`design_ro4350b_final.yaml` by `tools/export_fab.py`; see `fab/README.md`.
The outline adds a Ø0.5 mm half-hole at the tip that the HFSS model does not
have (it notches by the wire radius only).

## Learning-loop notes

Candidates only — none is approved; the playbook changes only with explicit
user approval (ADR 0002).

1. The template `verify_spec_replay.py` replays `design.yaml` only, so a
   Route A workspace with add-on stages gets a false mismatch.
2. pyAEDT 1.3.0 `enable_adaptive_setup_broadband` raises `KeyError` on a
   freshly created setup; seeding `MultipleAdaptiveFreqsSetup` first works.
3. A kept subtract tool's name stays reserved while the old blank exists, so a
   re-run renames it (`InnerCond` → `InnerCond_2`); op order avoids it.
4. `variable_manager[...].numeric_value` raises an AEDT API error over gRPC.
5. The compiler's finite-conductivity boundary called a method pyAEDT 1.3.0
   does not have (fixed on this branch; the main checkout holds the same fix
   uncommitted).
6. There is no precheck estimator for a log-periodic array.

## Run card

### clarify+build+solve — log periodic antenna hfss port

- slug: log periodic antenna hfss port
- host: claude-code
- created: 2026-11-10T16:33:39Z
- updated: 2026-11-10T18:26:15Z
- duration: 1 h 52 min 36 s
- tokens_input: 155
- tokens_output: 119877
- tokens_reasoning: 42640
- tokens_cache_read: 20585908
- tokens_cache_write: 363436
- billed: 120032
- parts: 375
- store_bytes: 7815016
- subagents: 2
- subagent: kb-lookup "pyAEDT signature lookups" billed=14735 parts=74 duration=0 h 1 min 8 s
- subagent: runcard "Draft summary and run card" billed=14241 parts=41 duration=0 h 0 min 55 s

### Run total

- run_id: logper-0800-6000-2026-11-10
- skill_commit: 739fcba
- sessions: 1 (clarify+build+solve)
- unresolved: 0
- subagents: 2
- created: 2026-11-10T16:33:39Z
- updated: 2026-11-10T18:26:15Z
- duration: 1 h 52 min 36 s
- active_wall_start: 2026-11-10T17:21:26Z
- active_wall_start_source: sessions.jsonl
- solve_gate: 2026-11-10T17:43:36Z
- solve_submissions: 1
- active_wall: 0 h 22 min 9 s
- tokens_input: 181
- tokens_output: 148827
- tokens_reasoning: 53964
- tokens_cache_read: 21465674
- tokens_cache_write: 579868
- billed: 149008
- billed_sessions: 120032
- billed_subagents: 28976
- parts: 490
- store_bytes: 9462570
- outcome: completed (Phase A solved and QA'd; user verdict on the results not yet given)
- escape_hatch_scripts: 3
- billed_per_completed_sim: 149,008
