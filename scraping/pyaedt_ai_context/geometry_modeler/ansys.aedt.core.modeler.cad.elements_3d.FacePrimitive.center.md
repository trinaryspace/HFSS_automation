---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# center 

property FacePrimitive.center: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Face center in model units.
Note
It returns the face center from AEDT. It falls back to get the face centroid if number of face vertices is >1. For curved faces returns a point on the surface even if it is not properly the center of mass. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") `values` 
    
Centroid of all vertices of the face.
References

```
>>> oEditor.GetFaceCenter

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.center

```
Copy to clipboard
# center 

property FacePrimitive.center: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Face center in model units.
Note
It returns the face center from AEDT. It falls back to get the face centroid if number of face vertices is >1. For curved faces returns a point on the surface even if it is not properly the center of mass. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") `values` 
    
Centroid of all vertices of the face.
References

```
>>> oEditor.GetFaceCenter

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.center

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center.rst.txt)

# center 

property FacePrimitive.center: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Face center in model units.
Note
It returns the face center from AEDT. It falls back to get the face centroid if number of face vertices is >1. For curved faces returns a point on the surface even if it is not properly the center of mass. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") `values` 
    
Centroid of all vertices of the face.
References

```
>>> oEditor.GetFaceCenter

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.center

```
Copy to clipboard