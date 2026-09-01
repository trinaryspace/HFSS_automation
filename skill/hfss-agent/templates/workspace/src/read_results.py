"""Scripted readout that works on pyAEDT 1.3.0 — the reader, in one place.

Every run so far wrote its own `09_plots.py` from scratch, and every one of them
judged fill-state with `data_real`. That attribute **does not exist in pyAEDT
1.3.0** (zero occurrences in the installed wheel), so the check reports
"unfilled SolutionData" *even on a perfectly good fetch* and any success is
discarded before it can be seen. Two pilots rediscovered that from scratch nine
days after it was diagnosed, because there was nowhere for the fix to live: the
template ships no plots stage, so the reader was reinvented per workspace.

This module is that missing home. Call shapes here are the ones validated on
this box against a solved project on 2026-08-07
(`workspaces/readout-route-around/summary.md`, evidence in its `evidence/`):

| shape | verdict on 1.3.0 |
|---|---|
| `data.data_real` / `data_imag` | **ABSENT** — never test fill-state with these |
| `data.full_matrix_real_imag` | exists, filled |
| `data.get_expression_data(expr, formula="real")` | exists, filled (touchstone parser uses it) |
| `data.primary_sweep_values` | exists |
| `post.export_report_to_file` | 102-line files, real values |
| `SolutionData.export_data_to_csv` | 101-row CSV |
| `hfss.results.get_solution_data` | **ABSENT** — `Hfss` has no `results` |

**The one-shot policy is the caller's, not this module's.** SKILL.md caps
scripted readout at one attempt plus one retry on a fresh process, then hands
the plot to the user and reports the signal as read from the UI — the pilot
tried eight shapes and ended the run. Nothing here loops; `read_expression`
returns a verdict and never retries at all, and `ReadoutSession` spends exactly
one escalation per run and then never again.

**The retry has to be a fresh PROCESS, and the verdict has to say which one
read the data.** patch-array-5800 (2026-08-18) solved cleanly, failed both of
its scripted readouts with `GrpcApiError` on `GetVariables` and `GetPropValue`
— generic desktop calls, the transport failure class — and wrote into the
playbook that scripted readouts are systematically impossible on this pairing.
Its own ledger records that earlier in the same run that exact error class on
that exact channel was cured by recycling the desktop. The retry could not have
falsified anything: it went through `ws_common.attach()`, which reconnects by
the pinned port and only re-pins when the bounded connect finds the desktop
*dead* — a degraded desktop still answers a TCP connect. Every retry landed on
the same sick process, and a hypothesis that was never tested got recorded as a
finding. `ReadoutSession` exists so that cannot happen again: it escalates to a
genuinely fresh process once, and it labels the outcome with which of the three
things actually happened (`ROUTE_*` / `VERDICTS` below).

Usage:
    import read_results, ws_common
    read_results.apply_route_arounds()          # before constructing Hfss
    sweep = read_results.resolve_sweep(hfss)    # never guess the auto-suffix
    freqs, values, note = read_results.read_expression(hfss, "dB(S(1,1))", sweep)

    # ... or with the one escalation wired in, which is the readout path:
    session = read_results.ReadoutSession(hfss, recycle=ws_common.recycle_desktop)
    s11 = session.read("dB(S(1,1))")
    read_results.write_readouts(ws_common.STATE,
                                [read_results.verdict_line("s11", s11)])
"""

import collections
import os

CANDIDATE_ACCESSORS = ("full_matrix_real_imag", "get_expression_data")

# The four things that can happen to a signal, and the only tokens allowed in
# `results/state/readouts.txt`. They are the whole scientific point of the
# escalation: without them a failed readout is indistinguishable from an
# untested one, which is precisely how "systematically broken over gRPC"
# reached the playbook on no evidence.
ROUTE_LIVE = "live-channel"        # read on the channel the run already had
ROUTE_FRESH = "fresh-process"      # read only after a fresh desktop process
ROUTE_BOTH_FAILED = "both-failed"  # failed on the live channel AND on a fresh one
ROUTE_UNTESTED = "untested"        # failed live, and no fresh process ever ran

VERDICTS = {
    ROUTE_LIVE: "OK on the live channel",
    ROUTE_FRESH: ("CHANNEL DEGRADATION CONFIRMED - the live channel could not read this "
                  "signal and a freshly launched desktop process could"),
    # Deliberately narrower than it used to be. This token once read
    # "SYSTEMATIC on this pyAEDT/AEDT pairing", which is more than two failures
    # can carry: environment-compat #6 records the same call working on the same
    # pairing on 2026-08-07, so "systematic on this pairing" cannot be inferred
    # from one project. The 2026-09-01 experiment then traced the real cause to
    # pyAEDT releasing its own session mid-read - not the transport at all - and
    # a verdict string that had already named the pairing would have sent the
    # reader past it. Name what was tried; leave the cause to the investigation.
    ROUTE_BOTH_FAILED: ("read failed on BOTH the live channel and a freshly launched "
                        "desktop process - so not the channel's age; cause is shared by "
                        "both processes (project, expression, or client) and is NOT "
                        "established by this run alone"),
    ROUTE_UNTESTED: ("HYPOTHESIS UNTESTED - the read failed on the live channel and no "
                     "fresh process ever ran, so nothing here says whether the channel "
                     "or the pairing is at fault"),
}

