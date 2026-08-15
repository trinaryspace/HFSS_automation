# 03 — Real-artifact fixture corpus, and the rule that keeps fixtures honest

**What to build:** Both P0 bugs (tickets 01, 02) passed a 72-test green suite
because the fixtures were hand-written and wrong in ways the author could not
see: real artifact *names* written as files where AEDT writes directories, and a
profile fixture with unescaped quotes where AEDT escapes them. Green tests
actively concealed two broken safety paths. Build `fixtures/real/` — a small
corpus captured from actual workspaces by a script (`scripts/capture_fixtures.py`),
preserving entity type (file vs directory), relative layout, and byte content for
text artifacts, truncated/anonymised where large. Cover: a Normal Completion
profile, the `Engine Detected Error` profile from `bowtie-3500`, a profile
carrying two Solution Process groups, the `.imesh`/`.cmesh`/`_ADP*` directory
families, `_F####_SU.txt` sweep files, `.sd` in both file and directory form, and
`.asol.semaphore` in-flight markers. Then make the rule enforceable: every parser
test runs against the real corpus, and a synthetic fixture is permitted only
alongside a real counterpart. Add the rule to `docs/agents/` so it outlives this
feature.

**Blocked by:** None — capture can start immediately; 01 and 02 consume it.

**Status:** ready-for-human

- [x] `scripts/capture_fixtures.py` regenerates `fixtures/real/` from a named workspace, idempotently and byte-stably
- [x] Corpus covers every artifact class listed above, with entity type preserved (a test asserts `os.path.isdir` where AEDT makes a directory)
- [x] All profile / family / semaphore parser tests read from the corpus
- [x] A test fails loudly if the corpus is missing rather than silently skipping
- [x] The fixture-fidelity rule is written into `docs/agents/` and referenced from the template README
- [x] Corpus is committed (it is small and it is the ground truth); large binaries excluded via `.gitignore`

## Comments

- 2026-08-14: **DONE.** `scripts/capture_fixtures.py` captures three cases
  from workspaces that actually solved here: `pilot-normal` (two profiles,
  including the two-Solution-Process one), `baseline-engine-error` (the
  `Engine Detected Error` profile), and `bowtie-3670`. Corpus lives at
  `skill/hfss-agent/templates/workspace/src/fixtures/real/` so it travels
  with the workspace template and a copy can verify itself. Total 315 KB.
- **Profiles are sliced, not truncated.** Originals run 112-448 KB, most of
  it `ProfileItem` rows no parser reads. Lines are kept where they carry
  structure, a group name, an elapsed time, or a footnote — escaping
  byte-preserved. The capture **refuses to write a slice that does not
  parse identically to its original**, so a fixture cannot drift from the
  artifact it stands for.
- **`tree.json` records entity type.** `real_fixtures.materialize()` rebuilds
  a tree creating a directory wherever AEDT created one, and reproduces
  total file counts exactly (1142 / 2666 / 5164, matching the real trees).
  This is the device that makes the ticket-02 bug class impossible to
  reproduce by accident.
- **Loud on absence.** `real_fixtures` raises `FixtureCorpusMissing` rather
  than skipping, and `scripts/tier0.py` runs a corpus check as its first
  suite. Rerunning capture with unchanged inputs is byte-stable (verified
  by sha256 over the whole corpus).
- The rule is written into `docs/agents/fixture-fidelity.md` and indexed
  from `AGENTS.md`, including the honest account of both bugs — the
  knowledge previously lived only in one ticket's comment thread, which is
  why ticket 13 shipped without it minutes after ticket 14 recorded it.
