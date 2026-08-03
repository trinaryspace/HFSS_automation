---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.add_bird.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_bird 

Modeler3D.add_bird(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _flapping_rate : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 50_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → 'Bird' | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Bird Multipart from 3D Components.
It requires a json file in the folder containing bird infos. An example json file is showed here.
> 
```
{
    "name": "bird1",
    "version": 1,
    "class":"bird",
    "xlim":["-.7","2.75"],
    "ylim":["-1.2","1.2"],
    "parts": {
        "body": {
            "comp_name": "body.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        },
            "wing_right": {
            "comp_name": "wing_left.a3dcomp",
            "rotation_cs":[".001778" ,".00508" ,".00762"],
            "rotation":"-45deg",
            "rotation_axis":"X"
        },
            "wing_left": {
            "comp_name": "wing_right.a3dcomp",
            "rotation_cs":[".001778" ,"-.00508" ,".00762"],
            "rotation":"45deg",
            "rotation_axis":"X"
        },
            "tail": {
            "comp_name": "tail.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        },
            "beak": {
            "comp_name": "beak.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file) 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Object movement speed with time (m_per_sec). 

**global_offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset from Global Coordinate System [x,y,z] in meters. 

**yaw**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw Rotation from Global Coordinate System in deg. 

**pitch**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch Rotation from Global Coordinate System in deg. 

**roll**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll Rotation from Global Coordinate System in deg. 

**flapping_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Motion flapping rate in Hz. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Bird`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> bird_dir = "path/to/bird/directory"
>>> bird1 = app.modeler.add_bird(bird_dir,1.0,[19, 4, 3],120,-5,flapping_rate=30)

```
Copy to clipboard
# add_bird 

Modeler3D.add_bird(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _flapping_rate : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 50_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → 'Bird' | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Bird Multipart from 3D Components.
It requires a json file in the folder containing bird infos. An example json file is showed here.
> 
```
{
    "name": "bird1",
    "version": 1,
    "class":"bird",
    "xlim":["-.7","2.75"],
    "ylim":["-1.2","1.2"],
    "parts": {
        "body": {
            "comp_name": "body.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        },
            "wing_right": {
            "comp_name": "wing_left.a3dcomp",
            "rotation_cs":[".001778" ,".00508" ,".00762"],
            "rotation":"-45deg",
            "rotation_axis":"X"
        },
            "wing_left": {
            "comp_name": "wing_right.a3dcomp",
            "rotation_cs":[".001778" ,"-.00508" ,".00762"],
            "rotation":"45deg",
            "rotation_axis":"X"
        },
            "tail": {
            "comp_name": "tail.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        },
            "beak": {
            "comp_name": "beak.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file) 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Object movement speed with time (m_per_sec). 

**global_offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset from Global Coordinate System [x,y,z] in meters. 

**yaw**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw Rotation from Global Coordinate System in deg. 

**pitch**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch Rotation from Global Coordinate System in deg. 

**roll**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll Rotation from Global Coordinate System in deg. 

**flapping_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Motion flapping rate in Hz. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Bird`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> bird_dir = "path/to/bird/directory"
>>> bird1 = app.modeler.add_bird(bird_dir,1.0,[19, 4, 3],120,-5,flapping_rate=30)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.add_bird.rst.txt)

# add_bird 

Modeler3D.add_bird(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _flapping_rate : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 50_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → 'Bird' | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Bird Multipart from 3D Components.
It requires a json file in the folder containing bird infos. An example json file is showed here.
> 
```
{
    "name": "bird1",
    "version": 1,
    "class":"bird",
    "xlim":["-.7","2.75"],
    "ylim":["-1.2","1.2"],
    "parts": {
        "body": {
            "comp_name": "body.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        },
            "wing_right": {
            "comp_name": "wing_left.a3dcomp",
            "rotation_cs":[".001778" ,".00508" ,".00762"],
            "rotation":"-45deg",
            "rotation_axis":"X"
        },
            "wing_left": {
            "comp_name": "wing_right.a3dcomp",
            "rotation_cs":[".001778" ,"-.00508" ,".00762"],
            "rotation":"45deg",
            "rotation_axis":"X"
        },
            "tail": {
            "comp_name": "tail.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        },
            "beak": {
            "comp_name": "beak.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "rotation_axis":null
        }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file) 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Object movement speed with time (m_per_sec). 

**global_offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Offset from Global Coordinate System [x,y,z] in meters. 

**yaw**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw Rotation from Global Coordinate System in deg. 

**pitch**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch Rotation from Global Coordinate System in deg. 

**roll**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll Rotation from Global Coordinate System in deg. 

**flapping_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Motion flapping rate in Hz. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Bird`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> bird_dir = "path/to/bird/directory"
>>> bird1 = app.modeler.add_bird(bird_dir,1.0,[19, 4, 3],120,-5,flapping_rate=30)

```
Copy to clipboard