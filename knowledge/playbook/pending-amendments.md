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
| 2c | scripted result readouts are systematically broken over this pairing's gRPC | `environment-compat.md` #6 | **BLOCKED** - the conclusion is probably wrong; needs the two-arm experiment, which needs a licence |
| 2d-code | `canon()` normalizes setup prop keys before comparing | template `12_verify_sync.py` | **DEFERRED - needs a licence.** Not a playbook item; blocked on capturing a real pair of setup blocks (`docs/agents/fixture-fidelity.md`). See entry 16 for the caution about blanket normalization. |

### Resolved 2026-09-01

| # | proposal | outcome |
|---|---|---|
| 1 | register a `patch_resonance` estimator for `corporate-patch-array` | **NOT REGISTERED.** The recipe stays `UNCHECKED`. Of the three shapes offered, the maintainer took the third: n=1 supports a recorded datapoint, not a tolerance, and registering 5% would assert confidence the single hardware check does not support (it consumed ~70% of that budget). The measurement stands as the standing record in `.scratch/hfss-agent-parallel-tests/estimator-calibration.md`; revisit when a second hardware point exists. Cost of the decision: the `no-estimator` verdict the run already lived with. |
| 2a | `unite` is like-to-like only | **APPROVED and applied** as `environment-compat.md` entry 14. |
| 2b | 2D sheets expose no Material property | **APPROVED and applied** as `environment-compat.md` entry 15. |
| 2d-note | setup prop-key spellings vary by fetch view | **APPROVED and applied** as `environment-compat.md` entry 16. The proposal's two halves were split: the note lands now, the `canon()` code change is deferred (see the pending table) because its fixture cannot be captured without a live session. |
| 2e | `environment-compat.md` #6 says "fresh attach" and does not define it | **APPROVED and applied** as a precision note at the top of entry 6. It deliberately decides nothing: it records that "fresh attach"/"fresh session" is ambiguous between a new connection and a new process, that the entry is cited in both directions because of it, that `attach()` on this box reconnects by pinned port, and that `SKILL.md` now says process. Raised because the skill and the playbook had come to contradict each other while 2c stayed blocked. |
| 3 | keep `verify_spec_replay.py` as the design-spec route's replay verifier | **PROMOTED into the workspace template.** Not a playbook amendment. The design-spec route is the primary route and `12_verify_sync.py` replays only numbered staged scripts, so a `design.yaml` run had no ADR-0005 replay path without it. Promoted with a defect fix - the default spec list required `design_elements.yaml` and reported `FAIL: sync mismatch` on any workspace lacking it. |

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

## 2d-code. Normalize setup prop-key spellings in the sync verifier's `canon()`

**Split 2026-09-01.** The playbook half of this proposal was approved and is now
`environment-compat.md` entry 16, which carries the evidence below. What remains
here is the **code** half, which is not a playbook item and does not need the
ADR 0002 ceremony — it needs a fixture, and the fixture needs a live session.

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

**What is left to do, and what blocks it.** `canon()` in the sync-verify runner
(`12_verify_sync.py` in the workspace template) should normalize setup prop keys
before comparison. Blocked on the fixture: `docs/agents/fixture-fidelity.md`
requires it be a *captured* pair of real setup blocks, and no such capture is on
disk - the ledger recorded the key *names*, not the blocks. Writing the fixture
from that prose is precisely the move the fixture-fidelity rule exists to
prevent, and it would produce a test that passes against a guess at AEDT's
format rather than against AEDT.

Capture the pair the next time a live session is up. The readout experiment
(2c) needs a desktop anyway, so the two pair naturally in one sitting.

**Implementation caution when it does land.** Prefer an explicit alias map of
observed pairs over a blanket "strip spaces and the `Is` prefix" transform.
Normalization makes the comparison strictly more permissive, and a general rule
can collapse two genuinely distinct keys - weakening the verifier in a direction
nobody would notice. That is the same failure class as the `read_results`
`__main__` bug that reported healthy while doing nothing.

