# Summary — bowtie-3500

Written by the hfss-agent conversation at its end; appended to by read-back
sync deltas and learning-loop notes as they occur.

## What the Model is

- Design: Bowtie3500 · Project: `workspaces/bowtie-3500/bowtie_3500.aedt` ·
  Solution type: Modal (explicit, EC#11)
- Purpose / prompt: build the reference bow-tie microstrip patch antenna
  from Astuti et al. 2022 (JCM 17:12) — the baseline version WITHOUT the
  cross-dumbbell DGS (user decision), dimensions per paper Table I,
  resonating ~3.5 GHz (paper baseline: 3.46–3.55 GHz, 2.66% FBW); standard
  driven-antenna simulation with a single waveport; stop before solving for
  user review.

## Acute design decisions

- Baseline bow-tie only: user chose the NO-DGS antenna over the paper's
  cross-dumbbell variant (which gives 10.44% FBW and three resonances
  3.5/3.66/3.77). Clean ground plane.
- Layout (user-confirmed): substrate 90 (X) x 80 (Y) x 1.6 mm; waist at the
  substrate center (0,0); the two triangle petals flare in +/−Y (bases
  along X at y = ±L); feed stub runs along +X from the waist to the +X edge
  (x = +45, Lz = 45 = half the PCB width, per paper text); waveport plane
  flush at x = +SubW/2.
- Every dimension is a design variable (PatchW, PatchL, SubW, SubL, SubH,
  CuT, FeedW, FeedL, AirGap, PortW, PortH) — ADR 0005 convention.
- Ports.pdf-derived port shape: 3*FeedW x 3*FeedW sheet in the YZ plane on
  the airbox +X face (external boundary, single-mode microstrip
  cross-section, 50 Ω renormalized) — the sheet-port shape that validated
  and solved in the earlier bowtie-3670 session.

## Clarification record

- Recipe: derived, "bowtie-5g" (baseline, no playbook entry yet): Modal,
  single waveport, λ/4 airbox + radiation boundary, adaptive Setup1 @
  3.5 GHz + discrete sweep.
- Assumptions (stated in the Clarification block): FR-4 εr 4.3, tanδ 0.02
  (paper states εr only; tanδ is the standard FR-4 value); copper t = 0.1
  (Table I); 50 Ω line width Wz = 3.1118 modelled via a rectangular line;
  airbox gap 25 mm (≥ λ/4 @ 3.5 GHz = 21.4 mm); port 3*FeedW square;
  aluminum-free "standard" driven-antenna bookkeeping (radiation boundary,
  not PML).
- User answers (verbatim): Q1 DGS → "Baseline bow-tie only"; Q2 layout →
  "Feed along +X, petals flare ±Y".
- Approved Result QA signals (baseline-adjusted):
  1. convergence — ΔS ≤ 0.02 reached
  2. port excited — P1WavePort present, S11 data populated
  3. in-band resonance — S11 min ≤ −10 dB within 3.4–3.6 GHz
  4. bandwidth — VSWR ≤ 2 span ≥ 2.6% of center (paper baseline 3.46–3.55)
  5. plausibility — |S11| magnitudes sane for a single-port passive device

## Read-back sync deltas

<none yet>

## Results

<not solved yet — awaiting Review gate>

## Learning-loop notes

<none yet>
