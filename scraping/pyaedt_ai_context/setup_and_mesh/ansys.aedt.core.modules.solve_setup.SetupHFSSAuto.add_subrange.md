---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_subrange 

SetupHFSSAuto.add_subrange(_range_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _count : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _clear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a subrange to the sweep. 

Parameters: 
     

**range_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the subrange. Options are `"LinearCount"`, `"LinearStep"`, and `"LogScale"`. 

**start**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency. 

**end**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stopping frequency. 

**count**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Frequency count or frequency step. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency Units. 

**clear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the subrange has to be appended to existing ones or replace them. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.add_subrange(range_type="LinearCount", start=1, end=2)

```
Copy to clipboard
# add_subrange 

SetupHFSSAuto.add_subrange(_range_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _count : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _clear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a subrange to the sweep. 

Parameters: 
     

**range_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the subrange. Options are `"LinearCount"`, `"LinearStep"`, and `"LogScale"`. 

**start**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency. 

**end**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stopping frequency. 

**count**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Frequency count or frequency step. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency Units. 

**clear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the subrange has to be appended to existing ones or replace them. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.add_subrange(range_type="LinearCount", start=1, end=2)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange.rst.txt)

# add_subrange 

SetupHFSSAuto.add_subrange(_range_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _count : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _clear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a subrange to the sweep. 

Parameters: 
     

**range_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the subrange. Options are `"LinearCount"`, `"LinearStep"`, and `"LogScale"`. 

**start**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency. 

**end**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stopping frequency. 

**count**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Frequency count or frequency step. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency Units. 

**clear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the subrange has to be appended to existing ones or replace them. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.add_subrange(range_type="LinearCount", start=1, end=2)

```
Copy to clipboard