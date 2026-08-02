---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_objects_by_name.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_objects_by_name 

Modeler2D.get_objects_by_name(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _case_sensitive : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Return the objects whose names match a wildcard pattern.
The `*` character acts as a wildcard that matches any sequence of characters (including none). The matching mode is inferred automatically from the position of `*` in `assignment`: 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Wildcard pattern to match against object names. Use `*` as a wildcard for any sequence of characters. 

**case_sensitive**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the match is case-sensitive. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Objects whose names satisfy the pattern.
Examples
# Exact match >>> objs = modeler.get_objects_by_name(“Patch_1”)
# All objects whose name starts with “Substrate” >>> objs = modeler.get_objects_by_name(“Substrate*”)
# All objects whose name ends with “_gnd” >>> objs = modeler.get_objects_by_name(”[*](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_objects_by_name.html#id1)_gnd”)
# All objects whose name contains “patch” >>> objs = modeler.get_objects_by_name(” _patch_ ”, case_sensitive=False)
# Mid-string wildcard: names like “Sub_1”, “Sub_gnd_1”. >>> objs = modeler.get_objects_by_name(“Sub*_1”)
# get_objects_by_name 

Modeler2D.get_objects_by_name(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _case_sensitive : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Return the objects whose names match a wildcard pattern.
The `*` character acts as a wildcard that matches any sequence of characters (including none). The matching mode is inferred automatically from the position of `*` in `assignment`: 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Wildcard pattern to match against object names. Use `*` as a wildcard for any sequence of characters. 

**case_sensitive**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the match is case-sensitive. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Objects whose names satisfy the pattern.
Examples
# Exact match >>> objs = modeler.get_objects_by_name(“Patch_1”)
# All objects whose name starts with “Substrate” >>> objs = modeler.get_objects_by_name(“Substrate*”)
# All objects whose name ends with “_gnd” >>> objs = modeler.get_objects_by_name(”[*](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_objects_by_name.html#id1)_gnd”)
# All objects whose name contains “patch” >>> objs = modeler.get_objects_by_name(” _patch_ ”, case_sensitive=False)
# Mid-string wildcard: names like “Sub_1”, “Sub_gnd_1”. >>> objs = modeler.get_objects_by_name(“Sub*_1”)
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_objects_by_name.rst.txt)

# get_objects_by_name 

Modeler2D.get_objects_by_name(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _case_sensitive : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Return the objects whose names match a wildcard pattern.
The `*` character acts as a wildcard that matches any sequence of characters (including none). The matching mode is inferred automatically from the position of `*` in `assignment`: 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Wildcard pattern to match against object names. Use `*` as a wildcard for any sequence of characters. 

**case_sensitive**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the match is case-sensitive. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Objects whose names satisfy the pattern.
Examples
# Exact match >>> objs = modeler.get_objects_by_name(“Patch_1”)
# All objects whose name starts with “Substrate” >>> objs = modeler.get_objects_by_name(“Substrate*”)
# All objects whose name ends with “_gnd” >>> objs = modeler.get_objects_by_name(”[*](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_objects_by_name.html#id1)_gnd”)
# All objects whose name contains “patch” >>> objs = modeler.get_objects_by_name(” _patch_ ”, case_sensitive=False)
# Mid-string wildcard: names like “Sub_1”, “Sub_gnd_1”. >>> objs = modeler.get_objects_by_name(“Sub*_1”)