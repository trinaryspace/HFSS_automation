---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# Quaternion 

class ansys.aedt.core.generic.quaternion.Quaternion(_a : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _b : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _c : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _d : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) 
    
Implements fundamental quaternion operations.
Quaternions are created using `Quaternion(a, b, c, d)`.
Quaternions are only used to represent rotations in 3D space. They are not used to represent translations or other transformations. Only methods related to rotations are implemented.
The quaternion is defined as:
𝑞=𝑎+𝑏⁢𝑖+𝑐⁢𝑗+𝑑⁢𝑘
where `a` is the scalar part and `b`, `c`, and `d` are the vector parts.
This updated class offers enhanced functionality compared to the previous implementation, supporting both intrinsic and extrinsic rotations. Note that AEDT coordinate systems use intrinsic rotation.
References
[1] <https://en.wikipedia.org/wiki/Quaternion> [2] <https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles> [3] <https://www.euclideanspace.com/maths/geometry/rotations/conversions/>
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> rotation = Quaternion(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)
>>> rotation.coefficients()
(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)

```
Copy to clipboard
Methods  
| [`Quaternion.add`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.add.html#ansys.aedt.core.generic.quaternion.Quaternion.add "ansys.aedt.core.generic.quaternion.Quaternion.add")(other)  | Adds another quaternion or compatible value to this quaternion.  |  
| --- | --- |  
| [`Quaternion.axis_to_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix")(x_axis, ...)  | Construct a rotation matrix from three orthonormal axes.  |  
| [`Quaternion.coefficients`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.coefficients.html#ansys.aedt.core.generic.quaternion.Quaternion.coefficients "ansys.aedt.core.generic.quaternion.Quaternion.coefficients")()  | Returns the coefficients of the quaternion as a tuple.  |  
| [`Quaternion.conjugate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.conjugate.html#ansys.aedt.core.generic.quaternion.Quaternion.conjugate "ansys.aedt.core.generic.quaternion.Quaternion.conjugate")()  | Returns the conjugate of the quaternion.  |  
| [`Quaternion.div`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.div.html#ansys.aedt.core.generic.quaternion.Quaternion.div "ansys.aedt.core.generic.quaternion.Quaternion.div")(other)  | Performs quaternion division with another quaternion or compatible value.  |  
| [`Quaternion.from_axis_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle.html#ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle "ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle")(axis, angle)  | Creates a normalized rotation quaternion from a given axis and rotation angle.  |  
| [`Quaternion.from_euler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_euler.html#ansys.aedt.core.generic.quaternion.Quaternion.from_euler "ansys.aedt.core.generic.quaternion.Quaternion.from_euler")(angles, sequence[, ...])  | Creates a normalized rotation quaternion from the Euler angles using the specified rotation sequence.  |  
| [`Quaternion.from_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix")(rotation_matrix)  | Converts a 3x3 rotation matrix to a quaternion.  |  
| [`Quaternion.hamilton_prod`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod.html#ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod "ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod")(q1, q2)  | Evaluate the Hamilton product of two quaternions, `q1` and `q2`, defined as:  |  
| [`Quaternion.inverse`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.inverse.html#ansys.aedt.core.generic.quaternion.Quaternion.inverse "ansys.aedt.core.generic.quaternion.Quaternion.inverse")()  | Returns the inverse of the quaternion.  |  
| [`Quaternion.inverse_rotate_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector.html#ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector "ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector")(v)  | Evaluate the inverse rotation of a vector that is defined by a quaternion.  |  
| [`Quaternion.mul`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.mul.html#ansys.aedt.core.generic.quaternion.Quaternion.mul "ansys.aedt.core.generic.quaternion.Quaternion.mul")(other)  | Performs quaternion multiplication with another quaternion or compatible value.  |  
| [`Quaternion.norm`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.norm.html#ansys.aedt.core.generic.quaternion.Quaternion.norm "ansys.aedt.core.generic.quaternion.Quaternion.norm")()  | Returns the norm of the quaternion.  |  
| [`Quaternion.normalize`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.normalize.html#ansys.aedt.core.generic.quaternion.Quaternion.normalize "ansys.aedt.core.generic.quaternion.Quaternion.normalize")()  | Returns the normalized form of the quaternion.  |  
| [`Quaternion.rotate_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector.html#ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector "ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector")(v)  | Evaluate the rotation of a vector, defined by a quaternion.  |  
| [`Quaternion.rotation_matrix_to_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis.html#ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis "ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis")(...)  | Convert a rotation matrix to the corresponding axis of rotation.  |  
| [`Quaternion.to_axis_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle.html#ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle "ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle")()  | Convert a quaternion to the axis angle rotation formulation.  |  
| [`Quaternion.to_euler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_euler.html#ansys.aedt.core.generic.quaternion.Quaternion.to_euler "ansys.aedt.core.generic.quaternion.Quaternion.to_euler")(sequence[, extrinsic])  | Converts the quaternion to Euler angles using the specified rotation sequence.  |  
| [`Quaternion.to_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix")()  | Returns the rotation matrix corresponding to the quaternion.  |  
Attributes  
| [`Quaternion.a`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.a.html#ansys.aedt.core.generic.quaternion.Quaternion.a "ansys.aedt.core.generic.quaternion.Quaternion.a")  | Retrieve a.  |  
| --- | --- |  
| [`Quaternion.b`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.b.html#ansys.aedt.core.generic.quaternion.Quaternion.b "ansys.aedt.core.generic.quaternion.Quaternion.b")  | Retrieve b.  |  
| [`Quaternion.c`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.c.html#ansys.aedt.core.generic.quaternion.Quaternion.c "ansys.aedt.core.generic.quaternion.Quaternion.c")  | Retrieve c.  |  
| [`Quaternion.d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.d.html#ansys.aedt.core.generic.quaternion.Quaternion.d "ansys.aedt.core.generic.quaternion.Quaternion.d")  | Retrieve d.  |  
| [`Quaternion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.public_dir.html#ansys.aedt.core.generic.quaternion.Quaternion.public_dir "ansys.aedt.core.generic.quaternion.Quaternion.public_dir")  | Shortcut for dir(self).  |  
# Quaternion 

class ansys.aedt.core.generic.quaternion.Quaternion(_a : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _b : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _c : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _d : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) 
    
Implements fundamental quaternion operations.
Quaternions are created using `Quaternion(a, b, c, d)`.
Quaternions are only used to represent rotations in 3D space. They are not used to represent translations or other transformations. Only methods related to rotations are implemented.
The quaternion is defined as:
𝑞=𝑎+𝑏⁢𝑖+𝑐⁢𝑗+𝑑⁢𝑘
where `a` is the scalar part and `b`, `c`, and `d` are the vector parts.
This updated class offers enhanced functionality compared to the previous implementation, supporting both intrinsic and extrinsic rotations. Note that AEDT coordinate systems use intrinsic rotation.
References
[1] <https://en.wikipedia.org/wiki/Quaternion> [2] <https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles> [3] <https://www.euclideanspace.com/maths/geometry/rotations/conversions/>
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> rotation = Quaternion(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)
>>> rotation.coefficients()
(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)

```
Copy to clipboard
Methods  
| [`Quaternion.add`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.add.html#ansys.aedt.core.generic.quaternion.Quaternion.add "ansys.aedt.core.generic.quaternion.Quaternion.add")(other)  | Adds another quaternion or compatible value to this quaternion.  |  
| --- | --- |  
| [`Quaternion.axis_to_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix")(x_axis, ...)  | Construct a rotation matrix from three orthonormal axes.  |  
| [`Quaternion.coefficients`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.coefficients.html#ansys.aedt.core.generic.quaternion.Quaternion.coefficients "ansys.aedt.core.generic.quaternion.Quaternion.coefficients")()  | Returns the coefficients of the quaternion as a tuple.  |  
| [`Quaternion.conjugate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.conjugate.html#ansys.aedt.core.generic.quaternion.Quaternion.conjugate "ansys.aedt.core.generic.quaternion.Quaternion.conjugate")()  | Returns the conjugate of the quaternion.  |  
| [`Quaternion.div`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.div.html#ansys.aedt.core.generic.quaternion.Quaternion.div "ansys.aedt.core.generic.quaternion.Quaternion.div")(other)  | Performs quaternion division with another quaternion or compatible value.  |  
| [`Quaternion.from_axis_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle.html#ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle "ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle")(axis, angle)  | Creates a normalized rotation quaternion from a given axis and rotation angle.  |  
| [`Quaternion.from_euler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_euler.html#ansys.aedt.core.generic.quaternion.Quaternion.from_euler "ansys.aedt.core.generic.quaternion.Quaternion.from_euler")(angles, sequence[, ...])  | Creates a normalized rotation quaternion from the Euler angles using the specified rotation sequence.  |  
| [`Quaternion.from_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix")(rotation_matrix)  | Converts a 3x3 rotation matrix to a quaternion.  |  
| [`Quaternion.hamilton_prod`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod.html#ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod "ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod")(q1, q2)  | Evaluate the Hamilton product of two quaternions, `q1` and `q2`, defined as:  |  
| [`Quaternion.inverse`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.inverse.html#ansys.aedt.core.generic.quaternion.Quaternion.inverse "ansys.aedt.core.generic.quaternion.Quaternion.inverse")()  | Returns the inverse of the quaternion.  |  
| [`Quaternion.inverse_rotate_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector.html#ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector "ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector")(v)  | Evaluate the inverse rotation of a vector that is defined by a quaternion.  |  
| [`Quaternion.mul`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.mul.html#ansys.aedt.core.generic.quaternion.Quaternion.mul "ansys.aedt.core.generic.quaternion.Quaternion.mul")(other)  | Performs quaternion multiplication with another quaternion or compatible value.  |  
| [`Quaternion.norm`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.norm.html#ansys.aedt.core.generic.quaternion.Quaternion.norm "ansys.aedt.core.generic.quaternion.Quaternion.norm")()  | Returns the norm of the quaternion.  |  
| [`Quaternion.normalize`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.normalize.html#ansys.aedt.core.generic.quaternion.Quaternion.normalize "ansys.aedt.core.generic.quaternion.Quaternion.normalize")()  | Returns the normalized form of the quaternion.  |  
| [`Quaternion.rotate_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector.html#ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector "ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector")(v)  | Evaluate the rotation of a vector, defined by a quaternion.  |  
| [`Quaternion.rotation_matrix_to_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis.html#ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis "ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis")(...)  | Convert a rotation matrix to the corresponding axis of rotation.  |  
| [`Quaternion.to_axis_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle.html#ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle "ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle")()  | Convert a quaternion to the axis angle rotation formulation.  |  
| [`Quaternion.to_euler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_euler.html#ansys.aedt.core.generic.quaternion.Quaternion.to_euler "ansys.aedt.core.generic.quaternion.Quaternion.to_euler")(sequence[, extrinsic])  | Converts the quaternion to Euler angles using the specified rotation sequence.  |  
| [`Quaternion.to_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix")()  | Returns the rotation matrix corresponding to the quaternion.  |  
Attributes  
| [`Quaternion.a`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.a.html#ansys.aedt.core.generic.quaternion.Quaternion.a "ansys.aedt.core.generic.quaternion.Quaternion.a")  | Retrieve a.  |  
| --- | --- |  
| [`Quaternion.b`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.b.html#ansys.aedt.core.generic.quaternion.Quaternion.b "ansys.aedt.core.generic.quaternion.Quaternion.b")  | Retrieve b.  |  
| [`Quaternion.c`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.c.html#ansys.aedt.core.generic.quaternion.Quaternion.c "ansys.aedt.core.generic.quaternion.Quaternion.c")  | Retrieve c.  |  
| [`Quaternion.d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.d.html#ansys.aedt.core.generic.quaternion.Quaternion.d "ansys.aedt.core.generic.quaternion.Quaternion.d")  | Retrieve d.  |  
| [`Quaternion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.public_dir.html#ansys.aedt.core.generic.quaternion.Quaternion.public_dir "ansys.aedt.core.generic.quaternion.Quaternion.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rst.txt)

# Quaternion 

class ansys.aedt.core.generic.quaternion.Quaternion(_a : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _b : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _c : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _d : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) 
    
Implements fundamental quaternion operations.
Quaternions are created using `Quaternion(a, b, c, d)`.
Quaternions are only used to represent rotations in 3D space. They are not used to represent translations or other transformations. Only methods related to rotations are implemented.
The quaternion is defined as:
𝑞=𝑎+𝑏⁢𝑖+𝑐⁢𝑗+𝑑⁢𝑘
where `a` is the scalar part and `b`, `c`, and `d` are the vector parts.
This updated class offers enhanced functionality compared to the previous implementation, supporting both intrinsic and extrinsic rotations. Note that AEDT coordinate systems use intrinsic rotation.
References
[1] <https://en.wikipedia.org/wiki/Quaternion> [2] <https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles> [3] <https://www.euclideanspace.com/maths/geometry/rotations/conversions/>
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> rotation = Quaternion(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)
>>> rotation.coefficients()
(0.9238795325112867, 0.0, -0.3826834323650898, 0.0)

```
Copy to clipboard
Methods  
| [`Quaternion.add`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.add.html#ansys.aedt.core.generic.quaternion.Quaternion.add "ansys.aedt.core.generic.quaternion.Quaternion.add")(other)  | Adds another quaternion or compatible value to this quaternion.  |  
| --- | --- |  
| [`Quaternion.axis_to_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.axis_to_rotation_matrix")(x_axis, ...)  | Construct a rotation matrix from three orthonormal axes.  |  
| [`Quaternion.coefficients`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.coefficients.html#ansys.aedt.core.generic.quaternion.Quaternion.coefficients "ansys.aedt.core.generic.quaternion.Quaternion.coefficients")()  | Returns the coefficients of the quaternion as a tuple.  |  
| [`Quaternion.conjugate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.conjugate.html#ansys.aedt.core.generic.quaternion.Quaternion.conjugate "ansys.aedt.core.generic.quaternion.Quaternion.conjugate")()  | Returns the conjugate of the quaternion.  |  
| [`Quaternion.div`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.div.html#ansys.aedt.core.generic.quaternion.Quaternion.div "ansys.aedt.core.generic.quaternion.Quaternion.div")(other)  | Performs quaternion division with another quaternion or compatible value.  |  
| [`Quaternion.from_axis_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle.html#ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle "ansys.aedt.core.generic.quaternion.Quaternion.from_axis_angle")(axis, angle)  | Creates a normalized rotation quaternion from a given axis and rotation angle.  |  
| [`Quaternion.from_euler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_euler.html#ansys.aedt.core.generic.quaternion.Quaternion.from_euler "ansys.aedt.core.generic.quaternion.Quaternion.from_euler")(angles, sequence[, ...])  | Creates a normalized rotation quaternion from the Euler angles using the specified rotation sequence.  |  
| [`Quaternion.from_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.from_rotation_matrix")(rotation_matrix)  | Converts a 3x3 rotation matrix to a quaternion.  |  
| [`Quaternion.hamilton_prod`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod.html#ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod "ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod")(q1, q2)  | Evaluate the Hamilton product of two quaternions, `q1` and `q2`, defined as:  |  
| [`Quaternion.inverse`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.inverse.html#ansys.aedt.core.generic.quaternion.Quaternion.inverse "ansys.aedt.core.generic.quaternion.Quaternion.inverse")()  | Returns the inverse of the quaternion.  |  
| [`Quaternion.inverse_rotate_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector.html#ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector "ansys.aedt.core.generic.quaternion.Quaternion.inverse_rotate_vector")(v)  | Evaluate the inverse rotation of a vector that is defined by a quaternion.  |  
| [`Quaternion.mul`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.mul.html#ansys.aedt.core.generic.quaternion.Quaternion.mul "ansys.aedt.core.generic.quaternion.Quaternion.mul")(other)  | Performs quaternion multiplication with another quaternion or compatible value.  |  
| [`Quaternion.norm`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.norm.html#ansys.aedt.core.generic.quaternion.Quaternion.norm "ansys.aedt.core.generic.quaternion.Quaternion.norm")()  | Returns the norm of the quaternion.  |  
| [`Quaternion.normalize`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.normalize.html#ansys.aedt.core.generic.quaternion.Quaternion.normalize "ansys.aedt.core.generic.quaternion.Quaternion.normalize")()  | Returns the normalized form of the quaternion.  |  
| [`Quaternion.rotate_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector.html#ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector "ansys.aedt.core.generic.quaternion.Quaternion.rotate_vector")(v)  | Evaluate the rotation of a vector, defined by a quaternion.  |  
| [`Quaternion.rotation_matrix_to_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis.html#ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis "ansys.aedt.core.generic.quaternion.Quaternion.rotation_matrix_to_axis")(...)  | Convert a rotation matrix to the corresponding axis of rotation.  |  
| [`Quaternion.to_axis_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle.html#ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle "ansys.aedt.core.generic.quaternion.Quaternion.to_axis_angle")()  | Convert a quaternion to the axis angle rotation formulation.  |  
| [`Quaternion.to_euler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_euler.html#ansys.aedt.core.generic.quaternion.Quaternion.to_euler "ansys.aedt.core.generic.quaternion.Quaternion.to_euler")(sequence[, extrinsic])  | Converts the quaternion to Euler angles using the specified rotation sequence.  |  
| [`Quaternion.to_rotation_matrix`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix.html#ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix "ansys.aedt.core.generic.quaternion.Quaternion.to_rotation_matrix")()  | Returns the rotation matrix corresponding to the quaternion.  |  
Attributes  
| [`Quaternion.a`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.a.html#ansys.aedt.core.generic.quaternion.Quaternion.a "ansys.aedt.core.generic.quaternion.Quaternion.a")  | Retrieve a.  |  
| --- | --- |  
| [`Quaternion.b`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.b.html#ansys.aedt.core.generic.quaternion.Quaternion.b "ansys.aedt.core.generic.quaternion.Quaternion.b")  | Retrieve b.  |  
| [`Quaternion.c`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.c.html#ansys.aedt.core.generic.quaternion.Quaternion.c "ansys.aedt.core.generic.quaternion.Quaternion.c")  | Retrieve c.  |  
| [`Quaternion.d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.d.html#ansys.aedt.core.generic.quaternion.Quaternion.d "ansys.aedt.core.generic.quaternion.Quaternion.d")  | Retrieve d.  |  
| [`Quaternion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.public_dir.html#ansys.aedt.core.generic.quaternion.Quaternion.public_dir "ansys.aedt.core.generic.quaternion.Quaternion.public_dir")  | Shortcut for dir(self).  |