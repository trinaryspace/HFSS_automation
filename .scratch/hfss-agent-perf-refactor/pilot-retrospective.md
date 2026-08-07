# Pilot retrospective — ticket 06 (acceptance gate) breakdown & corrective plan

Written 2026-08-06, immediately after the user terminated the test at the
corrected-geometry QA read. Applies to the `shiny-canyon` pilot session.

## Verdict

**NO-GO on all three acceptance axes.** The user terminated the pilot at the
results-readout step (which never worked), after a paper-consistency
discovery: Astuti et al. 2022's bow-tie dimensions are internally
inconsistent (the authors' equations do not reproduce their Table I / Fig 1;
their real patch was ~2*26.32 base with ~26.32 sides).

| Metric | baseline silent-engine | pilot shiny-canyon | vs baseline | threshold | verdict |
|---|---|---|---|---|---|
| billed tokens | 398,130 | 1,579,333 | **+297%** | ≥50% lower | FAIL |
| parts | 424 | 1,392 | **+228%** | ≥40% lower | FAIL |
| wall time | ~1.6 h | 25 h 1 min | **+1463%** | ≥40% lower | FAIL |

Wall time includes ~21 h idle between the solve-3 completion and the user's
return; even excluding that gap the session ran ~4 h of active work versus
~1.6 h baseline. The refactor's own instrumentation did its job: the run
card caught a regression the ceremony should have prevented.

## What the ceremony did right (fair accounting)

- Clarification → ledger: one locked parameter set, one correction
  (the Fig-1 L/W reading) instead of the baseline's three wipe-and-rebuild
  chains.
- Static gate + PASS lines: stages 01–07 all passed first or second try;
  the feed-location assertions (user's steering note) held exactly
  (PatchBowtie xmax == 45.0 mm).
- delete-then-create (ADR 0008): re-runs converged in place repeatedly —
  including geometry correction, variable cleanup, and boundary restore.
  Wipe-and-rebuild never happened.
- Sync-verify runner ultimately printed `PASS: sync replay matches
  snapshot` twice — and in doing so exposed **five genuine template bugs**
  (below). The machinery works; it was just too noisy this run.
- validate_simple() True at every gate; every completed solve profile says
  Normal Completion; physics per solve ~6–7 min (fine).
- The user-in-the-loop gates all fired correctly and caught the real
  domain issue (resonance at 3.85 GHz / −4 dB).

## Where the run went wrong — breakdown of the 1.58 M tokens

### 1. Solve orchestration churn (the largest cost)

- **Five solve submissions** for what should be one. Sequence: solve 1
  (watchdog false stall → user confirms done → teardown purged results) →
  solve 2 (engine error mid-sweep) → solve 3 (OK, then geometry
  correction invalidated it by design) → solve 4 (corrected geometry OK,
  results read impossible) → solve 5 (re-solve after user found UI reset).
  Every submission is an attach + analyze + watchdog launch + status reads,
  each ~10–25 k tokens with full PyAEDT INFO logs.
- **Teardown before banking results** (my worst call): after the user said
  "simulation complete", I tore the desktop down (`close_projects=True`),
  which purged the solved results. The correct order is: bank results
  evidence (profile + counts) FIRST, teardown never before that, and
  `close_projects=False` for solved workspaces.
- **Watchdog semantics guesses**: I passed `EXPECTED_SD=201` assuming one
  `.sd` file per sweep point; this AEDT writes per-frequency `F###` dirs
  (202) and ~11 `.sd` files, so the completion criterion never fired and
  the watchdog fell through to a false `stalled` — escalating to the user
  for nothing. Then without EXPECTED_SD, settle-mode declared `complete`
  once on an engine-error plateau (solve 2), and once genuinely (solve 3).
  The watchdog needs: no guesses, plus a completion confirm reading the
  profile's `Status: Normal Completion` line before claiming done.
- **Stage-08 launcher bugs**: `cleanup_solution` thrusts `GrpcApiError
  DeleteFullVariation` on first-ever solve (benign no-op — fixed by
  skip-if-no-stale), and the PowerShell `Start-Process` quoting broke
  twice before the deterministic `subprocess.Popen(DETACHED_PROCESS)`
  shape landed. Each fix cycle = another run + logs.

### 2. Results retrieval (the unclosed loop)

- The readout surface is this box's documented flaky zone (EC#6:
  "the positive case has not been reproduced since"). I tried ~8 distinct
  shapes across multiple fresh attaches: `get_solution_data` (no name,
  with sweep, with variations, quoted port, VSWR), `create_report`
  (matplotlib both ways), `export_touchstone`, `export_results`. Each
  attempt re-attaches, re-parses, prints the same failing gRPC
  `GetVariables`/`GetSetups` errors, plus a pyAEDT 1.3.0 client bug
  (`HfssConstants.default_solution` missing) breaking the export paths.
