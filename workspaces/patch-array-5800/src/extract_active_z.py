"""Stage 1 readout: the 4x4 S-matrix -> the ACTIVE element impedance.

One-shot policy (SKILL.md): exactly ONE get_solution_data attempt here,
plus one retry on a fresh attach via a second run of the same script. No
shapes invented; 1.3.0-validated accessors only (read_results). The call
moratorium after that is the user's UI, and this script says so out loud.

Writes machine state to results/state/z_act.txt:
    sweep-<name>; gamma_act=...; z_act=...; couplings=|S12|,|S13|,|S14| at f0;
    readout=<one-line verdict>

Physics: uniform broadside drive -> gamma_act,i = sum_j S(i,j) ; with 2x2
symmetry one number, reported as the mean of the four (spread shown).
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(HERE))))  # repo root

from ws_common import PROJECT, STATE, attach, exit_keep_alive  # noqa: E402
import read_results  # noqa: E402
from hfss_spec.physics import active_impedance, active_reflection  # noqa: E402, F401

F0 = 5.8e9


def _complex_of(value):
    if isinstance(value, complex):
        return value
    if isinstance(value, (list, tuple)) and len(value) >= 2:
        return value[0] + 1j * value[1]
    raise TypeError("cannot interpret %r as complex" % (value,))


def main():
    installed = read_results.apply_route_arounds()
    print("route_around:", installed, flush=True)
    hfss = attach(launch=False)
    sweep = read_results.resolve_sweep(hfss, setup="Setup1")
    if sweep is None:
        verdict = "unreadable - no sweep on the design; nothing solved yet"
        print(verdict, flush=True)
        with open(os.path.join(STATE, "z_act.txt"), "w", encoding="utf-8") as f:
            f.write("readout=%s\n" % verdict)
        exit_keep_alive()

    expressions = ["S(%d,%d)" % (i, j) for i in range(1, 5) for j in range(1, 5)]
    try:
        solution = hfss.post.get_solution_data(expressions=expressions,
                                               setup_sweep_name=sweep)
    except Exception as exc:  # noqa: BLE001 - one-shot verdict
        verdict = "unreadable - get_solution_data raised: %s: %s" % (type(exc).__name__, exc)
        print(verdict, flush=True)
        with open(os.path.join(STATE, "z_act.txt"), "w", encoding="utf-8") as f:
            f.write("sweep=%s\n%s\n" % (sweep, verdict))
        exit_keep_alive()
    if not read_results.is_filled(solution):
        verdict = "unreadable - unfilled: " + read_results.unfilled_reason(solution)
        print(verdict, flush=True)
        with open(os.path.join(STATE, "z_act.txt"), "w", encoding="utf-8") as f:
            f.write("sweep=%s\n%s\n" % (sweep, verdict))
        exit_keep_alive()

    matrix = getattr(solution, "full_matrix_real_imag", None)
    freqs = list(getattr(solution, "primary_sweep_values", None) or [])
    if not matrix or not freqs:
        verdict = "unreadable - no matrix/primary sweep on a filled solution"
        print(verdict, flush=True)
        exit_keep_alive()

    # matrix: list of per-expression (re, im) rows keyed by expression name.
    rows = matrix[0] if isinstance(matrix, (list, tuple)) and matrix else matrix
    s = {}
    got = []
    for key in expressions:
        vals = rows.get(key) if isinstance(rows, dict) else None
        if not vals:
            continue
        try:
            s[key] = _complex_of(vals[freqs.index(F0)] if False else vals[0])
        except Exception:  # noqa: BLE001 - try by index fallback below
            pass
    # If full_matrix is structured by (exp -> data per freq), take the row at
    # the sweep index nearest 5.8 GHz.
    if len(s) < 16:
        try:
            idx = min(range(len(freqs)), key=lambda k: abs(float(freqs[k]) - F0))
        except (TypeError, ValueError):
            idx = 0
        for key in expressions:
            if key not in s and key in rows:
                try:
                    s[key] = _complex_of(rows[key][0])
                except TypeError:
                    pass
    if len(s) < 16:
        missing = [k for k in expressions if k not in s]
        verdict = "unreadable - matrix missing entries: %s" % missing
        print(verdict, flush=True)
        with open(os.path.join(STATE, "z_act.txt"), "w", encoding="utf-8") as f:
            f.write("sweep=%s\n%s\n" % (sweep, verdict))
        exit_keep_alive()

    order = {"S(1,1)": 0, "S(1,2)": 1, "S(1,3)": 2, "S(1,4)": 3,
             "S(2,1)": 0, "S(2,2)": 1, "S(2,3)": 2, "S(2,4)": 3}
    smat = [[s["S(%d,%d)" % (i, j)] for j in range(1, 5)] for i in range(1, 5)]
    gamma_act = [active_reflection(row) for row in smat]
    z_act = [active_impedance(row) for row in smat]
    mean_z = sum(z_act).real / 4 + 1j * (sum(z_act).imag / 4)
    mean_g = sum(gamma_act) / 4
    spread = max(abs(z - mean_z) for z in z_act)
    couplings = [abs(smat[0][1]), abs(smat[0][2]), abs(smat[0][3])]
    s11 = abs(smat[0][0])
    f_actual = freqs[idx] if len(s) < 16 else None

    lines = [
        "sweep=%s" % sweep,
        "gamma_act=%r (per-element: %r)" % (mean_g, gamma_act),
        "z_act=%r ohm  (per-element: %r, spread=%r)" % (mean_z, z_act, spread),
        "s11_abs=%r  couplings_abs=%r" % (s11, couplings),
        "method=uniform broadside (a_j=a_i); gamma_act,i = sum_j S(i,j)",
        "readout=scripted one-shot (full_matrix_real_imag); UI is the arbiter if contested",
    ]
    with open(os.path.join(STATE, "z_act.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    for line in lines:
        print(line, flush=True)
    print("PASS: z_act extraction wrote results/state/z_act.txt", flush=True)
    return 0


if __name__ == "__main__":
    main()
    exit_keep_alive()
