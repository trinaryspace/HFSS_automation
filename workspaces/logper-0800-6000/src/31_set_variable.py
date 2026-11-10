"""Set one design variable on the design selected by HFSS_WS_DESIGN.

A variant that differs from its spec by a dimension is a VARIABLE EDIT, not a
rebuild (hard rule 6): the geometry follows, and AEDT keeps the previous
value's solution as its own variation. Variant B of the RO4350B design is
`feed_W` re-tuned on the design variant A was solved on.

Usage (workspace root):
    set HFSS_WS_DESIGN=LogPer_RO4350B_20mil
    python src/31_set_variable.py feed_W 1.6mm
Prints one Verification line:  PASS: set_variable <name>=<value> ...
"""

import sys

import ws_common


def main(argv):
    if len(argv) != 2:
        raise SystemExit("usage: 31_set_variable.py <name> <value-with-unit>")
    name, value = argv
    hfss = ws_common.attach()
    known = list(hfss.variable_manager.design_variable_names)
    if name not in known:
        raise RuntimeError("%r is not a design variable of %s" % (name, ws_common.DESIGN))
    before = str(hfss[name])
    hfss[name] = value
    after = str(hfss[name])
    if after.replace(" ", "") != value.replace(" ", ""):
        raise RuntimeError("%s read back as %r, not %r" % (name, after, value))
    if not bool(hfss.validate_simple()):
        raise RuntimeError("validate_simple() returned False with %s=%s" % (name, value))
    hfss.save_project()
    print("PASS: set_variable design=%s %s=%s (was %s) validate_simple=True"
          % (ws_common.DESIGN, name, after, before), flush=True)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