- The QA contract already allows "unreadable — flaky readout" reported
  explicitly with the user as arbiter — I kept retrying instead of
  escalating after ONE failed attempt. The user had to read the plot
  twice; the first read surfaced the resonance anomaly, exactly the
  value of the UI gate.

### 3. Sync-verify replays (legitimate, but costly)

Six verify runs over the pilot. They found **five real template bugs**:
(a) `capture_state.py` — `model.variables` is None on fresh attach
(fixed: variable_manager fallback, `.expression` for Variable objects);
(b) `12_verify_sync.py` diff — AEDT random suffixes (`Sweep_XXXXXX`,
`Rad__XXXXXX`) broke equality (fixed: `canon()` normalization before
diff); (c) `make_copy` put scripts at the copy root so `ws_common`'s
WORKSPACE resolved one level up (fixed: copy into `copy/src/`);
(d) `poll_solve.scan_results` counted `.sd` dirs only, missing the
`.sd`/`F###` FILES (fixed: count both); (e) `04_excitations` used the
nonexistent `hfss.delete_boundary` (fixed: `BoundaryObject.delete()`).
Each find was a fix + a full ~8 min replay to confirm. That is the
pilot's real deliverable — the template is significantly more correct
now — but the replays doubled the solve-phase wall time.

### 4. Context hygiene failures (the multiplier)

- Staged-script runs print tens of PyAEDT INFO lines each; ~35 process
  launches across stages ×2 rebuilds + 6 verify replays × 8 scripts +
  probes dumped a huge fraction of the 55.5 M cache reads and 1.86 MB
  conversation store into context with no filtering.
- Exploratory probes were ad hoc (`material_keys` probes, snapshot
  probes, readout probes as throwaway files) rather than one
  purpose-built diagnostics script used once.
- I read full `solve_progress.txt` tails and full verify logs into
  context instead of single-line summaries.

### 5. State / "where is the sim" discipline (user's direct complaint)

- After a 21 h gap the pinned desktop was dead and a new one (55700) had
  come up at a different port; my pinned port was stale; a probe hung on
  the stale pin (the `Desktop(port=...)` attach with a dead pin). The
  ledger is supposed to be the resume point — I re-derived state from
  disk instead of checking the pin liveness first, and a teardown after
  the gap nearly touched an unattended desktop.
- No single "solved/banked" marker: after every solve I had to re-run
  archaeology (profile parse, F-entry counts) instead of reading one
  `results/state/solved.txt`.

## Corrective plan (for the next task, on a better paper)

### A. Clarification changes
1. Add a **dimension-consistency check to the Clarification block**: when
   the recipe comes from a paper, confirm (in the UI question) that the
   user vouches for the Table ↔ Figure ↔ equations mapping; require the
   user's confirmation on the few key dims (base/height/feed) up front,
   not at first QA. A better paper with self-consistent geometry is the
   user's precondition — this check catches the rest.
2. Lock the **results path** in the Clarification: how S11 will be read on
   this box (UI-arbiter ready as the default; scripted readout is a bonus,
   never a blocker), so no run can stall on retrieval again.
3. Keep ONE locked parameter set per run (ADR 0007 already says so) —
   the Fig-1 correction proved the mechanism works.

### B. Solve orchestration (cap submissions to one per verified state)
1. `08_solve.py`: keep the skip-if-no-stale cleanup and the
   `subprocess.Popen(DETACHED_PROCESS)` launcher (both fixed this pilot);
   **no EXPECTED_SD guesses** — settle-mode is the default.
