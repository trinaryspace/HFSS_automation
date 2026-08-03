---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# from_rotation_matrix 

classmethod Quaternion.from_rotation_matrix(_rotation_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Converts a 3x3 rotation matrix to a quaternion. It uses the method described in [1]. 

Parameters: 
     

**rotation_matrix: List or tuple**
    
Rotation matrix defined as a list of lists or a tuple of tuples. The matrix should be 3x3 and orthogonal. The matrix is assumed to be in the form: ((m00, m01, m02), (m10, m11, m12), (m20, m21, m22)) 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
The quaternion defined by the rotation matrix.
References
[1] <https://doi.org/10.1145/325334.325242> (pp. 245-254)
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> x = (0.7053456158585982, 0.07053456158585963, 0.7053456158585982)
>>> y = (0.19470872568244832, 0.937486456989565, -0.2884573713814046)
>>> z = (-0.681598176590997, 0.34079908829549865, 0.6475182677614472)
>>> rotation_matrix = Quaternion.axis_to_rotation_matrix(x, y, z)
>>> q = Quaternion.from_rotation_matrix(rotation_matrix)
>>> q
Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)

```
Copy to clipboard
# from_rotation_matrix 

classmethod Quaternion.from_rotation_matrix(_rotation_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Converts a 3x3 rotation matrix to a quaternion. It uses the method described in [1]. 

Parameters: 
     

**rotation_matrix: List or tuple**
    
Rotation matrix defined as a list of lists or a tuple of tuples. The matrix should be 3x3 and orthogonal. The matrix is assumed to be in the form: ((m00, m01, m02), (m10, m11, m12), (m20, m21, m22)) 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
The quaternion defined by the rotation matrix.
References
[1] <https://doi.org/10.1145/325334.325242> (pp. 245-254)
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> x = (0.7053456158585982, 0.07053456158585963, 0.7053456158585982)
>>> y = (0.19470872568244832, 0.937486456989565, -0.2884573713814046)
>>> z = (-0.681598176590997, 0.34079908829549865, 0.6475182677614472)
>>> rotation_matrix = Quaternion.axis_to_rotation_matrix(x, y, z)
>>> q = Quaternion.from_rotation_matrix(rotation_matrix)
>>> q
Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix.rst.txt)

# from_rotation_matrix 

classmethod Quaternion.from_rotation_matrix(_rotation_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Converts a 3x3 rotation matrix to a quaternion. It uses the method described in [1]. 

Parameters: 
     

**rotation_matrix: List or tuple**
    
Rotation matrix defined as a list of lists or a tuple of tuples. The matrix should be 3x3 and orthogonal. The matrix is assumed to be in the form: ((m00, m01, m02), (m10, m11, m12), (m20, m21, m22)) 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
The quaternion defined by the rotation matrix.
References
[1] <https://doi.org/10.1145/325334.325242> (pp. 245-254)
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> x = (0.7053456158585982, 0.07053456158585963, 0.7053456158585982)
>>> y = (0.19470872568244832, 0.937486456989565, -0.2884573713814046)
>>> z = (-0.681598176590997, 0.34079908829549865, 0.6475182677614472)
>>> rotation_matrix = Quaternion.axis_to_rotation_matrix(x, y, z)
>>> q = Quaternion.from_rotation_matrix(rotation_matrix)
>>> q
Quaternion(0.9069661433330367, -0.17345092325178477, -0.3823030778615049, -0.03422789400943274)

```
Copy to clipboard