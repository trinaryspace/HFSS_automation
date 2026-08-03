---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# SurfaceMaterial 

class ansys.aedt.core.modules.material.SurfaceMaterial(_materiallib_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _material_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages surface material properties for Icepak only. 

Parameters: 
     

**materiallib**[`ansys.aedt.core.modules.material_lib.Materials`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.html#ansys.aedt.core.modules.material_lib.Materials "ansys.aedt.core.modules.material_lib.Materials") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material 

**props**
    
The default is `None`. 

**material_update**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`.
Examples

```
>>> from ansys.aedt.core.modules.material import SurfaceMaterial
>>> obj = SurfaceMaterial()

```
Copy to clipboard
Methods  
| [`SurfaceMaterial.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.update.html#ansys.aedt.core.modules.material.SurfaceMaterial.update "ansys.aedt.core.modules.material.SurfaceMaterial.update")()  | Update the surface material in AEDT.  |  
| --- | --- |  
Attributes  
| [`SurfaceMaterial.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system.html#ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system "ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system")  | Material coordinate system.  |  
| --- | --- |  
| [`SurfaceMaterial.emissivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.emissivity.html#ansys.aedt.core.modules.material.SurfaceMaterial.emissivity "ansys.aedt.core.modules.material.SurfaceMaterial.emissivity")  | Emissivity.  |  
| [`SurfaceMaterial.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.is_used.html#ansys.aedt.core.modules.material.SurfaceMaterial.is_used "ansys.aedt.core.modules.material.SurfaceMaterial.is_used")  | Checks if a project material is in use.  |  
| [`SurfaceMaterial.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.public_dir.html#ansys.aedt.core.modules.material.SurfaceMaterial.public_dir "ansys.aedt.core.modules.material.SurfaceMaterial.public_dir")  | Shortcut for dir(self).  |  
| [`SurfaceMaterial.surface_diffuse_absorptance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance "ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance")  | Surface diffuse absorptance.  |  
| [`SurfaceMaterial.surface_incident_absorptance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance "ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance")  | Surface incident absorptance.  |  
| [`SurfaceMaterial.surface_roughness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness "ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness")  | Surface roughness.  |  
# SurfaceMaterial 

class ansys.aedt.core.modules.material.SurfaceMaterial(_materiallib_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _material_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages surface material properties for Icepak only. 

Parameters: 
     

**materiallib**[`ansys.aedt.core.modules.material_lib.Materials`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.html#ansys.aedt.core.modules.material_lib.Materials "ansys.aedt.core.modules.material_lib.Materials") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material 

**props**
    
The default is `None`. 

**material_update**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`.
Examples

```
>>> from ansys.aedt.core.modules.material import SurfaceMaterial
>>> obj = SurfaceMaterial()

```
Copy to clipboard
Methods  
| [`SurfaceMaterial.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.update.html#ansys.aedt.core.modules.material.SurfaceMaterial.update "ansys.aedt.core.modules.material.SurfaceMaterial.update")()  | Update the surface material in AEDT.  |  
| --- | --- |  
Attributes  
| [`SurfaceMaterial.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system.html#ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system "ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system")  | Material coordinate system.  |  
| --- | --- |  
| [`SurfaceMaterial.emissivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.emissivity.html#ansys.aedt.core.modules.material.SurfaceMaterial.emissivity "ansys.aedt.core.modules.material.SurfaceMaterial.emissivity")  | Emissivity.  |  
| [`SurfaceMaterial.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.is_used.html#ansys.aedt.core.modules.material.SurfaceMaterial.is_used "ansys.aedt.core.modules.material.SurfaceMaterial.is_used")  | Checks if a project material is in use.  |  
| [`SurfaceMaterial.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.public_dir.html#ansys.aedt.core.modules.material.SurfaceMaterial.public_dir "ansys.aedt.core.modules.material.SurfaceMaterial.public_dir")  | Shortcut for dir(self).  |  
| [`SurfaceMaterial.surface_diffuse_absorptance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance "ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance")  | Surface diffuse absorptance.  |  
| [`SurfaceMaterial.surface_incident_absorptance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance "ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance")  | Surface incident absorptance.  |  
| [`SurfaceMaterial.surface_roughness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness "ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness")  | Surface roughness.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.rst.txt)

# SurfaceMaterial 

class ansys.aedt.core.modules.material.SurfaceMaterial(_materiallib_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _material_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages surface material properties for Icepak only. 

Parameters: 
     

**materiallib**[`ansys.aedt.core.modules.material_lib.Materials`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.html#ansys.aedt.core.modules.material_lib.Materials "ansys.aedt.core.modules.material_lib.Materials") 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the surface material 

**props**
    
The default is `None`. 

**material_update**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `True`.
Examples

```
>>> from ansys.aedt.core.modules.material import SurfaceMaterial
>>> obj = SurfaceMaterial()

```
Copy to clipboard
Methods  
| [`SurfaceMaterial.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.update.html#ansys.aedt.core.modules.material.SurfaceMaterial.update "ansys.aedt.core.modules.material.SurfaceMaterial.update")()  | Update the surface material in AEDT.  |  
| --- | --- |  
Attributes  
| [`SurfaceMaterial.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system.html#ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system "ansys.aedt.core.modules.material.SurfaceMaterial.coordinate_system")  | Material coordinate system.  |  
| --- | --- |  
| [`SurfaceMaterial.emissivity`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.emissivity.html#ansys.aedt.core.modules.material.SurfaceMaterial.emissivity "ansys.aedt.core.modules.material.SurfaceMaterial.emissivity")  | Emissivity.  |  
| [`SurfaceMaterial.is_used`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.is_used.html#ansys.aedt.core.modules.material.SurfaceMaterial.is_used "ansys.aedt.core.modules.material.SurfaceMaterial.is_used")  | Checks if a project material is in use.  |  
| [`SurfaceMaterial.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.public_dir.html#ansys.aedt.core.modules.material.SurfaceMaterial.public_dir "ansys.aedt.core.modules.material.SurfaceMaterial.public_dir")  | Shortcut for dir(self).  |  
| [`SurfaceMaterial.surface_diffuse_absorptance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance "ansys.aedt.core.modules.material.SurfaceMaterial.surface_diffuse_absorptance")  | Surface diffuse absorptance.  |  
| [`SurfaceMaterial.surface_incident_absorptance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance "ansys.aedt.core.modules.material.SurfaceMaterial.surface_incident_absorptance")  | Surface incident absorptance.  |  
| [`SurfaceMaterial.surface_roughness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness.html#ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness "ansys.aedt.core.modules.material.SurfaceMaterial.surface_roughness")  | Surface roughness.  |