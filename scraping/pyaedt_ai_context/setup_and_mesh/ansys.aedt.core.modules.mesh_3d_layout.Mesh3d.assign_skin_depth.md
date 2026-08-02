---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_skin_depth 

Mesh3d.assign_skin_depth(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _net : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skin_depth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _triangulation_max_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _layers_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → Mesh3DOperation 
    
Assign skin depth to the mesh. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**net**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the net. 

**skin_depth**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Depth of the skin. The default is `1`. 

**maximum_elements**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum element length. The default is `None`, which disables this parameter. 

**triangulation_max_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum surface triangulation length. The default is `0.1`. 

**layers_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `"2"`. 

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
>>> obj.assign_skin_depth(setup="Setup1", layer="TOP", net="VCC")

```
Copy to clipboard
# assign_skin_depth 

Mesh3d.assign_skin_depth(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _net : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skin_depth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _triangulation_max_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _layers_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → Mesh3DOperation 
    
Assign skin depth to the mesh. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**net**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the net. 

**skin_depth**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Depth of the skin. The default is `1`. 

**maximum_elements**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum element length. The default is `None`, which disables this parameter. 

**triangulation_max_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum surface triangulation length. The default is `0.1`. 

**layers_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `"2"`. 

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
>>> obj.assign_skin_depth(setup="Setup1", layer="TOP", net="VCC")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_3d_layout.Mesh3d.assign_skin_depth.rst.txt)

# assign_skin_depth 

Mesh3d.assign_skin_depth(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _net : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skin_depth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _triangulation_max_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.1_, _layers_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → Mesh3DOperation 
    
Assign skin depth to the mesh. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**layer**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**net**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the net. 

**skin_depth**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Depth of the skin. The default is `1`. 

**maximum_elements**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum element length. The default is `None`, which disables this parameter. 

**triangulation_max_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum surface triangulation length. The default is `0.1`. 

**layers_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `"2"`. 

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
>>> obj.assign_skin_depth(setup="Setup1", layer="TOP", net="VCC")

```
Copy to clipboard