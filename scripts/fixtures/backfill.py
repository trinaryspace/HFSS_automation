"""Backfill `results/state/sessions.jsonl` for the runs that predate it.

Run logging, ticket 10. Ticket 01 made every `scripts/session.py --phase`
declaration append one line to `sessions.jsonl`; the three runs the
acceptance grades happened before that, so their workspaces cannot name
their own sessions. This writes the record by hand, from what the runs left
behind, and marks every line `backfilled: true` so no reader mistakes it
for a line the run wrote:

- `patch-array-5800` — the seven `--name patch-array-5800-*` declarations
  the 2026-08-18 run made inside ONE opencode session (`neon-eagle`,
  `ses_fe9ae6dd3ffe2a8knbeE1b4yrr`; the ledger's `hidden-falcon` is its
  runcard subagent), each at the emission instant of its `session.py
  --phase` call in the step trace (`results/state/trace/<id>.steps.jsonl`,
  seq quoted per line; the solve-1b declaration at seq 648 failed on its
  cwd and is not a declaration — seq 652 landed); plus the 2026-09-01
  readout experiment's declaration from the Claude Code session
  `e5cdcdf5-e3fe-4a62-9402-0e4010171c51` at the `started_ms` its
  `session.json` recorded. `skill_commit` for the Aug 18 lines is the
  campaign log's frozen skill commit for cell S7SIM (`2d47289`). These
  are records of declarations the run made (`declared_by_run: true`).
- `bowtie-3500-pilot` — `shiny-canyon` (`ses_02ac8a0abffeZ11jkrOvvXgcxR`),
  one opencode session that declared no phase (the boundary did not exist
  on 2026-08-06). The ledger's three sessions are mapped onto it at the
  trace's instants: the session's first step, the template copy that
  created the workspace, the first `08_solve.py` run. The pilot went back
  to build work after its first solve (the geometry correction); those
  steps sit under `solve` here. `declared_by_run: false`.
- `patch-2400` — `kind-rocket` (`ses_ffcffc801ffekiGf69dPTa9SQw`), the
  same shape (opencode.json's comment names the slug; the DB titles it
  "2.4 GHz inset-fed patch antenna HFSS sim"). `declared_by_run: false`.

A line has ticket 01's keys (`hfss_spec.session.history_record`: `ts`,
`ts_ms`, `phase`, `name`, `host`, `host_session_id`, `cwd`, `worktree`,
`skill_commit`, `pid`) plus `backfilled`, `backfill_source` (the evidence
the instant and name were read from) and `declared_by_run`. `pid` is null
and `skill_commit` "" where nothing recorded them. `hfss_spec.painpoints`
attributes steps by these lines like any other and, for a
`declared_by_run: false` line, still reports the session as undeclared by
the run itself.

    python scripts/fixtures/backfill.py [--workspaces DIR]

writes `scripts/fixtures/<workspace>/state/sessions.jsonl` (the committed
copy) and `workspaces/<workspace>/results/state/sessions.jsonl` (the
gitignored one the report reads), byte-identical, and materializes every
other captured state file of `scripts/fixtures/<workspace>/state/` into the
workspace when the workspace lacks it — never over a file the workspace
already has. Rerunning is byte-stable. Events are not backfilled: stage
boundaries the run never wrote cannot be reconstructed, and the report
says so in its headline.
"""

import argparse
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
STATE_SUBDIR = "state"
SESSIONS_FILE = "sessions.jsonl"
BACKFILL_INDEX = "backfill.json"
WRITTEN_ON = "2026-09-02"
MAIN_CHECKOUT = "C:/Users/afpim/Repos/HFSS_automation"

OPENCODE, CLAUDE = "opencode", "claude-code"
NEON = "ses_fe9ae6dd3ffe2a8knbeE1b4yrr"
READOUT = "e5cdcdf5-e3fe-4a62-9402-0e4010171c51"
CANYON = "ses_02ac8a0abffeZ11jkrOvvXgcxR"
ROCKET = "ses_ffcffc801ffekiGf69dPTa9SQw"
S7SIM_SKILL_COMMIT = "2d47289"       # campaign-log.md, "skill commit (frozen)", 2026-08-16

TRACE = "results/state/trace/{sid}.steps.jsonl seq {seq}: {cmd}"


