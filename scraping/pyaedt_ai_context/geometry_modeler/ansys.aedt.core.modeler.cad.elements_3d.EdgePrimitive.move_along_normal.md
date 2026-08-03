---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# move_along_normal 

EdgePrimitive.move_along_normal(_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move this edge.
This method moves an edge which belong to the same solid. 

Parameters: 
     

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
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()
>>> obj.move_along_normal(offset="1mm")

```
Copy to clipboard
# move_along_normal 

EdgePrimitive.move_along_normal(_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move this edge.
This method moves an edge which belong to the same solid. 

Parameters: 
     

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
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()
>>> obj.move_along_normal(offset="1mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal.rst.txt)

# move_along_normal 

EdgePrimitive.move_along_normal(_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move this edge.
This method moves an edge which belong to the same solid. 

Parameters: 
     

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
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()
>>> obj.move_along_normal(offset="1mm")

```
Copy to clipboard