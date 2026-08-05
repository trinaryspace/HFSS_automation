# Summary — <workspace name>

Written by the hfss-agent conversation at its end; appended to by read-back
sync deltas and learning-loop notes as they occur.

## What the Model is

- Design: <name> · Project: <path> · Solution type: <type>
- Purpose / prompt: <recap of what the user asked for>

## Acute design decisions

<What was decided and why — the interesting choices, not a build log.>

## Clarification record

- Recipe: <recipe name> (playbook-backed path)
- Assumptions: <every assumption stated in the Clarification block>
- Approved Result QA signals: <convergence, ports, energy, in-band resonance, plausibility>

## Read-back sync deltas

<Each user UI tweak: what changed, which stage's script was amended.>
Model shape record: `results/state/model_snapshot.json` — the machine-precise
snapshot of objects/bboxes/materials/boundaries/excitations/setups/variables,
written by `src/capture_state.py` and verified by replaying the amended
scripts (`src/12_verify_sync.py`, one PASS/FAIL line).

## Results

<QA signal values read from the solve, or "unreadable — flaky readout"
with what was (not) observed; user verdict if given.>

## Learning-loop notes

<Any generalizing tweak, QA anomaly, or backend-compat discovery —
proposed amendments only after user approval (ADR 0002).>

## Run card

Filled by the measurement harness (`scripts/run_card.py --summary summary.md`):
slug, created/updated, duration, `tokens_input`/`tokens_output`/
`tokens_reasoning`/`tokens_cache_read`/`tokens_cache_write`, billed, parts,
store_bytes — one `- key: value` line per metric.
