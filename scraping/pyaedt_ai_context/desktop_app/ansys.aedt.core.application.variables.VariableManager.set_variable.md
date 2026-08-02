---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.set_variable.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# set_variable 

VariableManager.set_variable(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _read_only : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _hidden : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _description : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_post_processing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _circuit_parameter : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the value of a design property or project variable. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design property or project variable (`$var`). If this variable does not exist, a new one is created and a value is set. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Valid string expression within the AEDT design and project structure. For example, `"3*cos(34deg)"`. 

**read_only**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the design property or project variable to read-only. The default is `False`. 

**hidden**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the design property or project variable. The default is `False`. 

**description**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Text to display for the design property or project variable in the `Properties` window. The default is `None`. 

**sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Allows you to designate variables to include in solution indexing as a way to permit faster post-processing. Variables with the Sweep check box cleared are not used in solution indexing. The default is `True`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite an existing value for the design property or project variable. The default is `False`, in which case this method is ignored. 

**is_post_processing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to define a postprocessing variable.
    
The default is `False`, in which case the variable is not used in postprocessing. 

**circuit_parameter**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to define a parameter in a circuit design or a local parameter.
    
The default is `True`, in which case a circuit variable is created as a parameter default. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.ChangeProperty
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> aedtapp = Maxwell3d(version="2026.1")

```
Copy to clipboard
Set the value of design property `p1` to `"10mm"`, creating the property if it does not already eixst.

```
>>> aedtapp.variable_manager.set_variable("p1", expression="10mm")

```
Copy to clipboard
Set the value of design property `p1` to `"20mm"` only if the property does not already exist.

```
>>> aedtapp.variable_manager.set_variable("p1", expression="20mm", overwrite=False)

```
Copy to clipboard
Set the value of design property `p2` to `"10mm"`, creating the property if it does not already exist. Also make it read-only and hidden and add a description.

```
>>> aedtapp.variable_manager.set_variable(
...     name="p2",
...     expression="10mm",
...     read_only=True,
...     hidden=True,
...     description="This is the description of this variable.",
... )

```
Copy to clipboard
Set the value of the project variable `$p1` to `"30mm"`, creating the variable if it does not exist.

```
>>> aedtapp.variable_manager.set_variable["$p1"] == "30mm"

```
Copy to clipboard
# set_variable 

VariableManager.set_variable(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _read_only : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _hidden : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _description : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_post_processing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _circuit_parameter : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the value of a design property or project variable. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design property or project variable (`$var`). If this variable does not exist, a new one is created and a value is set. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Valid string expression within the AEDT design and project structure. For example, `"3*cos(34deg)"`. 

**read_only**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the design property or project variable to read-only. The default is `False`. 

**hidden**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the design property or project variable. The default is `False`. 

**description**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Text to display for the design property or project variable in the `Properties` window. The default is `None`. 

**sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Allows you to designate variables to include in solution indexing as a way to permit faster post-processing. Variables with the Sweep check box cleared are not used in solution indexing. The default is `True`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite an existing value for the design property or project variable. The default is `False`, in which case this method is ignored. 

**is_post_processing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to define a postprocessing variable.
    
The default is `False`, in which case the variable is not used in postprocessing. 

**circuit_parameter**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to define a parameter in a circuit design or a local parameter.
    
The default is `True`, in which case a circuit variable is created as a parameter default. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.ChangeProperty
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> aedtapp = Maxwell3d(version="2026.1")

```
Copy to clipboard
Set the value of design property `p1` to `"10mm"`, creating the property if it does not already eixst.

```
>>> aedtapp.variable_manager.set_variable("p1", expression="10mm")

```
Copy to clipboard
Set the value of design property `p1` to `"20mm"` only if the property does not already exist.

```
>>> aedtapp.variable_manager.set_variable("p1", expression="20mm", overwrite=False)

```
Copy to clipboard
Set the value of design property `p2` to `"10mm"`, creating the property if it does not already exist. Also make it read-only and hidden and add a description.

```
>>> aedtapp.variable_manager.set_variable(
...     name="p2",
...     expression="10mm",
...     read_only=True,
...     hidden=True,
...     description="This is the description of this variable.",
... )

```
Copy to clipboard
Set the value of the project variable `$p1` to `"30mm"`, creating the variable if it does not exist.

```
>>> aedtapp.variable_manager.set_variable["$p1"] == "30mm"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.set_variable.rst.txt)

# set_variable 

VariableManager.set_variable(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _read_only : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _hidden : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _description : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_post_processing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _circuit_parameter : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the value of a design property or project variable. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design property or project variable (`$var`). If this variable does not exist, a new one is created and a value is set. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Valid string expression within the AEDT design and project structure. For example, `"3*cos(34deg)"`. 

**read_only**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the design property or project variable to read-only. The default is `False`. 

**hidden**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the design property or project variable. The default is `False`. 

**description**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Text to display for the design property or project variable in the `Properties` window. The default is `None`. 

**sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Allows you to designate variables to include in solution indexing as a way to permit faster post-processing. Variables with the Sweep check box cleared are not used in solution indexing. The default is `True`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite an existing value for the design property or project variable. The default is `False`, in which case this method is ignored. 

**is_post_processing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to define a postprocessing variable.
    
The default is `False`, in which case the variable is not used in postprocessing. 

**circuit_parameter**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to define a parameter in a circuit design or a local parameter.
    
The default is `True`, in which case a circuit variable is created as a parameter default. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oProject.ChangeProperty
>>> oDesign.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> aedtapp = Maxwell3d(version="2026.1")

```
Copy to clipboard
Set the value of design property `p1` to `"10mm"`, creating the property if it does not already eixst.

```
>>> aedtapp.variable_manager.set_variable("p1", expression="10mm")

```
Copy to clipboard
Set the value of design property `p1` to `"20mm"` only if the property does not already exist.

```
>>> aedtapp.variable_manager.set_variable("p1", expression="20mm", overwrite=False)

```
Copy to clipboard
Set the value of design property `p2` to `"10mm"`, creating the property if it does not already exist. Also make it read-only and hidden and add a description.

```
>>> aedtapp.variable_manager.set_variable(
...     name="p2",
...     expression="10mm",
...     read_only=True,
...     hidden=True,
...     description="This is the description of this variable.",
... )

```
Copy to clipboard
Set the value of the project variable `$p1` to `"30mm"`, creating the variable if it does not exist.

```
>>> aedtapp.variable_manager.set_variable["$p1"] == "30mm"

```
Copy to clipboard