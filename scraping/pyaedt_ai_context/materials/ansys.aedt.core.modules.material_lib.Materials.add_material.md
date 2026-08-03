---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# add_material 

Materials.add_material(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a material with default values.
When the added material object is returned, you can customize the material. This method does not update the material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**properties**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Material property dictionary. The default is `None`. 

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
>>> mat = hfss.materials.add_material("MyMaterial")
>>> print(mat.conductivity.value)

```
Copy to clipboard

```
>>> oDefinitionManager.GetProjectMaterialNames
>>> oMaterialManager.GetData

```
Copy to clipboard
# add_material 

Materials.add_material(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a material with default values.
When the added material object is returned, you can customize the material. This method does not update the material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**properties**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Material property dictionary. The default is `None`. 

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
>>> mat = hfss.materials.add_material("MyMaterial")
>>> print(mat.conductivity.value)

```
Copy to clipboard

```
>>> oDefinitionManager.GetProjectMaterialNames
>>> oMaterialManager.GetData

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_material.rst.txt)

# add_material 

Materials.add_material(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a material with default values.
When the added material object is returned, you can customize the material. This method does not update the material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. 

**properties**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Material property dictionary. The default is `None`. 

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
>>> mat = hfss.materials.add_material("MyMaterial")
>>> print(mat.conductivity.value)

```
Copy to clipboard

```
>>> oDefinitionManager.GetProjectMaterialNames
>>> oMaterialManager.GetData

```
Copy to clipboard