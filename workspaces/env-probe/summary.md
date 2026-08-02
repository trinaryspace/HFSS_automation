# env-probe workspace summary — Ticket 01 (RESOLVED 2026-08-02)

> Archival note: the `src/diag_*.py` and `env_probe_{ipc,nongraphical}.py`
> files are a one-time investigation record from the ticket-01 escalation —
> not maintained tooling. `src/env_probe.py` remains the acceptance probe.
> Findings are authoritative in `knowledge/playbook/environment-compat.md`.

Ticket 01 acceptance passed: `import ansys.aedt.core` at 1.3.0, trivial
graphical desktop launch against AEDT 2024 R1, throwaway HFSS design
created, clean exit with zero orphan processes.

## Blocker history (root cause)

- Design-open froze in every pyAEDT path until the license was fixed.
- Stock-AEDT scripting showed the cause: `FlexNet error -15,10032`,
  `Feature: hfss_gui`, `Server name: 141.211.4.186`,
  `License path: 1055@LICENSE-ANSYS.ENGIN.UMICH.EDU`.
- Both hosts were unreachable on TCP 1055; no license env override
  existed; `%APPDATA%\Ansys\v241\licensing` empty.
- **User fixed the license by restoring/connecting the UM license server;
  the server requires the UM VPN (Cisco Secure Connect).** After that the
  host pair became reachable on 1055 and the probe passed unchanged.
- The plan's open item ("license availability unverified") is now
  RESOLVED with the caveat: **VPN access to the UM network is a standing
  prerequisite for any AEDT work on this box.**

## Verified environment facts (feed ticket 02's environment-compat entry)

- Python 3.10.0, pip 25.1, `pip check` clean.
- pyAEDT **1.3.0** installed. **`import pyaedt` does not exist by design**
  (official 1.3.0 wheel ships zero `pyaedt/` files); the importable
  namespace is `ansys.aedt.core`. PLAN's "verify import pyaedt" premise is
  corrected.
- AEDT 2024 R1 `v241` at `C:\Program Files\AnsysEM\v241\Win64`;
  `ANSYSEM_ROOT241` set.
- pyaedt 1.3.0 transport is gRPC "wnua" (in-process client DLL loading
  AEDT's `PyDesktopPlugin.dll`); it LAUNCHES a real `ansysedt.exe` process
  (aedt_process_id). `settings.use_grpc_api=False` does not change the
  transport (verified in logs). pyaedt 1.2.0 behaved identically.
- Working over gRPC on 2024 R1: launch, NewProject, GetActiveProject,
  InsertDesign("HFSS", name, "HFSS Modal Network", ""), full Hfss()
  lifecycle now that licensing works.
- Known awkward: previously-broken design discovery calls
  (GetActiveDesign/SetActiveDesign/GetDesignNames/GetActiveProjectName)
  behaved as suspected only under the dead-license stall; they were NOT
  re-bisected after the license fix — retest them in ticket 02's matrix
  before trusting them. The successful `Hfss()` path implies
  GetActiveDesign works when licensed.
- **Release behavior:** `release_desktop(close_on_exit=True)` logs
  "released" but does NOT terminate the launched `ansysedt.exe` in all
  cases; the probe therefore kills the `aedt_process_id` until gone
  (psutil) and asserts exit. Staged scripts in the skill should account
  for this (server reuse is the intended attach story, explicit quit is
  the probe's).
- **New HFSS design default solution type under 1.3.0/2024 R1 is
  "Terminal"** (observed on `Hfss(design=...)` with no solution_type).
  Recipe/Clarification work must set `solution_type="Modal"` explicitly
  for driven-modal recipes.
- Secondary observation: `HFSSCOMENGINE.exe` exits with code -3 standalone
  (no WER report); not blocking — investigate only if a later stage
  needs it.

## Artifacts

- `src/env_probe.py` — acceptance probe (launch → create design →
  release → assert zero orphan). Passing.
- `src/env_probe_ipc.py`, `src/env_probe_nongraphical.py` — transport/mode
  variants (kept as records; non-graphical path passes since license fix).
- `src/diag_*.py` — call-surface/mode bisection scripts from the blocker
  investigation (historical; useful for ticket 02's matrix).
