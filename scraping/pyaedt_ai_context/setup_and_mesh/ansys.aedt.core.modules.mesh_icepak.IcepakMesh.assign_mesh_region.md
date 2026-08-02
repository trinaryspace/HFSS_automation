---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_mesh_region 

IcepakMesh.assign_mesh_region(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [MeshRegion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion "ansys.aedt.core.modules.mesh_icepak.MeshRegion") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a predefined surface mesh level to an object. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects to apply the mesh region to. The default is `None`, in which case all objects are selected. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Level of the surface mesh. Options are `1` through `5`. The default is `5`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh region. The default is `"MeshRegion1"`. 

Returns: 
     

`ansys.aedt.core.modules.mesh_icepak.IcepakMesh.MeshRegion`
    
References

```
>>> oModule.AssignMeshRegion

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_region(assignment="Box1", name="MyObject")

```
Copy to clipboard
# assign_mesh_region 

IcepakMesh.assign_mesh_region(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [MeshRegion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion "ansys.aedt.core.modules.mesh_icepak.MeshRegion") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a predefined surface mesh level to an object. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects to apply the mesh region to. The default is `None`, in which case all objects are selected. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Level of the surface mesh. Options are `1` through `5`. The default is `5`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh region. The default is `"MeshRegion1"`. 

Returns: 
     

`ansys.aedt.core.modules.mesh_icepak.IcepakMesh.MeshRegion`
    
References

```
>>> oModule.AssignMeshRegion

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_region(assignment="Box1", name="MyObject")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.assign_mesh_region.rst.txt)

# assign_mesh_region 

IcepakMesh.assign_mesh_region(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [MeshRegion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion "ansys.aedt.core.modules.mesh_icepak.MeshRegion") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign a predefined surface mesh level to an object. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects to apply the mesh region to. The default is `None`, in which case all objects are selected. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Level of the surface mesh. Options are `1` through `5`. The default is `5`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh region. The default is `"MeshRegion1"`. 

Returns: 
     

`ansys.aedt.core.modules.mesh_icepak.IcepakMesh.MeshRegion`
    
References

```
>>> oModule.AssignMeshRegion

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.assign_mesh_region(assignment="Box1", name="MyObject")

```
Copy to clipboard