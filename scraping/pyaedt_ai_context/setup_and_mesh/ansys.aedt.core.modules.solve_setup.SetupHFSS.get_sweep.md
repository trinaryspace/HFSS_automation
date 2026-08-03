---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# get_sweep 

SetupHFSS.get_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return frequency sweep object of a given sweep. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case the first sweep is used. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup()
>>> sweep = setup.add_sweep()
>>> sweep.add_subrange("LinearCount", 0, 10, 1, "Hz")
>>> sweep.add_subrange("LogScale", 10, 1e8, 100, "Hz")

```
Copy to clipboard
# get_sweep 

SetupHFSS.get_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return frequency sweep object of a given sweep. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case the first sweep is used. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup()
>>> sweep = setup.add_sweep()
>>> sweep.add_subrange("LinearCount", 0, 10, 1, "Hz")
>>> sweep.add_subrange("LogScale", 10, 1e8, 100, "Hz")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep.rst.txt)

# get_sweep 

SetupHFSS.get_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SweepHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Return frequency sweep object of a given sweep. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep. The default is `None`, in which case the first sweep is used. 

Returns: 
     

[`ansys.aedt.core.modules.solve_sweeps.SweepHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.html#ansys.aedt.core.modules.solve_sweeps.SweepHFSS "ansys.aedt.core.modules.solve_sweeps.SweepHFSS")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup()
>>> sweep = setup.add_sweep()
>>> sweep.add_subrange("LinearCount", 0, 10, 1, "Hz")
>>> sweep.add_subrange("LogScale", 10, 1e8, 100, "Hz")

```
Copy to clipboard