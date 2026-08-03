---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.purge_history.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# purge_history 

Modeler3D.purge_history(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Purge history objects from object names. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of object names to purge. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Convert new parts to non-model objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.PurgeHistory

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> cylinder1 = hfss.modeler.create_cylinder(orientation="X", origin=[5, 0, 0], radius=1, height=20)
>>> aedtapp.modeler.purge_history(assignment=cylinder1)

```
Copy to clipboard
# purge_history 

Modeler3D.purge_history(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Purge history objects from object names. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of object names to purge. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Convert new parts to non-model objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.PurgeHistory

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> cylinder1 = hfss.modeler.create_cylinder(orientation="X", origin=[5, 0, 0], radius=1, height=20)
>>> aedtapp.modeler.purge_history(assignment=cylinder1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.purge_history.rst.txt)

# purge_history 

Modeler3D.purge_history(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Purge history objects from object names. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of object names to purge. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Convert new parts to non-model objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.PurgeHistory

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> cylinder1 = hfss.modeler.create_cylinder(orientation="X", origin=[5, 0, 0], radius=1, height=20)
>>> aedtapp.modeler.purge_history(assignment=cylinder1)

```
Copy to clipboard