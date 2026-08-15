# HFSS Agent run — performance & token-efficiency analysis

Measured from the opencode session database (the actual runs, not estimates):
`~/.local/share/opencode/opencode.db`. Dates 2026-08-02/03, project
`HFSS_automation`, model `accounts/fireworks/models/deepseek-v4-flash-0731`.

## 1. The numbers that matter

| Session | What it was | Input tok | Output tok | Cache-read tok | **Total billed-ish** | Wall time |
|---|---|---|---|---|---|---|
| `playful-river` | Bowtie @ 3.67 GHz (first full greenfield) | 1,100,785 | 251,977 | 39,168,744 | **1,352,762** | ~2.3 h |
| `silent-engine` | Bowtie @ 3.5 GHz (second attempt) | 329,760 | 68,370 | 9,186,701 | **398,130** | ~1.6 h |

The "430k" figure matches `silent-engine` (398k + overhead). Both runs together
are ~1.75 M tokens. The single biggest structural fact:

- 152 agent steps in `playful-river`, **no compaction** (`compact=False`).
- 39.2 M cache-read tokens ÷ 152 steps ≈ **260 k tokens of context re-read on
  every single step**. The conversation grew to ~500 k tokens and stayed there;
  every turn re-billed nearly the whole thing through the cache.

So the fight is not "the model is slow" — it is **context growth** feeding both
cost (input + cache reads) and time (processing a huge context every turn).
The model is already the cheap one ($0.14/$0.28 per 1M on Fireworks); switching
LLMs is the last lever, not the first.

## 2. What the tokens were spent on (conversation store, 1.97 MB / ~500 k tok)

| Store share | Content | Waste factor |
|---|---|---|
| ~695 KB (35%) | **Reasoning traces** — 109 parts; single parts of 78.9 KB, 42.5 KB, 34.9 KB, 32.6 KB, 29.4 KB, 24.1 KB… | The model streams long reasoning on *every* step, including trivial ones ("write: file"), and it stays in context forever. |
| ~350 KB | Tool outputs that persist: two `Get-ChildItem` KB/result listings of 89–90 KB each, a 43.9 KB grep result, paper-analysis notes of 85.8 + 106.7 KB, env-compat (24 KB), figures (PNGs 23 KB ×2) | Everything read once lives for all 152 steps. The 90 KB file listings alone sat in context for 20+ subsequent steps each. |
| — | 181 tool calls: 95 bash, 23 edit, 22 read, 20 write, 10 grep, 5 todowrite, 3 glob, 2 question, 1 skill | Many bash calls are *exploration* (listing KB folders to find filenames) that a static index would remove entirely. |

## 3. The timeline: where the hour+ went

From the part trace of `playful-river` (152 steps):

1. **Steps 1–30 (~20% of steps): KB spelunking by listing.** Repeated
   `Get-ChildItem "scraping\pyaedt_ai_context\<area>" -Recurse -Filter "*.md"`
   with `Where-Object Name -match …` to discover file names, plus greps. The KB
   is **8,412 files / 48 MB**. The agent was disciplined (only ~8 KB files read
   in full), but *finding* them took ~20 steps and produced huge listing outputs
   that stayed in context. (The 43.9 KB grep at step 14 was the "wave_port" API
   hunt; the 89 KB listing at step 11 was folder counts.)
2. **Steps 31–45: writing the 11 staged scripts.** One `write` per script +
   patches. This is legitimate work but high-token: every stage script is ~2–4 KB
   and they are written serially with full-context overhead per step.
3. **Steps 46–89: run + self-correction**. Three full **clean rebuild chains**
   (teardown → wipe project → rerun stages 01→04), each because the EC#8
   same-name-duplication trap invalidated the project, plus per-stage bash runs
   whose output (with `Select-String` filters) is still sizable. Each failed run
   triggers a reasoning dump of 16–26 KB *explaining* the fix.
4. **Steps 89–125 (~36 steps!): the review-gate + read-back-sync saga.** The user
   corrected geometry in the UI; ADR 0005 forced introspection → diff → amend →
   **verify in an isolated second desktop**. Two desktops + port-pin mistakes
   killed both desktops twice; a 78.9 KB reasoning block (step 97) reconstructs
   the geometry by reasoning; steps 102–123 re-verify twice. This block is
   wall-time-heavy because every introspection is a real AEDT attach (each adds
   6–25 s attach + python startup).
