"""Stage 5: materials — each solid reports its Recipe material.

Recipe: FR4_43 (er 4.3, tan-d 0.02) substrate; pec conductors (patch, feed,
ground); air airbox (no DGS: ground is a plain pec slab). Verification
stage: reports what each solid resolves to.
"""

import sys

from ws_common import attach, exit_keep_alive


def main() -> int:
    hfss = attach(launch=False)
    print("materials in library:", sorted(hfss.materials.material_keys)[:20], flush=True)
    expect = {
        "Substrate": "FR4_43",
        "PatchBowtie": "pec",
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
        print(f"  {o}: material = {got} (want {want})", flush=True)
        if got != want:
            ok = False
    print("STAGE_OK materials" if ok else "STAGE_FAILED materials mismatch", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
