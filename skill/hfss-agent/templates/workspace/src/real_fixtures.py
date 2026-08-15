"""Loader for the real-artifact fixture corpus (ticket 03).

The corpus under `src/fixtures/real/` is captured from workspaces that
actually solved on this box (`scripts/capture_fixtures.py`). This module
is how tests consume it. Its one important job is `materialize()`, which
rebuilds a results tree from a captured manifest **creating a directory
wherever AEDT created a directory** — `.imesh`, `.cmesh` and `_ADP*`
artifacts are directories on this box, and writing them as files is
exactly what let the ticket-02 watchdog bug pass a green suite.

The corpus travels with the workspace template, so a workspace copy can
verify itself. A missing corpus is an error, never a silent skip: tests
that quietly pass when their ground truth is absent are how both P0 bugs
survived.

Stdlib only; no pyAEDT, no side effects on import.
"""

import json
import os

FIXTURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "fixtures", "real")

_FILLER_DIR = "_filler"


class FixtureCorpusMissing(RuntimeError):
    """Raised when the corpus is absent — never swallowed into a skip."""


def _require(path, what):
    if not os.path.exists(path):
        raise FixtureCorpusMissing(
            "real-artifact fixture corpus missing (%s at %s). Regenerate it "
            "with `python scripts/capture_fixtures.py` from a repo checkout "
            "that still has the solved workspaces." % (what, path))
    return path


def available():
    """True when the corpus is present and has an index."""
    return os.path.isfile(os.path.join(FIXTURES_DIR, "index.json"))


def cases():
    """Captured case names, sorted."""
    index_path = _require(os.path.join(FIXTURES_DIR, "index.json"), "index.json")
    with open(index_path, encoding="utf-8") as handle:
        return sorted(json.load(handle).get("cases", []))


def case_dir(case):
    return _require(os.path.join(FIXTURES_DIR, case), "case %r" % case)


def meta(case):
    """The case's recorded expectations (parse results from the originals)."""
    path = _require(os.path.join(case_dir(case), "meta.json"), "meta.json")
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def tree(case):
    """The case's entity-type-faithful tree manifest."""
    path = _require(os.path.join(case_dir(case), "tree.json"), "tree.json")
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def profile_path(case, name):
    """Path to a captured (sliced, parse-faithful) profile."""
    return _require(os.path.join(case_dir(case), "profiles", name),
                    "profile %r" % name)


def profile_names(case):
    return sorted(meta(case).get("profiles", {}))


def materialize(case, dest, include_profiles=True):
    """Rebuild the captured results tree under `dest`; returns `dest`.

    Artifact entries are created with their recorded type — **directories
    stay directories** — and their recorded size. Everything else is
    reproduced in aggregate under `_filler/` so that total file and byte
    counters match the real tree exactly, which is what makes growth and
    settle logic testable without a 5,000-file copy.
    """
    manifest = tree(case)
    os.makedirs(dest, exist_ok=True)

    captured_profiles = set(profile_names(case)) if include_profiles else set()

    for entry in manifest["entries"]:
        target = os.path.join(dest, entry["path"].replace("/", os.sep))
        os.makedirs(os.path.dirname(target), exist_ok=True)
        if entry["type"] == "dir":
            os.makedirs(target, exist_ok=True)
            continue
        base = os.path.basename(target)
        if base in captured_profiles:
            with open(profile_path(case, base), encoding="utf-8") as handle:
                body = handle.read()
            with open(target, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(body)
            continue
        with open(target, "wb") as handle:
            if entry["size"]:
                handle.write(b"\0" * entry["size"])

    filler_root = os.path.join(dest, _FILLER_DIR)
    other_files = manifest.get("other_files", 0)
    other_bytes = manifest.get("other_bytes", 0)
    if other_files:
        os.makedirs(filler_root, exist_ok=True)
        for index in range(other_files):
            payload = other_bytes if index == 0 else 0
            with open(os.path.join(filler_root, "f%05d.bin" % index), "wb") as handle:
                if payload:
                    handle.write(b"\0" * payload)
    return dest


def expected_totals(case):
    """`(total_files, total_bytes)` recorded from the real tree.

    `materialize()` reproduces these exactly, minus the profile slices,
    which are smaller than the originals by design — callers comparing
    byte totals should compare against a materialized tree, not these.
    """
    manifest = tree(case)
    return manifest["total_files"], manifest["total_bytes"]
