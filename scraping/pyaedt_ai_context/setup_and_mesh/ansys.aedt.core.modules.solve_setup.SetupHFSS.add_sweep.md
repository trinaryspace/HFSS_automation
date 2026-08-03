---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_sweep 

SetupHFSS.add_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Interpolating'_, _** props_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a sweep to the project. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. The default is `"Interpolating"`. 

****props**`Optional` context-dependent [`keyword`](https://docs.python.org/3.11/library/keyword.html#module-keyword "\(in Python v3.11\)") `arguments` `can` `be` `passed` 
    
to the sweep setup 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")
    
Sweep object.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup()
>>> setup.add_sweep()

```
Copy to clipboard
# add_sweep 

SetupHFSS.add_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Interpolating'_, _** props_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a sweep to the project. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. The default is `"Interpolating"`. 

****props**`Optional` context-dependent [`keyword`](https://docs.python.org/3.11/library/keyword.html#module-keyword "\(in Python v3.11\)") `arguments` `can` `be` `passed` 
    
to the sweep setup 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")
    
Sweep object.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup()
>>> setup.add_sweep()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep.rst.txt)

# add_sweep 

SetupHFSS.add_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Interpolating'_, _** props_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a sweep to the project. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case a name is automatically assigned. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. The default is `"Interpolating"`. 

****props**`Optional` context-dependent [`keyword`](https://docs.python.org/3.11/library/keyword.html#module-keyword "\(in Python v3.11\)") `arguments` `can` `be` `passed` 
    
to the sweep setup 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")
    
Sweep object.
References

```
>>> oModule.InsertFrequencySweep

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup()
>>> setup.add_sweep()

```
Copy to clipboard