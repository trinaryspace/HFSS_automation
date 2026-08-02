---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperations.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# meshoperations 

property Mesh.meshoperations: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[MeshOperation] 
    
Return the available mesh operations. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[`ansys.aedt.core.modules.mesh.MeshOperation`]
    
List of mesh operation object.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> mr1 = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")
>>> mesh_operations_list = hfss.mesh.meshoperations

```
Copy to clipboard
# meshoperations 

property Mesh.meshoperations: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[MeshOperation] 
    
Return the available mesh operations. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[`ansys.aedt.core.modules.mesh.MeshOperation`]
    
List of mesh operation object.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> mr1 = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")
>>> mesh_operations_list = hfss.mesh.meshoperations

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperations.rst.txt)

# meshoperations 

property Mesh.meshoperations: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[MeshOperation] 
    
Return the available mesh operations. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[`ansys.aedt.core.modules.mesh.MeshOperation`]
    
List of mesh operation object.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> mr1 = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")
>>> mesh_operations_list = hfss.mesh.meshoperations

```
Copy to clipboard