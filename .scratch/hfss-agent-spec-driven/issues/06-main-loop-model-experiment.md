# 06 — Main-loop model experiment: the cheapest test of the most expensive assumption

**What to build:** Re-run the pilot's problem class with the main loop on a
capable reasoning model, changing nothing else, and record the run card. The
perf refactor's decision 7 pinned `deepseek-v4-flash-0731` at `variant: low` on
the reasoning that the model was not the cost driver. The pilot then spent
1,579,333 tokens — 4× the baseline — and the retrospective's own breakdown
attributes the bulk to capability failures rather than ceremony failures: five
solve submissions where one was correct, eight readout shapes tried in
succession, a guessed `EXPECTED_SD` that could not have been right, and
process-detach churn. Foam-Agent's ablation is the external evidence: identical
harness, 88.2% success on Claude 3.5 Sonnet versus 59.1% on GPT-4o — a larger
swing than their entire retrieval improvement. Ticket 08 of the perf refactor
already built the single swap point, so this is a config change plus one run.
Sequenced deliberately **before** the architecture work: it is the cheapest
experiment with the largest expected effect, and a strong result changes how much
of phases 2–4 is worth building.

**Blocked by:** 01, 02 (banking and stage detection must work or the run is
unmeasurable), 04 (the metric), 05 (a vetted case to run).

**Status:** needs-triage

- [x] Main loop re-tiered in the single config point; subagents left on the cheap tier — **amended 2026-08-14**: no second capable model is available on this account, so the change is `agent.build.variant` `low` → `max` on the same model rather than a provider-alias repoint (see Comments; the hypothesis is weakened accordingly)
- [x] One greenfield run on a vetted canonical case, same ceremony, nothing else changed — `patch-2400`, session `kind-rocket`, 2026-08-15
- [x] Run card records tokens, parts, wall time, outcome, escape-hatch count, and cost per completed simulation against both prior baselines — wall recorded as raw only; the active-wall axis is unmeasurable by construction (defect D2)
- [x] Retrospective note: which of the pilot's five cost centres shrank, and which did not — the ones that did not are the true architecture problems and should be cited in the phase-2 go/no-go
- [x] Explicit go/no-go recommendation on phases 2–4 written into this ticket's Comments — conditional GO, resequenced

## Comments

- 2026-08-14: **Unblocked and ready to run — but it needs you, not me.**
  Tickets 01-05 have landed, so the prerequisites are met: banking works,
  stage detection works, the metric can express the outcome, and there are
  vetted cases to run.
- What this needs that an agent session cannot supply: a live AEDT 2024 R1
  desktop, a valid license with the VPN up, and a full greenfield run of
  the tool itself. Nothing about it can be faked offline, and faking it
  would defeat the point.
