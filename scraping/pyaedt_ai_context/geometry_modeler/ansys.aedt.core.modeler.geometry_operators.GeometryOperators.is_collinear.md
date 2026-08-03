---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_collinear.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_collinear 

static GeometryOperators.is_collinear(_a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if two vectors are collinear (parallel or anti-parallel). 

Parameters: 
     

**a**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if vectors are collinear, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_collinear(a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
# is_collinear 

static GeometryOperators.is_collinear(_a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if two vectors are collinear (parallel or anti-parallel). 

Parameters: 
     

**a**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if vectors are collinear, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_collinear(a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_collinear.rst.txt)

# is_collinear 

static GeometryOperators.is_collinear(_a : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if two vectors are collinear (parallel or anti-parallel). 

Parameters: 
     

**a**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**b**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if vectors are collinear, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_collinear(a=[1, 0, 0], b=[0, 1, 0])

```
Copy to clipboard