5. **Steps 126–152 (~27 steps): solve orchestration.** `analyze(blocking=False)`,
   then long **foreground PowerShell poll loops** (12 / 25 / 30 min windows) that
   hit the tool's 2-minute shell timeout and got killed; the agent then rebuilt
   the poll as `Start-Process`, then WMI-detached (`Invoke-CimMethod
   Win32_Process Create`), re-submitting 4 times (runs 1–4) — one of which
   double-solved because a solve was already in flight on the user's desktop
   (the 11:38 PM → 12:49 AM batch.log run = **71 min** of one stuck sweep, then
   a second launched on top). The final diagnosis (sweep "plateaus" at 11/201
   `.sd` points while adaptive completes) was in progress when the session
   ended. **The solve stage alone burned ~30 steps and ~1 h of wall clock.**

`silent-engine` (bowtie-3500) was materially better – it invented, ad hoc:
`results/state/*.txt` files (`objects.txt`, `boundaries.txt`, `sweeps.txt`,
`solve_started.txt`, `aedt_process_id.txt`, `aedt_port.txt`), port-pinned
attach, recursive `.sd` globbing, `cleanup_solution` before re-submit,
WMI-detached solve wrapper. **None of that is in the skill text yet.**

## 4. Root causes (ranked by blast radius)

1. **No context lifecycle.** One session, 152 steps, no compaction, no pruning,
   no stage-boundary summarization. This multiplies *every* other problem: a
   mid-run context of ~260 k tokens makes each of the 152 steps slow and every
   input token billed repeatedly through the cache.
2. **Long reasoning on a flash model with `variant: max`.** The per-step
   reasoning is the single largest store category and the reason message
   metadata shows `variant: max` (deepseek flash = thinking model). Reasoning
   isn't just tokens — on Fireworks it delays time-to-first-token on *every*
   step. Most of those 146 reasoning parts were trivial steps.
3. **Solving controlled interactively.** Because the skill says "poll with short
   status checks", the agent wrote increasingly long bash poll loops, hit the
   tool timeout, and then spent 5+ steps engineering process detachment. The
   solve must be fire-and-forget: detached OS process + tiny state files +
   short reads. The 3500 run proved the state-file pattern works.
4. **EC#8 violated → repeated full rebuild chains.** Same-name objects
   duplicate silently on dirty projects; the only escape the agent found was
   wipe-and-rerun. Each chain costs multiple AEDT launches (6–25 s each) + run
   outputs. The skill needs *idempotent stage scripts* (delete-then-create per
   object) so re-runs never invalidate.
5. **KB discovery by brute force.** ~20 steps of listing folders to find API
   doc filenames. A generated topic→file index (or a search sub-agent) removes
   them and the giant listing outputs.
6. **Verification ceremony duplicated in the main context.** The second-desktop
   verify chain (steps 99–124) is exactly the kind of self-contained work a
   sub-agent should own: parallel-safe, memory-free, and it *moved* (the agent
   correctly copied the workspace to a temp dir), but every step of it ran in
   the main context.

## 5. Opportunity map (ordered by return on effort)

### P0-1. Run the solve as a detached watchdog, not a foreground poll
Codify exactly what `silent-engine` invented:

- `08_solve.py`: cleanup, `analyze(setup=…, blocking=False)`, write
  `results/state/solve_started.txt`, exit.
- A separate small `poll_solve.py` launched once with `Start-Process` (or WMI),
  writing `results/state/solve_progress.txt` every 20 s from **recursive**
  `*.sd`/`.asol` discovery; exits when done.
- The agent then only does short `Read` calls to the state file (or delegates
  the whole watch to a background sub-agent — see P0-3).

This removes ~20 steps and ~1 h of wall time on a healthy solve, and kills the
tool-timeout WMI battle permanently. Verified working pattern already exists in
`workspaces/bowtie-3500/`.

### P0-2. Thinking budget / variant down for the main loop
Try `variant: low` (cycle via the `variant_cycle` keybind, or pin per mode/agent;
custom variants can set `reasoningEffort`/budget via provider model options in
`opencode.json`). Keep the `max` variant only for the rare true-diagnosis steps
(geometry sync, sweep-plateau investigations). Expect: −30–50 % output tokens,
faster first token on every step, and ~35 % less stored conversation (the
reasoning parts disappear from context).

