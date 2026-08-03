---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# MultiPartComponent 

class ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent(_comp_folder_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _relative_cs_name =None_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _offset =('0', '0', '0')_, _yaw : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_, _pitch : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_, _roll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_) 
    
Supports multi-part 3D components for HFSS SBR+.
Note
Forward motion is in the X-axis direction if motion is set. 

Parameters: 
     

**comp_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder with the JSON file containing the component definition. This JSON file must have the same name as the folder. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the multipart component. If this value is set, the component is selected from the corresponding JSON file in `comp_folder`. The default is `None`, in which case the name of the first JSON file in the folder is used. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. Set to `False` if the multi-part component doesn’t move. Set to `True` if the multi-part component moves relative to the global coordinate system. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system to connect the multipart relative system to when `use_relative_cs=True`. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether expressions should be used to define the position and orientation of the multi-part component. The default is `False`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinate values defining the component offset. The default is `["0", "0", "0"]`. 

**yaw**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw angle, indicating the rotation about the component’s Z-axis. The default is `"0deg"`. 

**pitch**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch angle, indicating the rotation about the component Y-axis The default is `"0deg"`. 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll angle, indicating the rotation about the component X-axis. The default is `"0deg"`. 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll angle, indicating the rotation about the component’s X-axis. The default
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import MultiPartComponent
>>> component = MultiPartComponent(r"C:\temp\actors")

