---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.add_person.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_person 

Modeler3D.add_person(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coordinate_system =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Person](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.html#ansys.aedt.core.modeler.advanced_cad.actors.Person "ansys.aedt.core.modeler.advanced_cad.actors.Person") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Walking Person Multipart from 3D Components.
It requires a json file in the folder containing person infos. An example json file follows:
> 
```
{
    "name": "person3",
    "version": 1,
    "class":"person",
    "stride":"0.76meter",
    "xlim":["-.43",".43"],
    "ylim":["-.25",".25"],
    "parts": {
        "arm_left": {
            "comp_name": "arm_left.a3dcomp",
            "rotation_cs":["-.04","0","1.37"],
            "rotation":"-30deg",
            "compensation_angle":"-15deg",
            "rotation_axis":"Y"
            },
        "arm_right": {
            "comp_name": "arm_right.a3dcomp",
            "rotation_cs":["0","0","1.37"],
            "rotation":"30deg",
            "compensation_angle":"30deg",
            "rotation_axis":"Y"
            },
        "leg_left": {
            "comp_name": "leg_left.a3dcomp",
            "rotation_cs":["0","0",".9"],
            "rotation":"20deg",
            "compensation_angle":"22.5deg",
            "rotation_axis":"Y"
            },
        "leg_right": {
            "comp_name": "leg_right.a3dcomp",
            "rotation_cs":["-.04","0",".9375"],
            "rotation":"-20deg",
            "compensation_angle":"-22.5deg",
            "rotation_axis":"Y"
            },
        "torso": {
            "comp_name": "torso.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "compensation_angle":null,
            "rotation_axis":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor folder. It must contain a json settings file and a 3dcomponent (.a3dcomp). 

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

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
If provided, it overrides the actor name in the JSON. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Person`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_person(input_dir="example.txt")

```
Copy to clipboard
# add_person 

Modeler3D.add_person(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coordinate_system =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Person](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.html#ansys.aedt.core.modeler.advanced_cad.actors.Person "ansys.aedt.core.modeler.advanced_cad.actors.Person") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Walking Person Multipart from 3D Components.
It requires a json file in the folder containing person infos. An example json file follows:
> 
```
{
    "name": "person3",
    "version": 1,
    "class":"person",
    "stride":"0.76meter",
    "xlim":["-.43",".43"],
    "ylim":["-.25",".25"],
    "parts": {
        "arm_left": {
            "comp_name": "arm_left.a3dcomp",
            "rotation_cs":["-.04","0","1.37"],
            "rotation":"-30deg",
            "compensation_angle":"-15deg",
            "rotation_axis":"Y"
            },
        "arm_right": {
            "comp_name": "arm_right.a3dcomp",
            "rotation_cs":["0","0","1.37"],
            "rotation":"30deg",
            "compensation_angle":"30deg",
            "rotation_axis":"Y"
            },
        "leg_left": {
            "comp_name": "leg_left.a3dcomp",
            "rotation_cs":["0","0",".9"],
            "rotation":"20deg",
            "compensation_angle":"22.5deg",
            "rotation_axis":"Y"
            },
        "leg_right": {
            "comp_name": "leg_right.a3dcomp",
            "rotation_cs":["-.04","0",".9375"],
            "rotation":"-20deg",
            "compensation_angle":"-22.5deg",
            "rotation_axis":"Y"
            },
        "torso": {
            "comp_name": "torso.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "compensation_angle":null,
            "rotation_axis":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor folder. It must contain a json settings file and a 3dcomponent (.a3dcomp). 

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

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
If provided, it overrides the actor name in the JSON. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Person`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_person(input_dir="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.add_person.rst.txt)

# add_person 

Modeler3D.add_person(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _global_offset =[0, 0, 0]_, _yaw : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _pitch : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _roll : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coordinate_system =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Person](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.html#ansys.aedt.core.modeler.advanced_cad.actors.Person "ansys.aedt.core.modeler.advanced_cad.actors.Person") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a Walking Person Multipart from 3D Components.
It requires a json file in the folder containing person infos. An example json file follows:
> 
```
{
    "name": "person3",
    "version": 1,
    "class":"person",
    "stride":"0.76meter",
    "xlim":["-.43",".43"],
    "ylim":["-.25",".25"],
    "parts": {
        "arm_left": {
            "comp_name": "arm_left.a3dcomp",
            "rotation_cs":["-.04","0","1.37"],
            "rotation":"-30deg",
            "compensation_angle":"-15deg",
            "rotation_axis":"Y"
            },
        "arm_right": {
            "comp_name": "arm_right.a3dcomp",
            "rotation_cs":["0","0","1.37"],
            "rotation":"30deg",
            "compensation_angle":"30deg",
            "rotation_axis":"Y"
            },
        "leg_left": {
            "comp_name": "leg_left.a3dcomp",
            "rotation_cs":["0","0",".9"],
            "rotation":"20deg",
            "compensation_angle":"22.5deg",
            "rotation_axis":"Y"
            },
        "leg_right": {
            "comp_name": "leg_right.a3dcomp",
            "rotation_cs":["-.04","0",".9375"],
            "rotation":"-20deg",
            "compensation_angle":"-22.5deg",
            "rotation_axis":"Y"
            },
        "torso": {
            "comp_name": "torso.a3dcomp",
            "rotation_cs":null,
            "rotation":null,
            "compensation_angle":null,
            "rotation_axis":null
            }
    }
}

```
Copy to clipboard 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the actor folder. It must contain a json settings file and a 3dcomponent (.a3dcomp). 

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

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Relative CS Name of the actor. `None` for Global CS. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
If provided, it overrides the actor name in the JSON. 

Returns: 
     

`ansys.aedt.core.modeler.actors.Person`
    
References

```
>>> oEditor.Insert3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.add_person(input_dir="example.txt")

```
Copy to clipboard