---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_object_coordinate_system.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_object_coordinate_system 

Modeler3D.create_object_coordinate_system(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _origin : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _move_to_end : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reverse_x_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reverse_y_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → ObjectCoordinateSystem 
    
Create an object coordinate system. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Object to attach the object coordinate system to. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Refer to the origin where the object coordinate system is anchored. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the origin coordinate system `[x, y, z]`.
> 

**x_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Entity that the x axis of the object coordinate system points to. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the point coordinate system `[x, y, z]` that the x axis points to.
> 

**y_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Entity that the y axis of the object coordinate system points to. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the point coordinate system `[x, y, z]` that the y axis points to.
> 

**move_to_end**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the Coordinate System creation operation will always be moved to the end of subsequent objects operation. This will guarantee that the coordinate system will remain solidal with the object face. If `False` the option “Always Move CS to End” is set to off. The default is `True`. 

**reverse_x_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the x-axis is in the reverse direction. The default is `False`. 

**reverse_y_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the y-axis is in the reverse direction. The default is `False`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_object_coordinate_system(
...     assignment="Box1", origin=[0, 0, 0], x_axis=[1, 0, 0], y_axis=[0, 1, 0], name="ObjectCS1"
... )

```
Copy to clipboard
# create_object_coordinate_system 

Modeler3D.create_object_coordinate_system(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _origin : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _move_to_end : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reverse_x_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reverse_y_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → ObjectCoordinateSystem 
    
Create an object coordinate system. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Object to attach the object coordinate system to. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Refer to the origin where the object coordinate system is anchored. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the origin coordinate system `[x, y, z]`.
> 

**x_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Entity that the x axis of the object coordinate system points to. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the point coordinate system `[x, y, z]` that the x axis points to.
> 

**y_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Entity that the y axis of the object coordinate system points to. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the point coordinate system `[x, y, z]` that the y axis points to.
> 

**move_to_end**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the Coordinate System creation operation will always be moved to the end of subsequent objects operation. This will guarantee that the coordinate system will remain solidal with the object face. If `False` the option “Always Move CS to End” is set to off. The default is `True`. 

**reverse_x_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the x-axis is in the reverse direction. The default is `False`. 

**reverse_y_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the y-axis is in the reverse direction. The default is `False`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_object_coordinate_system(
...     assignment="Box1", origin=[0, 0, 0], x_axis=[1, 0, 0], y_axis=[0, 1, 0], name="ObjectCS1"
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_object_coordinate_system.rst.txt)

# create_object_coordinate_system 

Modeler3D.create_object_coordinate_system(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _origin : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _move_to_end : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _reverse_x_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reverse_y_axis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → ObjectCoordinateSystem 
    
Create an object coordinate system. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Object to attach the object coordinate system to. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Refer to the origin where the object coordinate system is anchored. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the origin coordinate system `[x, y, z]`.
> 

**x_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Entity that the x axis of the object coordinate system points to. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the point coordinate system `[x, y, z]` that the x axis points to.
> 

**y_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `VertexPrimitive`, `EdgePrimitive`, `FacePrimitive`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Entity that the y axis of the object coordinate system points to. It can be:
>   * int in which case it refers to the entity Id.
>   * VertexPrimitive, EdgePrimitive, FacePrimitive in which case it refers to the entity type.
>   * list in which case it refers to the point coordinate system `[x, y, z]` that the y axis points to.
> 

**move_to_end**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the Coordinate System creation operation will always be moved to the end of subsequent objects operation. This will guarantee that the coordinate system will remain solidal with the object face. If `False` the option “Always Move CS to End” is set to off. The default is `True`. 

**reverse_x_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the x-axis is in the reverse direction. The default is `False`. 

**reverse_y_axis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the y-axis is in the reverse direction. The default is `False`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_object_coordinate_system(
...     assignment="Box1", origin=[0, 0, 0], x_axis=[1, 0, 0], y_axis=[0, 1, 0], name="ObjectCS1"
... )

```
Copy to clipboard