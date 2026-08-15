"""Capture real AEDT artifacts into the fixture corpus (ticket 03).

Both P0 bugs of 2026-08-14 passed a 72-test green suite because the
fixtures were hand-written and wrong in ways the author could not see:
real artifact *names* written as files where AEDT writes **directories**,
and a profile fixture with **unescaped** quotes where AEDT escapes them.
Green tests actively concealed two broken safety paths. This script
removes the guesswork by capturing the ground truth from workspaces that
actually solved on this box.

Two things are captured per case:

* **`tree.json`** — an entity-type-faithful manifest of the results tree.
  Every artifact of a class a parser cares about is recorded with its
  `type` (`file` or `dir`) and size, plus aggregate counts for everything
  else so total file/byte counters can be reproduced exactly.
  `real_fixtures.materialize()` rebuilds a real tree from it, creating a
  directory wherever AEDT created a directory. That is the device that
  makes the ticket-02 bug class impossible to reproduce by accident.

* **`profiles/*.profile`** — parse-faithful slices. Profiles run 112-448 KB,
  most of it `ProfileItem` detail rows no parser reads, so lines are kept
  only where they carry structure (`$begin`/`$end`), a group name, an
  elapsed time, or a terminal footnote. Escaping is preserved byte-for-byte.
  The slice is written **only if it parses identically to the original**,
  so a slice can never quietly drift from the artifact it stands for.

Expected parse results are computed from the FULL originals and recorded
in `meta.json`; the tests assert against those recorded values, so the
corpus pins behaviour rather than merely providing input.

Usage:
    python scripts/capture_fixtures.py            # recapture every known case
    python scripts/capture_fixtures.py --list     # show what would be captured
    python scripts/capture_fixtures.py <case> ... # recapture named cases

Rerunning with unchanged inputs is byte-stable (no timestamps in output).
"""

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "skill", "hfss-agent", "templates", "workspace", "src")
CORPUS = os.path.join(SRC, "fixtures", "real")

sys.path.insert(0, SRC)
import profile_evidence  # noqa: E402  (needs SRC on the path)

# Artifact classes any parser keys on. Order matters only for readability.
ARTIFACT_SUFFIXES = (".profile", ".imesh", ".cmesh", ".sd", ".su",
                     "_SU.txt", ".semaphore")
ARTIFACT_SUBSTRINGS = ("_ADP",)

# case name -> (workspace-relative results root, profiles worth slicing)
CASES = {
    "pilot-normal": (
        "workspaces/bowtie-3500-pilot/bowtie_3500_pilot.aedtresults",
        ["DV3019_S1911_V2586.profile", "DV2487_S1911_V0.profile"],
    ),
    "baseline-engine-error": (
        "workspaces/bowtie-3500/bowtie_3500.aedtresults",
        ["DV86_S83_V106.profile"],
    ),
    "bowtie-3670": (
        "workspaces/bowtie-3670/bowtie_3670.aedtresults",
        ["DV1602_S29_V1112.profile"],
    ),
}

_KEEP_MARKERS = ("$begin", "$end", "Name=", "Elapsed Time", "Status",
                 "Stop Time", "ProfileFootnote")


def is_artifact(name):
    """True when a tree entry belongs to a class a parser keys on."""
    if any(name.endswith(suffix) for suffix in ARTIFACT_SUFFIXES):
        return True
    return any(sub in name for sub in ARTIFACT_SUBSTRINGS)


def scan_tree(root):
    """Entity-type-faithful manifest of a results tree.

    Records artifact entries individually with their real `type`, and
    everything else only in aggregate — enough to reproduce total file and
    byte counters without copying a 5,000-file tree.
    """
    entries = []
    other_files = 0
    other_bytes = 0
    total_files = 0
    total_bytes = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for name in sorted(dirnames):
            if is_artifact(name):
                rel = os.path.relpath(os.path.join(dirpath, name), root)
                entries.append({"path": rel.replace(os.sep, "/"),
                                "type": "dir", "size": 0})
        for name in sorted(filenames):
            full = os.path.join(dirpath, name)
            try:
                size = os.path.getsize(full)
            except OSError:
                size = 0
            total_files += 1
            total_bytes += size
            if is_artifact(name):
                rel = os.path.relpath(full, root)
                entries.append({"path": rel.replace(os.sep, "/"),
                                "type": "file", "size": size})
            else:
                other_files += 1
                other_bytes += size
    entries.sort(key=lambda e: (e["path"], e["type"]))
    return {
        "entries": entries,
        "other_files": other_files,
        "other_bytes": other_bytes,
        "total_files": total_files,
        "total_bytes": total_bytes,
    }


