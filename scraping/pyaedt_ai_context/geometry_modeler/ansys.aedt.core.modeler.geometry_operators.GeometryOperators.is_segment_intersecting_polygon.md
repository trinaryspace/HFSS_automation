---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_segment_intersecting_polygon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_segment_intersecting_polygon 

static GeometryOperators.is_segment_intersecting_polygon(_a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if a segment defined by two points `a` and `b` intersects a polygon.
Points on the vertices and on the polygon boundaries are not considered intersecting. 

Parameters: 
     

**a**`List` 
    
First point of the segment. List of `[x, y]` coordinates. 

**b**`List` 
    
Second point of the segment. List of `[x, y]` coordinates. 

**polygon**`List` 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
`True` if the segment intersect the polygon. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_segment_intersecting_polygon(a=[1, 0, 0], b=[0, 1, 0], polygon=["Box1"])

```
Copy to clipboard
# is_segment_intersecting_polygon 

static GeometryOperators.is_segment_intersecting_polygon(_a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if a segment defined by two points `a` and `b` intersects a polygon.
Points on the vertices and on the polygon boundaries are not considered intersecting. 

Parameters: 
     

**a**`List` 
    
First point of the segment. List of `[x, y]` coordinates. 

**b**`List` 
    
Second point of the segment. List of `[x, y]` coordinates. 

**polygon**`List` 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
`True` if the segment intersect the polygon. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_segment_intersecting_polygon(a=[1, 0, 0], b=[0, 1, 0], polygon=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_segment_intersecting_polygon.rst.txt)

# is_segment_intersecting_polygon 

static GeometryOperators.is_segment_intersecting_polygon(_a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if a segment defined by two points `a` and `b` intersects a polygon.
Points on the vertices and on the polygon boundaries are not considered intersecting. 

Parameters: 
     

**a**`List` 
    
First point of the segment. List of `[x, y]` coordinates. 

**b**`List` 
    
Second point of the segment. List of `[x, y]` coordinates. 

**polygon**`List` 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
`True` if the segment intersect the polygon. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_segment_intersecting_polygon(a=[1, 0, 0], b=[0, 1, 0], polygon=["Box1"])

```
Copy to clipboard