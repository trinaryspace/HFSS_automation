---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# set_electrical_steel_coreloss 

Material.set_electrical_steel_coreloss(_kh : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _kc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _ke : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set electrical steel core loss. 

Parameters: 
     

**kh**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Hysteresis core loss coefficient. The default is `0`. 

**kc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Eddy-current core loss coefficient. The default is `0`. 

**ke**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excess core loss coefficient. The default is `0`. 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Coefficient considering the DC flux bias effects. The default is `0`. 

**cut_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Equivalent cut depth considering manufacturing effects on core loss computation. The default value is `"1mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_electrical_steel_coreloss(kh=1, kc=1)

```
Copy to clipboard
# set_electrical_steel_coreloss 

Material.set_electrical_steel_coreloss(_kh : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _kc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _ke : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set electrical steel core loss. 

Parameters: 
     

**kh**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Hysteresis core loss coefficient. The default is `0`. 

**kc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Eddy-current core loss coefficient. The default is `0`. 

**ke**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excess core loss coefficient. The default is `0`. 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Coefficient considering the DC flux bias effects. The default is `0`. 

**cut_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Equivalent cut depth considering manufacturing effects on core loss computation. The default value is `"1mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_electrical_steel_coreloss(kh=1, kc=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.Material.set_electrical_steel_coreloss.rst.txt)

# set_electrical_steel_coreloss 

Material.set_electrical_steel_coreloss(_kh : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _kc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _ke : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set electrical steel core loss. 

Parameters: 
     

**kh**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Hysteresis core loss coefficient. The default is `0`. 

**kc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Eddy-current core loss coefficient. The default is `0`. 

**ke**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excess core loss coefficient. The default is `0`. 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Coefficient considering the DC flux bias effects. The default is `0`. 

**cut_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Equivalent cut depth considering manufacturing effects on core loss computation. The default value is `"1mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_electrical_steel_coreloss(kh=1, kc=1)

```
Copy to clipboard