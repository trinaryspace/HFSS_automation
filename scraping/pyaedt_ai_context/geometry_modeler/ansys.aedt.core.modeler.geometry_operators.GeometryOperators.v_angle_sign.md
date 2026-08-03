---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_angle_sign.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# v_angle_sign 

static GeometryOperators.v_angle_sign(_va : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vb : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vn : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _right_handed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the signed angle between two geometry vectors.
The sign is evaluated respect to the normal to the plane containing the two vectors as per the following rule. In case of opposite vectors, it returns an angle equal to 180deg (always positive). Assuming that the plane normal is normalized (vb == 1), the signed angle is simplified. For the right-handed rotation from Va to Vb: - atan2((va x Vb) . vn, va . vb). For the left-handed rotation from Va to Vb: - atan2((Vb x va) . vn, va . vb). 

Parameters: 
     

**va**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**vb**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**vn**`List` 
    
List of `[x, y, z]` coordinates for the plane normal. 

**right_handed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to consider the right-handed rotation from va to vb. The default is `True`. When `False`, left-hand rotation from va to vb is considered. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Angle in radians.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_angle_sign(va=["Box1"], vb=["Box1"], vn=["Box1"])

```
Copy to clipboard
# v_angle_sign 

static GeometryOperators.v_angle_sign(_va : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vb : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vn : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _right_handed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the signed angle between two geometry vectors.
The sign is evaluated respect to the normal to the plane containing the two vectors as per the following rule. In case of opposite vectors, it returns an angle equal to 180deg (always positive). Assuming that the plane normal is normalized (vb == 1), the signed angle is simplified. For the right-handed rotation from Va to Vb: - atan2((va x Vb) . vn, va . vb). For the left-handed rotation from Va to Vb: - atan2((Vb x va) . vn, va . vb). 

Parameters: 
     

**va**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**vb**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**vn**`List` 
    
List of `[x, y, z]` coordinates for the plane normal. 

**right_handed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to consider the right-handed rotation from va to vb. The default is `True`. When `False`, left-hand rotation from va to vb is considered. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Angle in radians.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_angle_sign(va=["Box1"], vb=["Box1"], vn=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.v_angle_sign.rst.txt)

# v_angle_sign 

static GeometryOperators.v_angle_sign(_va : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vb : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vn : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _right_handed : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the signed angle between two geometry vectors.
The sign is evaluated respect to the normal to the plane containing the two vectors as per the following rule. In case of opposite vectors, it returns an angle equal to 180deg (always positive). Assuming that the plane normal is normalized (vb == 1), the signed angle is simplified. For the right-handed rotation from Va to Vb: - atan2((va x Vb) . vn, va . vb). For the left-handed rotation from Va to Vb: - atan2((Vb x va) . vn, va . vb). 

Parameters: 
     

**va**`List` 
    
List of `[x, y, z]` coordinates for the first vector. 

**vb**`List` 
    
List of `[x, y, z]` coordinates for the second vector. 

**vn**`List` 
    
List of `[x, y, z]` coordinates for the plane normal. 

**right_handed**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to consider the right-handed rotation from va to vb. The default is `True`. When `False`, left-hand rotation from va to vb is considered. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Angle in radians.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.v_angle_sign(va=["Box1"], vb=["Box1"], vn=["Box1"])

```
Copy to clipboard