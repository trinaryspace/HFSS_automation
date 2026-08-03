---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# chamfer 

EdgePrimitive.chamfer(_left_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _right_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 45.0_, _chamfer_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a chamfer to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

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
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()
>>> obj.chamfer(left_distance=1.0, right_distance=1.0)

```
Copy to clipboard
# chamfer 

EdgePrimitive.chamfer(_left_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _right_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 45.0_, _chamfer_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a chamfer to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

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
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()
>>> obj.chamfer(left_distance=1.0, right_distance=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer.rst.txt)

# chamfer 

EdgePrimitive.chamfer(_left_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _right_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 45.0_, _chamfer_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a chamfer to the selected edges in 3D/vertices in 2D. 

Parameters: 
     

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
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()
>>> obj.chamfer(left_distance=1.0, right_distance=1.0)

```
Copy to clipboard