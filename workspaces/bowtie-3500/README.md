# Workspace — bowtie-3500

Greenfield build: baseline bow-tie microstrip patch antenna (Astuti et al.,
"Bandwidth Enhancement of Bow-tie Microstrip Patch Antenna Using Defected
Ground Structure for 5G", JCM 17:12, 2022) — **without** the DGS per user
decision — reproducing the paper's baseline reference antenna (~3.5 GHz
resonance). Driven-Modal, single waveport, radiation airbox. The user
reviews the model in the AEDT UI before anything solves.

Shape:

```
workspaces/bowtie-3500/
├── src/                 # staged scripts, one per Stage: NN_<stage>.py
├── bowtie_3500.aedt     # the AEDT project file (created by the staged scripts)
├── results/             # requested plots and exported results
└── summary.md           # acute design decisions + what the Model is
```

- src/ scripts are the re-runnable record (one Stage = one script = one Run,
  attach-or-launch preamble, ADR 0003/0005).
- Session state lives in the AEDT project; the desktop stays alive between
  stages.
- summary.md is written at the end of the conversation and updated by
  read-back sync deltas (ADR 0005) and learning-loop notes (ADR 0002).
- .aedt, .aedtresults/, results/, lock files: gitignored.
  src/ and summary.md: the tracked record.
