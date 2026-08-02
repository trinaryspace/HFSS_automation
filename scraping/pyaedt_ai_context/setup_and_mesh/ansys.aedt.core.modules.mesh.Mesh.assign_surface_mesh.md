---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_surface_mesh 

Mesh.assign_surface_mesh(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a surface mesh level to one or more objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the objects. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of the surface mesh. Options are `1` through `10` 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignTrueSurfOp

```
Copy to clipboard
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> surface = hfss.mesh.assign_surface_mesh(o.id, 3, "Surface")

```
Copy to clipboard
# assign_surface_mesh 

Mesh.assign_surface_mesh(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a surface mesh level to one or more objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the objects. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of the surface mesh. Options are `1` through `10` 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignTrueSurfOp

```
Copy to clipboard
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> surface = hfss.mesh.assign_surface_mesh(o.id, 3, "Surface")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh.rst.txt)

# assign_surface_mesh 

Mesh.assign_surface_mesh(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _level : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a surface mesh level to one or more objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the objects. 

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Level of the surface mesh. Options are `1` through `10` 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the mesh operation. The default is `None`. 

Returns: 
     

`ansys.aedt.core.modules.mesh.MeshOperation`
    
Mesh operation object.
References

```
>>> oModule.AssignTrueSurfOp

```
Copy to clipboard
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> o = hfss.modeler.create_cylinder(0, [0, 0, 0], 3, 20, 0)
>>> surface = hfss.mesh.assign_surface_mesh(o.id, 3, "Surface")

```
Copy to clipboard