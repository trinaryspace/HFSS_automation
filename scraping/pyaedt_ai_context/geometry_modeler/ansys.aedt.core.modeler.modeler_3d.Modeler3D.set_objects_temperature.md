---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.set_objects_temperature.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# set_objects_temperature 

Modeler3D.set_objects_temperature(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _ambient_temperature : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _create_project_var : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign temperatures to objects.
The materials assigned to the objects must have a thermal modifier. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**ambient_temperature**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Ambient temperature. The default is `22`. 

**create_project_var**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create a project variable for the ambient temperature. The default is `False`. If `True,` `$AmbientTemp` is created. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetObjectTemperature

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.set_objects_temperature(assignment="Box1")

```
Copy to clipboard
# set_objects_temperature 

Modeler3D.set_objects_temperature(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _ambient_temperature : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _create_project_var : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign temperatures to objects.
The materials assigned to the objects must have a thermal modifier. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**ambient_temperature**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Ambient temperature. The default is `22`. 

**create_project_var**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create a project variable for the ambient temperature. The default is `False`. If `True,` `$AmbientTemp` is created. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetObjectTemperature

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.set_objects_temperature(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.set_objects_temperature.rst.txt)

# set_objects_temperature 

Modeler3D.set_objects_temperature(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _ambient_temperature : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _create_project_var : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Assign temperatures to objects.
The materials assigned to the objects must have a thermal modifier. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects. 

**ambient_temperature**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Ambient temperature. The default is `22`. 

**create_project_var**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create a project variable for the ambient temperature. The default is `False`. If `True,` `$AmbientTemp` is created. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetObjectTemperature

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.set_objects_temperature(assignment="Box1")

```
Copy to clipboard