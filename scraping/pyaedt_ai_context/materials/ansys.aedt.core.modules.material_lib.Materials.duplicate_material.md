---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_material.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# duplicate_material 

Materials.duplicate_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _properties : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate a material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name for the copy of the material. If a new name is not specified, the new material name is `material_name` plusa “_clone”`` suffix. 

**properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of properties to parameterize when the material is duplicated. Parameterized properties have project scope. Options are:
  * ‘permittivity’
  * ‘permeability’
  * ‘conductivity’
  * ‘dielectric_loss_tan’
  * ‘magnetic_loss_tan’

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
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
>>> hfss.materials.duplicate_material("MyMaterial", "MyMaterial2")

```
Copy to clipboard
# duplicate_material 

Materials.duplicate_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _properties : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate a material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name for the copy of the material. If a new name is not specified, the new material name is `material_name` plusa “_clone”`` suffix. 

**properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of properties to parameterize when the material is duplicated. Parameterized properties have project scope. Options are:
  * ‘permittivity’
  * ‘permeability’
  * ‘conductivity’
  * ‘dielectric_loss_tan’
  * ‘magnetic_loss_tan’

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
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
>>> hfss.materials.duplicate_material("MyMaterial", "MyMaterial2")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_material.rst.txt)

# duplicate_material 

Materials.duplicate_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _properties : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate a material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name for the copy of the material. If a new name is not specified, the new material name is `material_name` plusa “_clone”`` suffix. 

**properties**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of properties to parameterize when the material is duplicated. Parameterized properties have project scope. Options are:
  * ‘permittivity’
  * ‘permeability’
  * ‘conductivity’
  * ‘dielectric_loss_tan’
  * ‘magnetic_loss_tan’

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
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
>>> hfss.materials.duplicate_material("MyMaterial", "MyMaterial2")

```
Copy to clipboard