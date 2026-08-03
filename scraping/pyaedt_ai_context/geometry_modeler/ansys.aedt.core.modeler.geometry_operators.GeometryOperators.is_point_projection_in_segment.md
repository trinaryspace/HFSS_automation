---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_point_projection_in_segment.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_point_projection_in_segment 

static GeometryOperators.is_point_projection_in_segment(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a point projection lies on the segment defined by two points. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the projection point lies on the segment defined by the two points, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_point_projection_in_segment(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
# is_point_projection_in_segment 

static GeometryOperators.is_point_projection_in_segment(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a point projection lies on the segment defined by two points. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the projection point lies on the segment defined by the two points, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_point_projection_in_segment(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_point_projection_in_segment.rst.txt)

# is_point_projection_in_segment 

static GeometryOperators.is_point_projection_in_segment(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a point projection lies on the segment defined by two points. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the projection point lies on the segment defined by the two points, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_point_projection_in_segment(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard