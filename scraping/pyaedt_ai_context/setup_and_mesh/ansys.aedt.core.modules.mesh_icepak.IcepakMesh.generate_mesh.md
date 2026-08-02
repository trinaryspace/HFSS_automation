---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# generate_mesh 

IcepakMesh.generate_mesh(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate the mesh for a given setup name. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design to mesh. Default is `None` in which case the first available setup will be selected. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.GenerateMesh

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.generate_mesh(name="MyObject")

```
Copy to clipboard
# generate_mesh 

IcepakMesh.generate_mesh(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate the mesh for a given setup name. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design to mesh. Default is `None` in which case the first available setup will be selected. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.GenerateMesh

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.generate_mesh(name="MyObject")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.IcepakMesh.generate_mesh.rst.txt)

# generate_mesh 

IcepakMesh.generate_mesh(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate the mesh for a given setup name. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design to mesh. Default is `None` in which case the first available setup will be selected. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.GenerateMesh

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import IcepakMesh
>>> obj = IcepakMesh()
>>> obj.generate_mesh(name="MyObject")

```
Copy to clipboard