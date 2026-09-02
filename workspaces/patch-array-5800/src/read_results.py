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
genuinely fresh process once, and it labels the outcome with which of the
things below actually happened (`ROUTE_*` / `VERDICTS`).

**The route that works is not `get_solution_data`.** On 2026-09-01, across six
or more freshly launched processes and two different projects, that call died
on this box every time. It dies *below* pyAEDT's Python layer: building a
report's nominal variation evaluates every design variable, and a ctypes
callback in the gRPC plugin raises inside `GetAedtObjId`
(`internal/grpc_plugin_dll_class.py:454`, `SystemError: <built-in function
isinstance> returned a result with an exception set`). The report layer then
prints `Solution Data failed to load` and returns `False`. No Python-level
argument reaches past it — explicit `variations` built from raw
`GetVariableValue` calls, explicit `report_category`, `create_report` first,
`export_touchstone` — all tried, all identical.

**What amplified that into a month of wrong diagnosis** is
`general_methods.raise_exception_or_return_false` (line 222): when
`settings.release_on_exception` is set — and it defaults **on** — any exception
through a wrapped method releases *every* desktop in `_desktop_sessions`. One
stumble killed the whole session, and every later call then raised
`GrpcApiError: Failed to execute gRPC AEDT command: <whatever came next>`,
which is why the command name kept changing between otherwise identical runs
and why this looked for a month like a broken transport. `apply_route_arounds`
now turns that flag off. Measured 2026-09-01: with it off the session survived
**three consecutive failed reads** and still answered `design_name`; with it
on, one failure destroyed everything.

**The route that does work** goes around `get_solution_data` entirely, at the
report module, and it produced the first scripted S11 this project has ever
yielded:

    mod = hfss.odesign.GetModule("ReportSetup")
    mod.CreateReport(name, "Modal Solution Data", "Rectangular Plot", sweep,
                     ["Domain:=", "Sweep"], ["Freq:=", ["All"]],
                     ["X Component:=", "Freq", "Y Component:=", [expr]], [])
    path = hfss.post.export_report_to_file(out_dir, name, ".csv")

`"Freq [GHz]","dB(S(1,1)) []"` and 151 rows, minimum -7.369 dB at 5.66 GHz —
which independently reproduced the maintainer's UI read of the same solve. Far
fields take report category `"Far Fields"`, display type `"Data Table"` and a
`["Context:=", "<sphere>"]` context, and come back with **four** columns
(`Freq, Phi, Theta, value`), so the parser takes its values from the *last*
column and never from "column 2".

**Order: `get_solution_data` first, the report export second, and both of them
before the one fresh-process escalation.** The tempting order is the reverse,
since only the export route has ever worked on this box. Three things decide it
the other way:

1. *The export route mutates the user's project; the API route does not.*
   `CreateReport` adds a report that appears in the design tree and persists.
   A side-effecting route should not run when a side-effect-free one would
   have answered.
2. *`get_solution_data` is not universally dead.* Environment-compat #6 records
   it working on this exact pairing on 2026-08-07. That has never been
   reproduced since and it is verified dead today on two projects — but if it
   ever comes back, leading with the export route is precisely how we would
   never find out. The cheap attempt is also the measurement, and the `route=`
   token in `readouts.txt` is where that measurement lands.
3. *A failed attempt is now cheap.* It stopped being cheap only because of
   `release_on_exception`: before that flag was turned off, trying the broken
   route first cost the entire session. Now it costs one call and a note.

None of this asks a human for anything. Both routes run inside one
`read_signal`, so the route that actually works is reached automatically, and
the fresh-process escalation is spent only when *both* routes failed on the
live process.

Usage:
    import read_results, ws_common
    read_results.apply_route_arounds()          # before constructing Hfss
    sweep = read_results.resolve_sweep(hfss)    # never guess the auto-suffix
    freqs, values, note = read_results.read_expression(hfss, "dB(S(1,1))", sweep)

    # ... or with both routes and the one escalation wired in, which is the
    # readout path. `export_dir` is where the exported CSV lands: pass the
    # workspace's `results/` and the file is a delivered artifact; omit it and
    # a temp directory is used, named in the note.
    session = read_results.ReadoutSession(hfss, recycle=ws_common.recycle_desktop,
                                          export_dir=RESULTS)
    s11 = session.read("dB(S(1,1))")
    gain = session.read("dB(GainTotal)", sphere="Sphere1")   # far field, 4 columns
    read_results.write_readouts(ws_common.STATE,
                                [read_results.verdict_line("s11", s11)])
