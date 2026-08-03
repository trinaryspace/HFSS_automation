---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# delete_sweep 

SetupHFSS.delete_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a sweep. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.DeleteSweep

```
Copy to clipboard
Examples
Create a frequency sweep and then delete it.

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.create_frequency_sweep("GHz", 24, 24.25, 26, "Sweep1", sweep_type="Fast")
>>> setup1.delete_sweep("Sweep1")

```
Copy to clipboard
# delete_sweep 

SetupHFSS.delete_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a sweep. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.DeleteSweep

```
Copy to clipboard
Examples
Create a frequency sweep and then delete it.

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.create_frequency_sweep("GHz", 24, 24.25, 26, "Sweep1", sweep_type="Fast")
>>> setup1.delete_sweep("Sweep1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep.rst.txt)

# delete_sweep 

SetupHFSS.delete_sweep(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a sweep. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.DeleteSweep

```
Copy to clipboard
Examples
Create a frequency sweep and then delete it.

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.create_frequency_sweep("GHz", 24, 24.25, 26, "Sweep1", sweep_type="Fast")
>>> setup1.delete_sweep("Sweep1")

```
Copy to clipboard