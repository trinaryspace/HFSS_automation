---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.set_working_coordinate_system.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# set_working_coordinate_system 

Modeler3D.set_working_coordinate_system(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the working coordinate system to another coordinate system. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `FaceCoordinateSystem`, `CoordinateSystem` 
    
Name of the coordinate system or `CoordinateSystem` object to set as the working coordinate system. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.SetWCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.set_working_coordinate_system(name="Global")

```
Copy to clipboard
# set_working_coordinate_system 

Modeler3D.set_working_coordinate_system(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the working coordinate system to another coordinate system. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `FaceCoordinateSystem`, `CoordinateSystem` 
    
Name of the coordinate system or `CoordinateSystem` object to set as the working coordinate system. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.SetWCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.set_working_coordinate_system(name="Global")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.set_working_coordinate_system.rst.txt)

# set_working_coordinate_system 

Modeler3D.set_working_coordinate_system(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the working coordinate system to another coordinate system. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `FaceCoordinateSystem`, `CoordinateSystem` 
    
Name of the coordinate system or `CoordinateSystem` object to set as the working coordinate system. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.SetWCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.set_working_coordinate_system(name="Global")

```
Copy to clipboard