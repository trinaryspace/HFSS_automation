---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.move_face.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# move_face 

Modeler3D.move_face(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move an input face or a list of input faces of a specific object.
This method moves a face or a list of faces which belong to the same solid. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List[int] or list[[`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")] object or mixed. 

**offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset to apply in model units. The default is `1.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.MoveFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.move_face(assignment="Box1")

```
Copy to clipboard
# move_face 

Modeler3D.move_face(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move an input face or a list of input faces of a specific object.
This method moves a face or a list of faces which belong to the same solid. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List[int] or list[[`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")] object or mixed. 

**offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset to apply in model units. The default is `1.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.MoveFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.move_face(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.move_face.rst.txt)

# move_face 

Modeler3D.move_face(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move an input face or a list of input faces of a specific object.
This method moves a face or a list of faces which belong to the same solid. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List[int] or list[[`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")] object or mixed. 

**offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset to apply in model units. The default is `1.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.MoveFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.move_face(assignment="Box1")

```
Copy to clipboard