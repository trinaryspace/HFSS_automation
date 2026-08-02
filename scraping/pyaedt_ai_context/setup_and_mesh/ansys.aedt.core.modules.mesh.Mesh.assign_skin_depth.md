---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_skin_depth 

Mesh.assign_skin_depth(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skin_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2mm'_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _triangulation_max_length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.1mm'_, _layers_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a skin depth for the mesh refinement. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the object names, face IDs or edges IDs for Maxwell 2D design. 

**skin_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Skin depth value. It can be either provided as a float or as a string. The default is `"0.2mm"`. 

**maximum_elements**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of elements. The default is `None`, which means this parameter is disabled. 

**triangulation_max_length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum surface triangulation length with units. The default is `"0.1mm"`. 

**layers_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `"2"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignSkinDepthOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_skin_depth(assignment="Box1")

```
Copy to clipboard
# assign_skin_depth 

Mesh.assign_skin_depth(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skin_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2mm'_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _triangulation_max_length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.1mm'_, _layers_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a skin depth for the mesh refinement. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the object names, face IDs or edges IDs for Maxwell 2D design. 

**skin_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Skin depth value. It can be either provided as a float or as a string. The default is `"0.2mm"`. 

**maximum_elements**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of elements. The default is `None`, which means this parameter is disabled. 

**triangulation_max_length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum surface triangulation length with units. The default is `"0.1mm"`. 

**layers_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `"2"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignSkinDepthOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_skin_depth(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth.rst.txt)

# assign_skin_depth 

Mesh.assign_skin_depth(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skin_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2mm'_, _maximum_elements : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _triangulation_max_length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.1mm'_, _layers_number : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a skin depth for the mesh refinement. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the object names, face IDs or edges IDs for Maxwell 2D design. 

**skin_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Skin depth value. It can be either provided as a float or as a string. The default is `"0.2mm"`. 

**maximum_elements**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of elements. The default is `None`, which means this parameter is disabled. 

**triangulation_max_length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum surface triangulation length with units. The default is `"0.1mm"`. 

**layers_number**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `"2"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignSkinDepthOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_skin_depth(assignment="Box1")

```
Copy to clipboard