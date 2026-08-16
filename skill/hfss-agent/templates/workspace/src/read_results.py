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
scripted readout at one attempt plus one retry on a fresh attach, then hands the
plot to the user and reports the signal as read from the UI — the pilot tried
eight shapes and ended the run. Nothing here loops or retries; `read_expression`
returns a verdict and the caller decides once.

Usage:
    import read_results
    read_results.apply_route_arounds()          # before constructing Hfss
    sweep = read_results.resolve_sweep(hfss)    # never guess the auto-suffix
    freqs, values, note = read_results.read_expression(hfss, "dB(S(1,1))", sweep)
"""

import os

CANDIDATE_ACCESSORS = ("full_matrix_real_imag", "get_expression_data")


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
    installed = apply_route_arounds()
    print(f"PASS: read_results route_around={'installed' if installed else 'not-needed'} "
          f"accessors={','.join(CANDIDATE_ACCESSORS)}")