```
Copy to clipboard
Methods  
| [`MultiPartComponent.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`MultiPartComponent.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`MultiPartComponent.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`MultiPartComponent.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`MultiPartComponent.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index")  | Number of multi-part components.  |  
| [`MultiPartComponent.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units")  | Value for modeler units.  |  
| [`MultiPartComponent.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name")  | Unique instance name.  |  
| [`MultiPartComponent.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset")  | Offset values for the multi-part component.  |  
| [`MultiPartComponent.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`MultiPartComponent.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name")  | X-axis offset name.  |  
| [`MultiPartComponent.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name")  | Y-axis offset name.  |  
| [`MultiPartComponent.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name")  | Z-axis offset name.  |  
| [`MultiPartComponent.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch")  | Pitch variable value.  |  
| [`MultiPartComponent.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name")  | Pitch variable name.  |  
| [`MultiPartComponent.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir")  | Shortcut for dir(self).  |  
| [`MultiPartComponent.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll")  | Roll variable value.  |  
| [`MultiPartComponent.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name")  | Roll variable name.  |  
| [`MultiPartComponent.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs")  | Global coordinate system.  |  
| [`MultiPartComponent.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw")  | Yaw variable value.  |  
| [`MultiPartComponent.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name")  | Yaw variable name.  |  
# MultiPartComponent 

class ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent(_comp_folder_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _relative_cs_name =None_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _offset =('0', '0', '0')_, _yaw : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_, _pitch : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_, _roll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_) 
    
Supports multi-part 3D components for HFSS SBR+.
Note
Forward motion is in the X-axis direction if motion is set. 

Parameters: 
     

**comp_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder with the JSON file containing the component definition. This JSON file must have the same name as the folder. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the multipart component. If this value is set, the component is selected from the corresponding JSON file in `comp_folder`. The default is `None`, in which case the name of the first JSON file in the folder is used. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. Set to `False` if the multi-part component doesn’t move. Set to `True` if the multi-part component moves relative to the global coordinate system. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system to connect the multipart relative system to when `use_relative_cs=True`. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether expressions should be used to define the position and orientation of the multi-part component. The default is `False`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinate values defining the component offset. The default is `["0", "0", "0"]`. 

**yaw**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw angle, indicating the rotation about the component’s Z-axis. The default is `"0deg"`. 

**pitch**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch angle, indicating the rotation about the component Y-axis The default is `"0deg"`. 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll angle, indicating the rotation about the component X-axis. The default is `"0deg"`. 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll angle, indicating the rotation about the component’s X-axis. The default
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import MultiPartComponent
>>> component = MultiPartComponent(r"C:\temp\actors")

```
Copy to clipboard
Methods  
| [`MultiPartComponent.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`MultiPartComponent.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`MultiPartComponent.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`MultiPartComponent.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`MultiPartComponent.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index")  | Number of multi-part components.  |  
| [`MultiPartComponent.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units")  | Value for modeler units.  |  
| [`MultiPartComponent.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name")  | Unique instance name.  |  
| [`MultiPartComponent.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset")  | Offset values for the multi-part component.  |  
| [`MultiPartComponent.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`MultiPartComponent.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name")  | X-axis offset name.  |  
| [`MultiPartComponent.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name")  | Y-axis offset name.  |  
| [`MultiPartComponent.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name")  | Z-axis offset name.  |  
| [`MultiPartComponent.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch")  | Pitch variable value.  |  
| [`MultiPartComponent.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name")  | Pitch variable name.  |  
| [`MultiPartComponent.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir")  | Shortcut for dir(self).  |  
| [`MultiPartComponent.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll")  | Roll variable value.  |  
| [`MultiPartComponent.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name")  | Roll variable name.  |  
| [`MultiPartComponent.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs")  | Global coordinate system.  |  
| [`MultiPartComponent.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw")  | Yaw variable value.  |  
| [`MultiPartComponent.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.rst.txt)

# MultiPartComponent 

class ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent(_comp_folder_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_relative_cs : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _relative_cs_name =None_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _offset =('0', '0', '0')_, _yaw : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_, _pitch : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_, _roll : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0deg'_) 
    
Supports multi-part 3D components for HFSS SBR+.
Note
Forward motion is in the X-axis direction if motion is set. 

Parameters: 
     

**comp_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder with the JSON file containing the component definition. This JSON file must have the same name as the folder. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the multipart component. If this value is set, the component is selected from the corresponding JSON file in `comp_folder`. The default is `None`, in which case the name of the first JSON file in the folder is used. 

**use_relative_cs**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use the relative coordinate system. The default is `False`. Set to `False` if the multi-part component doesn’t move. Set to `True` if the multi-part component moves relative to the global coordinate system. 

**relative_cs_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system to connect the multipart relative system to when `use_relative_cs=True`. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether expressions should be used to define the position and orientation of the multi-part component. The default is `False`. 

**offset**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinate values defining the component offset. The default is `["0", "0", "0"]`. 

**yaw**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Yaw angle, indicating the rotation about the component’s Z-axis. The default is `"0deg"`. 

**pitch**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Pitch angle, indicating the rotation about the component Y-axis The default is `"0deg"`. 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll angle, indicating the rotation about the component X-axis. The default is `"0deg"`. 

**roll**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Roll angle, indicating the rotation about the component’s X-axis. The default
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import MultiPartComponent
>>> component = MultiPartComponent(r"C:\temp\actors")

```
Copy to clipboard
Methods  
| [`MultiPartComponent.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.insert")(app[, motion])  | Insert the object in HFSS SBR+.  |  
| --- | --- |  
| [`MultiPartComponent.position_in_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.position_in_app")(app)  | Set up design variables and values to enable motion for the multi-part 3D component.  |  
| [`MultiPartComponent.start`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.start")(app)  | Initialize app for SBR+ simulation.  |  
Attributes  
| [`MultiPartComponent.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.cs_name")  | Coordinate system name.  |  
| --- | --- |  
| [`MultiPartComponent.index`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.index")  | Number of multi-part components.  |  
| [`MultiPartComponent.modeler_units`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.modeler_units")  | Value for modeler units.  |  
| [`MultiPartComponent.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.name")  | Unique instance name.  |  
| [`MultiPartComponent.offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset")  | Offset values for the multi-part component.  |  
| [`MultiPartComponent.offset_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_names")  | X-, Y-, and Z-axis offset names.  |  
| [`MultiPartComponent.offset_x_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_x_name")  | X-axis offset name.  |  
| [`MultiPartComponent.offset_y_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_y_name")  | Y-axis offset name.  |  
| [`MultiPartComponent.offset_z_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.offset_z_name")  | Z-axis offset name.  |  
| [`MultiPartComponent.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch")  | Pitch variable value.  |  
| [`MultiPartComponent.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.pitch_name")  | Pitch variable name.  |  
| [`MultiPartComponent.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.public_dir")  | Shortcut for dir(self).  |  
| [`MultiPartComponent.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll")  | Roll variable value.  |  
| [`MultiPartComponent.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.roll_name")  | Roll variable name.  |  
| [`MultiPartComponent.use_global_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.use_global_cs")  | Global coordinate system.  |  
| [`MultiPartComponent.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw")  | Yaw variable value.  |  
| [`MultiPartComponent.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name "ansys.aedt.core.modeler.advanced_cad.multiparts.MultiPartComponent.yaw_name")  | Yaw variable name.  |