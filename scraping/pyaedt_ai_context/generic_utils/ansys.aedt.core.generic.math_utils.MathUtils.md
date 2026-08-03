---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# MathUtils 

class ansys.aedt.core.generic.math_utils.MathUtils 
    
MathUtils is a utility class that provides methods for numerical comparisons and checks.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_zero(1e-16)
True

```
Copy to clipboard
Methods  
| [`MathUtils.atan2`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.atan2.html#ansys.aedt.core.generic.math_utils.MathUtils.atan2 "ansys.aedt.core.generic.math_utils.MathUtils.atan2")(y, x)  | Implementation of atan2 that does not suffer from the following issues: math.atan2(0.0, 0.0) = 0.0 math.atan2(-0.0, 0.0) = -0.0 math.atan2(0.0, -0.0) = 3.141592653589793 math.atan2(-0.0, -0.0) = -3.141592653589793 and returns always 0.0.  |  
| --- | --- |  
| [`MathUtils.fix_negative_zero`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero.html#ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero "ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero")(value)  | Fix the negative zero.  |  
| [`MathUtils.is_close`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_close.html#ansys.aedt.core.generic.math_utils.MathUtils.is_close "ansys.aedt.core.generic.math_utils.MathUtils.is_close")(a, b[, ...])  | Whether two numbers are close to each other given relative and absolute tolerances.  |  
| [`MathUtils.is_equal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_equal.html#ansys.aedt.core.generic.math_utils.MathUtils.is_equal "ansys.aedt.core.generic.math_utils.MathUtils.is_equal")(a, b[, eps])  | Return True if numbers a and b are equal within a small epsilon tolerance.  |  
| [`MathUtils.is_scalar_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number.html#ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number "ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number")(x)  | Check if a value is a scalar number (int or float).  |  
| [`MathUtils.is_zero`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_zero.html#ansys.aedt.core.generic.math_utils.MathUtils.is_zero "ansys.aedt.core.generic.math_utils.MathUtils.is_zero")(x[, eps])  | Check if a number is close to zero within a small epsilon tolerance.  |  
Attributes  
| [`MathUtils.EPSILON`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.EPSILON.html#ansys.aedt.core.generic.math_utils.MathUtils.EPSILON "ansys.aedt.core.generic.math_utils.MathUtils.EPSILON")  | Epsilon.  |  
| --- | --- |  
| [`MathUtils.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.public_dir.html#ansys.aedt.core.generic.math_utils.MathUtils.public_dir "ansys.aedt.core.generic.math_utils.MathUtils.public_dir")  | Shortcut for dir(self).  |  
# MathUtils 

class ansys.aedt.core.generic.math_utils.MathUtils 
    
MathUtils is a utility class that provides methods for numerical comparisons and checks.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_zero(1e-16)
True

```
Copy to clipboard
Methods  
| [`MathUtils.atan2`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.atan2.html#ansys.aedt.core.generic.math_utils.MathUtils.atan2 "ansys.aedt.core.generic.math_utils.MathUtils.atan2")(y, x)  | Implementation of atan2 that does not suffer from the following issues: math.atan2(0.0, 0.0) = 0.0 math.atan2(-0.0, 0.0) = -0.0 math.atan2(0.0, -0.0) = 3.141592653589793 math.atan2(-0.0, -0.0) = -3.141592653589793 and returns always 0.0.  |  
| --- | --- |  
| [`MathUtils.fix_negative_zero`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero.html#ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero "ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero")(value)  | Fix the negative zero.  |  
| [`MathUtils.is_close`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_close.html#ansys.aedt.core.generic.math_utils.MathUtils.is_close "ansys.aedt.core.generic.math_utils.MathUtils.is_close")(a, b[, ...])  | Whether two numbers are close to each other given relative and absolute tolerances.  |  
| [`MathUtils.is_equal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_equal.html#ansys.aedt.core.generic.math_utils.MathUtils.is_equal "ansys.aedt.core.generic.math_utils.MathUtils.is_equal")(a, b[, eps])  | Return True if numbers a and b are equal within a small epsilon tolerance.  |  
| [`MathUtils.is_scalar_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number.html#ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number "ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number")(x)  | Check if a value is a scalar number (int or float).  |  
| [`MathUtils.is_zero`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_zero.html#ansys.aedt.core.generic.math_utils.MathUtils.is_zero "ansys.aedt.core.generic.math_utils.MathUtils.is_zero")(x[, eps])  | Check if a number is close to zero within a small epsilon tolerance.  |  
Attributes  
| [`MathUtils.EPSILON`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.EPSILON.html#ansys.aedt.core.generic.math_utils.MathUtils.EPSILON "ansys.aedt.core.generic.math_utils.MathUtils.EPSILON")  | Epsilon.  |  
| --- | --- |  
| [`MathUtils.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.public_dir.html#ansys.aedt.core.generic.math_utils.MathUtils.public_dir "ansys.aedt.core.generic.math_utils.MathUtils.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.rst.txt)

# MathUtils 

class ansys.aedt.core.generic.math_utils.MathUtils 
    
MathUtils is a utility class that provides methods for numerical comparisons and checks.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_zero(1e-16)
True

```
Copy to clipboard
Methods  
| [`MathUtils.atan2`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.atan2.html#ansys.aedt.core.generic.math_utils.MathUtils.atan2 "ansys.aedt.core.generic.math_utils.MathUtils.atan2")(y, x)  | Implementation of atan2 that does not suffer from the following issues: math.atan2(0.0, 0.0) = 0.0 math.atan2(-0.0, 0.0) = -0.0 math.atan2(0.0, -0.0) = 3.141592653589793 math.atan2(-0.0, -0.0) = -3.141592653589793 and returns always 0.0.  |  
| --- | --- |  
| [`MathUtils.fix_negative_zero`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero.html#ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero "ansys.aedt.core.generic.math_utils.MathUtils.fix_negative_zero")(value)  | Fix the negative zero.  |  
| [`MathUtils.is_close`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_close.html#ansys.aedt.core.generic.math_utils.MathUtils.is_close "ansys.aedt.core.generic.math_utils.MathUtils.is_close")(a, b[, ...])  | Whether two numbers are close to each other given relative and absolute tolerances.  |  
| [`MathUtils.is_equal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_equal.html#ansys.aedt.core.generic.math_utils.MathUtils.is_equal "ansys.aedt.core.generic.math_utils.MathUtils.is_equal")(a, b[, eps])  | Return True if numbers a and b are equal within a small epsilon tolerance.  |  
| [`MathUtils.is_scalar_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number.html#ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number "ansys.aedt.core.generic.math_utils.MathUtils.is_scalar_number")(x)  | Check if a value is a scalar number (int or float).  |  
| [`MathUtils.is_zero`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_zero.html#ansys.aedt.core.generic.math_utils.MathUtils.is_zero "ansys.aedt.core.generic.math_utils.MathUtils.is_zero")(x[, eps])  | Check if a number is close to zero within a small epsilon tolerance.  |  
Attributes  
| [`MathUtils.EPSILON`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.EPSILON.html#ansys.aedt.core.generic.math_utils.MathUtils.EPSILON "ansys.aedt.core.generic.math_utils.MathUtils.EPSILON")  | Epsilon.  |  
| --- | --- |  
| [`MathUtils.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.public_dir.html#ansys.aedt.core.generic.math_utils.MathUtils.public_dir "ansys.aedt.core.generic.math_utils.MathUtils.public_dir")  | Shortcut for dir(self).  |