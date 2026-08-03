---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_euler.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# from_euler 

classmethod Quaternion.from_euler(_angles : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _sequence : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extrinsic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Creates a normalized rotation quaternion from the Euler angles using the specified rotation sequence. 

Parameters: 
     

**angles**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` 3 `floats` 
    
The Euler angles in radians. 

**sequence**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A three-character string indicating the rotation axis sequence (e.g., “xyz” or “ZYX”). It is case-insensitive and must contain only the characters ‘x’, ‘y’, or ‘z’. 

**extrinsic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True`, the rotation is treated as extrinsic. If `False` (default), it is treated as intrinsic. 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A unit quaternion representing the rotation defined by the Euler angles in the given sequence.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> from math import pi
>>> q = Quaternion.from_euler([pi / 2, 0, 0], "xyz")
>>> q
Quaternion(0.7071067811865476, 0.7071067811865476, 0, 0)

```
Copy to clipboard

```
>>> q = Quaternion.from_euler([0, pi / 2, pi], "zyz", extrinsic=True)
>>> q
Quaternion(0, -0.7071067811865476, 0, 0.7071067811865476)

```
Copy to clipboard

```
>>> q = Quaternion.from_euler([0, pi / 2, pi], "zyz")
>>> q
Quaternion(0, 0.7071067811865476, 0, 0.7071067811865476)

```
Copy to clipboard
# from_euler 

classmethod Quaternion.from_euler(_angles : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _sequence : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extrinsic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Creates a normalized rotation quaternion from the Euler angles using the specified rotation sequence. 

Parameters: 
     

**angles**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` 3 `floats` 
    
The Euler angles in radians. 

**sequence**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A three-character string indicating the rotation axis sequence (e.g., “xyz” or “ZYX”). It is case-insensitive and must contain only the characters ‘x’, ‘y’, or ‘z’. 

**extrinsic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True`, the rotation is treated as extrinsic. If `False` (default), it is treated as intrinsic. 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A unit quaternion representing the rotation defined by the Euler angles in the given sequence.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> from math import pi
>>> q = Quaternion.from_euler([pi / 2, 0, 0], "xyz")
>>> q
Quaternion(0.7071067811865476, 0.7071067811865476, 0, 0)

```
Copy to clipboard

```
>>> q = Quaternion.from_euler([0, pi / 2, pi], "zyz", extrinsic=True)
>>> q
Quaternion(0, -0.7071067811865476, 0, 0.7071067811865476)

```
Copy to clipboard

```
>>> q = Quaternion.from_euler([0, pi / 2, pi], "zyz")
>>> q
Quaternion(0, 0.7071067811865476, 0, 0.7071067811865476)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_euler.rst.txt)

# from_euler 

classmethod Quaternion.from_euler(_angles : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _sequence : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extrinsic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Creates a normalized rotation quaternion from the Euler angles using the specified rotation sequence. 

Parameters: 
     

**angles**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` 3 `floats` 
    
The Euler angles in radians. 

**sequence**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A three-character string indicating the rotation axis sequence (e.g., “xyz” or “ZYX”). It is case-insensitive and must contain only the characters ‘x’, ‘y’, or ‘z’. 

**extrinsic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True`, the rotation is treated as extrinsic. If `False` (default), it is treated as intrinsic. 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A unit quaternion representing the rotation defined by the Euler angles in the given sequence.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> from math import pi
>>> q = Quaternion.from_euler([pi / 2, 0, 0], "xyz")
>>> q
Quaternion(0.7071067811865476, 0.7071067811865476, 0, 0)

```
Copy to clipboard

```
>>> q = Quaternion.from_euler([0, pi / 2, pi], "zyz", extrinsic=True)
>>> q
Quaternion(0, -0.7071067811865476, 0, 0.7071067811865476)

```
Copy to clipboard

```
>>> q = Quaternion.from_euler([0, pi / 2, pi], "zyz")
>>> q
Quaternion(0, 0.7071067811865476, 0, 0.7071067811865476)

```
Copy to clipboard