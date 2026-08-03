---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_variation.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_variation 

SetupParam.add_variation(_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LinearCount'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a variation to an existing parametric setup. 

Parameters: 
     

**sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**start_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Variation Start Point. 

**end_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation End Point. This parameter is optional if a Single Value is defined. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation Step or Count depending on variation_type. Default is 100. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation units. Default is None. 

**variation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation Type. Admitted values are “SingleValue”, `”LinearCount”, “LinearStep”, “DecadeCount”, “OctaveCount”, “ExponentialCount”. 

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
>>> obj.add_variation(sweep_variable=1, start_point=1.0)

```
Copy to clipboard
# add_variation 

SetupParam.add_variation(_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LinearCount'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a variation to an existing parametric setup. 

Parameters: 
     

**sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**start_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Variation Start Point. 

**end_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation End Point. This parameter is optional if a Single Value is defined. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation Step or Count depending on variation_type. Default is 100. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation units. Default is None. 

**variation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation Type. Admitted values are “SingleValue”, `”LinearCount”, “LinearStep”, “DecadeCount”, “OctaveCount”, “ExponentialCount”. 

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
>>> obj.add_variation(sweep_variable=1, start_point=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_variation.rst.txt)

# add_variation 

SetupParam.add_variation(_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LinearCount'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a variation to an existing parametric setup. 

Parameters: 
     

**sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**start_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Variation Start Point. 

**end_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation End Point. This parameter is optional if a Single Value is defined. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation Step or Count depending on variation_type. Default is 100. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation units. Default is None. 

**variation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation Type. Admitted values are “SingleValue”, `”LinearCount”, “LinearStep”, “DecadeCount”, “OctaveCount”, “ExponentialCount”. 

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
>>> obj.add_variation(sweep_variable=1, start_point=1.0)

```
Copy to clipboard