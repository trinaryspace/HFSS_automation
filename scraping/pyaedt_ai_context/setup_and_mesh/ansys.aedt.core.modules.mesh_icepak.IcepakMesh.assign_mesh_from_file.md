---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_mesh_from_file 

IcepakMesh.assign_mesh_from_file(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a mesh from a file to objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to apply the mesh file to. 

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the mesh (MSH) file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operations. Default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh Operation object. `False` when failed.
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_from_file(assignment="Box1", file_name="example.txt")

```
Copy to clipboard
# assign_mesh_from_file 

IcepakMesh.assign_mesh_from_file(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a mesh from a file to objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to apply the mesh file to. 

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the mesh (MSH) file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operations. Default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh Operation object. `False` when failed.
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_from_file(assignment="Box1", file_name="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_from_file.rst.txt)

# assign_mesh_from_file 

IcepakMesh.assign_mesh_from_file(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a mesh from a file to objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects to apply the mesh file to. 

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the mesh (MSH) file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operations. Default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh Operation object. `False` when failed.
References

```
>>> oModule.AssignMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_from_file(assignment="Box1", file_name="example.txt")

```
Copy to clipboard