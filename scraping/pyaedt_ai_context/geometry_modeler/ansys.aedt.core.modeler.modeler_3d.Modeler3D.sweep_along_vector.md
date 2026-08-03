---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.sweep_along_vector.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# sweep_along_vector 

Modeler3D.sweep_along_vector(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _sweep_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _draft_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Round'_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Sweep the selection along a vector. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Name or ID of the object. 

**sweep_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1, y1, z1]` coordinates or Application.Position object for the vector. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Draft angle in degrees. The default is `0`. 

**draft_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the draft. Options are `"Round"`, `"Natural"`, and `"Extended"`. The default is `"Round"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
One or more objects created.
References

```
>>> oEditor.SweepAlongVector

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.sweep_along_vector(assignment="Box1", sweep_vector=[1, 0, 0])

```
Copy to clipboard
# sweep_along_vector 

Modeler3D.sweep_along_vector(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _sweep_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _draft_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Round'_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Sweep the selection along a vector. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Name or ID of the object. 

**sweep_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1, y1, z1]` coordinates or Application.Position object for the vector. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Draft angle in degrees. The default is `0`. 

**draft_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the draft. Options are `"Round"`, `"Natural"`, and `"Extended"`. The default is `"Round"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
One or more objects created.
References

```
>>> oEditor.SweepAlongVector

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.sweep_along_vector(assignment="Box1", sweep_vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.sweep_along_vector.rst.txt)

# sweep_along_vector 

Modeler3D.sweep_along_vector(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _sweep_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _draft_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Round'_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Sweep the selection along a vector. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Name or ID of the object. 

**sweep_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1, y1, z1]` coordinates or Application.Position object for the vector. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Draft angle in degrees. The default is `0`. 

**draft_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the draft. Options are `"Round"`, `"Natural"`, and `"Extended"`. The default is `"Round"`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
One or more objects created.
References

```
>>> oEditor.SweepAlongVector

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.sweep_along_vector(assignment="Box1", sweep_vector=[1, 0, 0])

```
Copy to clipboard