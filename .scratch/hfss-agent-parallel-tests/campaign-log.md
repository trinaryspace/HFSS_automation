# Campaign log — parallel test campaign

One file, appended as the campaign runs. Cell-level detail goes in `cells/<ID>.md`;
this is the spine: what was true of the machine, and what each wave concluded.

Runbook: `../hfss-agent-spec-driven/campaign-runbook.md`
Design:  `../hfss-agent-spec-driven/parallel-test-campaign.md`

---

## Fixed conditions

| | value | recorded |
|---|---|---|
| campaign start | | |
| base commit | | |
| **skill commit (frozen)** | `2d47289` — teach the skill the Design Spec route | 2026-08-16 |
| `install_skill --check` | `PASS: install_skill targets=2 failed=0` | 2026-08-16 |
| `agent.build.variant` at start | `max` (pinned for the re-pilot; revert to `low` after D3) | 2026-08-16 |
| tier0 baseline (main checkout) | `PASS: tier0 suites=10 failed=0 elapsed=229.3s` | 2026-08-16 |
| license seats (W0-2) | **pending** — needs VPN | |
| stale AEDT desktops cleared (W0-3) | **pending** — pids 25460, 25380 | |
| W0-5 attribution outcome | **pending** — see below | |
| Wave C scope (W0-10) | **pending** — 2 cells, or 4–5 with the Fault A fix landed | |

**The skill is frozen at the commit above.** Both install targets are junctions
into the main checkout, so every terminal in every worktree runs that one text.
Changing it starts a new batch and every cell before it is a different
experiment.

---

## W0-5 — attribution probe

The question: does opencode register a `project` row **per worktree**? If it
does, cells run from worktrees must be carded with `--worktree`.

Baseline measured 2026-08-16, before any worktree session existed:

```
matching project rows: 1
    52 sessions  C:/Users/afpim/Repos/HFSS_automation
```

`run_card.py` has since been patched (`IN`, not `=`) so several matching project
rows no longer collapse to one arbitrary row. The probe is therefore no longer
*blocking* — it is confirmation, and it tells you whether to pass `--worktree`
routinely.

**ANSWERED 2026-08-16.** A headless session (`opencode run --dir <worktree>`)
was started in `.claude/worktrees/probe-attrib`, session `stellar-wizard`:

```
project rows matching 'HFSS_automation': 1
     53 sessions  C:/Users/afpim/Repos/HFSS_automation
verdict: one project row - opencode resolves worktrees to the main project.
PASS: check_attribution project_rows=1
```

Session count 52 → 53 in the **main** project row. Carded clean:
`run_card.py --slug stellar-wizard` → 10,086 billed / 5 parts.

Verdict: ☑ **one row — `--slug` alone is sufficient**

Two consequences:
- Worktrees do **not** partition sessions. Slug is the only discriminator, so
  recording it per cell is mandatory and `--latest` is unusable with parallel
  cells (on top of ticket 06's D1 defect).
- The `IN`-not-`=` patch is defensive, not load-bearing — the failure it prevents
  cannot occur on this configuration. It stays because it is correct.

### Fixed overhead floor

`stellar-wizard`'s only instruction was "reply with one word, use no tools":
**10,086 billed / 5 parts.** That is what every cell pays to load `AGENTS.md` and
the skill before doing any work — 13% of the 80,000-token acceptance budget and
8% of the 60-part budget, spent before the first useful token.

---

## Noise floor (X0a vs X0b)

| | billed | parts | wall (raw) |
|---|---|---|---|
| X0a | | | |
| X0b | | | |
| spread | | | |

**If the billed spread exceeds ~25%, every single-cell delta in this campaign is
noise** and the rollup must say so rather than rank cells.

---

## Wave log

| date | wave | cells launched | notes |
|---|---|---|---|
| 2026-08-18 | **B (first cell)** | `S7SIM` - the 2x2 corporate-feed array, `TASK-verify-2x2-feed.md` | **The first hardware run of the campaign.** Workspace `workspaces/patch-array-5800`, slug `hidden-falcon`. Candidate C1-generalized chosen. Three solves banked Normal Completion (`#1a` flat-PEC elements 2 adaptive passes; `#1b` 1-oz-copper elements 10 passes 150 pts; `#2` fed array 14 passes 150 pts). Feed **not** falsified as a defect: no -9..-10 dB in-band signature. Resonance **5.6 GHz in BOTH designs**, dip ~7 dB. User verdict: "not outright failure, its just a tuning issue that can be corrected with a human hand." Stage-1 Z_act extraction parked (readout, below). Broadside gain and element balance never read - still outstanding. |

Two findings from that cell outlive the cell and are filed separately:

- **The first non-circular check of `hfss_spec/physics.py`.** `precheck`
  predicted 5.8000 GHz offline for the locked element dimensions; the solver put
  both designs at 5.6 GHz. That is a **+3.57%** estimator error (repo
  `delta_pct` convention, solve as target; -3.45% with the prediction as
  denominator) measured against a solve rather than against the module itself -
  the thing section 8 of `RECOMMENDATIONS.md` says the campaign did not have.
  n=1, attribution open. Written up in `estimator-calibration.md`.
- **Six learning-loop proposals, none applied**, queued for one-pass approval in
  `knowledge/playbook/pending-amendments.md` per ADR 0002. One of them (2c, the
  readout claim) is held back as probably wrong; the experiment that settles it
  is `TASK-readout-channel-vs-systematic.md`.

---

## Machine-state incidents

Anything that could confound a wall-clock or readout number: concurrent solves,
orphan desktops, other repos' test suites running, VPN drops, license denials.
Record it here the moment it happens; it is unrecoverable afterwards.

| date | what | which cells affected |
|---|---|---|
| 2026-08-16 | another repo (`datasheet_analyzer`) running pytest suites in its own worktrees during planning | none — planning only, no cells live |
| 2026-08-18 | **gRPC channel degraded mid-session, twice.** `GetVariables` + `Subtract` failed on the long-lived channel during the build; cured by recycling the desktop. Later `create_report` (`GetVariables`) and `get_solution_data` (`GetPropValue`) both failed at readout on the replacement channel and were **not** cured, because the retry reattached by pinned port to the same process. Confounds every scripted readout number from this cell; the QA signals that exist were read from the UI. | S7SIM |
| 2026-08-18 | **Two `ws_common.DESIGN` misroutes** - the fed spec compiled over `ElementsOnly` once, and a second misroute on the same constant. Both recovered idempotently, nothing lost, but they cost two rebuilds of wall time on the cell that was being timed. | S7SIM |
| 2026-08-31 | **The S7SIM desktop is still running - 13 days.** pid 25840, port 57850, started 2026-08-18 18:51:56, verified alive by `Get-Process` on 2026-08-31; holds the banked project and a licence seat. It is the only `ansysedt.exe` on the box (the W0-3 pids 25460 / 25380 are gone). **Deliberately not killed**: it is arm 1 of `TASK-readout-channel-vs-systematic.md` and the last place the run's two outstanding UI reads can be taken. Any cell launched before that task runs will contend with it for a seat. | any future cell; S7SIM's outstanding reads |
