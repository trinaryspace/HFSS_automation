---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_close.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# is_close 

static MathUtils.is_close(_a : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _b : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _relative_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _absolute_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether two numbers are close to each other given relative and absolute tolerances. 

Parameters: 
     

**a**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
First number to compare. 

**b**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Second number to compare. 

**relative_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Relative tolerance. The default value is `1e-9`. 

**absolute_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Absolute tolerance. The default value is `0.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the two numbers are closed, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_close(1.0, 1.0 + 1e-10)
True

```
Copy to clipboard
# is_close 

static MathUtils.is_close(_a : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _b : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _relative_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _absolute_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether two numbers are close to each other given relative and absolute tolerances. 

Parameters: 
     

**a**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
First number to compare. 

**b**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Second number to compare. 

**relative_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Relative tolerance. The default value is `1e-9`. 

**absolute_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Absolute tolerance. The default value is `0.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the two numbers are closed, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_close(1.0, 1.0 + 1e-10)
True

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.is_close.rst.txt)

# is_close 

static MathUtils.is_close(_a : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _b : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _relative_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _absolute_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether two numbers are close to each other given relative and absolute tolerances. 

Parameters: 
     

**a**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
First number to compare. 

**b**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Second number to compare. 

**relative_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Relative tolerance. The default value is `1e-9`. 

**absolute_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Absolute tolerance. The default value is `0.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the two numbers are closed, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.is_close(1.0, 1.0 + 1e-10)
True

```
Copy to clipboard