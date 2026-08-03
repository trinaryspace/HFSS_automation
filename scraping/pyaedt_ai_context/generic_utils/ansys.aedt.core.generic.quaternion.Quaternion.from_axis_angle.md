---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# from_axis_angle 

classmethod Quaternion.from_axis_angle(_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Creates a normalized rotation quaternion from a given axis and rotation angle. 

Parameters: 
     

**axis**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
A 3D vector representing the axis of rotation. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The rotation angle in radians. 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A unit quaternion representing the rotation around the specified axis by the given angle.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> from math import pi, sqrt
>>> Quaternion.from_axis_angle((sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3), 2 * pi / 3)
Quaternion(0.5, 0.5, 0.5, 0.5)

```
Copy to clipboard
# from_axis_angle 

classmethod Quaternion.from_axis_angle(_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Creates a normalized rotation quaternion from a given axis and rotation angle. 

Parameters: 
     

**axis**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
A 3D vector representing the axis of rotation. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The rotation angle in radians. 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A unit quaternion representing the rotation around the specified axis by the given angle.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> from math import pi, sqrt
>>> Quaternion.from_axis_angle((sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3), 2 * pi / 3)
Quaternion(0.5, 0.5, 0.5, 0.5)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle.rst.txt)

# from_axis_angle 

classmethod Quaternion.from_axis_angle(_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Creates a normalized rotation quaternion from a given axis and rotation angle. 

Parameters: 
     

**axis**`List` or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
A 3D vector representing the axis of rotation. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The rotation angle in radians. 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A unit quaternion representing the rotation around the specified axis by the given angle.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> from math import pi, sqrt
>>> Quaternion.from_axis_angle((sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3), 2 * pi / 3)
Quaternion(0.5, 0.5, 0.5, 0.5)

```
Copy to clipboard