# Re-pilot runbook — the spec-driven path, measured

Status: ready-for-human
Feature: hfss-agent-spec-driven
Written 2026-08-15, the night before.

This is the run that decides whether phase 2 paid. Everything built so far is
proven *correct* — the compiler reproduces the pilot's model exactly — and
entirely **unmeasured**: no one has run a greenfield job through the spec path
and counted the tokens.

## The number

| run | billed | parts | wall | outcome |
|---|---|---|---|---|
| `silent-engine` baseline | 398,130 | 424 | ~1.6 h | completed |
| `shiny-canyon` pilot | 1,579,333 | 1,392 | 25 h | abandoned |
| `kind-rocket` (patch-2400, free-form) | 346,993 | 477 | 0.69 h | completed |
| **this run** | ? | ? | ? | ? |
| spec's phase-2 threshold | **≤80,000** | **≤60** | — | completed |

`kind-rocket` is the number to beat, and it is the fair comparison: same box,
same skill, same harness, a clean run with no flailing. The 4.3x gap between it
and the threshold is exactly what the compiler is supposed to close — a run
that writes one document instead of ten scripts should not need 477 parts.

**Do not expect ≤80,000 on the first attempt.** A useful result is anything
that shows the shape of the remaining cost. If it lands at 150k the bet is
working and the residue is worth chasing; if it lands near 340k the compiler
saved nothing measurable and the cost is somewhere neither of us has looked.

## Decide these three before starting

1. **Case.** `patch-2400` is the strongest choice: it is the only structure
   with a *directly comparable* free-form run (`kind-rocket`, 346,993 / 477),
   so the delta is attributable to the route rather than to case difficulty. It
   also already has a spec, which is a confound — see "the honest variant"
   below. `microstrip-50r` is the cheapest but has no comparable prior run.
2. **Whether the agent writes the spec, or uses the existing one.**
   - *Realistic*: the agent writes `design.yaml` from scratch during
     Clarification. This measures the real workflow, and it is the only version
     that tests whether an LLM can produce a valid spec.
   - *Optimistic*: the agent starts from `knowledge/cases/patch-2400/design.yaml`.
     This measures the compiler alone and will look far better than the tool
     actually is. If you run this variant, label the number as such.
   **Recommend the realistic one**, and delete/ignore the existing spec for the
   duration so it cannot be copied.
3. **Model tier.** `agent.build.variant` is back at `low`. Ticket 06 ran at
   `max` and the effort change was inconclusive against a moved case and prompt
   shape. Holding it at `low` keeps this run comparable to `kind-rocket`, which
   was `max` — so if you want a clean comparison, set it to `max` again. My
   recommendation: **`max`, to match `kind-rocket` exactly**, so the route is
   the only variable that moved.

## Pre-flight

```
git checkout main                        # phase 2 is merged; see below
python scripts/install_skill.py --check  # PASS: install_skill targets=2 failed=0
python scripts/tier0.py                  # PASS: tier0 suites=10 failed=0
opencode debug config                    # confirm agent.build.variant
```

Then: VPN up, AEDT 2024 R1 free, and **close the patch-2400 desktop** if it is
still running (pid 25460 as of tonight — it holds the solved patch project and
is already banked, so closing it is safe).

## Launch

Start opencode **from the repo directory** — `run_card.py` filters sessions by
project worktree. Give a plain user-shaped request with **no mention of
tickets, measurement, specs or performance**; the point is to see which route
the skill chooses on its own. The patch request that worked last time is in
`.scratch/hfss-agent-spec-driven/issues/06-main-loop-model-experiment.md`.

If the agent picks Route B (staged scripts) when Route A would have worked,
**that is a finding, not an operator error** — it means SKILL.md's routing
language is not strong enough. Record it and let the run continue.

## Watch for

- **Did it use Route A at all?** The single most important observation.
- **Escape-hatch count.** `compile_spec` reports it. Non-zero on a patch means
  the schema is wrong somewhere.
- **How many validator round-trips** before the spec passed. This is the new
  self-correction loop, and it should be cheap — but nobody has measured an LLM
  writing one of these.
- **Whether the pre-check fired** and what the user did with it.
- **Parts spent before the first AEDT launch.** Under Route A this should be
  small; the offline gates are ~1 s each.

## Record afterwards

```
python scripts/run_card.py --slug <slug> --summary workspaces/<name>/summary.md \
    --verdict --outcome <completed|escalated|abandoned>
```

Sum all top-level sessions for the run and report subagent tokens separately —
`load_card` is `LIMIT 1` and does not aggregate. Snapshot it immediately; a
session that stays open keeps accumulating (`shiny-canyon` drifted from 1.58 M
to 2.38 M after its card was taken).

Then file the comparison in ticket 17/18 and, if the number is good, in the
spec's phase-2 acceptance section.

## Known gaps going in — none of these are bugs to fix first

- **No orchestrator (ticket 14).** The three LLM seams are still a human-driven
  conversation, not a state machine. This run measures the spec path under the
  *existing* ceremony.
- **`coupled-filter-2400` has no spec**; its coupled sections need even/odd-mode
  synthesis that is not implemented.
- **Read-back sync is a snapshot diff, not a spec diff** (ticket 12 proper).
  The recipe in `reference/design-spec.md` works and deletes the eight-minute
  replay, but it compares snapshots rather than specs.
- **Only the bow-tie has a reproduction target.** For any other case the
  strongest claim is "builds clean and the closed form agrees".
