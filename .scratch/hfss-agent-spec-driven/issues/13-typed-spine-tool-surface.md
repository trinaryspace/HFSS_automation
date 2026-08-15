# 13 — Typed spine tool surface; demote the KB to a fallback

**What to build:** Wrap the spine call set as validated Python functions with
explicit signatures, so that neither the compiler nor the agent ever looks up how
to call pyAEDT. The repo already found the right number: `generate_spine_api.py`
distils **36 calls** out of a 4,376-file corpus. Thirty-six typed functions are a
tool surface; 4,376 markdown files are a retrieval problem — and retrieval is a
weak lever (Foam-Agent's hierarchical multi-index RAG moves success 44.6% →
57.3%, against 50% → 80%+ for their reviewer node). Every CAD agent in the wild
exposes typed tools instead: the schema *is* the documentation, it is validated
at the call boundary, and signature discovery — roughly twenty steps in the
baseline run — costs nothing because it never happens.

Each wrapper carries its env-compat caveats as behaviour, not prose: assign
excitations by face object; never touch the raw COM surface (EC#3); set solution
type explicitly (EC#11); `analyze(blocking=False)` returns submission, not
completion (EC#5). The KB stays exactly as it is, demoted to a documented cold
path for calls outside the spine — `kb-lookup` keeps its read-only
exact-signature-or-NOT-FOUND contract for that case.

Wire in the ticket-16 readout findings while here, since they belong to this
surface and are currently stranded in an untracked workspace: `data_real` does
not exist in pyAEDT 1.3.0 (so the historical "unfilled" verdicts were a broken
reader, not an empty server), `full_matrix_real_imag` /
`get_expression_data` are the working accessors, and
`HfssConstants.default_solution = HfssConstants.solution_default` is the
validated one-line route-around. Amend env-compat #6 accordingly under ADR 0002.

**Blocked by:** None strictly; most valuable alongside 10.

**Status:** needs-triage

- [ ] All 36 spine calls wrapped with explicit signatures and validated arguments
- [ ] Env-compat caveats enforced in code where enforceable, cited in docstrings where not
- [ ] Readout wrappers use 1.3.0's real accessors; the `default_solution` route-around is applied defensively
- [ ] env-compat #6 amended with the ticket-16 evidence, through the ADR 0002 approval ceremony
- [ ] `SKILL.md` KB rules updated: typed surface first, `spine-api.md` second, corpus as cold-path fallback
- [ ] The `readout-route-around` workspace and its evidence are committed rather than left untracked
