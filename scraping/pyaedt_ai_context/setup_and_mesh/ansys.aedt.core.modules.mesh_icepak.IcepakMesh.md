---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# IcepakMesh 

class ansys.aedt.core.modules.mesh_icepak.IcepakMesh(_app_) 
    
Manages Icepak meshes. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()

```
Copy to clipboard
Methods  
| [`IcepakMesh.assign_mesh_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file")(assignment, ...)  | Assign a mesh from a file to objects.  |  
| --- | --- |  
| [`IcepakMesh.assign_mesh_level`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level")(mesh_order[, name])  | Assign a mesh level to objects.  |  
| [`IcepakMesh.assign_mesh_level_to_group`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group")(...[, ...])  | Assign a mesh level to a group.  |  
| [`IcepakMesh.assign_mesh_region`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region")([assignment, ...])  | Assign a predefined surface mesh level to an object.  |  
| [`IcepakMesh.assign_mesh_reuse`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse")(assignment, ...)  | Assign a mesh file to objects.  |  
| [`IcepakMesh.assign_priorities`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities")(assignment)  | Set objects priorities.  |  
| [`IcepakMesh.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh")([name])  | Generate the mesh for a given setup name.  |  
Attributes  
| [`IcepakMesh.boundingdimension`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension")  | Bounding dimension.  |  
| --- | --- |  
| [`IcepakMesh.meshregions_dict`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict")  | Get mesh regions in the design.  |  
| [`IcepakMesh.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule")  | Icepak Mesh Module.  |  
| [`IcepakMesh.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir")  | Shortcut for dir(self).  |  
# IcepakMesh 

class ansys.aedt.core.modules.mesh_icepak.IcepakMesh(_app_) 
    
Manages Icepak meshes. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()

```
Copy to clipboard
Methods  
| [`IcepakMesh.assign_mesh_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file")(assignment, ...)  | Assign a mesh from a file to objects.  |  
| --- | --- |  
| [`IcepakMesh.assign_mesh_level`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level")(mesh_order[, name])  | Assign a mesh level to objects.  |  
| [`IcepakMesh.assign_mesh_level_to_group`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group")(...[, ...])  | Assign a mesh level to a group.  |  
| [`IcepakMesh.assign_mesh_region`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region")([assignment, ...])  | Assign a predefined surface mesh level to an object.  |  
| [`IcepakMesh.assign_mesh_reuse`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse")(assignment, ...)  | Assign a mesh file to objects.  |  
| [`IcepakMesh.assign_priorities`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities")(assignment)  | Set objects priorities.  |  
| [`IcepakMesh.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh")([name])  | Generate the mesh for a given setup name.  |  
Attributes  
| [`IcepakMesh.boundingdimension`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension")  | Bounding dimension.  |  
| --- | --- |  
| [`IcepakMesh.meshregions_dict`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict")  | Get mesh regions in the design.  |  
| [`IcepakMesh.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule")  | Icepak Mesh Module.  |  
| [`IcepakMesh.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.rst.txt)

# IcepakMesh 

class ansys.aedt.core.modules.mesh_icepak.IcepakMesh(_app_) 
    
Manages Icepak meshes. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()

```
Copy to clipboard
Methods  
| [`IcepakMesh.assign_mesh_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file")(assignment, ...)  | Assign a mesh from a file to objects.  |  
| --- | --- |  
| [`IcepakMesh.assign_mesh_level`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level")(mesh_order[, name])  | Assign a mesh level to objects.  |  
| [`IcepakMesh.assign_mesh_level_to_group`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group")(...[, ...])  | Assign a mesh level to a group.  |  
| [`IcepakMesh.assign_mesh_region`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region")([assignment, ...])  | Assign a predefined surface mesh level to an object.  |  
| [`IcepakMesh.assign_mesh_reuse`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_reuse")(assignment, ...)  | Assign a mesh file to objects.  |  
| [`IcepakMesh.assign_priorities`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_priorities")(assignment)  | Set objects priorities.  |  
| [`IcepakMesh.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh")([name])  | Generate the mesh for a given setup name.  |  
Attributes  
| [`IcepakMesh.boundingdimension`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.boundingdimension")  | Bounding dimension.  |  
| --- | --- |  
| [`IcepakMesh.meshregions_dict`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.meshregions_dict")  | Get mesh regions in the design.  |  
| [`IcepakMesh.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.omeshmodule")  | Icepak Mesh Module.  |  
| [`IcepakMesh.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir.html#ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir "ansys.aedt.core.modules.mesh_icepak.IcepakMesh.public_dir")  | Shortcut for dir(self).  |