---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.reference_cs_to_global.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# reference_cs_to_global 

Modeler3D.reference_cs_to_global(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")] 
    
Get the origin and quaternion defining the coordinate system in the global coordinates. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates of the origin and the quaternion defining the coordinate system in the global coordinates.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.reference_cs_to_global(coordinate_system="Global")

```
Copy to clipboard
# reference_cs_to_global 

Modeler3D.reference_cs_to_global(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")] 
    
Get the origin and quaternion defining the coordinate system in the global coordinates. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates of the origin and the quaternion defining the coordinate system in the global coordinates.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.reference_cs_to_global(coordinate_system="Global")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.reference_cs_to_global.rst.txt)

# reference_cs_to_global 

Modeler3D.reference_cs_to_global(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")] 
    
Get the origin and quaternion defining the coordinate system in the global coordinates. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
List of the `[x, y, z]` coordinates of the origin and the quaternion defining the coordinate system in the global coordinates.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.reference_cs_to_global(coordinate_system="Global")

```
Copy to clipboard