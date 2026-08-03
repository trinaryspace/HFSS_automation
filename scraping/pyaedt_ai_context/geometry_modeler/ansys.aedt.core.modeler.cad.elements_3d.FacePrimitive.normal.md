---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# normal 

property FacePrimitive.normal: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Face normal.
Limitations: #. The face must be planar. #. Currently it works only if the face has at least two vertices. Notable excluded items are circles and ellipses that have only one vertex. #. If a bounding box is specified, the normal is orientated outwards with respect to the bounding box. Usually the bounding box refers to a volume where the face lies. If no bounding box is specified, the normal can be inward or outward the volume. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") `values` or `None` 
    
Normal vector (normalized `[x, y, z]` coordinates) or `None`.
References

```
>>> oEditor.GetVertexPosition

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.normal

```
Copy to clipboard
# normal 

property FacePrimitive.normal: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Face normal.
Limitations: #. The face must be planar. #. Currently it works only if the face has at least two vertices. Notable excluded items are circles and ellipses that have only one vertex. #. If a bounding box is specified, the normal is orientated outwards with respect to the bounding box. Usually the bounding box refers to a volume where the face lies. If no bounding box is specified, the normal can be inward or outward the volume. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") `values` or `None` 
    
Normal vector (normalized `[x, y, z]` coordinates) or `None`.
References

```
>>> oEditor.GetVertexPosition

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.normal

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal.rst.txt)

# normal 

property FacePrimitive.normal: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Face normal.
Limitations: #. The face must be planar. #. Currently it works only if the face has at least two vertices. Notable excluded items are circles and ellipses that have only one vertex. #. If a bounding box is specified, the normal is orientated outwards with respect to the bounding box. Usually the bounding box refers to a volume where the face lies. If no bounding box is specified, the normal can be inward or outward the volume. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") `values` or `None` 
    
Normal vector (normalized `[x, y, z]` coordinates) or `None`.
References

```
>>> oEditor.GetVertexPosition

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()
>>> obj.normal

```
Copy to clipboard