---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_prod.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# v_prod 

static GeometryOperators.v_prod(_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _v : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate the product between a scalar value and a vector. 

Parameters: 
     

**s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Scalar value. 

**v**`List` 
    
List of values for the vector in the format `[v1, v2,..., vn]`. The vector can be any length. 

Returns: 
     

`List`
    
List of values for the result vector. This list is the same length as the list for the input vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_prod(s=2, v=[0, 1, 0])

```
Copy to clipboard
# v_prod 

static GeometryOperators.v_prod(_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _v : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate the product between a scalar value and a vector. 

Parameters: 
     

**s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Scalar value. 

**v**`List` 
    
List of values for the vector in the format `[v1, v2,..., vn]`. The vector can be any length. 

Returns: 
     

`List`
    
List of values for the result vector. This list is the same length as the list for the input vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_prod(s=2, v=[0, 1, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_prod.rst.txt)

# v_prod 

static GeometryOperators.v_prod(_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _v : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate the product between a scalar value and a vector. 

Parameters: 
     

**s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Scalar value. 

**v**`List` 
    
List of values for the vector in the format `[v1, v2,..., vn]`. The vector can be any length. 

Returns: 
     

`List`
    
List of values for the result vector. This list is the same length as the list for the input vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_prod(s=2, v=[0, 1, 0])

```
Copy to clipboard