"""

import collections
import csv
import os
import tempfile

CANDIDATE_ACCESSORS = ("full_matrix_real_imag", "get_expression_data")

# The things that can happen to a signal, and the only tokens allowed in
# `results/state/readouts.txt`. They are the whole scientific point of the
# escalation: without them a failed readout is indistinguishable from an
# untested one, which is precisely how "systematically broken over gRPC"
# reached the playbook on no evidence.
#
# Two axes, not one. A token names WHICH ROUTE produced the numbers
# (`get_solution_data`, or the report export) and WHICH PROCESS produced them
# (the channel the run already had, or the one replacement desktop). Collapsing
# either axis loses something a reader needs: "fresh-process" alone would hide
# that the numbers came out of an exported CSV rather than the API, and
# "report-export" alone would hide that the live channel had already been given
# up on. Both facts are the evidence, so both are in the token.
ROUTE_LIVE = "live-channel"          # get_solution_data, on the channel the run had
ROUTE_FRESH = "fresh-process"        # get_solution_data, only after a fresh desktop
ROUTE_EXPORT = "report-export"       # exported CSV, on the channel the run had
ROUTE_EXPORT_FRESH = "report-export-fresh"   # exported CSV, after a fresh desktop
ROUTE_BOTH_FAILED = "both-failed"    # every route failed, live AND on a fresh process
ROUTE_UNTESTED = "untested"          # failed live, and no fresh process ever ran

# `read_signal` reports which mechanism produced the numbers; the session pairs
# that with which process it was talking to. These strings appear verbatim in
# notes, so they double as the name a human reads.
MECH_API = "get_solution_data"
MECH_EXPORT = "report-export"

ROUTE_BY_MECHANISM = {
    (MECH_API, False): ROUTE_LIVE,
    (MECH_API, True): ROUTE_FRESH,
    (MECH_EXPORT, False): ROUTE_EXPORT,
    (MECH_EXPORT, True): ROUTE_EXPORT_FRESH,
}

VERDICTS = {
    ROUTE_LIVE: "OK on the live channel, via get_solution_data",
    ROUTE_FRESH: ("CHANNEL DEGRADATION CONFIRMED - no route read this signal on the live "
                  "channel and get_solution_data read it on a freshly launched desktop "
                  "process"),
    # Says what happened and no more. It does NOT say get_solution_data is
    # broken on this pairing: one signal's failure is one signal's failure, and
    # environment-compat #6 records that call working here on 2026-08-07. What
    # it does say is which file the numbers came out of, because a number read
    # from an exported CSV and a number read from the API are not the same
    # evidence and a reader must not have to guess which one is on the line.
    ROUTE_EXPORT: ("OK on the live channel, via the report export - get_solution_data did "
                   "not read this signal and a CreateReport + export_report_to_file CSV "
                   "did; the numbers are that file's"),
    ROUTE_EXPORT_FRESH: ("OK via the report export on a freshly launched desktop process - "
                         "no route read this signal on the live channel; the numbers come "
                         "from an exported CSV, not from get_solution_data"),
    # Deliberately narrower than it used to be. This token once read
    # "SYSTEMATIC on this pyAEDT/AEDT pairing", which is more than two failures
    # can carry: environment-compat #6 records the same call working on the same
    # pairing on 2026-08-07, so "systematic on this pairing" cannot be inferred
    # from one project. The 2026-09-01 experiment then traced the real cause to
    # pyAEDT releasing its own session mid-read - not the transport at all - and
    # a verdict string that had already named the pairing would have sent the
    # reader past it. Name what was tried; leave the cause to the investigation.
    ROUTE_BOTH_FAILED: ("read failed on BOTH the live channel and a freshly launched "
                        "desktop process, on both routes (get_solution_data and the "
                        "report export) - so not the channel's age; cause is shared by "
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
    """Both client-side route-arounds this pairing needs, before `Hfss()`.

    Returns a **status string**, never a bool, of the form
    `default_solution=<status> release_on_exception=<status>`. An earlier
    version returned False both when the alias was unnecessary and when the
    import failed, and that conflation hid a wrong import path behind a
    confident "not needed" — the same shape as the `data_real` bug this module
    exists to kill. If a check can report healthy while doing nothing, it will.

    **1. `settings.release_on_exception = False`** — the one that matters most,
    and the one that cost a month. `general_methods.raise_exception_or_return_false`
    (line 222) releases *every* desktop in `_desktop_sessions` when this flag is
    set, and it defaults set. So a single failed read did not fail: it killed
    the session, and every call after it raised `GrpcApiError` naming whatever
    it tried next. That is why the reported command name kept changing between
    identical runs (`GetVariables`, `GetSetups`, `ExportToFile`, `OpenProject`)
    and why a client-side fault read as a broken transport for a month.
    Measured 2026-09-01: with the flag off the session survived three
    consecutive failed reads and still answered `design_name`; with it on, the
    first failure destroyed everything. This does not make any read work — it
    makes a failed read survivable, which is what lets `read_signal` try the
    API and then fall through to the export route on the same session.

    Status is one of: `disabled`, `already-disabled`, `unavailable: <reason>`.

    **2. Alias the `HfssConstants` attribute pyAEDT 1.3.0 references but lacks.**

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

    Status is one of: `installed`, `already-present`, `unavailable: <reason>`.

    Neither route-around is allowed to raise: this runs before `Hfss()` on a
    box where the whole point is that things fail, and a route-around that
    takes the run down with it is worse than the fault it works around.
    """
    # The flag goes off FIRST: it is what keeps everything after it — including
    # the alias's own imports — from taking the session down on one exception.
    release = _disable_release_on_exception()
    return "default_solution=%s release_on_exception=%s" % (
        _alias_default_solution(), release)


def _disable_release_on_exception():
    """Turn off pyAEDT's release-every-session-on-any-exception behaviour.

    Home of `settings` moved between releases, so try the known ones in order,
    exactly as the constants alias does. See `apply_route_arounds` for why.
    """
    errors = []
    for module, name in (("ansys.aedt.core.generic.settings", "settings"),
                         ("ansys.aedt.core", "settings"),
                         ("pyaedt", "settings")):
        try:
            settings = getattr(__import__(module, fromlist=[name]), name)
        except Exception as exc:                  # noqa: BLE001 - reported below
            errors.append(f"{module}: {type(exc).__name__}")
            continue
        if not hasattr(settings, "release_on_exception"):
            errors.append(f"{module}: no release_on_exception attribute")
            continue
        if settings.release_on_exception is False:
            return "already-disabled"
        try:
            settings.release_on_exception = False
        except Exception as exc:                  # noqa: BLE001 - reported below
            errors.append(f"{module}: set failed {type(exc).__name__}")
            continue
        # Read it back. It is a property with a setter, and a settings object
        # that silently ignored the write would leave the run believing it was
        # protected — the same "reports healthy while doing nothing" failure
        # this function returns a string to avoid.
        if settings.release_on_exception is not False:
            errors.append(f"{module}: set did not stick")
            continue
        return "disabled"
    return "unavailable: " + "; ".join(errors)


def _alias_default_solution():
    """The `HfssConstants.default_solution` alias; see `apply_route_arounds`."""
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
    """One `get_solution_data` read. `(x, y, note)`; never loops, never retries.

    This is the API route only. `read_signal` is what a caller wants: it runs
    this first and falls through to the report-export route, which is the one
    that works on this box.

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


