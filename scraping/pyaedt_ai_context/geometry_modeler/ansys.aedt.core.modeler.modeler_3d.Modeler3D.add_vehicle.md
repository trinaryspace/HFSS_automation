---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.add_vehicle.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_vehicle 

Modeler3D.add_vehicle(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Vehicle](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Moving Vehicle Multipart from 3D Components.
It requires a json file in the folder containing vehicle infos. An example json file follows:
> 
```
{
    "name": "vehicle3",
    "version": 1,
    "type":"mustang",
    "class":"vehicle",
    "xlim":["-1.94","2.8"],
    "ylim":["-.91",".91"],
    "parts": {
        "wheels_front": {
            "comp_name": "wheels_front.a3dcomp",
            "rotation_cs":["1.8970271810532" ,"0" ,"0.34809664860487"],
            "tire_radius":"0.349",
            "rotation_axis":"Y"
            },
        "wheels_rear": {
            "comp_name": "wheels_rear.a3dcomp",
            "rotation_cs":["-0.82228746728897" ,"0","0.34809664860487"],
            "tire_radius":"0.349",
            "rotation_axis":"Y"
            },
        "body": {
            "comp_name": "body.a3dcomp",
            "rotation_cs":null,
            "tire_radius":null,
            "rotation_axis":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file). 

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

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Relative CS Name of the actor. `None` for Global CS. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Vehicle name. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Vehicle`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_vehicle(input_dir="example.txt")

```
Copy to clipboard
# add_vehicle 

Modeler3D.add_vehicle(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Vehicle](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Moving Vehicle Multipart from 3D Components.
It requires a json file in the folder containing vehicle infos. An example json file follows:
> 
```
{
    "name": "vehicle3",
    "version": 1,
    "type":"mustang",
    "class":"vehicle",
    "xlim":["-1.94","2.8"],
    "ylim":["-.91",".91"],
    "parts": {
        "wheels_front": {
            "comp_name": "wheels_front.a3dcomp",
            "rotation_cs":["1.8970271810532" ,"0" ,"0.34809664860487"],
            "tire_radius":"0.349",
            "rotation_axis":"Y"
            },
        "wheels_rear": {
            "comp_name": "wheels_rear.a3dcomp",
            "rotation_cs":["-0.82228746728897" ,"0","0.34809664860487"],
            "tire_radius":"0.349",
            "rotation_axis":"Y"
            },
        "body": {
            "comp_name": "body.a3dcomp",
            "rotation_cs":null,
            "tire_radius":null,
            "rotation_axis":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file). 

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

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Relative CS Name of the actor. `None` for Global CS. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Vehicle name. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Vehicle`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_vehicle(input_dir="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.add_vehicle.rst.txt)

# add_vehicle 

Modeler3D.add_vehicle(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Vehicle](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Moving Vehicle Multipart from 3D Components.
It requires a json file in the folder containing vehicle infos. An example json file follows:
> 
```
{
    "name": "vehicle3",
    "version": 1,
    "type":"mustang",
    "class":"vehicle",
    "xlim":["-1.94","2.8"],
    "ylim":["-.91",".91"],
    "parts": {
        "wheels_front": {
            "comp_name": "wheels_front.a3dcomp",
            "rotation_cs":["1.8970271810532" ,"0" ,"0.34809664860487"],
            "tire_radius":"0.349",
            "rotation_axis":"Y"
            },
        "wheels_rear": {
            "comp_name": "wheels_rear.a3dcomp",
            "rotation_cs":["-0.82228746728897" ,"0","0.34809664860487"],
            "tire_radius":"0.349",
            "rotation_axis":"Y"
            },
        "body": {
            "comp_name": "body.a3dcomp",
            "rotation_cs":null,
            "tire_radius":null,
            "rotation_axis":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor directory. It must contain a json settings file and a 3dcomponent (`.a3dcomp` file). 

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

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Relative CS Name of the actor. `None` for Global CS. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Vehicle name. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Vehicle`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_vehicle(input_dir="example.txt")

```
Copy to clipboard