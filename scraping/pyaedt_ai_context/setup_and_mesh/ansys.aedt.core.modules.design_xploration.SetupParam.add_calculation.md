---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_calculation 

SetupParam.add_calculation(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a calculation to the setup. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of ranges with respective values. Values can be: None for all values, a List of Discrete Values, a tuple of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. The default is `None`, to be used e.g. in “Eigenmode” design type. 

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
>>> from ansys.aedt.core.modules.design_xploration import CommonOptimetrics
>>> obj = CommonOptimetrics()
>>> obj.add_calculation(calculation=1)

```
Copy to clipboard
# add_calculation 

SetupParam.add_calculation(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a calculation to the setup. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of ranges with respective values. Values can be: None for all values, a List of Discrete Values, a tuple of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. The default is `None`, to be used e.g. in “Eigenmode” design type. 

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
>>> from ansys.aedt.core.modules.design_xploration import CommonOptimetrics
>>> obj = CommonOptimetrics()
>>> obj.add_calculation(calculation=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation.rst.txt)

# add_calculation 

SetupParam.add_calculation(_calculation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ranges : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _variables : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a calculation to the setup. 

Parameters: 
     

**calculation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the calculation. 

**ranges**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of ranges with respective values. Values can be: None for all values, a List of Discrete Values, a tuple of start and stop range. It includes intrinsics like “Freq”, “Time”, “Theta”, “Distance”. The default is `None`, to be used e.g. in “Eigenmode” design type. 

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
>>> from ansys.aedt.core.modules.design_xploration import CommonOptimetrics
>>> obj = CommonOptimetrics()
>>> obj.add_calculation(calculation=1)

```
Copy to clipboard