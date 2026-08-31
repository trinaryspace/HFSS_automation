# STATUS — 2026-08-31

Where this project actually is, written for someone picking it back up after two
weeks away. Every claim below traces to a file in the repo or to a command run on
this box on 2026-08-31; where something could not be checked, it says so.

Read `AGENTS.md` and `CONTEXT.md` first for the vocabulary — this file uses it
(Spine, Stage, Recipe, Workspace, Review gate, Readout, Learning loop, State
ledger, Bank).

---

## 1. Where development is

The project is in **phase 2, the spec-driven route**. The spec that defines it is
`.scratch/hfss-agent-spec-driven/spec.md`; the tickets are the numbered files in
`.scratch/hfss-agent-spec-driven/issues/`.

Phase 1 made the agent's primary output artifact free-form Python — ten staged
scripts per run — and every containment mechanism in the repo (static gate,
`PASS:` Verification line, ADR 0008 idempotency-as-discipline, the two-desktop
sync replay, the 4,376-file KB) existed to bound the blast radius of that one
choice. The post-refactor pilot (`shiny-canyon`) cost 1,579,333 tokens / 1,392
parts / ~25 h and returned NO-GO on all three acceptance axes. Phase 2's response
is to move the centre of gravity from generated code to a **validated Design Spec
plus a hand-written compiler**:

```
request --> Clarification --> design.yaml --+--> validate_spec   (schema/refs/units)
                                            +--> precheck        (closed-form physics)
                                            +--> compile_spec --dry-run
                                                      |
                                                      v
                                             compile_spec --launch
                                                      |  live AEDT model
                                                      v
                                             Review gate (visual, ADR 0003)
                                                      v
                                             solve under detached watchdog (ADR 0006)
                                                      v
                                             bank --> Result QA --> summary.md
```

**What exists and runs today.** `hfss_spec/` is the phase-2 core: `schema.py`,
`loader.py`, `validate.py`, `units.py`, `expressions.py`, `physics.py`,
`compiler.py`, `model_checks.py`, `feed_check.py`, `snapshot_to_spec.py`,
`session.py`, `acceptance.py`, with their tests alongside. The offline gates, the
compiler, the phase-session boundary and the tiered harness are all implemented
and are what the last run used end to end.

**What does not exist.** Ticket 14's deterministic orchestrator — the state
machine that would run the Spine and call the model at exactly three seams
(clarify / diagnose / narrate). Today a run is still a conversation, and the
conversation's length is the bill. Ticket 14 is marked *"now the highest-priority
item in the backlog"* on the strength of three independent measurements from the
2026-08-17 campaign: cell S11 spent 51 min / 151,526 tokens / 250 parts writing a
2D field solver inside a Clarification block and delivered nothing; cells X0a and
X0b got byte-identical prompts and cost 106,932 vs 201,765 billed (an 88% spread);
every Wave A cell spent 109–301 parts before anything was built.

**Ticket status across phase 2** (the `Status:` line in each issue file):
`ready-for-human` on 01–05, 07–11 and 12a; `ready-for-agent` on 12 and 15;
`needs-triage` on 06, 13, 14, 16 and 17.

The campaign's own one-paragraph verdict, in
`.scratch/hfss-agent-parallel-tests/RECOMMENDATIONS.md`, is worth re-reading
before choosing the next piece of work: an LLM *can* author a valid spec (6/6,
zero escape hatches), the schema is not the bottleneck, and **half of the specs
that pass every automated gate are wrong** — always in a *relational* property no
gate examined at the time. Two relational gates landed afterwards on
`worktree-spec-fixes-2026-08-17` (since merged); the feed-network walk
(`hfss_spec/feed_check.py`) is the third.

---

## 2. The last run — `workspaces/patch-array-5800`

Sources: that workspace's `summary.md` and `state.md`, plus the machine state
under its `results/state/` on disk.

**What it was.** A 2x2 array of rectangular microstrip patches at 5.8 GHz on
RO4350B (er 3.48, tand 0.0037, h 0.762 mm), element spacing lambda0/2 =
25.8442 mm, fed by a corporate microstrip network from one 50 ohm input. The brief
(`.scratch/hfss-agent-parallel-tests/TASK-verify-2x2-feed.md`) asked the run to
**falsify** the corrected corporate feed, and required the feed to be matched to
the *active* element impedance rather than the isolated one. One project, two
designs: `ElementsOnly` (four patches, a lumped port at each notch mouth — the
Z_act extraction model) and `PatchArray` (the fed array, one wave port).

