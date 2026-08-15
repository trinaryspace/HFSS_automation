"""Stage 7: mesh — recipe says adaptive-only for this model class.

Records that the mesh-operations list is deliberately empty; adaptivity in
Setup1 (stage 06) does the refinement (HFSS intro manual: adaptive mesh
refinement is the key to accurate results without manual meshing).
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    ops = list(hfss.mesh.meshoperations)
    print("mesh operations:", ops, flush=True)
    write_state("mesh_ops", str(ops))
    print("STAGE_OK mesh adaptive-only" if not ops else "STAGE_FAILED unexpected mesh ops", flush=True)
    return 0 if not ops else 1


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
