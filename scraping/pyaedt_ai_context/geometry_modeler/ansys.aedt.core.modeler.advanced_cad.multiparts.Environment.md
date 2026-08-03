---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Environment 

class ansys.aedt.core.modeler.advanced_cad.multiparts.Environment(_env_folder_ , _relative_cs_name =None_) 
    
Supports multi-part 3D components without motion for HFSS SBR+.
This class is derived from [`MultiPartComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent"). Its call signature is identical to the parent class except `motion` is always set to `False`. 

Parameters: 
     

**env_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder with the JSON file containing the component definition. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system to connect the component’s relative system to when `use_relative_cs=True`. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import Environment
>>> env = Environment(r"C:\temp\actors")
>>> env

```
Copy to clipboard
Methods  
| [`Environment.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`Environment.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Environment.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Environment.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Environment.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index")  | Number of multi-part components.  |  
| [`Environment.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units")  | Value for modeler units.  |  
| [`Environment.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name")  | Unique instance name.  |  
| [`Environment.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset")  | Offset for the multi-part component.  |  
| [`Environment.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Environment.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name")  | X-axis offset name.  |  
| [`Environment.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name")  | Y-axis offset name.  |  
| [`Environment.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name")  | Z-axis offset name.  |  
| [`Environment.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch")  | Pitch variable value.  |  
| [`Environment.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name")  | Pitch variable name.  |  
| [`Environment.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir")  | Shortcut for dir(self).  |  
| [`Environment.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll")  | Roll variable value.  |  
| [`Environment.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name")  | Roll variable name.  |  
| [`Environment.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs")  | Global coordinate system.  |  
| [`Environment.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw")  | Yaw variable value.  |  
| [`Environment.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name")  | Yaw variable name.  |  
# Environment 

class ansys.aedt.core.modeler.advanced_cad.multiparts.Environment(_env_folder_ , _relative_cs_name =None_) 
    
Supports multi-part 3D components without motion for HFSS SBR+.
This class is derived from [`MultiPartComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent"). Its call signature is identical to the parent class except `motion` is always set to `False`. 

Parameters: 
     

**env_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder with the JSON file containing the component definition. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system to connect the component’s relative system to when `use_relative_cs=True`. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import Environment
>>> env = Environment(r"C:\temp\actors")
>>> env

```
Copy to clipboard
Methods  
| [`Environment.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`Environment.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Environment.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Environment.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Environment.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index")  | Number of multi-part components.  |  
| [`Environment.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units")  | Value for modeler units.  |  
| [`Environment.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name")  | Unique instance name.  |  
| [`Environment.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset")  | Offset for the multi-part component.  |  
| [`Environment.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Environment.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name")  | X-axis offset name.  |  
| [`Environment.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name")  | Y-axis offset name.  |  
| [`Environment.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name")  | Z-axis offset name.  |  
| [`Environment.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch")  | Pitch variable value.  |  
| [`Environment.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name")  | Pitch variable name.  |  
| [`Environment.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir")  | Shortcut for dir(self).  |  
| [`Environment.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll")  | Roll variable value.  |  
| [`Environment.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name")  | Roll variable name.  |  
| [`Environment.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs")  | Global coordinate system.  |  
| [`Environment.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw")  | Yaw variable value.  |  
| [`Environment.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.rst.txt)

# Environment 

class ansys.aedt.core.modeler.advanced_cad.multiparts.Environment(_env_folder_ , _relative_cs_name =None_) 
    
Supports multi-part 3D components without motion for HFSS SBR+.
This class is derived from [`MultiPartComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent"). Its call signature is identical to the parent class except `motion` is always set to `False`. 

Parameters: 
     

**env_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder with the JSON file containing the component definition. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system to connect the component’s relative system to when `use_relative_cs=True`. The default is `None`, in which case the global coordinate system is used.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import Environment
>>> env = Environment(r"C:\temp\actors")
>>> env

```
Copy to clipboard
Methods  
| [`Environment.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`Environment.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`Environment.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`Environment.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`Environment.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.index")  | Number of multi-part components.  |  
| [`Environment.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.modeler_units")  | Value for modeler units.  |  
| [`Environment.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.name")  | Unique instance name.  |  
| [`Environment.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset")  | Offset for the multi-part component.  |  
| [`Environment.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`Environment.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_x_name")  | X-axis offset name.  |  
| [`Environment.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_y_name")  | Y-axis offset name.  |  
| [`Environment.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.offset_z_name")  | Z-axis offset name.  |  
| [`Environment.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch")  | Pitch variable value.  |  
| [`Environment.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.pitch_name")  | Pitch variable name.  |  
| [`Environment.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.public_dir")  | Shortcut for dir(self).  |  
| [`Environment.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll")  | Roll variable value.  |  
| [`Environment.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.roll_name")  | Roll variable name.  |  
| [`Environment.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.use_global_cs")  | Global coordinate system.  |  
| [`Environment.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw")  | Yaw variable value.  |  
| [`Environment.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.Environment.yaw_name")  | Yaw variable name.  |