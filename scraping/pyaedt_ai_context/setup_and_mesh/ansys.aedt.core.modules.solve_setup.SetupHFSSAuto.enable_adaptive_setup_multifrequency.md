---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# enable_adaptive_setup_multifrequency 

SetupHFSSAuto.enable_adaptive_setup_multifrequency(_frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS multi-frequency setup. 

Parameters: 
     

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency at which to set the adaptive convergence. You can enter list entries as float values in GHz or as strings. 

**max_delta_s**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Delta S convergence criteria. The default is `0.02`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_multifrequency(frequencies=["Box1"]

```
Copy to clipboard
# enable_adaptive_setup_multifrequency 

SetupHFSSAuto.enable_adaptive_setup_multifrequency(_frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS multi-frequency setup. 

Parameters: 
     

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency at which to set the adaptive convergence. You can enter list entries as float values in GHz or as strings. 

**max_delta_s**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Delta S convergence criteria. The default is `0.02`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_multifrequency(frequencies=["Box1"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency.rst.txt)

# enable_adaptive_setup_multifrequency 

SetupHFSSAuto.enable_adaptive_setup_multifrequency(_frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _max_delta_s : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable HFSS multi-frequency setup. 

Parameters: 
     

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency at which to set the adaptive convergence. You can enter list entries as float values in GHz or as strings. 

**max_delta_s**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Delta S convergence criteria. The default is `0.02`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> setup = hfss.create_setup(setup_type=0)
>>> setup.enable_adaptive_setup_multifrequency(frequencies=["Box1"]

```
Copy to clipboard