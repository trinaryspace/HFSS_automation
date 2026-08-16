# State of the tool — 2026-08-16

Status: needs-triage
Feature: hfss-agent-spec-driven
Audience: a fresh session asked to plan improvements.

Read this first, then the paths it points at. It does not duplicate the specs,
ADRs or tickets — it says what is true, what is proven, what is only claimed,
and where the next win is. Everything here is evidence-backed; where it is not,
it says so.

---

## 1. Measurement history — four runs, scored honestly

| run | date | route | billed | parts | wall | completed? |
|---|---|---|---|---|---|---|
| `silent-engine` | 08-03 | free-form scripts | 398,130 | 424 | ~1.6 h | yes |
| `shiny-canyon` | 08-06 | free-form + `/implement` meta-work | 1,579,333 | 1,392 | 25 h | **no** |
| `kind-rocket` | 08-15 | staged scripts (Route B) | 346,993 | 477 | 41 min | yes |
| `swift-otter` | 08-16 | staged scripts, **replayed** | 123,448 | 312 | 23 min | **no** |

Notes that matter more than the numbers:

- `silent-engine` is the baseline and predates the subagent tier, so its
  398,130 is the whole run. `kind-rocket` is 269,378 main loop + 77,615
  subagents; **compare combined totals or you will flatter yourself.**
- `shiny-canyon` was launched through the `/implement` meta-skill carrying
  ticket text, TDD, code-review and commit instructions, so a real share of its
  1.58 M was never HFSS work. It is a bad baseline for anything.
- `swift-otter` is **not a valid data point** — see §3.
- The spec's phase-2 acceptance threshold is **≤80,000 billed and ≤60 parts**.
  Nothing has come close on parts. The best honest run is 477.

**The metric is cost per *completed* simulation** (`scripts/run_card.py`,
ticket 04). A run that burns tokens and delivers no readable result scores as
infinite, not as "somewhat worse". Two of four runs score infinite.

---

## 2. What exists and is proven

**Phase 2 is built and correct.** `hfss_spec/` — units and dimensional algebra,
expression evaluation, the Pydantic schema, the offline validator, the
snapshot reducer, the compiler, the acceptance diff, the closed-form physics
pre-check. 79 Tier 0 tests, ~1 s, no license. Six CLIs in `scripts/`.
Route documentation in `skill/hfss-agent/reference/design-spec.md`.

Proven on hardware, not just in tests:

- **The compiler reproduces the pilot's bow-tie exactly** — zero snapshot
  differences, zero bbox differences, `validate_simple=True`. That model took
  a 25-hour pilot to produce the old way; the compiler rebuilt it from a
  document in about a minute. (Ticket 11.)
- **Microstrip and the horn built clean, first attempt each.** The horn's flare
  is a `connect` loft, so the Q1c decision — native modeler over an external
  CAD kernel — is vindicated on hardware, with zero escape-hatch ops.
- **Parametrics survive**: a compiled microstrip reads back
  `sub_W: 'trace_W + 12*h'`, the expression, not an evaluated number.
- **The physics pre-check works and is honest**: it predicts 3.8782 GHz for the
  pilot's bow-tie geometry, which *measured* 3.85 GHz (+0.7%), and flags
  +10.81% against that design's 3.5 GHz target. That is the Astuti failure —
  twenty hours and four solves on the pilot — caught in microseconds.

**What is NOT proven, and is the whole remaining risk:**

- **No LLM has ever written a `design.yaml`.** Every spec in the repo was
  hand-written or generated from a snapshot. The authoring step is untested.
- **No run has ever used Route A.** The compiler has never been driven by an
  agent in a real pilot.
- **No token saving has been measured.** Every claim about phase 2 saving
  tokens is currently an argument, not a number.

---

## 3. Why `swift-otter` measured nothing

It was meant to test (a) can an agent write a spec, and (b) does Route A save
tokens. It tested neither.

- `knowledge/cases/patch-2400/design.yaml` was supposed to be moved aside and
  was not — it is still in place, dated Aug 15. The ledger records
  *"construction shape = `design.yaml` (validated 2026-08-15 build)"*.
