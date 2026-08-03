---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# duplicate_and_mirror 

UserDefinedComponent.duplicate_and_mirror(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Duplicate and mirror a selection. 

Parameters: 
     

**origin**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates or Application.Position object for the selection. 

**vector**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x1, y1, z1]` coordinates or Application.Position object for the vector. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of objects created or an empty list.
References

```
>>> oEditor.DuplicateMirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_and_mirror(origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard
# duplicate_and_mirror 

UserDefinedComponent.duplicate_and_mirror(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Duplicate and mirror a selection. 

Parameters: 
     

**origin**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates or Application.Position object for the selection. 

**vector**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x1, y1, z1]` coordinates or Application.Position object for the vector. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of objects created or an empty list.
References

```
>>> oEditor.DuplicateMirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_and_mirror(origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror.rst.txt)

# duplicate_and_mirror 

UserDefinedComponent.duplicate_and_mirror(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Duplicate and mirror a selection. 

Parameters: 
     

**origin**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates or Application.Position object for the selection. 

**vector**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x1, y1, z1]` coordinates or Application.Position object for the vector. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of objects created or an empty list.
References

```
>>> oEditor.DuplicateMirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_and_mirror(origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard