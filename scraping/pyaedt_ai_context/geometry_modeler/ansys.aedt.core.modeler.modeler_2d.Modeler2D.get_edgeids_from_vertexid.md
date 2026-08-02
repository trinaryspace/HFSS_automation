---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_edgeids_from_vertexid.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_edgeids_from_vertexid 

Modeler2D.get_edgeids_from_vertexid(_vertex : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve edge IDs for a vertex ID. 

Parameters: 
     

**vertex**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Vertex ID. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

Returns: 
     

`List`
    
List of edge IDs for the vertex ID.
References

```
>>> oEditor.GetEdgeIDsFromObject
>>> oEditor.GetVertexIDsFromEdge

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edgeids_from_vertexid(vertex=1, assignment="Box1")

```
Copy to clipboard
# get_edgeids_from_vertexid 

Modeler2D.get_edgeids_from_vertexid(_vertex : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve edge IDs for a vertex ID. 

Parameters: 
     

**vertex**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Vertex ID. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

Returns: 
     

`List`
    
List of edge IDs for the vertex ID.
References

```
>>> oEditor.GetEdgeIDsFromObject
>>> oEditor.GetVertexIDsFromEdge

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edgeids_from_vertexid(vertex=1, assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_edgeids_from_vertexid.rst.txt)

# get_edgeids_from_vertexid 

Modeler2D.get_edgeids_from_vertexid(_vertex : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve edge IDs for a vertex ID. 

Parameters: 
     

**vertex**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Vertex ID. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

Returns: 
     

`List`
    
List of edge IDs for the vertex ID.
References

```
>>> oEditor.GetEdgeIDsFromObject
>>> oEditor.GetVertexIDsFromEdge

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edgeids_from_vertexid(vertex=1, assignment="Box1")

```
Copy to clipboard