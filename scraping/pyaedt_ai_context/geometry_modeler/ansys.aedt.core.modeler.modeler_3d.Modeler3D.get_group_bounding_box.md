---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_group_bounding_box.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_group_bounding_box 

Modeler3D.get_group_bounding_box(_group : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the bounding box of a group. 

Parameters: 
     

**group**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the group. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of six float values representing the bounding box in the form `[min_x, min_y, min_z, max_x, max_y, max_z]`.
References

```
>>> oEditor.GetObjectsInGroup
>>> oEditor.GetModelBoundingBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_group_bounding_box(group=1)

```
Copy to clipboard
# get_group_bounding_box 

Modeler3D.get_group_bounding_box(_group : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the bounding box of a group. 

Parameters: 
     

**group**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the group. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of six float values representing the bounding box in the form `[min_x, min_y, min_z, max_x, max_y, max_z]`.
References

```
>>> oEditor.GetObjectsInGroup
>>> oEditor.GetModelBoundingBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_group_bounding_box(group=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_group_bounding_box.rst.txt)

# get_group_bounding_box 

Modeler3D.get_group_bounding_box(_group : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the bounding box of a group. 

Parameters: 
     

**group**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the group. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of six float values representing the bounding box in the form `[min_x, min_y, min_z, max_x, max_y, max_z]`.
References

```
>>> oEditor.GetObjectsInGroup
>>> oEditor.GetModelBoundingBox

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_group_bounding_box(group=1)

```
Copy to clipboard