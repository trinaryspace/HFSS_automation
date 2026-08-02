---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_rotational_layer 

Mesh.assign_rotational_layer(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _layers_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _total_thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a rotational layer mesh. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**layers_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of layers to create in the radial direction, starting from the faces most adjacent to the band. The default is `3`, which is the maximum. 

**total_thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Total thickness of all layers with units. The default is `"1mm"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignRotationalLayerOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_rotational_layer(assignment="Box1")

```
Copy to clipboard
# assign_rotational_layer 

Mesh.assign_rotational_layer(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _layers_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _total_thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a rotational layer mesh. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**layers_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of layers to create in the radial direction, starting from the faces most adjacent to the band. The default is `3`, which is the maximum. 

**total_thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Total thickness of all layers with units. The default is `"1mm"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignRotationalLayerOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_rotational_layer(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_rotational_layer.rst.txt)

# assign_rotational_layer 

Mesh.assign_rotational_layer(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _layers_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _total_thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a rotational layer mesh. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**layers_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of layers to create in the radial direction, starting from the faces most adjacent to the band. The default is `3`, which is the maximum. 

**total_thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Total thickness of all layers with units. The default is `"1mm"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignRotationalLayerOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_rotational_layer(assignment="Box1")

```
Copy to clipboard