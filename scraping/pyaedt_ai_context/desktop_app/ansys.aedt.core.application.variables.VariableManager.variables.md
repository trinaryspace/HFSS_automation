---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.variables.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# variables 

property VariableManager.variables 
    
Variables. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable")]
    
Dictionary of the Variable objects for each project variable and each design property in the active design.
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
>>> hfss.variable_manager.variables

```
Copy to clipboard
# variables 

property VariableManager.variables 
    
Variables. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable")]
    
Dictionary of the Variable objects for each project variable and each design property in the active design.
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
>>> hfss.variable_manager.variables

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.variables.rst.txt)

# variables 

property VariableManager.variables 
    
Variables. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable")]
    
Dictionary of the Variable objects for each project variable and each design property in the active design.
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
>>> hfss.variable_manager.variables

```
Copy to clipboard