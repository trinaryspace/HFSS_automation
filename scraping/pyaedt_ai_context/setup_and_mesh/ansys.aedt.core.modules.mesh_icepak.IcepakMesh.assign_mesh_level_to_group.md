---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_mesh_level_to_group 

IcepakMesh.assign_mesh_level_to_group(_mesh_level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _group_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _enable_local_mesh_parameters : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _local_mesh_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'No local mesh parameters'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a mesh level to a group. 

Parameters: 
     

**mesh_level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of mesh to assign. Options are `1` through `5`. 

**group_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the group. 

**enable_local_mesh_parameters**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**local_mesh_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"No Local Mesh Parameters"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_level_to_group(mesh_level=1, group_name=1)

```
Copy to clipboard
# assign_mesh_level_to_group 

IcepakMesh.assign_mesh_level_to_group(_mesh_level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _group_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _enable_local_mesh_parameters : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _local_mesh_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'No local mesh parameters'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a mesh level to a group. 

Parameters: 
     

**mesh_level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of mesh to assign. Options are `1` through `5`. 

**group_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the group. 

**enable_local_mesh_parameters**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**local_mesh_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"No Local Mesh Parameters"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_level_to_group(mesh_level=1, group_name=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level_to_group.rst.txt)

# assign_mesh_level_to_group 

IcepakMesh.assign_mesh_level_to_group(_mesh_level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _group_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _enable_local_mesh_parameters : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _local_mesh_parameters : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'No local mesh parameters'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a mesh level to a group. 

Parameters: 
     

**mesh_level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of mesh to assign. Options are `1` through `5`. 

**group_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the group. 

**enable_local_mesh_parameters**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**local_mesh_parameters**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `"No Local Mesh Parameters"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_level_to_group(mesh_level=1, group_name=1)

```
Copy to clipboard