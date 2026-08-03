---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.add_environment.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_environment 

Modeler3D.add_environment(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _global_offset =[0, 0, 0]_, _yaw : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _pitch : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _roll : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Environment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add an Environment Multipart Component from JSON file.
> 
```
{
    "name": "open1",
    "version": 1,
    "class":"environment",
    "xlim":["-5","95"],
    "ylim":["-60","60"],
    "parts": {
        "open_area": {
            "comp_name": "open1.a3dcomp",
            "offset":null,
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null,
            "duplicate_number":null,
            "duplicate_vector":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file). 

**global_offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset from Global Coordinate System [x,y,z] in meters. 

**yaw**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw Rotation from Global Coordinate System in deg. 

**pitch**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch Rotation from Global Coordinate System in deg. 

**roll**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll Rotation from Global Coordinate System in deg. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

Returns: 
     

`ansys.aedt.core.modeler.multiparts.Environment`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_environment(input_dir="example.txt")

```
Copy to clipboard
# add_environment 

Modeler3D.add_environment(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _global_offset =[0, 0, 0]_, _yaw : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _pitch : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _roll : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Environment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add an Environment Multipart Component from JSON file.
> 
```
{
    "name": "open1",
    "version": 1,
    "class":"environment",
    "xlim":["-5","95"],
    "ylim":["-60","60"],
    "parts": {
        "open_area": {
            "comp_name": "open1.a3dcomp",
            "offset":null,
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null,
            "duplicate_number":null,
            "duplicate_vector":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file). 

**global_offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset from Global Coordinate System [x,y,z] in meters. 

**yaw**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw Rotation from Global Coordinate System in deg. 

**pitch**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch Rotation from Global Coordinate System in deg. 

**roll**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll Rotation from Global Coordinate System in deg. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

Returns: 
     

`ansys.aedt.core.modeler.multiparts.Environment`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_environment(input_dir="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.add_environment.rst.txt)

# add_environment 

Modeler3D.add_environment(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _global_offset =[0, 0, 0]_, _yaw : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _pitch : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _roll : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Environment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add an Environment Multipart Component from JSON file.
> 
```
{
    "name": "open1",
    "version": 1,
    "class":"environment",
    "xlim":["-5","95"],
    "ylim":["-60","60"],
    "parts": {
        "open_area": {
            "comp_name": "open1.a3dcomp",
            "offset":null,
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null,
            "duplicate_number":null,
            "duplicate_vector":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file). 

**global_offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset from Global Coordinate System [x,y,z] in meters. 

**yaw**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw Rotation from Global Coordinate System in deg. 

**pitch**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch Rotation from Global Coordinate System in deg. 

**roll**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll Rotation from Global Coordinate System in deg. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

Returns: 
     

`ansys.aedt.core.modeler.multiparts.Environment`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_environment(input_dir="example.txt")

```
Copy to clipboard