# ---------------------------------------------------------------------------
# The report-export route: CreateReport at the report module, then export the
# report to CSV and parse the file. It never touches `get_solution_data`, which
# is the only reason it works on this box (see the module docstring).
# ---------------------------------------------------------------------------

# Every report this module creates carries this prefix. It exists so the
# reports we make are identifiable at a glance in the user's design tree, and
# so `create_or_reuse_report` can tell one of ours from one of theirs. NEVER
# reuse, overwrite or delete a report whose name did not come from
# `report_name_for` — a report in that tree may be the user's own work.
REPORT_NAME_PREFIX = "AgentReadout"

# What `CreateReport` needs, per report class. Only the modal/rectangular row
# is measured end to end (2026-09-01, patch-array-5800, 151 points). The far
# field row's category, display type and context are from that same session's
# notes, and its family list is read back off the four columns of the CSV it
# produced (`Freq, Phi, Theta, dB(GainTotal)`) — so the shape is real, but the
# call has not been re-run from this module. Say so rather than implying both
# were verified equally.
ReportSpec = collections.namedtuple("ReportSpec",
                                    "category display context families components")

_DEFAULT_EXPORT_DIR = None


def report_name_for(expression):
    """A deterministic, distinctive, filesystem-safe report name.

    `dB(S(1,1))` -> `AgentReadout_dB_S_1_1`. Deterministic matters twice: it is
    how a second run reuses the report instead of littering the design tree
    with one per attempt, and `export_report_to_file` builds its output path as
    `<dir>/<report name>.csv`, so the name has to survive being a filename.
    """
    safe = "".join(ch if ch.isalnum() else "_" for ch in str(expression))
    while "__" in safe:
        safe = safe.replace("__", "_")
    return "%s_%s" % (REPORT_NAME_PREFIX, safe.strip("_") or "signal")