### P0-3. One background sub-agent = solve watchdog + result QA
`task(type=general, background=true)`-style delegation is the perfect shape for
the solve phase: a cheap-model sub-agent receives the workspace path + QA
signals, polls the state file, and returns a single completion message
(+"unreadable — flaky readout" where applicable). The main agent **goes idle
cheap or drafts plots/summary scripts** meanwhile instead of re-reading a
260 k-token context every 20 s.

### P0-4. Stage-boundary state file = the anti-compaction
The skill already has a "session state lives in the AEDT project" doctrine;
extend it to conversation state: after each stage, append
`workspaces/<name>/state.md` (what exists, variables, ports, sweep name,
pitfalls hit). Then the running conversation can be split / resumed per stage in
a *fresh session* that reads only `state.md` + the offending staged script —
context drops from ~260 k to ~10 k. (opencode: start a new session per stage or
use the checkpoint/handoff skills; manual  stage-break point = the review gate.)

### P0-5. Turn on compaction + pruning (`opencode.json`)
```jsonc
{
  "compaction": { "auto": true, "prune": true, "reserved": 10000 }
}
```
`prune` removes old tool outputs (the persistent 90 KB listings / grep blobs)
when compacting. Free insurance even before any other change.

### P1-1. Sub-agents with *cheaper* models for the memory-free work
Define project agents in `opencode.json` (mode `subagent`, own `model`,
`steps`, `permission`) and have the skill route:
- **`kb-lookup`** (read-only): query → terse "use X with args" snippets from the
  KB (it may glob/grep freely; its results are summarized by itself).
- **`paper-digest`**: the analyze-papers step (already a sub-agent today, but
  run it for 106 KB paper notes that currently land in the main context).
- **`stage-script-writer`**: given the locked Recipe + parameters *(after
  Clarification)* returns all staged scripts as one message; main context only
  sees the scripts.
- **`verify-copy`**: the isolated second-desktop reproduce check (P0-3's poll
  equivalent for sync).

Cheap-model candidates on the same Fireworks key (models.dev, reasoning=No,
tool-calling=Yes): `accounts/fireworks/models/llama-v3p2-3b-instruct` /
`llama-v3p2-1b-instruct` (≈$0.02/$0.06), `accounts/fireworks/models/mistral-7b-instruct-v3`(-class), and
`accounts/fireworks/models/qwen3-4b`(class). Sub-agent quality matters most for
`kb-lookup` (verbatim API work) and least for `paper-digest`. Benchmark with one
project: if the cheapest tier produces wrong API signatures, step up one tier —
still ~5–10 × cheaper per sub-agent token than the main loop. The main loop
stays `deepseek-v4-flash` — it is already the cheap-and-competent option;
**do not move the main loop to a weaker model**.

### P1-2. Idempotent stage scripts (kill the rebuild chains)
Change the per-stage convention: every geometry/material/boundary/mesh/setup
object is deleted if present before recreate (or built with a `delete_` sweep
up front). Then a failed stage is re-run in-place — no wipe, no relaunch chain.
This turns EC#8 from a trap into a non-event and removes the 3 rebuild cycles
seen in the trace.

### P1-3. KB topic index
One-time script over `scraping/pyaedt_ai_context/` emitting
`knowledge/playbook/kb-index.md`: task-word → `file.md` mappings (e.g.
`sweep → setup_and_mesh/…SetupHFSS.create_linear_count_sweep.md`). The skill
then reads one index file instead of ~20 listing/grep steps. Also add the index-
generator to the scraper so KB top-ups regenerate it (tickets 03/08/09 pattern).

### P2. Smaller / later
- **Recipe sweep size policy**: 201-point discrete sweep is what plateaued/felt
  glacial; smoke use was 101 points. Recipe guidance "one point per ~2 MHz"
  instead of fixed 201 — halves sweep wall time at negligible fidelity cost for
  wideband checks. (Design judgement, not a token win — flag for the playbook.)
- **Verify once, not twice**: the sync-verify chain reran because of teardown
  port bugs; a single pinned-port teardown helper (already in the 3500
  `ws_common`) plus "verify uses its own `Desktop(port=…)`" text removes the
  duplicate.
