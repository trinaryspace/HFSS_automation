---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.set_non_linear.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# set_non_linear 

MatProperty.set_non_linear(_x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable non-linear material.
> This is a private method, and should not be used directly. 

Parameters: 
     

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
X units. Defaults will be used if None. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y units. Defaults will be used if None. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if succeeded.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2026.1")
>>> B_value = [0.0, 0.1, 0.3, 0.4, 0.48, 0.55, 0.6, 0.61, 0.65]
>>> H_value = [0.0, 500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3500.0, 5000.0, 10000.0]
>>> mat = hfss.materials.add_material("newMat")
>>> b_h_dataset = [[b, h] for b, h in zip(B_value, H_value)]
>>> mat.permeability = b_h_dataset

```
Copy to clipboard
# set_non_linear 

MatProperty.set_non_linear(_x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable non-linear material.
> This is a private method, and should not be used directly. 

Parameters: 
     

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
X units. Defaults will be used if None. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y units. Defaults will be used if None. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if succeeded.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2026.1")
>>> B_value = [0.0, 0.1, 0.3, 0.4, 0.48, 0.55, 0.6, 0.61, 0.65]
>>> H_value = [0.0, 500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3500.0, 5000.0, 10000.0]
>>> mat = hfss.materials.add_material("newMat")
>>> b_h_dataset = [[b, h] for b, h in zip(B_value, H_value)]
>>> mat.permeability = b_h_dataset

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.set_non_linear.rst.txt)

# set_non_linear 

MatProperty.set_non_linear(_x_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _y_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable non-linear material.
> This is a private method, and should not be used directly. 

Parameters: 
     

**x_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
X units. Defaults will be used if None. 

**y_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y units. Defaults will be used if None. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
True if succeeded.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2026.1")
>>> B_value = [0.0, 0.1, 0.3, 0.4, 0.48, 0.55, 0.6, 0.61, 0.65]
>>> H_value = [0.0, 500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3500.0, 5000.0, 10000.0]
>>> mat = hfss.materials.add_material("newMat")
>>> b_h_dataset = [[b, h] for b, h in zip(B_value, H_value)]
>>> mat.permeability = b_h_dataset

```
Copy to clipboard