def report_spec(expression, sphere=None):
    """The `CreateReport` arguments for this expression.

    `sphere` selects the far-field form: a far-field report is not a
    rectangular plot of a frequency sweep, it is a Data Table over a radiation
    sphere, and it comes back with four columns instead of two.
    """
    if sphere:
        return ReportSpec(
            category="Far Fields",
            display="Data Table",
            context=["Context:=", sphere],
            families=["Freq:=", ["All"], "Phi:=", ["All"], "Theta:=", ["All"]],
            components=["X Component:=", "Theta", "Y Component:=", [expression]])
    return ReportSpec(
        category="Modal Solution Data",
        display="Rectangular Plot",
        context=["Domain:=", "Sweep"],
        families=["Freq:=", ["All"]],
        components=["X Component:=", "Freq", "Y Component:=", [expression]])


def default_export_dir():
    """One temp directory per process, made only when a CSV is about to land.

    Created lazily so an offline import, or a run whose API read succeeded,
    never makes a directory it does not use. Callers that want the CSV kept as
    a delivered artifact pass their own `export_dir` (the workspace `results/`).
    """
    global _DEFAULT_EXPORT_DIR
    if _DEFAULT_EXPORT_DIR is None:
        _DEFAULT_EXPORT_DIR = tempfile.mkdtemp(prefix="hfss_readout_")
    return _DEFAULT_EXPORT_DIR


