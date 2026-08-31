# Task - is the gRPC readout failure the channel, or the pairing?

Status: ready-to-run
Written 2026-08-31. Hand this to a maintainer (or the hfss-agent) when the VPN
is up. It needs a licence seat and about an hour.

**The point of this task is to break the claim "the scripted readout is
systematically broken on this pairing", not to confirm it.** That claim is
pending as learning-loop proposal 2c
(`knowledge/playbook/pending-amendments.md`) and it is queued for a playbook
that ADR 0002 makes append-only. If it goes in wrong, it stays wrong, and it
removes the only route by which it could later be found wrong. A run that
reports "yes, still broken" without having tried the one condition that would
have shown otherwise has tested nothing.

## Why the claim is suspect

The 2026-08-18 run `patch-array-5800` recorded two readout failures and
concluded from them that the scripted surface is systematically dead over this
pyAEDT 1.3.0 / AEDT 2024 R1 pairing, and that the AEDT UI is the readout
surface on this box. Four things are wrong with that inference.

1. **Both failures are the transport error class, not a missing API.**

   - `results/state/outcome.txt`: `readout=unreadable - create_report raised:
     GrpcApiError: Failed to execute gRPC AEDT command: GetVariables`
   - `results/state/readouts.txt`: `s11: unreadable - get_solution_data raised
     on 'Setup1 : Sweep1': GrpcApiError: Failed to execute gRPC AEDT command:
     GetPropValue`

   "Failed to execute gRPC AEDT command" is the channel failing to carry a
   call. It is not the shape of a missing attribute. Environment-compat #6
   already draws exactly this line: `data_real`, `hfss.results` and
   `HfssConstants.default_solution` are absent, raise `AttributeError`, and
   reproduce on any fresh process. Nothing in that entry says `GetVariables`
   is absent - and the entry records `get_solution_data` **working** on this
   exact pairing across three independent fresh attaches on 2026-08-07.

2. **The same run cured the same error class by recycling the desktop.**
   Earlier in the same session, `GetVariables` and `Subtract` were both failing
   on the long-lived channel. The fix was to kill the desktop and relaunch
   (`state.md`, FED REBUILD LOG item 2; `summary.md` acute decision 5). So the
   run holds a within-session counter-example to its own conclusion: that error
   class, on that channel, was transient at least once.

3. **The retry never tested the hypothesis.** The skill's policy is one
   scripted attempt plus one retry "on a fresh attach". On this box the attach
   pins the port - `results/state/aedt_port.txt` = `57850`,
   `aedt_process_id.txt` = `25840` - so the retry reconnected to the *same*
   degraded process. A fresh socket to a bad server is not a fresh server. The
   competing explanation was never given a chance to fail.

4. **The failing session was very long-lived.** The desktop that produced both
   failures started 2026-08-18 18:51:56 and was still running on 2026-08-31
   when this task was written - **13 days**, verified by `Get-Process -Id
   25840`. If channel degradation over session lifetime is real, this is the
   most degraded channel the repo has ever measured, and it is the only one the
   claim rests on.

## What would falsify the claim

**A single successful scripted read of any solved signal from the banked
project, from a freshly launched desktop process.** One success on a fresh
process is sufficient: "systematic on this pairing" is a universal claim and
one counter-example ends it. Nothing about the sample size matters in that
direction.

The reverse does not hold symmetrically, and the task must not pretend it does.
A failure on the fresh process supports the claim but does not prove it - it
narrows the cause to something shared by both processes (the project, the
solution data, the expression, the pairing) rather than the channel's age.
Say which, if it happens; do not report "systematic" from one fresh process
either.

## The instrument

Do not hand-write this. `skill/hfss-agent/templates/workspace/src/read_results.py`
was changed on 2026-08-31 (the readout fresh-process fix, by another worker;
its tests pass) so that the retry is a fresh **process** rather than a fresh
attach on the pinned port, and so that the outcome is labelled with which route
produced it: `ROUTE_FRESH` (live channel failed, fresh process read it -
channel degradation confirmed), `ROUTE_BOTH_FAILED` (failed live and on a fresh
process), `ROUTE_UNTESTED` (failed live and no fresh process ever ran - which
is what the 2026-08-18 run actually produced, though it did not have the word
for it).

That change is the reason this experiment is now cheap. Use it as the
instrument rather than reimplementing the two arms by hand, and report the
route label it returns verbatim.

## Preconditions - honest ones

- **VPN up, licence server reachable.** `1055@LICENSE-ANSYS.ENGIN.UMICH.EDU`
  is reachable only on the UM VPN (environment-compat, standing prerequisites).
  Without it, arm 2's relaunch will stall at design-open and the result is
  uninterpretable - it will look like a fresh-process failure and it is not.
  Check the licence *before* killing anything.
- **The live desktop is a wasting asset.** pid 25840 / port 57850 holds the
  banked project and a licence seat, and has done for 13 days. It can die on
  its own at any moment. Arm 1 is unrepeatable once it does.
- **Take the outstanding UI reads FIRST.** Two QA signals from the run are
  still pending and were never taken: **broadside gain** (expected 12-13 dBi)
  and **element balance** (near-field symmetry across the four patches). The
  live session already has the solved project open, so it is the cheapest place
  in the world to get them, and arm 2 destroys it. Take them before touching
  anything else. If arm 2 goes badly - licence gone, project will not reopen -
  those two reads are the only part of this task that is not recoverable.
