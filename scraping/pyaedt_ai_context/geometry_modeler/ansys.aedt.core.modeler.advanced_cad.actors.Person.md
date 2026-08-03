---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Person 

class ansys.aedt.core.modeler.advanced_cad.actors.Person(_actor_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0'_, _stride : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.8meters'_, _relative_cs_name =None_) 
    
Provides an instance of a person.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction of the person coordinate system. 

Parameters: 
     

**actor_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the definition of the person. This can be changed later in the [`Person`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.html#ansys.aedt.core.modeler.advanced_cad.actors.Person "ansys.aedt.core.modeler.advanced_cad.actors.Person") class definition. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the person in the X-axis direction. The default is `"0"`. 

**stride**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Stride length of the person. The default is “0.8meters”. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Person
>>> person = Person(r"C:\temp\actors\person", speed="1m_per_sec", stride="0.8meters")
>>> person.stride
'0.8meters'

```
Copy to clipboard
Methods  
| [`Person.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.insert "ansys.aedt.core.modeler.advanced_cad.actors.Person.insert")(app[, motion])  | Insert the person in HFSS SBR+.  |  
| --- | --- |  
| [`Person.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Person.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.start "ansys.aedt.core.modeler.advanced_cad.actors.Person.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Person.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Person.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.index "ansys.aedt.core.modeler.advanced_cad.actors.Person.index")  | Number of multi-part components.  |  
| [`Person.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units")  | Value for modeler units.  |  
| [`Person.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.name "ansys.aedt.core.modeler.advanced_cad.actors.Person.name")  | Unique instance name.  |  
| [`Person.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset")  | Offset values for the multi-part component.  |  
| [`Person.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Person.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name")  | X-axis offset name.  |  
| [`Person.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name")  | Y-axis offset name.  |  
| [`Person.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name")  | Z-axis offset name.  |  
| [`Person.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch")  | Pitch variable value.  |  
| [`Person.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name")  | Pitch variable name.  |  
| [`Person.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir")  | Shortcut for dir(self).  |  
| [`Person.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.roll "ansys.aedt.core.modeler.advanced_cad.actors.Person.roll")  | Roll variable value.  |  
| [`Person.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name")  | Roll variable name.  |  
| [`Person.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression")  | Speed variable expression.  |  
| [`Person.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name")  | Speed variable name.  |  
| [`Person.stride`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.stride.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.stride "ansys.aedt.core.modeler.advanced_cad.actors.Person.stride")  | Stride in meters.  |  
| [`Person.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs")  | Global coordinate system.  |  
| [`Person.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw")  | Yaw variable value.  |  
| [`Person.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name")  | Yaw variable name.  |  
# Person 

class ansys.aedt.core.modeler.advanced_cad.actors.Person(_actor_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0'_, _stride : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.8meters'_, _relative_cs_name =None_) 
    
Provides an instance of a person.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction of the person coordinate system. 

Parameters: 
     

**actor_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the definition of the person. This can be changed later in the [`Person`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.html#ansys.aedt.core.modeler.advanced_cad.actors.Person "ansys.aedt.core.modeler.advanced_cad.actors.Person") class definition. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the person in the X-axis direction. The default is `"0"`. 

**stride**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Stride length of the person. The default is “0.8meters”. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Person
>>> person = Person(r"C:\temp\actors\person", speed="1m_per_sec", stride="0.8meters")
>>> person.stride
'0.8meters'

```
Copy to clipboard
Methods  
| [`Person.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.insert "ansys.aedt.core.modeler.advanced_cad.actors.Person.insert")(app[, motion])  | Insert the person in HFSS SBR+.  |  
| --- | --- |  
| [`Person.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Person.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.start "ansys.aedt.core.modeler.advanced_cad.actors.Person.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Person.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Person.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.index "ansys.aedt.core.modeler.advanced_cad.actors.Person.index")  | Number of multi-part components.  |  
| [`Person.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units")  | Value for modeler units.  |  
| [`Person.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.name "ansys.aedt.core.modeler.advanced_cad.actors.Person.name")  | Unique instance name.  |  
| [`Person.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset")  | Offset values for the multi-part component.  |  
| [`Person.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Person.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name")  | X-axis offset name.  |  
| [`Person.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name")  | Y-axis offset name.  |  
| [`Person.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name")  | Z-axis offset name.  |  
| [`Person.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch")  | Pitch variable value.  |  
| [`Person.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name")  | Pitch variable name.  |  
| [`Person.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir")  | Shortcut for dir(self).  |  
| [`Person.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.roll "ansys.aedt.core.modeler.advanced_cad.actors.Person.roll")  | Roll variable value.  |  
| [`Person.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name")  | Roll variable name.  |  
| [`Person.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression")  | Speed variable expression.  |  
| [`Person.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name")  | Speed variable name.  |  
| [`Person.stride`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.stride.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.stride "ansys.aedt.core.modeler.advanced_cad.actors.Person.stride")  | Stride in meters.  |  
| [`Person.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs")  | Global coordinate system.  |  
| [`Person.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw")  | Yaw variable value.  |  
| [`Person.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.rst.txt)

# Person 

class ansys.aedt.core.modeler.advanced_cad.actors.Person(_actor_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0'_, _stride : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.8meters'_, _relative_cs_name =None_) 
    
Provides an instance of a person.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction of the person coordinate system. 

Parameters: 
     

**actor_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the definition of the person. This can be changed later in the [`Person`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.html#ansys.aedt.core.modeler.advanced_cad.actors.Person "ansys.aedt.core.modeler.advanced_cad.actors.Person") class definition. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the person in the X-axis direction. The default is `"0"`. 

**stride**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Stride length of the person. The default is “0.8meters”. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Person
>>> person = Person(r"C:\temp\actors\person", speed="1m_per_sec", stride="0.8meters")
>>> person.stride
'0.8meters'

```
Copy to clipboard
Methods  
| [`Person.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.insert "ansys.aedt.core.modeler.advanced_cad.actors.Person.insert")(app[, motion])  | Insert the person in HFSS SBR+.  |  
| --- | --- |  
| [`Person.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Person.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Person.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.start "ansys.aedt.core.modeler.advanced_cad.actors.Person.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Person.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Person.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.index "ansys.aedt.core.modeler.advanced_cad.actors.Person.index")  | Number of multi-part components.  |  
| [`Person.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Person.modeler_units")  | Value for modeler units.  |  
| [`Person.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.name "ansys.aedt.core.modeler.advanced_cad.actors.Person.name")  | Unique instance name.  |  
| [`Person.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset")  | Offset values for the multi-part component.  |  
| [`Person.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Person.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_x_name")  | X-axis offset name.  |  
| [`Person.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_y_name")  | Y-axis offset name.  |  
| [`Person.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.offset_z_name")  | Z-axis offset name.  |  
| [`Person.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch")  | Pitch variable value.  |  
| [`Person.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.pitch_name")  | Pitch variable name.  |  
| [`Person.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Person.public_dir")  | Shortcut for dir(self).  |  
| [`Person.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.roll "ansys.aedt.core.modeler.advanced_cad.actors.Person.roll")  | Roll variable value.  |  
| [`Person.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.roll_name")  | Roll variable name.  |  
| [`Person.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_expression")  | Speed variable expression.  |  
| [`Person.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.speed_name")  | Speed variable name.  |  
| [`Person.stride`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.stride.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.stride "ansys.aedt.core.modeler.advanced_cad.actors.Person.stride")  | Stride in meters.  |  
| [`Person.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Person.use_global_cs")  | Global coordinate system.  |  
| [`Person.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw")  | Yaw variable value.  |  
| [`Person.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Person.yaw_name")  | Yaw variable name.  |