---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_angle_sign_2D.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# v_angle_sign_2D 

static GeometryOperators.v_angle_sign_2D(_va : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vb : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _right_handed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the signed angle between two 2D geometry vectors.
It is the 2D version of the `GeometryOperators.v_angle_sign` considering vn = [0,0,1]. In case of opposite vectors, it returns an angle equal to 180deg (always positive). 

Parameters: 
     

**va**`List` 
    
List of `[x, y]` coordinates for the first vector. 

**vb**`List` 
    
List of `[x, y]` coordinates for the second vector. 

**right_handed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to consider the right-handed rotation from Va to Vb. The default is `True`. When `False`, left-hand rotation from Va to Vb is considered. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Angle in radians.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_angle_sign_2D(va=["Box1"], vb=["Box1"])

```
Copy to clipboard
# v_angle_sign_2D 

static GeometryOperators.v_angle_sign_2D(_va : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vb : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _right_handed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the signed angle between two 2D geometry vectors.
It is the 2D version of the `GeometryOperators.v_angle_sign` considering vn = [0,0,1]. In case of opposite vectors, it returns an angle equal to 180deg (always positive). 

Parameters: 
     

**va**`List` 
    
List of `[x, y]` coordinates for the first vector. 

**vb**`List` 
    
List of `[x, y]` coordinates for the second vector. 

**right_handed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to consider the right-handed rotation from Va to Vb. The default is `True`. When `False`, left-hand rotation from Va to Vb is considered. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Angle in radians.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_angle_sign_2D(va=["Box1"], vb=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_angle_sign_2D.rst.txt)

# v_angle_sign_2D 

static GeometryOperators.v_angle_sign_2D(_va : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vb : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _right_handed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the signed angle between two 2D geometry vectors.
It is the 2D version of the `GeometryOperators.v_angle_sign` considering vn = [0,0,1]. In case of opposite vectors, it returns an angle equal to 180deg (always positive). 

Parameters: 
     

**va**`List` 
    
List of `[x, y]` coordinates for the first vector. 

**vb**`List` 
    
List of `[x, y]` coordinates for the second vector. 

**right_handed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to consider the right-handed rotation from Va to Vb. The default is `True`. When `False`, left-hand rotation from Va to Vb is considered. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Angle in radians.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_angle_sign_2D(va=["Box1"], vb=["Box1"])

```
Copy to clipboard