---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_equal.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# is_equal 

static MathUtils.is_equal(_a : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _b : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _eps : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.220446049250313e-15_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return True if numbers a and b are equal within a small epsilon tolerance. 

Parameters: 
     

**a: float**
    
First number. 

**b: float**
    
Second number. 

**eps**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Tolerance for the comparison. Default is `EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the absolute difference between a and b is less than epsilon, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_equal(2.0, 2.0)
True

```
Copy to clipboard
# is_equal 

static MathUtils.is_equal(_a : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _b : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _eps : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.220446049250313e-15_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return True if numbers a and b are equal within a small epsilon tolerance. 

Parameters: 
     

**a: float**
    
First number. 

**b: float**
    
Second number. 

**eps**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Tolerance for the comparison. Default is `EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the absolute difference between a and b is less than epsilon, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_equal(2.0, 2.0)
True

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_equal.rst.txt)

# is_equal 

static MathUtils.is_equal(_a : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _b : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _eps : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.220446049250313e-15_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return True if numbers a and b are equal within a small epsilon tolerance. 

Parameters: 
     

**a: float**
    
First number. 

**b: float**
    
Second number. 

**eps**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Tolerance for the comparison. Default is `EPSILON`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the absolute difference between a and b is less than epsilon, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_equal(2.0, 2.0)
True

```
Copy to clipboard