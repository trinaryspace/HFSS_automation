---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# Mesh 

class ansys.aedt.core.modules.mesh.Mesh(_app_) 
    
Manages AEDT mesh functions for 2D and 3D solvers (HFSS, Maxwell, and Q3D). 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> cylinder = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> model_resolution = hfss.mesh.assign_model_resolution(cylinder, 1e-4, "ModelRes1")

```
Copy to clipboard
Methods  
| [`Mesh.assign_curvature_extraction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction.html#ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction "ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction")(assignment)  | Assign curvature extraction.  |  
| --- | --- |  
| [`Mesh.assign_curvilinear_elements`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements.html#ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements "ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements")(assignment)  | Assign curvilinear elements.  |  
| [`Mesh.assign_cylindrical_gap`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap.html#ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap "ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap")(entity[, name, ...])  | Assign a cylindrical gap for a 2D or 3D design to enable a clone mesh and associated band mapping angle.  |  
| [`Mesh.assign_density_control`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_density_control.html#ansys.aedt.core.modules.mesh.Mesh.assign_density_control "ansys.aedt.core.modules.mesh.Mesh.assign_density_control")(assignment[, ...])  | Assign density control.  |  
| [`Mesh.assign_edge_cut`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut.html#ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut "ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut")(assignment[, ...])  | Assign an edge cut layer mesh.  |  
| [`Mesh.assign_initial_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh")([method, ...])  | Assign a surface mesh level to an object.  |  
| [`Mesh.assign_initial_mesh_from_slider`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider.html#ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider "ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider")([...])  | Assign a surface mesh level to an object.  |  
| [`Mesh.assign_length_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh")(assignment[, ...])  | Assign a length for the model resolution.  |  
| [`Mesh.assign_model_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution.html#ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution "ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution")(assignment[, ...])  | Assign the model resolution.  |  
| [`Mesh.assign_rotational_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer.html#ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer "ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer")(assignment[, ...])  | Assign a rotational layer mesh.  |  
| [`Mesh.assign_skin_depth`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth.html#ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth "ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth")(assignment[, ...])  | Assign a skin depth for the mesh refinement.  |  
| [`Mesh.assign_surf_priority_for_tau`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau.html#ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau "ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau")(assignment)  | Assign a surface representation priority for the TAU mesh.  |  
| [`Mesh.assign_surface_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh")(assignment, level)  | Assign a surface mesh level to one or more objects.  |  
| [`Mesh.assign_surface_mesh_manual`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual.html#ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual "ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual")(assignment)  | Assign a surface mesh to a list of faces.  |  
| [`Mesh.delete_mesh_operations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations.html#ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations "ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations")([mesh_type])  | Remove mesh operations from a design.  |  
| [`Mesh.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.generate_mesh.html#ansys.aedt.core.modules.mesh.Mesh.generate_mesh "ansys.aedt.core.modules.mesh.Mesh.generate_mesh")(name)  | Generate the mesh for a design.  |  
Attributes  
| [`Mesh.initial_mesh_settings`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings.html#ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings "ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings")  | Return the global mesh object.  |  
| --- | --- |  
| [`Mesh.meshoperation_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperation_names.html#ansys.aedt.core.modules.mesh.Mesh.meshoperation_names "ansys.aedt.core.modules.mesh.Mesh.meshoperation_names")  | Return the available mesh operation names.  |  
| [`Mesh.meshoperations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperations.html#ansys.aedt.core.modules.mesh.Mesh.meshoperations "ansys.aedt.core.modules.mesh.Mesh.meshoperations")  | Return the available mesh operations.  |  
| [`Mesh.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.omeshmodule.html#ansys.aedt.core.modules.mesh.Mesh.omeshmodule "ansys.aedt.core.modules.mesh.Mesh.omeshmodule")  | AEDT Mesh Module.  |  
| [`Mesh.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.public_dir.html#ansys.aedt.core.modules.mesh.Mesh.public_dir "ansys.aedt.core.modules.mesh.Mesh.public_dir")  | Shortcut for dir(self).  |  
# Mesh 

class ansys.aedt.core.modules.mesh.Mesh(_app_) 
    
Manages AEDT mesh functions for 2D and 3D solvers (HFSS, Maxwell, and Q3D). 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> cylinder = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> model_resolution = hfss.mesh.assign_model_resolution(cylinder, 1e-4, "ModelRes1")

```
Copy to clipboard
Methods  
| [`Mesh.assign_curvature_extraction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction.html#ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction "ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction")(assignment)  | Assign curvature extraction.  |  
| --- | --- |  
| [`Mesh.assign_curvilinear_elements`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements.html#ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements "ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements")(assignment)  | Assign curvilinear elements.  |  
| [`Mesh.assign_cylindrical_gap`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap.html#ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap "ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap")(entity[, name, ...])  | Assign a cylindrical gap for a 2D or 3D design to enable a clone mesh and associated band mapping angle.  |  
| [`Mesh.assign_density_control`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_density_control.html#ansys.aedt.core.modules.mesh.Mesh.assign_density_control "ansys.aedt.core.modules.mesh.Mesh.assign_density_control")(assignment[, ...])  | Assign density control.  |  
| [`Mesh.assign_edge_cut`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut.html#ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut "ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut")(assignment[, ...])  | Assign an edge cut layer mesh.  |  
| [`Mesh.assign_initial_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh")([method, ...])  | Assign a surface mesh level to an object.  |  
| [`Mesh.assign_initial_mesh_from_slider`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider.html#ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider "ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider")([...])  | Assign a surface mesh level to an object.  |  
| [`Mesh.assign_length_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh")(assignment[, ...])  | Assign a length for the model resolution.  |  
| [`Mesh.assign_model_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution.html#ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution "ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution")(assignment[, ...])  | Assign the model resolution.  |  
| [`Mesh.assign_rotational_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer.html#ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer "ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer")(assignment[, ...])  | Assign a rotational layer mesh.  |  
| [`Mesh.assign_skin_depth`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth.html#ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth "ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth")(assignment[, ...])  | Assign a skin depth for the mesh refinement.  |  
| [`Mesh.assign_surf_priority_for_tau`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau.html#ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau "ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau")(assignment)  | Assign a surface representation priority for the TAU mesh.  |  
| [`Mesh.assign_surface_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh")(assignment, level)  | Assign a surface mesh level to one or more objects.  |  
| [`Mesh.assign_surface_mesh_manual`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual.html#ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual "ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual")(assignment)  | Assign a surface mesh to a list of faces.  |  
| [`Mesh.delete_mesh_operations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations.html#ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations "ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations")([mesh_type])  | Remove mesh operations from a design.  |  
| [`Mesh.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.generate_mesh.html#ansys.aedt.core.modules.mesh.Mesh.generate_mesh "ansys.aedt.core.modules.mesh.Mesh.generate_mesh")(name)  | Generate the mesh for a design.  |  
Attributes  
| [`Mesh.initial_mesh_settings`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings.html#ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings "ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings")  | Return the global mesh object.  |  
| --- | --- |  
| [`Mesh.meshoperation_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperation_names.html#ansys.aedt.core.modules.mesh.Mesh.meshoperation_names "ansys.aedt.core.modules.mesh.Mesh.meshoperation_names")  | Return the available mesh operation names.  |  
| [`Mesh.meshoperations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperations.html#ansys.aedt.core.modules.mesh.Mesh.meshoperations "ansys.aedt.core.modules.mesh.Mesh.meshoperations")  | Return the available mesh operations.  |  
| [`Mesh.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.omeshmodule.html#ansys.aedt.core.modules.mesh.Mesh.omeshmodule "ansys.aedt.core.modules.mesh.Mesh.omeshmodule")  | AEDT Mesh Module.  |  
| [`Mesh.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.public_dir.html#ansys.aedt.core.modules.mesh.Mesh.public_dir "ansys.aedt.core.modules.mesh.Mesh.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.rst.txt)

# Mesh 

class ansys.aedt.core.modules.mesh.Mesh(_app_) 
    
Manages AEDT mesh functions for 2D and 3D solvers (HFSS, Maxwell, and Q3D). 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis_3d.FieldAnalysis3D` 
    
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> cylinder = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> model_resolution = hfss.mesh.assign_model_resolution(cylinder, 1e-4, "ModelRes1")

```
Copy to clipboard
Methods  
| [`Mesh.assign_curvature_extraction`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction.html#ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction "ansys.aedt.core.modules.mesh.Mesh.assign_curvature_extraction")(assignment)  | Assign curvature extraction.  |  
| --- | --- |  
| [`Mesh.assign_curvilinear_elements`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements.html#ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements "ansys.aedt.core.modules.mesh.Mesh.assign_curvilinear_elements")(assignment)  | Assign curvilinear elements.  |  
| [`Mesh.assign_cylindrical_gap`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap.html#ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap "ansys.aedt.core.modules.mesh.Mesh.assign_cylindrical_gap")(entity[, name, ...])  | Assign a cylindrical gap for a 2D or 3D design to enable a clone mesh and associated band mapping angle.  |  
| [`Mesh.assign_density_control`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_density_control.html#ansys.aedt.core.modules.mesh.Mesh.assign_density_control "ansys.aedt.core.modules.mesh.Mesh.assign_density_control")(assignment[, ...])  | Assign density control.  |  
| [`Mesh.assign_edge_cut`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut.html#ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut "ansys.aedt.core.modules.mesh.Mesh.assign_edge_cut")(assignment[, ...])  | Assign an edge cut layer mesh.  |  
| [`Mesh.assign_initial_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh")([method, ...])  | Assign a surface mesh level to an object.  |  
| [`Mesh.assign_initial_mesh_from_slider`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider.html#ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider "ansys.aedt.core.modules.mesh.Mesh.assign_initial_mesh_from_slider")([...])  | Assign a surface mesh level to an object.  |  
| [`Mesh.assign_length_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh")(assignment[, ...])  | Assign a length for the model resolution.  |  
| [`Mesh.assign_model_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution.html#ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution "ansys.aedt.core.modules.mesh.Mesh.assign_model_resolution")(assignment[, ...])  | Assign the model resolution.  |  
| [`Mesh.assign_rotational_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer.html#ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer "ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer")(assignment[, ...])  | Assign a rotational layer mesh.  |  
| [`Mesh.assign_skin_depth`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth.html#ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth "ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth")(assignment[, ...])  | Assign a skin depth for the mesh refinement.  |  
| [`Mesh.assign_surf_priority_for_tau`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau.html#ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau "ansys.aedt.core.modules.mesh.Mesh.assign_surf_priority_for_tau")(assignment)  | Assign a surface representation priority for the TAU mesh.  |  
| [`Mesh.assign_surface_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh.html#ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh "ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh")(assignment, level)  | Assign a surface mesh level to one or more objects.  |  
| [`Mesh.assign_surface_mesh_manual`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual.html#ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual "ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual")(assignment)  | Assign a surface mesh to a list of faces.  |  
| [`Mesh.delete_mesh_operations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations.html#ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations "ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations")([mesh_type])  | Remove mesh operations from a design.  |  
| [`Mesh.generate_mesh`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.generate_mesh.html#ansys.aedt.core.modules.mesh.Mesh.generate_mesh "ansys.aedt.core.modules.mesh.Mesh.generate_mesh")(name)  | Generate the mesh for a design.  |  
Attributes  
| [`Mesh.initial_mesh_settings`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings.html#ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings "ansys.aedt.core.modules.mesh.Mesh.initial_mesh_settings")  | Return the global mesh object.  |  
| --- | --- |  
| [`Mesh.meshoperation_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperation_names.html#ansys.aedt.core.modules.mesh.Mesh.meshoperation_names "ansys.aedt.core.modules.mesh.Mesh.meshoperation_names")  | Return the available mesh operation names.  |  
| [`Mesh.meshoperations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperations.html#ansys.aedt.core.modules.mesh.Mesh.meshoperations "ansys.aedt.core.modules.mesh.Mesh.meshoperations")  | Return the available mesh operations.  |  
| [`Mesh.omeshmodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.omeshmodule.html#ansys.aedt.core.modules.mesh.Mesh.omeshmodule "ansys.aedt.core.modules.mesh.Mesh.omeshmodule")  | AEDT Mesh Module.  |  
| [`Mesh.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.public_dir.html#ansys.aedt.core.modules.mesh.Mesh.public_dir "ansys.aedt.core.modules.mesh.Mesh.public_dir")  | Shortcut for dir(self).  |