---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# enable_adaptive_setup_single 

SetupHFSSAuto.enable_adaptive_setup_single(_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS single frequency setup. 

Parameters: 
     

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency to set the adaptive convergence at. The default is `None`, in which case the value in the setup is not updated. You can specify a float value (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `None` which will not update the value in setup. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S convergence criteria. The default is `None` which will not update the value in setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_single(frequency="1GHz", max_passes=2)

```
Copy to clipboard
# enable_adaptive_setup_single 

SetupHFSSAuto.enable_adaptive_setup_single(_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS single frequency setup. 

Parameters: 
     

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency to set the adaptive convergence at. The default is `None`, in which case the value in the setup is not updated. You can specify a float value (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `None` which will not update the value in setup. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S convergence criteria. The default is `None` which will not update the value in setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_single(frequency="1GHz", max_passes=2)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single.rst.txt)

# enable_adaptive_setup_single 

SetupHFSSAuto.enable_adaptive_setup_single(_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS single frequency setup. 

Parameters: 
     

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Frequency to set the adaptive convergence at. The default is `None`, in which case the value in the setup is not updated. You can specify a float value (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `None` which will not update the value in setup. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S convergence criteria. The default is `None` which will not update the value in setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_single(frequency="1GHz", max_passes=2)

```
Copy to clipboard