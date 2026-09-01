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
| 2c | ~~scripted readouts are systematically broken over this pairing's gRPC~~ **-> pyAEDT tears down its own session mid-read** | `environment-compat.md` #6 | **UNBLOCKED, REWRITTEN, ready to approve.** Experiment run 2026-09-01: the readout does fail on fresh processes, but the transport is not the cause and the original wording teaches the wrong lesson. |
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


## 2c. A ctypes callback fault, amplified by `release_on_exception` (FINAL, 2026-09-01)

**Round 2, same day — supersedes the round-1 text below.** The three follow-up
tests were run. The claim to record is now:

> On this box, pyAEDT 1.3.0's gRPC plugin raises inside the ctypes callback
> `AEDT.GetAedtObjId` (`internal/grpc_plugin_dll_class.py:454`,
> `SystemError: <built-in function isinstance> returned a result with an
> exception set`). Object resolution then fails, the report layer reports
> `Solution Data failed to load` / `No Data Available` and returns **`False`**.
> Separately, `settings.release_on_exception` defaults **on**, so pyAEDT
> releases **every** desktop session on any wrapped exception - turning one
> fault into total session death and a misleading
> `GrpcApiError: ... <whatever was called next>`. The transport is not the
> fault, and the varying command name is an artefact of the teardown.
>
> **Mitigation, verified: `settings.release_on_exception = False`.** The session
> then survives a failed read - measured across three consecutive failures. It
> does not make the readout work. No Python-level route-around does; the fault
> is below pyAEDT's Python layer. The realistic fix is a pyAEDT version change
> (ADR 0004 pins 1.3.0) or an upstream report.

Refuted by measurement in round 2, and none of these should be recorded: the
per-project reading (a 10-variable project fails identically to the
17-variable one), the version-branch reading (forcing the other branch changes
nothing), `Design.__exit__`, and `Desktop.__del__` (which fires only at
interpreter exit). Full method: `readout-experiment-result-2026-09-01.md`.

This also reopens something #6 closed. `Solution Data failed to load` is
verbatim the 2026-08-02 symptom; the 2026-08-17 amendment concluded the
flakiness was "mostly our own reader", which was true of the reader and left
this underneath it.

---

### Round-1 text, retained for provenance

## 2c. pyAEDT tears down its own session mid-read (REWRITTEN 2026-09-01)

**The original claim is withdrawn.** It read: "scripted result readouts
systematically fail over this pairing's gRPC (`GetVariables` / `GetPropValue`
error classes) - UI is the readout surface." The experiment
(`TASK-readout-channel-vs-systematic.md`) ran on 2026-09-01. Full result and
method: `.scratch/hfss-agent-parallel-tests/readout-experiment-result-2026-09-01.md`.

That wording is right about the symptom and wrong about the cause, and the
cause is the part a playbook entry teaches.

**Claim, as it should be recorded.** On AEDT 2024 R1 / pyAEDT 1.3.0, a scripted
readout of this project fails reproducibly on freshly launched desktop
processes - but the gRPC transport is not the fault. **pyAEDT releases its own
session from inside the read.** Building a report evaluates every design
variable, and evaluating a variable calls `release_desktop`:

    get_solution_data
      -> visualization/report/standard.py:57   Report.__init__
      -> visualization/report/common.py:513    nominal_variation(dependent_params=False)
      -> application/analysis.py:3035          {k: v.evaluated_value for k, v in ...}
      -> application/variables.py:2435         numeric_value
      -> release_desktop(close_projects=False, close_on_exit=False)

Every `GrpcApiError: Failed to execute gRPC AEDT command: X` observed here is a
**symptom of an already-dead session**; `X` is whatever call came next, which is
why the name varies across otherwise identical runs (`GetVariables`,
`GetSetups`, `ExportToFile`, `OpenProject`). Reading `X` as the defect is what
produced the original claim.

**Evidence.** Arm 2 returned `route=both-failed`, with the pin moving
`57850/25840` -> `64077/29620` proving a genuine relaunch. Six or more
independently launched processes failed. On a live session, `design_name`,
`existing_analysis_sweeps`, `odesign.GetVariables()` (all 17 variables),
`GetVariableValue`, `variable_manager.independent_variables` and
`post.all_report_names` all returned real values - so the API is present and the
channel carries calls. Ruled out by direct test: session age (every process was
seconds old), garbage collection (`gc.disable()`), the anonymous `Desktop()` in
`ws_common.attach` (reproduced holding an explicit reference), attach-vs-launch,
and the licence (reachable throughout). Arm 1 could not be run - the 13-day
desktop died on its own first, exactly as the task doc warned.

**Why this matters more than the original.** It reconciles the one piece of
evidence that never fitted: environment-compat #6 records `get_solution_data`
**working** on this same pairing on 2026-08-07 across three fresh attaches. The
trigger runs through the design's own variables, so it is per-project - a simple
project clears it, this 17-variable parametric one does not. "Systematic over
this pairing" cannot be true while #6 stands; "pyAEDT tears down the session
when it evaluates this project's variables" is consistent with both.

**If approved.** `knowledge/playbook/environment-compat.md` entry #6, amended in
its established style - new text on top, superseded reading retained inline. The
amendment must say the transport is not the fault, must carry the stack path so
the next reader can recognise it, and must state that the UI remains the
practical readout surface on this box **for this reason** rather than because
the scripted surface is absent. It should not say "systematic over this
pairing".

**Known limits, to travel with the entry.** Arm 1 was never reproduced, so the
original 2026-08-18 failure is attributed by inference, not measurement. The
post-construction teardown (one run logged "released **and closed**") was
observed but not traced to its caller. One project, one design, one expression:
a second project is the cheapest remaining question, and would settle the
per-project reading.

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

Capture the pair the next time a live session is up. (The 2026-09-01 readout
experiment had a desktop up and would have been the natural moment; it went
into diagnosing the teardown instead and the capture was not taken. It is a
few minutes' work whenever a session next exists.)

**Implementation caution when it does land.** Prefer an explicit alias map of
observed pairs over a blanket "strip spaces and the `Is` prefix" transform.
Normalization makes the comparison strictly more permissive, and a general rule
can collapse two genuinely distinct keys - weakening the verifier in a direction
nobody would notice. That is the same failure class as the `read_results`
`__main__` bug that reported healthy while doing nothing.

