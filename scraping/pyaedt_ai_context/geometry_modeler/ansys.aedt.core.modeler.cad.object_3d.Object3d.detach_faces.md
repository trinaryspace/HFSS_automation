---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.detach_faces.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# detach_faces 

Object3d.detach_faces(_faces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")] | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Section the object. 

Parameters: 
     

**faces**`List`[`FacePrimitive`] `or` `List`[[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `FacePrimitive` 
    
Face or faces to detach from the object. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
List of object resulting from the operation.
References

```
>>> oEditor.DetachFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.detach_faces(faces=[1])

```
Copy to clipboard
# detach_faces 

Object3d.detach_faces(_faces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")] | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Section the object. 

Parameters: 
     

**faces**`List`[`FacePrimitive`] `or` `List`[[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `FacePrimitive` 
    
Face or faces to detach from the object. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
List of object resulting from the operation.
References

```
>>> oEditor.DetachFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.detach_faces(faces=[1])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.detach_faces.rst.txt)

# detach_faces 

Object3d.detach_faces(_faces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")] | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] 
    
Section the object. 

Parameters: 
     

**faces**`List`[`FacePrimitive`] `or` `List`[[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `FacePrimitive` 
    
Face or faces to detach from the object. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
List of object resulting from the operation.
References

```
>>> oEditor.DetachFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.detach_faces(faces=[1])

```
Copy to clipboard