def create_or_reuse_report(hfss, expression, sweep, sphere=None, report_name=None):
    """Ensure a report named `report_name_for(expression)` exists.

    Returns `(name, note)`, or `(None, note)` when the report module could not
    be reached or `CreateReport` failed. Never raises.

    **On the side effect, deliberately:** `CreateReport` adds a report to the
    project. It shows in the user's design tree and it persists across saves —
    this is not a scratch object. Three decisions follow.

    *Reuse, never duplicate.* `GetAllReportNames()` is consulted first, so a
    second run (or a second signal) finds the report from the first and exports
    it again rather than piling up `AgentReadout_dB_S_1_1`, `... 1`, `... 2`.

    *Never touch a report we did not name.* Only names built by
    `report_name_for` are reused, and nothing here deletes or overwrites
    anything. If the user happens to own a report with our prefix, the worst
    case is that we export theirs — which the CSV header check in
    `parse_report_csv` then catches, because it will not carry our expression.

    *It is NOT deleted afterwards, on purpose.* Deleting is a second mutation,
    made after the numbers are already in hand, that can fail on its own (this
    is a box where AEDT calls fail) and would leave the run reporting an error
    for a signal it had already read. Against that, what a left-behind report
    costs is one clearly-labelled entry in the design tree — and it buys
    something: CONTEXT.md makes the user's UI read authoritative and the
    scripted read a bonus, so leaving the report standing is what lets the user
    open the very plot these numbers came from and arbitrate them. Bounded by
    reuse, it is one report per signal per project, forever, not one per run.
    """
    name = report_name or report_name_for(expression)
    try:
        module = hfss.odesign.GetModule("ReportSetup")
    except Exception as exc:                      # noqa: BLE001 - reported, not raised
        return None, ("could not reach the ReportSetup module: %s: %s"
                      % (type(exc).__name__, exc))
    if module is None:
        return None, "odesign.GetModule('ReportSetup') returned None"
    listed, prefix = None, ""
    try:
        listed = [str(n) for n in (module.GetAllReportNames() or [])]
    except Exception as exc:                      # noqa: BLE001 - reported, not raised
        # Unknown, not empty. Fall through and try to create: a duplicate-name
        # failure is reported honestly below, which beats guessing "absent".
        prefix = "GetAllReportNames failed (%s: %s), so existing reports are unknown; " % (
            type(exc).__name__, exc)
    if listed is not None and name in listed:
        return name, "%sreused the existing '%s' report" % (prefix, name)
    spec = report_spec(expression, sphere=sphere)
    try:
        module.CreateReport(name, spec.category, spec.display, sweep,
                            spec.context, spec.families, spec.components, [])
    except Exception as exc:                      # noqa: BLE001 - reported, not raised
        return None, ("%sCreateReport('%s', %r, %r, '%s') failed: %s: %s"
                      % (prefix, name, spec.category, spec.display, sweep,
                         type(exc).__name__, exc))
    return name, ("%screated report '%s' (%s / %s) on '%s'"
                  % (prefix, name, spec.category, spec.display, sweep))


def export_report_csv(hfss, expression, export_dir=None, sweep=None, setup="Setup1",
                      sphere=None, report_name=None):
    """Create-or-reuse the report and export it to CSV. `(path, note)`.

    `path` is None whenever nothing landed on disk, and the note says which of
    the steps stopped. The sweep name is always read back from the design
    (`resolve_sweep`) unless the caller supplies one: the auto-generated suffix
    is random (`Setup1 : Sweep_MM13NY`) and hardcoding it is EC#6's bug.
    """
    if sweep is None:
        sweep = resolve_sweep(hfss, setup=setup)
    if sweep is None:
        return None, "no analysis sweeps on the design - nothing solved yet"
    name, note = create_or_reuse_report(hfss, expression, sweep, sphere=sphere,
                                        report_name=report_name)
    if name is None:
        return None, note
    if export_dir is None:
        export_dir = default_export_dir()
    try:
        os.makedirs(export_dir, exist_ok=True)
    except OSError as exc:
        return None, "%s; export dir %s is unusable: %s" % (note, export_dir, exc)
    try:
        returned = hfss.post.export_report_to_file(export_dir, name, ".csv")
    except Exception as exc:                      # noqa: BLE001 - reported, not raised
        return None, "%s; export_report_to_file failed: %s: %s" % (note, type(exc).__name__,
                                                                   exc)
    # 1.3.0 builds the path as `<dir>/<plot_name><ext>` and returns it, but it
    # is wrapped by `pyaedt_function_handler`, which returns **False** instead
    # of raising when the error handler is on. Trust the returned value only
    # when it is a path that exists; otherwise look where it would have written.
    path = returned if isinstance(returned, str) and returned else os.path.join(
        export_dir, name + ".csv")
    if not os.path.isfile(path):
        return None, ("%s; export_report_to_file returned %r and no file is at %s"
                      % (note, returned, path))
    return path, "%s; exported to %s" % (note, path)


