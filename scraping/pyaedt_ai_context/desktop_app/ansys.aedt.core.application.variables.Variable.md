---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# Variable 

class ansys.aedt.core.application.variables.Variable(_expression : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _si_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _full_variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _app =None_, _readonly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _hidden : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _description : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _postprocessing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _circuit_parameter : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Stores design properties and project variables and provides operations to perform on them. 

Parameters: 
     

**expression**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variable expression. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit string to enforce. If provided, must be consistent with parsed units. 

**si_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Value in SI units. If provided, it overrides the parsed/calculated value. 

**full_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Map of known variables for expression decomposition. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variable name in AEDT. 

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)"), `optional` 
    
AEDT application of type `ansys.aedt.core.application`. 

**readonly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flag controlling read only property. The default is `False`. 

**hidden**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling hidden property. The default is `False`. 

**sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling sweep property. The default is `True`. 

**postprocessing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling postprocessing property. 

**circuit_parameter**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Define Parameter Default variable in Circuit design.
Examples

```
>>> from ansys.aedt.core.application.variables import Variable

```
Copy to clipboard
Define a variable using a string value consistent with the AEDT properties.

```
>>> v = Variable("45mm")

```
Copy to clipboard
Define an unitless variable with a value of 3.0.

```
>>> v = Variable(3.0)

```
Copy to clipboard
Define a variable defined by a numeric result and a unit string.