- **Suggested protocol.** Repoint the main loop via the existing provider
  alias in `opencode.json` (ticket 08's swap point), leave the subagents on
  the cheap tier, and run `patch-2400` or `microstrip-50r` greenfield —
  NOT the bowtie, whose source paper is the known-inconsistent one. Record
  the card with `python scripts/run_card.py --latest --summary
  workspaces/<name>/summary.md --verdict --outcome <completed|escalated|abandoned>`.
- **What to look at afterwards**, per the ticket body: which of the pilot's
  five cost centres shrank and which did not. The ones that did not are the
  true architecture problems, and they are the evidence for or against
  phase 2. A strong result here legitimately shrinks the bet to tickets 09,
  13 and 15 — all of which are worth doing regardless.

- 2026-08-14: **Armed. The variable is reasoning effort, not the model.**
  `deepseek-v4-flash-0731` is the only capable tier available on this
  account, so the cross-model swap this ticket describes (Foam-Agent's
  88.2%-vs-59.1% ablation) **cannot be run here**. The nearest available
  test is the effort tier on the same model: the pilot ran the main loop at
  `variant: low`; this run raises it to `max` with both subagents left at
  `low`. Recorded as a deliberate weakening of the hypothesis — a null
  result does NOT refute "a more capable model would fix this", but a null
  result IS strong evidence that the five cost centres are architectural,
  which is the phase-2 question.
  - Config: `opencode.json` `agent.build.variant` `low` → `max`, with a
    leading comment carrying the revert value. `kb-lookup` and `runcard`
    untouched on `fireworks-ai/hfss-subagent` @ `low`. Top-level `model`
    unchanged.
- **Case: `patch-2400`** (inset-fed Balanis patch, 2.4 GHz, FR4, Modal,
  radiation boundary, 5% tolerance). Not the bowtie: `bowtie-3500`'s
  `case.json` carries no geometry — only `measured_resonance_ghz: 3.85` and
  a snapshot pointer — and its notes designate it a counter-example
  fixture, "a test, not a build target". **Comparability caveat to carry
  into the retrospective:** both baselines (`silent-engine`,
  `shiny-canyon`) built a bowtie, so part of any delta is case difficulty,
  not effort. The asymmetry is only conclusive in one direction — patch is
  the simpler geometry, so a cost near baseline would be damning.
- **Pre-flight, in order.** (1) `opencode debug config` and confirm the main
  loop actually resolves at `variant: max` — ticket 08 recorded a silent
  failure mode where a misresolved variant showed as empty with no warning
  and startup still "succeeded"; an unverified variant wastes the whole
  run. (2) `python scripts/tier0.py` — green at time of arming:
  `PASS: tier0 suites=8 failed=0 elapsed=13.0s`. (3) AEDT 2024 R1 free,
  VPN up, no stray desktop a teardown could touch.
- **Run rules, locked before launch** (all from the pilot retrospective, so
  the run measures effort rather than re-measuring known bugs): fresh
  greenfield workspace `workspaces/patch-2400-<slug>/`, no Re-entry;
  readout route fixed in Clarification as UI-arbiter with at most ONE
  scripted `get_solution_data` attempt (§C1, ticket 17); no `EXPECTED_SD`
  guess — settle mode plus the profile-status confirm (§B1/B2);
  bank-before-teardown with `close_projects=False` on a solved workspace
  (§B3); resolve-once on any solve anomaly — escalate with evidence rather
  than re-submit (§B4).
- **Recording.** `python scripts/run_card.py --latest --summary
  workspaces/patch-2400-<slug>/summary.md --verdict --outcome
  <completed|escalated|abandoned>`, then a retrospective note scoring each
  of the pilot's five cost centres shrank/unchanged — solve-orchestration
  churn (5 submissions), readout archaeology (8 shapes), sync-verify
  replays (6 × ~8 min), context hygiene, state discipline — and the
  explicit phases 2–4 go/no-go in these Comments.
- **Revert `agent.build.variant` to `low` once the card is recorded**, so
  the config does not silently carry an experimental pin into later work.

- 2026-08-14: **Run-invalidating blocker found and fixed before launch —
  the skill opencode loads was four files and eight edits stale.** opencode
  reads skills from `~/.agents/skills/`, but `scripts/install_skill.py` only
  linked the repo skill into `.claude/skills/` for Claude Code, and nothing
  kept the opencode copy in sync. It was missing `confirm_solve.py`
  (bank-before-teardown), `profile_evidence.py` (ticket 01's single profile
  parser), `real_fixtures.py` and `test_poll_solve_stages.py`, and carried
  stale `SKILL.md`, `reference/execution.md`, `ws_common.py`, `poll_solve.py`,
  `capture_state.py`, template README and `state.md`. Launching against it
  would have run the pre-ticket-01/02 tooling with **both P0 bugs live**
  (`terminal_status()` → `None` → `guard_verdict()` proceeds → teardown
  purges results; `scan_results()` blind to the `.imesh`/`.cmesh`
  directories) and measured the old template rather than the current one.
  - Fixed by extending `install_skill.py` to manage **both** targets as
    links: `claude-code` (`.claude/skills/`, always) and `opencode`
    (`~/.agents/skills/`, only when that root exists, otherwise reported
    `skipped` so a clone elsewhere neither creates it nor fails tier 0).
    `diff -rq` now reports the two trees identical through the junction.
    This is the third time duplicated sources have cost this repo — the
    docstring records all three.
  - Post-fix: `PASS: install_skill targets=2 failed=0`,
    `PASS: tier0 suites=8 failed=0 elapsed=12.3s`.
- **The pilot was not a clean run — comparability warning for the
  retrospective.** `shiny-canyon`'s opening prompt, read back from the
  session DB, launched it through the `/implement` meta-skill carrying the
  ticket text plus "use /tdd", "run the full test suite", "use
  /code-review", "commit your work". A real share of its 1,579,333 was
  ticket execution, test-writing, review and commits — plus the five
  template bugs it found and fixed — not the HFSS build. This run uses a
  plain user-shaped request with **no mention of the ticket, measurement or
  performance**, which is the right experimental hygiene but means part of
  any improvement is prompt shape, not reasoning effort. Say so in the
  retrospective rather than banking it as an effort win.
- 2026-08-15: **RUN COMPLETE — `patch-2400`, outcome `completed`.** One
  opencode session (`kind-rocket`, 01:19–02:00Z) plus two subagent
  sessions; the run did not split into three phase sessions.

  | | billed | parts | wall |
  |---|---|---|---|
  | main loop `kind-rocket` | 269,378 | 412 | 41 min 40 s raw |
  | subagents (`witty-garden`, `quick-cactus`) | 77,615 | 65 | — |
  | **combined** | **346,993** | **477** | |
  | baseline `silent-engine` | 398,130 | 424 | ~1.6 h |
  | pilot `shiny-canyon` | 1,579,333 | 1,392 | 25 h |

  The baseline predates the subagent tier, so **combined is the honest
  comparison**: **−12.8% tokens, +12.5% parts, ~−57% raw wall**. Main-loop
  only it is −32% / −3%. Against the pilot: −78% tokens, −66% parts.
  - **Perf-refactor acceptance axes: FAIL / FAIL** (needed ≥50% tokens,
    ≥40% parts). Wall is informational — see the metric defects below.
  - **Ticket-04 headline metric: best of the three.** Cost per completed
    simulation = 346,993 combined (269,378 main-only), against 398,130 for
    the baseline and `infinite` for the pilot. This is the first run since
    the refactor that delivered a readable result.
  - **Result:** S11 minimum **2.317 GHz at −20 dB**, inside the 2.28–2.52
    band (3.5% low against a 5% tolerance). One solve submission, profile
    `Normal Completion`, 200 sweep points, banked. All four locked QA
    signals PASS.

- **The five cost centres, scored.**
  1. **Solve-orchestration churn — SHRANK, decisively.** Five submissions
     became **one**. No `EXPECTED_SD` guess. The watchdog died mid-sweep
     without a terminal line, and the agent applied resolve-once: collected
     evidence in a single pass, read the profile once through the shared
     parser, escalated to the user, and did **not** re-submit. Bank before
     teardown held — `solved.txt` written before anything closed.
  2. **Readout archaeology — SHRANK.** Eight shapes became **one** failed
     scripted `get_solution_data` (GrpcApiError GetVariables, EC#6 still
     live), then UI arbitration. The one-shot policy held exactly.
  3. **Sync-verify replays — SHRANK.** Six replays became **one**
     (`results/state/verify/20260814_213905/`).
  4. **Context hygiene — SHRANK vs the pilot, FLAT vs baseline.** Cache
     reads 9.0 M against the pilot's 55.5 M; store 1.09 MB against
     1.86 MB. But 412 parts against the baseline's 424 is noise. A run this
     clean should have cost far fewer turns than the baseline's three
     wipe-and-rebuild chains, and it did not.
  5. **State discipline — MIXED.** `solved.txt` exists and the ledger was
     maintained, but `state.md` is 6,940 bytes against its own ≤2 KB cap,
     its `Started:` value is local time mislabelled `Z`, and
     `qa_signals.txt` still reads `unreadable — flaky readout` for three
     signals that `summary.md` reports as PASS — machine state was never
     updated after the UI arbitration.

- **Defects this run exposed** (file separately; none are agent error):
  - **D1 — the run card published the wrong session.** The `runcard`
    subagent ran `run_card.py --latest`, which carded **its own subagent
    session** (`quick-cactus`, 62,381 / 52 parts) and wrote that into
    `summary.md` as the run's card. Any run that delegates the card
    publishes a wrong one. `--latest` needs to resolve to the parent
    session, or the skill must pass `--slug`. Corrected by hand here.
  - **D2 — the active-wall metric is dead on arrival**, two independent
    causes: the template placeholder invites a trailing parenthetical and
    `ledger_start_ms`'s regex requires the timestamp to end the line, so
    the start boundary never parses; and `solve_submitted_at.txt` is
    referenced **only** by `run_card.py` — no skill text, template or
    staged script writes it, so the gate boundary cannot exist. Ticket 11's
    axis has never been measurable on any run.
  - **D3 — the watchdog died at tick 8 with no terminal line**, root cause
    undetermined. Benign only because the banked evidence was independent
    of it. Ticket 14's territory; a heartbeat or journal would diagnose it.
  - **D4 — no S11 plot artifact in `results/`.** The solve session's Done
    condition requires the requested plots on disk; the scripted readout
    failed, so the delivered number is transcribed from the UI. The first
    transcription was wrong (3.317 GHz, outside the swept band) and **the
    user caught it** — the UI gate is load-bearing, not ceremonial.
  - **D5 — two pyAEDT defects consumed the self-correction budget:**
    `lumped_port` rejects a `FacePrimitive` (face id lands in
    `props["Objects"]`; pass the sheet name plus an explicit integration
    line), and `create_rectangle("XZ")` maps sizes to `[z, x]`. Both are in
    the run's learning-loop notes awaiting approval.

- **GO / NO-GO on phases 2–4: conditional GO, resequenced.**
  The decisive number is not the delta against the baseline — it is the
  delta against the spec's own target. A run with **zero flailing** (one
  solve, one readout attempt, one verify replay, no wipe-and-rebuild) still
  cost **346,993 tokens and 477 parts** against the spec's acceptance
  threshold of **≤80,000 and ≤60**. That is 4.3× and 8× away. Ceremony
  optimisation is now exhausted: there is no remaining flailing to remove,
  so the gap cannot be closed by tuning the containment machinery. What
  remains is the irreducible cost of authoring ten stage scripts and
  discovering API shapes — and this run's two hardest moments (D5) were
  **both** API-discovery failures, which is precisely the cost a typed
  surface and a compiler delete. That is evidence for phase 2's premise.
  - **Do first, they stand alone:** ticket 13 (typed spine surface — aims
    straight at D5), 09 (physics pre-check), 15 (token discipline).
  - **Then phase 2 proper**, in the Q7 order (07 → 12a → 08 → 10 → 11) so
    the schema is shaped by a real snapshot rather than guesswork.
  - **Caveats that must travel with this verdict.** N=1. Three variables
    moved at once — reasoning effort, prompt shape (the pilot ran through
    `/implement` with ticket, TDD, review and commit work folded in), and
    the case (both baselines built a bowtie; `patch-2400` is simpler and
    landed a −20 dB match on the first solve, which is lucky, not typical).
    **The effort change itself is confirmed** — the user verified
    `variant: max` in `opencode debug config` before launching. Note for
    future cards: the DB still reported `tokens_reasoning: 0` for the main
    loop, so on this model that column is a provider reporting gap, **not**
    a signal that reasoning was off. Do not read it as evidence either way.

- **Card mechanics.** `load_card` is `LIMIT 1` — one session, no
  aggregation — and subagent sessions are separate rows excluded from the
  parent's totals. Both baselines are single top-level sessions
  (`silent-engine` still reads exactly 398,130 / 424). The skill runs as
  three phase sessions, so **record all three slugs** and sum them, with
  subagent tokens reported separately: the experiment raises only the main
  loop to `max`, so a card that silently omits subagent cost would flatter
  it. Snapshot the card the moment the run ends — `shiny-canyon` has since
  drifted to 2,382,800 / 1,652 in the DB because the session kept being
  used after the retrospective froze it at 1,579,333 / 1,392.
