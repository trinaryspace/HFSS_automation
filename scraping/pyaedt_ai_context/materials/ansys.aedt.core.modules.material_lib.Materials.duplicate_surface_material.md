---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# duplicate_surface_material 

Materials.duplicate_surface_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SurfaceMaterial](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.html#ansys.aedt.core.modules.material.SurfaceMaterial "ansys.aedt.core.modules.material.SurfaceMaterial") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate a surface material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name for the copy of the surface material. 

Returns: 
     

`ansys.aedt.core.modules.SurfaceMaterial`
    
References

```
>>> oDefinitionManager.AddSurfaceMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.materials.add_surface_material("MyMaterial")
>>> hfss.materials.duplicate_surface_material("MyMaterial", "MyMaterial2")

```
Copy to clipboard
# duplicate_surface_material 

Materials.duplicate_surface_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SurfaceMaterial](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.html#ansys.aedt.core.modules.material.SurfaceMaterial "ansys.aedt.core.modules.material.SurfaceMaterial") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate a surface material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name for the copy of the surface material. 

Returns: 
     

`ansys.aedt.core.modules.SurfaceMaterial`
    
References

```
>>> oDefinitionManager.AddSurfaceMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.materials.add_surface_material("MyMaterial")
>>> hfss.materials.duplicate_surface_material("MyMaterial", "MyMaterial2")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.duplicate_surface_material.rst.txt)

# duplicate_surface_material 

Materials.duplicate_surface_material(_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SurfaceMaterial](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.html#ansys.aedt.core.modules.material.SurfaceMaterial "ansys.aedt.core.modules.material.SurfaceMaterial") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate a surface material. 

Parameters: 
     

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name for the copy of the surface material. 

Returns: 
     

`ansys.aedt.core.modules.SurfaceMaterial`
    
References

```
>>> oDefinitionManager.AddSurfaceMaterial

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.materials.add_surface_material("MyMaterial")
>>> hfss.materials.duplicate_surface_material("MyMaterial", "MyMaterial2")

```
Copy to clipboard