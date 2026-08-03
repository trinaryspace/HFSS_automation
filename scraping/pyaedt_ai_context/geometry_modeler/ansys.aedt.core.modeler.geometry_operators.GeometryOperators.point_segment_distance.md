---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.point_segment_distance.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# point_segment_distance 

static GeometryOperators.point_segment_distance(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Calculate the distance between a point `p` and a segment defined by two points `a` and `b`. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Distance between the point and the segment.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.point_segment_distance(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
# point_segment_distance 

static GeometryOperators.point_segment_distance(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Calculate the distance between a point `p` and a segment defined by two points `a` and `b`. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Distance between the point and the segment.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.point_segment_distance(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.point_segment_distance.rst.txt)

# point_segment_distance 

static GeometryOperators.point_segment_distance(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Calculate the distance between a point `p` and a segment defined by two points `a` and `b`. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Distance between the point and the segment.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.point_segment_distance(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard