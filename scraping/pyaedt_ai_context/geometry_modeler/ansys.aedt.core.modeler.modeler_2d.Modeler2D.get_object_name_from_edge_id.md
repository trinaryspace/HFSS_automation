---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_object_name_from_edge_id.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_object_name_from_edge_id 

Modeler2D.get_object_name_from_edge_id(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Retrieve the object name for a predefined edge ID. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the edge. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the edge if it exists, `False` otherwise.
References

```
>>> oEditor.GetEdgeIDsFromObject

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_object_name_from_edge_id(assignment="Box1")

```
Copy to clipboard
# get_object_name_from_edge_id 

Modeler2D.get_object_name_from_edge_id(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Retrieve the object name for a predefined edge ID. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the edge. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the edge if it exists, `False` otherwise.
References

```
>>> oEditor.GetEdgeIDsFromObject

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_object_name_from_edge_id(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_object_name_from_edge_id.rst.txt)

# get_object_name_from_edge_id 

Modeler2D.get_object_name_from_edge_id(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Retrieve the object name for a predefined edge ID. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
ID of the edge. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the edge if it exists, `False` otherwise.
References

```
>>> oEditor.GetEdgeIDsFromObject

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_object_name_from_edge_id(assignment="Box1")

```
Copy to clipboard