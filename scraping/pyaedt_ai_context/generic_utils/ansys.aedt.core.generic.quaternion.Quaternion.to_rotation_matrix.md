---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# to_rotation_matrix 

Quaternion.to_rotation_matrix() → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Returns the rotation matrix corresponding to the quaternion. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
A 3×3 rotation matrix equivalent to the quaternion’s rotation. The matrix is provided in the form: ((m00, m01, m02), (m10, m11, m12), (m20, m21, m22))
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)
>>> rotation_matrix = q.to_rotation_matrix()
>>> rotation_matrix
((0.7053456158585982, 0.07053456158585963, 0.7053456158585982),
 (0.19470872568244832, 0.937486456989565, -0.2884573713814046),
 (-0.681598176590997, 0.34079908829549865, 0.6475182677614472))

```
Copy to clipboard
# to_rotation_matrix 

Quaternion.to_rotation_matrix() → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Returns the rotation matrix corresponding to the quaternion. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
A 3×3 rotation matrix equivalent to the quaternion’s rotation. The matrix is provided in the form: ((m00, m01, m02), (m10, m11, m12), (m20, m21, m22))
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)
>>> rotation_matrix = q.to_rotation_matrix()
>>> rotation_matrix
((0.7053456158585982, 0.07053456158585963, 0.7053456158585982),
 (0.19470872568244832, 0.937486456989565, -0.2884573713814046),
 (-0.681598176590997, 0.34079908829549865, 0.6475182677614472))

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix.rst.txt)

# to_rotation_matrix 

Quaternion.to_rotation_matrix() → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Returns the rotation matrix corresponding to the quaternion. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
A 3×3 rotation matrix equivalent to the quaternion’s rotation. The matrix is provided in the form: ((m00, m01, m02), (m10, m11, m12), (m20, m21, m22))
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q = Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)
>>> rotation_matrix = q.to_rotation_matrix()
>>> rotation_matrix
((0.7053456158585982, 0.07053456158585963, 0.7053456158585982),
 (0.19470872568244832, 0.937486456989565, -0.2884573713814046),
 (-0.681598176590997, 0.34079908829549865, 0.6475182677614472))

```
Copy to clipboard