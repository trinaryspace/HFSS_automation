# 03 — SKILL.md + execution.md rewrite

**What to build:** the skill-text layer of the refactor (no code): 

- **Phase sessions (ADR 0007):** SKILL.md's "The run" restructured as three named sessions — Clarification (writes the State ledger), Build through the Review gate incl. read-back sync (amends ledger), Solve+QA (reads ledger; submits via watchdog; QA + summary + run card). Each session starts from `workspaces/<name>/state.md`, not the prior conversation.
- **State ledger:** `state.md` convention — stage progress, locked parameters/variables, pitfalls, snapshot pointer; machine state stays in `results/state/*.txt`.
- **Verification contract:** every staged script ends in one `PASS: <stage> <assertions>` line; static `py_compile` + import gate before any AEDT launch; self-correction reads the PASS line, caps stay at 3 failed runs per stage.
- **Bash discipline:** explicit `timeout` argument on anything that can exceed ~90 s; no full recursive listings (count/size summaries, `tail`, state files); final agent messages ≤ ~250 words (verbosity cap).
- **Solve (ADR 0006):** 08_solve = cleanup + in-flight-solve probe (results-dir age, solver processes; ask user before submitting if live) + submit + detach watchdog; agent reads `solve_progress.txt` only; never foreground-polls, never estimates.
- **Sync verify:** replace the interactive ceremony with `capture_state.py` → `model_snapshot.json`, `12_verify_sync.py` replay+diff on a port-pinned second desktop, one PASS/FAIL line; teardown must be port-pinned (user's desktop untouchable).
- **Idempotency (ADR 0008):** delete-then-create per object becomes the build doctrine; execution.md's EC#8 route-around rewritten (wipe = escalation only).
- **KB rules:** `spine-api.md` is the first-class reference for the spine call set; `.rst.md` files are stubs — never read/grep; use `rg -l` for discovery.
- Keep every contract element that `verify_skill.py` checks (markers move with ticket 04).

**Status:** ready-for-agent
**Blocked by:** 02 (config semantics exist to reference: subagents, variant note)

- [ ] SKILL.md restructured into the three phase sessions with ledger handoff
- [ ] execution.md carries verification contract, bash discipline, watchdog flow, verify-runner flow, idempotency, KB rules
- [ ] All pre-existing contract markers still present (ticket 04 re-runs verify_skill.py)
- [ ] Wording cross-references ADRs 0006–0008 and the glossary terms

## Comments

- 2026-08-04: All content decisions locked in the grilling session (questions 3–11).
- 2026-08-05: Implemented (commit e9dfdb1, working tree only touches `skill/hfss-agent/SKILL.md` + `reference/execution.md`). Verification: `verify_skill.py` ALL PASS before (37 lines) and after (same, markers untouched); temp seam test mirroring 04's planned markers 15/15 green; full suite green (`scripts/test_run_card.py` 10/10, `scraping/verify_kb.py` all pass, verify_skill all pass). Code-review (standards+spec axes) passed with fixes applied: dropped the falsifiable "ripgrep installed machine-wide" claim (verified absent on this box; `rg -l` instruction kept per ticket), EC#8 cited only for validation facts with idempotency attributed to ADR 0008, sync runner's PASS/FAIL line no longer called a Verification line (staged-script term only), "handoff" wording removed, `validated.txt` dropped from machine-state list.
- 2026-08-05: Pending on 04 (by design, reference-only): `poll_solve.py`, `capture_state.py`, `12_verify_sync.py`, static-gate script, `state.md` skeleton, `## Run card` in summary template, `ws_common.py` port-pinned helpers — all cited in the text but landed by ticket 04. Ticket 07 should re-check citations resolve after 04 lands.
- 2026-08-05: Ticket 04 landed (f6cfc7f). Re-verified: verify_skill.py now 58/58 ALL PASS against the landed text (04's new markers: verification line, state ledger, run card, watchdog, sync verify, static gate, idempotency, KB rules, ADR 0006–0008, template src files) with zero wording changes needed; full suite green (test_run_card 10/10, test_template_runners 24/24). Spot-checked all citations against the landed scripts: `model_snapshot.json` path, exact `PASS: sync replay matches snapshot` / `FAIL: sync mismatch - <differing keys>` lines, `solve_progress.txt` / `solve_watchdog_pid.txt` / `aedt_port.txt` / `aedt_process_id.txt`, ≤ ~2 KB ledger skeleton — all resolve. Only change: execution.md now cites the static gate by its landed name `00_static_gate.py` (commit ebdc52c). Pending-on-04 list is now resolved.

**Status:** ready-for-human
