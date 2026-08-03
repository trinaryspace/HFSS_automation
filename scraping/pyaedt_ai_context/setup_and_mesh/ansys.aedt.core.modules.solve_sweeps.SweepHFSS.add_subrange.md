---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_subrange 

SweepHFSS.add_subrange(_range_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _count : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _save_single_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _clear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a range to the sweep. 

Parameters: 
     

**range_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the range. Options are `"LinearCount"`, `"LinearStep"`, `"LogScale"`, and `"SinglePoints"`. 

**start**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency. 

**end**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stopping frequency. The default value is `None`. A value is required for `range_type="LinearCount"|"LinearStep"|"LogScale"`. 

**count**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency count or frequency step. The default is `None`. A value is required for `range_type="LinearCount"|"LinearStep"|"LogScale"`. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. The default is `"GHz"`. 

**save_single_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields of the single point. The default is `False`. This parameter is used only for `range_type="SinglePoints"`. 

**clear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to suppress all other subranges except the current one under creation. The default value is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Create a setup in an HFSS design and add multiple sweep ranges.

```
>>> setup = hfss.create_setup(name="MySetup")
>>> sweep = setup.add_sweep()
>>> sweep.change_type("Interpolating")
>>> sweep.change_range("LinearStep", 1.1, 2.1, 0.4, "GHz")
>>> sweep.add_subrange("LinearCount", 1, 1.5, 5, "MHz")
>>> sweep.add_subrange("LogScale", 1, 3, 10, "GHz")

```
Copy to clipboard
# add_subrange 

SweepHFSS.add_subrange(_range_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _count : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _save_single_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _clear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a range to the sweep. 

Parameters: 
     

**range_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the range. Options are `"LinearCount"`, `"LinearStep"`, `"LogScale"`, and `"SinglePoints"`. 

**start**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency. 

**end**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stopping frequency. The default value is `None`. A value is required for `range_type="LinearCount"|"LinearStep"|"LogScale"`. 

**count**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency count or frequency step. The default is `None`. A value is required for `range_type="LinearCount"|"LinearStep"|"LogScale"`. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. The default is `"GHz"`. 

**save_single_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields of the single point. The default is `False`. This parameter is used only for `range_type="SinglePoints"`. 

**clear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to suppress all other subranges except the current one under creation. The default value is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Create a setup in an HFSS design and add multiple sweep ranges.

```
>>> setup = hfss.create_setup(name="MySetup")
>>> sweep = setup.add_sweep()
>>> sweep.change_type("Interpolating")
>>> sweep.change_range("LinearStep", 1.1, 2.1, 0.4, "GHz")
>>> sweep.add_subrange("LinearCount", 1, 1.5, 5, "MHz")
>>> sweep.add_subrange("LogScale", 1, 3, 10, "GHz")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange.rst.txt)

# add_subrange 

SweepHFSS.add_subrange(_range_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _end : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _count : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _save_single_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _clear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a range to the sweep. 

Parameters: 
     

**range_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the range. Options are `"LinearCount"`, `"LinearStep"`, `"LogScale"`, and `"SinglePoints"`. 

**start**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency. 

**end**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stopping frequency. The default value is `None`. A value is required for `range_type="LinearCount"|"LinearStep"|"LogScale"`. 

**count**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency count or frequency step. The default is `None`. A value is required for `range_type="LinearCount"|"LinearStep"|"LogScale"`. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. The default is `"GHz"`. 

**save_single_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields of the single point. The default is `False`. This parameter is used only for `range_type="SinglePoints"`. 

**clear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to suppress all other subranges except the current one under creation. The default value is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Create a setup in an HFSS design and add multiple sweep ranges.

```
>>> setup = hfss.create_setup(name="MySetup")
>>> sweep = setup.add_sweep()
>>> sweep.change_type("Interpolating")
>>> sweep.change_range("LinearStep", 1.1, 2.1, 0.4, "GHz")
>>> sweep.add_subrange("LinearCount", 1, 1.5, 5, "MHz")
>>> sweep.add_subrange("LogScale", 1, 3, 10, "GHz")

```
Copy to clipboard