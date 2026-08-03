---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# add_thermal_modifier_closed_form 

MatProperty.add_thermal_modifier_closed_form(_tref : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _c1 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0001_, _c2 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_, _tl =-273.15_, _tu : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'cel'_, _auto_calc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tml : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _tmu : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a thermal modifier to a material property using a closed-form formula. 

Parameters: 
     

**tref**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Reference temperature. The default is `22`. 

**c1**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
First coefficient value. The default is `0.0001`. 

**c2**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Second coefficient value. The default is `1e-6`. 

**tl**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Lower temperature limit. The default is `273.15`. 

**tu**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper temperature limit. The default is `1000`. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the reference temperature. The default is `"cel"`. 

**auto_calc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to calculate the lower and upper temperature limits automatically. The default is `True`. 

**tml**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Lower temperature limit when `auto_calc=True.` The default is `1000`. 

**tmu**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper temperature limit when `auto_calc=True.` The default is `1000`. 

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
>>> mat1.permittivity.add_thermal_modifier_closed_form(c1=1e-3)

```
Copy to clipboard
# add_thermal_modifier_closed_form 

MatProperty.add_thermal_modifier_closed_form(_tref : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _c1 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0001_, _c2 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_, _tl =-273.15_, _tu : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'cel'_, _auto_calc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tml : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _tmu : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a thermal modifier to a material property using a closed-form formula. 

Parameters: 
     

**tref**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Reference temperature. The default is `22`. 

**c1**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
First coefficient value. The default is `0.0001`. 

**c2**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Second coefficient value. The default is `1e-6`. 

**tl**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Lower temperature limit. The default is `273.15`. 

**tu**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper temperature limit. The default is `1000`. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the reference temperature. The default is `"cel"`. 

**auto_calc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to calculate the lower and upper temperature limits automatically. The default is `True`. 

**tml**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Lower temperature limit when `auto_calc=True.` The default is `1000`. 

**tmu**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper temperature limit when `auto_calc=True.` The default is `1000`. 

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
>>> mat1.permittivity.add_thermal_modifier_closed_form(c1=1e-3)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.MatProperty.add_thermal_modifier_closed_form.rst.txt)

# add_thermal_modifier_closed_form 

MatProperty.add_thermal_modifier_closed_form(_tref : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _c1 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0001_, _c2 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_, _tl =-273.15_, _tu : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'cel'_, _auto_calc : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tml : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _tmu : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a thermal modifier to a material property using a closed-form formula. 

Parameters: 
     

**tref**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Reference temperature. The default is `22`. 

**c1**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
First coefficient value. The default is `0.0001`. 

**c2**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Second coefficient value. The default is `1e-6`. 

**tl**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Lower temperature limit. The default is `273.15`. 

**tu**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper temperature limit. The default is `1000`. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the reference temperature. The default is `"cel"`. 

**auto_calc**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to calculate the lower and upper temperature limits automatically. The default is `True`. 

**tml**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Lower temperature limit when `auto_calc=True.` The default is `1000`. 

**tmu**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper temperature limit when `auto_calc=True.` The default is `1000`. 

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
>>> mat1.permittivity.add_thermal_modifier_closed_form(c1=1e-3)

```
Copy to clipboard