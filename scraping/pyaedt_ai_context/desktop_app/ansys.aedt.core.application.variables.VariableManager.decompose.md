---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.decompose.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# decompose 

VariableManager.decompose(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Decompose a variable string to a floating with its unit. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The float value of the variable and the units exposed as a string.
Examples

```
>>> hfss = Hfss()
>>> print(hfss.variable_manager.decompose("5mm"))
>>> (5.0, "mm")
>>> hfss["v1"] = "3N"
>>> print(hfss.variable_manager.decompose("v1"))
>>> (3.0, "N")
>>> hfss["v2"] = "2*v1"
>>> print(hfss.variable_manager.decompose("v2"))
>>> (6.0, "N")

```
Copy to clipboard
# decompose 

VariableManager.decompose(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Decompose a variable string to a floating with its unit. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The float value of the variable and the units exposed as a string.
Examples

```
>>> hfss = Hfss()
>>> print(hfss.variable_manager.decompose("5mm"))
>>> (5.0, "mm")
>>> hfss["v1"] = "3N"
>>> print(hfss.variable_manager.decompose("v1"))
>>> (3.0, "N")
>>> hfss["v2"] = "2*v1"
>>> print(hfss.variable_manager.decompose("v2"))
>>> (6.0, "N")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.decompose.rst.txt)

# decompose 

VariableManager.decompose(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Decompose a variable string to a floating with its unit. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The float value of the variable and the units exposed as a string.
Examples

```
>>> hfss = Hfss()
>>> print(hfss.variable_manager.decompose("5mm"))
>>> (5.0, "mm")
>>> hfss["v1"] = "3N"
>>> print(hfss.variable_manager.decompose("v1"))
>>> (3.0, "N")
>>> hfss["v2"] = "2*v1"
>>> print(hfss.variable_manager.decompose("v2"))
>>> (6.0, "N")

```
Copy to clipboard