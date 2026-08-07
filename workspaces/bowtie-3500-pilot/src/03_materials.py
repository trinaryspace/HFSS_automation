"""Stage 3: materials — every solid reports its Recipe material (read-back verify).

Materials were assigned at creation (stage 02). This stage verifies the
assignment and the FR4_43 definition (permittivity 4.3, loss tangent 0.02)
so the Verification line carries the material contract. No objects are
created here, so there is nothing to delete-then-create (ADR 0008).
"""

import sys

from ws_common import attach, exit_keep_alive, write_state

EXPECTED = {
    "Substrate": "FR4_43",
    "Ground": "pec",
    "PatchBowtie": "pec",
    "AirBox": "air",
}


def main() -> int:
    hfss = attach(launch=False)
    m = hfss.modeler
    reported = {}
    for name, want in EXPECTED.items():
        obj = m.objects_by_name[name]
        got = getattr(obj, "material_name", "") or ""
        reported[name] = got
        assert got.lower() == want.lower(), (
            "material mismatch on %s: want %s got %s" % (name, want, got)
        )
    mat = hfss.materials["FR4_43"]  # indexing resolves the project library
    assert mat is not None, "FR4_43 missing from project library"
    print("FR4_43 permittivity =", mat.permittivity.evaluated_value, flush=True)
    print("FR4_43 loss tangent =", mat.dielectric_loss_tangent.evaluated_value, flush=True)
    assert abs(mat.permittivity.evaluated_value - 4.3) < 1e-9, "FR4_43 er wrong"
    assert abs(mat.dielectric_loss_tangent.evaluated_value - 0.02) < 1e-9, "FR4_43 tand wrong"
    write_state("materials", ",".join("%s=%s" % kv for kv in sorted(reported.items())))
    print(
        "PASS: materials %s, FR4_43 er=4.3 tand=0.02" %
        ", ".join("%s=%s" % (k, v) for k, v in sorted(reported.items())),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
