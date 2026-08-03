---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# delete 

CoordinateSystem.delete() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete the coordinate system. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Delete all coordinate systems in the design.

```
>>> from ansys.aedt.core import Maxwell2d
>>> app = Maxwell2d()
>>> cs_copy = [i for i in app.modeler.coordinate_systems]
>>> [i.delete() for i in cs_copy]

```
Copy to clipboard
# delete 

CoordinateSystem.delete() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete the coordinate system. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Delete all coordinate systems in the design.

```
>>> from ansys.aedt.core import Maxwell2d
>>> app = Maxwell2d()
>>> cs_copy = [i for i in app.modeler.coordinate_systems]
>>> [i.delete() for i in cs_copy]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete.rst.txt)

# delete 

CoordinateSystem.delete() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete the coordinate system. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples
Delete all coordinate systems in the design.

```
>>> from ansys.aedt.core import Maxwell2d
>>> app = Maxwell2d()
>>> cs_copy = [i for i in app.modeler.coordinate_systems]
>>> [i.delete() for i in cs_copy]

```
Copy to clipboard