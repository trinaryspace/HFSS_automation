---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_density_control.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_density_control 

Mesh.assign_density_control(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _refine_inside : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _maximum_element_length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _layers_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign density control. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**refine_inside**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to refine inside objects. The default is `True`. 

**maximum_element_length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum element length with units. The default is `None`, which disables this parameter. 

**layers_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `None`, which disables this parameter. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignDensityControlOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_density_control(assignment="Box1")

```
Copy to clipboard
# assign_density_control 

Mesh.assign_density_control(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _refine_inside : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _maximum_element_length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _layers_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign density control. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**refine_inside**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to refine inside objects. The default is `True`. 

**maximum_element_length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum element length with units. The default is `None`, which disables this parameter. 

**layers_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `None`, which disables this parameter. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignDensityControlOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_density_control(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_density_control.rst.txt)

# assign_density_control 

Mesh.assign_density_control(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _refine_inside : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _maximum_element_length : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _layers_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign density control. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**refine_inside**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to refine inside objects. The default is `True`. 

**maximum_element_length**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Maximum element length with units. The default is `None`, which disables this parameter. 

**layers_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of layers. The default is `None`, which disables this parameter. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignDensityControlOp

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modules.mesh import Mesh
>>> obj = Mesh()
>>> obj.assign_density_control(assignment="Box1")

```
Copy to clipboard