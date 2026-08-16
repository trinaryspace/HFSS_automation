# Parallel test campaign — how to learn the most from N terminals

Status: ready-for-human
Feature: hfss-agent-spec-driven
Written 2026-08-16, against `state-of-the-tool-2026-08-16.md`.
Audience: the operator (you) driving several opencode terminals, plus whoever
plans improvements afterwards.

This is a **measurement plan, not a build plan**. Nothing here proposes a fix.
Its whole job is to produce evidence sharp enough that the improvement plan
writes itself — every cell ends with a *failure-layer tag*, and the improvement
backlog is those tags sorted by frequency and cost.

---

## 0. The one-paragraph answer

The tool's untested surface is **offline**. Authoring a `design.yaml` needs no
license, no desktop, no readout, and runs its gates in about a second — and no
LLM has ever done it. So the campaign front-loads everything into a wide,
cheap, fully parallel **authoring wave** that you can start today at full
terminal width with zero hardware contention and zero pending fixes. Hardware
comes second and narrow (2–3 concurrent, port-pinned, build-only). Solving comes
last and **strictly serial**, because concurrent solves destroy the wall-clock
metric and concurrent desktops are the documented cause of the readout probe
failing. Structures are chosen not because they are interesting antennas but
because each one probes a specific, named unknown.

---

## 1. What we do not know, ranked by value of knowing

Straight from the state doc's §2 "not proven" list, plus two the doc implies but
does not name.

| # | Unknown | Cost to test | Why it dominates |
|---|---|---|---|
| **U1** | Can an LLM write a valid `design.yaml` at all? | ~free, offline, parallel | Route A is the entire phase-2 bet and its first step has never been executed once. |
| **U2** | Can an LLM write a **correct** `design.yaml`? | free + human review | Validation ≠ correctness. A spec can pass `validate_spec`, pass `precheck`, compile clean, and still be the wrong antenna. This is the tool's worst failure mode and it has **no measurement at all**. |
| **U3** | Does the skill actually *choose* Route A? | free, offline | Evidence so far says no — given a workspace it could copy, it copied (§3). One observation, uncontrolled. |
| **U4** | Where does schema v1 break on structures nobody hand-wrote? | free offline, cheap on hardware | Every existing spec was written by a human who knew the schema. Escape-hatch rate on novel structures is the v2 requirements document. |
| **U5** | Does Route A save tokens/parts? | expensive, needs clean pairs | Currently an argument, not a number — and both prior attempts to get the number were confounded. |
| **U6** | Does the readout work today? | serial, hardware, blocked | Two independent faults diagnosed 08-07, unlanded. See §7. |

**U2 is the headline.** Everything else has at least one data point; U2 has zero,
and it is the only failure that produces a *confident wrong answer* rather than
an error message. The campaign is designed around measuring it.

The number this campaign should produce that nobody has: the **false-green
rate** — of specs that pass every automated gate, what fraction does a competent
human judge to be the wrong antenna?

---

## 2. Six rules that make parallel runs interpretable

Break any of these and you get another `swift-otter`: tokens burned, nothing
learned. Multiplied by N terminals.

**R1 — One git worktree per terminal.** Non-negotiable, and not for tidiness:
`run_card.py` filters sessions **by project worktree**, slugs repeat, and
`load_card` is `LIMIT 1`. Two terminals in one checkout means you cannot
attribute tokens to a run afterwards. The worktree is the unit of attribution.

**R2 — Hygiene is asserted, not assumed.** `swift-otter` failed because
`knowledge/cases/patch-2400/design.yaml` "was supposed to be moved aside and was
not". Every cell begins by *printing* the state of the things that could
contaminate it, and that printout is pasted into the cell record. If it wasn't
printed, it didn't happen.

**R3 — The agent never sees the harness.** The prompt is a plain engineering
request in a customer's voice. No mention of tickets, routes, specs, tokens,
measurement, or this document. The moment you tell it "use Route A" you have
destroyed U3 and biased U1. The cell record is operator-side, kept outside the
agent's context.

**R4 — Pre-register before you launch.** Write your predictions (route, escape
hatches, precheck verdict, rough parts) into the cell record *before* the first
message. Unregistered tests get rationalised into successes; this costs 60
seconds and is the difference between learning and confirming.

