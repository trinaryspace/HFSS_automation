"""Snapshot a model that is already open in the AEDT UI — read-only.

For capturing reference models by hand (ticket 12a's input): you build
something in the UI, and this records its shape so `snapshot_to_spec` can
be designed against real models rather than against one bowtie.

**This is deliberately NOT `src/capture_state.py`.** That one goes through
`ws_common.attach()`, which is workspace-scoped and, with no pinned port
recorded, attaches to whatever desktop is listening and then *pins it* —
after which a later `teardown()` would target your session. It also passes
`solution_type` and `remove_lock`, which can mutate the design. Neither is
acceptable against a desktop you are working in.

Safety contract for this script:

  * attaches with `new_desktop=False` and binds to the ACTIVE project and
    design — it never creates one, and aborts if nothing is open;
  * passes no `solution_type`, no `remove_lock`, no project path — nothing
    that could change what is on screen;
  * writes NO machine state: no `aedt_port.txt`, no `aedt_process_id.txt`,
    no pin of any kind;
  * never calls `release_desktop`, never closes a project, never kills a
    process. It exits via `os._exit(0)` because gRPC teardown otherwise
    hangs (env-compat #10), leaving your desktop exactly as it was.

It also applies the validated ticket-16 route-around for the pyAEDT 1.3.0
`HfssConstants.default_solution` bug, which is latent on a working attach
but fires when the gRPC transport flakes. It is a one-line alias and
changes nothing on the working path.

Usage (repo root, with the model open in AEDT):

    python scripts/capture_live.py --name horn-10ghz
    python scripts/capture_live.py --name horn --out /some/where.json
    python scripts/capture_live.py --list        # just show what is open

Prints one `PASS: capture_live ...` line and the path it wrote.
"""

import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "skill", "hfss-agent", "templates", "workspace", "src")
DEFAULT_DIR = os.path.join(REPO, "knowledge", "cases", "_snapshots")
DEFAULT_VERSION = "2024.1"


def _apply_readout_route_around():
    """Ticket 16's route-around, aliased on the classes that actually need it.

    Verified against the installed pyAEDT 1.3.0: the constants live in
    `generic/aedt_constants.py` (NOT `application/design_solutions.py`,
    which only *references* them), and every design-type constants class
    defines `solution_default` while `design_solutions.py` reads
    `self._design_type.default_solution` — twelve times. The attribute is
    missing, so the read raises whenever the fallback path is taken (no
    odesign attached, or `GetSolutionType()` failing over gRPC per EC#3).
    Aliasing is a no-op on the working path.
    """
    try:
        from ansys.aedt.core.generic import aedt_constants
    except ImportError:
        return "unavailable"
    patched = 0
    for name in dir(aedt_constants):
        cls = getattr(aedt_constants, name, None)
        if not isinstance(cls, type):
            continue
        if hasattr(cls, "default_solution"):
            continue
        fallback = getattr(cls, "solution_default", None)
        if fallback is None:
            continue
        try:
            cls.default_solution = fallback
            patched += 1
        except Exception:  # noqa: BLE001 - metaclass may forbid assignment
            continue
    return "patched=%d" % patched if patched else "not-needed"


def _load_shape_fn():
    """Reuse the template's pure extractor, without importing ws_common."""
    sys.path.insert(0, SRC)
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "capture_state_pure", os.path.join(SRC, "capture_state.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)      # top level imports only json/os/sys
    return module.shape_from_model


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--name", help="label for the snapshot file")
    parser.add_argument("--out", help="explicit output path (.json)")
    parser.add_argument("--version", default=DEFAULT_VERSION,
                        help="AEDT version (default %s)" % DEFAULT_VERSION)
    parser.add_argument("--list", action="store_true",
                        help="list open projects/designs and exit")
    args = parser.parse_args(argv)

    # Prudence, not a known defect: this script writes nothing, but any
    # script that attaches to a live session shares its process space with
    # your unsaved work. Save first.
    print("note: attaching read-only to your open session — save your work "
          "first if you have unsaved changes", flush=True)
    route = _apply_readout_route_around()
    from ansys.aedt.core import Desktop, Hfss

    # Attach only. close_on_exit=False so nothing we do can close your work.
    desktop = Desktop(version=args.version, new_desktop=False,
                      non_graphical=False, close_on_exit=False)

    projects = list(getattr(desktop, "project_list", []) or [])
    if not projects:
        print("capture_live aborted: no project is open in AEDT — open the "
              "model first, then re-run", flush=True)
        sys.stdout.flush()
        os._exit(2)

    if args.list:
        for project in projects:
            try:
                designs = list(desktop.design_list(project) or [])
            except Exception:  # noqa: BLE001 - report, never mask
                designs = ["<unreadable>"]
            print("  %-32s designs: %s" % (project, ", ".join(designs)))
        print("PASS: capture_live listed projects=%d" % len(projects), flush=True)
        sys.stdout.flush()
        os._exit(0)

    # Bind to the ACTIVE project/design: no arguments means "what is open",
    # and no solution_type/remove_lock means nothing gets rewritten.
    model = Hfss(new_desktop=False)

    shape_from_model = _load_shape_fn()
    shape = shape_from_model(model)

    shape["_capture"] = {
        "project": str(getattr(model, "project_name", "") or ""),
        "design": str(getattr(model, "design_name", "") or ""),
        "solution_type": str(getattr(model, "solution_type", "") or ""),
        "aedt_version": args.version,
        "route_around": route,
        "source": "capture_live.py (read-only, UI session)",
    }

    name = args.name or shape["_capture"]["design"] or "snapshot"
    out = args.out or os.path.join(DEFAULT_DIR, "%s.json" % name)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(shape, handle, indent=1, sort_keys=True)
        handle.write("\n")

    counts = {
        "objects": len(shape["objects"]),
        "materials": len([m for m in shape["materials"].values() if m]),
        "boundaries": len(shape["boundaries"]),
        "excitations": len(shape["excitations"]),
        "setups": len(shape["setups"]),
        "sweeps": len(shape["sweeps"]),
        "variables": len(shape["variables"]),
    }
    print("project: %s   design: %s   solution: %s"
          % (shape["_capture"]["project"], shape["_capture"]["design"],
             shape["_capture"]["solution_type"]), flush=True)
    print("snapshot written: %s" % out, flush=True)
    if counts["variables"] == 0:
        print("! no design variables captured — if this model was built by "
              "hand with literal dimensions, that is expected, and it is "
              "exactly the parametric link the spec would add", flush=True)
    print("PASS: capture_live " +
          " ".join("%s=%d" % kv for kv in sorted(counts.items())), flush=True)
    sys.stdout.flush()
    # No release_desktop, no close, no kill: your session is untouched.
    os._exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(exc).__name__, str(exc)[:600], flush=True)
        sys.stdout.flush()
        os._exit(1)
