---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_face_coordinate_system.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_face_coordinate_system 

Modeler3D.create_face_coordinate_system(_face : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _origin : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _axis_position : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _offset : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rotation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _always_move_to_end : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → FaceCoordinateSystem 
    
Create a face coordinate system.
The face coordinate has always the Z axis parallel to face normal. The X and Y axis lie on the face plane. 

Parameters: 
     

**face**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face where the coordinate system is defined. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive`, `EdgePrimitive`, `VertexPrimitive` 
    
Coordinate system origin. The origin must belong to the face where the coordinate system is defined.
  * If a face is specified, the origin is placed on the face center. It must be the same as the `face` parameter.
  * If an edge is specified, the origin is placed on the edge midpoint.
  * If a vertex is specified, the origin is placed on the vertex.

**axis_position**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive`, `EdgePrimitive`, `VertexPrimitive` 
    
Specify where the X or Y axis is pointing. The position must belong to the face where the coordinate system is defined. Select which axis is considered with the option `axis`. If a face is specified, the position is placed on the face center. It must be the same as `face`. If an edge is specified, the position is placed on the edce midpoint. If a vertex is specified, the position is placed on the vertex. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Select which axis is considered for positioning. Possible values are `"X"` and `"Y"`. The default is `"X"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y]` coordinates specifying the offset of the coordinate system origin. The offset specified in the face coordinate system reference. The default is `[0, 0]`. 

**rotation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Rotation angle of the coordinate system around its Z axis. Angle is in degrees. The default is `0`. 

**always_move_to_end**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the Face Coordinate System creation operation will always be moved to the end of subsequent objects operation. This will guarantee that the coordinate system will remain solidal with the object face. If `False` the option “Always Move CS to End” is set to off. The default is `True`. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.FaceCoordinateSystem`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_face_coordinate_system(face=1, origin=1, axis_position=1, name="FaceCS1")

```
Copy to clipboard
# create_face_coordinate_system 

Modeler3D.create_face_coordinate_system(_face : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _origin : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _axis_position : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _offset : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rotation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _always_move_to_end : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → FaceCoordinateSystem 
    
Create a face coordinate system.
The face coordinate has always the Z axis parallel to face normal. The X and Y axis lie on the face plane. 

Parameters: 
     

**face**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face where the coordinate system is defined. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive`, `EdgePrimitive`, `VertexPrimitive` 
    
Coordinate system origin. The origin must belong to the face where the coordinate system is defined.
  * If a face is specified, the origin is placed on the face center. It must be the same as the `face` parameter.
  * If an edge is specified, the origin is placed on the edge midpoint.
  * If a vertex is specified, the origin is placed on the vertex.

**axis_position**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive`, `EdgePrimitive`, `VertexPrimitive` 
    
Specify where the X or Y axis is pointing. The position must belong to the face where the coordinate system is defined. Select which axis is considered with the option `axis`. If a face is specified, the position is placed on the face center. It must be the same as `face`. If an edge is specified, the position is placed on the edce midpoint. If a vertex is specified, the position is placed on the vertex. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Select which axis is considered for positioning. Possible values are `"X"` and `"Y"`. The default is `"X"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y]` coordinates specifying the offset of the coordinate system origin. The offset specified in the face coordinate system reference. The default is `[0, 0]`. 

**rotation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Rotation angle of the coordinate system around its Z axis. Angle is in degrees. The default is `0`. 

**always_move_to_end**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the Face Coordinate System creation operation will always be moved to the end of subsequent objects operation. This will guarantee that the coordinate system will remain solidal with the object face. If `False` the option “Always Move CS to End” is set to off. The default is `True`. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.FaceCoordinateSystem`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_face_coordinate_system(face=1, origin=1, axis_position=1, name="FaceCS1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_face_coordinate_system.rst.txt)

# create_face_coordinate_system 

Modeler3D.create_face_coordinate_system(_face : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _origin : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _axis_position : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive") | [EdgePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive") | [VertexPrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive")_, _axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'X'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _offset : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rotation : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _always_move_to_end : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → FaceCoordinateSystem 
    
Create a face coordinate system.
The face coordinate has always the Z axis parallel to face normal. The X and Y axis lie on the face plane. 

Parameters: 
     

**face**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face where the coordinate system is defined. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive`, `EdgePrimitive`, `VertexPrimitive` 
    
Coordinate system origin. The origin must belong to the face where the coordinate system is defined.
  * If a face is specified, the origin is placed on the face center. It must be the same as the `face` parameter.
  * If an edge is specified, the origin is placed on the edge midpoint.
  * If a vertex is specified, the origin is placed on the vertex.

**axis_position**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive`, `EdgePrimitive`, `VertexPrimitive` 
    
Specify where the X or Y axis is pointing. The position must belong to the face where the coordinate system is defined. Select which axis is considered with the option `axis`. If a face is specified, the position is placed on the face center. It must be the same as `face`. If an edge is specified, the position is placed on the edce midpoint. If a vertex is specified, the position is placed on the vertex. 

**axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Select which axis is considered for positioning. Possible values are `"X"` and `"Y"`. The default is `"X"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y]` coordinates specifying the offset of the coordinate system origin. The offset specified in the face coordinate system reference. The default is `[0, 0]`. 

**rotation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Rotation angle of the coordinate system around its Z axis. Angle is in degrees. The default is `0`. 

**always_move_to_end**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
If `True` the Face Coordinate System creation operation will always be moved to the end of subsequent objects operation. This will guarantee that the coordinate system will remain solidal with the object face. If `False` the option “Always Move CS to End” is set to off. The default is `True`. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.FaceCoordinateSystem`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_face_coordinate_system(face=1, origin=1, axis_position=1, name="FaceCS1")

```
Copy to clipboard