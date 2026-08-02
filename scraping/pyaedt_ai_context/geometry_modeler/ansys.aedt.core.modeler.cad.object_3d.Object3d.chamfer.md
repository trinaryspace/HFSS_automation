---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.chamfer.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# chamfer 

Object3d.chamfer(_vertices : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _edges : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _left_distance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _right_distance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 45_, _chamfer_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a chamfer to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

**vertices**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of vertices to chamfer. 

**edges**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of edges to chamfer. 

**left_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Left distance from the edge. The default is `1`. 

**right_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Right distance from the edge. The default is `None`. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), optional. 
    
Angle value for chamfer types 2 and 3. The default is `0`. 

**chamfer_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Type of the chamfer. Options are:
    
  * 0 - Symmetric
  * 1 - Left Distance-Right Distance
  * 2 - Left Distance-Angle
  * 3 - Right Distance-Angle

The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Chamfer

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.chamfer(vertices=["Box1"], edges=[1])

```
Copy to clipboard
# chamfer 

Object3d.chamfer(_vertices : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _edges : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _left_distance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _right_distance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 45_, _chamfer_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a chamfer to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

**vertices**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of vertices to chamfer. 

**edges**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of edges to chamfer. 

**left_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Left distance from the edge. The default is `1`. 

**right_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Right distance from the edge. The default is `None`. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), optional. 
    
Angle value for chamfer types 2 and 3. The default is `0`. 

**chamfer_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Type of the chamfer. Options are:
    
  * 0 - Symmetric
  * 1 - Left Distance-Right Distance
  * 2 - Left Distance-Angle
  * 3 - Right Distance-Angle

The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Chamfer

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.chamfer(vertices=["Box1"], edges=[1])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.chamfer.rst.txt)

# chamfer 

Object3d.chamfer(_vertices : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _edges : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _left_distance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _right_distance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 45_, _chamfer_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a chamfer to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

**vertices**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of vertices to chamfer. 

**edges**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of edges to chamfer. 

**left_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Left distance from the edge. The default is `1`. 

**right_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Right distance from the edge. The default is `None`. 

**angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), optional. 
    
Angle value for chamfer types 2 and 3. The default is `0`. 

**chamfer_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Type of the chamfer. Options are:
    
  * 0 - Symmetric
  * 1 - Left Distance-Right Distance
  * 2 - Left Distance-Angle
  * 3 - Right Distance-Angle

The default is `0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Chamfer

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.chamfer(vertices=["Box1"], edges=[1])

```
Copy to clipboard