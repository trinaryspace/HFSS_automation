---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.unite.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# unite 

Modeler3D.unite(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _purge : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _keep_originals : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Unite objects from a list. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of objects to unite. 

**purge**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Purge history after unite. Default is False. 

**keep_originals**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Keep original objects used for the operation. Default is False. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The united object that is the first in the list.
References

```
>>> oEditor.Unite

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.unite(assignment="Box1")

```
Copy to clipboard
# unite 

Modeler3D.unite(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _purge : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _keep_originals : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Unite objects from a list. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of objects to unite. 

**purge**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Purge history after unite. Default is False. 

**keep_originals**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Keep original objects used for the operation. Default is False. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The united object that is the first in the list.
References

```
>>> oEditor.Unite

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.unite(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.unite.rst.txt)

# unite 

Modeler3D.unite(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _purge : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _keep_originals : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Unite objects from a list. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of objects to unite. 

**purge**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Purge history after unite. Default is False. 

**keep_originals**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Keep original objects used for the operation. Default is False. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
The united object that is the first in the list.
References

```
>>> oEditor.Unite

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.unite(assignment="Box1")

```
Copy to clipboard