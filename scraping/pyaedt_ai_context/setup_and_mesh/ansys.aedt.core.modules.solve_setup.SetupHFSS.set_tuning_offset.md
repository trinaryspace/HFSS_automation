---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# set_tuning_offset 

SetupHFSS.set_tuning_offset(_offsets : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set derivative variable to a specific offset value.
This method adjusts the tuning ranges for derivative variables in the design, allowing for specific offset values to be applied. If a variable is not specified in the `offsets` dictionary, its offset is set to `0` by default. Each value must be within ±10% of the nominal value of the corresponding variable. 

Parameters: 
     

**offsets**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are variable names and values are the corresponding offset values to be applied. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetTuningRanges

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["der_var"] = "1mm"
>>> setup = hfss.create_setup(setup_type=1)
>>> setup.add_derivatives("der_var")
>>> hfss.analyze()
>>> setup.set_tuning_offset({"der_var": 0.05})

```
Copy to clipboard
# set_tuning_offset 

SetupHFSS.set_tuning_offset(_offsets : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set derivative variable to a specific offset value.
This method adjusts the tuning ranges for derivative variables in the design, allowing for specific offset values to be applied. If a variable is not specified in the `offsets` dictionary, its offset is set to `0` by default. Each value must be within ±10% of the nominal value of the corresponding variable. 

Parameters: 
     

**offsets**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are variable names and values are the corresponding offset values to be applied. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetTuningRanges

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["der_var"] = "1mm"
>>> setup = hfss.create_setup(setup_type=1)
>>> setup.add_derivatives("der_var")
>>> hfss.analyze()
>>> setup.set_tuning_offset({"der_var": 0.05})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset.rst.txt)

# set_tuning_offset 

SetupHFSS.set_tuning_offset(_offsets : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set derivative variable to a specific offset value.
This method adjusts the tuning ranges for derivative variables in the design, allowing for specific offset values to be applied. If a variable is not specified in the `offsets` dictionary, its offset is set to `0` by default. Each value must be within ±10% of the nominal value of the corresponding variable. 

Parameters: 
     

**offsets**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are variable names and values are the corresponding offset values to be applied. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetTuningRanges

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["der_var"] = "1mm"
>>> setup = hfss.create_setup(setup_type=1)
>>> setup.add_derivatives("der_var")
>>> hfss.analyze()
>>> setup.set_tuning_offset({"der_var": 0.05})

```
Copy to clipboard