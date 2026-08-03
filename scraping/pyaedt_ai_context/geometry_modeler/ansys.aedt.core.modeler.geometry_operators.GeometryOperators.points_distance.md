---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.points_distance.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# points_distance 

static GeometryOperators.points_distance(_p1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _p2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the distance between two points expressed as their Cartesian coordinates. 

Parameters: 
     

**p1**`List` 
    
List of `[x1,y1,z1]` coordinates for the first point. 

**p2**`List` 
    
List of `[x2,y2,z2]` coordinates for the second ppint. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Distance between the two points in the same unit as the coordinates for the points.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.points_distance(p1=[0, 0, 0], p2=[10, 0, 0])

```
Copy to clipboard
# points_distance 

static GeometryOperators.points_distance(_p1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _p2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the distance between two points expressed as their Cartesian coordinates. 

Parameters: 
     

**p1**`List` 
    
List of `[x1,y1,z1]` coordinates for the first point. 

**p2**`List` 
    
List of `[x2,y2,z2]` coordinates for the second ppint. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Distance between the two points in the same unit as the coordinates for the points.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.points_distance(p1=[0, 0, 0], p2=[10, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.points_distance.rst.txt)

# points_distance 

static GeometryOperators.points_distance(_p1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _p2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the distance between two points expressed as their Cartesian coordinates. 

Parameters: 
     

**p1**`List` 
    
List of `[x1,y1,z1]` coordinates for the first point. 

**p2**`List` 
    
List of `[x2,y2,z2]` coordinates for the second ppint. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Distance between the two points in the same unit as the coordinates for the points.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.points_distance(p1=[0, 0, 0], p2=[10, 0, 0])

```
Copy to clipboard