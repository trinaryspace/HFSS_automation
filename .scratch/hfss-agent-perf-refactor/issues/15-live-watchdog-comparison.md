# 15 — Live watchdog stage-agreement test

**What to build:** A live-box acceptance test for the stage-aware watchdog, decoupled from the full pilot. Take a throwaway copy (Re-entry copy semantics — the original project is never touched) of a solve-ready design, submit a non-blocking solve, and run the new watchdog while the user watches the desktop UI for the solve's duration. The user records the stages they observe in the UI; the watchdog writes its stage lines; the two sequences are diffed. Any disagreement is triaged as a watchdog bug (not "UI was right") and fixed before the re-pilot. This also answers the open implementation unknown: whether the solve profile is written incrementally per stage or only at the end.

**Blocked by:** 14 — stage-aware solve watchdog.

**Status:** ready-for-agent

- [ ] Solve completes on the copy; the original project is verified untouched
- [ ] User-observed stage sequence recorded (UI is the ground truth)
- [ ] Diff report posted to this ticket: stage-by-stage agreement, or the mismatches listed
- [ ] Every mismatch fixed as a watchdog bug and re-verified before the re-pilot
