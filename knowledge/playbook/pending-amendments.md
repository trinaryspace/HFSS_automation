# Pending playbook amendments - awaiting user approval

**This file is not the playbook.** It is the queue in front of it. ADR 0002
makes the playbook append-only-after-explicit-user-approval, so a proposal
earned by a run has to wait somewhere a human can read it in one pass and say
yes or no. That is this file. Nothing **still listed as pending** here has been
applied to `environment-compat.md`, `precheck-tolerances.json`, `spine-api.md`
or any `knowledge/cases/*` entry, and nothing still pending should be read by
an agent as compat truth. Items that have been decided move to the "Resolved"
table and are removed from the queue; the applied text then lives in the target
file with its provenance, and the target is the thing to read.

Approving an item means: apply it to the target named in its "If approved"
line, then delete the item from this file (the applied text carries its own
provenance in the target). Rejecting it means: delete it and record the
rejection in the run's `summary.md`.

Written 2026-08-31 from the 2026-08-18 hardware run `patch-array-5800`
(`workspaces/patch-array-5800/summary.md`, "Learning-loop notes"; state ledger
`workspaces/patch-array-5800/state.md`). Every piece of evidence below was
observed in that session, on AEDT 2024 R1 (`v241`) with pyAEDT 1.3.0.

## Status at a glance

| # | proposal | target | status |
|---|---|---|---|
| 2c | scripted result readouts are systematically broken over this pairing's gRPC | `environment-compat.md` #6 | **BLOCKED** - the conclusion is probably wrong; see below |
| 2d | normalize setup prop-key spellings in the sync verifier's `canon()` | `hfss_spec` / template `12_verify_sync.py`, plus a compat note | ready to approve |
| 3 | keep `verify_spec_replay.py` as the design-spec route's replay verifier | workspace template, not the playbook | decision needed, not an amendment |

### Resolved 2026-09-01

| # | proposal | outcome |
|---|---|---|
| 1 | register a `patch_resonance` estimator for `corporate-patch-array` | **NOT REGISTERED.** The recipe stays `UNCHECKED`. Of the three shapes offered, the maintainer took the third: n=1 supports a recorded datapoint, not a tolerance, and registering 5% would assert confidence the single hardware check does not support (it consumed ~70% of that budget). The measurement stands as the standing record in `.scratch/hfss-agent-parallel-tests/estimator-calibration.md`; revisit when a second hardware point exists. Cost of the decision: the `no-estimator` verdict the run already lived with. |
| 2a | `unite` is like-to-like only | **APPROVED and applied** as `environment-compat.md` entry 14. |
| 2b | 2D sheets expose no Material property | **APPROVED and applied** as `environment-compat.md` entry 15. |

---

## 2c. Scripted result readouts over this pairing's gRPC - **BLOCKED**

**Claim as the run proposed it.** "Scripted result readouts systematically fail
over this pairing's gRPC (`GetVariables` / `GetPropValue` error classes) - UI
is the readout surface."

**Do not approve this. The conclusion is probably wrong, and the playbook is
append-only.**

**What was actually observed.** Two failures, both recorded, both on the same
long-lived pinned session:

- `results/state/outcome.txt`:
  `readout=unreadable - create_report raised: GrpcApiError: Failed to execute
  gRPC AEDT command: GetVariables`
- `results/state/readouts.txt`:
  `s11: unreadable - get_solution_data raised on 'Setup1 : Sweep1':
  GrpcApiError: Failed to execute gRPC AEDT command: GetPropValue`

Both are the same error class - "Failed to execute gRPC AEDT command" - which
is the transport failing, not the readout API being absent. Compare
environment-compat #6, which distinguishes a genuinely missing API
(`data_real`, `hfss.results`, `HfssConstants.default_solution` - all
`AttributeError`, all reproducible on a fresh process) from a channel that has
gone bad.

**Why the "systematic" reading is not supported by the run's own ledger.**
Earlier in the same run, on the same channel, the identical error class was
observed on `GetVariables` and on `Subtract`, and it was **cured by recycling
the desktop** (state.md, FED REBUILD LOG item 2: "desktop recycled
(`GetVariables` + `Subtract` gRPC failures on the long-lived channel)";
summary.md acute decision 5). The run therefore holds a within-session
counter-example to its own conclusion: that error class on that channel was
transient degradation at least once.

