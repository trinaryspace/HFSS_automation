---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_faces_from_materials.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_faces_from_materials 

Modeler3D.get_faces_from_materials(_filter_materials : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Select all outer faces given a list of materials. 

Parameters: 
     

**filter_materials**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of materials to include in the search for outer faces. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of all outer faces of the specified materials.
References

```
>>> oEditor.GetObjectsByMaterial
>>> oEditor.GetFaceIDs

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_faces_from_materials(filter_materials=["copper"])

```
Copy to clipboard
# get_faces_from_materials 

Modeler3D.get_faces_from_materials(_filter_materials : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Select all outer faces given a list of materials. 

Parameters: 
     

**filter_materials**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of materials to include in the search for outer faces. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of all outer faces of the specified materials.
References

```
>>> oEditor.GetObjectsByMaterial
>>> oEditor.GetFaceIDs

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_faces_from_materials(filter_materials=["copper"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_faces_from_materials.rst.txt)

# get_faces_from_materials 

Modeler3D.get_faces_from_materials(_filter_materials : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Select all outer faces given a list of materials. 

Parameters: 
     

**filter_materials**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of materials to include in the search for outer faces. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of all outer faces of the specified materials.
References

```
>>> oEditor.GetObjectsByMaterial
>>> oEditor.GetFaceIDs

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_faces_from_materials(filter_materials=["copper"])

```
Copy to clipboard