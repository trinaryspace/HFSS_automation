---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.distance_vector.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# distance_vector 

static GeometryOperators.distance_vector(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate the vector distance between point `p` and a line defined by two points, `a` and `b`.
Note
he formula is `d = (a-p)-((a-p)dot p)n`, where `a` is a point of the line (either `a` or `b`) and `n` is the unit vector in the direction of the line. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

`List`
    
List of `[x, y, z]` coordinates for the distance vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.distance_vector(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
# distance_vector 

static GeometryOperators.distance_vector(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate the vector distance between point `p` and a line defined by two points, `a` and `b`.
Note
he formula is `d = (a-p)-((a-p)dot p)n`, where `a` is a point of the line (either `a` or `b`) and `n` is the unit vector in the direction of the line. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

`List`
    
List of `[x, y, z]` coordinates for the distance vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.distance_vector(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.distance_vector.rst.txt)

# distance_vector 

static GeometryOperators.distance_vector(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate the vector distance between point `p` and a line defined by two points, `a` and `b`.
Note
he formula is `d = (a-p)-((a-p)dot p)n`, where `a` is a point of the line (either `a` or `b`) and `n` is the unit vector in the direction of the line. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

`List`
    
List of `[x, y, z]` coordinates for the distance vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.distance_vector(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard