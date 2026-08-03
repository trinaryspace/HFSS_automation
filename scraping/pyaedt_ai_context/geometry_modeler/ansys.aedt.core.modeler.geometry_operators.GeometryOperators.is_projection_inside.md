---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_projection_inside.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_projection_inside 

static GeometryOperators.is_projection_inside(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Project a segment onto another segment and check if the projected segment is inside it. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the projected segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the projected segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the other segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the other segment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the projected segment is inside the other segment, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_projection_inside(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard
# is_projection_inside 

static GeometryOperators.is_projection_inside(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Project a segment onto another segment and check if the projected segment is inside it. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the projected segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the projected segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the other segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the other segment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the projected segment is inside the other segment, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_projection_inside(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_projection_inside.rst.txt)

# is_projection_inside 

static GeometryOperators.is_projection_inside(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Project a segment onto another segment and check if the projected segment is inside it. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the projected segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the projected segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the other segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the other segment. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the projected segment is inside the other segment, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_projection_inside(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard