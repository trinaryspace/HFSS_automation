---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Vehicle 

class ansys.aedt.core.modeler.advanced_cad.actors.Vehicle(_car_folder_ , _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_, _relative_cs_name =None_) 
    
Provides an instance of a vehicle.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**car_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `required` 
    
Full path to the folder containing the definition of the vehicle. This can be changed later. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the vehicle. The default is `10.0`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Vehicle
>>> vehicle = Vehicle(r"C:\temp\actors\vehicle", speed=10.0)
>>> vehicle

```
Copy to clipboard
Methods  
| [`Vehicle.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert")(app[, motion])  | Insert the vehicle in HFSS SBR+.  |  
| --- | --- |  
| [`Vehicle.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Vehicle.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Vehicle.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Vehicle.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index")  | Number of multi-part components.  |  
| [`Vehicle.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units")  | Value for modeler units.  |  
| [`Vehicle.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name")  | Unique instance name.  |  
| [`Vehicle.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset")  | Offset values for the multi-part component.  |  
| [`Vehicle.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Vehicle.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name")  | X-axis offset name.  |  
| [`Vehicle.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name")  | Y-axis offset name.  |  
| [`Vehicle.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name")  | Z-axis offset name.  |  
| [`Vehicle.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch")  | Pitch variable value.  |  
| [`Vehicle.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name")  | Pitch variable name.  |  
| [`Vehicle.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir")  | Shortcut for dir(self).  |  
| [`Vehicle.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll")  | Roll variable value.  |  
| [`Vehicle.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name")  | Roll variable name.  |  
| [`Vehicle.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression")  | Speed variable expression.  |  
| [`Vehicle.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name")  | Speed variable name.  |  
| [`Vehicle.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs")  | Global coordinate system.  |  
| [`Vehicle.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw")  | Yaw variable value.  |  
| [`Vehicle.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name")  | Yaw variable name.  |  
# Vehicle 

class ansys.aedt.core.modeler.advanced_cad.actors.Vehicle(_car_folder_ , _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_, _relative_cs_name =None_) 
    
Provides an instance of a vehicle.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**car_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `required` 
    
Full path to the folder containing the definition of the vehicle. This can be changed later. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the vehicle. The default is `10.0`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Vehicle
>>> vehicle = Vehicle(r"C:\temp\actors\vehicle", speed=10.0)
>>> vehicle

```
Copy to clipboard
Methods  
| [`Vehicle.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert")(app[, motion])  | Insert the vehicle in HFSS SBR+.  |  
| --- | --- |  
| [`Vehicle.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Vehicle.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Vehicle.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Vehicle.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index")  | Number of multi-part components.  |  
| [`Vehicle.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units")  | Value for modeler units.  |  
| [`Vehicle.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name")  | Unique instance name.  |  
| [`Vehicle.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset")  | Offset values for the multi-part component.  |  
| [`Vehicle.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Vehicle.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name")  | X-axis offset name.  |  
| [`Vehicle.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name")  | Y-axis offset name.  |  
| [`Vehicle.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name")  | Z-axis offset name.  |  
| [`Vehicle.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch")  | Pitch variable value.  |  
| [`Vehicle.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name")  | Pitch variable name.  |  
| [`Vehicle.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir")  | Shortcut for dir(self).  |  
| [`Vehicle.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll")  | Roll variable value.  |  
| [`Vehicle.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name")  | Roll variable name.  |  
| [`Vehicle.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression")  | Speed variable expression.  |  
| [`Vehicle.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name")  | Speed variable name.  |  
| [`Vehicle.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs")  | Global coordinate system.  |  
| [`Vehicle.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw")  | Yaw variable value.  |  
| [`Vehicle.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.rst.txt)

# Vehicle 

class ansys.aedt.core.modeler.advanced_cad.actors.Vehicle(_car_folder_ , _speed : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_, _relative_cs_name =None_) 
    
Provides an instance of a vehicle.
This class is derived from `ansys.aedt.core.modeler.multiparts.MultiPartComponent`.
Note
Motion is always forward in the X-axis direction. 

Parameters: 
     

**car_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `required` 
    
Full path to the folder containing the definition of the vehicle. This can be changed later. 

**speed**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Speed of the vehicle. The default is `10.0`. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the relative coordinate system of the actor. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Vehicle
>>> vehicle = Vehicle(r"C:\temp\actors\vehicle", speed=10.0)
>>> vehicle

```
Copy to clipboard
Methods  
| [`Vehicle.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.insert")(app[, motion])  | Insert the vehicle in HFSS SBR+.  |  
| --- | --- |  
| [`Vehicle.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Vehicle.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Vehicle.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Vehicle.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.index")  | Number of multi-part components.  |  
| [`Vehicle.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.modeler_units")  | Value for modeler units.  |  
| [`Vehicle.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.name")  | Unique instance name.  |  
| [`Vehicle.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset")  | Offset values for the multi-part component.  |  
| [`Vehicle.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Vehicle.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_x_name")  | X-axis offset name.  |  
| [`Vehicle.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_y_name")  | Y-axis offset name.  |  
| [`Vehicle.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.offset_z_name")  | Z-axis offset name.  |  
| [`Vehicle.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch")  | Pitch variable value.  |  
| [`Vehicle.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.pitch_name")  | Pitch variable name.  |  
| [`Vehicle.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.public_dir")  | Shortcut for dir(self).  |  
| [`Vehicle.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll")  | Roll variable value.  |  
| [`Vehicle.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.roll_name")  | Roll variable name.  |  
| [`Vehicle.speed_expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_expression")  | Speed variable expression.  |  
| [`Vehicle.speed_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.speed_name")  | Speed variable name.  |  
| [`Vehicle.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.use_global_cs")  | Global coordinate system.  |  
| [`Vehicle.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw")  | Yaw variable value.  |  
| [`Vehicle.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name "ansys.aedt.core.modeler.advanced_cad.actors.Vehicle.yaw_name")  | Yaw variable name.  |