**Three solves banked**, all `Normal Completion`:

| solve | design | passes | sweep pts | note |
|---|---|---|---|---|
| #1a | ElementsOnly, flat PEC | 2 adaptive | — | superseded by the copper change; record kept |
| #1b | ElementsOnly, 1-oz copper | 10 adaptive | 150 | |
| #2 | PatchArray, 1-oz copper | 14 adaptive | 150 | watchdog done 19:07:16 local |

`results/state/solved.txt` reads `status=Normal Completion`, `sweep_points=150`,
`banked_at=1787096304`.

**The result.** Resonance came in at **5.6 GHz, ~7 dB deep, in BOTH designs**
(the user's UI read — see below for why it was a UI read). The verdict recorded
verbatim in `summary.md`: *"So the resonance for both the single patch and the
array is at 5.6 GHz and are about 7dB deep. That isn't outright failure, its just
a tuning issue that can be corrected with a human hand."*

**What that does and does not settle.** The shift is at the *same frequency in
both designs*, so it is element-level (Balanis fringing / er on this stack), not
the feed. And ~7 dB is not the −9..−10 dB in-band signature the approved QA band
defined as the 2:1 feed defect. So **the feed was not falsified**. It was also
**not vindicated**: the run's whole method was to measure Z_act on `ElementsOnly`
first and re-denominate the network to it, and that extraction was **parked** —
every scripted readout hit `GrpcApiError` (`GetVariables` / `GetPropValue`
classes). `results/state/z_act.txt` contains, verbatim,
`readout=unreadable - create_report raised: GrpcApiError: Failed to execute gRPC
AEDT command: GetVariables`. The active-vs-isolated question the run was built to
answer is still open.

The correction path recorded in `summary.md`: retune `patch_L` (and re-derive
`q_x`) for 5.6 GHz, or set `f0 = 5.6 GHz` and rebuild, then re-check dip depth —
the −25 dB band is the feed's acceptance test, and Z_act (UI-arbitrated, or via a
recovered channel) remains the proper match target at half-wave spacing.

---

## 3. Outstanding, honestly ordered

**1. An AEDT desktop from that run is still alive, 13 days on.**
`results/state/aedt_process_id.txt` reads `25840`. Checked on 2026-08-31:
`Get-Process -Id 25840` returns `ansysedt`, started 2026-08-18 18:51:56, ~543 MB
working set. It has been holding a licence seat ever since. It was deliberately
left alive because two QA reads were still owed against it (below) — but 13 days
is not what "the session's desktop stays alive between stages" was meant to mean.
Decide: take the two reads now, or release the seat. The workspace is banked, so
closing it loses nothing — `results/state/solved.txt` is the survival evidence.

**2. Two Result-QA reads were never taken.** Broadside gain (expected 12–13 dBi)
and element balance (near-field symmetry). Both are UI-arbitrated under the same
readout policy that forced the S11 read into the UI. `state.md` lists them under
*"Pending"*.

**3. The readout question.** The run recorded scripted readout failure as
*systematic* over this pairing (AEDT 2024 R1 / pyAEDT 1.3.0) — attempted once plus
one retry each, route recorded in `results/state/readouts.txt` — and fell back to
the UI. Whether that is genuinely systematic or a degraded long-lived gRPC channel
is **not settled** by the evidence in the workspace: the same session had already
had `GetVariables` and `Subtract` fail mid-session and had been recycled once.
Work is in flight on exactly this — a change making "fresh attach" mean a fresh
*process* is being landed in `skill/hfss-agent/templates/workspace/src/`
(`read_results.py`, `ws_common.py` and their tests), alongside an untracked
`.scratch/hfss-agent-parallel-tests/TASK-readout-channel-vs-systematic.md`. Read
those before re-litigating the question; this document does not assert their
contents.

**4. Three learning-loop amendments are pending user approval (ADR 0002).**
Nothing has been applied — ADR 0002 is append-only-after-approval, and the run
respected it. From `summary.md`:

1. register an estimator for the `corporate-patch-array` recipe in
   `knowledge/playbook/precheck-tolerances.json`. That recipe has none today, so
   `precheck` returned `no-estimator` / UNCHECKED for both specs.
