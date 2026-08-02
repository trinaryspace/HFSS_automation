---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.set_license_type.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# set_license_type 

Hfss3dLayout.set_license_type(_license_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Pool'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the license type between `"Pack"` and `"Pool"`. 

Parameters: 
     

**license_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of license type, which can be either `"Pack"` or `"Pool"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True`.
Note
Because of an API limitation, the command returns `True` even when the key is wrong.
References

```
>>> oDesktop.SetRegistryString

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.set_license_type()

```
Copy to clipboard
# set_license_type 

Hfss3dLayout.set_license_type(_license_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Pool'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the license type between `"Pack"` and `"Pool"`. 

Parameters: 
     

**license_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of license type, which can be either `"Pack"` or `"Pool"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True`.
Note
Because of an API limitation, the command returns `True` even when the key is wrong.
References

```
>>> oDesktop.SetRegistryString

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.set_license_type()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.set_license_type.rst.txt)

# set_license_type 

Hfss3dLayout.set_license_type(_license_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Pool'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the license type between `"Pack"` and `"Pool"`. 

Parameters: 
     

**license_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of license type, which can be either `"Pack"` or `"Pool"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True`.
Note
Because of an API limitation, the command returns `True` even when the key is wrong.
References

```
>>> oDesktop.SetRegistryString

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.set_license_type()

```
Copy to clipboard