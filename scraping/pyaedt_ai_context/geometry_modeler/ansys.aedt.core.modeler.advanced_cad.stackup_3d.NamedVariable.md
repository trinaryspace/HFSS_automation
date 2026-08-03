---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# NamedVariable 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable(_application_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression_) 
    
Cast PyAEDT variable object to simplify getters and setters in Stackup3D. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The name of the variable. If the name begins with an ‘$’, the variable will be a project variable. Otherwise, it will be a design variable. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression of the value.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import NamedVariable
>>> hfss = Hfss()
>>> my_frequency = NamedVariable(hfss, "my_frequency", "900000Hz")
>>> wave_length_formula = "c0/" + my_frequency.name
>>> my_wave_length = NamedVariable(hfss, "my_wave_length", wave_length_formula)
>>> my_permittivity = NamedVariable(hfss, "my_permittivity", "2.2")
>>> my_wave_length.expression = my_wave_length.expression + "/" + my_permittivity.name

```
Copy to clipboard
Methods  
| [`NamedVariable.hide_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable")([value])  | Set the variable to a hidden variable.  |  
| --- | --- |  
| [`NamedVariable.read_only_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable")([value])  | Set the variable to a read-only variable.  |  
Attributes  
| [`NamedVariable.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value")  | String that combines the numeric value and the units.  |  
| --- | --- |  
| [`NamedVariable.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression")  | Expression of the variable as a string.  |  
| [`NamedVariable.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name")  | Name of the variable as a string.  |  
| [`NamedVariable.numeric_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value")  | Numeric part of the expression as a float value.  |  
| [`NamedVariable.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir")  | Shortcut for dir(self).  |  
| [`NamedVariable.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system")  | Unit system of the expression as a string.  |  
| [`NamedVariable.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units")  | Units.  |  
| [`NamedVariable.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value")  | Value.  |  
# NamedVariable 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable(_application_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression_) 
    
Cast PyAEDT variable object to simplify getters and setters in Stackup3D. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The name of the variable. If the name begins with an ‘$’, the variable will be a project variable. Otherwise, it will be a design variable. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression of the value.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import NamedVariable
>>> hfss = Hfss()
>>> my_frequency = NamedVariable(hfss, "my_frequency", "900000Hz")
>>> wave_length_formula = "c0/" + my_frequency.name
>>> my_wave_length = NamedVariable(hfss, "my_wave_length", wave_length_formula)
>>> my_permittivity = NamedVariable(hfss, "my_permittivity", "2.2")
>>> my_wave_length.expression = my_wave_length.expression + "/" + my_permittivity.name

```
Copy to clipboard
Methods  
| [`NamedVariable.hide_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable")([value])  | Set the variable to a hidden variable.  |  
| --- | --- |  
| [`NamedVariable.read_only_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable")([value])  | Set the variable to a read-only variable.  |  
Attributes  
| [`NamedVariable.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value")  | String that combines the numeric value and the units.  |  
| --- | --- |  
| [`NamedVariable.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression")  | Expression of the variable as a string.  |  
| [`NamedVariable.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name")  | Name of the variable as a string.  |  
| [`NamedVariable.numeric_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value")  | Numeric part of the expression as a float value.  |  
| [`NamedVariable.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir")  | Shortcut for dir(self).  |  
| [`NamedVariable.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system")  | Unit system of the expression as a string.  |  
| [`NamedVariable.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units")  | Units.  |  
| [`NamedVariable.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value")  | Value.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.rst.txt)

# NamedVariable 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable(_application_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression_) 
    
Cast PyAEDT variable object to simplify getters and setters in Stackup3D. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The name of the variable. If the name begins with an ‘$’, the variable will be a project variable. Otherwise, it will be a design variable. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression of the value.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import NamedVariable
>>> hfss = Hfss()
>>> my_frequency = NamedVariable(hfss, "my_frequency", "900000Hz")
>>> wave_length_formula = "c0/" + my_frequency.name
>>> my_wave_length = NamedVariable(hfss, "my_wave_length", wave_length_formula)
>>> my_permittivity = NamedVariable(hfss, "my_permittivity", "2.2")
>>> my_wave_length.expression = my_wave_length.expression + "/" + my_permittivity.name

```
Copy to clipboard
Methods  
| [`NamedVariable.hide_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.hide_variable")([value])  | Set the variable to a hidden variable.  |  
| --- | --- |  
| [`NamedVariable.read_only_variable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.read_only_variable")([value])  | Set the variable to a read-only variable.  |  
Attributes  
| [`NamedVariable.evaluated_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.evaluated_value")  | String that combines the numeric value and the units.  |  
| --- | --- |  
| [`NamedVariable.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.expression")  | Expression of the variable as a string.  |  
| [`NamedVariable.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.name")  | Name of the variable as a string.  |  
| [`NamedVariable.numeric_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.numeric_value")  | Numeric part of the expression as a float value.  |  
| [`NamedVariable.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.public_dir")  | Shortcut for dir(self).  |  
| [`NamedVariable.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.unit_system")  | Unit system of the expression as a string.  |  
| [`NamedVariable.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.units")  | Units.  |  
| [`NamedVariable.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.NamedVariable.value")  | Value.  |