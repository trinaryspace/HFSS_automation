---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# rotation_matrix_to_axis 

static Quaternion.rotation_matrix_to_axis(_rotation_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Convert a rotation matrix to the corresponding axis of rotation. 

Parameters: 
     

**rotation_matrix**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` `tuples` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `lists` 
    
A 3x3 rotation matrix defined as a tuple of tuples or a list of lists. The matrix should be orthogonal. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The X, Y, and Z axes of the rotated frame.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> rotation_matrix = (
...     (0.7071067811865476, 0.0, 0.7071067811865476),
...     (0.0, 1.0, 0.0),
...     (-0.7071067811865476, 0.0, 0.7071067811865476),
... )
>>> x, y, z = Quaternion.rotation_matrix_to_axis(rotation_matrix)
>>> x
(0.7071067811865476, 0.0, -0.7071067811865476)
>>> y
(0.0, 1.0, 0.0)
>>> z
(-0.7071067811865476, 0.0, 0.7071067811865476)

```
Copy to clipboard
# rotation_matrix_to_axis 

static Quaternion.rotation_matrix_to_axis(_rotation_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Convert a rotation matrix to the corresponding axis of rotation. 

Parameters: 
     

**rotation_matrix**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` `tuples` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `lists` 
    
A 3x3 rotation matrix defined as a tuple of tuples or a list of lists. The matrix should be orthogonal. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The X, Y, and Z axes of the rotated frame.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> rotation_matrix = (
...     (0.7071067811865476, 0.0, 0.7071067811865476),
...     (0.0, 1.0, 0.0),
...     (-0.7071067811865476, 0.0, 0.7071067811865476),
... )
>>> x, y, z = Quaternion.rotation_matrix_to_axis(rotation_matrix)
>>> x
(0.7071067811865476, 0.0, -0.7071067811865476)
>>> y
(0.0, 1.0, 0.0)
>>> z
(-0.7071067811865476, 0.0, 0.7071067811865476)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis.rst.txt)

# rotation_matrix_to_axis 

static Quaternion.rotation_matrix_to_axis(_rotation_matrix : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Convert a rotation matrix to the corresponding axis of rotation. 

Parameters: 
     

**rotation_matrix**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` `tuples` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `lists` 
    
A 3x3 rotation matrix defined as a tuple of tuples or a list of lists. The matrix should be orthogonal. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The X, Y, and Z axes of the rotated frame.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> rotation_matrix = (
...     (0.7071067811865476, 0.0, 0.7071067811865476),
...     (0.0, 1.0, 0.0),
...     (-0.7071067811865476, 0.0, 0.7071067811865476),
... )
>>> x, y, z = Quaternion.rotation_matrix_to_axis(rotation_matrix)
>>> x
(0.7071067811865476, 0.0, -0.7071067811865476)
>>> y
(0.0, 1.0, 0.0)
>>> z
(-0.7071067811865476, 0.0, 0.7071067811865476)

```
Copy to clipboard