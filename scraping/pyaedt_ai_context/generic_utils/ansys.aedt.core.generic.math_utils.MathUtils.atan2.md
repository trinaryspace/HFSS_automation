---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.atan2.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# atan2 

static MathUtils.atan2(_y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Implementation of atan2 that does not suffer from the following issues: math.atan2(0.0, 0.0) = 0.0 math.atan2(-0.0, 0.0) = -0.0 math.atan2(0.0, -0.0) = 3.141592653589793 math.atan2(-0.0, -0.0) = -3.141592653589793 and returns always 0.0. 

Parameters: 
     

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y-axis value for atan2. 

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X-axis value for atan2. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.atan2(-0.0, -0.0)
0.0

```
Copy to clipboard
# atan2 

static MathUtils.atan2(_y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Implementation of atan2 that does not suffer from the following issues: math.atan2(0.0, 0.0) = 0.0 math.atan2(-0.0, 0.0) = -0.0 math.atan2(0.0, -0.0) = 3.141592653589793 math.atan2(-0.0, -0.0) = -3.141592653589793 and returns always 0.0. 

Parameters: 
     

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y-axis value for atan2. 

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X-axis value for atan2. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.atan2(-0.0, -0.0)
0.0

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.math_utils.MathUtils.atan2.rst.txt)

# atan2 

static MathUtils.atan2(_y : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _x : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Implementation of atan2 that does not suffer from the following issues: math.atan2(0.0, 0.0) = 0.0 math.atan2(-0.0, 0.0) = -0.0 math.atan2(0.0, -0.0) = 3.141592653589793 math.atan2(-0.0, -0.0) = -3.141592653589793 and returns always 0.0. 

Parameters: 
     

**y**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Y-axis value for atan2. 

**x**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
X-axis value for atan2. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.generic.math_utils import MathUtils
>>> MathUtils.atan2(-0.0, -0.0)
0.0

```
Copy to clipboard