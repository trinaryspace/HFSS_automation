---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.duplicate_coordinate_system_to_global.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# duplicate_coordinate_system_to_global 

Modeler2D.duplicate_coordinate_system_to_global(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") 
    
Create a duplicate coordinate system referenced to the global coordinate system.
Having this coordinate system referenced to the global coordinate system removes all nested coordinate system dependencies. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.CoordinateSystem`
    
Created coordinate system.
References

```
>>> oEditor.CreateRelativeCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.duplicate_coordinate_system_to_global(coordinate_system="Global")

```
Copy to clipboard
# duplicate_coordinate_system_to_global 

Modeler2D.duplicate_coordinate_system_to_global(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") 
    
Create a duplicate coordinate system referenced to the global coordinate system.
Having this coordinate system referenced to the global coordinate system removes all nested coordinate system dependencies. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.CoordinateSystem`
    
Created coordinate system.
References

```
>>> oEditor.CreateRelativeCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.duplicate_coordinate_system_to_global(coordinate_system="Global")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.duplicate_coordinate_system_to_global.rst.txt)

# duplicate_coordinate_system_to_global 

Modeler2D.duplicate_coordinate_system_to_global(_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") 
    
Create a duplicate coordinate system referenced to the global coordinate system.
Having this coordinate system referenced to the global coordinate system removes all nested coordinate system dependencies. 

Parameters: 
     

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `CoordinateSystem` 
    
Name of the destination reference system. The `CoordinateSystem` object can also be used. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.CoordinateSystem`
    
Created coordinate system.
References

```
>>> oEditor.CreateRelativeCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.duplicate_coordinate_system_to_global(coordinate_system="Global")

```
Copy to clipboard