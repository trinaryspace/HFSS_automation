"""Z_act extraction, attempt 3: on-disk export (the sanctioned fallback shape).

get_solution_data raised GrpcApiError(GetVariables) twice (one-shot + one
fresh-attach retry, both documented in the ledger). read_results.export_fallback
is the one remaining scripted shape — a create_report + export_report_to_file
CSV. If this fails too, the readout is UI-arbitrated, per the policy: Z_act
from the user's S-matrix read, and the z_act.txt verdict says "unreadable -
flaky readout, UI-arbitrated".
"""

import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(HERE))))  # repo root

from ws_common import STATE, attach, exit_keep_alive  # noqa: E402
import read_results  # noqa: E402
from hfss_spec.physics import active_impedance, active_reflection  # noqa: E402

F0 = 5.8e9
EXPRESSIONS = ["S(%d,%d)" % (i, j) for i in range(1, 5) for j in range(1, 5)]


def main():
    hfss = attach(launch=False)
    sweep = read_results.resolve_sweep(hfss, setup="Setup1")
    if sweep is None:
        _write("unreadable - no sweep on the design; nothing solved yet")
        exit_keep_alive()
    csv_dir = os.path.join(STATE, "zact_export")
    os.makedirs(csv_dir, exist_ok=True)
    try:
        report = hfss.post.create_report(expressions=EXPRESSIONS,
                                         setup_sweep_name=sweep)
    except Exception as exc:  # noqa: BLE001
        _write("unreadable - create_report raised: %s: %s" % (type(exc).__name__, exc))
        exit_keep_alive()
    try:
        hfss.post.export_report_to_file(csv_dir,
                                        getattr(report, "plot_name", "Plot 1"),
                                        ".csv")
    except Exception as exc:  # noqa: BLE001
        _write("unreadable - export_report_to_file raised: %s: %s" % (type(exc).__name__, exc))
        exit_keep_alive()

    files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]
    if not files:
        _write("unreadable - export landed no csv")
        exit_keep_alive()
    path = os.path.join(csv_dir, sorted(files)[-1])
    print("exported:", path, flush=True)
    rows = list(csv.reader(open(path, encoding="utf-8", errors="replace")))
    # find the F column and the row nearest 5.8 GHz
    freq_col = None
    for row in rows[:4]:
        for i, cell in enumerate(row):
            try:
                if abs(float(cell) - F0 / 1e9) < 0.5:
                    freq_col = i
            except ValueError:
                continue
        if freq_col is not None:
            break
    selected = None
    for row in rows:
        try:
            f = float(row[freq_col])
        except (ValueError, TypeError):
            continue
        if selected is None or abs(f - 5.8) < abs(selected[0] - 5.8):
            selected = (f, row)
    if selected is None or len(selected[1]) < 17:
        _write("unreadable - no 5.8 GHz row in the export")
        exit_keep_alive()
    f_act, row = selected
    # header: F, |S(1,1)|, phase..., or the exported naming; try common shapes
    smat = {}
    header = [h.strip().lower() for h in rows[0]]
    for i in range(1, 5):
        for j in range(1, 5):
            for tag in ("s(%d,%d)" % (i, j), "%d,%d" % (i, j), "s(%d,%d)mag" % (i, j)):
                if tag in header:
                    idx = header.index(tag)
                    break
            else:
                idx = None
            if idx is None or idx >= len(row):
                continue
            try:
                smat["S(%d,%d)" % (i, j)] = complex(float(row[idx]))
            except ValueError:
                pass
    if len(smat) < 16:
        _write("unreadable - export parsed %d/16 S entries (see %s); UI-arbitrated"
               % (len(smat), path))
        exit_keep_alive()
    order = [["S(%d,%d)" % (i, j) for j in range(1, 5)] for i in range(1, 5)]
    matrix = [[smat[k] for k in row_tags] for row_tags in order]
    gammas = [active_reflection(r) for r in matrix]
    zs = [active_impedance(r) for r in matrix]
    mean_z = sum(zs) / 4
    spread = max(abs(z - mean_z) for z in zs)
    lines = [
        "sweep=%s" % sweep,
        "f_extracted=%.4f GHz" % f_act,
        "gamma_act=%r (per-element: %r)" % (sum(gammas) / 4, gammas),
        "z_act=%r ohm (per-element: %r, spread=%r)" % (mean_z, zs, spread),
        "s11_abs=%r couplings_abs=%r" % (
            abs(matrix[0][0]), [abs(matrix[0][k]) for k in (1, 2, 3)]),
        "export=%s" % path,
        "readout=scripted export fallback (create_report + export_report_to_file); "
        "UI is the arbiter if contested",
    ]
    with open(os.path.join(STATE, "z_act.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    for line in lines:
        print(line, flush=True)
    print("PASS: z_act extraction via export fallback", flush=True)
    return 0


def _write(verdict):
    print(verdict, flush=True)
    with open(os.path.join(STATE, "z_act.txt"), "w", encoding="utf-8") as f:
        f.write("readout=%s\n" % verdict)


if __name__ == "__main__":
    main()
    exit_keep_alive()