2. environment-compat notes — (a) `unite` is like-to-like only: boxes with boxes,
   planars with planars; mixed sets silently no-op on 2024 R1 / pyAEDT 1.3.0;
   (b) 2D sheets have no "Material" attribute-tab property on 2024 R1
   (`material_name` returns `''`; the saved project's `MaterialValue` is
   authoritative, and the GUI shows "unassigned"); (c) scripted result readouts
   fail over this pairing's gRPC; (d) setup prop-key spellings vary between
   sessions — normalize in `12_verify_sync` `canon()`.
3. keep `verify_spec_replay.py` in the workspace as the design-spec route's
   ADR-0005 replay (`12_verify_sync` only replays numbered staged scripts).

An untracked `knowledge/playbook/pending-amendments.md` is being written by
another worker to hold these; its contents are not asserted here.

**5. The `patch_resonance` estimator missed by 3.4%.** Verified offline before the
run and recorded in `state.md`: `patch_resonance(13.6238, 17.2679, 0.762, 3.48) =
5.8000 GHz` — *exact*. Hardware said 5.6 GHz. That is a 3.4% overprediction, which
is **inside** the 5% tolerance registered for `inset-fed-rectangular-patch` in
`precheck-tolerances.json` — so the gate would have passed it even had an
estimator been wired to this recipe. The interesting failure is not the number; it
is that a closed form reporting "exact" bought no confidence. An untracked
`.scratch/hfss-agent-parallel-tests/estimator-calibration.md` is being written on
this by another worker; read it rather than re-deriving.

**6. Ticket 14's remaining checklist**
(`.scratch/hfss-agent-spec-driven/issues/14-deterministic-orchestrator.md`).
Done: session boundaries enforced (`hfss_spec/session.py`, 17 tier-0 tests, wired
into `compile_spec`) and a per-session call budget (default 60). Both are recorded
as **partial by construction** — the boundary covers every expensive action that
goes through this repo's tooling and does *not* cover an arbitrary `python -c`,
which is how S11 actually wrote its solver. Still unticked:

- per-phase tool gating in the harness — the piece that would actually have
  stopped S11;
- decide when an undeclared session flips from unguarded to "declare or refuse";
- exactly three LLM call sites, with a test asserting no others exist;
- all three using structured output against the exported JSON Schema;
- the ledger as sole resume point: a killed run resumes without redoing
  clarification;
- capped diagnosis that escalates with the script, the finding and the attempts
  attached;
- the run card broken down by seam;
- both human gates preserved, in the same place, with the same authority.

**7. Repo hygiene.** See §6. Nothing there is urgent; the orphaned-work problem it
used to describe is now solved (§6.3).

---

## 4. How to run things

All commands run from the repo root, with this box's Python.

**Tier 0 — offline, no licence.** Run before any AEDT launch.

```
python scripts/tier0.py            # everything
python scripts/tier0.py --list     # show the suites without running
python scripts/tier0.py -v         # stream each suite's own output
```

It prints one line in the house format: `PASS: tier0 suites=N failed=0`. The most
recent recorded run is `PASS: tier0 suites=14 failed=0 elapsed=101s` (2026-08-18,
in the patch-array ledger); the campaign log records `suites=10 ... elapsed=229.3s`
on 2026-08-16. The workspace template README still says "about fifteen seconds",
which no measurement in this repo supports — budget minutes. **Not re-run for this
document**: other work is in flight in `skill/hfss-agent/templates/workspace/src/`,
so a result now would describe neither the committed tree nor the finished change.

**Tier 1 — builds on the live desktop, never solves.** Needs a licence and the VPN
up so the licence server is reachable.

```
python scripts/tier1.py --workspace workspaces/<name>
python scripts/tier1.py --workspace workspaces/<name> --dry-run
```

It **refuses** any stage numbered 08 or above — refuses, not skips — so it cannot
consume solver time or licence-hours by accident.

**Tier 2** is the full end-to-end run including solve, readout and QA. There is no
single script for it; it is the skill's own path (`skill/hfss-agent/SKILL.md`).

**Phase sessions (ADR 0007 / ticket 14).** One command at the top of each session;
this is the step that turns the boundary *on*. An undeclared session is currently
unguarded, deliberately, so the boundary could land without breaking older
workspaces.

```
python scripts/session.py --workspace workspaces/<name> --phase clarify
python scripts/session.py --workspace workspaces/<name> --phase build
python scripts/session.py --workspace workspaces/<name> --phase solve
python scripts/session.py --workspace workspaces/<name>      # report phase + budget
```

