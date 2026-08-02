---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.generate_mesh.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# generate_mesh 

Mesh.generate_mesh(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate the mesh for a design. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the simulation setup. 

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
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> m3d.create_setup(setupname="Setup1")
>>> m3d.mesh.assign_length_mesh(maxlength=5, maxel="None")
>>> m3d.mesh.generate_mesh("Setup1")

```
Copy to clipboard
# generate_mesh 

Mesh.generate_mesh(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate the mesh for a design. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the simulation setup. 

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
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> m3d.create_setup(setupname="Setup1")
>>> m3d.mesh.assign_length_mesh(maxlength=5, maxel="None")
>>> m3d.mesh.generate_mesh("Setup1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.generate_mesh.rst.txt)

# generate_mesh 

Mesh.generate_mesh(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Generate the mesh for a design. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the simulation setup. 

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
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> m3d.create_setup(setupname="Setup1")
>>> m3d.mesh.assign_length_mesh(maxlength=5, maxel="None")
>>> m3d.mesh.generate_mesh("Setup1")

```
Copy to clipboard