---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Bird 

class ansys.aedt.core.modeler.advanced_cad.actors.Bird(_bird_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_, _flapping_rate : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '50Hz'_, _relative_cs_name =None_) 
    
Provides an instance of a bird.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**bird_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the directory containing the definition of the bird. This can be changed later. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the bird. The default is `"2.0"`. 

**flapping_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Flapping rate. The default is `"50Hz"`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is``None``, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Bird
>>> bird = Bird(r"C:\temp\actors\bird", speed="2.0", flapping_rate="50Hz")
>>> bird

```
Copy to clipboard
Methods  
| [`Bird.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert "ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert")(app[, motion])  | Insert the bird in HFSS SBR+.  |  
| --- | --- |  
| [`Bird.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Bird.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.start "ansys.aedt.core.modeler.advanced_cad.actors.Bird.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Bird.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Bird.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.index "ansys.aedt.core.modeler.advanced_cad.actors.Bird.index")  | Number of multi-part components.  |  
| [`Bird.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units")  | Value for modeler units.  |  
| [`Bird.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.name")  | Unique instance name.  |  
| [`Bird.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset")  | Offset values for the multi-part component.  |  
| [`Bird.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Bird.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name")  | X-axis offset name.  |  
| [`Bird.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name")  | Y-axis offset name.  |  
| [`Bird.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name")  | Z-axis offset name.  |  
| [`Bird.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch")  | Pitch variable value.  |  
| [`Bird.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name")  | Pitch variable name.  |  
| [`Bird.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir")  | Shortcut for dir(self).  |  
| [`Bird.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll "ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll")  | Roll variable value.  |  
| [`Bird.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name")  | Roll variable name.  |  
| [`Bird.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression")  | Speed variable expression.  |  
| [`Bird.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name")  | Speed variable name.  |  
| [`Bird.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs")  | Global coordinate system.  |  
| [`Bird.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw")  | Yaw variable value.  |  
| [`Bird.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name")  | Yaw variable name.  |  
# Bird 

class ansys.aedt.core.modeler.advanced_cad.actors.Bird(_bird_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_, _flapping_rate : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '50Hz'_, _relative_cs_name =None_) 
    
Provides an instance of a bird.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**bird_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the directory containing the definition of the bird. This can be changed later. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the bird. The default is `"2.0"`. 

**flapping_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Flapping rate. The default is `"50Hz"`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is``None``, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Bird
>>> bird = Bird(r"C:\temp\actors\bird", speed="2.0", flapping_rate="50Hz")
>>> bird

```
Copy to clipboard
Methods  
| [`Bird.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert "ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert")(app[, motion])  | Insert the bird in HFSS SBR+.  |  
| --- | --- |  
| [`Bird.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Bird.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.start "ansys.aedt.core.modeler.advanced_cad.actors.Bird.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Bird.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Bird.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.index "ansys.aedt.core.modeler.advanced_cad.actors.Bird.index")  | Number of multi-part components.  |  
| [`Bird.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units")  | Value for modeler units.  |  
| [`Bird.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.name")  | Unique instance name.  |  
| [`Bird.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset")  | Offset values for the multi-part component.  |  
| [`Bird.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Bird.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name")  | X-axis offset name.  |  
| [`Bird.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name")  | Y-axis offset name.  |  
| [`Bird.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name")  | Z-axis offset name.  |  
| [`Bird.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch")  | Pitch variable value.  |  
| [`Bird.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name")  | Pitch variable name.  |  
| [`Bird.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir")  | Shortcut for dir(self).  |  
| [`Bird.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll "ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll")  | Roll variable value.  |  
| [`Bird.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name")  | Roll variable name.  |  
| [`Bird.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression")  | Speed variable expression.  |  
| [`Bird.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name")  | Speed variable name.  |  
| [`Bird.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs")  | Global coordinate system.  |  
| [`Bird.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw")  | Yaw variable value.  |  
| [`Bird.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.rst.txt)

# Bird 

class ansys.aedt.core.modeler.advanced_cad.actors.Bird(_bird_folder_ , _speed : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_, _flapping_rate : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '50Hz'_, _relative_cs_name =None_) 
    
Provides an instance of a bird.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**bird_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the directory containing the definition of the bird. This can be changed later. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the bird. The default is `"2.0"`. 

**flapping_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Flapping rate. The default is `"50Hz"`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is``None``, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Bird
>>> bird = Bird(r"C:\temp\actors\bird", speed="2.0", flapping_rate="50Hz")
>>> bird

```
Copy to clipboard
Methods  
| [`Bird.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert "ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert")(app[, motion])  | Insert the bird in HFSS SBR+.  |  
| --- | --- |  
| [`Bird.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Bird.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Bird.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.start "ansys.aedt.core.modeler.advanced_cad.actors.Bird.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Bird.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Bird.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.index "ansys.aedt.core.modeler.advanced_cad.actors.Bird.index")  | Number of multi-part components.  |  
| [`Bird.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Bird.modeler_units")  | Value for modeler units.  |  
| [`Bird.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.name")  | Unique instance name.  |  
| [`Bird.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset")  | Offset values for the multi-part component.  |  
| [`Bird.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Bird.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_x_name")  | X-axis offset name.  |  
| [`Bird.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_y_name")  | Y-axis offset name.  |  
| [`Bird.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.offset_z_name")  | Z-axis offset name.  |  
| [`Bird.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch")  | Pitch variable value.  |  
| [`Bird.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.pitch_name")  | Pitch variable name.  |  
| [`Bird.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Bird.public_dir")  | Shortcut for dir(self).  |  
| [`Bird.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll "ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll")  | Roll variable value.  |  
| [`Bird.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.roll_name")  | Roll variable name.  |  
| [`Bird.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_expression")  | Speed variable expression.  |  
| [`Bird.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.speed_name")  | Speed variable name.  |  
| [`Bird.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Bird.use_global_cs")  | Global coordinate system.  |  
| [`Bird.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw")  | Yaw variable value.  |  
| [`Bird.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Bird.yaw_name")  | Yaw variable name.  |