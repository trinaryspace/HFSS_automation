---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_face_center.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_face_center 

Modeler3D.get_face_center(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the center position for a given planar face ID. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the face. 

Returns: 
     

`List`
    
A list of `[x, y, z]` coordinates for the planar face center position.
References

```
>>> oEditor.GetFaceCenter

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_face_center(assignment="Box1")

```
Copy to clipboard
# get_face_center 

Modeler3D.get_face_center(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the center position for a given planar face ID. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the face. 

Returns: 
     

`List`
    
A list of `[x, y, z]` coordinates for the planar face center position.
References

```
>>> oEditor.GetFaceCenter

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_face_center(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_face_center.rst.txt)

# get_face_center 

Modeler3D.get_face_center(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the center position for a given planar face ID. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the face. 

Returns: 
     

`List`
    
A list of `[x, y, z]` coordinates for the planar face center position.
References

```
>>> oEditor.GetFaceCenter

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_face_center(assignment="Box1")

```
Copy to clipboard