Once declared, a clarify session cannot `compile_spec --launch`, and only a solve
session may solve. `--budget N` overrides the default call budget (0 disables it).

**The spec-driven gates, in the order they run:**

```
python scripts/validate_spec.py <path/to/design.yaml>          # --schema, --quiet
python scripts/precheck.py      <path/to/design.yaml>          # --strict for a nonzero exit
python scripts/compile_spec.py --workspace workspaces/<name> --spec <design.yaml> --dry-run
python scripts/compile_spec.py --workspace workspaces/<name> --spec <design.yaml> --launch
```

`validate_spec` exits 0 only when there are no errors, so it is usable as a gate.
`precheck` **never blocks** — exit 0 even on an inconsistent verdict, because the
user arbitrates which reading is canonical and the choice is recorded in the spec's
`provenance.canonical_reading`. `compile_spec` builds only and never solves; solve
submission stays imperative under the detached watchdog (ADR 0006).

---

## 5. The map

| path | what lives there |
|---|---|
| `hfss_spec/` | the phase-2 core: schema, loader, validator, units, expressions, closed-form physics, the spec compiler, relational model checks, the feed-network walk, snapshot-to-spec, the phase-session boundary — plus their tests |
| `scripts/` | the entry points: `tier0.py`, `tier1.py`, `session.py`, `validate_spec.py`, `precheck.py`, `compile_spec.py`, `run_card.py`, `install_skill.py`, fixture capture, spec acceptance |
| `skill/hfss-agent/` | the agent-facing skill: `SKILL.md`, `reference/execution.md`, `reference/design-spec.md`, and `templates/workspace/` — the workspace template every run is copied from, including the real-artifact fixture corpus |
| `knowledge/` | `playbook/` (environment-compat entry, `spine-api.md`, `precheck-tolerances.json`), `cases/` (five canonical cases plus `_snapshots/`), `reference-papers/` (user-supplied PDFs) |
| `scraping/` | the KB: the crawler, `verify_kb.py`, and `pyaedt_ai_context/` — the scraped pyAEDT API corpus, demoted to a cold-path fallback under phase 2 |
| `workspaces/` | one folder per conversation. `src/`, `state.md` and `summary.md` are tracked; `.aedt`, `.aedtresults/`, `results/` and lock files are gitignored |
| `.scratch/` | the issue tracker, one folder per feature: `hfss-agent-foundation/`, `hfss-agent-perf-refactor/`, `hfss-agent-spec-driven/` (the live one), `hfss-agent-parallel-tests/` (the 2026-08-16/17 campaign) |
| `docs/adr/` | eight settled decisions — 0001 re-entry copies, 0002 approved amendments only, 0003 visual review gate, 0004 the pyAEDT pin, 0005 script re-sync, 0006 detached watchdog, 0007 phase sessions, 0008 idempotent stages |
| `docs/agents/` | the working conventions: issue tracker, triage labels, domain docs, fixture fidelity |

---

## 6. Repo audit — 2026-08-31

### 6.1 Stale worktrees and their branches

Twelve worktrees from the 2026-08-16/17 campaign are still registered under
`.claude/worktrees/`, and the directory totals **914 MB** (~70 MB each; that figure
includes the active `handoff-2026-08-31` worktree). From `git worktree list`,
`git branch -a -vv` and a per-branch `git log main..<branch>`:

| worktree | branch | on origin? | commits not in `main` | safe to remove? |
|---|---|---|---|---|
| `spec-fixes-2026-08-17` | `worktree-spec-fixes-2026-08-17` | yes, same SHA | 0 — **merged into main** | **yes** |
| `test-plan-2026-08-16` | `worktree-test-plan-2026-08-16` | yes, same SHA | 0 — **merged into main** | **yes** |
| `capability-writeup` | `worktree-capability-writeup` | yes, same SHA `92fdc9c` | **2** | worktree yes; **branch: do not delete** |
| `flush-face-fix` | `worktree-flush-face-fix` | yes, same SHA `587cc23` | **3** | worktree yes; **branch: do not delete** |
| `cell-S1` | `cell/S1` | **no** | 1 — `0b281ed` "wip" | see below |
| `cell-S4` | `cell/S4` | **no** | 1 — same `0b281ed` | see below |
| `cell-S7` | `cell/S7` | **no** | 1 — same `0b281ed` | see below |
| `cell-S3` | `cell/S3` | **no** | 2 — `d7295ab`, `0b281ed` | see below |
| `cell-S6` | `cell/S6` | **no** | 1 — `a22e612` "wip" | see below |
| `cell-S11` | `cell/S11` | **no** | 1 — same `a22e612` | see below |
| `cell-X0a` | `cell/X0a` | **no** | 2 — `31485d1`, `0b281ed` | see below |
| `cell-X0b` | `cell/X0b` | **no** | 2 — same | see below |

