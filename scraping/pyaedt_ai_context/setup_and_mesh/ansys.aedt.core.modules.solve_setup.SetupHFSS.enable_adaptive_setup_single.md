---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# enable_adaptive_setup_single 

SetupHFSS.enable_adaptive_setup_single(_freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS single frequency setup. 

Parameters: 
     

**freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency at which to set the adaptive convergence. The default is `None` which will not update the value in setup. You can enter a float value in (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `None` which will not update the value in setup. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S convergence criteria. The default is `None` which will not update the value in setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.enable_adaptive_setup_single(freq="1GHz", max_passes=2)

```
Copy to clipboard
# enable_adaptive_setup_single 

SetupHFSS.enable_adaptive_setup_single(_freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS single frequency setup. 

Parameters: 
     

**freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency at which to set the adaptive convergence. The default is `None` which will not update the value in setup. You can enter a float value in (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `None` which will not update the value in setup. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S convergence criteria. The default is `None` which will not update the value in setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.enable_adaptive_setup_single(freq="1GHz", max_passes=2)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single.rst.txt)

# enable_adaptive_setup_single 

SetupHFSS.enable_adaptive_setup_single(_freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS single frequency setup. 

Parameters: 
     

**freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency at which to set the adaptive convergence. The default is `None` which will not update the value in setup. You can enter a float value in (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `None` which will not update the value in setup. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S convergence criteria. The default is `None` which will not update the value in setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1")
>>> setup1.enable_adaptive_setup_single(freq="1GHz", max_passes=2)

```
Copy to clipboard