- **Nine of twelve staged scripts are byte-identical** to the 08-15 run
  (`workspaces/patch-2400/src` vs `workspaces/patch-2400-2/src`). Only
  `09_plots.py` and two template files differ.
- The ledger names `workspaces/patch-2400/` as *"Predecessor run (reference,
  not to be mutated)"* — the copying was deliberate, not accidental.
- There is **no `design.yaml` in the workspace**, so Route B was taken.

So the 64% token drop is "it had the answers to hand". Worse, the run never
produced `summary.md`, so by the skill's own Session-3 completion contract it
did not finish, and by the ticket-04 metric it delivered zero completed
simulations. The ledger's live-state block also still reads `banked = no` while
`results/state/solved.txt` exists — the ledger went stale at the end.

**One real finding survives:** the skill did not choose Route A even though
SKILL.md now presents it as the default. Given a workspace it could copy, it
copied. That is a fact about the routing language, and it is fixable.

---

## 4. The readout failure — diagnosed, with the fix already written

The solve itself is reliable: `Normal Completion`, 200 sweep points, banked.
Reading S11 back is what fails, on both recent runs. There are **two
independent faults**.

**Fault A — the reader is structurally broken, with no AEDT involved.**
`workspaces/patch-2400-2/src/09_plots.py:28` gates fill-state on
`getattr(sol, "data_real", None)`. Verified against the installed wheel:

| accessor | pyAEDT 1.3.0 |
|---|---|
| `data_real`, `data_imag` | **ABSENT** |
| `full_matrix_real_imag` | EXISTS |
| `get_expression_data` | EXISTS |
| `primary_sweep_values` | EXISTS |
| `export_data_to_csv` | EXISTS |

So the check reports `unfilled SolutionData` **even on a perfectly good fetch**.
Any success is discarded before it can be seen.

**Fault B — `get_solution_data` also genuinely raises.** Reproduced today on a
*copy* of the solved project, from a clean process (`workspaces/readout-probe-2/`):
`GetVariables` with no context, `GetSetups` with a sweep name — while
`existing_analysis_sweeps` on the same handle succeeds and returns the sweep
list. A partially functional gRPC channel, matching EC#3/EC#6.

This kills the obvious hypothesis: **the failure is not confined to the session
that solved.** It reproduces on a fresh attach.

**Not proven today:** I never obtained a successful read. My probe ran
non-graphical with other desktops alive, and the graphical retry did not finish
in the window. So "the readout works if called correctly" remains ticket 16's
claim from 08-07, not something re-confirmed on 08-16.

### The part that should drive the plan

Both faults were diagnosed on **2026-08-07** in
`workspaces/readout-route-around/summary.md` — the `data_real` false negative,
the working call shapes, and a one-line route-around for the
`HfssConstants.default_solution` client bug. That summary ends:

> Proposed entry text drafted in ticket 16 Comments ... File untouched.
> (ADR 0002 — approval required)

The fix has sat in a workspace summary and a ticket comment for nine days while
two pilots rediscovered the same failure from scratch. **This is the same
pattern the spec identified for the escaped-quote bug: the knowledge had
nowhere to live but one ticket's comment thread.** The ADR 0002 approval gate
is currently a place where validated findings go to die.

---

## 5. Open problems, ranked by expected value

1. **Land ticket 16.** Fix the fill-state check to use `get_expression_data` /
   `primary_sweep_values`, add the export-path fallback
   (`export_report_to_file`, `export_data_to_csv`), apply the route-around, and
   write the env-compat entry. Then re-probe properly — graphical, single
   desktop — to settle whether the call shape works at all today. This unblocks
   the one QA signal that has failed on every run.
2. **Fix the knowledge-landing path.** Ticket 16 is not an isolated miss; it is
   a structural one. Either ADR 0002's approval gate needs to be cheap and
   routine, or validated findings need to land as code and tests immediately
   with the playbook entry following. Decide which.