The retry that was supposed to test this did not test it. The skill's policy is
"one scripted attempt plus one retry on a fresh attach", but the attach on this
box pins the port (`results/state/aedt_port.txt` = `57850`,
`aedt_process_id.txt` = `25840`), so the "fresh attach" reattached to the same
degraded process. The hypothesis "the channel is degraded" was never given a
chance to fail.

**Why approving it now is worse than leaving it pending.** The playbook is
append-only by ADR 0002. An approved entry saying the scripted readout is
systematically broken on this pairing would (a) contradict environment-compat
#6, which records `get_solution_data` working on this exact pairing across
three independent fresh attaches on 2026-08-07, (b) retire the readout path
that ticket 16 was built to fix, and (c) make every future run skip straight to
a manual UI read, which removes the only route by which the claim could ever be
falsified. A wrong entry here is self-sealing.

**What unblocks it.** The two-arm experiment in
`.scratch/hfss-agent-parallel-tests/TASK-readout-channel-vs-systematic.md`. The
long-lived desktop from the run (pid 25840, port 57850) was still alive on
2026-08-31 - 13 days - holding the banked project and a licence seat, so both
arms are runnable today and the "before" arm is a genuine reproduction rather
than a re-creation.

- If arm 2 (fresh process, same project, same expression) also fails, the claim
  is supported and can be rewritten with two-process evidence and approved.
- If arm 2 succeeds, the claim is false as written. The correct amendment is
  the opposite one - a readout gets a fresh process, and the retry policy must
  stop reattaching by pinned port - and the UI-is-the-surface conclusion should
  never enter the playbook.

**If approved (after the experiment, and only in the form the result
supports).** `knowledge/playbook/environment-compat.md` entry #6, amended in
the same style as its 2026-08-17 amendment: new text on top, the superseded
reading retained inline for provenance.

---

## 2d. Normalize setup prop-key spellings in the sync verifier's `canon()`

**Claim.** Setup property keys come back with different spellings from
different sessions - `BasisOrder` vs `Basis Order`, `IsEnabled` vs `Enabled` -
so a byte comparison of setup blocks between a live session and a replay
desktop reports a difference where there is none. The sync verifier should
canonicalize the keys (strip spaces, normalize the `Is` prefix) before
comparing.

**Evidence observed in-session.**

- The read-back sync run diffed live against replay: every model section
  matched exactly - objects, bounding boxes, boundaries, ports, variables -
  and only the setups section differed, on key spelling alone (state.md,
  COMPAT NOTE candidate 3; summary.md "Model shape record").
- The variance is a fetch-view artifact, not a model difference: the same
  setup, fetched two ways, names its own properties differently. It was
  recorded and retried once during the run.

**If approved.** Two parts, and they are different kinds of change:

- code: `canon()` in the sync-verify runner (`12_verify_sync.py` in the
  workspace template) normalizes setup prop keys before comparison. This is an
  ordinary code change, not a playbook append, and needs a tier-0 test with a
  real captured pair of spellings as its fixture (`docs/agents/fixture-fidelity.md`
  - do not write the fixture from memory).
- playbook: a short `environment-compat.md` note recording that the spelling
  varies by fetch view, so the next reader does not chase a phantom model diff.

---

## 3. Keep `verify_spec_replay.py` in the workspace

**Claim.** `verify_spec_replay.py` is the design-spec route's ADR-0005 replay
verifier: `12_verify_sync.py` only replays numbered staged scripts, so a run
that built from a `design.yaml` has no replay path without it. It should stay
in the workspace as the route's verifier.

**Evidence observed in-session.** The run's read-back sync was performed by
this script, and the model sections diffed zero against
`results/state/model_snapshot.json` (summary.md, "Model shape record"). It
takes `--spec <name>` to match the `ws_common.DESIGN` constant; its default
compiles both specs into one design, which is a replay-only artifact
(state.md, pitfall 6).

**This is not a playbook amendment.** It is a question about the workspace
template - whether the script is promoted into
`skill/hfss-agent/templates/workspace/src/` so every design-spec run gets it,
or stays a per-run local file. It is listed here only because the run filed it
alongside the other two and it should not get lost. Route it to the template
owner rather than to the playbook.