2. `poll_solve.py`: keep the file counting fix; add a final
   **completion confirm** — when the ticker reaches complete/stalled, the
   watchdog appends the parsed `Status:` line from the newest `.profile`
   (Normal Completion / Engine Detected Error) to `solve_progress.txt`, so
   the agent's single read distinguishes done from plateau.
3. **Bank-before-teardown rule**: a solve session only ends after
   `results/state/solved.txt` exists (written by a post-solve confirm:
   profile status + sweep-point count), and teardown for a solved
   workspace uses `close_projects=False`. Nothing else closes.
4. **Resolve-once discipline**: after any solve anomaly, read the profile
   once, then escalate to the user with evidence — never re-submit
   without the user knowing (5 submissions happened this run).
5. On resume: check pin liveness with a bounded connect (short timeout)
   instead of a hanging attach; clear the stale pin and let ws_common
   re-pin.

### C. Readout policy (single shot, then UI)
1. At most ONE scripted readout attempt per session
   (`get_solution_data` with no sweep name — the only shape that ever
   returned data in prior art), one retry on a fresh attach, then the
   question tool hands the plot to the user. Never the ~8-shape
   archaeology of this run.
2. Fix the pyAEDT 1.3.0 readout bug (`HfssConstants.default_solution`)
   as a pre-work tooling item (monkeypatch or route-around validated on a
   throwaway copy), so the scripted path works at all; the acceptance
   never depends on it.
3. Document in the ledger the read route actually used per run (UI vs
   scripted), so summary.md's QA section is honest.

### D. Context hygiene (enforceable rules, not vibes)
1. Run every staged script with `logging` at WARNING (strip PyAEDT INFO
   before it enters context) and filter the bash call to the
   PASS/STAGE_FAILED line plus assertions only.
2. One diagnostics script (`src/diag_solve.py`, written once) that prints
   everything needed in one attach: pin liveness, project path, objects,
   boundary count, profile status, F-entry count, readout one-shot.
   No throwaway probe files.
3. Never read whole progress files into context: tail 1–3 lines.
4. Keep per-stage agent messages ≤ ~250 words (the skill rule, enforced).
5. Explicit bash timeouts on every prolonged call (mostly done; make it
   uniform).

### E. State discipline
1. Ledger gains a **live-state block** updated per stage: desktop port/pid
   pin, solve status, `solved.txt` pointer, next action. Resume reads the
   ledger first, always.
2. `results/state/solved.txt` = machine marker (profile status + counts),
   written by the post-solve confirm script; teardown refuses to close a
   solved workspace's desktop without it.
3. Verify every claim against one machine file — this run proved the
   pattern four times (watchdog false stall, engine-error plateau,
   results purge, desktop reset).

### F. Template deliverables already landed by this pilot (keep)
- `capture_state.py`: variable_manager fallback (variables carried).
- `12_verify_sync.py`: canon() suffix normalization (count-preserving) +
  copy into `copy/src/`.
- `poll_solve.py`: count `.sd`/`.asol` files AND dirs.
- `test_template_runners.py`: make_copy layout tests updated + canon
  count-preservation tests (26/26).
The four files above are synced to
`skill/hfss-agent/templates/workspace/src/`. Fixes 5-6 live only in the
pilot workspace's staged scripts (`04_excitations.py` —
`BoundaryObject.delete()`; `08_solve.py` — skip-if-no-stale cleanup +
Popen DETACHED launch): the template has no per-stage exemplar files to
sync them into, so the pilot workspace is the reference implementation
until a future template pass adds full stage exemplars.

## Measured overhead inventory (token evidence)

- ~35 AEDT-bound process launches across stages, rebuilds, verify replays
  and probes; each adds attach/output overhead.
- 6 verify replays (~8 min each) against 2 full passes and 1 replay that
  eventually PASSed; each replay replays 8 staged scripts on a second
  desktop.
- 8 distinct readout attempts + 2 explicit UI reads.
- 5 solve submissions (one per verified state change) vs 1 expected.