# `route` names the evidence class; `note` names exactly what was tried, in
# order, including the recycle's own account of itself.
Readout = collections.namedtuple("Readout", "x y route note")


def apply_route_arounds():
    """Alias the `HfssConstants` attribute pyAEDT 1.3.0 references but lacks.

    `HfssConstants` defines `solution_default`; `HFSSDesignSolution`'s
    solution_type getter/setter fallbacks and the base-class setter all
    reference `default_solution`, which does not exist. The mismatch ships in
    the current release and still pairs that way on pyaedt main.

    On the live box the normal open+readout path never hits it — with a design
    attached, `GetSolutionType()` works over gRPC. The trap fires only when
    `design_solutions` has no odesign or `GetSolutionType()` raises, i.e.
    exactly when the gRPC transport is flaking (EC#3). That is also exactly
    when a readout is being retried, so apply it defensively: it changes
    nothing on the working path.

    Verified live on this box, pyAEDT 1.3.0:

        HfssConstants.solution_default -> 'HFSS Terminal Network'
        HfssConstants.default_solution -> AttributeError

    Returns a **status string**, never a bool. An earlier version returned
    False both when the alias was unnecessary and when the import failed, and
    that conflation hid a wrong import path behind a confident "not needed" —
    the same shape as the `data_real` bug this module exists to kill. If a
    check can report healthy while doing nothing, it will.

    Status is one of: `installed`, `already-present`, `unavailable: <reason>`.
    """
    constants = None
    errors = []
    # Module path moved between versions; try the known homes in order.
    for module, name in (("ansys.aedt.core.generic.aedt_constants", "HfssConstants"),
                         ("ansys.aedt.core.application.design_solutions", "HfssConstants")):
        try:
            constants = getattr(__import__(module, fromlist=[name]), name)
            break
        except Exception as exc:                  # noqa: BLE001 - reported below
            errors.append(f"{module}: {type(exc).__name__}")
    if constants is None:
        return "unavailable: " + "; ".join(errors)
    if hasattr(constants, "default_solution"):
        return "already-present"
    fallback = getattr(constants, "solution_default", None)
    if fallback is None:
        return "unavailable: neither default_solution nor solution_default exists"
    constants.default_solution = fallback
    return "installed"


def resolve_sweep(hfss, setup="Setup1", prefer_sweep=True):
    """Return the real `"<setup> : <sweep>"` name, read back from the design.

    `create_linear_count_sweep` auto-suffixes the sweep name with a random
    tag (`Setup1 : Sweep_MM13NY`), so a hardcoded name misses (EC#6). Read it
    back rather than guessing. `prefer_sweep=False` selects the adaptive
    solution instead, which is a single point at the setup frequency.
    """
    names = list(getattr(hfss, "existing_analysis_sweeps", None) or [])
    if not names:
        return None
    scoped = [n for n in names if n.split(":")[0].strip() == setup] or names
    if prefer_sweep:
        for name in scoped:
            if "LastAdaptive" not in name:
                return name
    for name in scoped:
        if "LastAdaptive" in name:
            return name
    return scoped[0]


def is_filled(solution):
    """True when a SolutionData actually carries values.

    NEVER test `data_real` — absent on 1.3.0, so it reports unfilled on every
    good fetch. This checks the accessors that exist, and treats a present but
    empty sweep as unfilled.
    """
    if solution is None:
        return False
    sweep = getattr(solution, "primary_sweep_values", None)
    if not sweep:
        return False
    for name in CANDIDATE_ACCESSORS:
        if hasattr(solution, name):
            return True
    return False


def unfilled_reason(solution):
    """Why `is_filled` said no — phrased so a reader can act on it."""
    if solution is None:
        return "get_solution_data returned None"
    if not getattr(solution, "primary_sweep_values", None):
        return "no primary_sweep_values - solution not loaded for this sweep"
    return ("no usable accessor: expected one of "
            + ", ".join(CANDIDATE_ACCESSORS)
            + " (do NOT test data_real - absent on pyAEDT 1.3.0)")


