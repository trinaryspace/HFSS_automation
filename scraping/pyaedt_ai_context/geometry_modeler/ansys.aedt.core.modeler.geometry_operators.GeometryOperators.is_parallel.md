---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_parallel.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_parallel 

static GeometryOperators.is_parallel(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a segment defined by two points is parallel to a segment defined by two other points. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the fiirst segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the first segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the second segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the second segment. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_parallel(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard
# is_parallel 

static GeometryOperators.is_parallel(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a segment defined by two points is parallel to a segment defined by two other points. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the fiirst segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the first segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the second segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the second segment. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_parallel(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_parallel.rst.txt)

# is_parallel 

static GeometryOperators.is_parallel(_a1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _a2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _b2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a segment defined by two points is parallel to a segment defined by two other points. 

Parameters: 
     

**a1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the fiirst segment. 

**a2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the first segment. 

**b1**`List` 
    
List of `[x, y, z]` coordinates for the first point of the second segment. 

**b2**`List` 
    
List of `[x, y, z]` coordinates for the second point of the second segment. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Linear tolerance. The default value is `1e-6`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_parallel(a1=["Box1"], a2=["Box1"], b1=["Box1"], b2=["Box1"])

```
Copy to clipboard