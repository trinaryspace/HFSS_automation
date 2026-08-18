# Vision

The layer above the ADRs. `CONTEXT.md` fixes the vocabulary, `docs/adr/` records
what was decided, `.scratch/<feature>/spec.md` records what a feature is for —
and this document is what all three are answerable to. An ADR argues from a
local incident; this says what the incidents are supposed to add up to.

It is deliberately short. A vision nobody can hold in their head does not bind,
and this project has already learned, expensively, that guidance which does not
bind is decoration.

---

## 1. North star

An engineer describes what they need — a band, a gain, a structure, a
constraint — and gets back a correct, solved HFSS simulation: geometry,
materials, excitations, setup, results and plots, with every assumption stated,
every derived number traceable to a relation that was actually checked, and
every claim backed by evidence they can inspect themselves.

The conversation does the engineering work it can verify, **asks about the rest
rather than guessing**, and never lets the difference between those two go
unmarked.

## 2. Who it is for

**Now:** one researcher, on one machine, with AEDT 2024 R1 and a reachable
licence. Every environment fact is honest about being that specific.

**Next:** the lab — colleagues with their own installs, their own structures,
and no interest in this repo's internals.

**Not:** a general public tool. That is not a permanent exclusion, but it is not
what any current decision is optimized for.

*Consequence.* `knowledge/playbook/environment-compat.md` is a **staging
artifact with a known expiry**, not a permanent fixture. We do not pay a
portability tax on every decision today; we also do not hard-code in ways that
make portability impossible later. When a choice is cheap to keep portable, keep
it portable. When it is expensive, write down what it costs to undo.

## 3. What it is: a design partner, earned in stages

**The destination.** You bring a requirement; the agent derives the structure
and the dimensions, proposes them with its reasoning exposed, and builds what
you approve. Synthesis is a first-class goal, not an apology.

**Where it actually stands.** Today it is a fine draftsman with six closed-form
estimators. Give it dimensions and a structure the op set can express, and it
builds, gates, solves, and reports honestly. Ask it to *derive* dimensions
outside those six and it has nothing — and correctly says so. The distance
between draftsman and design partner **is the project**.

**How that distance gets closed: every synthesis capability enters through the
front door.** A capability is real when it:

- **computes**, rather than advising in prose;
- **cites its relation**, so a reader can check the source;
- is **tested against a worked example** whose answer is known independently;
- carries a **tolerance that is data, not code**, because what counts as a
  disagreement worth raising is a domain judgement;
- **fails loudly outside its validity range**, because a gate that reports a
  meaningless number confidently is worse than no gate.

This is not invented. It is the pattern `hfss_spec/physics.py` already follows —
Hammerstad's validity bounds, tolerances in JSON, worked examples recomputed in
`knowledge/cases/` — promoted from a habit to a law.

**Therefore hard rule 8 is a routing rule, not a ban.** "Never build the missing
capability" has always meant *never build it inline, mid-conversation, untested,
to get past a blocker*. Building it deliberately, as its own reviewed piece of
work, is the front door and is exactly how the tool is supposed to grow.
Synthesis is welcome. Improvisation is not. The measured failure that rule 8
exists to prevent was never "an agent did synthesis" — it was an agent writing a
field solver inside a Clarification block and delivering nothing.

## 4. The division of labor

Three parties, and one principle that assigns work between them.

**Deterministic code** owns everything checkable without judgement: building the
model, resolving selectors, units and dimensions, reference and topological
integrity, idempotency, process lifecycle, watching a solve, banking evidence,
capturing and diffing state. *If it can be a test, it must not be a prompt.*

**The language model** owns what is genuinely open-ended: understanding an
under-specified request, mapping it to technique, proposing assumptions worth
confirming, diagnosing a failure from precise evidence, and writing the account
of what was done. Ideally three seams, not a continuous conversation.

**The human** owns what neither can: deciding what *right* means for this
design, and looking at the model.

*The principle.* Work moves **down** that list over time — from model to code —
and never back up. Every time a behaviour graduates from "the agent should
remember to" into a function with a test, the tool gets more capable and
cheaper at once. That single move is the source of nearly every real improvement
this project has made.

## 5. Correctness, in stages

