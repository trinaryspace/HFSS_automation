---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_object 

FacePrimitive.create_object(_non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Return a new object from the selected face. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to create the new object as model or non-model. Default is `False`.
References

```
>>> oEditor.CreateObjectFromFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.create_object(non_model=True)

```
Copy to clipboard
# create_object 

FacePrimitive.create_object(_non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Return a new object from the selected face. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to create the new object as model or non-model. Default is `False`.
References

```
>>> oEditor.CreateObjectFromFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.create_object(non_model=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object.rst.txt)

# create_object 

FacePrimitive.create_object(_non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Return a new object from the selected face. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either to create the new object as model or non-model. Default is `False`.
References

```
>>> oEditor.CreateObjectFromFaces

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.create_object(non_model=True)

```
Copy to clipboard