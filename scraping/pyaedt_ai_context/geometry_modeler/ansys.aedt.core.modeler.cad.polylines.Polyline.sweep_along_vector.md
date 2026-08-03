---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.sweep_along_vector.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# sweep_along_vector 

Polyline.sweep_along_vector(_sweep_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _draft_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Round'_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sweep the selection along a vector. 

Parameters: 
     

**sweep_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Application.Position object. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of the draft in degrees. The default is `0`. 

**draft_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the draft. Options are `"Extended"`, `"Round"`, and `"Natural"`. The default value is `"Round`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when model, `False` otherwise.
References

```
>>> oEditor.SweepAlongVector

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.sweep_along_vector(sweep_vector=[1, 0, 0])

```
Copy to clipboard
# sweep_along_vector 

Polyline.sweep_along_vector(_sweep_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _draft_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Round'_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sweep the selection along a vector. 

Parameters: 
     

**sweep_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Application.Position object. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of the draft in degrees. The default is `0`. 

**draft_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the draft. Options are `"Extended"`, `"Round"`, and `"Natural"`. The default value is `"Round`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when model, `False` otherwise.
References

```
>>> oEditor.SweepAlongVector

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.sweep_along_vector(sweep_vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.sweep_along_vector.rst.txt)

# sweep_along_vector 

Polyline.sweep_along_vector(_sweep_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _draft_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Round'_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sweep the selection along a vector. 

Parameters: 
     

**sweep_vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Application.Position object. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of the draft in degrees. The default is `0`. 

**draft_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the draft. Options are `"Extended"`, `"Round"`, and `"Natural"`. The default value is `"Round`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when model, `False` otherwise.
References

```
>>> oEditor.SweepAlongVector

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.sweep_along_vector(sweep_vector=[1, 0, 0])

```
Copy to clipboard