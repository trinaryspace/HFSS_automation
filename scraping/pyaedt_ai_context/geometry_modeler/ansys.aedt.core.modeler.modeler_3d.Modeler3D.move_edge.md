---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.move_edge.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# move_edge 

Modeler3D.move_edge(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move an input edge or a list of input edges of a specific object.
This method moves an edge or a list of edges which belong to the same solid. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Edge ID or list[[`ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive")] object or mixed. 

**offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset to apply in model units. The default is `1.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.MoveEdges

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.move_edge(assignment="Box1")

```
Copy to clipboard
# move_edge 

Modeler3D.move_edge(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move an input edge or a list of input edges of a specific object.
This method moves an edge or a list of edges which belong to the same solid. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Edge ID or list[[`ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive")] object or mixed. 

**offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset to apply in model units. The default is `1.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.MoveEdges

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.move_edge(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.move_edge.rst.txt)

# move_edge 

Modeler3D.move_edge(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move an input edge or a list of input edges of a specific object.
This method moves an edge or a list of edges which belong to the same solid. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of Edge ID or list[[`ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive")] object or mixed. 

**offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Offset to apply in model units. The default is `1.0`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.MoveEdges

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.move_edge(assignment="Box1")

```
Copy to clipboard