Three further local branches have no worktree: `campaign/base` (= `a22e612`),
`campaign/base-nohorn` (= `d7295ab`) and `campaign/base-nopatch` (= `31485d1`).
Two more, `phase-2-spec-driven` and `ticket-06-model-experiment`, are **merged into
main** and safe to delete.

**Branches whose deletion would lose commits — flagged explicitly:**

- **`worktree-capability-writeup`** — 2 commits not in `main`: `6be8544` "the
  capability report: what the tool does today, and what it has not proven" and
  `92fdc9c` "the guiding vision: the layer the ADRs are answerable to". It branched
  from `cba0b91` (= `origin/main`), not from current `main`. It **is pushed** to
  `origin/worktree-capability-writeup` at the identical SHA, so the commits survive
  a local delete — but they are in no mainline and would otherwise be forgotten.
  Merge or cherry-pick before deleting the local branch.
- **`worktree-flush-face-fix`** — 3 commits not in `main`: `1d89a39` "a flush
  boundary face is only legitimate under a wave port", `c5dc257` "post-mortem on
  the 2x2 run, and the recommendations that follow", `587cc23` "see the geometry
  before AEDT does, and fix what the gates could not see". Same story: pushed to
  origin at the identical SHA, still unmerged. This one bears directly on §2 and
  §3 — read `c5dc257` before re-doing the post-mortem.
- The eight **`cell/*`** and three **`campaign/*`** branches are **local only** —
  no remote tracking, nothing on origin. Their unmerged commits (`0b281ed`,
  `a22e612`, `d7295ab`, `31485d1`, all titled "wip") are **pure deletions**,
  verified: `0b281ed` and `a22e612` are each 152 files / 28,915 deletions with
  **zero added lines**, wiping `workspaces/` to clean-room the cell; `d7295ab`
  deletes `knowledge/cases/horn-10ghz/`; `31485d1` deletes
  `knowledge/cases/patch-2400/`. Deleting these branches loses nothing but the
  clean-room conditions, which are described in
  `.scratch/hfss-agent-spec-driven/campaign-runbook.md`.

**But the cell worktrees hold uncommitted output.** Each cell's actual product —
the `design.yaml` the LLM authored — sits *untracked* in its worktree:

| worktree | untracked (beyond `__pycache__`) | already preserved? |
|---|---|---|
| `cell-S1` | `workspaces/patch-5800/{design.yaml,state.md}` | `design.yaml` identical to `.scratch/.../cells/S1.design.yaml`; `state.md` **not preserved** |
| `cell-S3` | `workspaces/horn-10ghz/{design.yaml,state.md}` | `S3.design.yaml` identical; `state.md` not preserved |
| `cell-S4` | `workspaces/dipole-2450/{design.yaml,state.md}` | `S4.design.yaml` identical; `state.md` not preserved |
| `cell-S7` | `workspaces/patch-array-5800/{design.yaml,state.md}` | `S7.design.yaml` identical; `state.md` not preserved |
| `cell-X0a` | `workspaces/patch-2400-inset/{design.yaml,state.md}` | `X0a.design.yaml` identical; `state.md` not preserved |
| `cell-X0b` | `workspaces/patch-2400/{design.yaml,state.md}` | `X0b.design.yaml` identical; `state.md` not preserved |
| `cell-S6`, `cell-S11` | none | consistent with the honesty cells delivering no spec |
| `flush-face-fix` | `workspaces/bowtie-3500-pilot/results/state/model_snapshot.json` | gitignored path, regenerable by `capture_state.py` |

All six `design.yaml` files were diffed against their `.scratch` copies on `main`
and are byte-identical modulo line endings. The **six `state.md` files (60–85 lines
each) are the only artifacts not preserved anywhere else** — only
`X0a-DRY.state.md` made it into `.scratch/hfss-agent-parallel-tests/cells/`.

**Recommendation (not executed).** Copy those six `state.md` files into
`.scratch/hfss-agent-parallel-tests/cells/` as `S1.state.md` … `X0b.state.md`
first. Then remove all twelve worktrees and delete the `cell/*` and `campaign/*`
branches. Keep `worktree-capability-writeup` and `worktree-flush-face-fix` as
branches until their commits are merged or explicitly abandoned. Nothing has been
deleted; this is a recommendation only.

