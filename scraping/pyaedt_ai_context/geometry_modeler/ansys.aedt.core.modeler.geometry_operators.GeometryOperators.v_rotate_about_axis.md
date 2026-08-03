---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_rotate_about_axis.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# v_rotate_about_axis 

static GeometryOperators.v_rotate_about_axis(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _radians : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'z'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate rotation of a vector around an axis. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the three component of the vector. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Angle by which the vector is to be rotated (radians or degree). 

**radians**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the angle is expressed in radians. Default is `False`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Axis about which to rotate the vector. Default is `"z"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of values for the result vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_rotate_about_axis(vector=[1, 0, 0], angle=45)

```
Copy to clipboard
# v_rotate_about_axis 

static GeometryOperators.v_rotate_about_axis(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _radians : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'z'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate rotation of a vector around an axis. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the three component of the vector. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Angle by which the vector is to be rotated (radians or degree). 

**radians**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the angle is expressed in radians. Default is `False`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Axis about which to rotate the vector. Default is `"z"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of values for the result vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_rotate_about_axis(vector=[1, 0, 0], angle=45)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_rotate_about_axis.rst.txt)

# v_rotate_about_axis 

static GeometryOperators.v_rotate_about_axis(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _radians : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'z'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Evaluate rotation of a vector around an axis. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the three component of the vector. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Angle by which the vector is to be rotated (radians or degree). 

**radians**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the angle is expressed in radians. Default is `False`. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Axis about which to rotate the vector. Default is `"z"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of values for the result vector.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_rotate_about_axis(vector=[1, 0, 0], angle=45)

```
Copy to clipboard