---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# add_thermal_modifier_dataset 

MatProperty.add_thermal_modifier_dataset(_dataset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a thermal modifier to a material property using an existing dataset. 

Parameters: 
     

**dataset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the project dataset. 

**index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Value for the index. The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDefinitionManager.EditMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2021.2")
>>> mat1 = hfss.materials.add_material("new_copper2")
>>> mat1.add_thermal_modifier_dataset("$ds1")

```
Copy to clipboard
# add_thermal_modifier_dataset 

MatProperty.add_thermal_modifier_dataset(_dataset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a thermal modifier to a material property using an existing dataset. 

Parameters: 
     

**dataset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the project dataset. 

**index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Value for the index. The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDefinitionManager.EditMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2021.2")
>>> mat1 = hfss.materials.add_material("new_copper2")
>>> mat1.add_thermal_modifier_dataset("$ds1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_dataset.rst.txt)

# add_thermal_modifier_dataset 

MatProperty.add_thermal_modifier_dataset(_dataset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a thermal modifier to a material property using an existing dataset. 

Parameters: 
     

**dataset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the project dataset. 

**index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Value for the index. The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDefinitionManager.EditMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2021.2")
>>> mat1 = hfss.materials.add_material("new_copper2")
>>> mat1.add_thermal_modifier_dataset("$ds1")

```
Copy to clipboard