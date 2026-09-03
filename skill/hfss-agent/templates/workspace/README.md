# Workspace template

One Workspace per conversation, one conversation = three phase sessions
bound by the State ledger (ADR 0007): Clarification → Build (through the
Review gate incl. read-back sync) → Solve+QA. Copy this folder to
`workspaces/<name>/` when a conversation starts (the hfss-agent skill
creates it), then fill the workspace constants (project + design names,
solution type) in `src/ws_common.py` and the placeholders in `state.md`.
Tool and knowledge directories stay clean; workspace outputs are gitignored.

Shape:

```
workspaces/<name>/
├── src/                 # staged scripts, one per Stage: NN_<stage>.py
├── state.md             # the State ledger: stage progress, locked params,
│                        # pitfalls, pointers (ADR 0007)
├── <name>.aedt          # the AEDT project file (created by the staged scripts)
├── results/state/       # machine state, one .txt per key (port, pid, …)
├── results/             # requested plots and exported results
├── summary.md           # acute design decisions + what the Model is + Run card
└── run-report.md        # the run report (+ run-report.json): where the tokens,
                         # wall, retries and escalations went, machine-derived
```

Rules that make the workspace work:

- **Tier 0 first, before any AEDT launch.** `python scripts/tier0.py` runs
  every check that needs no desktop and no license — the runner suites
  against real captured artifacts, the measurement harness, the skill
  markers, the KB checks, and the static gate — in about fifteen seconds.
  It is the cheapest place to find a break, and the fixture corpus it
  checks for is what keeps those tests from silently becoming no-ops (see
  `docs/agents/fixture-fidelity.md`). `scripts/tier1.py --workspace <dir>`
  is the next rung: it builds the model on the live desktop and **refuses
  to run any stage numbered 08 or above**, so it can never consume solver
  time by accident.
- **src/ scripts are the re-runnable record.** One Stage = one script =
  one Run, ending in its `PASS: <stage> <assertions>` Verification line
  (see `src/stage_skeleton.py`). Every script attaches (or launches, first
  stage) through `src/ws_common.py`, which is **port-pinned**: the session
  desktop records its port and pid in `results/state/aedt_port.txt` /
  `aedt_process_id.txt`, and every later attach AND every teardown
  reconnects by that recorded port — a teardown without a pinned port
  refuses to act, so it can never close or kill the user's own desktop.
- **Idempotent stages (ADR 0008).** Delete-then-create: every script
  deletes the objects/boundaries/mesh ops/sweeps it (re)creates before
  creating them, so re-running any stage in place converges. Wipe-and-
  rebuild is an explicit escalation only.
- **Static gate before any AEDT launch.** `python src/00_static_gate.py`
  py_compiles and import-checks every `src/*.py`.
- **State ledger + machine state (ADR 0007).** `state.md` is the human
  record carried between phase sessions; `results/state/*.txt` is the
  machine state (never hand-edited). The session's desktop stays alive
  between stages; only `ws_common.teardown()` (session end) closes it.
- **The solve runs under a detached watchdog (ADR 0006).** `08_solve.py`
  cleans stale results, probes for an in-flight solve, submits
  `analyze(blocking=False)`, launches `python src/poll_solve.py
  <name>.aedt` detached, and exits. The stage-aware watchdog appends one
  line to `results/state/solve_progress.txt` every ~20 s: stage
  (initial meshing / adaptive meshing / frequency sweep / finalizing /
  done) + evidence from the stage-family artifacts (`*.imesh`/`*.cmesh`,
  `*_ADP*`, `*_F####_SU.txt`) and the newest `.profile`'s stage ledger
  and terminal `Status` footnote. It exits with 0 on complete (profile
  `Status: Normal Completion` + settle), 2 on stalled (stage named), 3 on
  aborted (any non-Normal profile status appended verbatim, or in-flight
  markers gone + no completion + solver process dead). No output-count
  prediction anywhere. The agent only reads the state file — never
  foreground-polls, never estimates.
- **Read-back sync is verified mechanically (ADR 0005).**
  `python src/capture_state.py` snapshots the live model into
  `results/state/model_snapshot.json`; after user UI tweaks and the
  sync amends, `python src/12_verify_sync.py` replays the amended
  scripts on a fresh copy under `results/state/verify/` on a port-pinned
  second desktop, captures the same shape there, diffs, and prints one
  `PASS: sync replay matches snapshot` / `FAIL: sync mismatch — <differing
  keys>` line,
  then tears that second desktop down port-pinned (the live session
  desktop is never touched).
- **summary.md is written at the end of the conversation** (see skeleton),
  updated by read-back sync deltas and learning-loop notes; the `## Run
  card` section is filled by the measurement harness
  (`scripts/run_card.py --summary summary.md`).
- **End-of-run checklist, in this order, every command from the repo root:**
  1. `python scripts/record_outcome.py --workspace workspaces/<name>
     --outcome completed|escalated|abandoned --completions <n> --note "<user
     verdict verbatim>"` — the outcome in the key=value form the card parses.
  2. `python scripts/run_card.py --workspace workspaces/<name> --summary
     workspaces/<name>/summary.md` — the measured card, appended.
  3. `python scripts/run_report.py --workspace workspaces/<name>` — the run
     report, `run-report.md` + `run-report.json`, beside `summary.md`.
  Each prints one `PASS:` line; the run is closed out when all three have.
- `.aedt`, `.aedtresults/`, `results/`, and lock files are gitignored;
  `src/`, `state.md`, `summary.md`, `run-report.md` and `run-report.json`
  are the tracked record.
