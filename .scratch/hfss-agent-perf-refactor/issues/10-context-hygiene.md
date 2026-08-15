# 10 — Context hygiene: quiet scripts, one diagnostics script

**What to build:** Staged-script runs stop flooding the conversation: every script suppresses pyAEDT INFO output by default so only its verification line and assertions surface in context. A single purpose-built diagnostics script, written once per Workspace, prints the whole machine snapshot in one attach — pin liveness, project path, object/boundary counts, newest solve profile status, sweep-entry count, and the Readout one-shot where available — and becomes the only legitimate diagnostics surface; throwaway probe files are a ceremony violation. Execution text tightens the existing tail rule (exactly 1–3 lines, never whole progress/log files) and the agent-message cap is retained.

**Blocked by:** None — can start immediately.

**Status:** ready-for-agent

- [ ] Running any staged script produces no pyAEDT INFO lines in its output
- [ ] One diagnostics script exists in the Workspace template and prints the full snapshot in a single attach
- [ ] Execution text states: tail exactly 1–3 lines, never whole files; no throwaway probe files (diagnostics script is the only surface)
- [ ] Template-runner test suite green (no-AEDT seam covers the quieting default)
