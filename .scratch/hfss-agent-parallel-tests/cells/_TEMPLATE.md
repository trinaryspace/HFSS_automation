# Cell <ID> — <structure> — wave <A|B|C|D>

## Identity
- terminal / worktree / branch:
- base commit:
- skill/hfss-agent commit (shared across all worktrees):
- model variant (`agent.build.variant`, as resolved by `opencode debug config`):
- pinned port (B/C only):
- prompt given (verbatim):

## Hygiene — paste the `pilot_preflight.py` block verbatim
```
(python scripts/pilot_preflight.py --cell <ID> [--expect-missing <case>])
```
- clean-roomed? (`git rm -r -q workspaces`): yes / no — if no, why
- spec moved aside? which:

## Pre-registration — written BEFORE launch
- predicted route (A/B) and confidence:
- predicted escape hatches (count + which ops):
- predicted precheck verdict (recipe covered? consistent?):
- predicted parts / billed:
- what would surprise me:

## Observed — authoring
- route taken + **the reason it gave**:
- validator round-trips: <n>  (list each error path)
- precheck: verdict / delta / recipe named
  - precheck-blind structure? did it notice the absent estimator? yes / no
- escape hatches: <n>  (op + stated reason for each)
- dimensions produced without naming a relation:
- KB / `spine-api.md` lookups:

## Observed — build (Wave B)
- dry-run op count:
- live build PASS / FAIL:
- face-selector ambiguities:
- stage retries:
- snapshot path:

## Observed — solve (Wave C)
- watchdog terminal line:
- banked (`solved.txt`)?:
- readout route: scripted / UI-arbitrated / unreadable
- QA signals reported:

## Cost — snapshot immediately at cell end
- slugs (every one, incl. subagents):
- billed, main loop:
- billed, subagents:
- parts:
- wall (**raw only** — active wall is unmeasurable, ticket 06 D2):
- outcome: completed | escalated | abandoned
- cost per completed simulation:

## Verdicts
- **Gates passed?** validate / precheck / compile --dry-run: y / n
- **Human correctness verdict:** correct | subtly wrong | grossly wrong
  - if wrong: what exactly, and **would any automated gate have caught it?**
- **False green?** (gates passed AND human says wrong): yes / no
- **Failure-layer tag:** authoring | schema | physics-gate | compiler | pyaedt |
  readout | ceremony | harness | none
- one sentence: what this cell taught that no other cell would have
