---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# set_bp_curve_coreloss 

Material.set_bp_curve_coreloss(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0001_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'kw/m^3'_, _bunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'tesla'_, _frequency : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 60_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set B-P Type Core Loss. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of [x,y] points. 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**cut_depth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Core loss unit. The default is `"kw/m^3"`. 

**bunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Magnetic field unit. The default is `"tesla"`. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lamination thickness. The default is `"0.5mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_bp_curve_coreloss(points=[0, 0, 0])

```
Copy to clipboard
# set_bp_curve_coreloss 

Material.set_bp_curve_coreloss(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0001_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'kw/m^3'_, _bunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'tesla'_, _frequency : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 60_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set B-P Type Core Loss. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of [x,y] points. 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**cut_depth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Core loss unit. The default is `"kw/m^3"`. 

**bunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Magnetic field unit. The default is `"tesla"`. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lamination thickness. The default is `"0.5mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_bp_curve_coreloss(points=[0, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.Material.set_bp_curve_coreloss.rst.txt)

# set_bp_curve_coreloss 

Material.set_bp_curve_coreloss(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0001_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'kw/m^3'_, _bunit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'tesla'_, _frequency : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 60_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set B-P Type Core Loss. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of [x,y] points. 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**cut_depth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Core loss unit. The default is `"kw/m^3"`. 

**bunit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Magnetic field unit. The default is `"tesla"`. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
     

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lamination thickness. The default is `"0.5mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_bp_curve_coreloss(points=[0, 0, 0])

```
Copy to clipboard