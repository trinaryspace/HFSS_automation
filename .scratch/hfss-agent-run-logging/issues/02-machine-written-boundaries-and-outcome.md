# 02 — Machine-written boundaries and outcome

**What to build:** Every boundary the run card and the report depend on is
written by a script at the instant it happens. Three are currently missing or
unparseable in the last run, which is why its card reads `unrecorded` and
`unmeasurable`.

- **Solve gate.** `results/state/solve_submitted_at.txt` is empty and nothing
  writes it (campaign runbook defect D2). The solve stage that `compile_spec`
  emits (and the template `08_solve`) writes it, epoch-seconds float, in the
  same call that submits `analyze(blocking=False)`, after the in-flight probe
  and the user's approval. A re-submission appends a second line; the card
  uses the first, the report counts the lines as submissions.
- **Session-1 start.** `run_card.ledger_start_ms` requires the ledger line to
  end at the timestamp; the real ledger has trailing text. Read the start
  from `sessions.jsonl` (ticket 01) first and fall back to a tolerant regex
  on the ledger. The ledger stops being a machine boundary.
- **Outcome.** `results/state/outcome.txt` was written as free text
  (`completed - user verdict: ...`) and parsed as nothing. Add
  `scripts/record_outcome.py --workspace W --outcome completed
  --completions 2 --note "..."` that writes the key=value form, validates the
  outcome word, and refuses anything else. The skill's Session-3 checklist
  names this command; `Outcome._read` gains a loud
  `outcome.txt is not key=value: <first line>` warning instead of silence.
- **Review gate.** `results/state/review_gate.txt` appended by a new
  `scripts/record_gate.py --workspace W --gate 1 --verdict pass|fixes
  --note "..."`, so gate waits and fix rounds are attributable.
- **Calls.** Drop the pretence that `note_call` is called. The budget verdict
  in `scripts/session.py` reads the actual step count from the trace (ticket
  04) when a transcript is available, and says `unaccounted` otherwise.

**Blocked by:** None. Land before the next Tier-2 run.

**Status:** ready-for-agent

- [ ] The compiled solve stage and template `08_solve` write `solve_submitted_at.txt`; tier-0 test on the template with the launch mocked
- [ ] `run_card.py` measures active wall on the real `patch-array-5800` ledger once a gate timestamp exists (fixture captured from that ledger)
- [ ] `record_outcome.py` and `record_gate.py` exist, print one `PASS:` line, and refuse malformed input
- [ ] `Outcome._read` warns on a non key=value file; the last run's file triggers the warning in a test
- [ ] SKILL.md Session 3 "done when" names `record_outcome.py`; execution.md checklist names `record_gate.py`
