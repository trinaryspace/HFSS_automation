---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# axis_to_rotation_matrix 

static Quaternion.axis_to_rotation_matrix(_x_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Construct a rotation matrix from three orthonormal axes. 

Parameters: 
     

**x_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The X axis of the rotated frame. 

**y_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The Y axis of the rotated frame. 

**z_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The Z axis of the rotated frame. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` `tuples` 
    
A 3x3 rotation matrix where each column is one of the given axes. 

Raises: 
     

[`ValueError`](https://docs.python.org/3.11/library/exceptions.html#ValueError "\(in Python v3.11\)")
    
If the axes do not form an orthonormal basis.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> Quaternion.axis_to_rotation_matrix((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))

```
Copy to clipboard
# axis_to_rotation_matrix 

static Quaternion.axis_to_rotation_matrix(_x_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Construct a rotation matrix from three orthonormal axes. 

Parameters: 
     

**x_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The X axis of the rotated frame. 

**y_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The Y axis of the rotated frame. 

**z_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The Z axis of the rotated frame. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` `tuples` 
    
A 3x3 rotation matrix where each column is one of the given axes. 

Raises: 
     

[`ValueError`](https://docs.python.org/3.11/library/exceptions.html#ValueError "\(in Python v3.11\)")
    
If the axes do not form an orthonormal basis.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> Quaternion.axis_to_rotation_matrix((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix.rst.txt)

# axis_to_rotation_matrix 

static Quaternion.axis_to_rotation_matrix(_x_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _z_axis : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Construct a rotation matrix from three orthonormal axes. 

Parameters: 
     

**x_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The X axis of the rotated frame. 

**y_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The Y axis of the rotated frame. 

**z_axis**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The Z axis of the rotated frame. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") `of` `tuples` 
    
A 3x3 rotation matrix where each column is one of the given axes. 

Raises: 
     

[`ValueError`](https://docs.python.org/3.11/library/exceptions.html#ValueError "\(in Python v3.11\)")
    
If the axes do not form an orthonormal basis.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> Quaternion.axis_to_rotation_matrix((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))

```
Copy to clipboard