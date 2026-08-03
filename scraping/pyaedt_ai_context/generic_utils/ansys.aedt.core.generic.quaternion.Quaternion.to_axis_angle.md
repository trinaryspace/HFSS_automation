---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# to_axis_angle 

Quaternion.to_axis_angle() 
    
Convert a quaternion to the axis angle rotation formulation. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
((ux, uy, uz), theta) containing the rotation axes expressed as X, Y, Z components of the unit vector `u` and the rotation angle theta expressed in radians.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(1, 1, 1, 1)
>>> (axis, angle) = q.to_axis_angle()
>>> axis
(0.5773502691896257, 0.5773502691896257, 0.5773502691896257)
>>> angle
2.0943951023931953

```
Copy to clipboard
# to_axis_angle 

Quaternion.to_axis_angle() 
    
Convert a quaternion to the axis angle rotation formulation. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
((ux, uy, uz), theta) containing the rotation axes expressed as X, Y, Z components of the unit vector `u` and the rotation angle theta expressed in radians.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(1, 1, 1, 1)
>>> (axis, angle) = q.to_axis_angle()
>>> axis
(0.5773502691896257, 0.5773502691896257, 0.5773502691896257)
>>> angle
2.0943951023931953

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle.rst.txt)

# to_axis_angle 

Quaternion.to_axis_angle() 
    
Convert a quaternion to the axis angle rotation formulation. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
((ux, uy, uz), theta) containing the rotation axes expressed as X, Y, Z components of the unit vector `u` and the rotation angle theta expressed in radians.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(1, 1, 1, 1)
>>> (axis, angle) = q.to_axis_angle()
>>> axis
(0.5773502691896257, 0.5773502691896257, 0.5773502691896257)
>>> angle
2.0943951023931953

```
Copy to clipboard