---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# assign_surface_mesh_manual 

Mesh.assign_surface_mesh_manual(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _surface_deviation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _normal_dev : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _aspect_ratio : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a surface mesh to a list of faces. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") 
    
List of faces to apply the surface mesh to. 

**surface_deviation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Surface deviation. The default is `None`. You can specify a float value, a number with units, or “inf”. 

**normal_dev**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Normal deviation. The default is `None`. 

**aspect_ratio**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Aspect ratio. The default is `None`. 

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
>>> surface = hfss.mesh.assign_surface_mesh_manual(o.id, 1e-6, aspect_ratio=3, name="Surface_Manual")

```
Copy to clipboard
# assign_surface_mesh_manual 

Mesh.assign_surface_mesh_manual(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _surface_deviation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _normal_dev : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _aspect_ratio : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a surface mesh to a list of faces. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") 
    
List of faces to apply the surface mesh to. 

**surface_deviation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Surface deviation. The default is `None`. You can specify a float value, a number with units, or “inf”. 

**normal_dev**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Normal deviation. The default is `None`. 

**aspect_ratio**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Aspect ratio. The default is `None`. 

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
>>> surface = hfss.mesh.assign_surface_mesh_manual(o.id, 1e-6, aspect_ratio=3, name="Surface_Manual")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh.Mesh.assign_surface_mesh_manual.rst.txt)

# assign_surface_mesh_manual 

Mesh.assign_surface_mesh_manual(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _surface_deviation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _normal_dev : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _aspect_ratio : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → MeshOperation 
    
Assign a surface mesh to a list of faces. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") 
    
List of faces to apply the surface mesh to. 

**surface_deviation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Surface deviation. The default is `None`. You can specify a float value, a number with units, or “inf”. 

**normal_dev**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Normal deviation. The default is `None`. 

**aspect_ratio**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Aspect ratio. The default is `None`. 

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
>>> surface = hfss.mesh.assign_surface_mesh_manual(o.id, 1e-6, aspect_ratio=3, name="Surface_Manual")

```
Copy to clipboard