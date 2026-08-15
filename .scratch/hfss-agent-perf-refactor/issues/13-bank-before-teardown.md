# 13 — Bank-before-teardown: solved marker and teardown guard

**What to build:** The results-purge failure class ends. A solve session ends by banking: a post-solve confirm reads the solve evidence (newest profile status + sweep-point count) and writes the solved marker to the machine state, making the solved workspace durable. Teardown becomes guarded: a banked workspace tears down with projects left open on disk (`close_projects=False`) while the desktop process is still reaped; an unbanked workspace that shows solve evidence on disk is refused with an actionable "bank it first" message and a non-zero exit; a workspace with no solve evidence tears down exactly as today. The solve lifecycle contract — watchdog terminal → confirm → bank → teardown — is recorded in the amended ADR 0006 (docs ticket 19 reconciles and commits it).

**Blocked by:** None — can start immediately.

**Status:** ready-for-human

- [ ] A solved workspace gains the solved marker after the post-solve confirm (status + sweep count + bank time)
- [ ] Teardown of a banked workspace keeps the project and results on disk and reaps the desktop process
- [ ] Teardown of an unbanked workspace with solve evidence on disk refuses with an actionable message and non-zero exit
- [x] Build-phase and verify-copy teardowns behave exactly as today
- [x] Template-runner tests green (no-AEDT seam covers the guard decision logic)

## Comments

- 2026-08-07 (ticket 13, bank-before-teardown): Build = `src/confirm_solve.py` (new), the teardown guard in `ws_common.py` (teardown function only + appended guard helpers), and appended `TestConfirmSolve` + `TestGuardedTeardown` classes in `test_template_runners.py`. Not touched: `poll_solve.py`, `execution.md`, `SKILL.md`, ADR 0006.

  **What was built.**
  1. `confirm_solve.py` (filesystem-only, stdlib, no pyAEDT, no other-module imports) — reads the solve evidence from `<project>.aedtresults/` and banks it: pass `<project>.aedt` via argv[1] / `SOLVE_PROJECT` / single `.aedt` in the workspace (the poll_solve resolution contract). Newest `*.profile` (mtime) → terminal `'Status'` token from the Stop-Time ProfileFootnote (LAST `'Status','…'` pair wins; missing footnote = unfinished/crashed/never-run). Sweep-point count = `*_SU.txt` beside the profile sharing its `DV<id>` prefix (pilot ground truth: `DV3019_S1918_V2657_F####_SU.txt`, 200/family; a stale earlier family `DV2569_…` in the same results dir is excluded; no DV prefix → counts all). In-flight test = any `*.semaphore` touched AFTER the newest terminal profile (pilot evidence: kill-based releases leave semaphores behind — `.Bowtie3501.asol.semaphore` at 00:29 vs profile at 00:48 — so a raw counts-test would never clear; older-than-their-completion semaphores are ignored). Writes `results/state/solved.txt` as key=value lines `status=… / sweep_points=… / banked_at=<epoch>` and prints one `PASS: confirm_solve banked status=… sweep_points=… banked_at=…` line; exit 0. Non-`Normal Completion` terminal statuses (e.g. `Engine Detected Error`, the pilot solve-2 class) ARE banked — the marker's status field carries them and a `!` warning line is printed for the resolve-once read — so confirm and the guard can never deadlock. Refuses (exit 2, nothing written) when no terminal profile exists or an in-flight solve is detected.
  2. `ws_common.py` teardown guard — `guard_verdict(project, state_dir=None)` is a pure, filesystem-only three-way decision shared with confirm via a lazy `import confirm_solve` (one parsing truth): `banked` (solved.txt exists) → `release_desktop(close_projects=False, close_on_exit=True)` + the existing reap kill-loop unchanged; `refuse` (unbanked but newest terminal profile with no in-flight semaphores) → prints `teardown refused: solve evidence on disk is NOT banked — tearing down would purge the solved results. Bank it first: python src/confirm_solve.py <project>.aedt, then re-run teardown.` and `os._exit(2)` BEFORE any attach/release — the desktop is never touched; `proceed` (neither) → byte-for-byte today's `close_projects=True` release + reap. Build-phase, verify-copy (make_copy excludes `.aedtresults` and `results/` → always `proceed`), mid-flight (fresh semaphores, no completion), and unfinished-profile workspaces all land in `proceed`.
  3. Tests appended to `test_template_runners.py`: 12 confirm tests (terminal parse incl. last-token-wins and unfinished/missing → None, newest-terminal skips unfinished-newer, DV-prefix sweep counting + no-prefix fallback, in-flight/stale semaphore test, banking incl. non-normal status + warning, both refusal exits) and 7 guard tests (banked-with-evidence, banked-no-results-dir, unbanked-with-evidence → refuse, never-solved → proceed, unfinished → proceed, in-flight → proceed, verdict constants distinct), all on fixture state (temp trees + fixed mtimes/`now`).

  **Verification evidence.**
  - `python -m py_compile src/confirm_solve.py src/ws_common.py src/test_template_runners.py` — clean.
  - Static gate on the template: `PASS: static_gate compiled=8 imported=7` (was 7/6; confirm_solve.py now passing the compile+import gate).
  - `python src/test_template_runners.py TestConfirmSolve TestGuardedTeardown -v` — 19/19 OK.
  - Branch trace (throwaway script, no AEDT, fixture trees):
    - [A] banked → `guard_verdict -> banked` (close_projects=False, still reaps)
    - [B] unbanked + evidence → `guard_verdict -> refuse`; `confirm_solve -> rc=0 PASS: … sweep_points=200`; marker contents `status=Normal Completion/sweep_points=200/banked_at=1786073539`; verdict after bank → `banked`
    - [C] neither (no results tree) → `proceed` (today's behavior)
    - [D] fresh semaphore after last completion → `guard_verdict -> proceed`; `confirm_solve -> rc=2` (in-flight, nothing banked)
    - [E] unfinished newest profile → `proceed`; confirm rc=2 (no terminal profile)
    - [F] `Engine Detected Error` terminal → confirm rc=0, verdict -> banked (results kept)

  **Concurrency note (must land at integration):** the batch's parallel ticket-14 agent replaced `poll_solve.py` in this shared working tree mid-flight (stage-aware rewrite, written 12:43 today) before its own tests landed. The old `TestPollSolveScan`/`TestPollSolveStateMachine` tests in `test_template_runners.py` now fail against it (8 failures: `scan_results` tuple→dict shape, `watchdog_tick` dict metrics, `format_progress` signature) — the file's poll tests are untouched-old code, my append is exclusive, and all other suites (confirm, guard, capture, verify, gate) are green. This is ticket 14's reconciliation (its prompt owns a new leaf test module and the completion rule); coordinate deletion/replacement of the old poll tests there. At HEAD the suite was green (24/24); the red is not from ticket 13's change.
