---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.delete_all_points.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# delete_all_points 

Modeler2D.delete_all_points() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete all points.
This method doesn’t rely on the PyAEDT object management and directly deletes all points in the modeler. This avoid issues with points created in AEDT which are renamed on the fly. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.GetPoints
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.delete_all_points()

```
Copy to clipboard
# delete_all_points 

Modeler2D.delete_all_points() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete all points.
This method doesn’t rely on the PyAEDT object management and directly deletes all points in the modeler. This avoid issues with points created in AEDT which are renamed on the fly. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.GetPoints
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.delete_all_points()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.delete_all_points.rst.txt)

# delete_all_points 

Modeler2D.delete_all_points() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete all points.
This method doesn’t rely on the PyAEDT object management and directly deletes all points in the modeler. This avoid issues with points created in AEDT which are renamed on the fly. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.GetPoints
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.delete_all_points()

```
Copy to clipboard