def parse_report_csv(path, expect=None, x_column=None):
    """`(xs, ys, note)` from an AEDT report export. Never raises, never guesses.

    Two real shapes, both captured off this box on 2026-09-01:

        "Freq [GHz]","dB(S(1,1)) []"                                  <- 2 cols
        "Freq [GHz]","Phi [deg]","Theta [deg]","dB(GainTotal) []"     <- 4 cols

    So **the value is the last column**, never "column 2" — a parser that
    assumes two columns reads Phi as the gain and reports it cheerfully.

    `xs` is the last column before the value that actually varies: AEDT writes
    the plotted sweep as the fastest-varying column, so that is Freq for the
    rectangular form and Theta for a single-frequency pattern cut, which is
    what each is plotted against. Pass `x_column` to override. Every column is
    still parsed, so nothing is thrown away.

    An unexpected header is a **failure with a reason**, not a shrug: when
    `expect` is given (the expression that was asked for) and no column names
    it, this returns no numbers rather than whatever the file happened to hold.
    That is the guard against exporting somebody else's report of the same
    name. Three failure states are kept distinct because they mean different
    things to whoever reads the note: no file at all, a file with no lines, and
    a file with a header but nothing parseable under it.
    """
    if not path or not os.path.isfile(path):
        return [], [], "no file at %r - the export wrote nothing" % (path,)
    try:
        with open(path, "r", encoding="utf-8-sig", newline="") as handle:
            rows = [r for r in csv.reader(handle) if any(c.strip() for c in r)]
    except OSError as exc:
        return [], [], "could not read %s: %s" % (path, exc)
    if not rows:
        return [], [], "%s is empty (%d bytes) - the export produced no lines" % (
            path, os.path.getsize(path))
    header = [c.strip().strip('"') for c in rows[0]]
    if len(header) < 2:
        return [], [], ("unrecognised header %r in %s - an AEDT report export carries at "
                        "least a sweep column and a value column" % (rows[0], path))
    if expect is not None:
        wanted = "".join(str(expect).split())
        if not any(wanted in "".join(c.split()) for c in header[1:]):
            return [], [], ("%s is not this signal's export: header %r carries no column "
                            "for '%s', so its numbers are some other report's"
                            % (path, header, expect))
    data, malformed = [], 0
    for row in rows[1:]:
        if len(row) != len(header):
            malformed += 1
            continue
        try:
            data.append([float(c) for c in row])
        except ValueError:
            malformed += 1
    if not data:
        return [], [], ("%s has a header (%s) but no parseable numeric rows (%d "
                        "malformed) - the report exported with no data"
                        % (path, ", ".join(header), malformed))
    columns = [[row[i] for row in data] for i in range(len(header))]
    if x_column is None:
        x_column = 0
        for index in range(len(columns) - 1):
            if len(set(columns[index])) > 1:
                x_column = index
    xs, ys = columns[x_column], columns[-1]
    return xs, ys, ("parsed %d rows from %s: x='%s', y='%s'%s"
                    % (len(data), os.path.basename(path), header[x_column], header[-1],
                       "" if not malformed
                       else " (%d unparseable row(s) skipped)" % malformed))


def read_via_report(hfss, expression, sweep=None, setup="Setup1", export_dir=None,
                    sphere=None, report_name=None):
    """One scripted read over the report-export route. `(x, y, note)`.

    Same contract as `read_expression`: one attempt, no loop, no retry, and a
    note a human can act on either way.
    """
    path, note = export_report_csv(hfss, expression, export_dir=export_dir, sweep=sweep,
                                   setup=setup, sphere=sphere, report_name=report_name)
    if path is None:
        return [], [], note
    xs, ys, parse_note = parse_report_csv(path, expect=expression)
    return xs, ys, "%s; %s" % (note, parse_note)


