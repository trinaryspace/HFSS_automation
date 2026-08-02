# env-probe workspace summary — Ticket 01 (hard-gate escalation)

Date: 2026-08-02. Status of ticket 01: **BLOCKED/ESCALATED** — the trivial
desktop launch works, but no HFSS design can be opened on this box because
the AEDT license prerequisite (the plan's open item) is unmet.

## Verified environment facts

- Python 3.10.0 (`C:\Users\afpim\AppData\Local\Programs\Python\Python310`),
  pip 25.1, `pip check` clean.
- pyAEDT reinstalled at 1.3.0 (user reinstall; same version as before).
- **`import pyaedt` does not exist, by design**: the official PyPI
  `pyaedt-1.3.0-py3-none-any.whl` contains zero `pyaedt/` files (verified
  from the wheel). The namespace is `ansys.aedt.core` (imports fine, 1.3.0).
  PLAN task "verify import pyaedt" premise corrected → use `ansys.aedt.core`.
- AEDT 2024 R1 `v241` installed at `C:\Program Files\AnsysEM\v241\Win64`,
  `ANSYSEM_ROOT241` set, `ansysedt.exe` present. Only v241 on disk
  (`%APPDATA%\Ansys\v252` residue exists but no install).
- pyAEDT 1.3.0 transport is gRPC-only ("wnua"), **in-process**: the client
  loads AEDT's own `PyDesktopPlugin.dll` (`PyDLL`, holds the GIL during
  calls). `settings.use_grpc_api=False` does not change the transport
  (verified in logs). No remote-server components in the install.

## Probe matrix (all against live 2024 R1)

| path | result |
|---|---|
| pyaedt 1.3.0 launch, graphical `Hfss(design=...)` | desktop up + project created; **freeze at design-open** |
| pyaedt 1.3.0 launch, non-graphical | same freeze |
| pyaedt 1.2.0 (isolated venv), launch | same freeze |
| interactive scheduled task (user session) | same freeze |
| pyaedt attach (`new_desktop=False`, native gRPC :50051) | fails earlier: `GetActiveProjectName` GrpcApiError |
| stock `ansysedt.exe` GUI launch | **works**, window "Ansys Electronics Desktop 2024 R1", responding |
| stock `ansysedt.exe -RunScriptAndExit` (IronPython, create HFSS design) | **fails with license error** (see below) |

Call-surface detail (through the gRPC plugin): `NewProject`, `GetActiveProject`,
`GetName`, `InsertDesign("HFSS",·,"HFSS Modal Network",·)` work;
`SetActiveDesign`, `GetDesignNames`, `GetNumDesigns`, `GetActiveProjectName`
raise GrpcApiError; `GetActiveDesign` returns None with no design and
hard-freezes the client when a design exists (DLL call holds the GIL; even
watchdog threads stop). `InsertDesign("CIRCUIT",...)` → AEDT-side macro
error "unsupported design type = circuit".

## Root cause (license)

Stock-AEDT script error message, verbatim:

```
[error] Cannot connect to license server system.
Feature: hfss_gui
Server name: 141.211.4.186
License path: 1055@LICENSE-ANSYS.ENGIN.UMICH.EDU;
FlexNet Licensing error -15,10032
```

- Both `LICENSE-ANSYS.ENGIN.UMICH.EDU` and `141.211.4.186` unreachable on
  TCP 1055 (verified with Test-NetConnection).
- No `ANSYSLMD_LICENSE_FILE` / `LM_LICENSE_FILE` env override.
- `%APPDATA%\Ansys\v241\licensing` is empty; no stale config found under
  `%APPDATA%\Ansys`, `ProgramData\Ansys`, `HKCU\SOFTWARE\Ansys\Ansoft`.
- So: design-open (`hfss_gui` feature checkout) stalls on the dead server;
  every pyAEDT design flow wedges at that point. Secondary observation:
  `HFSSCOMENGINE.exe` exits with code -3 standalone (no WER report found).

## What feeds ticket 02 (environment-compat entry)

1. `ansys.aedt.core` (not `pyaedt`) is the importable namespace at 1.3.0.
2. pyAEDT 1.3.0 = gRPC-only in-process hosting of AEDT 2024 R1; broad COM
   objects work; `GetActiveDesign`/`SetActiveDesign` broken with a design
   present; attach-mode session broken.
3. License: the box is not licensed for AEDT 2024 R1 (dead UMich server) —
   a hard prerequisite, currently unmet.
4. pyaedt 1.2.0 behaves identically — not a client-version issue.

## Artifacts

- `src/env_probe.py` — acceptance probe (launch → design → release + exit).
- `src/env_probe_ipc.py`, `src/env_probe_nongraphical.py` — transport/mode variants.
- `src/diag_design_hang.py`, `src/diag_transport_bisect.py`,
  `src/diag_call_surface.py`, `src/diag_gui_windows.py`,
  `src/diag_attach_mode.py` — call-surface and mode bisections.
