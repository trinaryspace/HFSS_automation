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
| | | | |

---

## Machine-state incidents

Anything that could confound a wall-clock or readout number: concurrent solves,
orphan desktops, other repos' test suites running, VPN drops, license denials.
Record it here the moment it happens; it is unrecoverable afterwards.

| date | what | which cells affected |
|---|---|---|
| 2026-08-16 | another repo (`datasheet_analyzer`) running pytest suites in its own worktrees during planning | none — planning only, no cells live |
