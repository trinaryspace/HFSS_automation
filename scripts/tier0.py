"""Tier 0: everything verifiable with no AEDT, no license, no desktop.

The pilot found five real template bugs, and it found them by replaying
eight staged scripts on a second desktop at roughly eight minutes a go.
Two more bugs (the banking regex and the watchdog's directory families)
were not found at all, because the only fast tests in the repo ran against
hand-written fixtures that did not match reality. Tier 0 is the answer to
both: it runs in seconds, it needs no license, and it reads its ground
truth from artifacts captured off this box.

What runs here:

  * the runner suites at the no-AEDT seams (`test_template_runners`,
    `test_poll_solve_stages`) — including the corpus-driven checks
  * the measurement harness tests (`test_run_card`)
  * the skill-text markers (`verify_skill`)
  * the KB checks (`verify_kb`)
  * the static gate over the template `src/` (py_compile + import)
  * a corpus presence check, so a missing fixture corpus fails loudly
    instead of quietly turning the real-artifact tests into no-ops

Everything prints one machine-parseable summary line in the house format:
`PASS: tier0 suites=N failed=0` or `FAIL: tier0 ...`.

Usage:
    python scripts/tier0.py            # everything
    python scripts/tier0.py --list     # show the suites without running
    python scripts/tier0.py -v         # stream each suite's own output
"""

import argparse
import os
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "skill", "hfss-agent", "templates", "workspace", "src")

# (label, argv) — every entry must exit 0 and must not need AEDT.
SUITES = [
    ("template-runners", [sys.executable, os.path.join(SRC, "test_template_runners.py")]),
    ("watchdog-stages", [sys.executable, os.path.join(SRC, "test_poll_solve_stages.py")]),
    # The readout reader. Offline by construction: it never imports pyAEDT, so
    # the fill-state regression that survived two pilots is now caught in
    # milliseconds instead of after a solve.
    ("readout", [sys.executable, os.path.join(SRC, "test_read_results.py")]),
    ("run-card", [sys.executable, os.path.join(REPO, "scripts", "test_run_card.py")]),
    ("static-gate", [sys.executable, os.path.join(SRC, "00_static_gate.py")]),
    ("skill-markers", [sys.executable, os.path.join(REPO, "skill", "hfss-agent", "verify_skill.py")]),
    ("kb-checks", [sys.executable, os.path.join(REPO, "scraping", "verify_kb.py")]),
    ("skill-install", [sys.executable, os.path.join(REPO, "scripts", "install_skill.py"),
                       "--check"]),
    # Phase 2: schema, validator, reducer and the compiler's golden call
    # sequences against a recorder. The whole point of the bet is that the
    # build path becomes checkable without license-hours, so it belongs here.
    ("design-spec", [sys.executable, os.path.join(REPO, "hfss_spec", "test_hfss_spec.py")]),
    # Relational checks (clearance, port geometry) — the two rules written
    # against the 2026-08-17 review, where three of six machine-clean specs
    # were wrong and no existing check could see any of it.
    ("model-checks", [sys.executable, os.path.join(REPO, "hfss_spec", "test_model_checks.py")]),
    # The session boundary (ticket 14): a clarify session cannot reach a licence
    # or a solver. Written against cell S11, which spent 51 minutes writing a
    # field solver inside a Clarification block.
    ("session", [sys.executable, os.path.join(REPO, "hfss_spec", "test_session.py")]),
    ("canonical-specs", [sys.executable, os.path.join(REPO, "scripts", "validate_cases.py")]),
]


def check_corpus():
    """The real-artifact corpus must exist, or the tests that matter are inert."""
    sys.path.insert(0, SRC)
    try:
        import real_fixtures
    except ImportError as exc:
        return False, "cannot import real_fixtures: %s" % exc
    if not real_fixtures.available():
        return False, ("fixture corpus missing at %s — regenerate with "
                       "`python scripts/capture_fixtures.py`"
                       % os.path.relpath(real_fixtures.FIXTURES_DIR, REPO))
    try:
        cases = real_fixtures.cases()
    except Exception as exc:  # noqa: BLE001 - report, never mask
        return False, "corpus unreadable: %s" % exc
    if not cases:
        return False, "fixture corpus is empty"
    return True, "%d case(s): %s" % (len(cases), ", ".join(cases))


def run_suite(label, argv, verbose=False):
    started = time.time()
    proc = subprocess.run(argv, cwd=REPO, capture_output=True, text=True)
    elapsed = time.time() - started
    ok = proc.returncode == 0
    if verbose or not ok:
        tail = (proc.stdout or "") + (proc.stderr or "")
        for line in tail.strip().splitlines()[-25:]:
            print("    | %s" % line)
    print("  %-18s %-5s %5.1fs" % (label, "ok" if ok else "FAIL", elapsed))
    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--list", action="store_true", help="list suites and exit")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="stream each suite's own output")
    args = parser.parse_args(argv)

    if args.list:
        print("corpus-check")
        for label, _ in SUITES:
            print(label)
        return 0

    started = time.time()
    ok, detail = check_corpus()
    print("  %-18s %-5s        %s" % ("corpus-check", "ok" if ok else "FAIL", detail))
    failed = [] if ok else ["corpus-check"]

    for label, suite_argv in SUITES:
        if not run_suite(label, suite_argv, verbose=args.verbose):
            failed.append(label)

    elapsed = time.time() - started
    total = len(SUITES) + 1
    if failed:
        print("FAIL: tier0 suites=%d failed=%d (%s) elapsed=%.1fs"
              % (total, len(failed), ", ".join(failed), elapsed))
        return 1
    print("PASS: tier0 suites=%d failed=0 elapsed=%.1fs" % (total, elapsed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
