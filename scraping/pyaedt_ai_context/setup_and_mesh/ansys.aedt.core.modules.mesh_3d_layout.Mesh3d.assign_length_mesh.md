---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_length_mesh 

Mesh3d.assign_length_mesh(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _net : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _is_inside : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _maximum_length : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → Mesh3DOperation 
    
Assign mesh length. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the HFSS setup to apply. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**net**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the net. 

**is_inside**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the mesh length is inside the selection. The default is `True`. 

**maximum_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum length of the element. The default is `1` When `None`, this parameter is disabled. 

**maximum_elements**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of elements. The default is `1000`. When `None`, this parameter is disabled. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Mesh operation object.
References

```
>>> oModule.AddMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_3d_layout import Mesh3d
>>> obj = Mesh3d()
>>> obj.assign_length_mesh(setup="Setup1", layer="TOP", net="VCC")

```
Copy to clipboard
# assign_length_mesh 

Mesh3d.assign_length_mesh(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _net : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _is_inside : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _maximum_length : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → Mesh3DOperation 
    
Assign mesh length. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the HFSS setup to apply. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**net**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the net. 

**is_inside**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the mesh length is inside the selection. The default is `True`. 

**maximum_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum length of the element. The default is `1` When `None`, this parameter is disabled. 

**maximum_elements**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of elements. The default is `1000`. When `None`, this parameter is disabled. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Mesh operation object.
References

```
>>> oModule.AddMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_3d_layout import Mesh3d
>>> obj = Mesh3d()
>>> obj.assign_length_mesh(setup="Setup1", layer="TOP", net="VCC")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_length_mesh.rst.txt)

# assign_length_mesh 

Mesh3d.assign_length_mesh(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _net : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _is_inside : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _maximum_length : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → Mesh3DOperation 
    
Assign mesh length. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the HFSS setup to apply. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**net**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the net. 

**is_inside**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the mesh length is inside the selection. The default is `True`. 

**maximum_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum length of the element. The default is `1` When `None`, this parameter is disabled. 

**maximum_elements**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of elements. The default is `1000`. When `None`, this parameter is disabled. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Mesh operation object.
References

```
>>> oModule.AddMeshOperation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh_3d_layout import Mesh3d
>>> obj = Mesh3d()
>>> obj.assign_length_mesh(setup="Setup1", layer="TOP", net="VCC")

```
Copy to clipboard