def _decl(ts_ms, phase, name, host, sid, source, by_run, skill_commit="", cwd=MAIN_CHECKOUT):
    return {
        "ts": datetime.fromtimestamp(ts_ms / 1000.0, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ts_ms": ts_ms, "phase": phase, "name": name, "host": host, "host_session_id": sid,
        "cwd": cwd, "worktree": cwd, "skill_commit": skill_commit, "pid": None,
        "backfilled": True, "backfill_source": source, "declared_by_run": by_run,
    }


def _neon(ts_ms, phase, name, seq):
    return _decl(ts_ms, phase, name, OPENCODE, NEON, by_run=True, skill_commit=S7SIM_SKILL_COMMIT,
                 source=TRACE.format(sid=NEON, seq=seq,
                                     cmd=f"python scripts/session.py --workspace workspaces/patch-array-5800 "
                                         f"--phase {phase} --name {name}"))


RECORDS = {
    "patch-array-5800": [
        _neon(1787081256565, "clarify", "patch-array-5800-clarify", 149),
        _neon(1787086715883, "build", "patch-array-5800-build", 243),
        _neon(1787088958781, "solve", "patch-array-5800-solve", 473),
        _neon(1787089493218, "build", "patch-array-5800-build-2", 536),
        _neon(1787092164214, "solve", "patch-array-5800-solve-1b", 652),
        _neon(1787093462757, "build", "patch-array-5800-build-3", 740),
        _neon(1787093994327, "solve", "patch-array-5800-solve-2", 822),
        _decl(1788289309350, "solve", "readout-experiment-2026-09-01", CLAUDE, READOUT, by_run=True,
              source="results/state/session.json started_ms (the declaration's own write); the command "
                     f"is results/state/trace/{READOUT}.steps.jsonl seq 728: cd C:/Users/afpim/Repos/"
                     "HFSS_automation && ... python scripts/session.py --workspace workspaces/"
                     "patch-array-5800 --phase solve --name readout-experiment-2026-09-01"),
    ],
    "bowtie-3500-pilot": [
        _decl(1785988603879, "clarify", "", OPENCODE, CANYON, by_run=False,
              source=f"the session's first step (results/state/trace/{CANYON}.steps.jsonl seq 0); "
                     "state.md Session 1; summary.md `slug: shiny-canyon`"),
        _decl(1785989296311, "build", "", OPENCODE, CANYON, by_run=False,
              source=TRACE.format(sid=CANYON, seq="of the call at 2026-08-06T04:08:16Z",
                                  cmd='$tpl = "skill\\hfss-agent\\templates\\workspace"; $dst = '
                                      '"workspaces\\bowtie-3500-pilot"; New-Item ... (the template copy '
                                      'that created the workspace); state.md Session 2')),
        _decl(1785991540165, "solve", "", OPENCODE, CANYON, by_run=False,
              source=TRACE.format(sid=CANYON, seq="of the call at 2026-08-06T04:45:40Z",
                                  cmd="python src\\08_solve.py 2>&1 | Select-Object -Last 8 (the first "
                                      "solve submission); state.md Session 3")),
    ],
    "patch-2400": [
        _decl(1786756741592, "clarify", "", OPENCODE, ROCKET, by_run=False,
              source=f"the session's first step (results/state/trace/{ROCKET}.steps.jsonl seq 0); "
                     "state.md Session 1; summary.md `slug: kind-rocket`; opencode.json comment "
                     "(kind-rocket = patch-2400)"),
        _decl(1786757157667, "build", "", OPENCODE, ROCKET, by_run=False,
              source=TRACE.format(sid=ROCKET, seq="of the call at 2026-08-15T01:25:57Z",
                                  cmd='New-Item -ItemType Directory -Force -Path "workspaces\\patch-2400\\src" '
                                      '| Out-Null; Copy-Item ... (the template copy that created the '
                                      'workspace); state.md Session 2')),
        _decl(1786758015714, "solve", "", OPENCODE, ROCKET, by_run=False,
              source=TRACE.format(sid=ROCKET, seq="of the call at 2026-08-15T01:40:15Z",
                                  cmd="python src\\08_solve.py (the only solve submission); "
                                      "state.md Session 3")),
    ],
}


def lines(workspace_name):
    """The `sessions.jsonl` text for a workspace: one sorted-key JSON object per line."""
    return "".join(json.dumps(r, sort_keys=True) + "\n" for r in RECORDS[workspace_name])


def _write_if_changed(path, text):
    data = text.encode("utf-8")
    try:
        with open(path, "rb") as handle:
            if handle.read() == data:
                return False
    except OSError:
        pass
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    return True


def materialize(workspace_name, workspaces_dir, fixtures_root=HERE):
    """Copy the captured state files into the workspace where absent; return the names copied."""
    src_dir = os.path.join(fixtures_root, workspace_name, STATE_SUBDIR)
    dst_dir = os.path.join(workspaces_dir, workspace_name, "results", "state")
    copied = []
    if not os.path.isdir(src_dir):
        return copied
    os.makedirs(dst_dir, exist_ok=True)
    for name in sorted(os.listdir(src_dir)):
        if name == SESSIONS_FILE or not os.path.isfile(os.path.join(src_dir, name)):
            continue
        target = os.path.join(dst_dir, name)
        if os.path.exists(target):
            continue
        shutil.copyfile(os.path.join(src_dir, name), target)
        copied.append(name)
    return copied


def backfill(workspaces_dir=None, fixtures_root=HERE):
    """Write every workspace's lines to the fixture dir and the workspace; return a summary."""
    workspaces_dir = workspaces_dir or os.path.join(REPO, "workspaces")
    summary = {}
    for name in RECORDS:
        text = lines(name)
        fixture = os.path.join(fixtures_root, name, STATE_SUBDIR, SESSIONS_FILE)
        _write_if_changed(fixture, text)
        with open(os.path.join(fixtures_root, name, BACKFILL_INDEX), "w", encoding="utf-8") as handle:
            json.dump({"written": WRITTEN_ON, "lines": len(RECORDS[name]),
                       "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                       "note": __doc__.strip().splitlines()[0]}, handle, indent=2)
            handle.write("\n")
        copied = []
        if os.path.isdir(os.path.join(workspaces_dir, name)):
            _write_if_changed(os.path.join(workspaces_dir, name, "results", "state", SESSIONS_FILE), text)
            copied = materialize(name, workspaces_dir, fixtures_root)
        summary[name] = {"lines": len(RECORDS[name]), "materialized": copied}
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workspaces", help="workspaces dir to write into (default: this checkout's)")
    args = parser.parse_args(argv)
    summary = backfill(args.workspaces)
    parts = " ".join(f"{n}={s['lines']}" for n, s in summary.items())
    copied = sum(len(s["materialized"]) for s in summary.values())
    print(f"PASS: backfill sessions {parts} materialized={copied}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
