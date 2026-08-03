---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.add.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add 

ParametricSetups.add(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _variation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LinearCount'_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SetupParam](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a basic sensitivity analysis. You can customize all options after the analysis is added. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**start_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variation Start Point if a variation is defined or Single Value. 

**end_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation End Point. This parameter is optional if a Single Value is defined. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `or` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variation Step or Count depending on variation_type. The default is `100` for the “LinearCount” variation_type. If a string is passed as an argument, it must be a valid expression in the given context. For example, “0.1mm” may be passed for a step size when the variation_type is “LinearStep”. 

**variation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation Type. Permitted values are “LinearCount”, “LinearStep”, “LogScale”, “SingleValue”. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sensitivity analysis. The default is `None`, in which case a default name is assigned. 

Returns: 
     

[`ansys.aedt.core.modules.design_xploration.SetupParam`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam")
    
Optimization Object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import ParametricSetups
>>> obj = ParametricSetups()
>>> obj.add(variable=1, start_point=1.0)

```
Copy to clipboard
# add 

ParametricSetups.add(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _variation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LinearCount'_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SetupParam](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a basic sensitivity analysis. You can customize all options after the analysis is added. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**start_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variation Start Point if a variation is defined or Single Value. 

**end_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation End Point. This parameter is optional if a Single Value is defined. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `or` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variation Step or Count depending on variation_type. The default is `100` for the “LinearCount” variation_type. If a string is passed as an argument, it must be a valid expression in the given context. For example, “0.1mm” may be passed for a step size when the variation_type is “LinearStep”. 

**variation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation Type. Permitted values are “LinearCount”, “LinearStep”, “LogScale”, “SingleValue”. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sensitivity analysis. The default is `None`, in which case a default name is assigned. 

Returns: 
     

[`ansys.aedt.core.modules.design_xploration.SetupParam`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam")
    
Optimization Object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import ParametricSetups
>>> obj = ParametricSetups()
>>> obj.add(variable=1, start_point=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.add.rst.txt)

# add 

ParametricSetups.add(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end_point : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _variation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'LinearCount'_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SetupParam](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a basic sensitivity analysis. You can customize all options after the analysis is added. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**start_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variation Start Point if a variation is defined or Single Value. 

**end_point**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Variation End Point. This parameter is optional if a Single Value is defined. 

**step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `or` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Variation Step or Count depending on variation_type. The default is `100` for the “LinearCount” variation_type. If a string is passed as an argument, it must be a valid expression in the given context. For example, “0.1mm” may be passed for a step size when the variation_type is “LinearStep”. 

**variation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation Type. Permitted values are “LinearCount”, “LinearStep”, “LogScale”, “SingleValue”. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sensitivity analysis. The default is `None`, in which case a default name is assigned. 

Returns: 
     

[`ansys.aedt.core.modules.design_xploration.SetupParam`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam")
    
Optimization Object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import ParametricSetups
>>> obj = ParametricSetups()
>>> obj.add(variable=1, start_point=1.0)

```
Copy to clipboard