---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# create_single_point_sweep 

SetupHFSS.create_single_point_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = 1_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_single_field : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = True_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Sweep with a single frequency point. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. 

**freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency of the single point or list of frequencies to create distinct single points. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_single_field**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields of the single point. The default is `True`. If a list is specified, the length must be the same as the frequency length. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields for all points and subranges defined in the sweep. The default is `False`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save only the radiating fields. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearStepSetup"` and use it in a single point sweep named `"SinglePointSweep"`.

```
>>> setup = hfss.create_setup("LinearStepSetup")
>>> single_point_sweep = setup.create_single_point_sweep(name="SinglePointSweep", unit="MHz", freq=1.1e3)
>>> type(single_point_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard
# create_single_point_sweep 

SetupHFSS.create_single_point_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = 1_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_single_field : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = True_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Sweep with a single frequency point. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. 

**freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency of the single point or list of frequencies to create distinct single points. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_single_field**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields of the single point. The default is `True`. If a list is specified, the length must be the same as the frequency length. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields for all points and subranges defined in the sweep. The default is `False`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save only the radiating fields. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearStepSetup"` and use it in a single point sweep named `"SinglePointSweep"`.

```
>>> setup = hfss.create_setup("LinearStepSetup")
>>> single_point_sweep = setup.create_single_point_sweep(name="SinglePointSweep", unit="MHz", freq=1.1e3)
>>> type(single_point_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep.rst.txt)

# create_single_point_sweep 

SetupHFSS.create_single_point_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = 1_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_single_field : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = True_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Sweep with a single frequency point. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. 

**freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency of the single point or list of frequencies to create distinct single points. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_single_field**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields of the single point. The default is `True`. If a list is specified, the length must be the same as the frequency length. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields for all points and subranges defined in the sweep. The default is `False`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save only the radiating fields. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearStepSetup"` and use it in a single point sweep named `"SinglePointSweep"`.

```
>>> setup = hfss.create_setup("LinearStepSetup")
>>> single_point_sweep = setup.create_single_point_sweep(name="SinglePointSweep", unit="MHz", freq=1.1e3)
>>> type(single_point_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard