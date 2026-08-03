---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.parse_dim_arg.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# parse_dim_arg 

static GeometryOperators.parse_dim_arg(_string : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _scale_to_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variable_manager =None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Convert a number and unit to a float.
Angles are converted in radians. 

Parameters: 
     

**string**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String to convert. For example, `"2mm"`. The default is `None`. 

**scale_to_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the value to convert. For example, `"mm"`. 

**variable_manager**[`ansys.aedt.core.application.variables.VariableManager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.html#ansys.aedt.core.application.variables.VariableManager "ansys.aedt.core.application.variables.VariableManager"), `optional` 
    
Try to parse formula and returns numeric value. The default is `None`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Value for the converted value and units. For example, `0.002`.
Examples
Parse ‘“2mm”’.

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators as go
>>> go.parse_dim_arg("2mm")
>>> 0.002

```
Copy to clipboard
Use the optional argument `scale_to_unit` to specify the destination unit.

```
>>> go.parse_dim_arg("2mm", scale_to_unit="mm")
>>> 2.0

```
Copy to clipboard
# parse_dim_arg 

static GeometryOperators.parse_dim_arg(_string : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _scale_to_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variable_manager =None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Convert a number and unit to a float.
Angles are converted in radians. 

Parameters: 
     

**string**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String to convert. For example, `"2mm"`. The default is `None`. 

**scale_to_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the value to convert. For example, `"mm"`. 

**variable_manager**[`ansys.aedt.core.application.variables.VariableManager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.html#ansys.aedt.core.application.variables.VariableManager "ansys.aedt.core.application.variables.VariableManager"), `optional` 
    
Try to parse formula and returns numeric value. The default is `None`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Value for the converted value and units. For example, `0.002`.
Examples
Parse ‘“2mm”’.

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators as go
>>> go.parse_dim_arg("2mm")
>>> 0.002

```
Copy to clipboard
Use the optional argument `scale_to_unit` to specify the destination unit.

```
>>> go.parse_dim_arg("2mm", scale_to_unit="mm")
>>> 2.0

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.parse_dim_arg.rst.txt)

# parse_dim_arg 

static GeometryOperators.parse_dim_arg(_string : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _scale_to_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variable_manager =None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Convert a number and unit to a float.
Angles are converted in radians. 

Parameters: 
     

**string**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
String to convert. For example, `"2mm"`. The default is `None`. 

**scale_to_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the value to convert. For example, `"mm"`. 

**variable_manager**[`ansys.aedt.core.application.variables.VariableManager`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.VariableManager.html#ansys.aedt.core.application.variables.VariableManager "ansys.aedt.core.application.variables.VariableManager"), `optional` 
    
Try to parse formula and returns numeric value. The default is `None`. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Value for the converted value and units. For example, `0.002`.
Examples
Parse ‘“2mm”’.

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators as go
>>> go.parse_dim_arg("2mm")
>>> 0.002

```
Copy to clipboard
Use the optional argument `scale_to_unit` to specify the destination unit.

```
>>> go.parse_dim_arg("2mm", scale_to_unit="mm")
>>> 2.0

```
Copy to clipboard