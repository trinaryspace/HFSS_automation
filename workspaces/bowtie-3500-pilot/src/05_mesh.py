"""Stage 5: mesh — adaptive-only by Recipe (no mesh operations).

Records that the mesh-operations list is deliberately empty; Setup1's
adaptivity (stage 6) does the refinement. Nothing to delete-then-create:
an empty list is the idempotent state.
"""

import sys

from ws_common import attach, exit_keep_alive, write_state


def main() -> int:
    hfss = attach(launch=False)
    ops = list(hfss.mesh.meshoperations)
    print("mesh operations:", ops, flush=True)
    write_state("mesh_ops", str(ops))
    assert not ops, "unexpected mesh operations present: %r" % ops
    print("PASS: mesh adaptive-only (0 mesh operations)", flush=True)
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    exit_keep_alive()
