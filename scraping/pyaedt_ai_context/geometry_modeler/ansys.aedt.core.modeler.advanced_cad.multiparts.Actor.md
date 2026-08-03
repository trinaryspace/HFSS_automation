---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Actor 

class ansys.aedt.core.modeler.advanced_cad.multiparts.Actor(_actor_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = '0'_, _relative_cs_name =None_) 
    
Provides an instance of an actor.
This class is derived from [`MultiPartComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent").
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**actor_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the definition of the person. This can be changed later in the `Person` class definition. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Speed of the person in the X-direction. The default is `0``. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import Actor
>>> actor = Actor(r"C:\temp\actors")
>>> actor.speed_name
'actors_speed'

```
Copy to clipboard
Methods  
| [`Actor.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`Actor.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Actor.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Actor.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Actor.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index")  | Number of multi-part components.  |  
| [`Actor.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units")  | Value for modeler units.  |  
| [`Actor.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name")  | Unique instance name.  |  
| [`Actor.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset")  | Offset values for the multi-part component.  |  
| [`Actor.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Actor.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name")  | X-axis offset name.  |  
| [`Actor.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name")  | Y-axis offset name.  |  
| [`Actor.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name")  | Z-axis offset name.  |  
| [`Actor.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch")  | Pitch variable value.  |  
| [`Actor.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name")  | Pitch variable name.  |  
| [`Actor.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir")  | Shortcut for dir(self).  |  
| [`Actor.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll")  | Roll variable value.  |  
| [`Actor.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name")  | Roll variable name.  |  
| [`Actor.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression")  | Speed variable expression.  |  
| [`Actor.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name")  | Speed variable name.  |  
| [`Actor.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs")  | Global coordinate system.  |  
| [`Actor.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw")  | Yaw variable value.  |  
| [`Actor.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name")  | Yaw variable name.  |  
# Actor 

class ansys.aedt.core.modeler.advanced_cad.multiparts.Actor(_actor_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = '0'_, _relative_cs_name =None_) 
    
Provides an instance of an actor.
This class is derived from [`MultiPartComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent").
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**actor_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the definition of the person. This can be changed later in the `Person` class definition. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Speed of the person in the X-direction. The default is `0``. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import Actor
>>> actor = Actor(r"C:\temp\actors")
>>> actor.speed_name
'actors_speed'

```
Copy to clipboard
Methods  
| [`Actor.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`Actor.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Actor.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Actor.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Actor.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index")  | Number of multi-part components.  |  
| [`Actor.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units")  | Value for modeler units.  |  
| [`Actor.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name")  | Unique instance name.  |  
| [`Actor.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset")  | Offset values for the multi-part component.  |  
| [`Actor.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Actor.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name")  | X-axis offset name.  |  
| [`Actor.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name")  | Y-axis offset name.  |  
| [`Actor.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name")  | Z-axis offset name.  |  
| [`Actor.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch")  | Pitch variable value.  |  
| [`Actor.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name")  | Pitch variable name.  |  
| [`Actor.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir")  | Shortcut for dir(self).  |  
| [`Actor.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll")  | Roll variable value.  |  
| [`Actor.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name")  | Roll variable name.  |  
| [`Actor.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression")  | Speed variable expression.  |  
| [`Actor.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name")  | Speed variable name.  |  
| [`Actor.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs")  | Global coordinate system.  |  
| [`Actor.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw")  | Yaw variable value.  |  
| [`Actor.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.rst.txt)

# Actor 

class ansys.aedt.core.modeler.advanced_cad.multiparts.Actor(_actor_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = '0'_, _relative_cs_name =None_) 
    
Provides an instance of an actor.
This class is derived from [`MultiPartComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent").
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**actor_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the definition of the person. This can be changed later in the `Person` class definition. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Speed of the person in the X-direction. The default is `0``. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import Actor
>>> actor = Actor(r"C:\temp\actors")
>>> actor.speed_name
'actors_speed'

```
Copy to clipboard
Methods  
| [`Actor.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`Actor.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Actor.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Actor.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Actor.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.index")  | Number of multi-part components.  |  
| [`Actor.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.modeler_units")  | Value for modeler units.  |  
| [`Actor.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.name")  | Unique instance name.  |  
| [`Actor.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset")  | Offset values for the multi-part component.  |  
| [`Actor.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Actor.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_x_name")  | X-axis offset name.  |  
| [`Actor.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_y_name")  | Y-axis offset name.  |  
| [`Actor.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.offset_z_name")  | Z-axis offset name.  |  
| [`Actor.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch")  | Pitch variable value.  |  
| [`Actor.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.pitch_name")  | Pitch variable name.  |  
| [`Actor.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.public_dir")  | Shortcut for dir(self).  |  
| [`Actor.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll")  | Roll variable value.  |  
| [`Actor.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.roll_name")  | Roll variable name.  |  
| [`Actor.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_expression")  | Speed variable expression.  |  
| [`Actor.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.speed_name")  | Speed variable name.  |  
| [`Actor.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.use_global_cs")  | Global coordinate system.  |  
| [`Actor.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw")  | Yaw variable value.  |  
| [`Actor.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Actor.yaw_name")  | Yaw variable name.  |