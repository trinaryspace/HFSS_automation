---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_zero.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# is_zero 

static MathUtils.is_zero(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _eps : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.220446049250313e-15_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a number is close to zero within a small epsilon tolerance. 

Parameters: 
     

**x: float**
    
Number to check. 

**eps**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Tolerance for the comparison. Default is `EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the number is numerically zero, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_zero(1e-16)
True

```
Copy to clipboard
# is_zero 

static MathUtils.is_zero(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _eps : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.220446049250313e-15_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a number is close to zero within a small epsilon tolerance. 

Parameters: 
     

**x: float**
    
Number to check. 

**eps**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Tolerance for the comparison. Default is `EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the number is numerically zero, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_zero(1e-16)
True

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_zero.rst.txt)

# is_zero 

static MathUtils.is_zero(_x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _eps : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.220446049250313e-15_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a number is close to zero within a small epsilon tolerance. 

Parameters: 
     

**x: float**
    
Number to check. 

**eps**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Tolerance for the comparison. Default is `EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the number is numerically zero, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_zero(1e-16)
True

```
Copy to clipboard