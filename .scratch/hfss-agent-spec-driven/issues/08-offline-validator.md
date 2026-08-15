# 08 — Offline validator: catch it before AEDT launches

**What to build:** A validation pass over `design.yaml` that runs with no
desktop, no license, and no pyAEDT import, and that refuses to hand a spec to the
compiler until it is coherent. Four checks beyond schema conformance.
**Reference resolution:** every symbolic selector names an object the spec
actually declares, every variable reference resolves, and every material is
either an AEDT library material or declared in the spec. **Unit and dimensional
consistency:** expressions combining variables are dimensionally sound, and the
sweep range brackets the design's target frequency. **Topological sanity:**
ports sit on solids that exist, the radiation boundary encloses the radiating
structure, no two named objects collide by construction. **Completeness against
the recipe:** the spec declares everything its recipe requires — the class of
omission the Clarification block is supposed to catch ("critical setup features
the user left out") now checkable mechanically. Every finding is an error or a
warning with the offending path in the spec (`geometry[2].base`), so a diagnosis
seam gets a precise location rather than a stack trace. This is where most of
the current self-correction loop's work moves: schema and reference errors cost
zero AEDT time and near-zero tokens.

**Blocked by:** 07.

**Status:** ready-for-human

- [x] Runs in Tier 0 with no AEDT installed; no pyAEDT import anywhere in the module
- [x] All four check classes implemented, each with at least one deliberately-broken spec fixture
- [x] Findings carry a spec path and an error/warning severity; output is one summary line plus a findings list
- [~] The pilot's real geometry-correction episode is reproduced as a fixture and caught by the validator — **partly, and the gap is the point**: the validator catches the *reference* and *dimensional* classes, and a `sweep does not contain the target` fixture reproduces the shape of the pilot's failure. But the pilot's actual error was a VALUE error — Astuti's Table and Figure disagreeing — which no schema check can see. That is ticket 09's closed-form pre-check, and this ticket cannot close it
- [x] Validator is a hard gate in the compiler's entry point — the compiler cannot be invoked on an unvalidated spec

- 2026-08-15: **IMPLEMENTED** - `hfss_spec/validate.py`, CLI
  `scripts/validate_spec.py`, plus `scripts/validate_cases.py` which validates
  every canonical case holding a `design.yaml` and reports the ones that do
  not have one yet. Both wired into Tier 0.
  - All four classes fire with a deliberately-broken fixture each: reference
    ("'Sbu' is not a declared object - did you mean 'Sub'?"), dimensional
    ("size[2] must be length, got time^-1"), topological (a boolean whose tool
    does not exist *at the point it runs*, and zero extents), and completeness
    (a `qa_signals` entry with no evidence behind it, and no excitation).
  - **The sweep-bracket check earns its place twice.** It refuses a sweep that
    does not contain the target at all, and warns when it brackets by less than
    20% - which fires on both real specs, and would have fired on the pilot's
    3.2-4.2 GHz sweep against a 3.5 GHz target whose model resonated at 3.85.
  - Findings carry a path (`geometry[0].size[2]`) and a severity, output is one
    summary line plus a list, and the exit code is 0 only with zero errors.
  - `require_valid()` is called at the top of `compiler.build`, so the compiler
    physically cannot run on an unvalidated spec - asserted by a test.
  - Honest gap, marked in the checklist: the pilot's real failure was a VALUE
    error (Astuti's Table vs Figure), which no schema check can see. That is
    ticket 09's closed-form pre-check.
