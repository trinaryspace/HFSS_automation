---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.are_segments_intersecting.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# are_segments_intersecting 

static GeometryOperators.are_segments_intersecting(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _include_collinear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if the two segments a and b are intersecting. 

a1List 
    
First point of segment a. List of `[x, y]` coordinates. 

a2List 
    
Second point of segment a. List of `[x, y]` coordinates. 

b1List 
    
First point of segment b. List of `[x, y]` coordinates. 

b2List 
    
Second point of segment b. List of `[x, y]` coordinates. 

include_collinearbool 
    
If `True` two segments are considered intersecting also if just one end lies on the other segment. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the segments are intersecting. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.are_segments_intersecting(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard
# are_segments_intersecting 

static GeometryOperators.are_segments_intersecting(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _include_collinear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if the two segments a and b are intersecting. 

a1List 
    
First point of segment a. List of `[x, y]` coordinates. 

a2List 
    
Second point of segment a. List of `[x, y]` coordinates. 

b1List 
    
First point of segment b. List of `[x, y]` coordinates. 

b2List 
    
Second point of segment b. List of `[x, y]` coordinates. 

include_collinearbool 
    
If `True` two segments are considered intersecting also if just one end lies on the other segment. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the segments are intersecting. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.are_segments_intersecting(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.are_segments_intersecting.rst.txt)

# are_segments_intersecting 

static GeometryOperators.are_segments_intersecting(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _include_collinear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if the two segments a and b are intersecting. 

a1List 
    
First point of segment a. List of `[x, y]` coordinates. 

a2List 
    
Second point of segment a. List of `[x, y]` coordinates. 

b1List 
    
First point of segment b. List of `[x, y]` coordinates. 

b2List 
    
Second point of segment b. List of `[x, y]` coordinates. 

include_collinearbool 
    
If `True` two segments are considered intersecting also if just one end lies on the other segment. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the segments are intersecting. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.are_segments_intersecting(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard