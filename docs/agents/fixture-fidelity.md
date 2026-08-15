# Fixture fidelity

A test fixture that does not match the artifact it stands for is worse than
no test: it reports PASS while the code under it is broken, and it makes the
suite an argument *against* looking further.

This repo has paid for that twice, on the same day, in the two most
safety-critical paths it has:

- **Escaping.** AEDT writes profile footnotes with escaped quotes —
  `\'Status\', \'Normal Completion\'`. `confirm_solve`'s regex expected the
  bare form, so `terminal_status()` returned `None` for **9 of 9** real
  profiles. Nothing could ever be banked, `guard_verdict()` fell through to
  `proceed`, and teardown purged solved results — the exact incident the
  guard was written to prevent. Its tests passed, against a hand-written
  fixture with unescaped quotes.
- **Entity type.** `.imesh`, `.cmesh` and `_ADP*` artifacts are
  **directories** on this box. `scan_results()` applied its family patterns
  to filenames only, so `mesh` and `adp` read `(0, 0)` against every real
  tree and the watchdog was blind to stage until sweep files appeared. Its
  test used the real artifact *names* — written as files.

Both fixtures were written by someone who had read the real artifacts. The
knowledge was there; ticket 14's comments record the escaping correctly.
What was missing was a place for it to live other than prose.

## The rule

**Fixtures come from captured artifacts, not from memory.**

1. `skill/hfss-agent/templates/workspace/src/fixtures/real/` is the corpus,
   captured by `python scripts/capture_fixtures.py` from workspaces that
   actually ran on this box. It is committed, and it travels with the
   workspace template so a workspace copy can verify itself.
2. Parser and scanner tests read from that corpus. `real_fixtures.materialize()`
   rebuilds a results tree **creating a directory wherever AEDT created a
   directory**, so entity type is reproduced rather than assumed.
3. A synthetic fixture is allowed only **alongside a real one**, with a test
   asserting the two parse identically — see
   `test_synthetic_profile_matches_real_shape`. Synthetic fixtures are for
   varying a case, never for defining what the artifact looks like.
4. A missing corpus is a **failure, not a skip**. `real_fixtures` raises
   `FixtureCorpusMissing`, and `scripts/tier0.py` checks corpus presence as
   its first suite. Tests that quietly pass when their ground truth is
   absent are how both bugs survived.
5. The capture script **verifies its own slices**: a sliced profile is
   written only if it parses identically to the full original, so a fixture
   can never drift from the artifact it represents. Rerunning capture with
   unchanged inputs is byte-stable.

## When you add a parser

Ask what the artifact *actually* looks like on disk, and answer it by
looking — `find`, `ls -la`, `head` — not by recalling. Then capture what you
found. If a new artifact class matters, add it to `ARTIFACT_SUFFIXES` /
`ARTIFACT_SUBSTRINGS` in `scripts/capture_fixtures.py` and recapture.

Two questions catch most of this class:

- **Is it a file or a directory?** AEDT uses both, for names that look alike.
- **How are quotes and separators escaped?** Read a real line; do not infer
  it from the shape of the parsed value.

## One parser per evidence type

Profile status, stage ledger, and artifact families each have exactly one
implementation (`profile_evidence.py` for the first two). Two parsers for
one evidence type will disagree eventually, and the disagreement will be
silent — that is precisely how the banking bug happened. `verify_skill.py`
enforces this: a second compiled `Status` pattern anywhere in the template
`src/` fails the check.
