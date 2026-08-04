# 08 — Subagent model configurability (one swap point)

**What to build:** make the subagents' model assignment changeable in ONE place, so the tier can be re-pointed (e.g. to genuinely cheaper models after the pilot validates the contracts, or to a bigger model if `kb-lookup` proves wrong) without editing agent definitions.

Decision context (2026-08-04, supersedes part of grilling Q11): the subagents were originally planned on cheap-tier Fireworks models (~$0.02–0.06/M); the measured cost model shows the dollar delta of that tiering is ~$0.03–0.06 per refactor — negligible. So **both subagents (`kb-lookup`, `runcard`) now run the same `accounts/fireworks/models/deepseek-v4-flash-0731` at `variant: low` as the main loop**, removing a correctness unknown. Ticket 08 ensures the cheaper tier remains a one-line option later.

Implementation: prefer opencode config's env substitution — `"model": "{env:HFSS_SUBAGENT_MODEL}"` on both agents, with the flash ID as the documented default. If env substitution cannot carry the model+variant pair cleanly (verify with `opencode debug config`), fall back to a single provider model alias under `provider.fireworks-ai.models.<alias>` carrying the `variant: low` options, with both agents referencing `fireworks-ai/<alias>` — same property: change the alias's backing model, both agents follow. Document the knob (comment in `opencode.json` + a note in the repo README). The agents' quality contracts are model-incidental: `kb-lookup` must quote-the-KB-or-say-NOT-FOUND, `runcard` caps drafts at ~250 words — the prompts, not the model, carry the behavior.

**Status:** ready-for-human
**Blocked by:** 02 (the config file this lands in; implemented together with 02 in one session). File ownership was `opencode.json` + this ticket only.

- [x] Both subagents' `model` resolve through one swap point (env var or single alias)
- [x] Documented default is `accounts/fireworks/models/deepseek-v4-flash-0731 @ variant low`; downgrade path (swap point → cheap model) described in the config comment
- [x] `opencode debug config` shows both agents resolving and the variant options present
- [~] README note added (recommended) — SKIPPED: repo has no README and parallel-run ownership (agent-prompts.md) restricts file sets; knob fully documented in `opencode.json` leading comment + this ticket. Revisit at integration if a README lands.
- [x] Ticket Comments updated

## Comments

- 2026-08-04: Created per user direction — the tiering cost delta (~$0.03–0.06) doesn't justify a second unknown model; the swap point keeps the option open after the pilot. Spec Implementation Decision 7, ticket 02, and `agent-prompts.md` prompt 02 were updated to match.
- 2026-08-04: **DONE — alias swap point implemented and verified in `opencode.json`** (implemented jointly with ticket 02).
  - **Env substitution rejected after verification.** `"model": "{env:HFSS_SUBAGENT_MODEL}"` resolves to the flash id when the var is set, but with the var unset (the default state for every future session) `opencode debug config` silently shows `model: ""` for both agents — no warning, startup still "succeeds". That fails the "carries the model+variant pair cleanly" bar; record kept in ticket 02.
  - **Chosen: single provider alias.** `provider.fireworks-ai.models."hfss-subagent"` → `id: accounts/fireworks/models/deepseek-v4-flash-0731`, `variants: {low: {reasoningEffort: low}}`. Both `kb-lookup` and `runcard` set `model: fireworks-ai/hfss-subagent` + `variant: low`. Verified: `opencode models fireworks-ai --verbose` lists `fireworks-ai/hfss-subagent` with `api.id = accounts/fireworks/models/deepseek-v4-flash-0731`, inherited cost ($0.14/$0.28) and 1M limit, and the `low`/`high`/`max` variant map; `opencode debug config` shows both agents resolving through the alias with `variant: low`.
  - **Downgrade path documented** in a leading `//` comment in `opencode.json`: re-point the alias `id` (e.g. `accounts/fireworks/models/gpt-oss-20b`) and adjust the `variants` map; both agents follow with zero edits to agent definitions.
  - README note skipped per parallel-run ownership (no README.md exists at root; see checklist).
