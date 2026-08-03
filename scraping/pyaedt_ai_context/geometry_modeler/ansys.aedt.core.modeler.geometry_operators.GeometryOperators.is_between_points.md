---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_between_points.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_between_points 

static GeometryOperators.is_between_points(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a point lies on the segment defined by two points. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the point lies on the segment defined by the two points, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_between_points(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
# is_between_points 

static GeometryOperators.is_between_points(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a point lies on the segment defined by two points. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the point lies on the segment defined by the two points, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_between_points(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_between_points.rst.txt)

# is_between_points 

static GeometryOperators.is_between_points(_p : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a point lies on the segment defined by two points. 

Parameters: 
     

**p**`List` 
    
List of `[x, y, z]` coordinates for the reference point `p`. 

**a**`List` 
    
List of `[x, y, z]` coordinates for the first point of the segment. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second point of the segment. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the point lies on the segment defined by the two points, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_between_points(p=[0, 0, 0], a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard