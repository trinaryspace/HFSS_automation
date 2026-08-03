---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# SweepHFSS 

class ansys.aedt.core.modules.solve_sweeps.SweepHFSS(_setup_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Interpolating'_, _props =None_) 
    
Initializes, creates, and updates sweeps in HFSS. 

Parameters: 
     

**setup** :class ‘from ansys.aedt.core.modules.solve_setup.Setup’ 
    
Setup to use for the analysis. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. Options are `"Fast"`, `"Interpolating"`, and `"Discrete"`. The default is `"Interpolating"`. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the properties. The default is `None`, in which case the default properties are retrieved.
Examples

```
>>> hfss = Hfss(
...     version=version,
...     project=proj,
...     design=gtemDesign,
...     solution_type=solutiontype,
...     name=name,
...     new_desktop=False,
...     close_on_exit=False,
... )
>>> hfss_setup = hfss.setups[0]
>>> hfss_sweep = SweepHFSS(hfss_setup, "Sweep", sweep_type="Interpolating", props=None)

```
Copy to clipboard
Methods  
| [`SweepHFSS.add_subrange`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange")(range_type, start[, ...])  | Add a range to the sweep.  |  
| --- | --- |  
| [`SweepHFSS.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create")()  | Create a sweep.  |  
| [`SweepHFSS.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update")()  | Update a sweep.  |  
Attributes  
| [`SweepHFSS.basis_frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies")  | List of all frequencies that have fields available.  |  
| --- | --- |  
| [`SweepHFSS.frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies")  | List of all frequencies of the active sweep.  |  
| [`SweepHFSS.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved")  | Verify if solutions are available for the sweep.  |  
| [`SweepHFSS.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir")  | Shortcut for dir(self).  |  
# SweepHFSS 

class ansys.aedt.core.modules.solve_sweeps.SweepHFSS(_setup_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Interpolating'_, _props =None_) 
    
Initializes, creates, and updates sweeps in HFSS. 

Parameters: 
     

**setup** :class ‘from ansys.aedt.core.modules.solve_setup.Setup’ 
    
Setup to use for the analysis. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. Options are `"Fast"`, `"Interpolating"`, and `"Discrete"`. The default is `"Interpolating"`. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the properties. The default is `None`, in which case the default properties are retrieved.
Examples

```
>>> hfss = Hfss(
...     version=version,
...     project=proj,
...     design=gtemDesign,
...     solution_type=solutiontype,
...     name=name,
...     new_desktop=False,
...     close_on_exit=False,
... )
>>> hfss_setup = hfss.setups[0]
>>> hfss_sweep = SweepHFSS(hfss_setup, "Sweep", sweep_type="Interpolating", props=None)

```
Copy to clipboard
Methods  
| [`SweepHFSS.add_subrange`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange")(range_type, start[, ...])  | Add a range to the sweep.  |  
| --- | --- |  
| [`SweepHFSS.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create")()  | Create a sweep.  |  
| [`SweepHFSS.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update")()  | Update a sweep.  |  
Attributes  
| [`SweepHFSS.basis_frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies")  | List of all frequencies that have fields available.  |  
| --- | --- |  
| [`SweepHFSS.frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies")  | List of all frequencies of the active sweep.  |  
| [`SweepHFSS.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved")  | Verify if solutions are available for the sweep.  |  
| [`SweepHFSS.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.rst.txt)

# SweepHFSS 

class ansys.aedt.core.modules.solve_sweeps.SweepHFSS(_setup_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _sweep_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Interpolating'_, _props =None_) 
    
Initializes, creates, and updates sweeps in HFSS. 

Parameters: 
     

**setup** :class ‘from ansys.aedt.core.modules.solve_setup.Setup’ 
    
Setup to use for the analysis. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep. 

**sweep_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the sweep. Options are `"Fast"`, `"Interpolating"`, and `"Discrete"`. The default is `"Interpolating"`. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of the properties. The default is `None`, in which case the default properties are retrieved.
Examples

```
>>> hfss = Hfss(
...     version=version,
...     project=proj,
...     design=gtemDesign,
...     solution_type=solutiontype,
...     name=name,
...     new_desktop=False,
...     close_on_exit=False,
... )
>>> hfss_setup = hfss.setups[0]
>>> hfss_sweep = SweepHFSS(hfss_setup, "Sweep", sweep_type="Interpolating", props=None)

```
Copy to clipboard
Methods  
| [`SweepHFSS.add_subrange`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.add_subrange")(range_type, start[, ...])  | Add a range to the sweep.  |  
| --- | --- |  
| [`SweepHFSS.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.create")()  | Create a sweep.  |  
| [`SweepHFSS.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.update")()  | Update a sweep.  |  
Attributes  
| [`SweepHFSS.basis_frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.basis_frequencies")  | List of all frequencies that have fields available.  |  
| --- | --- |  
| [`SweepHFSS.frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.frequencies")  | List of all frequencies of the active sweep.  |  
| [`SweepHFSS.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.is_solved")  | Verify if solutions are available for the sweep.  |  
| [`SweepHFSS.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir "ansys.aedt.core.modules.solve_sweeps.SweepHFSS.public_dir")  | Shortcut for dir(self).  |