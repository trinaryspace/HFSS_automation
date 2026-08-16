"""Static gate (verification contract, ADR 0005 companion): py_compile +
import-check of every `src/*.py` BEFORE any AEDT launch.

Run it on the workspace:  python src/00_static_gate.py
- `py_compile` every script in this directory (catches SyntaxError).
- Import-check every script (catches NameError, bad imports, missing
  dependencies) via importlib source loading — nothing executes beyond
  module import, so nothing attaches to a desktop.
- The import-check imports `ws_common.py`, which imports pyAEDT: the gate
  must run in the AEDT-capable Python, which is the environment every
  staged script runs in anyway.

Output: one terminal Verification line
    PASS: static_gate compiled=<N> imported=<N>
exit 0, or FAIL lines + exit 1.
"""

import importlib.util
import os
import py_compile
import sys

SELF = "00_static_gate"


def gate_scripts(src_dir):
    """Sorted src/*.py paths (excluding the gate itself only if needed)."""
    names = sorted(n for n in os.listdir(src_dir) if n.endswith(".py"))
    return [os.path.join(src_dir, n) for n in names]


def run_gate(src_dir):
    """(ok, lines, n_compiled, total_importable): compile + import check."""
    lines = []
    scripts = gate_scripts(src_dir)
    compiled_ok = []
    for path in scripts:
        try:
            py_compile.compile(path, doraise=True)
            compiled_ok.append(os.path.basename(path))
            lines.append("compile ok: %s" % os.path.basename(path))
        except py_compile.PyCompileError as exc:
            lines.append("compile FAIL: %s %s" % (os.path.basename(path), exc))
    importable = [s for s in scripts if os.path.basename(s) != SELF + ".py"]
    imported_ok = []
    for path in importable:
        stem = os.path.splitext(os.path.basename(path))[0]
        try:
            spec = importlib.util.spec_from_file_location("_gate_" + stem, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            imported_ok.append(stem)
            lines.append("import ok: %s" % stem)
        except Exception as exc:  # noqa: BLE001 - any import failure is a gate failure
            lines.append("import FAIL: %s %s: %s" % (stem, type(exc).__name__, str(exc)[:200]))
    ok = len(compiled_ok) == len(scripts) and len(imported_ok) == len(importable)
    return ok, lines, len(compiled_ok), len(imported_ok)


def main():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    ok, lines, n_compiled, n_imported = run_gate(src_dir)
    for line in lines:
        print("  " + line, flush=True)
    if ok:
        print("PASS: static_gate compiled=%d imported=%d" % (n_compiled, n_imported), flush=True)
        return 0
    print("FAIL: static_gate compiled=%d imported=%d (see lines above)" % (n_compiled, n_imported),
          flush=True)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
