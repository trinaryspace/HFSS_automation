---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.global_to_cs.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# global_to_cs 

Modeler2D.global_to_cs(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Transform a point from the global coordinate system to another coordinate system. 

Parameters: 
     

**point**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates to transform. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the transformed `[x, y, z]` coordinates.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.global_to_cs(point=[1, 0, 0], coordinate_system="Global")

```
Copy to clipboard
# global_to_cs 

Modeler2D.global_to_cs(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Transform a point from the global coordinate system to another coordinate system. 

Parameters: 
     

**point**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates to transform. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the transformed `[x, y, z]` coordinates.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.global_to_cs(point=[1, 0, 0], coordinate_system="Global")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.global_to_cs.rst.txt)

# global_to_cs 

Modeler2D.global_to_cs(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Transform a point from the global coordinate system to another coordinate system. 

Parameters: 
     

**point**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates to transform. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of the transformed `[x, y, z]` coordinates.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.global_to_cs(point=[1, 0, 0], coordinate_system="Global")

```
Copy to clipboard