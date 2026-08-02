---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperation_names.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# meshoperation_names 

property Mesh.meshoperation_names: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Return the available mesh operation names. 

Returns: 
     

`List`
    
List of mesh operation names.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> mr1 = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")
>>> mr2 = hfss.mesh.assign_model_resolution(o, 1e-2, "ModelRes2")
>>> mesh_operations_names = hfss.mesh.meshoperation_names

```
Copy to clipboard
# meshoperation_names 

property Mesh.meshoperation_names: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Return the available mesh operation names. 

Returns: 
     

`List`
    
List of mesh operation names.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> mr1 = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")
>>> mr2 = hfss.mesh.assign_model_resolution(o, 1e-2, "ModelRes2")
>>> mesh_operations_names = hfss.mesh.meshoperation_names

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.meshoperation_names.rst.txt)

# meshoperation_names 

property Mesh.meshoperation_names: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Return the available mesh operation names. 

Returns: 
     

`List`
    
List of mesh operation names.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> mr1 = hfss.mesh.assign_model_resolution(o, 1e-4, "ModelRes1")
>>> mr2 = hfss.mesh.assign_model_resolution(o, 1e-2, "ModelRes2")
>>> mesh_operations_names = hfss.mesh.meshoperation_names

```
Copy to clipboard