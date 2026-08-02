---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Radar 

class ansys.aedt.core.modeler.advanced_cad.actors.Radar(_radar_folder_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _offset =('0', '0', '0')_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _relative_cs_name =None_) 
    
Manages the radar definition and placement in the HFSS design. 

Parameters: 
     

**radar_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the radar file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the radar file. The default is `None`. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the actor is in motion. The default is `False`. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of offset values. The default is `("0", "0", "0")`. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the vehicle. The default is `0`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Radar
>>> radar = Radar(r"C:\temp\actors\radar", name="radar1", speed=10)
>>> radar.speed_name
'radar1_speed'

```
Copy to clipboard
Methods  
| [`Radar.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert "ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert")(app[, motion])  | Insert radar in the HFSS application instance.  |  
| --- | --- |  
| [`Radar.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Radar.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.start "ansys.aedt.core.modeler.advanced_cad.actors.Radar.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Radar.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Radar.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.index "ansys.aedt.core.modeler.advanced_cad.actors.Radar.index")  | Number of multi-part components.  |  
| [`Radar.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units")  | Value for modeler units.  |  
| [`Radar.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.name")  | Unique instance name.  |  
| [`Radar.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset")  | Offset values for the multi-part component.  |  
| [`Radar.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Radar.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name")  | X-axis offset name.  |  
| [`Radar.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name")  | Y-axis offset name.  |  
| [`Radar.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name")  | Z-axis offset name.  |  
| [`Radar.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch")  | Pitch variable value.  |  
| [`Radar.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name")  | Pitch variable name.  |  
| [`Radar.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir")  | Shortcut for dir(self).  |  
| [`Radar.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll "ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll")  | Roll variable value.  |  
| [`Radar.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name")  | Roll variable name.  |  
| [`Radar.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression")  | Speed variable expression.  |  
| [`Radar.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name")  | Speed variable name.  |  
| [`Radar.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.units.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.units "ansys.aedt.core.modeler.advanced_cad.actors.Radar.units")  | Multi-part units.  |  
| [`Radar.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs")  | Global coordinate system.  |  
| [`Radar.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw")  | Yaw variable value.  |  
| [`Radar.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name")  | Yaw variable name.  |  
# Radar 

class ansys.aedt.core.modeler.advanced_cad.actors.Radar(_radar_folder_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _offset =('0', '0', '0')_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _relative_cs_name =None_) 
    
Manages the radar definition and placement in the HFSS design. 

Parameters: 
     

**radar_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the radar file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the radar file. The default is `None`. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the actor is in motion. The default is `False`. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of offset values. The default is `("0", "0", "0")`. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the vehicle. The default is `0`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Radar
>>> radar = Radar(r"C:\temp\actors\radar", name="radar1", speed=10)
>>> radar.speed_name
'radar1_speed'

```
Copy to clipboard
Methods  
| [`Radar.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert "ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert")(app[, motion])  | Insert radar in the HFSS application instance.  |  
| --- | --- |  
| [`Radar.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Radar.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.start "ansys.aedt.core.modeler.advanced_cad.actors.Radar.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Radar.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Radar.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.index "ansys.aedt.core.modeler.advanced_cad.actors.Radar.index")  | Number of multi-part components.  |  
| [`Radar.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units")  | Value for modeler units.  |  
| [`Radar.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.name")  | Unique instance name.  |  
| [`Radar.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset")  | Offset values for the multi-part component.  |  
| [`Radar.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Radar.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name")  | X-axis offset name.  |  
| [`Radar.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name")  | Y-axis offset name.  |  
| [`Radar.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name")  | Z-axis offset name.  |  
| [`Radar.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch")  | Pitch variable value.  |  
| [`Radar.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name")  | Pitch variable name.  |  
| [`Radar.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir")  | Shortcut for dir(self).  |  
| [`Radar.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll "ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll")  | Roll variable value.  |  
| [`Radar.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name")  | Roll variable name.  |  
| [`Radar.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression")  | Speed variable expression.  |  
| [`Radar.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name")  | Speed variable name.  |  
| [`Radar.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.units.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.units "ansys.aedt.core.modeler.advanced_cad.actors.Radar.units")  | Multi-part units.  |  
| [`Radar.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs")  | Global coordinate system.  |  
| [`Radar.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw")  | Yaw variable value.  |  
| [`Radar.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.rst.txt)

# Radar 

class ansys.aedt.core.modeler.advanced_cad.actors.Radar(_radar_folder_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _offset =('0', '0', '0')_, _speed : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _relative_cs_name =None_) 
    
Manages the radar definition and placement in the HFSS design. 

Parameters: 
     

**radar_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing the radar file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the radar file. The default is `None`. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the actor is in motion. The default is `False`. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of offset values. The default is `("0", "0", "0")`. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the vehicle. The default is `0`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Radar
>>> radar = Radar(r"C:\temp\actors\radar", name="radar1", speed=10)
>>> radar.speed_name
'radar1_speed'

```
Copy to clipboard
Methods  
| [`Radar.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert "ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert")(app[, motion])  | Insert radar in the HFSS application instance.  |  
| --- | --- |  
| [`Radar.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Radar.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.start "ansys.aedt.core.modeler.advanced_cad.actors.Radar.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Radar.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Radar.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.index "ansys.aedt.core.modeler.advanced_cad.actors.Radar.index")  | Number of multi-part components.  |  
| [`Radar.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Radar.modeler_units")  | Value for modeler units.  |  
| [`Radar.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.name")  | Unique instance name.  |  
| [`Radar.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset")  | Offset values for the multi-part component.  |  
| [`Radar.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Radar.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_x_name")  | X-axis offset name.  |  
| [`Radar.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_y_name")  | Y-axis offset name.  |  
| [`Radar.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.offset_z_name")  | Z-axis offset name.  |  
| [`Radar.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch")  | Pitch variable value.  |  
| [`Radar.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.pitch_name")  | Pitch variable name.  |  
| [`Radar.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Radar.public_dir")  | Shortcut for dir(self).  |  
| [`Radar.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll "ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll")  | Roll variable value.  |  
| [`Radar.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.roll_name")  | Roll variable name.  |  
| [`Radar.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_expression")  | Speed variable expression.  |  
| [`Radar.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.speed_name")  | Speed variable name.  |  
| [`Radar.units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.units.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.units "ansys.aedt.core.modeler.advanced_cad.actors.Radar.units")  | Multi-part units.  |  
| [`Radar.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Radar.use_global_cs")  | Global coordinate system.  |  
| [`Radar.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw")  | Yaw variable value.  |  
| [`Radar.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Radar.yaw_name")  | Yaw variable name.  |