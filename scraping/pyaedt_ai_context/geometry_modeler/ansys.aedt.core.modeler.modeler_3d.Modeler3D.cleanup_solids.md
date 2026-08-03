---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.cleanup_solids.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# cleanup_solids 

Modeler3D.cleanup_solids() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Clean up solids that no longer exist in the modeler because they were removed by previous operations.
This method also updates object IDs that may have changed via a modeler operation such as `ansys.aedt.core.modeler.Model3D.Modeler3D.unite()` or `ansys.aedt.core.modeler.Model2D.Modeler2D.unite()`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of updated object IDs.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.cleanup_solids()

```
Copy to clipboard
# cleanup_solids 

Modeler3D.cleanup_solids() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Clean up solids that no longer exist in the modeler because they were removed by previous operations.
This method also updates object IDs that may have changed via a modeler operation such as `ansys.aedt.core.modeler.Model3D.Modeler3D.unite()` or `ansys.aedt.core.modeler.Model2D.Modeler2D.unite()`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of updated object IDs.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.cleanup_solids()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.cleanup_solids.rst.txt)

# cleanup_solids 

Modeler3D.cleanup_solids() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Clean up solids that no longer exist in the modeler because they were removed by previous operations.
This method also updates object IDs that may have changed via a modeler operation such as `ansys.aedt.core.modeler.Model3D.Modeler3D.unite()` or `ansys.aedt.core.modeler.Model2D.Modeler2D.unite()`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of updated object IDs.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.cleanup_solids()

```
Copy to clipboard