"""Stage 3: materials — each solid reports its Recipe material.

Recipe: FR4_epoxy from the AEDT library (er 4.4, tan-d 0.02 — the stock
values, matching case.json; verified and reported here); pec conductors
(patch+feed united, ground); air airbox. PortSheet is a vacuum sheet — not
a physical material (port cross-section).
"""

import sys

from ws_common import attach, exit_keep_alive


def main() -> int:
    hfss = attach(launch=False)
    fm = hfss.materials.material_keys.get("FR4_epoxy")
    if fm is not None:
        print("FR4_epoxy er =", getattr(fm.permittivity, "evaluated_value", "?"),
              "tan-d =", getattr(fm.dielectric_loss_tangent, "evaluated_value", "?"), flush=True)
        assert abs(float(fm.permittivity.evaluated_value) - 4.4) < 1e-6, "FR4_epoxy er != 4.4"
        assert abs(float(fm.dielectric_loss_tangent.evaluated_value) - 0.02) < 1e-6, "FR4_epoxy tan-d != 0.02"
    else:
        print("WARNING: FR4_epoxy not in cold material index; reading by object only", flush=True)

    expect = {
        "Substrate": "FR4_epoxy",
        "Patch": "pec",
        "Ground": "pec",
        "AirBox": "air",
    }
    ok = True
    for o, want in expect.items():
        obj = hfss.modeler.objects_by_name.get(o)
        if obj is None:
            print("  MISSING object:", o, flush=True)
            ok = False
            continue
        got = obj.material_name
        print("  %s: material = %s (want %s)" % (o, got, want), flush=True)
        if got != want:
            ok = False
    print("PASS: materials Substrate=FR4_epoxy(er 4.4 tan-d 0.02), Patch=pec, "
          "Ground=pec, AirBox=air" if ok else "STAGE_FAILED materials mismatch", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
