# Readout experiment — result, 2026-09-01

Run against `TASK-readout-channel-vs-systematic.md`. Licence available, VPN up,
`LICENSE-ANSYS.ENGIN.UMICH.EDU:1055` verified reachable before anything was
launched and still reachable afterwards, so nothing here failed for want of a
seat.

**Headline: the channel-degradation hypothesis is wrong, and so is proposal 2c
as written. The readout does fail, reproducibly, on freshly launched processes
— but the transport is not the cause. pyAEDT tears down its own session
mid-call, and the gRPC error is the symptom.**

---

## What ran, and what did not

**Arm 1 was lost.** The long-lived desktop (pid 25840, port 57850, up since
2026-08-18 18:51:56) died on its own between 2026-08-31 and 2026-09-01. The
task doc predicted exactly this — "the live desktop is a wasting asset… arm 1
is unrepeatable once it does" — and it was right. Session age can not be
fast-forwarded, so the "before" arm can never be reproduced.

That costs the *causal attribution* the two-arm design was built for. It does
not cost the verdict, because the doc's falsification condition was arm 2
alone: "a single successful scripted read… from a freshly launched desktop
process. One success on a fresh process is sufficient." There was no success.

**Arm 2 ran, and is genuine.** The pin moved `57850/25840` -> `64077/29620`,
which is the doc's own test that a relaunch really happened. The instrument
(`read_results.ReadoutSession`) returned its token verbatim:

    route=both-failed

It escalated as designed: read attempt on the live channel, then
`recycle_desktop` released port 55583, reaped pid 16916, launched and pinned a
new desktop at port 64077 (pid 29620), and read again. Both failed.

## What the failure is not

Six or more independently launched AEDT processes were exercised. Across them:

- **Not the channel's age.** Several failed within seconds of construction.
- **Not a missing readout API.** On a live session these all returned real
  values: `hfss.design_name`, `hfss.existing_analysis_sweeps` (which correctly
  listed `Setup1 : Sweep1` and the variation-suffixed table),
  `odesign.GetVariables()` (all 17 variables), `odesign.GetVariableValue()`,
  `variable_manager.independent_variables`, `oproject.GetVariables()`,
  `post.all_report_names`.
- **Not garbage collection.** Reproduced with `gc.disable()`.
- **Not the anonymous `Desktop()` in `ws_common.attach`.** Reproduced while
  holding an explicit `Desktop` reference. (That anonymous construction is
  still worth tidying; it is simply not this bug.)
- **Not attach-vs-launch.** Reproduced with `new_desktop=True` and with
  attach-by-port.
- **Not the licence.** Verified reachable throughout.

## What the failure is

**pyAEDT releases its own session from inside the read.** Instrumenting
`Desktop.release_desktop` with a stack trace caught it:

    get_solution_data
      -> visualization/report/standard.py:57   Report.__init__
      -> visualization/report/common.py:513    nominal_variation(dependent_params=False)
      -> application/analysis.py:3035          {k: v.evaluated_value for k, v in ...}
      -> application/variables.py:2435         numeric_value
      -> release_desktop(close_projects=False, close_on_exit=False)

So building a report evaluates every design variable, and evaluating a variable
releases the desktop. A second teardown fires immediately after `Hfss()`
construction in some configurations — one run logged "Desktop has been released
**and closed**" — which is a different trigger with the same effect.

**Every `GrpcApiError: Failed to execute gRPC AEDT command: X` in this
investigation is a symptom of an already-dead session.** `X` is merely whatever
call came next, which is why the name kept changing across otherwise identical
runs: `GetVariables`, `GetSetups`, `ExportToFile`, `OpenProject`. Reading the
command name as the defect is what sent the 2026-08-18 run to the wrong
conclusion, and it is what would have gone into the playbook.

This also explains the one piece of evidence that never fitted: environment-
compat #6 records `get_solution_data` **working** on this exact pairing on
2026-08-07, across three fresh attaches. The trigger is per-project — it runs
through the design's own variables — so a simpler project clears it and this
17-variable parametric one does not. The task doc's predicted next step ("vary
the project, not the process") was the right instinct, and the trace gets there
without needing the extra run.

## Route-arounds tried, all failed

- `get_solution_data(variations=<built from raw GetVariableValue>)` — got
  further (past the variable evaluation) and then failed
  `KeyError: 'HFSS Terminal Network'`.
- `get_solution_data(variations={})` — session already gone.
- `post.export_report_to_file` — signature mismatch, then session gone.
- `hfss.export_touchstone(...)` — never reached the API; `odesign` was already
  `None`.
- `post.create_report` — hit the documented `HfssConstants.default_solution`
  trap, which environment-compat #6 already notes fires "when the gRPC
  transport is already flaking", i.e. downstream of the teardown.

No working scripted route was found today. **S11 was not read.** The banked
solve is intact and the UI remains the only surface that has ever produced
these numbers on this box.

## What this changes

**Proposal 2c must not be approved as written.** Its claim — "scripted result
readouts systematically fail over this pairing's gRPC; UI is the readout
surface" — is right about the symptom and wrong about the cause, and the cause
is the part a playbook entry teaches. Approving it would tell every future run
that the transport is broken, when the transport is fine and a client-side
teardown is not.

The corrected claim it should become is in `pending-amendments.md`.

**The instrument overclaims and should be fixed.** `ROUTE_BOTH_FAILED`'s
verdict string reads "SYSTEMATIC on this pyAEDT/AEDT pairing". That is exactly
the inference the task doc forbade: "do not report 'systematic' from one fresh
process either", and environment-compat #6 records the same call working on the
same pairing. The token is fine; the sentence attached to it asserts more than
two failures can support and should say so in narrower words.

## Honest limits

- Arm 1 was never reproduced, so the *original* 2026-08-18 failure is
  attributed by inference (same error class, same project, same call path), not
  by measurement.
- The teardown was traced on one path conclusively; the post-construction
  teardown was observed but not traced to its caller.
- One project, one design, one expression. A second project would confirm the
  per-project reading, and is now the cheapest remaining question.