```
>>> v = Variable(3.0 * 4.5, units="mm")
>>> assert v.numeric_value == 13.5
>>> assert v.units == "mm"

```
Copy to clipboard
Methods  
| [`Variable.decompose`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.decompose.html#ansys.aedt.core.application.variables.Variable.decompose "ansys.aedt.core.application.variables.Variable.decompose")()  | Decompose the evaluated expression into a floating-point number and units.  |  
| --- | --- |  
| [`Variable.format`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.format.html#ansys.aedt.core.application.variables.Variable.format "ansys.aedt.core.application.variables.Variable.format")(fmt)  | Return the string value using the specified numeric format ('06.2f').  |  
| [`Variable.rescale_to`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.rescale_to.html#ansys.aedt.core.application.variables.Variable.rescale_to "ansys.aedt.core.application.variables.Variable.rescale_to")(units)  | Rescale the expression to the provided _units_ within the same unit system.  |  
| [`Variable.update_var`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.update_var.html#ansys.aedt.core.application.variables.Variable.update_var "ansys.aedt.core.application.variables.Variable.update_var")()  | Push the current variable state to AEDT via variable manager.  |  
Attributes  
| [`Variable.description`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.description.html#ansys.aedt.core.application.variables.Variable.description "ansys.aedt.core.application.variables.Variable.description")  | Current description.  |  
| --- | --- |  
| [`Variable.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.evaluated_value.html#ansys.aedt.core.application.variables.Variable.evaluated_value "ansys.aedt.core.application.variables.Variable.evaluated_value")  | Concatenated numeric value and unit string.  |  
| [`Variable.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.expression.html#ansys.aedt.core.application.variables.Variable.expression "ansys.aedt.core.application.variables.Variable.expression")  | Raw AEDT expression.  |  
| [`Variable.has_definition_parameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.has_definition_parameters.html#ansys.aedt.core.application.variables.Variable.has_definition_parameters "ansys.aedt.core.application.variables.Variable.has_definition_parameters")  | Whether the design type has DefinitionParameters or only LocalVariables.  |  
| [`Variable.hidden`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.hidden.html#ansys.aedt.core.application.variables.Variable.hidden "ansys.aedt.core.application.variables.Variable.hidden")  | Current hidden flag.  |  
| [`Variable.is_circuit_parameter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_circuit_parameter.html#ansys.aedt.core.application.variables.Variable.is_circuit_parameter "ansys.aedt.core.application.variables.Variable.is_circuit_parameter")  | Whether this variable is a circuit parameter (for supported design types).  |  
| [`Variable.is_optimization_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_optimization_enabled.html#ansys.aedt.core.application.variables.Variable.is_optimization_enabled "ansys.aedt.core.application.variables.Variable.is_optimization_enabled")  | Whether optimization is enabled for this variable.  |  
| [`Variable.is_sensitivity_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled.html#ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled "ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled")  | Whether sensitivity analysis is enabled.  |  
| [`Variable.is_statistical_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_statistical_enabled.html#ansys.aedt.core.application.variables.Variable.is_statistical_enabled "ansys.aedt.core.application.variables.Variable.is_statistical_enabled")  | Whether statistical analysis is enabled.  |  
| [`Variable.is_tuning_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_tuning_enabled.html#ansys.aedt.core.application.variables.Variable.is_tuning_enabled "ansys.aedt.core.application.variables.Variable.is_tuning_enabled")  | Whether tuning is enabled.  |  
| [`Variable.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.name.html#ansys.aedt.core.application.variables.Variable.name "ansys.aedt.core.application.variables.Variable.name")  | Variable name.  |  
| [`Variable.numeric_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.numeric_value.html#ansys.aedt.core.application.variables.Variable.numeric_value "ansys.aedt.core.application.variables.Variable.numeric_value")  | Numeric value of the expression in current units.  |  
| [`Variable.optimization_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.optimization_max_value.html#ansys.aedt.core.application.variables.Variable.optimization_max_value "ansys.aedt.core.application.variables.Variable.optimization_max_value")  | Optimization upper bound.  |  
| [`Variable.optimization_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.optimization_min_value.html#ansys.aedt.core.application.variables.Variable.optimization_min_value "ansys.aedt.core.application.variables.Variable.optimization_min_value")  | Optimization lower bound.  |  
| [`Variable.post_processing`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.post_processing.html#ansys.aedt.core.application.variables.Variable.post_processing "ansys.aedt.core.application.variables.Variable.post_processing")  | Whether this variable is a post-processing variable.  |  
| [`Variable.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.public_dir.html#ansys.aedt.core.application.variables.Variable.public_dir "ansys.aedt.core.application.variables.Variable.public_dir")  | Shortcut for dir(self).  |  
| [`Variable.read_only`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.read_only.html#ansys.aedt.core.application.variables.Variable.read_only "ansys.aedt.core.application.variables.Variable.read_only")  | Current read-only flag.  |  
| [`Variable.sensitivity_initial_disp`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp.html#ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp "ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp")  | Sensitivity initial displacement (if applicable).  |  
| [`Variable.sensitivity_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_max_value.html#ansys.aedt.core.application.variables.Variable.sensitivity_max_value "ansys.aedt.core.application.variables.Variable.sensitivity_max_value")  | Sensitivity upper bound.  |  
| [`Variable.sensitivity_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_min_value.html#ansys.aedt.core.application.variables.Variable.sensitivity_min_value "ansys.aedt.core.application.variables.Variable.sensitivity_min_value")  | Sensitivity lower bound.  |  
| [`Variable.si_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.si_value.html#ansys.aedt.core.application.variables.Variable.si_value "ansys.aedt.core.application.variables.Variable.si_value")  | Current value in SI units (float).  |  
| [`Variable.sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sweep.html#ansys.aedt.core.application.variables.Variable.sweep "ansys.aedt.core.application.variables.Variable.sweep")  | Current sweep flag.  |  
| [`Variable.tuning_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_max_value.html#ansys.aedt.core.application.variables.Variable.tuning_max_value "ansys.aedt.core.application.variables.Variable.tuning_max_value")  | Tuning upper bound.  |  
| [`Variable.tuning_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_min_value.html#ansys.aedt.core.application.variables.Variable.tuning_min_value "ansys.aedt.core.application.variables.Variable.tuning_min_value")  | Tuning lower bound.  |  
| [`Variable.tuning_step_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_step_value.html#ansys.aedt.core.application.variables.Variable.tuning_step_value "ansys.aedt.core.application.variables.Variable.tuning_step_value")  | Tuning step value.  |  
| [`Variable.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.unit_system.html#ansys.aedt.core.application.variables.Variable.unit_system "ansys.aedt.core.application.variables.Variable.unit_system")  | Unit system name.  |  
| [`Variable.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.units.html#ansys.aedt.core.application.variables.Variable.units "ansys.aedt.core.application.variables.Variable.units")  | Unit string associated with the expression.  |  
# Variable 

class ansys.aedt.core.application.variables.Variable(_expression : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _si_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _full_variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _app =None_, _readonly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _hidden : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _description : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _postprocessing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _circuit_parameter : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Stores design properties and project variables and provides operations to perform on them. 

Parameters: 
     

**expression**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variable expression. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit string to enforce. If provided, must be consistent with parsed units. 

**si_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Value in SI units. If provided, it overrides the parsed/calculated value. 

**full_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Map of known variables for expression decomposition. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variable name in AEDT. 

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)"), `optional` 
    
AEDT application of type `ansys.aedt.core.application`. 

**readonly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flag controlling read only property. The default is `False`. 

**hidden**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling hidden property. The default is `False`. 

**sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling sweep property. The default is `True`. 

**postprocessing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling postprocessing property. 

**circuit_parameter**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Define Parameter Default variable in Circuit design.
Examples

```
>>> from ansys.aedt.core.application.variables import Variable

```
Copy to clipboard
Define a variable using a string value consistent with the AEDT properties.

```
>>> v = Variable("45mm")

```
Copy to clipboard
Define an unitless variable with a value of 3.0.

```
>>> v = Variable(3.0)

```
Copy to clipboard
Define a variable defined by a numeric result and a unit string.

```
>>> v = Variable(3.0 * 4.5, units="mm")
>>> assert v.numeric_value == 13.5
>>> assert v.units == "mm"

```
Copy to clipboard
Methods  
| [`Variable.decompose`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.decompose.html#ansys.aedt.core.application.variables.Variable.decompose "ansys.aedt.core.application.variables.Variable.decompose")()  | Decompose the evaluated expression into a floating-point number and units.  |  
| --- | --- |  
| [`Variable.format`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.format.html#ansys.aedt.core.application.variables.Variable.format "ansys.aedt.core.application.variables.Variable.format")(fmt)  | Return the string value using the specified numeric format ('06.2f').  |  
| [`Variable.rescale_to`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.rescale_to.html#ansys.aedt.core.application.variables.Variable.rescale_to "ansys.aedt.core.application.variables.Variable.rescale_to")(units)  | Rescale the expression to the provided _units_ within the same unit system.  |  
| [`Variable.update_var`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.update_var.html#ansys.aedt.core.application.variables.Variable.update_var "ansys.aedt.core.application.variables.Variable.update_var")()  | Push the current variable state to AEDT via variable manager.  |  
Attributes  
| [`Variable.description`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.description.html#ansys.aedt.core.application.variables.Variable.description "ansys.aedt.core.application.variables.Variable.description")  | Current description.  |  
| --- | --- |  
| [`Variable.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.evaluated_value.html#ansys.aedt.core.application.variables.Variable.evaluated_value "ansys.aedt.core.application.variables.Variable.evaluated_value")  | Concatenated numeric value and unit string.  |  
| [`Variable.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.expression.html#ansys.aedt.core.application.variables.Variable.expression "ansys.aedt.core.application.variables.Variable.expression")  | Raw AEDT expression.  |  
| [`Variable.has_definition_parameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.has_definition_parameters.html#ansys.aedt.core.application.variables.Variable.has_definition_parameters "ansys.aedt.core.application.variables.Variable.has_definition_parameters")  | Whether the design type has DefinitionParameters or only LocalVariables.  |  
| [`Variable.hidden`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.hidden.html#ansys.aedt.core.application.variables.Variable.hidden "ansys.aedt.core.application.variables.Variable.hidden")  | Current hidden flag.  |  
| [`Variable.is_circuit_parameter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_circuit_parameter.html#ansys.aedt.core.application.variables.Variable.is_circuit_parameter "ansys.aedt.core.application.variables.Variable.is_circuit_parameter")  | Whether this variable is a circuit parameter (for supported design types).  |  
| [`Variable.is_optimization_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_optimization_enabled.html#ansys.aedt.core.application.variables.Variable.is_optimization_enabled "ansys.aedt.core.application.variables.Variable.is_optimization_enabled")  | Whether optimization is enabled for this variable.  |  
| [`Variable.is_sensitivity_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled.html#ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled "ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled")  | Whether sensitivity analysis is enabled.  |  
| [`Variable.is_statistical_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_statistical_enabled.html#ansys.aedt.core.application.variables.Variable.is_statistical_enabled "ansys.aedt.core.application.variables.Variable.is_statistical_enabled")  | Whether statistical analysis is enabled.  |  
| [`Variable.is_tuning_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_tuning_enabled.html#ansys.aedt.core.application.variables.Variable.is_tuning_enabled "ansys.aedt.core.application.variables.Variable.is_tuning_enabled")  | Whether tuning is enabled.  |  
| [`Variable.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.name.html#ansys.aedt.core.application.variables.Variable.name "ansys.aedt.core.application.variables.Variable.name")  | Variable name.  |  
| [`Variable.numeric_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.numeric_value.html#ansys.aedt.core.application.variables.Variable.numeric_value "ansys.aedt.core.application.variables.Variable.numeric_value")  | Numeric value of the expression in current units.  |  
| [`Variable.optimization_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.optimization_max_value.html#ansys.aedt.core.application.variables.Variable.optimization_max_value "ansys.aedt.core.application.variables.Variable.optimization_max_value")  | Optimization upper bound.  |  
| [`Variable.optimization_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.optimization_min_value.html#ansys.aedt.core.application.variables.Variable.optimization_min_value "ansys.aedt.core.application.variables.Variable.optimization_min_value")  | Optimization lower bound.  |  
| [`Variable.post_processing`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.post_processing.html#ansys.aedt.core.application.variables.Variable.post_processing "ansys.aedt.core.application.variables.Variable.post_processing")  | Whether this variable is a post-processing variable.  |  
| [`Variable.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.public_dir.html#ansys.aedt.core.application.variables.Variable.public_dir "ansys.aedt.core.application.variables.Variable.public_dir")  | Shortcut for dir(self).  |  
| [`Variable.read_only`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.read_only.html#ansys.aedt.core.application.variables.Variable.read_only "ansys.aedt.core.application.variables.Variable.read_only")  | Current read-only flag.  |  
| [`Variable.sensitivity_initial_disp`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp.html#ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp "ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp")  | Sensitivity initial displacement (if applicable).  |  
| [`Variable.sensitivity_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_max_value.html#ansys.aedt.core.application.variables.Variable.sensitivity_max_value "ansys.aedt.core.application.variables.Variable.sensitivity_max_value")  | Sensitivity upper bound.  |  
| [`Variable.sensitivity_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_min_value.html#ansys.aedt.core.application.variables.Variable.sensitivity_min_value "ansys.aedt.core.application.variables.Variable.sensitivity_min_value")  | Sensitivity lower bound.  |  
| [`Variable.si_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.si_value.html#ansys.aedt.core.application.variables.Variable.si_value "ansys.aedt.core.application.variables.Variable.si_value")  | Current value in SI units (float).  |  
| [`Variable.sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sweep.html#ansys.aedt.core.application.variables.Variable.sweep "ansys.aedt.core.application.variables.Variable.sweep")  | Current sweep flag.  |  
| [`Variable.tuning_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_max_value.html#ansys.aedt.core.application.variables.Variable.tuning_max_value "ansys.aedt.core.application.variables.Variable.tuning_max_value")  | Tuning upper bound.  |  
| [`Variable.tuning_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_min_value.html#ansys.aedt.core.application.variables.Variable.tuning_min_value "ansys.aedt.core.application.variables.Variable.tuning_min_value")  | Tuning lower bound.  |  
| [`Variable.tuning_step_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_step_value.html#ansys.aedt.core.application.variables.Variable.tuning_step_value "ansys.aedt.core.application.variables.Variable.tuning_step_value")  | Tuning step value.  |  
| [`Variable.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.unit_system.html#ansys.aedt.core.application.variables.Variable.unit_system "ansys.aedt.core.application.variables.Variable.unit_system")  | Unit system name.  |  
| [`Variable.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.units.html#ansys.aedt.core.application.variables.Variable.units "ansys.aedt.core.application.variables.Variable.units")  | Unit string associated with the expression.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.Variable.rst.txt)

# Variable 

class ansys.aedt.core.application.variables.Variable(_expression : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _si_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _full_variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _app =None_, _readonly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _hidden : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _description : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _postprocessing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _circuit_parameter : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Stores design properties and project variables and provides operations to perform on them. 

Parameters: 
     

**expression**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variable expression. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit string to enforce. If provided, must be consistent with parsed units. 

**si_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Value in SI units. If provided, it overrides the parsed/calculated value. 

**full_variables**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Map of known variables for expression decomposition. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variable name in AEDT. 

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)"), `optional` 
    
AEDT application of type `ansys.aedt.core.application`. 

**readonly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flag controlling read only property. The default is `False`. 

**hidden**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling hidden property. The default is `False`. 

**sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling sweep property. The default is `True`. 

**postprocessing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Flags controlling postprocessing property. 

**circuit_parameter**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Define Parameter Default variable in Circuit design.
Examples

```
>>> from ansys.aedt.core.application.variables import Variable

```
Copy to clipboard
Define a variable using a string value consistent with the AEDT properties.

```
>>> v = Variable("45mm")

```
Copy to clipboard
Define an unitless variable with a value of 3.0.

```
>>> v = Variable(3.0)

```
Copy to clipboard
Define a variable defined by a numeric result and a unit string.

```
>>> v = Variable(3.0 * 4.5, units="mm")
>>> assert v.numeric_value == 13.5
>>> assert v.units == "mm"

```
Copy to clipboard
Methods  
| [`Variable.decompose`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.decompose.html#ansys.aedt.core.application.variables.Variable.decompose "ansys.aedt.core.application.variables.Variable.decompose")()  | Decompose the evaluated expression into a floating-point number and units.  |  
| --- | --- |  
| [`Variable.format`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.format.html#ansys.aedt.core.application.variables.Variable.format "ansys.aedt.core.application.variables.Variable.format")(fmt)  | Return the string value using the specified numeric format ('06.2f').  |  
| [`Variable.rescale_to`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.rescale_to.html#ansys.aedt.core.application.variables.Variable.rescale_to "ansys.aedt.core.application.variables.Variable.rescale_to")(units)  | Rescale the expression to the provided _units_ within the same unit system.  |  
| [`Variable.update_var`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.update_var.html#ansys.aedt.core.application.variables.Variable.update_var "ansys.aedt.core.application.variables.Variable.update_var")()  | Push the current variable state to AEDT via variable manager.  |  
Attributes  
| [`Variable.description`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.description.html#ansys.aedt.core.application.variables.Variable.description "ansys.aedt.core.application.variables.Variable.description")  | Current description.  |  
| --- | --- |  
| [`Variable.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.evaluated_value.html#ansys.aedt.core.application.variables.Variable.evaluated_value "ansys.aedt.core.application.variables.Variable.evaluated_value")  | Concatenated numeric value and unit string.  |  
| [`Variable.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.expression.html#ansys.aedt.core.application.variables.Variable.expression "ansys.aedt.core.application.variables.Variable.expression")  | Raw AEDT expression.  |  
| [`Variable.has_definition_parameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.has_definition_parameters.html#ansys.aedt.core.application.variables.Variable.has_definition_parameters "ansys.aedt.core.application.variables.Variable.has_definition_parameters")  | Whether the design type has DefinitionParameters or only LocalVariables.  |  
| [`Variable.hidden`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.hidden.html#ansys.aedt.core.application.variables.Variable.hidden "ansys.aedt.core.application.variables.Variable.hidden")  | Current hidden flag.  |  
| [`Variable.is_circuit_parameter`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_circuit_parameter.html#ansys.aedt.core.application.variables.Variable.is_circuit_parameter "ansys.aedt.core.application.variables.Variable.is_circuit_parameter")  | Whether this variable is a circuit parameter (for supported design types).  |  
| [`Variable.is_optimization_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_optimization_enabled.html#ansys.aedt.core.application.variables.Variable.is_optimization_enabled "ansys.aedt.core.application.variables.Variable.is_optimization_enabled")  | Whether optimization is enabled for this variable.  |  
| [`Variable.is_sensitivity_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled.html#ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled "ansys.aedt.core.application.variables.Variable.is_sensitivity_enabled")  | Whether sensitivity analysis is enabled.  |  
| [`Variable.is_statistical_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_statistical_enabled.html#ansys.aedt.core.application.variables.Variable.is_statistical_enabled "ansys.aedt.core.application.variables.Variable.is_statistical_enabled")  | Whether statistical analysis is enabled.  |  
| [`Variable.is_tuning_enabled`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_tuning_enabled.html#ansys.aedt.core.application.variables.Variable.is_tuning_enabled "ansys.aedt.core.application.variables.Variable.is_tuning_enabled")  | Whether tuning is enabled.  |  
| [`Variable.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.name.html#ansys.aedt.core.application.variables.Variable.name "ansys.aedt.core.application.variables.Variable.name")  | Variable name.  |  
| [`Variable.numeric_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.numeric_value.html#ansys.aedt.core.application.variables.Variable.numeric_value "ansys.aedt.core.application.variables.Variable.numeric_value")  | Numeric value of the expression in current units.  |  
| [`Variable.optimization_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.optimization_max_value.html#ansys.aedt.core.application.variables.Variable.optimization_max_value "ansys.aedt.core.application.variables.Variable.optimization_max_value")  | Optimization upper bound.  |  
| [`Variable.optimization_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.optimization_min_value.html#ansys.aedt.core.application.variables.Variable.optimization_min_value "ansys.aedt.core.application.variables.Variable.optimization_min_value")  | Optimization lower bound.  |  
| [`Variable.post_processing`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.post_processing.html#ansys.aedt.core.application.variables.Variable.post_processing "ansys.aedt.core.application.variables.Variable.post_processing")  | Whether this variable is a post-processing variable.  |  
| [`Variable.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.public_dir.html#ansys.aedt.core.application.variables.Variable.public_dir "ansys.aedt.core.application.variables.Variable.public_dir")  | Shortcut for dir(self).  |  
| [`Variable.read_only`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.read_only.html#ansys.aedt.core.application.variables.Variable.read_only "ansys.aedt.core.application.variables.Variable.read_only")  | Current read-only flag.  |  
| [`Variable.sensitivity_initial_disp`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp.html#ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp "ansys.aedt.core.application.variables.Variable.sensitivity_initial_disp")  | Sensitivity initial displacement (if applicable).  |  
| [`Variable.sensitivity_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_max_value.html#ansys.aedt.core.application.variables.Variable.sensitivity_max_value "ansys.aedt.core.application.variables.Variable.sensitivity_max_value")  | Sensitivity upper bound.  |  
| [`Variable.sensitivity_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sensitivity_min_value.html#ansys.aedt.core.application.variables.Variable.sensitivity_min_value "ansys.aedt.core.application.variables.Variable.sensitivity_min_value")  | Sensitivity lower bound.  |  
| [`Variable.si_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.si_value.html#ansys.aedt.core.application.variables.Variable.si_value "ansys.aedt.core.application.variables.Variable.si_value")  | Current value in SI units (float).  |  
| [`Variable.sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.sweep.html#ansys.aedt.core.application.variables.Variable.sweep "ansys.aedt.core.application.variables.Variable.sweep")  | Current sweep flag.  |  
| [`Variable.tuning_max_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_max_value.html#ansys.aedt.core.application.variables.Variable.tuning_max_value "ansys.aedt.core.application.variables.Variable.tuning_max_value")  | Tuning upper bound.  |  
| [`Variable.tuning_min_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_min_value.html#ansys.aedt.core.application.variables.Variable.tuning_min_value "ansys.aedt.core.application.variables.Variable.tuning_min_value")  | Tuning lower bound.  |  
| [`Variable.tuning_step_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.tuning_step_value.html#ansys.aedt.core.application.variables.Variable.tuning_step_value "ansys.aedt.core.application.variables.Variable.tuning_step_value")  | Tuning step value.  |  
| [`Variable.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.unit_system.html#ansys.aedt.core.application.variables.Variable.unit_system "ansys.aedt.core.application.variables.Variable.unit_system")  | Unit system name.  |  
| [`Variable.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.units.html#ansys.aedt.core.application.variables.Variable.units "ansys.aedt.core.application.variables.Variable.units")  | Unit string associated with the expression.  |