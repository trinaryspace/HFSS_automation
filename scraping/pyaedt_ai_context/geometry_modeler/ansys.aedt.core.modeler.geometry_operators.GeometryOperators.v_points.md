---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_points.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# v_points 

static GeometryOperators.v_points(_p1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _p2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Vector from one point to another point. 

Parameters: 
     

**p1**`List` 
    
Coordinates `[x1,y1,z1]` for the first point. 

**p2**`List` 
    
Coordinates `[x2,y2,z2]` for second point. 

Returns: 
     

`List`
    
Coordinates `[vx, vy, vz]` for the vector from the first point to the second point.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_points(p1=[0, 0, 0], p2=[10, 0, 0])

```
Copy to clipboard
# v_points 

static GeometryOperators.v_points(_p1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _p2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Vector from one point to another point. 

Parameters: 
     

**p1**`List` 
    
Coordinates `[x1,y1,z1]` for the first point. 

**p2**`List` 
    
Coordinates `[x2,y2,z2]` for second point. 

Returns: 
     

`List`
    
Coordinates `[vx, vy, vz]` for the vector from the first point to the second point.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_points(p1=[0, 0, 0], p2=[10, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_points.rst.txt)

# v_points 

static GeometryOperators.v_points(_p1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _p2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Vector from one point to another point. 

Parameters: 
     

**p1**`List` 
    
Coordinates `[x1,y1,z1]` for the first point. 

**p2**`List` 
    
Coordinates `[x2,y2,z2]` for second point. 

Returns: 
     

`List`
    
Coordinates `[vx, vy, vz]` for the vector from the first point to the second point.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_points(p1=[0, 0, 0], p2=[10, 0, 0])

```
Copy to clipboard