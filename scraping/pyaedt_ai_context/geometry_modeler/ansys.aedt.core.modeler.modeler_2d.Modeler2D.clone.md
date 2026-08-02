---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.clone.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# clone 

Modeler2D.clone(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)"), [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] 
    
Clone objects from a list of object IDs. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of object IDs. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed. 

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of objects cloned when successful.
References

```
>>> oEditor.Copy
>>> oEditor.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.clone(assignment="Box1")

```
Copy to clipboard
# clone 

Modeler2D.clone(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)"), [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] 
    
Clone objects from a list of object IDs. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of object IDs. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed. 

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of objects cloned when successful.
References

```
>>> oEditor.Copy
>>> oEditor.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.clone(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.clone.rst.txt)

# clone 

Modeler2D.clone(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)"), [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] 
    
Clone objects from a list of object IDs. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of object IDs. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed. 

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of objects cloned when successful.
References

```
>>> oEditor.Copy
>>> oEditor.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.clone(assignment="Box1")

```
Copy to clipboard