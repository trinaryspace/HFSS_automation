"""Route-B add-on: choose the initial-mesh method for the design in
HFSS_WS_DESIGN.

Why: on the 19-element design (v5) AEDT's default initial mesher failed
within 26 seconds with
    "Definition Mesh, process mesh3d : Unexpected internal software error"
before any field solve. The geometry validates; the mesher simply fails on
it. Switching the method (and, if needed, turning off the Phi mesher) is the
standard way round.

Does nothing unless LOGPER_MESH_METHOD is set, so other designs replay
unchanged.

Usage (workspace root):
    set HFSS_WS_DESIGN=LogPer_RO4350B_v5
    set LOGPER_MESH_METHOD=AnsoftClassic      (or AnsoftTAU, Auto)
    set LOGPER_MESH_PHI=0                      (optional: 0 turns Phi off)
    python src/25_initial_mesh.py
Prints one Verification line:  PASS: initial_mesh ...

API, from the installed pyAEDT 1.3.0 (modules/mesh.py):
    assign_initial_mesh_from_slider(level=5, method="Auto",
        dynamic_surface=True, flex_mesh=False, curvilinear=False,
        fallback=True, phi=True, auto_model_resolution=True,
        model_resolution_length="0.0001mm") -> bool
"""

import os

import ws_common

ALLOWED = ("Auto", "AnsoftTAU", "AnsoftClassic")


def main():
    method = os.environ.get("LOGPER_MESH_METHOD")
    if not method:
        print("PASS: initial_mesh skipped - LOGPER_MESH_METHOD not set", flush=True)
        return
    if method not in ALLOWED:
        raise RuntimeError("LOGPER_MESH_METHOD must be one of %s" % (ALLOWED,))
    phi = os.environ.get("LOGPER_MESH_PHI", "1") != "0"
    hfss = ws_common.attach()
    done = hfss.mesh.assign_initial_mesh_from_slider(level=5, method=method, phi=phi)
    if not done:
        raise RuntimeError("assign_initial_mesh_from_slider reported failure")
    if not bool(hfss.validate_simple()):
        raise RuntimeError("validate_simple() returned False after the mesh change")
    hfss.save_project()
    ws_common.write_state("stage_initial_mesh", "%s phi=%s" % (method, phi))
    print("PASS: initial_mesh design=%s method=%s phi=%s validate_simple=True"
          % (ws_common.DESIGN, method, phi), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
