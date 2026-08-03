---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_variation 

SetupOpti.add_variation(_variable_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _min_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _max_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _starting_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _min_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _max_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _use_manufacturable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _levels : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new variable as input for the optimization and defines its ranges. 

Parameters: 
     

**variable_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**min_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum Optimization Value for variable_name. 

**max_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Optimization Value for variable_name. 

**starting_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Starting point for optimization. If None, default will be used. 

**min_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum Step Size for optimization. If None, 1/100 of the range will be used. 

**max_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Step Size for optimization. If None, 1/10 of the range will be used. 

**use_manufacturable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if to use or not the manufacturable values. Default is False. 

**levels**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of available manufacturer levels. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()
>>> obj.add_variation(variable_name=1, min_value=1.0, max_value=1.0)

```
Copy to clipboard
# add_variation 

SetupOpti.add_variation(_variable_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _min_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _max_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _starting_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _min_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _max_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _use_manufacturable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _levels : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new variable as input for the optimization and defines its ranges. 

Parameters: 
     

**variable_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**min_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum Optimization Value for variable_name. 

**max_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Optimization Value for variable_name. 

**starting_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Starting point for optimization. If None, default will be used. 

**min_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum Step Size for optimization. If None, 1/100 of the range will be used. 

**max_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Step Size for optimization. If None, 1/10 of the range will be used. 

**use_manufacturable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if to use or not the manufacturable values. Default is False. 

**levels**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of available manufacturer levels. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()
>>> obj.add_variation(variable_name=1, min_value=1.0, max_value=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation.rst.txt)

# add_variation 

SetupOpti.add_variation(_variable_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _min_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _max_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _starting_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _min_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _max_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _use_manufacturable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _levels : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new variable as input for the optimization and defines its ranges. 

Parameters: 
     

**variable_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**min_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum Optimization Value for variable_name. 

**max_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Optimization Value for variable_name. 

**starting_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Starting point for optimization. If None, default will be used. 

**min_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum Step Size for optimization. If None, 1/100 of the range will be used. 

**max_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum Step Size for optimization. If None, 1/10 of the range will be used. 

**use_manufacturable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if to use or not the manufacturable values. Default is False. 

**levels**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of available manufacturer levels. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()
>>> obj.add_variation(variable_name=1, min_value=1.0, max_value=1.0)

```
Copy to clipboard