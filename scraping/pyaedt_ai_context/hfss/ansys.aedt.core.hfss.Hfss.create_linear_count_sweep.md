---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_linear_count_sweep.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_linear_count_sweep 

Hfss.create_linear_count_sweep(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _num_of_freq_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_, _interpolation_tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_, _interpolation_max_solutions : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 250_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a sweep with a specified number of points. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz"` or `"GHz"`. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency of the sweep, such as `1`. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stopping frequency of the sweep. 

**num_of_freq_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of frequency points in the range. The default is `401` for `sweep_type = "Interpolating"`. The defaults are “Fast”`` and `5` for `sweep_type = ""Discrete"`. 

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
>>> setup = hfss.create_setup("LinearCountSetup")
>>> linear_count_sweep = hfss.create_linear_count_sweep(
...     setup="LinearCountSetup",
...     sweep="LinearCountSweep",
...     unit="MHz",
...     start_frequency=1.1e3,
...     stop_frequency=1200.1,
...     num_of_freq_points=1658,
... )
>>> type(linear_count_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard
# create_linear_count_sweep 

Hfss.create_linear_count_sweep(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _num_of_freq_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_, _interpolation_tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_, _interpolation_max_solutions : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 250_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a sweep with a specified number of points. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz"` or `"GHz"`. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency of the sweep, such as `1`. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stopping frequency of the sweep. 

**num_of_freq_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of frequency points in the range. The default is `401` for `sweep_type = "Interpolating"`. The defaults are “Fast”`` and `5` for `sweep_type = ""Discrete"`. 

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
>>> setup = hfss.create_setup("LinearCountSetup")
>>> linear_count_sweep = hfss.create_linear_count_sweep(
...     setup="LinearCountSetup",
...     sweep="LinearCountSweep",
...     unit="MHz",
...     start_frequency=1.1e3,
...     stop_frequency=1200.1,
...     num_of_freq_points=1658,
... )
>>> type(linear_count_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_linear_count_sweep.rst.txt)

# create_linear_count_sweep 

Hfss.create_linear_count_sweep(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _num_of_freq_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_, _interpolation_tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_, _interpolation_max_solutions : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 250_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a sweep with a specified number of points. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz"` or `"GHz"`. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting frequency of the sweep, such as `1`. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Stopping frequency of the sweep. 

**num_of_freq_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of frequency points in the range. The default is `401` for `sweep_type = "Interpolating"`. The defaults are “Fast”`` and `5` for `sweep_type = ""Discrete"`. 

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
>>> setup = hfss.create_setup("LinearCountSetup")
>>> linear_count_sweep = hfss.create_linear_count_sweep(
...     setup="LinearCountSetup",
...     sweep="LinearCountSweep",
...     unit="MHz",
...     start_frequency=1.1e3,
...     stop_frequency=1200.1,
...     num_of_freq_points=1658,
... )
>>> type(linear_count_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard