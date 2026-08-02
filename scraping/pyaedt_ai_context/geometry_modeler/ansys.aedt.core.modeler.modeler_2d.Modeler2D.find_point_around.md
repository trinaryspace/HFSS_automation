---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.find_point_around.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# find_point_around 

Modeler2D.find_point_around(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the point around an object. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the starting position of the object. 

**offset**
    
Offset to apply. 

**plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate plane of the arc. Choices are `"YZ"`, `"ZX"`, and `"XY"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates for the point.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_point_around(assignment="Box1", origin=[0, 0, 0], offset="1mm", plane="XY")

```
Copy to clipboard
# find_point_around 

Modeler2D.find_point_around(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the point around an object. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the starting position of the object. 

**offset**
    
Offset to apply. 

**plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate plane of the arc. Choices are `"YZ"`, `"ZX"`, and `"XY"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates for the point.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_point_around(assignment="Box1", origin=[0, 0, 0], offset="1mm", plane="XY")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.find_point_around.rst.txt)

# find_point_around 

Modeler2D.find_point_around(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the point around an object. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the starting position of the object. 

**offset**
    
Offset to apply. 

**plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coordinate plane of the arc. Choices are `"YZ"`, `"ZX"`, and `"XY"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates for the point.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_point_around(assignment="Box1", origin=[0, 0, 0], offset="1mm", plane="XY")

```
Copy to clipboard