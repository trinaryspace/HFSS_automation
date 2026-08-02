---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_edge_vertices.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_edge_vertices 

Modeler2D.get_edge_vertices(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the vertex IDs of a given edge ID or edge name. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Object ID or object name, which is available using the methods `ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D.get_object_vertices()` or `ansys.aedt.core.modeler.cad.primitives_2d.Primitives2D.get_object_vertices()`. 

Returns: 
     

`List`
    
List of vertex IDs.
References

```
>>> oEditor.GetVertexIDsFromEdge

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edge_vertices(assignment="Box1")

```
Copy to clipboard
# get_edge_vertices 

Modeler2D.get_edge_vertices(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the vertex IDs of a given edge ID or edge name. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Object ID or object name, which is available using the methods `ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D.get_object_vertices()` or `ansys.aedt.core.modeler.cad.primitives_2d.Primitives2D.get_object_vertices()`. 

Returns: 
     

`List`
    
List of vertex IDs.
References

```
>>> oEditor.GetVertexIDsFromEdge

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edge_vertices(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_edge_vertices.rst.txt)

# get_edge_vertices 

Modeler2D.get_edge_vertices(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the vertex IDs of a given edge ID or edge name. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Object ID or object name, which is available using the methods `ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D.get_object_vertices()` or `ansys.aedt.core.modeler.cad.primitives_2d.Primitives2D.get_object_vertices()`. 

Returns: 
     

`List`
    
List of vertex IDs.
References

```
>>> oEditor.GetVertexIDsFromEdge

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edge_vertices(assignment="Box1")

```
Copy to clipboard