- **Zero other `ansysedt.exe`.** As of 2026-08-31 pid 25840 is the only one.
  If a second appears, stop: the port pinning makes it ambiguous which process
  answered.
- Record `aedt_port.txt` and `aedt_process_id.txt` before and after arm 2. The
  pin changing is how you know arm 2 really relaunched.

## The two arms

Both arms read **the identical expression from the identical banked project**.
If the expression differs between arms, the experiment is void - that is the
one way to accidentally answer a different question.

Use `dB(S(1,1))` on the `PatchArray` design, solve #2, sweep 5.0-6.5 GHz
(`results/state/solved.txt`: Normal Completion, 150 sweep points). Read the
sweep name back from `existing_analysis_sweeps`; it carries a random suffix and
must never be hardcoded (environment-compat #6).

### Arm 1 - the long-lived pinned desktop

Attach to pid 25840 on port 57850 and attempt the read. **Expect failure**;
the point is to reproduce 2026-08-18 rather than to discover anything. If arm 1
*succeeds*, that is itself a finding and a large one - it means the failure was
transient even within the pinned process, and proposal 2c is dead on the spot
with no need for arm 2.

Record the exact exception text, not a paraphrase. The error class is the whole
evidentiary content of this arm.

### Arm 2 - a genuinely fresh process

Kill 25840 (kill-until-gone, per environment-compat #10 - `release_desktop`
alone does not reliably reap it). Confirm no `ansysedt.exe` remains. Relaunch,
reopen the banked project from disk (`remove_lock=True` - the killed session
leaves a `.lock`, environment-compat #9), and attempt **the same read**.

## What each outcome means, and what it changes

| arm 1 | arm 2 | verdict | what changes |
|---|---|---|---|
| fails | **succeeds** | **channel degradation.** The claim is false as written. | Proposal 2c is rewritten to the opposite conclusion before any approval: a readout gets a fresh process, and the retry policy must stop reattaching by pinned port. The UI-is-the-readout-surface sentence never enters the playbook. Environment-compat #6's existing "the readout can genuinely raise on a partially functional channel" stands and gains a cause. |
| fails | fails | **not the channel's age.** Narrowed, not proven. | Proposal 2c may be approved only in the narrowed form: two processes, one project, one expression, both failed - cause shared by both, unattributed. It must not say "systematic over this pairing" while environment-compat #6 records the same call working on the same pairing on 2026-08-07. Next step is to vary the project, not the process. |
| **succeeds** | n/a | the 2026-08-18 failure was transient inside the pinned process. | Proposal 2c is withdrawn. Arm 2 is unnecessary; do not kill the desktop, and take any other outstanding reads while it is up. |

In all three rows, record the route label `read_results.py` returns alongside
the human verdict, so the next reader can tell an untested claim from a tested
one.

## Sequence

1. Preconditions: VPN up, licence reachable, exactly one `ansysedt.exe`
   (expected: pid 25840). Do not start otherwise.
2. Confirm the desktop is still the one from the run:
   `Get-Process -Id 25840` and check `StartTime` is 2026-08-18 18:51:56.
   If the pid is gone, arm 1 is unrecoverable - say so and run arm 2 alone as a
   weaker single-arm test.
3. **Take the two outstanding UI reads** - broadside gain and element balance -
   from the live session, and write them into
   `workspaces/patch-array-5800/summary.md` Results. This is run business left
   over from 2026-08-18, not part of the experiment, and it must happen first.
4. Arm 1: attach on the pinned port, one read, record the verbatim exception
   and the route label.
5. Arm 2: kill-until-gone, relaunch, reopen with `remove_lock=True`, same read,
   record the same two things plus the new port and pid.
6. Write the outcome into this file's sibling findings, update proposal 2c in
   `knowledge/playbook/pending-amendments.md` to whichever form the result
   supports, and note the machine-state change (desktop killed) in
   `campaign-log.md`.

## What counts as success

Not "the readout worked". A clear answer either way, with the evidence
attached:

- the exact expression and sweep name read, identical across both arms;
- the verbatim exception text from each failing arm, with its error class named;
- the route label `read_results.py` returned;
- the before/after pid and port, proving arm 2 was a different process;
- an explicit verdict on which row of the table above the run landed in;
- and the rewritten (or withdrawn) text for proposal 2c.

**A run that kills the desktop without first taking the broadside-gain and
element-balance reads has destroyed more than it measured**, whatever the
readout does afterwards.

## The prompt to paste

> The 2026-08-18 patch-array-5800 run concluded that scripted result readouts
> are systematically broken over this pyAEDT/AEDT pairing and that the UI is the
> only readout surface. I think that conclusion is wrong - both recorded
> failures are the gRPC transport error class, and the same run cured that same
> error class earlier by recycling the desktop. The retry that was supposed to
> test it reattached to the same process by pinned port, so it never tested
> anything.
>
> The desktop from that run (pid 25840, port 57850) is somehow still alive and
> holding the banked project. Run the two-arm experiment in
> .scratch/hfss-agent-parallel-tests/TASK-readout-channel-vs-systematic.md -
> read it first, it says what would falsify the claim and in which order to do
> things. Before you kill anything, get me the broadside gain and the element
> balance off the live session in the UI; those reads are still outstanding from
> the run and they die with that process.
>
> Tell me which row of the outcome table we landed in, and rewrite the pending
> proposal to match. Do not approve it into the playbook either way - that is
> mine to approve.
