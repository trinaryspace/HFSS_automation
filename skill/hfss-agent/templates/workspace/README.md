# Workspace template

One Workspace per conversation. Copy this folder to `workspaces/<name>/`
when a conversation starts (the hfss-agent skill creates it). Tool and
knowledge directories stay clean; workspace outputs are gitignored.

Shape:

```
workspaces/<name>/
├── src/                 # staged scripts, one per Stage: NN_<stage>.py
├── <name>.aedt          # the AEDT project file (created by the staged scripts)
├── results/             # requested plots and exported results
└── summary.md           # acute design decisions + what the Model is
```

Rules that make the workspace work:

- **src/ scripts are the re-runnable record.** One Stage = one script =
  one Run. Every script carries the attach-or-launch preamble from
  `skill/hfss-agent/reference/execution.md`. The Read-back sync (ADR 0005)
  amends these scripts after user UI tweaks so replaying top-to-bottom
  reproduces the delivered model.
- **Session state lives in the AEDT project**, never in a Python process:
  scripts attach to the running desktop, and the desktop stays alive
  between stages.
- **results/ holds deliverables** (plots, exported data); nothing else
  goes there.
- **summary.md is written at the end of the conversation** (see skeleton)
  and updated by read-back sync deltas and learning-loop notes.
- `.aedt`, `.aedtresults/`, `results/`, and lock files are gitignored;
  `src/` and `summary.md` are the tracked record.
