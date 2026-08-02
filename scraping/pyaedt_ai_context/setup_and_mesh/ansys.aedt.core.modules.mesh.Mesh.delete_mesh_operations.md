---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# delete_mesh_operations 

Mesh.delete_mesh_operations(_mesh_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove mesh operations from a design. 

Parameters: 
     

**mesh_type**`optional` 
    
Type of the mesh operation to delete. The default is `None`, in which case all mesh operations are deleted. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.DeleteOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.delete_mesh_operations(mesh_type=1)

```
Copy to clipboard
# delete_mesh_operations 

Mesh.delete_mesh_operations(_mesh_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove mesh operations from a design. 

Parameters: 
     

**mesh_type**`optional` 
    
Type of the mesh operation to delete. The default is `None`, in which case all mesh operations are deleted. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.DeleteOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.delete_mesh_operations(mesh_type=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.delete_mesh_operations.rst.txt)

# delete_mesh_operations 

Mesh.delete_mesh_operations(_mesh_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove mesh operations from a design. 

Parameters: 
     

**mesh_type**`optional` 
    
Type of the mesh operation to delete. The default is `None`, in which case all mesh operations are deleted. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.DeleteOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.delete_mesh_operations(mesh_type=1)

```
Copy to clipboard