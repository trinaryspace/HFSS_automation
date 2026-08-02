---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.post_processing_variables.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# post_processing_variables 

property VariableManager.post_processing_variables: [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Post Processing variables. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of the post processing variables (constant numeric values) available to the design.
References

```
>>> oProject.GetVariables
>>> oDesign.GetVariables
>>> oProject.GetChildObject("Variables").GetChildNames
>>> oDesign.GetChildObject("Variables").GetChildNames

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.variable_manager.set_variable("post_gain", expression="1", is_post_processing=True)
>>> hfss.variable_manager.post_processing_variables

```
Copy to clipboard
# post_processing_variables 

property VariableManager.post_processing_variables: [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Post Processing variables. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of the post processing variables (constant numeric values) available to the design.
References

```
>>> oProject.GetVariables
>>> oDesign.GetVariables
>>> oProject.GetChildObject("Variables").GetChildNames
>>> oDesign.GetChildObject("Variables").GetChildNames

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.variable_manager.set_variable("post_gain", expression="1", is_post_processing=True)
>>> hfss.variable_manager.post_processing_variables

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.post_processing_variables.rst.txt)

# post_processing_variables 

property VariableManager.post_processing_variables: [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Post Processing variables. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of the post processing variables (constant numeric values) available to the design.
References

```
>>> oProject.GetVariables
>>> oDesign.GetVariables
>>> oProject.GetChildObject("Variables").GetChildNames
>>> oDesign.GetChildObject("Variables").GetChildNames

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.variable_manager.set_variable("post_gain", expression="1", is_post_processing=True)
>>> hfss.variable_manager.post_processing_variables

```
Copy to clipboard