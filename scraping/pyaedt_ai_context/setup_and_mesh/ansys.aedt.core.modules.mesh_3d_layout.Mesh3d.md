---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# Mesh3d 

class ansys.aedt.core.modules.mesh_3d_layout.Mesh3d(_app_) 
    
Manages mesh operations for HFSS 3D Layout.
Provides the main AEDT mesh functionality. The inherited class `AEDTConfig` contains all `_desktop` hierarchical calls needed by this class. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d_layout.FieldAnalysis3DLayout` 
    
Examples

```
>>> from ansys.aedt.core.modules.mesh_3d_layout import Mesh3d
>>> obj = Mesh3d()

```
Copy to clipboard
Methods  
| [`Mesh3d.assign_length_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh")(setup, layer, net)  | Assign mesh length.  |  
| --- | --- |  
| [`Mesh3d.assign_skin_depth`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth")(setup, layer, net)  | Assign skin depth to the mesh.  |  
| [`Mesh3d.delete_mesh_operations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations")(setup, name)  | Remove mesh operations from a setup.  |  
| [`Mesh3d.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh")(name)  | Generate the mesh for a design.  |  
Attributes  
| [`Mesh3d.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule")  | AEDT Mesh Module.  |  
| --- | --- |  
| [`Mesh3d.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir")  | Shortcut for dir(self).  |  
# Mesh3d 

class ansys.aedt.core.modules.mesh_3d_layout.Mesh3d(_app_) 
    
Manages mesh operations for HFSS 3D Layout.
Provides the main AEDT mesh functionality. The inherited class `AEDTConfig` contains all `_desktop` hierarchical calls needed by this class. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d_layout.FieldAnalysis3DLayout` 
    
Examples

```
>>> from ansys.aedt.core.modules.mesh_3d_layout import Mesh3d
>>> obj = Mesh3d()

```
Copy to clipboard
Methods  
| [`Mesh3d.assign_length_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh")(setup, layer, net)  | Assign mesh length.  |  
| --- | --- |  
| [`Mesh3d.assign_skin_depth`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth")(setup, layer, net)  | Assign skin depth to the mesh.  |  
| [`Mesh3d.delete_mesh_operations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations")(setup, name)  | Remove mesh operations from a setup.  |  
| [`Mesh3d.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh")(name)  | Generate the mesh for a design.  |  
Attributes  
| [`Mesh3d.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule")  | AEDT Mesh Module.  |  
| --- | --- |  
| [`Mesh3d.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.rst.txt)

# Mesh3d 

class ansys.aedt.core.modules.mesh_3d_layout.Mesh3d(_app_) 
    
Manages mesh operations for HFSS 3D Layout.
Provides the main AEDT mesh functionality. The inherited class `AEDTConfig` contains all `_desktop` hierarchical calls needed by this class. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d_layout.FieldAnalysis3DLayout` 
    
Examples

```
>>> from ansys.aedt.core.modules.mesh_3d_layout import Mesh3d
>>> obj = Mesh3d()

```
Copy to clipboard
Methods  
| [`Mesh3d.assign_length_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh")(setup, layer, net)  | Assign mesh length.  |  
| --- | --- |  
| [`Mesh3d.assign_skin_depth`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth")(setup, layer, net)  | Assign skin depth to the mesh.  |  
| [`Mesh3d.delete_mesh_operations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.delete_mesh_operations")(setup, name)  | Remove mesh operations from a setup.  |  
| [`Mesh3d.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.generate_mesh")(name)  | Generate the mesh for a design.  |  
Attributes  
| [`Mesh3d.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.omeshmodule")  | AEDT Mesh Module.  |  
| --- | --- |  
| [`Mesh3d.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir.html#ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir "ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.public_dir")  | Shortcut for dir(self).  |