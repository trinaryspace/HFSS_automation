---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# VariableManager 

class ansys.aedt.core.application.variables.VariableManager(_app_) 
    
Manages design properties and project variables.
Design properties are the local variables in a design. Project variables are defined at the project level and start with `$`.
This class provides access to all variables or a subset of the variables. Manipulation of the numerical or string definitions of variable values is provided in the [`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable") class. 

Parameters: 
     

**variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all design properties and project variables in the active design. 

**design_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all design properties in the active design. 

**project_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all project variables available to the active design (key by variable name). 

**dependent_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all dependent variables available to the active design (key by variable name). 

**independent_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all independent variables (constant numeric values) available to the active design (key by variable name). 

**independent_design_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**independent_project_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more variable names. 

**project_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more project variable names. 

**design_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more design variable names. 

**dependent_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All dependent variable names within the project. 

**independent_variable_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
All independent variable names within the project. These can be sweep variables for optimetrics. 

**independent_project_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All independent project variable names within the project. These can be sweep variables for optimetrics. 

**independent_design_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All independent design properties (local variables) within the project. These can be sweep variables for optimetrics.
See also 

[`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable")
    
Examples

```
>>> from ansys.aedt.core.maxwell import Maxwell3d
>>> from ansys.aedt.core.desktop import Desktop
>>> d = Desktop()
>>> aedtapp = Maxwell3d()

```
Copy to clipboard
Define some test variables.

```
>>> aedtapp["Var1"] = 3
>>> aedtapp["Var2"] = "12deg"
>>> aedtapp["Var3"] = "Var1 * Var2"
>>> aedtapp["$PrjVar1"] = "pi"

```
Copy to clipboard
Get the variable manager for the active design.

```
>>> v = aedtapp.variable_manager

```
Copy to clipboard
Get a dictionary of all project and design variables.

```
>>> v.variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f34c448>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f34c308>,
 'Var3': <ansys.aedt.core.application.variables.Expression at 0x2661f34cb48>,
 '$PrjVar1': <ansys.aedt.core.application.variables.Expression at 0x2661f34cc48>}

```
Copy to clipboard
Get a dictionary of only the design variables.

```
>>> v.design_variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f339508>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f3415c8>,
 'Var3': <ansys.aedt.core.application.variables.Expression at 0x2661f341808>}

```
Copy to clipboard
Get a dictionary of only the independent design variables.

```
>>> v.independent_design_variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f335d08>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f3557c8>}

```
Copy to clipboard
Methods  
| [`VariableManager.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.aedt_object.html#ansys.aedt.core.application.variables.VariableManager.aedt_object "ansys.aedt.core.application.variables.VariableManager.aedt_object")(name)  | Retrieve an AEDT object.  |  
| --- | --- |  
| [`VariableManager.decompose`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.decompose.html#ansys.aedt.core.application.variables.VariableManager.decompose "ansys.aedt.core.application.variables.VariableManager.decompose")(variable)  | Decompose a variable string to a floating with its unit.  |  
| [`VariableManager.delete_separator`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_separator.html#ansys.aedt.core.application.variables.VariableManager.delete_separator "ansys.aedt.core.application.variables.VariableManager.delete_separator")(name)  | Delete a separator from either the active project or design.  |  
| [`VariableManager.delete_unused_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_unused_variables.html#ansys.aedt.core.application.variables.VariableManager.delete_unused_variables "ansys.aedt.core.application.variables.VariableManager.delete_unused_variables")()  | Delete unused design and project variables.  |  
| [`VariableManager.delete_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_variable.html#ansys.aedt.core.application.variables.VariableManager.delete_variable "ansys.aedt.core.application.variables.VariableManager.delete_variable")(name)  | Delete a variable.  |  
| [`VariableManager.get_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.get_expression.html#ansys.aedt.core.application.variables.VariableManager.get_expression "ansys.aedt.core.application.variables.VariableManager.get_expression")(name)  | Retrieve the variable value of a project or design variable as a string.  |  
| [`VariableManager.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.is_used.html#ansys.aedt.core.application.variables.VariableManager.is_used "ansys.aedt.core.application.variables.VariableManager.is_used")(name)  | Find if a variable is used.  |  
| [`VariableManager.set_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.set_variable.html#ansys.aedt.core.application.variables.VariableManager.set_variable "ansys.aedt.core.application.variables.VariableManager.set_variable")(name[, ...])  | Set the value of a design property or project variable.  |  
Attributes  
| [`VariableManager.dependent_design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names")  | List of dependent design variables.  |  
| --- | --- |  
| [`VariableManager.dependent_design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_design_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_design_variables "ansys.aedt.core.application.variables.VariableManager.dependent_design_variables")  | Dependent design variables.  |  
| [`VariableManager.dependent_project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names")  | List of dependent project variables.  |  
| [`VariableManager.dependent_project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_project_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_project_variables "ansys.aedt.core.application.variables.VariableManager.dependent_project_variables")  | Dependent project variables.  |  
| [`VariableManager.dependent_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_variable_names")  | List of dependent variables.  |  
| [`VariableManager.dependent_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_variables "ansys.aedt.core.application.variables.VariableManager.dependent_variables")  | Dependent variables.  |  
| [`VariableManager.design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.design_variable_names "ansys.aedt.core.application.variables.VariableManager.design_variable_names")  | List of design variables.  |  
| [`VariableManager.design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.design_variables.html#ansys.aedt.core.application.variables.VariableManager.design_variables "ansys.aedt.core.application.variables.VariableManager.design_variables")  | Design variables.  |  
| [`VariableManager.independent_design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names")  | List of independent design variables.  |  
| [`VariableManager.independent_design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_design_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_design_variables "ansys.aedt.core.application.variables.VariableManager.independent_design_variables")  | Independent design variables.  |  
| [`VariableManager.independent_project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names")  | List of independent project variables.  |  
| [`VariableManager.independent_project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_project_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_project_variables "ansys.aedt.core.application.variables.VariableManager.independent_project_variables")  | Independent project variables.  |  
| [`VariableManager.independent_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_variable_names")  | List of independent variables.  |  
| [`VariableManager.independent_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_variables "ansys.aedt.core.application.variables.VariableManager.independent_variables")  | Independent variables.  |  
| [`VariableManager.post_processing_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.post_processing_variables.html#ansys.aedt.core.application.variables.VariableManager.post_processing_variables "ansys.aedt.core.application.variables.VariableManager.post_processing_variables")  | Post Processing variables.  |  
| [`VariableManager.project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.project_variable_names "ansys.aedt.core.application.variables.VariableManager.project_variable_names")  | List of project variables.  |  
| [`VariableManager.project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.project_variables.html#ansys.aedt.core.application.variables.VariableManager.project_variables "ansys.aedt.core.application.variables.VariableManager.project_variables")  | Project variables.  |  
| [`VariableManager.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.public_dir.html#ansys.aedt.core.application.variables.VariableManager.public_dir "ansys.aedt.core.application.variables.VariableManager.public_dir")  | Shortcut for dir(self).  |  
| [`VariableManager.variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.variable_names.html#ansys.aedt.core.application.variables.VariableManager.variable_names "ansys.aedt.core.application.variables.VariableManager.variable_names")  | List of variables.  |  
| [`VariableManager.variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.variables.html#ansys.aedt.core.application.variables.VariableManager.variables "ansys.aedt.core.application.variables.VariableManager.variables")  | Variables.  |  
# VariableManager 

class ansys.aedt.core.application.variables.VariableManager(_app_) 
    
Manages design properties and project variables.
Design properties are the local variables in a design. Project variables are defined at the project level and start with `$`.
This class provides access to all variables or a subset of the variables. Manipulation of the numerical or string definitions of variable values is provided in the [`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable") class. 

Parameters: 
     

**variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all design properties and project variables in the active design. 

**design_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all design properties in the active design. 

**project_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all project variables available to the active design (key by variable name). 

**dependent_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all dependent variables available to the active design (key by variable name). 

**independent_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all independent variables (constant numeric values) available to the active design (key by variable name). 

**independent_design_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**independent_project_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more variable names. 

**project_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more project variable names. 

**design_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more design variable names. 

**dependent_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All dependent variable names within the project. 

**independent_variable_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
All independent variable names within the project. These can be sweep variables for optimetrics. 

**independent_project_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All independent project variable names within the project. These can be sweep variables for optimetrics. 

**independent_design_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All independent design properties (local variables) within the project. These can be sweep variables for optimetrics.
See also 

[`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable")
    
Examples

```
>>> from ansys.aedt.core.maxwell import Maxwell3d
>>> from ansys.aedt.core.desktop import Desktop
>>> d = Desktop()
>>> aedtapp = Maxwell3d()

```
Copy to clipboard
Define some test variables.

```
>>> aedtapp["Var1"] = 3
>>> aedtapp["Var2"] = "12deg"
>>> aedtapp["Var3"] = "Var1 * Var2"
>>> aedtapp["$PrjVar1"] = "pi"

```
Copy to clipboard
Get the variable manager for the active design.

```
>>> v = aedtapp.variable_manager

```
Copy to clipboard
Get a dictionary of all project and design variables.

```
>>> v.variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f34c448>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f34c308>,
 'Var3': <ansys.aedt.core.application.variables.Expression at 0x2661f34cb48>,
 '$PrjVar1': <ansys.aedt.core.application.variables.Expression at 0x2661f34cc48>}

```
Copy to clipboard
Get a dictionary of only the design variables.

```
>>> v.design_variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f339508>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f3415c8>,
 'Var3': <ansys.aedt.core.application.variables.Expression at 0x2661f341808>}

```
Copy to clipboard
Get a dictionary of only the independent design variables.

```
>>> v.independent_design_variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f335d08>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f3557c8>}

```
Copy to clipboard
Methods  
| [`VariableManager.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.aedt_object.html#ansys.aedt.core.application.variables.VariableManager.aedt_object "ansys.aedt.core.application.variables.VariableManager.aedt_object")(name)  | Retrieve an AEDT object.  |  
| --- | --- |  
| [`VariableManager.decompose`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.decompose.html#ansys.aedt.core.application.variables.VariableManager.decompose "ansys.aedt.core.application.variables.VariableManager.decompose")(variable)  | Decompose a variable string to a floating with its unit.  |  
| [`VariableManager.delete_separator`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_separator.html#ansys.aedt.core.application.variables.VariableManager.delete_separator "ansys.aedt.core.application.variables.VariableManager.delete_separator")(name)  | Delete a separator from either the active project or design.  |  
| [`VariableManager.delete_unused_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_unused_variables.html#ansys.aedt.core.application.variables.VariableManager.delete_unused_variables "ansys.aedt.core.application.variables.VariableManager.delete_unused_variables")()  | Delete unused design and project variables.  |  
| [`VariableManager.delete_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_variable.html#ansys.aedt.core.application.variables.VariableManager.delete_variable "ansys.aedt.core.application.variables.VariableManager.delete_variable")(name)  | Delete a variable.  |  
| [`VariableManager.get_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.get_expression.html#ansys.aedt.core.application.variables.VariableManager.get_expression "ansys.aedt.core.application.variables.VariableManager.get_expression")(name)  | Retrieve the variable value of a project or design variable as a string.  |  
| [`VariableManager.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.is_used.html#ansys.aedt.core.application.variables.VariableManager.is_used "ansys.aedt.core.application.variables.VariableManager.is_used")(name)  | Find if a variable is used.  |  
| [`VariableManager.set_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.set_variable.html#ansys.aedt.core.application.variables.VariableManager.set_variable "ansys.aedt.core.application.variables.VariableManager.set_variable")(name[, ...])  | Set the value of a design property or project variable.  |  
Attributes  
| [`VariableManager.dependent_design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names")  | List of dependent design variables.  |  
| --- | --- |  
| [`VariableManager.dependent_design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_design_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_design_variables "ansys.aedt.core.application.variables.VariableManager.dependent_design_variables")  | Dependent design variables.  |  
| [`VariableManager.dependent_project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names")  | List of dependent project variables.  |  
| [`VariableManager.dependent_project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_project_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_project_variables "ansys.aedt.core.application.variables.VariableManager.dependent_project_variables")  | Dependent project variables.  |  
| [`VariableManager.dependent_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_variable_names")  | List of dependent variables.  |  
| [`VariableManager.dependent_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_variables "ansys.aedt.core.application.variables.VariableManager.dependent_variables")  | Dependent variables.  |  
| [`VariableManager.design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.design_variable_names "ansys.aedt.core.application.variables.VariableManager.design_variable_names")  | List of design variables.  |  
| [`VariableManager.design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.design_variables.html#ansys.aedt.core.application.variables.VariableManager.design_variables "ansys.aedt.core.application.variables.VariableManager.design_variables")  | Design variables.  |  
| [`VariableManager.independent_design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names")  | List of independent design variables.  |  
| [`VariableManager.independent_design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_design_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_design_variables "ansys.aedt.core.application.variables.VariableManager.independent_design_variables")  | Independent design variables.  |  
| [`VariableManager.independent_project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names")  | List of independent project variables.  |  
| [`VariableManager.independent_project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_project_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_project_variables "ansys.aedt.core.application.variables.VariableManager.independent_project_variables")  | Independent project variables.  |  
| [`VariableManager.independent_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_variable_names")  | List of independent variables.  |  
| [`VariableManager.independent_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_variables "ansys.aedt.core.application.variables.VariableManager.independent_variables")  | Independent variables.  |  
| [`VariableManager.post_processing_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.post_processing_variables.html#ansys.aedt.core.application.variables.VariableManager.post_processing_variables "ansys.aedt.core.application.variables.VariableManager.post_processing_variables")  | Post Processing variables.  |  
| [`VariableManager.project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.project_variable_names "ansys.aedt.core.application.variables.VariableManager.project_variable_names")  | List of project variables.  |  
| [`VariableManager.project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.project_variables.html#ansys.aedt.core.application.variables.VariableManager.project_variables "ansys.aedt.core.application.variables.VariableManager.project_variables")  | Project variables.  |  
| [`VariableManager.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.public_dir.html#ansys.aedt.core.application.variables.VariableManager.public_dir "ansys.aedt.core.application.variables.VariableManager.public_dir")  | Shortcut for dir(self).  |  
| [`VariableManager.variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.variable_names.html#ansys.aedt.core.application.variables.VariableManager.variable_names "ansys.aedt.core.application.variables.VariableManager.variable_names")  | List of variables.  |  
| [`VariableManager.variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.variables.html#ansys.aedt.core.application.variables.VariableManager.variables "ansys.aedt.core.application.variables.VariableManager.variables")  | Variables.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.rst.txt)

# VariableManager 

class ansys.aedt.core.application.variables.VariableManager(_app_) 
    
Manages design properties and project variables.
Design properties are the local variables in a design. Project variables are defined at the project level and start with `$`.
This class provides access to all variables or a subset of the variables. Manipulation of the numerical or string definitions of variable values is provided in the [`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable") class. 

Parameters: 
     

**variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all design properties and project variables in the active design. 

**design_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all design properties in the active design. 

**project_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all project variables available to the active design (key by variable name). 

**dependent_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all dependent variables available to the active design (key by variable name). 

**independent_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of all independent variables (constant numeric values) available to the active design (key by variable name). 

**independent_design_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**independent_project_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
     

**variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more variable names. 

**project_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more project variable names. 

**design_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more design variable names. 

**dependent_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All dependent variable names within the project. 

**independent_variable_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
All independent variable names within the project. These can be sweep variables for optimetrics. 

**independent_project_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All independent project variable names within the project. These can be sweep variables for optimetrics. 

**independent_design_variable_names**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
All independent design properties (local variables) within the project. These can be sweep variables for optimetrics.
See also 

[`ansys.aedt.core.application.variables.Variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html#ansys.aedt.core.application.variables.Variable "ansys.aedt.core.application.variables.Variable")
    
Examples

```
>>> from ansys.aedt.core.maxwell import Maxwell3d
>>> from ansys.aedt.core.desktop import Desktop
>>> d = Desktop()
>>> aedtapp = Maxwell3d()

```
Copy to clipboard
Define some test variables.

```
>>> aedtapp["Var1"] = 3
>>> aedtapp["Var2"] = "12deg"
>>> aedtapp["Var3"] = "Var1 * Var2"
>>> aedtapp["$PrjVar1"] = "pi"

```
Copy to clipboard
Get the variable manager for the active design.

```
>>> v = aedtapp.variable_manager

```
Copy to clipboard
Get a dictionary of all project and design variables.

```
>>> v.variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f34c448>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f34c308>,
 'Var3': <ansys.aedt.core.application.variables.Expression at 0x2661f34cb48>,
 '$PrjVar1': <ansys.aedt.core.application.variables.Expression at 0x2661f34cc48>}

```
Copy to clipboard
Get a dictionary of only the design variables.

```
>>> v.design_variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f339508>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f3415c8>,
 'Var3': <ansys.aedt.core.application.variables.Expression at 0x2661f341808>}

```
Copy to clipboard
Get a dictionary of only the independent design variables.

```
>>> v.independent_design_variables
{'Var1': <ansys.aedt.core.application.variables.Variable at 0x2661f335d08>,
 'Var2': <ansys.aedt.core.application.variables.Variable at 0x2661f3557c8>}

```
Copy to clipboard
Methods  
| [`VariableManager.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.aedt_object.html#ansys.aedt.core.application.variables.VariableManager.aedt_object "ansys.aedt.core.application.variables.VariableManager.aedt_object")(name)  | Retrieve an AEDT object.  |  
| --- | --- |  
| [`VariableManager.decompose`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.decompose.html#ansys.aedt.core.application.variables.VariableManager.decompose "ansys.aedt.core.application.variables.VariableManager.decompose")(variable)  | Decompose a variable string to a floating with its unit.  |  
| [`VariableManager.delete_separator`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_separator.html#ansys.aedt.core.application.variables.VariableManager.delete_separator "ansys.aedt.core.application.variables.VariableManager.delete_separator")(name)  | Delete a separator from either the active project or design.  |  
| [`VariableManager.delete_unused_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_unused_variables.html#ansys.aedt.core.application.variables.VariableManager.delete_unused_variables "ansys.aedt.core.application.variables.VariableManager.delete_unused_variables")()  | Delete unused design and project variables.  |  
| [`VariableManager.delete_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.delete_variable.html#ansys.aedt.core.application.variables.VariableManager.delete_variable "ansys.aedt.core.application.variables.VariableManager.delete_variable")(name)  | Delete a variable.  |  
| [`VariableManager.get_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.get_expression.html#ansys.aedt.core.application.variables.VariableManager.get_expression "ansys.aedt.core.application.variables.VariableManager.get_expression")(name)  | Retrieve the variable value of a project or design variable as a string.  |  
| [`VariableManager.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.is_used.html#ansys.aedt.core.application.variables.VariableManager.is_used "ansys.aedt.core.application.variables.VariableManager.is_used")(name)  | Find if a variable is used.  |  
| [`VariableManager.set_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.set_variable.html#ansys.aedt.core.application.variables.VariableManager.set_variable "ansys.aedt.core.application.variables.VariableManager.set_variable")(name[, ...])  | Set the value of a design property or project variable.  |  
Attributes  
| [`VariableManager.dependent_design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_design_variable_names")  | List of dependent design variables.  |  
| --- | --- |  
| [`VariableManager.dependent_design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_design_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_design_variables "ansys.aedt.core.application.variables.VariableManager.dependent_design_variables")  | Dependent design variables.  |  
| [`VariableManager.dependent_project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_project_variable_names")  | List of dependent project variables.  |  
| [`VariableManager.dependent_project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_project_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_project_variables "ansys.aedt.core.application.variables.VariableManager.dependent_project_variables")  | Dependent project variables.  |  
| [`VariableManager.dependent_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_variable_names.html#ansys.aedt.core.application.variables.VariableManager.dependent_variable_names "ansys.aedt.core.application.variables.VariableManager.dependent_variable_names")  | List of dependent variables.  |  
| [`VariableManager.dependent_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.dependent_variables.html#ansys.aedt.core.application.variables.VariableManager.dependent_variables "ansys.aedt.core.application.variables.VariableManager.dependent_variables")  | Dependent variables.  |  
| [`VariableManager.design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.design_variable_names "ansys.aedt.core.application.variables.VariableManager.design_variable_names")  | List of design variables.  |  
| [`VariableManager.design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.design_variables.html#ansys.aedt.core.application.variables.VariableManager.design_variables "ansys.aedt.core.application.variables.VariableManager.design_variables")  | Design variables.  |  
| [`VariableManager.independent_design_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_design_variable_names")  | List of independent design variables.  |  
| [`VariableManager.independent_design_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_design_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_design_variables "ansys.aedt.core.application.variables.VariableManager.independent_design_variables")  | Independent design variables.  |  
| [`VariableManager.independent_project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_project_variable_names")  | List of independent project variables.  |  
| [`VariableManager.independent_project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_project_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_project_variables "ansys.aedt.core.application.variables.VariableManager.independent_project_variables")  | Independent project variables.  |  
| [`VariableManager.independent_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_variable_names.html#ansys.aedt.core.application.variables.VariableManager.independent_variable_names "ansys.aedt.core.application.variables.VariableManager.independent_variable_names")  | List of independent variables.  |  
| [`VariableManager.independent_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.independent_variables.html#ansys.aedt.core.application.variables.VariableManager.independent_variables "ansys.aedt.core.application.variables.VariableManager.independent_variables")  | Independent variables.  |  
| [`VariableManager.post_processing_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.post_processing_variables.html#ansys.aedt.core.application.variables.VariableManager.post_processing_variables "ansys.aedt.core.application.variables.VariableManager.post_processing_variables")  | Post Processing variables.  |  
| [`VariableManager.project_variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.project_variable_names.html#ansys.aedt.core.application.variables.VariableManager.project_variable_names "ansys.aedt.core.application.variables.VariableManager.project_variable_names")  | List of project variables.  |  
| [`VariableManager.project_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.project_variables.html#ansys.aedt.core.application.variables.VariableManager.project_variables "ansys.aedt.core.application.variables.VariableManager.project_variables")  | Project variables.  |  
| [`VariableManager.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.public_dir.html#ansys.aedt.core.application.variables.VariableManager.public_dir "ansys.aedt.core.application.variables.VariableManager.public_dir")  | Shortcut for dir(self).  |  
| [`VariableManager.variable_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.variable_names.html#ansys.aedt.core.application.variables.VariableManager.variable_names "ansys.aedt.core.application.variables.VariableManager.variable_names")  | List of variables.  |  
| [`VariableManager.variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.variables.html#ansys.aedt.core.application.variables.VariableManager.variables "ansys.aedt.core.application.variables.VariableManager.variables")  | Variables.  |