---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_euler.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# to_euler 

Quaternion.to_euler(_sequence : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extrinsic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Converts the quaternion to Euler angles using the specified rotation sequence.
The conversion follows the method described in [1]. In degenerate (gimbal lock) cases, the third angle is set to zero for stability. 

Parameters: 
     

**sequence**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A three-character string indicating the rotation axis sequence (e.g., “xyz” or “ZYX”). It is case-insensitive and must contain only the characters ‘x’, ‘y’, or ‘z’. 

**extrinsic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True`, the rotation is treated as extrinsic. If `False` (default), it is treated as intrinsic. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
A tuple of three Euler angles representing the same rotation as the quaternion. Angle in radians.
References
[1] <https://doi.org/10.1371/journal.pone.0276302> [2] <https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles>
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)
>>> q.to_euler("zxz")
(-2.0344439357957027, 0.8664730673456006, 1.9590019609437583)
>>> q.to_euler("zyz")
(2.677945044588987, 0.8664730673456006, -2.7533870194409316)

```
Copy to clipboard
# to_euler 

Quaternion.to_euler(_sequence : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extrinsic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Converts the quaternion to Euler angles using the specified rotation sequence.
The conversion follows the method described in [1]. In degenerate (gimbal lock) cases, the third angle is set to zero for stability. 

Parameters: 
     

**sequence**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A three-character string indicating the rotation axis sequence (e.g., “xyz” or “ZYX”). It is case-insensitive and must contain only the characters ‘x’, ‘y’, or ‘z’. 

**extrinsic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True`, the rotation is treated as extrinsic. If `False` (default), it is treated as intrinsic. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
A tuple of three Euler angles representing the same rotation as the quaternion. Angle in radians.
References
[1] <https://doi.org/10.1371/journal.pone.0276302> [2] <https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles>
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)
>>> q.to_euler("zxz")
(-2.0344439357957027, 0.8664730673456006, 1.9590019609437583)
>>> q.to_euler("zyz")
(2.677945044588987, 0.8664730673456006, -2.7533870194409316)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_euler.rst.txt)

# to_euler 

Quaternion.to_euler(_sequence : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extrinsic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Converts the quaternion to Euler angles using the specified rotation sequence.
The conversion follows the method described in [1]. In degenerate (gimbal lock) cases, the third angle is set to zero for stability. 

Parameters: 
     

**sequence**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A three-character string indicating the rotation axis sequence (e.g., “xyz” or “ZYX”). It is case-insensitive and must contain only the characters ‘x’, ‘y’, or ‘z’. 

**extrinsic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True`, the rotation is treated as extrinsic. If `False` (default), it is treated as intrinsic. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
A tuple of three Euler angles representing the same rotation as the quaternion. Angle in radians.
References
[1] <https://doi.org/10.1371/journal.pone.0276302> [2] <https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles>
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)
>>> q.to_euler("zxz")
(-2.0344439357957027, 0.8664730673456006, 1.9590019609437583)
>>> q.to_euler("zyz")
(2.677945044588987, 0.8664730673456006, -2.7533870194409316)

```
Copy to clipboard