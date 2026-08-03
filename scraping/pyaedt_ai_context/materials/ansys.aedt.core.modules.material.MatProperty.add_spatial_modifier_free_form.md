---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# add_spatial_modifier_free_form 

MatProperty.add_spatial_modifier_free_form(_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a spatial modifier to a material property using a free-form formula. 

Parameters: 
     

**formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full formula to apply. 

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
>>> mat1.add_spatial_modifier_free_form("if(X > 1mm, 1, if(X < 1mm, 2, 1))")

```
Copy to clipboard
# add_spatial_modifier_free_form 

MatProperty.add_spatial_modifier_free_form(_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a spatial modifier to a material property using a free-form formula. 

Parameters: 
     

**formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full formula to apply. 

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
>>> mat1.add_spatial_modifier_free_form("if(X > 1mm, 1, if(X < 1mm, 2, 1))")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_spatial_modifier_free_form.rst.txt)

# add_spatial_modifier_free_form 

MatProperty.add_spatial_modifier_free_form(_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a spatial modifier to a material property using a free-form formula. 

Parameters: 
     

**formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full formula to apply. 

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
>>> mat1.add_spatial_modifier_free_form("if(X > 1mm, 1, if(X < 1mm, 2, 1))")

```
Copy to clipboard