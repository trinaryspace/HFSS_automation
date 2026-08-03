---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.uncover_faces.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# uncover_faces 

Modeler3D.uncover_faces(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Uncover faces. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Sheet objects to uncover. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.UncoverFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> app = Maxwell3d()
>>> circle_1 = app.modeler.create_circle(orientation=0, origin=[0, 0, 0], radius=3, name="Circle1")
>>> box_1 = app.modeler.create_box(origin=[-13.9, 0, 0], sizes=[27.8, -40, 25.4], name="Box1")
>>> app.modeler.uncover_faces([circle_1.faces[0], [box_1.faces[0], box_1.faces[2]]])

```
Copy to clipboard
# uncover_faces 

Modeler3D.uncover_faces(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Uncover faces. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Sheet objects to uncover. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.UncoverFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> app = Maxwell3d()
>>> circle_1 = app.modeler.create_circle(orientation=0, origin=[0, 0, 0], radius=3, name="Circle1")
>>> box_1 = app.modeler.create_box(origin=[-13.9, 0, 0], sizes=[27.8, -40, 25.4], name="Box1")
>>> app.modeler.uncover_faces([circle_1.faces[0], [box_1.faces[0], box_1.faces[2]]])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.uncover_faces.rst.txt)

# uncover_faces 

Modeler3D.uncover_faces(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Uncover faces. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Sheet objects to uncover. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.UncoverFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d
>>> app = Maxwell3d()
>>> circle_1 = app.modeler.create_circle(orientation=0, origin=[0, 0, 0], radius=3, name="Circle1")
>>> box_1 = app.modeler.create_box(origin=[-13.9, 0, 0], sizes=[27.8, -40, 25.4], name="Box1")
>>> app.modeler.uncover_faces([circle_1.faces[0], [box_1.faces[0], box_1.faces[2]]])

```
Copy to clipboard