---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# create_frequency_sweep 

SetupHFSS.create_frequency_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_, _num_of_freq_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_, _interpolation_tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_, _interpolation_max_solutions : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 250_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a sweep with the specified number of points. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit of the frequency.. The default is `None`, in which case the default desktop units are used. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Starting frequency of the sweep. The default is `1.0`. If a unit is passed with number, such as `"1MHz"`, the unit is ignored. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Stopping frequency of the sweep. The default is `10.0`. If a unit is passed with number, such as [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#id1)”1MHz”[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#id3), the unit is ignored. 

**num_of_freq_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of frequency points in the range. The default is `401` for a sweep type of `"Interpolating"` or `"Fast"`. The default is `5` for a sweep type of `"Discrete"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields. The default is `True`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the radiating fields. The default is `False`. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. Options are `"Fast"`, `"Interpolating"`, and `"Discrete"`. The default is `"Discrete"`. 

**interpolation_tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Error tolerance threshold for the interpolation process. The default is `0.5`. 

**interpolation_max_solutions**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of solutions evaluated for the interpolation process. The default is `250`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearCountSetup"` and use it in a linear count sweep named `"LinearCountSweep"`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup("LinearCountSetup")
>>> linear_count_sweep = setup.create_linear_count_sweep(
...     name="LinearStepSweep", unit="MHz", start_frequency=1.1e3, stop_frequency=1200.1, step_size=153.8
... )
>>> type(linear_count_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard
# create_frequency_sweep 

SetupHFSS.create_frequency_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_, _num_of_freq_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_, _interpolation_tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_, _interpolation_max_solutions : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 250_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a sweep with the specified number of points. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit of the frequency.. The default is `None`, in which case the default desktop units are used. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Starting frequency of the sweep. The default is `1.0`. If a unit is passed with number, such as `"1MHz"`, the unit is ignored. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Stopping frequency of the sweep. The default is `10.0`. If a unit is passed with number, such as [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#id1)”1MHz”[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#id3), the unit is ignored. 

**num_of_freq_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of frequency points in the range. The default is `401` for a sweep type of `"Interpolating"` or `"Fast"`. The default is `5` for a sweep type of `"Discrete"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields. The default is `True`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the radiating fields. The default is `False`. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. Options are `"Fast"`, `"Interpolating"`, and `"Discrete"`. The default is `"Discrete"`. 

**interpolation_tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Error tolerance threshold for the interpolation process. The default is `0.5`. 

**interpolation_max_solutions**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of solutions evaluated for the interpolation process. The default is `250`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearCountSetup"` and use it in a linear count sweep named `"LinearCountSweep"`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup("LinearCountSetup")
>>> linear_count_sweep = setup.create_linear_count_sweep(
...     name="LinearStepSweep", unit="MHz", start_frequency=1.1e3, stop_frequency=1200.1, step_size=153.8
... )
>>> type(linear_count_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.rst.txt)

# create_frequency_sweep 

SetupHFSS.create_frequency_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_, _num_of_freq_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_, _interpolation_tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_, _interpolation_max_solutions : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 250_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a sweep with the specified number of points. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit of the frequency.. The default is `None`, in which case the default desktop units are used. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Starting frequency of the sweep. The default is `1.0`. If a unit is passed with number, such as `"1MHz"`, the unit is ignored. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Stopping frequency of the sweep. The default is `10.0`. If a unit is passed with number, such as [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#id1)”1MHz”[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#id3), the unit is ignored. 

**num_of_freq_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of frequency points in the range. The default is `401` for a sweep type of `"Interpolating"` or `"Fast"`. The default is `5` for a sweep type of `"Discrete"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields. The default is `True`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the radiating fields. The default is `False`. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. Options are `"Fast"`, `"Interpolating"`, and `"Discrete"`. The default is `"Discrete"`. 

**interpolation_tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Error tolerance threshold for the interpolation process. The default is `0.5`. 

**interpolation_max_solutions**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of solutions evaluated for the interpolation process. The default is `250`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearCountSetup"` and use it in a linear count sweep named `"LinearCountSweep"`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup("LinearCountSetup")
>>> linear_count_sweep = setup.create_linear_count_sweep(
...     name="LinearStepSweep", unit="MHz", start_frequency=1.1e3, stop_frequency=1200.1, step_size=153.8
... )
>>> type(linear_count_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard