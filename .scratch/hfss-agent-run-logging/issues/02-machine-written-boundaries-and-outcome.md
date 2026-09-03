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

**Status:** ready-for-human

- [x] The compiled solve stage and template `08_solve` write `solve_submitted_at.txt`; tier-0 test on the template with the launch mocked
- [x] `run_card.py` measures active wall on the real `patch-array-5800` ledger once a gate timestamp exists (fixture captured from that ledger)
- [x] `record_outcome.py` and `record_gate.py` exist, print one `PASS:` line, and refuse malformed input
- [x] `Outcome._read` warns on a non key=value file; the last run's file triggers the warning in a test
- [x] SKILL.md Session 3 "done when" names `record_outcome.py`; execution.md checklist names `record_gate.py`

## Comments

### 2026-09-02 — landed

One correction to the ticket's premise first: **there is no compiled solve
stage.** `scripts/compile_spec.py` says in its first line that it never
solves, `hfss_spec/compiler.py` has no `analyze(` anywhere, and the template
`src/` shipped no `08_solve.py` — every workspace carried its own copy
(patch-array-5800's docstring: "the template does not ship it"), and none of
those copies wrote the gate. So the compiler was not touched; the template
now ships the launcher and it is the single submission path for both Build
routes. Also: the real workspace's `solve_submitted_at.txt` does not exist at
all (the spec says "empty"); `outcome.txt` is free text **with a UTF-8 BOM**.

What landed, by file:

- `skill/hfss-agent/templates/workspace/src/08_solve.py` (new): the real
  patch-array-5800 launcher's shape, behavior kept, with `submit()` doing
  `analyze(setup, blocking=False)` and, in that same call, appending the
  epoch-seconds float to `results/state/solve_submitted_at.txt` via the new
  `ws_common.append_state`. Nothing is appended when `analyze` returns
  `False`. The in-flight probe is now a refusal (`FAIL: solve not submitted
  ...`, exit 2, no attach, no gate) instead of a warning that submitted
  anyway; the user's go is `--approved`. `12_verify_sync` never replays it
  (`SOLVE_LIKE` filter, asserted against the real tree).
  `test_template_runners.TestSolveGate` (8 tests): `attach` faked and never
  launches, `analyze` records its call, `Popen` faked, ws_common `STATE` /
  `PROJECT` redirected; one line on submission, two on re-submission with
  the first unchanged, none on refusal or a failed submission.
- `scripts/run_card.py`: `Wall` reads the start from the earliest `clarify`
  line of `sessions.jsonl` first (`history_start_ms`), then the ledger;
  `ledger_start_ms` matches the ISO token only, so the real `- Started:
  2026-08-18T09:27:37Z (\`session.json\`); task: ...` line parses;
  `epoch_ms_lines` parses the append-only gate (first line = gate, count =
  submissions; a garbage line is skipped, never guessed). Two card lines
  added: `active_wall_start_source` and `solve_submissions`.
  `Outcome._read` reads `utf-8-sig`, and a file whose first line is not
  `<key>=` prints `warning: outcome.txt is not key=value: <first line>` to
  stderr and carries it on the card (`outcome: unrecorded (outcome.txt is
  not key=value: completed - user verdict: ...)`).
- Fixtures: `scripts/fixtures/patch-array-5800/` — `state.session1.md` (the
  real ledger up to `## Session 2`) and `outcome.txt` (byte-for-byte, BOM
  included), captured by `capture.py` there, which refuses a slice that
  does not re-read identical and records size + sha256 in `index.json`;
  byte-stable on rerun; main checkout untouched.
  `test_run_card.TestPatchArrayRecord` (11 tests): the real `Started` line
  parses; active wall measures `3 h 0 min 0 s` once a gate exists; the
  real outcome file triggers the warning; history beats ledger; a history
  with no clarify falls back to the ledger.
- `scripts/record_outcome.py`, `scripts/record_gate.py` (new) with
  `scripts/test_record.py` (17 tests, registered in tier0 as
  `record-state`). Outcome: key=value (`outcome`, `completions`, optional
  `escape_hatch_scripts`, `note`, plus `recorded_at`), refuses any other
  outcome word, negative / non-integer counts, `completed` with 0
  completions, multi-line notes, a missing workspace — exit 1, one `FAIL:`
  line, nothing written. Gate: appends `ts=<epoch> gate=<n>
  verdict=pass|fixes note=<text>`; `read_gates()` parses it back.
- `hfss_spec/session.py`: `trace_calls(state_dir)` counts `"kind":
  "tool_use"` lines across `results/state/trace/*.steps.jsonl` (None when
  no trace file exists; `run_trace` is not imported);
  `budget_verdict(trace_calls=...)` says `calls unaccounted (no trace)`
  when there is neither a trace nor a hand count; `exceeds(calls)`.
  `scripts/session.py` reports `calls unaccounted (no trace); budget 60`
  or `N/60 (trace)` and exits 2 on a traced breach.
  `test_session.TestTraceBudget` (4 tests).
- `SKILL.md`: Session 3 names `record_outcome.py` in its text and its
  "done when"; Session 2 names `record_gate.py`. `execution.md`: checklist
  10 (Review gate) names `record_gate.py`; 14 (Summary) names
  `record_outcome.py`; the `08_solve.py` list carries the gate write, the
  refusal, and the real `Popen(DETACHED_PROCESS)` launch (it still said
  `Start-Process`).

Not done / for a human: `verify_skill.py` was not edited (outside this
ticket's file list), so `08_solve.py` is not yet in `TEMPLATE_SRC_FILES`
and the two new doc markers are not enforced; the template `README.md`
still describes `08_solve.py` without saying it is shipped. The existing
`TestRunFromHistory` test had to pin its declaration clock to the fixture
start, because the clarify declaration now *is* the start boundary.

Verification, verbatim:

- `PASS: tier0 suites=17 failed=0 elapsed=22.2s`
- `python skill/hfss-agent/verify_skill.py` → `ALL PASS`
- `python scripts/test_run_card.py` → `Ran 73 tests in 2.734s` / `OK`
- `python scripts/test_record.py` → `PASS: record tests=17 failed=0`
- `python hfss_spec/test_session.py` → `PASS: session tests=27 failed=0`
- `python scripts/fixtures/patch-array-5800/capture.py <main checkout ws>` →
  `PASS: capture patch-array-5800 fixtures state.session1.md=4231 outcome.txt=155`
- CLI smoke: `PASS: record_outcome outcome=completed completions=2 file=...`;
  `FAIL: record_outcome outcome must be one of completed, escalated, abandoned; got 'completed - user verdict: x'` (exit 1);
  `PASS: record_gate gate=1 verdict=fixes recorded=1 file=...`;
  `PASS: ok: session phase=clarify calls unaccounted (no trace) budget=60`, then
  `PASS: ok: session phase=clarify calls=2/60 (trace)` with a trace file present.
