---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.OptimizationSetups.add.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add 

OptimizationSetups.add(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _variables : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _optimization_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Optimization'_, _condition : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '<='_, _goal_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _goal_weight : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SetupOpti](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.html#ansys.aedt.core.modules.design_xploration.SetupOpti "ansys.aedt.core.modules.design_xploration.SetupOpti") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a basic optimization analysis. You can customize all options after the analysis is added. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of ranges with respective values. Values can be: a list of discrete values, a dict with tuple args of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. 

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include in the optimization. By default all variables are included. 

**optimization_type**`strm` `optional` 
    
Optimization Type. Possible values are “Optimization”, “DXDOE”,`”DesignExplorer”,”Sensitivity”,”Statistical”` and “optiSLang”. 

**condition**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"<="`. 

**goal_value**`optional` 
    
Value for the goal. The default is `1`. 

**goal_weight**`optional` 
    
Value for the goal weight. The default is `1`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the analysis. The default is `None`, in which case a default name is assigned. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Calculation contexts. It can be a sphere, a matrix or a polyline. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign id for Circuit and HFSS 3D Layout objects. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points for Polyline context. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Override the auto computation of Calculation Type. 

Returns: 
     

[`ansys.aedt.core.modules.design_xploration.SetupOpti`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.html#ansys.aedt.core.modules.design_xploration.SetupOpti "ansys.aedt.core.modules.design_xploration.SetupOpti")
    
Optimization object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import OptimizationSetups
>>> obj = OptimizationSetups()
>>> obj.add(name="MyObject", calculation=1)

```
Copy to clipboard
# add 

OptimizationSetups.add(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _variables : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _optimization_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Optimization'_, _condition : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '<='_, _goal_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _goal_weight : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SetupOpti](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.html#ansys.aedt.core.modules.design_xploration.SetupOpti "ansys.aedt.core.modules.design_xploration.SetupOpti") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a basic optimization analysis. You can customize all options after the analysis is added. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of ranges with respective values. Values can be: a list of discrete values, a dict with tuple args of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. 

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include in the optimization. By default all variables are included. 

**optimization_type**`strm` `optional` 
    
Optimization Type. Possible values are “Optimization”, “DXDOE”,`”DesignExplorer”,”Sensitivity”,”Statistical”` and “optiSLang”. 

**condition**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"<="`. 

**goal_value**`optional` 
    
Value for the goal. The default is `1`. 

**goal_weight**`optional` 
    
Value for the goal weight. The default is `1`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the analysis. The default is `None`, in which case a default name is assigned. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Calculation contexts. It can be a sphere, a matrix or a polyline. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign id for Circuit and HFSS 3D Layout objects. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points for Polyline context. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Override the auto computation of Calculation Type. 

Returns: 
     

[`ansys.aedt.core.modules.design_xploration.SetupOpti`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.html#ansys.aedt.core.modules.design_xploration.SetupOpti "ansys.aedt.core.modules.design_xploration.SetupOpti")
    
Optimization object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import OptimizationSetups
>>> obj = OptimizationSetups()
>>> obj.add(name="MyObject", calculation=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.OptimizationSetups.add.rst.txt)

# add 

OptimizationSetups.add(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _variables : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _optimization_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Optimization'_, _condition : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '<='_, _goal_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _goal_weight : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SetupOpti](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.html#ansys.aedt.core.modules.design_xploration.SetupOpti "ansys.aedt.core.modules.design_xploration.SetupOpti") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a basic optimization analysis. You can customize all options after the analysis is added. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of ranges with respective values. Values can be: a list of discrete values, a dict with tuple args of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. 

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include in the optimization. By default all variables are included. 

**optimization_type**`strm` `optional` 
    
Optimization Type. Possible values are “Optimization”, “DXDOE”,`”DesignExplorer”,”Sensitivity”,”Statistical”` and “optiSLang”. 

**condition**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"<="`. 

**goal_value**`optional` 
    
Value for the goal. The default is `1`. 

**goal_weight**`optional` 
    
Value for the goal weight. The default is `1`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the analysis. The default is `None`, in which case a default name is assigned. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Calculation contexts. It can be a sphere, a matrix or a polyline. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign id for Circuit and HFSS 3D Layout objects. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points for Polyline context. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Override the auto computation of Calculation Type. 

Returns: 
     

[`ansys.aedt.core.modules.design_xploration.SetupOpti`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.html#ansys.aedt.core.modules.design_xploration.SetupOpti "ansys.aedt.core.modules.design_xploration.SetupOpti")
    
Optimization object.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import OptimizationSetups
>>> obj = OptimizationSetups()
>>> obj.add(name="MyObject", calculation=1)

```
Copy to clipboard