---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.delete_setup.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# delete_setup 

Hfss3dLayout.delete_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.Delete

```
Copy to clipboard
Examples
Create a setup and then delete it.

```
>>> import ansys.aedt.core
>>> hfss3dlayout = ansys.aedt.core.Hfss3dLayout()
>>> setup1 = hfss3dlayout.create_setup(name="Setup1")
>>> hfss3dlayout.delete_setup()
PyAEDT INFO: Sweep was deleted correctly.

```
Copy to clipboard
# delete_setup 

Hfss3dLayout.delete_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.Delete

```
Copy to clipboard
Examples
Create a setup and then delete it.

```
>>> import ansys.aedt.core
>>> hfss3dlayout = ansys.aedt.core.Hfss3dLayout()
>>> setup1 = hfss3dlayout.create_setup(name="Setup1")
>>> hfss3dlayout.delete_setup()
PyAEDT INFO: Sweep was deleted correctly.

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.delete_setup.rst.txt)

# delete_setup 

Hfss3dLayout.delete_setup(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a setup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.Delete

```
Copy to clipboard
Examples
Create a setup and then delete it.

```
>>> import ansys.aedt.core
>>> hfss3dlayout = ansys.aedt.core.Hfss3dLayout()
>>> setup1 = hfss3dlayout.create_setup(name="Setup1")
>>> hfss3dlayout.delete_setup()
PyAEDT INFO: Sweep was deleted correctly.

```
Copy to clipboard