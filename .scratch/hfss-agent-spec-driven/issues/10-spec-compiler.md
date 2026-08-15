# 10 — The spec compiler: `design.yaml` → live model

**What to build:** Hand-written, deterministic Python that walks a validated
spec and builds the model on the live AEDT desktop via the typed spine surface.
No LLM in this layer, ever. It replaces the per-run generation of ten staged
scripts with one tested artifact, which is where most of the robustness and most
of the token saving come from simultaneously. Properties that matter:
**idempotent by construction** — every stage deletes the objects, boundaries,
excitations, mesh operations, and sweeps named in the spec before creating them,
so ADR 0008 stops depending on the model remembering it per script;
**selector resolution** — symbolic face and object selectors are resolved against
the live model at build time, so env-compat #7/#8 is enforced by the compiler
rather than by discipline; **variables first** — every dimension is emitted as an
AEDT design variable; **Verification lines preserved** — each stage still emits
its `PASS: <stage> <assertions>` line, so the existing self-correction and ledger
contracts continue to work unchanged; **quiet by default** — pyAEDT logging at
WARNING, one line out per stage. Keep the stage boundaries and their completion
criteria exactly as `SKILL.md` defines them: the Spine does not change, only who
writes the code that walks it.

Also close the template gap this exposes: `SKILL.md` references `08_solve` twice
and the template ships no `08_solve.py`, so every run re-derives it — along with
the pilot's hard-won fixes (skip-if-no-stale `cleanup_solution`, the
`subprocess.Popen(DETACHED_PROCESS)` launcher, `BoundaryObject.delete()`). Under
the compiler these become library code that no run re-derives.

**Blocked by:** 07, 08. Uses 13's typed surface if that has landed; otherwise
calls `ansys.aedt.core` directly and is refactored later.

**Status:** ready-for-human

- [ ] Compiler builds all five canonical cases end to end through `validate_simple()`, the horn included (sweep/loft ops per Q1) — **needs a live desktop**; `scripts/compile_spec.py --dry-run` passes for both existing specs
- [x] Re-running any stage in place converges — asserted by a test, not by doctrine
- [x] Symbolic selectors resolve against the live model; no id or edge reference anywhere in the compiler
- [x] Every stage emits its `PASS:` line in the existing format; the ledger contract is untouched
- [x] Golden tests: `spec → expected pyAEDT call sequence`, mocked, running in Tier 0
- [x] pyAEDT INFO logs suppressed; a full build prints one line per stage
- [~] The pilot's stage-script fixes are absorbed as library code and the escape-hatch path still works for anything the schema cannot express — three absorbed (lumped-port-by-name, XZ size order, `BoundaryObject.delete()`); the `08_solve` template gap is NOT closed, because solve submission stays imperative under the watchdog and belongs to a separate pass

- 2026-08-15: **IMPLEMENTED, pending its live run** - `hfss_spec/compiler.py`,
  CLI `scripts/compile_spec.py` (build only; `--dry-run` needs no desktop).
  - Walks the nine Spine stages in SKILL.md's order, one `PASS: <stage> ...`
    line each. The golden tests assert the exact call sequence against a
    recorder, so the whole build path is checkable with **no license** - which
    is the phase-2 claim in one file.
  - **Idempotency is asserted, not assumed**: build twice against the recorder,
    object count unchanged, and the deletes are in the log.
  - **Three defects from real runs are absorbed as library code.**
    `lumped_port` is given a sheet NAME plus an integration line, never a
    FacePrimitive (pyAEDT 1.3.0 serialises the face id into props["Objects"]
    and the macro layer rejects it - patch-2400 run); `create_rectangle("XZ")`
    sizes are swapped ONCE, in the compiler, because 2024 R1 maps them to
    [z, x]; boundaries are removed via `BoundaryObject.delete()` because
    `Hfss.delete_boundary` does not exist. No future run rediscovers any of
    them.
  - **Ambiguous selectors refuse** (Q3), and the error names the fix - add
    `pick: largest_area` or `nearest: [x, y, z]`.
  - pyAEDT is imported lazily and `PYAEDT_LOG_LEVEL=WARNING` is set before any
    import, so a full build costs the caller ten lines of context.
  - Remaining: the live build of all five cases, which needs a desktop and
    three more specs.