- **Save the session where it died**: `state.md` (P0-4) doubles as a
  resume-point so a killed session doesn't redo Clarification + script writing
  (`silent-engine` effectively re-did the pre-solve work).

## 6. KB retrieval — specifically the API lookups behind script generation

The doc above only sketched this (P1-1/P1-3). Measured detail: script
generation consumed steps 10–29 of `playful-river` (~20 steps) — not reading
(only ~8 KB files were read in full) but *discovering filenames* and filter
noise. Two structural facts, verified just now:

- **48% of the KB is duplicate stubs.** Of 8,411 files, **4,035 are
  `.rst.md` stubs** (~0.9 MB of 48 MB — each is a ~280 B sphinx re-export of
  the real `.md` twin). Every folder listing and every grep hits 2× the
  files; a grep can and did match the stub instead of the rich twin. Fixes:
  (a) regenerate/scrape clean and delete `*.rst.md` at source; (b) until then,
  a one-line rule in the skill: *"KB files ending `.rst.md` are stubs — never
  read or grep them; always prefer the plain `.md` twin."*
- **ripgrep is not installed** on this box, so the agent's `rg -l` calls
  failed and it fell back to `Get-ChildItem piped through Where-Object`, which
  over 8 k files is slow and returns names at best. `rg -l wave_port` returns
  *only filenames* (tiny, exact outputs the model can act on directly) and is
  ~100× faster than the PowerShell pipeline. Installing ripgrep
  (`winget install BurntSushi.ripgrep.MSVC`) is a two-minute change that
  removes the slowest, noisiest part of discovery. Teach the skill to use it
  instead of `Get-ChildItem`+`Where-Object` listings.

Beyond tooling, the highest-leverage retrieval idea is to **collapse discovery
to one distilled file per purpose**. A greenfield build uses a closed set of
~30–40 pyAEDT calls (`Hfss`, `Modeler3D.create_box/create_polyline/unite/
subtract`, `mat.update`, `wave_port`, `assign_radiation_boundary_to_objects`,
`create_setup`, `create_linear_count_sweep`, `validate_simple`, `analyze`,
`create_report`, `get_solution_data`, …). The KB is organized per API symbol;
the Spine is organized per stage — and never the two shall meet without a
synthesis layer:

1. **`knowledge/playbook/spine-api.md` — the distilled reference (top pick).**
   Generated from the KB at scrape time (same ceremony as KB top-ups, tickets
   03/08/09): for each call in the spine set, keep *signature line + one-line
   semantics + env-compat gotcha link*. ~6–10 KB total. Script generation then
   reads exactly one small file; per-file KB reads happen only for
   off-recipe calls. This replaces most of the 20 discovery steps *and* the
   ~8 scattered reads with one read that stays in context cheaply from step
   10 onward.
2. **Per-stage API cards** — the even smaller variant: one card per Spine
   stage listing that stage's 3–8 verified calls (wave-port card inline with
   EC#7/#8). A stage-authoring step reads exactly one card (~1–2 KB). This
   overlaps environment-compat, so fold it in there rather than a new file.
3. **`kb-lookup` sub-agent (cheap model, read-only)** — instead of the main
   loop touching the KB at all, the sub-agent answers "give me the exact
   `wave_port` call for a solid-face port, signature + args, quoting the KB
   file" and returns a single terse snippet, whose only cost in the main
   context is the snippet itself. Quality control matters here: instruct it
   to return the *exact* signature or explicitly "not found — known KB gap",
   never to paraphrase from memory, and spot-check its answers on the first
   two runs before trusting it. Works best on top of (1)/(2), not instead of.
4. **Guardrail for the 1 M context**: never bulk-read the KB ("preload the
   docs") — 48 MB / 4,376 real files would overflow or, worse, sit in every
   later step's context. Retrieval stays needle-aimed; the top-down
   distillation (1) is the mapping layer that makes that possible cheaply.

Also worth noting for later versions: a generated `usages.json`/`facts` file
(signature + example per spine call) doubles as a machine-checkable artifact —
the `verify_skill.py`-style verifier can diff it against KB changes and fail
loudly when a top-up renamed a method.

## 7. State-of-the-art survey (2026) and what it says for us

Surveyed: Anthropic's *Claude Code best practices* (the current
context-management playbook for agentic loops), LMSYS *RouteLLM* (cost-based
model routing), and the opencode docs themselves. Each technique below is
mapped to a concrete refactor item; "lore" rows mark established practice
I could not re-verify online today (those URLs have moved), flagged as such.

