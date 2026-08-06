# HFSS Automation Context

This repo lets a conversation with an agent produce a complete, correct ANSYS HFSS simulation — geometry, materials, excitations, setups, solves, plots, and results — by having the agent drive pyAEDT directly against a live AEDT desktop, guided by a scraped API knowledge base and a curated EM-design playbook.

## Language

**The Spine**:
The solution-type-agnostic pipeline every build runs through: interpret & clarify → choose solution type → design → geometry → materials → excitations/boundaries → mesh → setup+sweep → solve → post-process → reports/plots. Early adapters fill shared stages; the agent fills per-case details.
_Avoid_: pipeline, workflow, build process

**Greenfield build**:
A conversation that creates a new simulation from a user's description, walking forward through the Spine.
_Avoid_: new project, from scratch

**Stage**:
One named step of the Spine (geometry, materials, excitations/boundaries, ...). A stage is the unit the user reviews in the open desktop window before the next stage runs.
_Avoid_: step, phase, chunk

**Staged script**:
The single `.py` file a stage produces, written to the conversation's `src/` folder. It carries a standard preamble that attaches to (or launches) the running AEDT desktop, so session state lives in the AEDT project itself, not in any Python process.
_Avoid_: chunk, snippet

**Run**:
One execution of a staged script. Error self-correction amends the script and re-runs it.
_Avoid_: chunk, attempt

**Recipe**:
A named, playbook-backed path through the Spine for a problem class: default solution type, excitation/boundary strategy, setup+sweep choices, the Result QA signals that apply, and the standard plots. The playbook organizes by recipe; clarification maps the user's request onto a known recipe (or derives a new one), and a re-entry pivot is a recipe switch.
_Avoid_: workflow, preset, template

**Project**:
The AEDT `.aedt` file on disk. May contain multiple designs; in Re-entry it is the unit that is copied and whose original is never mutated.
_Avoid_: model, workspace

**Design**:
An AEDT design object inside a project. Used only when talking AEDT internals (e.g. which design a setup or boundary lives in).
_Avoid_: model, project

**Model**:
The EM artifact the user is building and reviewing — geometry, materials, excitations, setups — regardless of how many AEDT designs realize it. ("Math model" in the Review gate is the same thing.)
_Avoid_: design, project

**Workspace**:
The per-conversation folder holding the staged scripts (`src/`), the project file, `results/`, and `summary.md`. Tool and knowledge live outside it and stay clean.
_Avoid_: project folder, session folder

**Re-entry**:
A conversation that opens an existing project (possibly not AI-created) to add to or change its setup, then re-solves. The original `.aedt` (results included) is first copied into the workspace as a plain file operation; all introspection and changes happen on the copy, and the original is never opened or mutated.
_Avoid_: modify existing, edit, tweak

**Knowledge base (KB)**:
The scraped pyAEDT API documentation the agent reads to know exactly which pyAEDT call does what. It teaches "how to call the API", not "how to design the simulation".
_Avoid_: docs, api reference

**Playbook**:
The curated, reviewable store of EM-design technique, organized by Recipe: design equations, recommended setup/solution-type/sweep choices, the Result QA signals per recipe, canonical EM-simulation texts, and accumulated experience (including user-paper additions). Also holds the environment-compat entry recording what the pinned pyAEDT↔AEDT pairing does and doesn't support. It teaches "how to design the simulation correctly". Live web research is a backup only when the playbook has no entry.
_Avoid_: guide, manual, reference

**Clarification**:
The up-front, single-block exchange where the agent gathers the minimum information it needs, spots critical setup features the user left out, researches the appropriate technique, and proposes concrete suggestions. The user confirms or redirects — nothing is built until that agreement.
_Avoid_: questioning, polling, asking

**Assumption**:
Anything the agent fills in from domain knowledge without asking. Every assumption is stated to the user so it can be corrected.
_Avoid_: guess, default, inference

**Review gate**:
The point before solving where the user inspects the fully-built setup (visually in the opened math model, not by reading scripts) and may make manual changes. Nothing solves until the user passes it.
_Avoid_: checkpoint, approval, verification

**Result QA**:
The agent's automated post-solve check of physics signals (convergence, ports excited, energy pass, in-band resonance, plausibility against the playbook). It flags anomalies and reports them; only the user decides whether results are junk.
_Avoid_: validation, check, quality control

**Learning loop**:
The mechanism that turns experience into future capability: the agent fixes the current model now, THEN proposes a playbook amendment, and appends only after user approval. Three triggers earn a proposal: a user tweak that generalizes to the recipe class; a backend-compat discovery (lands in the environment-compat entry); a Result-QA anomaly whose resolution generalizes. Project-specific values stay in the summary.
_Avoid_: feedback, lessons, improvement

**State ledger**:
The per-Workspace file (`state.md`) recording stage progress, locked design variables, decisions, and pitfalls, written by each phase session and read by the next. Conversation state that survives between sessions; machine state lives in `results/state/*.txt`.
_Avoid_: handoff doc, status file, notes

**Run card**:
The per-run record of token spend, step count, and wall time, appended to `summary.md` by the measurement harness; the proof that an optimization refactor worked, judged against a baseline run.
_Avoid_: stats, metrics, analytics

**Verification line**:
The single machine-parseable `PASS:` line each staged script emits on success, carrying its stage's assertions; the self-correction loop reads that line rather than filtered logs.
_Avoid_: log line, PASS marker, exit status

**Summary**:
The end-of-conversation artifact recording the acute design decisions made and what the model is. Delivered alongside the project file and the requested plots.
_Avoid_: report, handoff, final output
