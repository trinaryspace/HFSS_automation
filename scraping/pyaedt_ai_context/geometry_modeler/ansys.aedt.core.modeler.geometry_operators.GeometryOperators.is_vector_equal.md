---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_vector_equal.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_vector_equal 

static GeometryOperators.is_vector_equal(_v1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return `True` if two vectors are equal. 

Parameters: 
     

**v1**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**v2**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Linear tolerance. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the two vectors are equal, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_vector_equal(v1=[0, 0, 0], v2=[10, 0, 0])

```
Copy to clipboard
# is_vector_equal 

static GeometryOperators.is_vector_equal(_v1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return `True` if two vectors are equal. 

Parameters: 
     

**v1**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**v2**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Linear tolerance. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the two vectors are equal, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_vector_equal(v1=[0, 0, 0], v2=[10, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_vector_equal.rst.txt)

# is_vector_equal 

static GeometryOperators.is_vector_equal(_v1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return `True` if two vectors are equal. 

Parameters: 
     

**v1**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**v2**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Linear tolerance. The default value is `None`. If not specified, the value is set to `MathUtils.EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the two vectors are equal, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_vector_equal(v1=[0, 0, 0], v2=[10, 0, 0])

```
Copy to clipboard