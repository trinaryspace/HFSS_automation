---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_auto_open.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# set_auto_open 

Hfss.set_auto_open(_enable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _opening_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Radiation'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the HFSS auto open type. 

Parameters: 
     

**enable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the HFSS auto open option. The default is `True`. 

**opening_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Boundary type to use with auto open. Options are `"Radiation"`, `"FEBI"`, and `"PML"`. The default is `"Radiation"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Enable auto open type for the PML boundary.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.set_auto_open(True, "PML")

```
Copy to clipboard
# set_auto_open 

Hfss.set_auto_open(_enable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _opening_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Radiation'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the HFSS auto open type. 

Parameters: 
     

**enable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the HFSS auto open option. The default is `True`. 

**opening_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Boundary type to use with auto open. Options are `"Radiation"`, `"FEBI"`, and `"PML"`. The default is `"Radiation"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Enable auto open type for the PML boundary.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.set_auto_open(True, "PML")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_auto_open.rst.txt)

# set_auto_open 

Hfss.set_auto_open(_enable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _opening_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Radiation'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the HFSS auto open type. 

Parameters: 
     

**enable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the HFSS auto open option. The default is `True`. 

**opening_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Boundary type to use with auto open. Options are `"Radiation"`, `"FEBI"`, and `"PML"`. The default is `"Radiation"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Enable auto open type for the PML boundary.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.set_auto_open(True, "PML")

```
Copy to clipboard