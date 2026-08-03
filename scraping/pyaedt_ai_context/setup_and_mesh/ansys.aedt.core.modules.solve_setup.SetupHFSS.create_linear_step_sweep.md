---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# create_linear_step_sweep 

SetupHFSS.create_linear_step_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.0_, _step_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.05_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Sweep with a specified frequency step. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Starting frequency of the sweep. The default is `0.1`. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stopping frequency of the sweep. The default is `2.0`. 

**step_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency size of the step. The default is `0.05`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields. The default is `True`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the radiating fields. The default is `False`. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to create a `"Discrete"`,``”Interpolating”`` or `"Fast"` sweep. The default is `"Discrete"`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearStepSetup"` and use it in a linear step sweep named `"LinearStepSweep"`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup("LinearStepSetup")
>>> linear_step_sweep = setup.create_linear_step_sweep(
...     name="LinearStepSweep", unit="MHz", start_frequency=1.1e3, stop_frequency=1200.1, step_size=153.8
... )
>>> type(linear_step_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard
# create_linear_step_sweep 

SetupHFSS.create_linear_step_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.0_, _step_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.05_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Sweep with a specified frequency step. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Starting frequency of the sweep. The default is `0.1`. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stopping frequency of the sweep. The default is `2.0`. 

**step_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency size of the step. The default is `0.05`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields. The default is `True`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the radiating fields. The default is `False`. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to create a `"Discrete"`,``”Interpolating”`` or `"Fast"` sweep. The default is `"Discrete"`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearStepSetup"` and use it in a linear step sweep named `"LinearStepSweep"`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup("LinearStepSetup")
>>> linear_step_sweep = setup.create_linear_step_sweep(
...     name="LinearStepSweep", unit="MHz", start_frequency=1.1e3, stop_frequency=1200.1, step_size=153.8
... )
>>> type(linear_step_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep.rst.txt)

# create_linear_step_sweep 

SetupHFSS.create_linear_step_sweep(_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GHz'_, _start_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _stop_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.0_, _step_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.05_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _save_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _save_rad_fields : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Discrete'_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Sweep with a specified frequency step. 

Parameters: 
     

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Unit of the frequency. For example, `"MHz` or `"GHz"`. 

**start_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Starting frequency of the sweep. The default is `0.1`. 

**stop_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Stopping frequency of the sweep. The default is `2.0`. 

**step_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Frequency size of the step. The default is `0.05`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**save_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the fields. The default is `True`. 

**save_rad_fields**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to save the radiating fields. The default is `False`. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to create a `"Discrete"`,``”Interpolating”`` or `"Fast"` sweep. The default is `"Discrete"`. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Sweep object if successful, `False` otherwise.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples
Create a setup named `"LinearStepSetup"` and use it in a linear step sweep named `"LinearStepSweep"`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup("LinearStepSetup")
>>> linear_step_sweep = setup.create_linear_step_sweep(
...     name="LinearStepSweep", unit="MHz", start_frequency=1.1e3, stop_frequency=1200.1, step_size=153.8
... )
>>> type(linear_step_sweep)
<class 'from ansys.aedt.core.modules.setup_templates.SweepHFSS'>

```
Copy to clipboard