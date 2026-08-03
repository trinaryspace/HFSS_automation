---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.invert_cs.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# invert_cs 

Modeler3D.invert_cs(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_, _to_global : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")] 
    
Get the inverse translation and the conjugate quaternion of the input coordinate system.
By defining a new coordinate system with this information, the reference coordinate system of the input coordinate system is obtained. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. A `CoordinateSystem` object can also be used. 

**to_global**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to compute the inverse transformation of the input coordinate system with respect to the global coordinate system. The default is `False`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates of the origin and the quaternion defining the coordinate system.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.invert_cs(coordinate_system="Global")

```
Copy to clipboard
# invert_cs 

Modeler3D.invert_cs(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_, _to_global : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")] 
    
Get the inverse translation and the conjugate quaternion of the input coordinate system.
By defining a new coordinate system with this information, the reference coordinate system of the input coordinate system is obtained. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. A `CoordinateSystem` object can also be used. 

**to_global**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to compute the inverse transformation of the input coordinate system with respect to the global coordinate system. The default is `False`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates of the origin and the quaternion defining the coordinate system.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.invert_cs(coordinate_system="Global")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.invert_cs.rst.txt)

# invert_cs 

Modeler3D.invert_cs(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_, _to_global : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")] 
    
Get the inverse translation and the conjugate quaternion of the input coordinate system.
By defining a new coordinate system with this information, the reference coordinate system of the input coordinate system is obtained. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. A `CoordinateSystem` object can also be used. 

**to_global**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to compute the inverse transformation of the input coordinate system with respect to the global coordinate system. The default is `False`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates of the origin and the quaternion defining the coordinate system.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.invert_cs(coordinate_system="Global")

```
Copy to clipboard