---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.check_plane.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# check_plane 

Modeler3D.check_plane(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _face_location : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Check for the plane that is defined as the face for an object. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Name of the object. 

**face_location**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the position of the face. 

**offset**`optional` 
    
Offset to apply. The default is `1`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the plane. It can be “XY”, “XZ” or “YZ”.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.check_plane(assignment="Box1", face_location=[1])

```
Copy to clipboard
# check_plane 

Modeler3D.check_plane(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _face_location : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Check for the plane that is defined as the face for an object. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Name of the object. 

**face_location**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the position of the face. 

**offset**`optional` 
    
Offset to apply. The default is `1`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the plane. It can be “XY”, “XZ” or “YZ”.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.check_plane(assignment="Box1", face_location=[1])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.check_plane.rst.txt)

# check_plane 

Modeler3D.check_plane(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _face_location : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Check for the plane that is defined as the face for an object. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Name of the object. 

**face_location**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the position of the face. 

**offset**`optional` 
    
Offset to apply. The default is `1`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the plane. It can be “XY”, “XZ” or “YZ”.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.check_plane(assignment="Box1", face_location=[1])

```
Copy to clipboard