---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_mesh_level 

IcepakMesh.assign_mesh_level(_mesh_order : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[MeshOperation] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a mesh level to objects. 

Parameters: 
     

**mesh_order**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where the key is the object name and the value is the mesh level. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[`ansys.aedt.core.modules.mesh.MeshOperation`]
    
`True` when successful, `False` when failed.
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_level(mesh_order={"Name": "Value"})

```
Copy to clipboard
# assign_mesh_level 

IcepakMesh.assign_mesh_level(_mesh_order : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[MeshOperation] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a mesh level to objects. 

Parameters: 
     

**mesh_order**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where the key is the object name and the value is the mesh level. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[`ansys.aedt.core.modules.mesh.MeshOperation`]
    
`True` when successful, `False` when failed.
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_level(mesh_order={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_level.rst.txt)

# assign_mesh_level 

IcepakMesh.assign_mesh_level(_mesh_order : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[MeshOperation] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a mesh level to objects. 

Parameters: 
     

**mesh_order**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where the key is the object name and the value is the mesh level. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[`ansys.aedt.core.modules.mesh.MeshOperation`]
    
`True` when successful, `False` when failed.
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_level(mesh_order={"Name": "Value"})

```
Copy to clipboard