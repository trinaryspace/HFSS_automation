---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# get_sweep_names 

SetupHFSS.get_sweep_names() → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the names of all sweeps in a given analysis setup. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of names of all sweeps for the setup.
References

```
>>> oModules.GetSweeps

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type="HFSSDriven")
>>> sweeps = setup.get_sweep_names()

```
Copy to clipboard
# get_sweep_names 

SetupHFSS.get_sweep_names() → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the names of all sweeps in a given analysis setup. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of names of all sweeps for the setup.
References

```
>>> oModules.GetSweeps

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type="HFSSDriven")
>>> sweeps = setup.get_sweep_names()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names.rst.txt)

# get_sweep_names 

SetupHFSS.get_sweep_names() → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the names of all sweeps in a given analysis setup. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of names of all sweeps for the setup.
References

```
>>> oModules.GetSweeps

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type="HFSSDriven")
>>> sweeps = setup.get_sweep_names()

```
Copy to clipboard