Caveat on the method: this audit compared each worktree's on-disk file list against
its branch tree, which finds **untracked** files. It could not run `git status`
*inside* those worktrees, so a *modified tracked* file in one of them would not
have been detected. Before removing any worktree, check its status is clean.

### 6.2 Tracked files that arguably should not be

Nothing accidental is tracked. Two deliberate-but-heavy items:

- `scraping/pyaedt_ai_context/rag_knowledge_base.jsonl` — **23.3 MB**, by far the
  largest tracked file, and *generated* by `scraping/generate_pyaedt_ai_context.py`
  from the same corpus that is already tracked file-by-file. It is not free to
  drop: `scraping/verify_kb.py` reads it, and `verify_kb` is a tier-0 suite. If the
  KB really is demoted to a cold-path fallback under phase 2, this file is the
  first thing to reconsider.
- `knowledge/reference-papers/*.pdf` — ~13 MB across four PDFs. Deliberate
  (ticket-10, user-supplied reference papers, with a README). Noted for size only.

The drop from 8,415 to 4,382 tracked files under `scraping/` between `origin/main`
and local `main` is **not** a loss: commit `3ac1f86` records a one-off prune of
4,035 `.rst.md` stub pages the scraper should never have fetched, with the corpus
rebuilt and the scrub recorded in the KB provenance.

Latent gap: the `workspaces/<name>/<name>.pyaedt/` sidecar directories AEDT creates
are matched by no `.gitignore` rule. They are empty on every workspace today and
git does not track empty directories, so nothing has leaked — but a rule would
close the trapdoor. Left alone rather than guessed at.

### 6.3 Reconciling `main` with `origin`

- `origin/main` is at `cba0b91`, last pushed **2026-08-02**.
- Local `main` is at `b45680d` — **45 commits ahead**, dated 2026-08-04 through
  2026-08-18.
- `handoff/2026-08-31` is at `bc9a052`, **47 commits ahead of `origin/main`**, and
  **is pushed** (`origin/handoff/2026-08-31` at the same SHA). It is local `main`
  plus two recovery commits: `2d9a6d0` (the feed-walk box-strip fix) and `bc9a052`
  (the `patch-array-5800` run workspace, committed as it stood).

So nothing is orphaned any more: every local commit through 2026-08-31 is on
GitHub, on `handoff/2026-08-31`. What remains is the user's call — `origin/main`
still points at 2026-08-02 work. Local `main` is strictly an ancestor of
`handoff/2026-08-31`, so reconciling is a fast-forward with no conflicts: open a
PR from `handoff/2026-08-31` into `main`, or fast-forward `main` locally and push
it. Deliberately not done here.

### 6.4 `.gitignore`

Two groupings appended, in the file's existing style — a short comment saying
*why*, above each rule:

- `.claude/worktrees/` — full second checkouts, ~70 MB each, disposable because
  their commits already live in the shared object store via their own branches.
- `/package.json` — the `@opencode-ai/desktop` 1.18.11 manifest the opencode tool
  drops at the repo root. This repo is pure Python and has no npm surface.
  **Root-anchored deliberately**: a bare `package.json` would match at any depth
  and could one day swallow a real one silently, and a silently-ignored source file
  is a worse failure than a stray tool artifact. The comment says to delete the
  line rather than reach for `git add -f` if this repo ever grows an npm surface.
  Verified with `git check-ignore`: root `package.json` is ignored,
  `skill/package.json` is not.

The stray `package.json` itself is still on disk in the main checkout. Ignoring it
does not remove it — deleting it is recommended, and left to the user.

---

## 7. What this document does not know

- Whether tier 0 passes right now. Not re-run; see §4.
- The contents of `knowledge/playbook/pending-amendments.md`,
  `.scratch/hfss-agent-parallel-tests/estimator-calibration.md`,
  `.scratch/hfss-agent-parallel-tests/TASK-readout-channel-vs-systematic.md`, and
  the readout fresh-process change in `skill/hfss-agent/templates/workspace/src/` —
  all in flight from other work on 2026-08-31, and referenced by name only.
- Whether the stale worktrees contain *modified tracked* files (§6.1 caveat).
- The true broadside gain and element balance of the last run. Nobody has read
  them.
