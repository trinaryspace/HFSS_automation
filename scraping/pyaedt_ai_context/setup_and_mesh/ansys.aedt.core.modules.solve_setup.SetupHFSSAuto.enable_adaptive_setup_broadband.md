---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# enable_adaptive_setup_broadband 

SetupHFSSAuto.enable_adaptive_setup_broadband(_low_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _high_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS broadband setup. 

Parameters: 
     

**low_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Lower frequency to set the adaptive convergence at. You can specify a float value (GHz) or a string. 

**high_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Lower frequency to set the adaptive convergence at. You can specify a float value (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `6`. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S Convergence criteria. The default is `0.02`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_broadband(low_frequency="1GHz", high_frequency="1GHz")

```
Copy to clipboard
# enable_adaptive_setup_broadband 

SetupHFSSAuto.enable_adaptive_setup_broadband(_low_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _high_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS broadband setup. 

Parameters: 
     

**low_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Lower frequency to set the adaptive convergence at. You can specify a float value (GHz) or a string. 

**high_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Lower frequency to set the adaptive convergence at. You can specify a float value (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `6`. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S Convergence criteria. The default is `0.02`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_broadband(low_frequency="1GHz", high_frequency="1GHz")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband.rst.txt)

# enable_adaptive_setup_broadband 

SetupHFSSAuto.enable_adaptive_setup_broadband(_low_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _high_frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _max_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS broadband setup. 

Parameters: 
     

**low_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Lower frequency to set the adaptive convergence at. You can specify a float value (GHz) or a string. 

**high_frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Lower frequency to set the adaptive convergence at. You can specify a float value (GHz) or a string. 

**max_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of adaptive passes. The default is `6`. 

**max_delta_s**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Delta S Convergence criteria. The default is `0.02`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_broadband(low_frequency="1GHz", high_frequency="1GHz")

```
Copy to clipboard