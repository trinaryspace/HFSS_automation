---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_bodynames_from_position.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_bodynames_from_position 

Modeler2D.get_bodynames_from_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _include_non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the names of the objects that are in contact with a given point. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the point. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units, such as `"m"`. The default is `None`, in which case the model units are used. 

**include_non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if include or not non model objects. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of object names.
References

```
>>> oEditor.GetBodyNamesByPosition

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_bodynames_from_position(position=[0, 0, 0])

```
Copy to clipboard
# get_bodynames_from_position 

Modeler2D.get_bodynames_from_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _include_non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the names of the objects that are in contact with a given point. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the point. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units, such as `"m"`. The default is `None`, in which case the model units are used. 

**include_non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if include or not non model objects. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of object names.
References

```
>>> oEditor.GetBodyNamesByPosition

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_bodynames_from_position(position=[0, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_bodynames_from_position.rst.txt)

# get_bodynames_from_position 

Modeler2D.get_bodynames_from_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _include_non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the names of the objects that are in contact with a given point. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the point. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units, such as `"m"`. The default is `None`, in which case the model units are used. 

**include_non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if include or not non model objects. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of object names.
References

```
>>> oEditor.GetBodyNamesByPosition

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_bodynames_from_position(position=[0, 0, 0])

```
Copy to clipboard