def slice_profile(path):
    """Keep only the lines any profile parser reads; escaping untouched."""
    kept = []
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if any(marker in line for marker in _KEEP_MARKERS):
                kept.append(line.rstrip("\n"))
    return "\n".join(kept) + "\n"


def _expectation(path):
    stages, status, stop = profile_evidence.parse_profile(path)
    return {"status": status, "stop": stop,
            "stages": [list(stage) for stage in stages]}


def capture_case(name, results_rel, profile_names):
    """Capture one case; returns its meta dict. Raises on slice drift."""
    root = os.path.join(REPO, results_rel)
    if not os.path.isdir(root):
        raise SystemExit("capture aborted: no results tree at %s" % root)

    out_dir = os.path.join(CORPUS, name)
    prof_dir = os.path.join(out_dir, "profiles")
    os.makedirs(prof_dir, exist_ok=True)

    tree = scan_tree(root)
    with open(os.path.join(out_dir, "tree.json"), "w", encoding="utf-8") as handle:
        json.dump(tree, handle, indent=2, sort_keys=True)
        handle.write("\n")

    by_name = {}
    for full in profile_evidence.find_profiles(root):
        by_name[os.path.basename(full)] = full

    profiles = {}
    for profile_name in profile_names:
        original = by_name.get(profile_name)
        if original is None:
            raise SystemExit("capture aborted: %s not found under %s"
                             % (profile_name, root))
        expected = _expectation(original)
        text = slice_profile(original)
        dest = os.path.join(prof_dir, profile_name)
        with open(dest, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        # Fidelity gate: a slice that does not parse like its original is
        # not a fixture, it is a new bug. Refuse to keep it.
        if _expectation(dest) != expected:
            os.remove(dest)
            raise SystemExit(
                "capture aborted: slice of %s does not parse like the "
                "original — the keep-markers are wrong, not the artifact"
                % profile_name)
        profiles[profile_name] = expected

    meta = {
        "case": name,
        "source_results_root": results_rel,
        "profiles": profiles,
        "artifact_entries": len(tree["entries"]),
        "total_files": tree["total_files"],
    }
    with open(os.path.join(out_dir, "meta.json"), "w", encoding="utf-8") as handle:
        json.dump(meta, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return meta


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("cases", nargs="*", help="case names (default: all)")
    parser.add_argument("--list", action="store_true",
                        help="list known cases and their sources")
    args = parser.parse_args(argv)

    if args.list:
        for name, (rel, profiles) in sorted(CASES.items()):
            present = "present" if os.path.isdir(os.path.join(REPO, rel)) else "MISSING"
            print("%-24s %-58s %s  %s" % (name, rel, present, ", ".join(profiles)))
        return 0

    wanted = args.cases or sorted(CASES)
    unknown = [name for name in wanted if name not in CASES]
    if unknown:
        print("unknown case(s): %s" % ", ".join(unknown))
        return 2

    os.makedirs(CORPUS, exist_ok=True)
    captured = []
    for name in wanted:
        rel, profiles = CASES[name]
        meta = capture_case(name, rel, profiles)
        captured.append(name)
        print("captured %-24s artifacts=%-5d total_files=%-6d profiles=%d"
              % (name, meta["artifact_entries"], meta["total_files"],
                 len(meta["profiles"])))

    index = {"cases": sorted(captured)}
    with open(os.path.join(CORPUS, "index.json"), "w", encoding="utf-8") as handle:
        json.dump(index, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print("PASS: capture_fixtures cases=%d corpus=%s"
          % (len(captured), os.path.relpath(CORPUS, REPO).replace(os.sep, "/")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
