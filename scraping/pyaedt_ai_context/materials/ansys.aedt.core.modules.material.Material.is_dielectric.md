---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.is_dielectric.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# is_dielectric 

Material.is_dielectric(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100000_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if the material is dielectric. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Threshold to define if a material is dielectric. The default is `100000`. If the conductivity is equal to or less than the threshold, the material is considered dielectric. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the material is dielectric, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.is_dielectric(threshold=1.0)

```
Copy to clipboard
# is_dielectric 

Material.is_dielectric(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100000_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if the material is dielectric. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Threshold to define if a material is dielectric. The default is `100000`. If the conductivity is equal to or less than the threshold, the material is considered dielectric. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the material is dielectric, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.is_dielectric(threshold=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.Material.is_dielectric.rst.txt)

# is_dielectric 

Material.is_dielectric(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100000_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if the material is dielectric. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Threshold to define if a material is dielectric. The default is `100000`. If the conductivity is equal to or less than the threshold, the material is considered dielectric. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when the material is dielectric, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.is_dielectric(threshold=1.0)

```
Copy to clipboard