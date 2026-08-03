---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# sync_variables 

SetupParam.sync_variables(_variables : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _sync_n : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sync variable variations in an existing parametric setup. Setting the sync number to 0 will effectively unsync the variables. 

Parameters: 
     

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of variables to sync. 

**sync_n**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Sync number. Sweep variables with the same Sync number will be synchronizad. Default is 1. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupParam
>>> obj = SetupParam()
>>> obj.sync_variables(variables=["Box1"])

```
Copy to clipboard
# sync_variables 

SetupParam.sync_variables(_variables : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _sync_n : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sync variable variations in an existing parametric setup. Setting the sync number to 0 will effectively unsync the variables. 

Parameters: 
     

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of variables to sync. 

**sync_n**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Sync number. Sweep variables with the same Sync number will be synchronizad. Default is 1. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupParam
>>> obj = SetupParam()
>>> obj.sync_variables(variables=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables.rst.txt)

# sync_variables 

SetupParam.sync_variables(_variables : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _sync_n : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sync variable variations in an existing parametric setup. Setting the sync number to 0 will effectively unsync the variables. 

Parameters: 
     

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of variables to sync. 

**sync_n**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Sync number. Sweep variables with the same Sync number will be synchronizad. Default is 1. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupParam
>>> obj = SetupParam()
>>> obj.sync_variables(variables=["Box1"])

```
Copy to clipboard