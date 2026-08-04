# 02 — opencode config: compaction, agents, variant

**What to build:** `opencode.json` (project root) with: (a) `compaction: {auto: true, prune: true, reserved: 10000}`; (b) two new subagents — `kb-lookup` (mode subagent; permissions read/glob/grep/list/bash(read-only-style) allowed, edit/write denied; contract: return exact KB signatures or "not found", never from memory) and `runcard` (mode subagent; drafts summary.md + run card from state.md + results for the main loop to revise; workspace-scoped); (c) main model `accounts/fireworks/models/deepseek-v4-flash-0731` pinned with `variant: low` via provider model options — verify variants exist with `opencode models`; if `low` is unsupported for this model, record it in the ticket and keep current behavior (output caps in ticket 03 still apply).

**Subagent models (decision 2026-08-04, supersedes the original cheap-tier plan):** both subagents use the SAME `accounts/fireworks/models/deepseek-v4-flash-0731` at `variant: low` — measured dollar delta of a cheaper tier is ~$0.03–0.06 per refactor (see ticket 08). The subagent `model` fields MUST resolve through one swap point (env substitution `{env:HFSS_SUBAGENT_MODEL}` preferred, else a single provider alias) per ticket 08 — do not hardcode per-agent if avoidable.

**Status:** ready-for-human
**Blocked by:** none

- [x] `compaction` block present and verified (`opencode debug config`)
- [x] `kb-lookup` agent defined, read-only, model through the ticket-08 swap point
- [x] `runcard` agent defined, workspace-scoped, model through the ticket-08 swap point
- [x] Main model pinned; `variant: low` applied OR recorded-unavailable with evidence
- [x] Subagent model resolution (env/alias) works per ticket 08; evidence recorded

## Comments

- 2026-08-04: Tiering split locked in the grilling session (two subagents, no more, for the pilot; script authoring / sync-diff / solve diagnosis stay in the main loop).
- 2026-08-04: Subagent tier changed to the same deepseek-v4-flash at `variant: low` (cheap-tier delta ~$0.03–0.06 deemed not worth a second unknown model); swappability contract moved to ticket 08.
- 2026-08-04: **DONE — `opencode.json` written and verified** (this ticket + ticket 08 implemented jointly in one session; no other files touched).
  - **Compaction** `{auto: true, prune: true, reserved: 10000}` — present in `opencode debug config` output.
  - **Main model** pinned `fireworks-ai/accounts/fireworks/models/deepseek-v4-flash-0731`; **`variant: low` APPLIED** via `agent.build.variant` (no top-level `variant` field exists in the config schema). Availability evidence: `opencode models fireworks-ai --verbose --refresh` (v1.18.11, registry refresh 2026-08-04) shows the 0731 model `status: active` with `variants: {low: {reasoningEffort: low}, high: {…}, max: {…}}`; the un-suffixed `deepseek-v4-flash` exposes only `{high, max}` (i.e. no `low`) — which explains the baseline runs hoisting to `max`. `debug config` shows `"build": {"variant": "low"}` loaded.
  - **Swap point used: provider alias, not env** (ticket 08's fallback, chosen because verified). `{env:HFSS_SUBAGENT_MODEL}` DOES interpolate (resolves to the flash id when set), but when the var is unset `opencode debug config` shows `model: ""` **silently** — a footgun for every future session that doesn't export it. The alias instead always resolves: `provider.fireworks-ai.models.hfss-subagent` → `id: accounts/fireworks/models/deepseek-v4-flash-0731` + `variants.low.reasoningEffort: low`; both agents reference `fireworks-ai/hfss-subagent` with `variant: low`. `opencode models fireworks-ai --verbose` lists `fireworks-ai/hfss-subagent` as a first-class model with `api.id = accounts/fireworks/models/deepseek-v4-flash-0731`, inherited cost/limit, and the variant map. Swap point documented in a leading comment in `opencode.json`.
  - **kb-lookup**: `mode: subagent`, model via swap point, permission `{read/glob/grep/list: allow, edit: deny, bash: ask (search-only per ticket), task: deny}`; exact KB-signature-or-`NOT FOUND` prompt as specified.
  - **runcard**: `mode: subagent`, model via swap point, permission `{read/glob/grep/list: allow, edit: {"*": deny, "workspaces/**": allow}, bash: deny, task: deny}` (workspace-scoped: can only write under `workspaces/`); ≤250-word draft prompt as specified.
  - Setup note: `opencode` CLI is not on PATH on this box (desktop-app install); verification ran the v1.18.11 CLI from a temp npm install against the same `~/.local/share/opencode` data dir. Restart opencode to load the new config.
