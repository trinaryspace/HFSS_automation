---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material_sweep.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# add_material_sweep 

Materials.add_material_sweep(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create a sweep material made of an array of materials. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of materials to merge into a single sweep material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep material. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Index of the project variable.
References

```
>>> oDefinitionManager.AddMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.materials.add_material("MyMaterial")
>>> hfss.materials.add_material("MyMaterial2")
>>> hfss.materials.add_material_sweep(["MyMaterial", "MyMaterial2"], "Sweep_copper")

```
Copy to clipboard
# add_material_sweep 

Materials.add_material_sweep(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create a sweep material made of an array of materials. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of materials to merge into a single sweep material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep material. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Index of the project variable.
References

```
>>> oDefinitionManager.AddMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.materials.add_material("MyMaterial")
>>> hfss.materials.add_material("MyMaterial2")
>>> hfss.materials.add_material_sweep(["MyMaterial", "MyMaterial2"], "Sweep_copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material_sweep.rst.txt)

# add_material_sweep 

Materials.add_material_sweep(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Create a sweep material made of an array of materials. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of materials to merge into a single sweep material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sweep material. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Index of the project variable.
References

```
>>> oDefinitionManager.AddMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.materials.add_material("MyMaterial")
>>> hfss.materials.add_material("MyMaterial2")
>>> hfss.materials.add_material_sweep(["MyMaterial", "MyMaterial2"], "Sweep_copper")

```
Copy to clipboard