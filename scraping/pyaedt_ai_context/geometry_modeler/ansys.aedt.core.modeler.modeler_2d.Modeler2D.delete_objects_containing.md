---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.delete_objects_containing.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# delete_objects_containing 

Modeler2D.delete_objects_containing(_contained_string : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _case_sensitive : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete all objects with a given prefix. 

Parameters: 
     

**contained_string**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix in the names of the objects to delete. 

**case_sensitive**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the prefix is case sensitive. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.delete_objects_containing(contained_string=1)

```
Copy to clipboard
# delete_objects_containing 

Modeler2D.delete_objects_containing(_contained_string : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _case_sensitive : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete all objects with a given prefix. 

Parameters: 
     

**contained_string**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix in the names of the objects to delete. 

**case_sensitive**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the prefix is case sensitive. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.delete_objects_containing(contained_string=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.delete_objects_containing.rst.txt)

# delete_objects_containing 

Modeler2D.delete_objects_containing(_contained_string : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _case_sensitive : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete all objects with a given prefix. 

Parameters: 
     

**contained_string**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix in the names of the objects to delete. 

**case_sensitive**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the prefix is case sensitive. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.delete_objects_containing(contained_string=1)

```
Copy to clipboard