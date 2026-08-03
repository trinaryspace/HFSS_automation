---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# rotate_vector 

Quaternion.rotate_vector(_v : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Evaluate the rotation of a vector, defined by a quaternion.
Evaluated as: `"q = q0 + q' = q0 + q1i + q2j + q3k"`, `"w = qvq* = (q0^2 - |q'|^2)v + 2(q' • v)q' + 2q0(q' x v)"`. 

Parameters: 
     

**v**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or `List` 
    
`(x, y, z)` coordinates for the vector to be rotated. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
`(w1, w2, w3)` coordinates for the rotated vector `w`.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)
>>> v = (1, 0, 0)
>>> q.rotate_vector(v)
(0.7071067811865475, 0.0, 0.7071067811865476)

```
Copy to clipboard
# rotate_vector 

Quaternion.rotate_vector(_v : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Evaluate the rotation of a vector, defined by a quaternion.
Evaluated as: `"q = q0 + q' = q0 + q1i + q2j + q3k"`, `"w = qvq* = (q0^2 - |q'|^2)v + 2(q' • v)q' + 2q0(q' x v)"`. 

Parameters: 
     

**v**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or `List` 
    
`(x, y, z)` coordinates for the vector to be rotated. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
`(w1, w2, w3)` coordinates for the rotated vector `w`.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)
>>> v = (1, 0, 0)
>>> q.rotate_vector(v)
(0.7071067811865475, 0.0, 0.7071067811865476)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector.rst.txt)

# rotate_vector 

Quaternion.rotate_vector(_v : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Evaluate the rotation of a vector, defined by a quaternion.
Evaluated as: `"q = q0 + q' = q0 + q1i + q2j + q3k"`, `"w = qvq* = (q0^2 - |q'|^2)v + 2(q' • v)q' + 2q0(q' x v)"`. 

Parameters: 
     

**v**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or `List` 
    
`(x, y, z)` coordinates for the vector to be rotated. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
`(w1, w2, w3)` coordinates for the rotated vector `w`.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)
>>> v = (1, 0, 0)
>>> q.rotate_vector(v)
(0.7071067811865475, 0.0, 0.7071067811865476)

```
Copy to clipboard