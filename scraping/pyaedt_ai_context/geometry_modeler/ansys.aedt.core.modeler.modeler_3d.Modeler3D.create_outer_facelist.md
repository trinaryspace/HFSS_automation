---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_outer_facelist.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_outer_facelist 

Modeler3D.create_outer_facelist(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'outer_faces'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a face list from a list of outer objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of outer objects. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new list. The default is `"outer_faces"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_outer_facelist(assignment="Box1")

```
Copy to clipboard
# create_outer_facelist 

Modeler3D.create_outer_facelist(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'outer_faces'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a face list from a list of outer objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of outer objects. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new list. The default is `"outer_faces"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_outer_facelist(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_outer_facelist.rst.txt)

# create_outer_facelist 

Modeler3D.create_outer_facelist(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'outer_faces'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a face list from a list of outer objects. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of outer objects. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the new list. The default is `"outer_faces"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_outer_facelist(assignment="Box1")

```
Copy to clipboard