"""Diagnostic: dump variable expressions + exact vertex positions + port assignment."""

import sys

sys.path.insert(0, "src")
from ws_common import attach

hfss = attach(launch=False)

print("== variable expressions ==", flush=True)
vm = hfss.variable_manager
for name in sorted(vm.variables):
    try:
        print(f"  {name} = {vm.variables[name].expression}", flush=True)
    except Exception as e:
        print(f"  {name} ERR {type(e).__name__}", flush=True)

print("== PatchBowtie faces with vertex positions ==", flush=True)
obj = hfss.modeler.objects_by_name["PatchBowtie"]
for f in obj.faces[:14]:
    try:
        vs = sorted(set(tuple(round(c, 3) for c in v.position) for v in f.vertices))
    except Exception as e:
        vs = f"ERR {type(e).__name__} {str(e)[:80]}"
    print(f"  face {f.id} center={tuple(round(c,3) for c in f.center)} verts={vs}", flush=True)

print("== Rectangle1 ==", flush=True)
r1 = hfss.modeler.objects_by_name["Rectangle1"]
for f in list(r1.faces)[:6]:
    vs = sorted(set(tuple(round(c, 3) for c in v.position) for v in f.vertices))
    print(f"  face {f.id} center={tuple(round(c,3) for c in f.center)} verts={vs}", flush=True)

print("== wave port boundary ==", flush=True)
for b in hfss.boundaries:
    if "Wave" in b.type:
        print(f"  name={b.name} type={b.type} faces={[f.id for f in b.faces]}", flush=True)
