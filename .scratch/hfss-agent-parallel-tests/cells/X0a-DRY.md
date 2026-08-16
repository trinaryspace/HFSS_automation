# Cell X0a-DRY — patch-2400 control — wave A — **harness validation, not a valid measurement**

Run 2026-08-16 to answer one question: does the hfss-agent skill work headless?
It does. It also invalidated itself as a measurement, for a reason worth more
than the cell cost.

## Identity
- worktree / branch: `.claude/worktrees/cell-X0a` / `cell/X0a` (from `campaign/base-nopatch`, **old version** — design.yaml only)
- session: `nimble-lagoon` (`ses_ff3bd328effe06SzF21uXutoQO`)
- model / variant: `accounts/fireworks/models/deepseek-v4-flash-0731`, `--variant max`
- mode: headless, `--auto`, `--format json`
- skill commit: `2d47289`

## Prompt (turn 1, verbatim)
> I need a rectangular microstrip patch antenna that resonates at 2.4 GHz on
> 1.6 mm FR4. Inset microstrip feed, 50 ohm, single element. I care about the
> resonance landing within about 5% and I want to see S11. Let's lock the design
> down first - don't open AEDT yet, I want to review the numbers before anything
> gets built.

Turn 2 (me, as operator): confirmed the numbers, accepted er 4.4, asked for the
sweep widened to 1.9-3.0 GHz, asked for the ledger, repeated "don't open AEDT".

## What happened — the mechanism works

1. `skill(hfss-agent)` loaded as the **first** tool call. The skill is reachable
   headless through the `~/.agents/skills` junction from a worktree.
2. It followed the Read-first protocol: ADRs, `CONTEXT.md`, playbook,
   `precheck.py`, `hfss_spec/physics.py`, three canonical `design.yaml` files.
3. It ran the closed-form relations itself in `python -c`, four times.
4. It wrote `workspaces/patch-2400/design.yaml` (3,597 bytes) — **the first
   `design.yaml` ever authored by an LLM in this repo.**
5. It ended turn 1 **cleanly at the Clarification confirmation gate**, exit 0:
   *"Confirm the numbers ... and I'll write the State ledger and proceed to
   build."* It did not stall, hang, or self-confirm.
6. Resumed with `--session`, it accepted the correction, widened the sweep, and
   wrote `state.md`. **It never launched AEDT** — process count stayed at the two
   pre-existing stale desktops throughout.

Gates on the authored spec:

```
PASS: validate_spec errors=0 warnings=1      (sweep margin; cleared to 0 after turn 2)
PASS: precheck recipe=inset-fed-rectangular-patch verdict=consistent
      target 2.4000 GHz | closed-form 2.4000 GHz | delta -0.00% | tolerance 5%
```

## Why this is not a valid measurement

The clean-room removed `knowledge/cases/patch-2400/design.yaml` and nothing else.
The agent then read **`patch-2400/notes.md` and `patch-2400/case.json`**, which
carry `key_dimensions`: patch_width_mm 38.0100, ereff 4.0857, fringing dL 0.7388,
patch_length_mm 29.4216 — plus the Balanis derivation in prose.

Its own summary says the port choice *"matches case.json's lumped_port + Modal"*.

So `delta -0.00%` is **not evidence that an LLM can derive a patch**. It is
evidence that it can transcribe four numbers from an adjacent file. The gates
passed on a spec whose provenance was the answer key.

This is the swift-otter failure in miniature, caught for the price of one cell
instead of a campaign: *the thing you moved aside was not the only copy.*

**Fix applied:** `campaign/base-nopatch` and `base-nohorn` now remove the entire
case directory, and `pilot_preflight.py --expect-missing` fails if the directory
merely exists.

## Cost — the finding that should reshape the acceptance target

| stage | billed | parts | wall |
|---|---|---|---|
| fixed overhead (`stellar-wizard`, one word, no tools) | 10,086 | 5 | — |
| **turn 1: Clarification + design.yaml** | **79,401** | **106** | 5 min 43 s |
| cumulative after turn 2 (+ledger) | 84,691 | 130 | 9 min 51 s |
| phase-2 acceptance threshold, **whole run** | ≤80,000 | ≤60 | — |

**Clarification alone consumed 99.3% of the token budget and 177% of the parts
budget** — before any build, any solve, any plot. Turn 2 added only ~5,290 billed
and 24 parts, so the cost is concentrated in the first turn's reading protocol,
not in the conversation.

That reframes the phase-2 target. The gap is not build-stage overhead, and it is
not solve-orchestration churn — `kind-rocket` already showed those shrinking. It
is the **cost of arriving at the first design decision**. Ticket 15 (token
discipline) and ticket 14 (orchestrator) both point here; nothing else in the
backlog does.

## Minor observations
- `state.md` is 2,947 bytes against the skill's own ≤2 KB cap — 47% over, though
  much better than `kind-rocket`'s 6,940.
- It ran `git status --short && git branch --show-current` as its 5th call. The
  neutral `wip` commit messages on cell branches are load-bearing, not paranoia.
- It surfaced the validator's sweep-margin warning to the user and offered a fix
  rather than silently proceeding. Good behaviour; worth preserving.

## Verdicts
- Gates passed: **yes** (validate, precheck)
- Human correctness verdict: **not scored** — contaminated provenance
- False green: **not applicable**, but note the shape: gates green, provenance
  worthless. This is exactly the failure the false-green rate exists to catch,
  and the automated gates did not catch it. Only reading the transcript did.
- Failure-layer tag: **`harness`**
- What this cell taught: the headless mechanism works end to end, including
  operator resume — and moving a spec aside does not blind a cell.
