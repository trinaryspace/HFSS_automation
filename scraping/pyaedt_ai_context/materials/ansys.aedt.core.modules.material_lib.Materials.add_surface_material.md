---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_surface_material.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# add_surface_material 

Materials.add_surface_material(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _emissivity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [SurfaceMaterial](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.html#ansys.aedt.core.modules.material.SurfaceMaterial "ansys.aedt.core.modules.material.SurfaceMaterial") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a surface material.
In AEDT, base properties are loaded from the XML database file `amat.xml` or from the emissivity. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material. 

**emissivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Emissivity value. 

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
>>> mat = hfss.materials.add_surface_material("Steel", 0.85)
>>> print(mat.emissivity.value)

```
Copy to clipboard
# add_surface_material 

Materials.add_surface_material(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _emissivity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [SurfaceMaterial](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.html#ansys.aedt.core.modules.material.SurfaceMaterial "ansys.aedt.core.modules.material.SurfaceMaterial") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a surface material.
In AEDT, base properties are loaded from the XML database file `amat.xml` or from the emissivity. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material. 

**emissivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Emissivity value. 

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
>>> mat = hfss.materials.add_surface_material("Steel", 0.85)
>>> print(mat.emissivity.value)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.add_surface_material.rst.txt)

# add_surface_material 

Materials.add_surface_material(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _emissivity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [SurfaceMaterial](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.html#ansys.aedt.core.modules.material.SurfaceMaterial "ansys.aedt.core.modules.material.SurfaceMaterial") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a surface material.
In AEDT, base properties are loaded from the XML database file `amat.xml` or from the emissivity. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material. 

**emissivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Emissivity value. 

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
>>> mat = hfss.materials.add_surface_material("Steel", 0.85)
>>> print(mat.emissivity.value)

```
Copy to clipboard