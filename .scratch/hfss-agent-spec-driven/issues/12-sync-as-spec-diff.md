# 12 — Read-back sync becomes a spec diff; retire the replay ceremony

**What to build:** Replace the two-desktop replay with a diff. Today, after a
user's UI tweak, `capture_state.py` snapshots the live model and
`12_verify_sync.py` copies the workspace, replays eight staged scripts on a
port-pinned second desktop, and diffs — 36 steps in the baseline run and six
replays at roughly eight minutes each in the pilot. The whole ceremony exists
because the generated scripts and the live model can silently diverge, and the
only way to know is to run them again. When the spec is the source of truth,
that question is answered by comparing two documents. Build `snapshot_to_spec`,
reducing `model_snapshot.json` to spec shape, and diff it against `design.yaml`:
differences are the user's UI tweaks, and applying them back into the spec *is*
the read-back sync. ADR 0005's guarantee — re-running top to bottom reproduces
the delivered model — holds more strongly than before, because the spec is what
gets re-run.

Retire `12_verify_sync.py` and the port-pinned second desktop only after the
diff path is proven equivalent on the pilot workspace; until then run both and
compare verdicts. Keep `capture_state.py`, which remains the snapshot source and
the solve-session handoff. Note that the pilot's five template bugs were found
*by* the replay ceremony — that value is preserved by the Tier 0/1 harness
(ticket 04), which finds the same class of bug without eight minutes of AEDT per
attempt.

**Blocked by:** 12a (the reducer this depends on lands there), 07, 10, 11.

**Status:** ready-for-agent

- [ ] Uses ticket 12a's `snapshot_to_spec`; the diff ignores fields 12a marks approximate (`op: unknown`) rather than reporting them as user tweaks
- [ ] Spec diff reproduces the pilot's recorded sync verdicts on the pilot workspace
- [ ] Both paths run in parallel for one full case and agree before the old one is retired
- [ ] ADR 0005 amended to describe sync as a spec diff, with the replay recorded as superseded and why
- [ ] Ledger and `summary.md` still record the delta, in the same house format