**Today — an explicit split.** The machine guarantees *mechanical* correctness:
the model is built exactly as specified, the run is reported honestly, terminal
states are evidenced. The human owns *design* correctness: whether this is the
right structure, the right dimensions, the right answer. Gates never certify
that a design is good, **and they say so** — a green run means the mechanical
properties hold, nothing more.

This is not humility for its own sake. Six specs once passed every automated
gate with zero errors and zero escape hatches, and three of them were wrong.

**The ladder.** Each synthesis capability that comes through the front door
brings a computed check with it. So the machine's coverage of design correctness
is not a claim — it is a quantity that grows, and that we can state.

**The far horizon, with a key rather than a vibe.** Machine review may
eventually take load off the human. It earns that when the **false-green rate,
measured on a real and growing corpus of specs, approaches zero** — on evidence,
never by assertion, and never because the checks *feel* mature. The door is
open. The key is a number, and today that number is 50%.

## 6. Durable principles

1. **Evidence before claiming.** A terminal state is read from an artifact, not
   inferred from a plateau. This generalizes: nothing is reported as true
   because it is probably true.
2. **The cheapest gate that can see a defect should be the one that catches
   it.** Milliseconds before seconds, seconds before a desktop, a desktop before
   the solver.
3. **A check that computes is not a check that advises.** Correct knowledge,
   correctly written and correctly read, has been demonstrated to change
   nothing. Encode limits as refusals with exit codes.
4. **Never promise what has not been probed.** The backend is discovered, not
   assumed; what it cannot do is written down where the next run will find it.
5. **Fixtures come from reality, never memory.** Two bugs reached production
   through 72 green tests written against invented artifacts.
6. **Account honestly, especially against yourself.** An incomplete run costs
   infinity, not "somewhat more". Bad runs stay in the table. A metric that
   flatters us is worse than no metric.
7. **The human gates are load-bearing.** Clarification agreement and the visual
   Review gate stay, in the same place, with the same authority, until §5's
   number says otherwise.

## 7. How we know it is working

- **Cost per *completed* simulation** — the headline. Incomplete scores
  infinite. Standing target: ≤ 80,000 billed tokens and ≤ 60 steps. Today's best
  honest run is 477 steps; the gap is real and is not to be redefined away.
- **False-green rate** — the most important number in the project, because it is
  the only one that measures whether a passing run deserves trust. Measured on a
  real corpus. Currently 50%.
- **Escape-hatch rate** — where the schema is wrong, expressed as a number
  rather than as quiet improvisation.
- **Estimator coverage** — how much of the design space the agent can derive
  rather than merely build. This is the design-partner progress bar.
- **Time to first honest "I don't know"** — how quickly a gap is surfaced rather
  than flailed at. The 51-minute detour is the anti-example.

## 8. Non-goals

- **Not a CAD kernel and not a solver.** AEDT is the engine; we drive it.
- **Not a multi-backend EM tool.** One backend, understood deeply.
- **Not autonomous.** It does not solve without a human gate, and will not until
  §5's ladder earns it.
- **Not a chatbot about electromagnetics.** The deliverable is a project file,
  plots, and a summary — artifacts, not advice.
- **Not cheap at the expense of honest.** Token cost is a real constraint and
  never a reason to skip evidence, a gate, or an escalation.

## 9. Horizons

**H0 — where we are.** The mechanical path is proven on hardware: the compiler
reproduces a model that once took a 25-hour pilot, with zero snapshot
differences. The authoring step in front of it has never been attempted.

**H1 — prove the seam (current).** Establish whether a language model can author
a valid `design.yaml` at all, measured against known-good cases. Then close the
deterministic orchestrator so a run is a state machine with three model seams
rather than an open-ended conversation. Depth before breadth: widening on an
unproven foundation multiplies false-greens rather than capability.

**H2 — become the partner.** Synthesis capabilities through the front door,
estimator coverage growing measurably, the schema learning what the escape-hatch
rate says it is missing, and portability to the lab.

**H3 — earn the review.** Machine review takes load off the human, gated on §5's
measured number.

## 10. How to use this document

Every ADR, spec, and ticket should be checkable against this. If a piece of work
cannot be justified here, then either the work is wrong or this document is out
of date — and finding out which is the point.

This changes deliberately, never incidentally. A revision is its own commit,
with its reason stated.
