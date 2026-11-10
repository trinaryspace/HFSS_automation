"""Print a compact card of the live model: objects, boundaries, setups.

Read-only. Used to diagnose a failed stage and as Review-gate evidence.

Usage (workspace root):  python src/15_model_card.py
Prints one Verification line:  PASS: model_card objects=<n> ...
"""

import ws_common


def main():
    hfss = ws_common.attach()
    m = hfss.modeler
    solids = sorted(m.solid_names)
    sheets = sorted(m.sheet_names)
    print("solids:", solids, flush=True)
    print("sheets:", sheets, flush=True)
    for name in solids + sheets:
        obj = m[name]
        box = [round(float(v), 4) for v in obj.bounding_box]
        print("  %-12s faces=%-4d mat=%-10s bbox=%s"
              % (name, len(obj.faces), obj.material_name or "-", box), flush=True)
    bnds = [(b.name, b.type) for b in hfss.boundaries]
    print("boundaries:", bnds, flush=True)
    print("setups:", hfss.setup_names, "sweeps:", hfss.existing_analysis_sweeps,
          flush=True)
    print("PASS: model_card objects=%d solids=%d sheets=%d boundaries=%d"
          % (len(solids) + len(sheets), len(solids), len(sheets), len(bnds)),
          flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
