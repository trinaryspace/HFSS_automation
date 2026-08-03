---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_goal 

SetupOpti.add_goal(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _condition : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '<='_, _goal_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _goal_weight : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a goal to the setup. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of ranges with respective values. Values can be: None for all values, a List of Discrete Values, a tuple of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. 

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include in the optimization. 

**condition**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"<="`. 

**goal_value**`optional` 
    
Value for the goal. The default is `1`. 

**goal_weight**`optional` 
    
Value for the goal weight. The default is `1`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Calculation contexts. It can be a sphere, a matrix or a polyline. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign id for Circuit and HFSS 3D Layout objects. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points for Polyline context. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Override the auto computation of Calculation Type. 

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
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()
>>> obj.add_goal(calculation=1, ranges={"Name": "Value"})

```
Copy to clipboard
# add_goal 

SetupOpti.add_goal(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _condition : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '<='_, _goal_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _goal_weight : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a goal to the setup. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of ranges with respective values. Values can be: None for all values, a List of Discrete Values, a tuple of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. 

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include in the optimization. 

**condition**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"<="`. 

**goal_value**`optional` 
    
Value for the goal. The default is `1`. 

**goal_weight**`optional` 
    
Value for the goal weight. The default is `1`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Calculation contexts. It can be a sphere, a matrix or a polyline. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign id for Circuit and HFSS 3D Layout objects. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points for Polyline context. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Override the auto computation of Calculation Type. 

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
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()
>>> obj.add_goal(calculation=1, ranges={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal.rst.txt)

# add_goal 

SetupOpti.add_goal(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _condition : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '<='_, _goal_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _goal_weight : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a goal to the setup. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of ranges with respective values. Values can be: None for all values, a List of Discrete Values, a tuple of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. 

**variables**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include in the optimization. 

**condition**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"<="`. 

**goal_value**`optional` 
    
Value for the goal. The default is `1`. 

**goal_weight**`optional` 
    
Value for the goal weight. The default is `1`. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. The default is `None`, in which case the default solution is used. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Calculation contexts. It can be a sphere, a matrix or a polyline. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign id for Circuit and HFSS 3D Layout objects. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points for Polyline context. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Override the auto computation of Calculation Type. 

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
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()
>>> obj.add_goal(calculation=1, ranges={"Name": "Value"})

```
Copy to clipboard