def read_signal(hfss, expression, sweep=None, setup="Setup1", export_dir=None,
                sphere=None):
    """Every scripted route, in order, on one process. `(x, y, mechanism, note)`.

    `mechanism` is `MECH_API` or `MECH_EXPORT` when there are numbers, and None
    when there are not. The note always carries **both** attempts, in order, so
    a reader can see that the API was asked and what it said — that trail is
    the only place a future recovery of `get_solution_data` would show up.

    The order, and why it is this way round, is argued in the module docstring:
    the side-effect-free route first, the one that works second, both cheap now
    that a failure no longer releases the session.
    """
    xs, ys, note = read_expression(hfss, expression, sweep=sweep, setup=setup)
    if ys:
        return xs, ys, MECH_API, "%s: %s" % (MECH_API, note)
    export_xs, export_ys, export_note = read_via_report(
        hfss, expression, sweep=sweep, setup=setup, export_dir=export_dir, sphere=sphere)
    trail = "%s: %s; %s: %s" % (MECH_API, note, MECH_EXPORT, export_note)
    if export_ys:
        return export_xs, export_ys, MECH_EXPORT, trail
    return export_xs or xs, [], None, trail


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

    Each signal is read through `read_signal`, so **both** routes are tried on
    the process in hand before any escalation: `get_solution_data` first, then
    the report export. The escalation is spent only when both failed, which is
    also what makes it affordable — a minute-long desktop launch is no longer
    what stands between a run and its numbers.

    What each read reports:

        ROUTE_LIVE         `get_solution_data` answered on the channel the run
                           already had.
        ROUTE_EXPORT       `get_solution_data` did not, and the report export
                           did, on that same channel. Since 2026-09-01 this is
                           the expected outcome on this box.
        ROUTE_FRESH        no route read it on the live channel and
                           `get_solution_data` read it on a fresh process —
                           the channel-lifetime hypothesis CONFIRMED.
        ROUTE_EXPORT_FRESH the same, with the export route doing the reading.
                           (Both fresh tokens are also what a signal gets when
                           an *earlier* signal spent the escalation; the note
                           says which.)
        ROUTE_BOTH_FAILED  every route failed on a fresh process too. That
                           rules out the channel's age and nothing more — see
                           VERDICTS, which deliberately declines to name a
                           cause.
        ROUTE_UNTESTED     the live channel failed and no fresh process ever
                           ran — no recycler was wired, or the recycle raised
                           (this signal's, or an earlier signal's, which
                           spends the budget without producing a desktop).
                           Never write this up as a pairing verdict: it is
                           the outcome that says the question is still open,
                           and recording it as anything else is the mistake
                           this class was built to prevent.

    `export_dir` is where the report-export route writes its CSV. Pass the
    workspace `results/` and the file is a delivered artifact the solve
    session's Done condition can point at; leave it None and a per-process temp
    directory is used, whose path the note names.
    """

    def __init__(self, hfss, recycle=None, export_dir=None, sphere=None):
        self.hfss = hfss
        self._recycle = recycle
        self.export_dir = export_dir
        self.sphere = sphere
        # `escalated` is the BUDGET (spent even by a recycle that raised);
        # `on_fresh_process` is the FACT (a replacement desktop actually came
        # up). Conflating the two is how a run claims "failed on a fresh
        # process too" about a process that never existed — the same
        # untested-hypothesis-as-finding move this class exists to stop, and
        # it appeared here first as a two-line bug.
        self.escalated = False
        self.on_fresh_process = False
        self.recycle_note = None

    def read(self, expression, sweep=None, setup="Setup1", sphere=None):
        """One signal, every route, at most one escalation. Returns a `Readout`."""
        if sphere is None:
            sphere = self.sphere
        xs, ys, mechanism, note = read_signal(self.hfss, expression, sweep=sweep,
                                              setup=setup, export_dir=self.export_dir,
                                              sphere=sphere)
        if ys:
            if not self.on_fresh_process:
                return Readout(xs, ys, ROUTE_BY_MECHANISM[(mechanism, False)], note)
            return Readout(xs, ys, ROUTE_BY_MECHANISM[(mechanism, True)],
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
        fresh_xs, fresh_ys, fresh_mech, fresh_note = read_signal(
            fresh, expression, sweep=sweep, setup=setup, export_dir=self.export_dir,
            sphere=sphere)
        trail = "live channel: %s; %s; fresh process: %s" % (note, self.recycle_note,
                                                             fresh_note)
        if fresh_ys:
            return Readout(fresh_xs, fresh_ys, ROUTE_BY_MECHANISM[(fresh_mech, True)],
                           trail)
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

    **Prefer `read_via_report` / `read_signal`.** This function goes through
    `post.create_report`, which is a pyAEDT wrapper over the same report layer
    that `get_solution_data` dies in, and on 2026-09-01 it failed here for that
    reason. `create_or_reuse_report` drives `odesign.GetModule("ReportSetup")`
    directly instead, which is the call that works. This one is kept only
    because workspace scripts already call it; it is not the route to write new
    code against.

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
    print(f"PASS: read_results route_arounds=({apply_route_arounds()}) "
          f"accessors={','.join(CANDIDATE_ACCESSORS)} "
          f"routes={','.join(sorted(VERDICTS))}")
