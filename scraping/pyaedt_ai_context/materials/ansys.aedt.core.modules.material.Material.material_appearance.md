---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.material_appearance.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# material_appearance 

property Material.material_appearance: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] 
    
Material appearance specified as a list.
The first three items are RGB color and the fourth one is transparency. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Color of the material in RGB and transparency. Color values are in the range `[0, 255]`. Transparency is a float in the range `[0,1]`.
Examples
Create a material with color `[0, 153, 153]` (darker cyan) and transparency `0.5`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2021.2")
>>> mat1 = hfss.materials.add_material("new_material")
>>> appearance_props = mat1.material_appearance
>>> mat1.material_appearance = [0, 153, 153, 0.5]

```
Copy to clipboard
# material_appearance 

property Material.material_appearance: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] 
    
Material appearance specified as a list.
The first three items are RGB color and the fourth one is transparency. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Color of the material in RGB and transparency. Color values are in the range `[0, 255]`. Transparency is a float in the range `[0,1]`.
Examples
Create a material with color `[0, 153, 153]` (darker cyan) and transparency `0.5`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2021.2")
>>> mat1 = hfss.materials.add_material("new_material")
>>> appearance_props = mat1.material_appearance
>>> mat1.material_appearance = [0, 153, 153, 0.5]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.Material.material_appearance.rst.txt)

# material_appearance 

property Material.material_appearance: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] 
    
Material appearance specified as a list.
The first three items are RGB color and the fourth one is transparency. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Color of the material in RGB and transparency. Color values are in the range `[0, 255]`. Transparency is a float in the range `[0,1]`.
Examples
Create a material with color `[0, 153, 153]` (darker cyan) and transparency `0.5`.

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(version="2021.2")
>>> mat1 = hfss.materials.add_material("new_material")
>>> appearance_props = mat1.material_appearance
>>> mat1.material_appearance = [0, 153, 153, 0.5]

```
Copy to clipboard