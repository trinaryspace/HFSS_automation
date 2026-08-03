---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_vertices_of_line.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_vertices_of_line 

Modeler3D.get_vertices_of_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Generate a list of vertex positions for a line object from AEDT in model units. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the line object in AEDT. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the `[x, y, (z)]` coordinates for the 2D or 3D line object.
References

```
>>> oEditor.GetVertexIDsFromObject

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_vertices_of_line(assignment="Box1")

```
Copy to clipboard
# get_vertices_of_line 

Modeler3D.get_vertices_of_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Generate a list of vertex positions for a line object from AEDT in model units. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the line object in AEDT. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the `[x, y, (z)]` coordinates for the 2D or 3D line object.
References

```
>>> oEditor.GetVertexIDsFromObject

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_vertices_of_line(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_vertices_of_line.rst.txt)

# get_vertices_of_line 

Modeler3D.get_vertices_of_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Generate a list of vertex positions for a line object from AEDT in model units. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the line object in AEDT. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the `[x, y, (z)]` coordinates for the 2D or 3D line object.
References

```
>>> oEditor.GetVertexIDsFromObject

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_vertices_of_line(assignment="Box1")

```
Copy to clipboard