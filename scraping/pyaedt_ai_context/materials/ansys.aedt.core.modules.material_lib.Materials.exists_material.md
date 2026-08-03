---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.exists_material.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# exists_material 

Materials.exists_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a material exists in AEDT or PyAEDT Definitions. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. If the material exists and is not in the materials database, it is added to this database. 

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
Material object if present, `False` when failed.
References

```
>>> oDefinitionManager.GetProjectMaterialNames
>>> oMaterialManager.GetData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.material_lib import Materials
>>> obj = Materials()
>>> obj.exists_material(material="copper")

```
Copy to clipboard
# exists_material 

Materials.exists_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a material exists in AEDT or PyAEDT Definitions. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. If the material exists and is not in the materials database, it is added to this database. 

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
Material object if present, `False` when failed.
References

```
>>> oDefinitionManager.GetProjectMaterialNames
>>> oMaterialManager.GetData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.material_lib import Materials
>>> obj = Materials()
>>> obj.exists_material(material="copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.exists_material.rst.txt)

# exists_material 

Materials.exists_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check if a material exists in AEDT or PyAEDT Definitions. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the material. If the material exists and is not in the materials database, it is added to this database. 

Returns: 
     

[`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")
    
Material object if present, `False` when failed.
References

```
>>> oDefinitionManager.GetProjectMaterialNames
>>> oMaterialManager.GetData

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.material_lib import Materials
>>> obj = Materials()
>>> obj.exists_material(material="copper")

```
Copy to clipboard