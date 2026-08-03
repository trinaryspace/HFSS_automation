---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# add_derivatives 

SetupHFSSAuto.add_derivatives(_derivative_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add derivatives to the setup. 

Parameters: 
     

**derivative_list**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `List` 
    
Derivative variable names. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1", setup_type="HFSSDrivenAuto")
>>> setup1.add_derivatives(derivative_list=["Box1"])

```
Copy to clipboard
# add_derivatives 

SetupHFSSAuto.add_derivatives(_derivative_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add derivatives to the setup. 

Parameters: 
     

**derivative_list**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `List` 
    
Derivative variable names. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1", setup_type="HFSSDrivenAuto")
>>> setup1.add_derivatives(derivative_list=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives.rst.txt)

# add_derivatives 

SetupHFSSAuto.add_derivatives(_derivative_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add derivatives to the setup. 

Parameters: 
     

**derivative_list**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `List` 
    
Derivative variable names. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1", setup_type="HFSSDrivenAuto")
>>> setup1.add_derivatives(derivative_list=["Box1"])

```
Copy to clipboard