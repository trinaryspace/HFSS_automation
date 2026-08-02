---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_sheet_to_ground.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_sheet_to_ground 

Modeler2D.create_sheet_to_ground(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ground_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orientation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _sheet_dim : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create a sheet between an object and a ground plane.
The ground plane must be bigger than the object and perpendicular to one of the three axes. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**ground_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ground. The default is `None`, in which case the bounding box is used. 

**orientation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Axis direction. Options are `0` through `5`. The default is `0`. 

**sheet_dim**`optional` 
    
Sheet dimension in millimeters. The default is `1`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the sheet created.
References

```
>>> oEditor.CreatePolyline

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_sheet_to_ground(assignment="Box1")

```
Copy to clipboard
# create_sheet_to_ground 

Modeler2D.create_sheet_to_ground(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ground_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orientation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _sheet_dim : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create a sheet between an object and a ground plane.
The ground plane must be bigger than the object and perpendicular to one of the three axes. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**ground_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ground. The default is `None`, in which case the bounding box is used. 

**orientation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Axis direction. Options are `0` through `5`. The default is `0`. 

**sheet_dim**`optional` 
    
Sheet dimension in millimeters. The default is `1`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the sheet created.
References

```
>>> oEditor.CreatePolyline

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_sheet_to_ground(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_sheet_to_ground.rst.txt)

# create_sheet_to_ground 

Modeler2D.create_sheet_to_ground(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ground_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orientation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _sheet_dim : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create a sheet between an object and a ground plane.
The ground plane must be bigger than the object and perpendicular to one of the three axes. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**ground_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ground. The default is `None`, in which case the bounding box is used. 

**orientation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Axis direction. Options are `0` through `5`. The default is `0`. 

**sheet_dim**`optional` 
    
Sheet dimension in millimeters. The default is `1`. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
ID of the sheet created.
References

```
>>> oEditor.CreatePolyline

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_sheet_to_ground(assignment="Box1")

```
Copy to clipboard