3. **Make Route A actually get chosen.** SKILL.md presents it as the default and
   the agent still copied a prior workspace. Options: forbid copying a
   predecessor workspace's scripts without an explicit ledger justification;
   make Route A the only documented route with Route B behind an escape-hatch
   note; or have Clarification emit a `design.yaml` as its named artifact so
   the route is structural rather than advisory.
4. **Protect the measurement.** Two of four runs are confounded — one by
   meta-work, one by a copyable predecessor. A pilot needs a case with no prior
   workspace, and a pre-flight that asserts it. Consider a `--pilot` mode that
   refuses to read sibling workspaces.
5. **Parts, not tokens, is the stuck axis.** 424 → 477 → 312, against a target
   of 60. Tokens can be argued down; 312 round-trips cannot. This is what
   ticket 14's orchestrator is for, and nothing else in the backlog addresses
   it.

---

## 6. Landmines for whoever plans next

- **Do not trust `swift-otter`'s 123,448.** §3.
- **`run_card.load_card` is `LIMIT 1`** and does not aggregate; subagent
  sessions are separate rows. Sum top-level sessions yourself and report
  subagent tokens separately. Snapshot the card immediately — `shiny-canyon`
  drifted from 1.58 M to 2.38 M after its card was taken.
- **Slugs repeat across projects and dates.** Filter by project worktree and
  break ties by recency.
- **Only the bow-tie has a reproduction target.** For every other case the
  strongest honest claim is "builds clean and the closed form agrees".
- **`coupled-filter-2400` has no spec** and needs even/odd-mode synthesis that
  does not exist. Do not fake it.
- **The skill is installed as a junction** into `skill/hfss-agent`. Whichever
  branch is checked out is what the agent runs. Everything is on `main` as of
  this writing; keep it that way.
- **`opencode.json` is pinned at `variant: max`** for a re-pilot. Revert to
  `low` afterwards.
- **Two AEDT desktops are alive** (25460 from 08-14, 25380 holding
  patch-2400-2). Both projects are banked; closing them is safe.
- **Two stray files at the repo root, both untracked, neither part of this
  project.** `package.json` is `@opencode-ai/desktop`. `README.md` is a
  byte-identical copy of `skill/hfss-agent/templates/workspace/README.md` that
  a pilot dropped in the wrong place on 08-15 — it opens "# Workspace template"
  and will be mistaken for the project README by anyone who reads it first.
  Both are safe to delete; they were left in place because they are the user's
  to remove.

---

## 7. What NOT to redo

- The compiler, schema, validator, reducer, acceptance diff and pre-check are
  built and tested. Read `hfss_spec/` before proposing anything there.
- Q1–Q8 are decided and the reasoning is in `phase-2-detail.md` §8–10. Do not
  reopen the external-CAD-kernel question; it was answered with evidence.
- The pilot retrospective's five cost centres (`.scratch/hfss-agent-perf-refactor/pilot-retrospective.md`)
  are scored in ticket 06's Comments. Four of five shrank; do not re-litigate.
- The horn's dimensions are synthesised and double-checked (closes on the
  requested gain, reproduces a textbook example). They are fine.

---

## 8. Pointers

| what | where |
|---|---|
| the architecture bet and its acceptance | `.scratch/hfss-agent-spec-driven/spec.md` |
| Q1–Q8 decisions and the worked design | `.scratch/hfss-agent-spec-driven/phase-2-detail.md` |
| per-ticket implementation records | `.scratch/hfss-agent-spec-driven/issues/` |
| pilot runbook (needs revising per §3) | `.scratch/hfss-agent-spec-driven/pilot-2-runbook.md` |
| the readout investigation and its unlanded fix | `workspaces/readout-route-around/summary.md` |
| today's readout probe | `workspaces/readout-probe-2/probe_readout.py` |
| the pilot that measured nothing | `workspaces/patch-2400-2/` |
| the run that is the fair baseline | `workspaces/patch-2400/` + ticket 06 Comments |
| environment quirks, authoritative | `knowledge/playbook/environment-compat.md` |
| the Design Spec route | `skill/hfss-agent/reference/design-spec.md` |
