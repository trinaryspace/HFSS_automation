---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.activate_variable_tuning.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# activate_variable_tuning 

Hfss.activate_variable_tuning(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _minimum : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _maximum : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Activate tuning analysis for a variable and optionally set up ranges. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**minimum**`optional` 
    
Minimum value for the variable. The default is `None`. 

**maximum**`optional` 
    
Maximum value for the variable. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.activate_variable_tuning("width", minimum=1, maximum=5)

```
Copy to clipboard
# activate_variable_tuning 

Hfss.activate_variable_tuning(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _minimum : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _maximum : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Activate tuning analysis for a variable and optionally set up ranges. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**minimum**`optional` 
    
Minimum value for the variable. The default is `None`. 

**maximum**`optional` 
    
Maximum value for the variable. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.activate_variable_tuning("width", minimum=1, maximum=5)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.activate_variable_tuning.rst.txt)

# activate_variable_tuning 

Hfss.activate_variable_tuning(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _minimum : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _maximum : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Activate tuning analysis for a variable and optionally set up ranges. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**minimum**`optional` 
    
Minimum value for the variable. The default is `None`. 

**maximum**`optional` 
    
Maximum value for the variable. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.activate_variable_tuning("width", minimum=1, maximum=5)

```
Copy to clipboard