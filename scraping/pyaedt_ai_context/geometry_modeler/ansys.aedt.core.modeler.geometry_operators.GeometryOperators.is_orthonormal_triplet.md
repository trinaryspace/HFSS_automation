---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_orthonormal_triplet.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_orthonormal_triplet 

static GeometryOperators.is_orthonormal_triplet(_x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if three vectors are orthonormal. 

Parameters: 
     

**x**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(x1, x2, x3)` coordinates for the first vector. 

**y**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(y1, y2, y3)` coordinates for the second vector. 

**z**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(z1, z2, z3)` coordinates for the third vector. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Linear tolerance. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the three vectors are orthonormal, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_orthonormal_triplet(x=0, y=0, z=0)

```
Copy to clipboard
# is_orthonormal_triplet 

static GeometryOperators.is_orthonormal_triplet(_x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if three vectors are orthonormal. 

Parameters: 
     

**x**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(x1, x2, x3)` coordinates for the first vector. 

**y**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(y1, y2, y3)` coordinates for the second vector. 

**z**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(z1, z2, z3)` coordinates for the third vector. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Linear tolerance. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the three vectors are orthonormal, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_orthonormal_triplet(x=0, y=0, z=0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_orthonormal_triplet.rst.txt)

# is_orthonormal_triplet 

static GeometryOperators.is_orthonormal_triplet(_x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if three vectors are orthonormal. 

Parameters: 
     

**x**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(x1, x2, x3)` coordinates for the first vector. 

**y**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(y1, y2, y3)` coordinates for the second vector. 

**z**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
List of `(z1, z2, z3)` coordinates for the third vector. 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Linear tolerance. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the three vectors are orthonormal, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_orthonormal_triplet(x=0, y=0, z=0)

```
Copy to clipboard