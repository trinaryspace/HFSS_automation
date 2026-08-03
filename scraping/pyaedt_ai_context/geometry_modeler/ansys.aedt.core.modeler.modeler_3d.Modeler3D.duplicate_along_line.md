---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.duplicate_along_line.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# duplicate_along_line 

Modeler3D.duplicate_along_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _attach : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_3d_comp : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _duplicate_assignment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Duplicate a selection along a line. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Name or ID of the object. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1,y1,z1]` coordinates or the Application.Position object for the vector. 

**attach**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**is_3d_comp**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If True, the method will try to return the duplicated list of 3dcomponents. The default is `False`. 

**duplicate_assignment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If True, the method duplicates selection assignments. The default value is `True`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
References

```
>>> oEditor.DuplicateAlongLine

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.duplicate_along_line(assignment="Box1", vector=[1, 0, 0])

```
Copy to clipboard
# duplicate_along_line 

Modeler3D.duplicate_along_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _attach : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_3d_comp : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _duplicate_assignment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Duplicate a selection along a line. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Name or ID of the object. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1,y1,z1]` coordinates or the Application.Position object for the vector. 

**attach**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**is_3d_comp**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If True, the method will try to return the duplicated list of 3dcomponents. The default is `False`. 

**duplicate_assignment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If True, the method duplicates selection assignments. The default value is `True`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
References

```
>>> oEditor.DuplicateAlongLine

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.duplicate_along_line(assignment="Box1", vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.duplicate_along_line.rst.txt)

# duplicate_along_line 

Modeler3D.duplicate_along_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _attach : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_3d_comp : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _duplicate_assignment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Duplicate a selection along a line. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Name or ID of the object. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1,y1,z1]` coordinates or the Application.Position object for the vector. 

**attach**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**is_3d_comp**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If True, the method will try to return the duplicated list of 3dcomponents. The default is `False`. 

**duplicate_assignment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If True, the method duplicates selection assignments. The default value is `True`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
References

```
>>> oEditor.DuplicateAlongLine

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.duplicate_along_line(assignment="Box1", vector=[1, 0, 0])

```
Copy to clipboard