def extract(solution, expression):
    """`(x_values, y_values)` from a filled SolutionData, 1.3.0 accessors only."""
    xs = list(getattr(solution, "primary_sweep_values", None) or [])
    getter = getattr(solution, "get_expression_data", None)
    if callable(getter):
        # A raising getter is the *expected* failure here, not an exotic one:
        # a partially functional gRPC channel is what Fault B looks like from
        # the client side (EC#3/EC#6). Fall through to the matrix rather than
        # letting it escape, or the fallback that exists never gets used.
        ys = []
        for call in (lambda: getter(expression, formula="real"),
                     lambda: getter(expression)):
            try:
                ys = list(call() or [])
            except Exception:                     # noqa: BLE001 - try the fallback
                continue
            if ys:
                break
        if ys:
            return xs, ys
    matrix = getattr(solution, "full_matrix_real_imag", None)
    if matrix:
        real = matrix[0] if isinstance(matrix, (list, tuple)) else matrix
        try:
            ys = list(real[expression])
            return xs, ys
        except (KeyError, TypeError, IndexError):
            pass
    return xs, []


def read_expression(hfss, expression, sweep=None, setup="Setup1"):
    """One scripted read. Returns `(x, y, note)`; never loops, never retries.

    `note` is always a sentence a human can act on. An empty `y` with a note is
    a *reportable* outcome — hand the plot to the user and report the signal as
    read from the UI, per SKILL.md. It is not an invitation to try shape nine.
    """
    if sweep is None:
        sweep = resolve_sweep(hfss, setup=setup)
    if sweep is None:
        return [], [], "no analysis sweeps on the design - nothing solved yet"
    try:
        solution = hfss.post.get_solution_data(expressions=expression,
                                               setup_sweep_name=sweep)
    except Exception as exc:                      # noqa: BLE001 - reported, not raised
        return [], [], f"get_solution_data raised on '{sweep}': {type(exc).__name__}: {exc}"
    if not is_filled(solution):
        return [], [], f"unfilled on '{sweep}': {unfilled_reason(solution)}"
    xs, ys = extract(solution, expression)
    if not ys:
        return xs, [], (f"filled on '{sweep}' but '{expression}' did not extract - "
                        "check the expression spelling against the report")
    return xs, ys, f"read {len(ys)} points from '{sweep}'"


class ReadoutSession:
    """A run's scripted readouts, with exactly ONE escalation to spend.

    Construct it once per readout stage around the attached design, hand it
    `recycle` (`ws_common.recycle_desktop`, or any callable returning
    `(hfss, note)` — injectable so this module still imports no pyAEDT), and
    read every signal through `read`. It holds the desktop it is reading
    through, so once the escalation is spent the remaining signals go to the
    fresh process rather than each paying for another launch.

    The escalation budget is one per RUN, not one per signal. That is the
    one-shot policy read literally: a readout stage may launch at most one
    replacement desktop, and it is spent even when it fails, so no failure
    mode can turn this into a loop. A fresh desktop costs a minute; eight of
    them is the pilot's shape-hunting failure wearing a different hat.

    What each read reports:

        ROUTE_LIVE         the signal came back on the channel the run had.
        ROUTE_FRESH        the live channel failed and a fresh process read
                           the same signal — the channel-lifetime hypothesis
                           CONFIRMED for this pairing. (Also the route for a
                           signal read after an earlier signal spent the
                           escalation; the note says which.)
        ROUTE_BOTH_FAILED  a fresh process failed too. THIS, and only this, is
                           evidence that the readout API is systematically
                           unavailable on the pairing.
        ROUTE_UNTESTED     the live channel failed and no fresh process ever
                           ran — no recycler was wired, or the recycle raised
                           (this signal's, or an earlier signal's, which
                           spends the budget without producing a desktop).
                           Never write this up as a pairing verdict: it is
                           the outcome that says the question is still open,
                           and recording it as anything else is the mistake
                           this class was built to prevent.
    """

    def __init__(self, hfss, recycle=None):
        self.hfss = hfss
        self._recycle = recycle
        # `escalated` is the BUDGET (spent even by a recycle that raised);
        # `on_fresh_process` is the FACT (a replacement desktop actually came
        # up). Conflating the two is how a run claims "failed on a fresh
        # process too" about a process that never existed — the same
        # untested-hypothesis-as-finding move this class exists to stop, and
        # it appeared here first as a two-line bug.
        self.escalated = False
        self.on_fresh_process = False
        self.recycle_note = None

    def read(self, expression, sweep=None, setup="Setup1"):
        """One signal, at most one escalation. Returns a `Readout`."""
        xs, ys, note = read_expression(self.hfss, expression, sweep=sweep, setup=setup)
        if ys:
            if not self.on_fresh_process:
                return Readout(xs, ys, ROUTE_LIVE, note)
            return Readout(xs, ys, ROUTE_FRESH,
                           "read on the recycled desktop (this run's one escalation was "
                           "already spent on an earlier signal): %s" % note)
        if self.on_fresh_process:
            # The live channel is not what failed here — this signal was only
            # ever asked of the replacement desktop. Same evidence class as a
            # both-failed read; the note keeps the distinction honest.
            return Readout(xs, [], ROUTE_BOTH_FAILED,
                           "fresh process (the escalation was spent on an earlier signal, "
                           "so this signal was only ever tried on the recycled desktop): %s"
                           % note)
        if self.escalated:
            # Budget spent on a recycle that never produced a desktop. No
            # fresh process has ever read anything in this run, so nothing
            # here may be reported as a verdict on the pairing.
            return Readout(xs, [], ROUTE_UNTESTED,
                           "live channel: %s; this run's one escalation was already spent "
                           "on a recycle that failed (%s), so no fresh process has ever "
                           "been asked" % (note, self.recycle_note))
        if self._recycle is None:
            return Readout(xs, [], ROUTE_UNTESTED,
                           "live channel: %s; no fresh-process escalation was wired into "
                           "this readout, so nothing tested whether the channel or the "
                           "pairing is at fault" % note)
        self.escalated = True  # spent before the attempt: a failed recycle is still spent
        try:
            fresh, self.recycle_note = self._recycle()
        except Exception as exc:                  # noqa: BLE001 - reported, not raised
            self.recycle_note = "%s: %s" % (type(exc).__name__, exc)
            return Readout(xs, [], ROUTE_UNTESTED,
                           "live channel: %s; the escalation to a fresh process itself "
                           "failed (%s), so the channel-lifetime question is still open"
                           % (note, self.recycle_note))
        self.hfss = fresh
        self.on_fresh_process = True
        fresh_xs, fresh_ys, fresh_note = read_expression(fresh, expression, sweep=sweep,
                                                         setup=setup)
        trail = "live channel: %s; %s; fresh process: %s" % (note, self.recycle_note,
                                                             fresh_note)
        if fresh_ys:
            return Readout(fresh_xs, fresh_ys, ROUTE_FRESH, trail)
        return Readout(fresh_xs, [], ROUTE_BOTH_FAILED, trail)


def verdict_line(signal, readout):
    """The one line `results/state/readouts.txt` carries for a signal.

    Fixed shape, so a later session can grep the verdict instead of reading
    prose: `<signal>: route=<token> <verdict> | <what was tried>`.
    """
    return "%s: route=%s %s | %s" % (signal, readout.route,
                                     VERDICTS[readout.route], readout.note)


def write_readouts(state_dir, lines):
    """Write the run's readout verdicts to `<state_dir>/readouts.txt`.

    One home for the file, because the verdict is evidence: the run that
    reported "scripted readouts fail systematically over this pairing"
    wrote that sentence into the playbook from two lines in this file, and
    the lines did not record which desktop process had been asked.
    """
    os.makedirs(state_dir, exist_ok=True)
    path = os.path.join(state_dir, "readouts.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    for line in lines:
        print(line, flush=True)
    return path


def export_fallback(hfss, expression, path, sweep=None, setup="Setup1"):
    """Write the data to disk when the in-process read fails.

    Both shapes are validated on this box. An export that lands is a delivered
    artifact even when `get_solution_data` will not fill, which matters because
    the solve session's Done condition requires the plots on disk — the run
    that skipped this delivered a number transcribed by hand, and the first
    transcription was wrong.
    """
    if sweep is None:
        sweep = resolve_sweep(hfss, setup=setup)
    if sweep is None:
        return None, "no analysis sweeps on the design"
    try:
        report = hfss.post.create_report(expressions=expression,
                                         setup_sweep_name=sweep)
    except Exception as exc:                      # noqa: BLE001
        return None, f"create_report failed: {type(exc).__name__}: {exc}"
    try:
        hfss.post.export_report_to_file(os.path.dirname(path),
                                        getattr(report, "plot_name", "Plot 1"),
                                        ".csv")
        return path, f"exported via export_report_to_file from '{sweep}'"
    except Exception as exc:                      # noqa: BLE001
        return None, f"export_report_to_file failed: {type(exc).__name__}: {exc}"


if __name__ == "__main__":
    # Print the status verbatim. The earlier line read
    # `'installed' if status else 'not-needed'`, and every one of the three
    # status strings is truthy — including `unavailable: ...` — so the check
    # reported "installed" while doing nothing. That is the exact conflation
    # `apply_route_arounds` returns a string to avoid.
    print(f"PASS: read_results route_around={apply_route_arounds()} "
          f"accessors={','.join(CANDIDATE_ACCESSORS)} "
          f"routes={','.join(sorted(VERDICTS))}")