**R5 — Vary one thing per pair.** A cell on its own tells you about that
structure. A *pair* differing in exactly one condition tells you about the tool.
Budget at least a third of your terminals for paired cells (§6, Wave D).

**R6 — Snapshot the run card at cell end, immediately.** `shiny-canyon` drifted
1.58 M → 2.38 M after its card was taken. Sum top-level sessions yourself; report
subagent tokens on a separate line.

---

## 3. Contention map — what may actually run at once

This is the part that decides the schedule. Sources: env-compat #1/#2/#4/#5/#6/#9/#10,
`reference/execution.md` port-pinning, state doc §4 and §6.

| Activity | Needs | Safe concurrency | Why |
|---|---|---|---|
| `validate_spec`, `precheck`, `compile_spec --dry-run` | nothing | **unlimited** | Pure offline, ~1 s each, no license, no desktop. |
| `tier0.py` (full runner) | nothing | unlimited, but **don't** | Offline, but **not ~1 s** — measured 2026-08-16 at >4 min in a fresh worktree, dominated by `scraping/verify_kb.py` walking the freshly-checked-out KB corpus. The "~1 s / 79 tests" figure in the state doc is the `hfss_spec` suite, which is one of tier0's nine. Run tier0 **once per campaign branch in Wave 0**, not once per cell — it validates the branch, and every worktree is the same branch. |
| Authoring conversation (Clarification → `design.yaml`) | nothing | **unlimited** | Same. This is where the untested surface lives. |
| `compile_spec --launch` / `tier1.py` (build, never solves) | VPN + license + a desktop | **2–3** | Multiple desktops coexist (EC#2) *if* each is port-pinned and graphical. `tier1.py` refuses any stage ≥08, so it cannot burn solver time by accident. |
| Solve (`08_solve` + watchdog) | license + cores | **1** | Concurrent solves split cores and make wall time meaningless — and wall time is a metric. Also unknown license-seat depth. |
| Readout / `get_solution_data` | a live desktop | **1, and no other desktop alive** | The 08-16 probe "ran non-graphical with other desktops alive" and that is the leading explanation for its failure. Diagnosing a flaky readout under concurrency is diagnosing nothing. |

**Blocking unknown before any Wave B width decision: how many license seats do
you have?** Probe it once, record the answer in the campaign log:

```
# adjust the path to your Ansys licensing utils
& "C:\Program Files\ANSYS Inc\Shared Files\Licensing\winx64\lmutil.exe" `
    lmstat -a -c 1055@LICENSE-ANSYS.ENGIN.UMICH.EDU
```

If it reports one seat, Wave B is serial too and the whole hardware half of this
campaign is a queue — which is fine, because Wave A is where the learning is.

### 3a. What a worktree does *not* isolate — measured 2026-08-16

R1 asks for a worktree per terminal. Before relying on it, two things about this
repo, both verified today by running tier0 in a fresh worktree off `main`:

**The Tier 0 corpus is gitignored, so a fresh worktree fails tier0.**

```
main checkout:   PASS: hfss_spec tests=79 failed=0     PASS: install_skill targets=2 failed=0
fresh worktree:  FAIL: hfss_spec tests=79 failed=11    FAIL: tier0 suites=10 failed=2 (skill-install, design-spec)
```

All 11 failures trace to one missing file:
`workspaces/bowtie-3500-pilot/results/state/model_snapshot.json`. `.gitignore`
excludes `workspaces/*/results/`, so the snapshot corpus the design-spec tests
read exists **only in the main checkout**. Nothing is broken on `main` — the code
is fine — but the offline suite is not portable to a worktree.

Consequences for the campaign:
- Run `tier0` **in the main checkout, in Wave 0**, and not again. (Independently
  the right call: 293 s.)
- If a cell ever needs the offline suite inside its worktree, copy the corpus
  first: `cp -r <main>/workspaces/bowtie-3500-pilot/results <worktree>/workspaces/bowtie-3500-pilot/`.
- Worth a ticket regardless: a test corpus that only exists in one checkout is
  the same class of problem as knowledge that only exists in one ticket comment.

**The skill is shared across every worktree.** `install_skill.py --check` reports
both targets linked to `skill/hfss-agent` — resolved against the **main
checkout**. So every terminal, in every worktree, runs the *same* skill text,
while its `scripts/`, `hfss_spec/` and `knowledge/` come from its own worktree.

- Good: skill text is automatically identical across cells. One less variable.
- Dangerous: **editing the skill mid-campaign silently changes every in-flight
  terminal**, and a worktree on a different branch would run that branch's
  compiler against main's skill.
- Therefore: **freeze `skill/hfss-agent` and the campaign branch for the
  duration.** If you must change the skill, that starts a new campaign batch and
  every cell before it is a different experiment. Record the skill commit in each
  cell record.

**Port assignment.** Terminal *k* owns port `5006k` (50061, 50062, …) for any
desktop it launches, recorded in its workspace `results/state/aedt_port.txt`.
Never let two terminals share a port, and leave `50051` to whatever the user's
own desktop is doing. Teardown is port-pinned; a terminal kills only its own.

**Before Wave B starts:** close the two stale desktops (pids 25460 / 25380 as of
08-16 — both projects banked, closing is safe). A campaign that starts with
orphan desktops alive inherits the exact confound that broke the readout probe.

---

## 4. The structure menu

Chosen so each structure probes a named unknown. Two facts drive the selections,
both verified in the tree today:

- **The compiler's op dispatch has no array/duplicate op.** `hfss_spec/compiler.py`
  handles `box, sheet, cylinder, polyline, unite, subtract, intersect,
  sweep_along_vector, sweep_along_path, sweep_around_axis, connect,
  thicken_sheet, import_cad, escape_hatch`. Any repeated element must be
  enumerated by hand or escape. That is the single largest suspected v1 gap and
  two structures below attack it from different sides.
- **The pre-check covers exactly five recipes** (`knowledge/playbook/precheck-tolerances.json`):
  `inset-fed-rectangular-patch`, `bow-tie-patch`, `microstrip-line`,
  `parallel-coupled-line-filter`, `pyramidal-horn`. Everything else gets *no
  estimator* and the physics gate is silent. **Precheck-blind structures are
  where the false-green rate will be highest**, so the menu deliberately spans
  both sides of that line.

Legend — **PC**: precheck covered ✓ / blind ✗. **GT**: hand-written ground-truth
spec exists to score against.

### Control

| id | structure | ops | PC | GT | probes |
|---|---|---|---|---|---|
| **X0** | `patch-2400` as-is, 2.4 GHz FR4 patch | box, sheet, lumped_port | ✓ | ✓ | Nothing about antennas — this is the **noise floor**. Run it in two terminals with an identical prompt. Without the spread between those two, no token/parts delta anywhere else in the campaign is interpretable. |

### Group 1 — in-schema, precheck-covered (isolates *authoring* skill)

| id | structure | ops | PC | GT | probes |
|---|---|---|---|---|---|
| **S1** | Inset-fed rectangular patch, **5.8 GHz**, Rogers RO4350B (εr 3.48, h 0.762 mm) | box, sheet, subtract, lumped_port, radiation | ✓ | ✗ | New band + new substrate on a covered recipe. Does it compute the inset depth from transmission-line theory or guess a fraction? Closed form will catch a wrong resonance. |
| **S2** | 50 Ω microstrip line with a **quarter-wave transformer** to 100 Ω @ 3.5 GHz | sheet, box, wave_port | ✓ | partial | Expression algebra under load: λg/4 needs εeff, which needs W/h. Tests whether parametrics stay symbolic (`trace_W + 12*h`) or collapse to numbers. |
| **S3** | **Blind rebuild of `horn-10ghz`** — canonical `design.yaml` moved aside | connect, box, wave_port | ✓ | ✓ | The only **objective authoring score** available: diff the LLM's spec against a known-correct hand-written one. Also re-exercises the `connect` loft. |

### Group 2 — in-schema, precheck-**blind** (isolates *knowing what it doesn't know*)

| id | structure | ops | PC | GT | probes |
|---|---|---|---|---|---|
| **S4** | Half-wave **dipole**, 2.45 GHz, free space, lumped gap port | cylinder ×2, sheet, lumped_port, radiation | ✗ | ✗ | No substrate, no ground — a boundary topology unlike every existing case. No estimator registered: does the agent *say so*? Cheapest possible solve, so it is also the best Wave C candidate. |
| **S5** | Quarter-wave **monopole** on a finite circular ground, 1.575 GHz | cylinder ×2, port, radiation | ✗ | ✗ | Coax-style feed and a finite ground plane. Second read on precheck-blindness. |
| **S6** | **Circular patch**, 2.4 GHz, FR4 | cylinder, sheet, lumped_port | ✗ | ✗ | **Trap cell.** There is no circular-patch estimator. If the agent labels `recipe: inset-fed-rectangular-patch` to get a green pre-check, that is a manufactured false green and one of the most damaging behaviours the tool could have. Watch the `recipe:` field specifically. |

### Group 3 — schema-stressing (writes the v2 requirements)

| id | structure | ops | PC | GT | probes |
|---|---|---|---|---|---|
| **S7** | **2×2 patch array**, corporate microstrip feed, 5.8 GHz | many sheets/boxes, unite, ports | ✗ | ✗ | The array gap head-on. Enumerate four elements plus a feed network, or reach for `escape_hatch`? Do the four elements stay parametrically linked, or drift into four independent literal-ish blocks? **Highest-information schema cell in the menu.** |
| **S8** | **SIW / via-fenced** guide section, 10 GHz | cylinder ×N, box, wave_port | ✗ | ✗ | Same gap, different shape — rows of vias. Confirms whether "no array op" is one problem or two. |
| **S9** | **Vivaldi** (exponentially tapered slot), 6–12 GHz | polyline (Spline/Arc), subtract, thicken_sheet | ✗ | ✗ | The polyline/spline path, exercised by nothing so far. Exponential taper is expression stress. Wideband sweep. |
| **S10** | **U-slot dual-band patch**, 2.4 / 5.8 GHz | subtract with narrow slots | ✗ | ✗ | The **mesh gap**: v1 is `adaptive_only` by construction (Q4), and a narrow slot is exactly where explicit refinement is needed. Expect a plausible, under-meshed, confidently-wrong result. Does the agent flag meshing as a limitation, or not mention it? |

### Group 4 — must-fail-honestly (cheap, high information)

| id | structure | ops | PC | GT | probes |
|---|---|---|---|---|---|
| **S11** | Parallel-**coupled-line bandpass filter**, 2.4 GHz | — | ✓(feed only) | ✗ | Known-unsupported: the coupled sections need even/odd-mode synthesis that does not exist, and the state doc says *do not fake it*. **Correct outcome is a refusal or a scoped partial with the gap named.** A confident full build is a failure — and a green pre-check here is meaningless by the tolerances file's own note. |
| **S12** | "I need a 20 dBi antenna for 28 GHz." Nothing else. | — | — | — | Deliberately underspecified. Correct outcome is Clarification doing its job: band, substrate, polarisation, feed, size envelope. The Clarification block has never been scored by any measurement. |

---

## 5. The wave schedule

### Wave 0 — operator-side, before anything (≈30 min, no terminals)

Not a test. The things that make the tests interpretable.

1. Probe license seats (§3) and record it.
2. Close the two stale AEDT desktops.
3. `python scripts/install_skill.py --check` and `python scripts/tier0.py` — both
   PASS, on the branch every terminal will run. Budget several minutes for tier0
   (§3) and run it **once**. (The skill is a **junction** into `skill/hfss-agent`;
   whichever branch is checked out is what every terminal runs. Keep the campaign
   on one branch.)
   - Note the machine is already shared: at the time of writing, another repo's
     test suites were running concurrently in their own worktrees. Wave A does
     not care, but Wave B/C wall-clock numbers do — check the box is quiet before
     any cell whose wall time you intend to report.
4. Confirm `opencode.json` `agent.build.variant` — it is pinned at `max` for the
   re-pilot. Wave A's D3 pair deliberately varies this, so know its start state.
5. Create the shared results directory **in the main checkout** (not in a
   worktree — worktrees get deleted):
   `.scratch/hfss-agent-parallel-tests/cells/`.
6. **Freeze the skill and the branch** (§3a) and record the commit of
   `skill/hfss-agent` at the top of the campaign log. Every terminal runs that
   one skill regardless of its worktree; changing it mid-campaign invalidates
   the comparison between cells run before and after.

**Decide now whether Wave C happens at all this round.** Waves A, B and D need
no fixes and can start today. Wave C is close to pointless until the readout
fault is landed — see §7.

### Wave A — authoring (all terminals, offline, ~1–3 h per cell)

Every terminal, fully parallel, **no AEDT**. The agent takes a plain request and
stops after `compile_spec --dry-run`. Explicitly: *do not let it launch a
desktop* — this wave's value is that it is uncontaminated by hardware flakiness.

Batch A-1 (6 terminals): **X0a, X0b, S1, S3, S4, S7**
— noise floor ×2, one covered-recipe new build, one ground-truth blind rebuild,
one precheck-blind, one schema-stressor.

Batch A-2 (6 terminals): **S6, S11, S12, S9, S10, S2**
— the trap, the must-refuse, the underspecified, and three schema stressors.

This ordering is deliberate: batch A-1 answers U1/U2 and gives you the noise
floor; if U1 fails outright (an LLM cannot produce a valid spec), batch A-2's
composition should change before you spend it.

### Wave B — build on hardware (2–3 terminals, build-only, never solves)

Promote only specs that **passed the offline gates *and* a 60-second human
sanity read**. Use `tier1.py --workspace …` (structurally incapable of solving)
or `compile_spec --launch` followed by `capture_state.py`.

Per terminal: its own worktree, its own pinned port, graphical desktop, and
nothing else running that touches AEDT.

Candidates in priority order: **S7** (does the array survive contact with the
modeler), **S1**, **S4**, **S9**, **S3**. Stop at four unless something surprises.

The Review gate needs you. Let terminals **queue at the gate** rather than
interrupt you one at a time, then do one gate sweep across all of them — you
review better in a batch, and the wall-clock cost is charged once.

### Wave C — solve + readout (strictly one at a time)

Two cells, no more. **S4 (dipole)** first: no substrate, small mesh, fastest path
to a real S11 and the cheapest possible test of the readout. Then **S1 (patch)**,
which is directly comparable in shape to `patch-2400`/`kind-rocket`.

During a Wave C cell: exactly one AEDT desktop alive on the whole machine. Every
other terminal is offline (Wave A/D work) or idle.

### Wave D — controlled pairs (interleave with A; offline, cheap)

These are the cells that produce *causal* statements. Each is the same structure,
same prompt, one condition changed.

| id | condition A | condition B | answers |
|---|---|---|---|
| **D1** | fresh worktree, `workspaces/` empty | a sibling workspace for a similar structure left in place | **U3, controlled.** Does it copy a predecessor when one exists? The §3 finding is currently a single uncontrolled observation. |
| **D2** | `knowledge/cases/<x>/design.yaml` present | moved aside | Does it start from the canonical spec, and does it *say* it did? Also quantifies how much the "optimistic variant" flatters the numbers. |
| **D3** | `agent.build.variant: max` | `variant: low` | **The biggest untested cost lever.** Authoring is offline and cheap, so run this 3× per side on the same structure (use X0 or S1). If `low` authors specs as well as `max`, that is a large, real saving that nobody has measured. |

D3 is the best return on terminal-time in the campaign after U1/U2 — six cheap
offline cells for a decision that touches every future run.

---

## 6. The cell protocol

Identical for every cell. The whole protocol is operator-side except the prompt.

### Before launch — pre-registration and hygiene

Create `.scratch/hfss-agent-parallel-tests/cells/<cell-id>.md` from the template
in §8, fill in **Pre-registration**, then:

```
# 1. fresh worktree off the campaign branch, one per terminal
git worktree add ../wt-<cell-id> -b cell/<cell-id> main

# 2. hygiene — PRINT the state, do not assume it (R2)
cd ../wt-<cell-id>
ls workspaces/                          # expect: empty, or note exactly what is there
ls knowledge/cases/*/design.yaml        # expect: the intended set for this cell
git log --oneline -1                    # the exact base commit
python scripts/validate_cases.py        # fast; the canonical specs still load
```

Do **not** run the full `tier0.py` per cell — it is minutes, not seconds (§3),
and it tests the branch, which is identical across every worktree. Once in
Wave 0 is enough; per cell you want the base commit recorded and the fast gates.

Paste that output verbatim into the cell record. For an authoring cell whose
structure has a canonical spec (X0, S3, D2-B), move it aside **and show that you
did**.

Wave 0 item worth building once: a `scripts/pilot_preflight.py` that asserts
exactly these four things and exits non-zero otherwise, printing a block you
paste in. It is ~30 lines and it is precisely the check whose absence cost the
last pilot its validity. The shell above is the manual equivalent — start with it
rather than waiting for the script.

### Launch

Start opencode **from the worktree root** (`run_card.py` filters by worktree).
Give a plain, customer-shaped request. Example shape for S1:

> I need an inset-fed rectangular patch antenna resonating at 5.8 GHz on Rogers
> RO4350B, 0.762 mm thick. Single element, microstrip feed, 50 Ω. Simulate it and
> show me S11.

No mention of routes, specs, tickets, tokens, or this plan (R3). For Wave A
cells, the only addition permitted is a scope bound in the user's own voice:
*"Just get me to the point where the design is fully specified and checked — don't
open AEDT yet."*

### During

Watch, do not steer. Note the moments, don't correct them. Specifically:

- Which route it announced, and **the reason it gave**.
- Every `validate_spec` failure and what the error path was.
- The `precheck` verdict — and for a precheck-blind structure, whether it
  *noticed* there was no estimator.
- Any `escape_hatch` and its stated `reason:`.
- Parts spent before the first AEDT launch (Wave B/C cells).
- Anywhere it guessed a dimension without stating the relation it used.

If it picks the "wrong" route or refuses, **that is data, not operator error**.
Let it run.

### After

```
python scripts/run_card.py --slug <slug> --outcome <completed|escalated|abandoned> \
    --escape-hatch <n> [--summary workspaces/<name>/summary.md] --verdict
```

Snapshot immediately (R6). Sum top-level sessions; report subagent tokens on
their own line. Then fill the rest of the cell record — including, for U2, the
**human correctness verdict**, which no script can produce.

---

## 7. On the readout, and why Wave C is last

Two independent faults, both diagnosed **2026-08-07**, neither landed:

- **Fault A** — the fill-state check gates on `getattr(sol, "data_real", None)`,
  and `data_real` does not exist on pyAEDT 1.3.0. A perfectly good fetch is
  discarded as "unfilled". Purely a code fault; no AEDT needed to see it.
- **Fault B** — `get_solution_data` also genuinely raises, reproducibly, on a
  *fresh attach to a copy* of a solved project. Not confined to the solving
  session.

Note a numbering discrepancy in the state doc worth fixing before anyone chases
it: §4/§5 say "ticket 16", but `issues/16-parametric-sweep.md` is the parametric
sweep. The readout work lives in **`issues/13-typed-spine-tool-surface.md`**,
whose checklist explicitly includes wiring in the readout findings and committing
the `readout-route-around` workspace. Point people at 13.

Consequence for this campaign: **a Wave C cell cannot produce a trustworthy
in-band-resonance signal today.** It can still produce a solve, a banked result,
a wall-clock number and a UI-arbitrated S11 read by you off the plot — which is
what the skill's own contract says is authoritative anyway. That is worth two
cells and not more. If you would rather land the Fault A fix first (it is a
one-line predicate change plus an export-path fallback), Wave C becomes worth
four or five cells instead of two.

Either way, Waves A, B and D are unaffected. Start them now.

---

## 8. Cell record template

Copy to `.scratch/hfss-agent-parallel-tests/cells/<cell-id>.md`.

```markdown
# Cell <id> — <structure> — wave <A|B|C|D>

## Identity
- terminal / worktree / branch:
- base commit:
- skill/hfss-agent commit (shared across all worktrees — §3a):
- model variant (agent.build.variant):
- pinned port (B/C only):
- prompt given (verbatim):

## Hygiene (pasted output, R2)
- ls workspaces/:
- ls knowledge/cases/*/design.yaml:
- tier0:
- canonical spec moved aside? (which file, where to):

## Pre-registration (written BEFORE launch, R4)
- predicted route (A/B) and confidence:
- predicted escape hatches (count + which ops):
- predicted precheck verdict (covered? consistent?):
- predicted parts / billed:
- what would surprise me:

## Observed — authoring
- route taken + the reason it gave:
- validator round-trips: <n>   (list each error path)
- precheck: verdict / delta / recipe named
  - precheck-blind structure? did it notice the absent estimator? yes/no
- escape hatches: <n>  (op + stated reason for each)
- dimensions it guessed without naming a relation:
- KB / spine-api lookups:

## Observed — build (Wave B)
- dry-run op count:
- live build PASS/FAIL:
- face-selector ambiguities:
- stage retries:
- snapshot captured? path:

## Observed — solve (Wave C)
- watchdog terminal line:
- banked (solved.txt)? :
- readout route: scripted / UI-arbitrated / unreadable
- QA signals reported:

## Cost (snapshot immediately, R6)
- billed, main loop:
- billed, subagents:
- parts:
- wall (active):
- outcome: completed | escalated | abandoned
- cost per completed simulation:

## Verdicts
- **Gates passed?** validate / precheck / compile-dry-run: y/n
- **Human correctness verdict (U2):** correct | subtly wrong | grossly wrong
  - if wrong: what exactly is wrong, and would any automated gate have caught it?
- **False green?** (gates passed AND human says wrong): yes/no
- **Failure layer tag** (see §9), or `none`:
- one sentence: what this cell taught that no other cell would have
```

---

## 9. The failure-layer taxonomy

Every non-clean cell gets exactly one primary tag. This is the bridge from
testing to the improvement plan: **the backlog is these tags sorted by frequency
× cost.** Do not tag "the model was dumb" — find the layer that let it be.

| tag | means | improvement it implies |
|---|---|---|
| `authoring` | The agent could have written a correct spec with what it had, and didn't. | Prompt/skill guidance, worked examples, Clarification structure. |
| `schema` | The structure is legitimate and schema v1 cannot express it. | v2 op (e.g. array/duplicate), or a documented boundary. |
| `physics-gate` | No estimator registered, or the estimator was wrong, or the recipe was mislabeled to get a green. | `physics.py` + `precheck-tolerances.json`; possibly a "no estimator — unchecked" loud verdict. |
| `compiler` | Spec was right, compiler built it wrong. | `hfss_spec/compiler.py`. |
| `pyaedt` | A backend defect the compiler hasn't absorbed yet. | env-compat entry + a compiler route-around. |
| `readout` | Solve fine, result unreadable. | Ticket 13. |
| `ceremony` | Phase sessions / ledger / gates cost more than they returned, or the route language failed. | SKILL.md, ticket 14's orchestrator. |
| `harness` | The *measurement* broke (attribution, hygiene, drift). | Pre-flight script, run_card aggregation. |

A cell tagged `harness` is a wasted cell — but tag it honestly, because a
campaign that produces three of them is telling you R1–R6 aren't tight enough.

---

## 10. Stop rules — what "enough" looks like

- **Wave A stops** when every launched cell has either a spec that passes the
  offline gates or a named blocker, **and** X0a/X0b have given you a noise floor.
  If the two X0 replicates differ by more than ~25% in billed tokens, treat every
  single-cell delta in the campaign as noise and say so in the write-up.
- **Wave B stops** at four builds, or earlier if two consecutive builds are clean
  — hardware time buys little once the compiler is reproducing dry-run plans.
- **Wave C stops** at two cells. More solving does not answer more questions
  while the readout is unlanded.
- **Wave D stops** when D3 has 3 cells per side. Fewer than three and the
  low-vs-max comparison is a coin flip.
- **Abort the campaign early** if U1 fails outright — if no LLM-authored spec
  passes the gates across batch A-1, stop and fix authoring; nothing downstream
  means anything until it does.

Total: **12–16 cells**, of which ~10 are offline and parallel, 4 need hardware,
2 need exclusive hardware.

---

## 11. What the campaign hands the improvement plan

Six artifacts, all falsifiable:

1. **A false-green rate** (U2) — the number the tool has never had, and the one
   that decides whether the automated gates are trustworthy enough to remove a
   human from the loop.
2. **An escape-hatch map** (U4) — which ops the schema is missing, ranked by how
   many structures needed them. This *is* the v2 schema requirements doc, and the
   array/duplicate gap is the standing hypothesis to confirm or kill.
3. **A controlled route-choice answer** (U3, D1/D2) — whether the routing
   language fails only when a copyable workspace exists, which decides between
   the three options in state doc §5.3.
4. **A low-vs-max authoring verdict** (D3) — a cost lever on every future run.
5. **A precheck-coverage gap list** — every precheck-blind structure attempted,
   and whether the agent noticed. Cheap estimators (dipole λ/2, monopole λ/4,
   circular patch) are trivial to add *if* the data says the blindness hurt.
6. **A parts profile** on the axis that is actually stuck — 424 → 477 → 312
   against a target of 60. Wave A gives the first-ever measurement of parts spent
   *before any desktop launch*, which is the part ticket 14's orchestrator would
   attack.

Write the improvement plan from those six, in that order. Not before.