| SOTA technique (source) | What it is | HFSS-agent application | Expected effect |
|---|---|---|---|
| **Verification-first loops** — give the agent a check it can run, not descriptions (Claude Code best practices, current) | Every loop closes on a runnable pass/fail signal; agent stops when check passes | Each staged script already prints `STAGE` lines; upgrade to a single machine-parseable `PASS:` line with assertions (objects exist, bbox in range, `validate_simple()==True`). Self-correction then reads one line, not re-filtered logs | Removes failed-run ambiguity; turns the 36-step sync saga into ≤3 steps |
| **Subagents for investigation; fresh-context review** (Claude Code) | Reviewers run in fresh contexts so they grade the artifact, not the reasoning that built it | The read-back-sync verification (owns the diff: scripts vs live model) runs as a subagent that sees only `state.md` + the sync target + live introspect output | Slashes the biggest single step-block (steps 89–125) out of the main context |
| **Spec, then fresh session to execute** (Claude Code) | Write a self-contained spec; execute it in a clean session | The Clarification block is already this spec. Formalize the boundary: after Clarification approval, a *new session* executes stages reading only `state.md`; at the Review gate a new session continues | Each session's context stays 10–30 k instead of 260 k; kills cross-stage drift |
| **Aggressive context hygiene** — `/clear` between unrelated tasks, `/compact <instructions>` with preservation directives, summarize-from-checkpoint (Claude Code) | Compaction is a skill, name it and direct it | Do this at stage boundaries instead of letting auto-compaction decide. Skill text: "at each stage end, `/compact Keep the Recipe, variable table, and state.md path; drop tool outputs" | Predictable context ceiling; compaction preserves what matters (variables/port names) |
| **Model routing** — RouteLLM (LMSYS, 2024): prefer cheap model where quality holds; 85 % cost cuts at 95 % quality | Learned/static routers split queries by difficulty | A hand-written routing table (no learned router needed): cheap tier → paper digest, KB filename discovery, summary drafting, QA table assembly; flash tier → script authoring, sync diffs, solve diagnosis. Encode as "stage → agent" text in SKILL.md | ~30–50 % of sub-agent-heavy stages at 5–10 × cheaper per token |
| **Deterministic gates via hooks** (Claude Code) | Scripts run at fixed lifecycle points, guarantee the action | opencode has no hooks here, so emulate: a single pre-run `py_compile`+import-lint of all staged scripts before any AEDT launch — a 2-second static gate that catches syntax/name errors at ~0 cost (replacing AEDT-launch-per-typo runs) | Cuts the failed-run cycles whose minimum cost is one 6–25 s launch + heavy logs |
| **CLI tools for context-efficient interaction** (Claude Code) | Prefer tools whose output is exactly the answer (e.g. `gh`) | ripgrep (noisy discovery → filenames), plus the section-6 `kb` finder and a `probe.py` introspection CLI so attach/introspect never re-plumbs inline python | Removes the biggest persistent output blobs (90 KB listings) |
| **Session naming / resume** (Claude Code) | Conversation persistence without re-explaining | Name per-stage sessions (`bowtie-3670-gate`, …); kills the re-do pattern that doubled work in `silent-engine` | No re-run of Clarification/script writing; resume from state.md |
| **Parallel sessions / agent teams** (Claude Code) | Fan out independent work | Only LLM-side work parallelizes here (AEDT is single-desktop, licensed): paper digest ∥ KB lookup ∥ script drafting in the pre-build window; solve-poll overlaps plot-script prep | Removes ~10 serial steps from the critical path |
| **Prompt-prefix/KV-cache discipline** (lore: OpenAI/Anthropic caching guides; not re-verified today) | Cached prefixes are cheap to read but not free of latency | Fireworks cache reads are ~5 × cheaper than fresh input, *but the 39.2 M cache reads still cost wall time* — so caching is not the answer; shrinking the context is. Keep the skill text/SYSTEM prefix byte-stable so what remains cached is the small part | Briefly: don't lean on caching; lean on section 5 P0-4/P0-5 |
| **Tool-output truncation policies** (lore: agent-harness reviews; not re-verified) | Cap/roll up verbose outputs | Give bash a `tail -50` habit and forbid full recursive listings; state drift files replace listings (silent-engine's `results/state/*.txt` is this) | Removes 20–90 KB outputs from conversation store |
| **Verbosity/effort caps** (OpenAI-style `textVerbosity`, `reasoningEffort`; opencode passes provider options through) | Bounded thinking and prose per step | Variant `low` on the main loop (P0-2) + skill line "final messages ≤ 250 words; no essays" | Output tokens −30–50 % on a prose-happy flash model |
| **Compaction config** (opencode docs, current) | `compaction.auto` + `prune` drop old tool outputs | Already P0-5; the SOTA note is to *also set `reserved` and treat compaction as a designed event at stage boundaries*, not a safety net | Free, measurable |
| **One more opencode-native lever, verified in this repo**: the **bash tool accepts an explicit `timeout`** (default 120 s) | The 120 s tool timeout killed the foreground polls, which caused the whole WMI-detach saga (steps 141–147) | Skill text: poll loops must pass a large explicit timeout (e.g. `timeout=1_800_000`) *or* use the detached watchdog + state files. Without this line, the P0-1 fix leaks back in | Removes 5+ rewrite steps and the double-solve incident class |

### Synthesis: what the refactor should adopt vs skip

**Adopt now (cheap, high-certainty):** verification-line contract, py_compile gate,
explicit bash timeouts, verbosity caps, session-per-stage with named sessions,
compaction-as-event, `prune: true`.
**Adopt with one pilot run (measure first):** subagent routing table (cheap tier),
fresh-context sync reviewer, per-stage sessions split at gates.
**Skip in this refactor:** learned routers (RouteLLM-class) — the step taxonomy is
stable and hand-encoded routing is free; token distillation into fine-tuned
models; speculative/JIT execution — the provider already does DSpark speculative
decoding on the deployed flash model.

## 8. What will NOT speed up (checked)

- **Faster model for the main loop**: current model is already $0.14/$0.28;
  the bottleneck is context size × steps, which a faster model pays for anyway.
  Revisit only after P0s.
- **Parallel AEDT jobs**: license (flexlm feature `hfss_gui` via VPN) + single
  desktop + DLL-holds-GIL mean solves/attaches cannot parallelize. The
  parallelism win is LLM-side (sub-agents), not solver-side.
- **KB deletion**: cutting the KB shrinks nothing the agent actually reads; the
  win is the index (P1-3), not the corpus.

## 9. Expected outcome

On `silent-engine`-class runs (~400 k tokens / ~1.6 h), the P0 set alone
(targeting the 152-step context growth, reasoning volume, and ~30 solve steps)
points at roughly **2–3 × fewer tokens and ~2–3 × less wall time** (solver
physics time excluded, which is untouchable). Adding P1 sub-agent routing and
idempotent scripts pushes toward **4–6 ×** on the modeling side of a run.
Orchestrate as: config + P0-1/2/4/5 first (zero script changes, one run to
measure), then skill text changes (P0-3, P1-1/2/3), then re-measure with the
query below.

## 10. Re-measuring (the same numbers, later)

```sql
-- per session, for project HFSS_automation
SELECT s.slug, s.time_created, s.time_updated,
       s.tokens_input, s.tokens_output, s.tokens_cache_read,
       s.tokens_input + s.tokens_output AS billed,
       (SELECT count(*) FROM part p WHERE p.session_id = s.id) AS parts,
       (SELECT sum(length(data)) FROM part p2 WHERE p2.session_id = s.id) AS storesize
FROM session s
WHERE s.project_id = (SELECT id FROM project WHERE worktree LIKE '%HFSS_automation%')
ORDER BY s.time_created;
```

Every optimization below either cuts `storesize` (less in context), `parts`
(fewer steps), or wall time between `time_created`/`time_updated`.

## 11. Files changed / created for this analysis

- This report: `docs/hfss-agent-performance-analysis.md`
- Working scripts (temp, outside repo): `C:\Users\afpim\AppData\Local\Temp\opencode\*_probe.py`,
  `sessions_probe.py`, `parts*.py`, `trace*.py`
- Evidence base: opencode DB at `~/.local/share/opencode/opencode.db`,
  `workspaces/bowtie-*` state files, `batch.log` timings.
