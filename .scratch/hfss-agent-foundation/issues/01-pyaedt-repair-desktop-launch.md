# 01 — Repair pyAEDT, prove live desktop launch

**What to build:** the environment probe gate passes. `import pyaedt` succeeds at the pinned 1.3.0 on this machine (pip registers 1.3.0 but the package files are missing today), and a trivial script launches the graphical AEDT 2024 R1 desktop, creates a throwaway design, and exits cleanly — so every later ticket runs against a working toolchain.

**Blocked by:** None — can start immediately. (A valid AEDT license on the box is a hard prerequisite; if one is unavailable, escalate with the evidence instead of working around it.)

**Status:** ready-for-agent

- [ ] `import pyaedt` succeeds at version 1.3.0 in the repo's Python environment (install fixed, not just dist-info registered)
- [ ] Trivial script launches the graphical desktop (version 2024.1), creates a throwaway design, exits cleanly with no orphan process left behind
- [ ] If repair or launch fails, the failure is escalated to the user with the traceback — nothing downstream proceeds (spec's hard gate)
- [x] The pinned version and launch notes are visible in the environment-compat entry when it is created (ticket 02) — inputs prepared in `workspaces/env-probe/summary.md`

## Comments

- 2026-08-02: **RESOLVED** — acceptance passed; see `workspaces/env-probe/summary.md`.
- Criterion 1's premise was corrected during implementation: `import pyaedt` does not exist at 1.3.0 **by design** (official 1.3.0 wheel ships no `pyaedt/` package); the verified importable namespace is `ansys.aedt.core` (imports at 1.3.0). Any spec/plan text saying "import pyaedt" should be read as `import ansys.aedt.core`.
- Hard-gate escalation occurred and was resolved by the user: launch worked but design-open froze because the box's AEDT license server (`1055@LICENSE-ANSYS.ENGIN.UMICH.EDU` / `141.211.4.186`, FlexNet -15,10032, feature `hfss_gui`) was unreachable. **Standing prerequisite: UM VPN (Cisco Secure Connect) required to reach the license server.**
- Probe (`workspaces/env-probe/src/env_probe.py`) passes: graphical 2024.1 launch, throwaway design created, `release_desktop` + kill-until-gone asserts zero orphan `ansysedt` processes.
- Note for ticket 02: `Hfss()` with no solution_type defaults new HFSS designs to **Terminal** under 1.3.0/2024 R1 — driven-modal recipes must pass `solution_type="Modal"` explicitly.
