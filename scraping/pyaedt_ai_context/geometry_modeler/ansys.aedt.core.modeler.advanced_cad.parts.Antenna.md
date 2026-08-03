---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Antenna 

class ansys.aedt.core.modeler.advanced_cad.parts.Antenna(_root_folder_ , _ant_dict_ , _parent =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages antennas.
This class is derived from [`Part`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.html#ansys.aedt.core.modeler.advanced_cad.parts.Part "ansys.aedt.core.modeler.advanced_cad.parts.Part"). 

Parameters: 
     

**root_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Root directory 

**ant_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Antenna dictionary 

**parent**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.parts import Antenna
>>> obj = Antenna()

```
Copy to clipboard
Methods  
| [`Antenna.do_rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate")(app, aedt_object)  | Set the rotation coordinate system relative to the parent coordinate system.  |  
| --- | --- |  
| [`Antenna.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert")(app[, units])  | Insert antenna in HFSS SBR+.  |  
| [`Antenna.set_relative_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs")(app)  | Create a parametric coordinate system.  |  
| [`Antenna.zero_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset")(kw)  | Check if the coordinate system defined by kw is [0, 0, 0].  |  
Attributes  
| [`Antenna.allowed_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys")  | Value for allowed keys.  |  
| --- | --- |  
| [`Antenna.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name")  | Coordinate system name.  |  
| [`Antenna.file_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name")  | Antenna file name.  |  
| [`Antenna.local_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin")  | Local part offset values.  |  
| [`Antenna.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name")  | Part name.  |  
| [`Antenna.params`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params")  | Multi-part component parameters.  |  
| [`Antenna.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch")  | Pitch variable value.  |  
| [`Antenna.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name")  | Pitch variable name.  |  
| [`Antenna.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir")  | Shortcut for dir(self).  |  
| [`Antenna.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll")  | Roll variable value.  |  
| [`Antenna.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name")  | Roll variable name.  |  
| [`Antenna.rot_cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name")  | Rotation coordinate system name.  |  
| [`Antenna.rotate_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin")  | Origin rotation list.  |  
| [`Antenna.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw")  | Yaw variable value.  |  
| [`Antenna.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name")  | Yaw variable name.  |  
# Antenna 

class ansys.aedt.core.modeler.advanced_cad.parts.Antenna(_root_folder_ , _ant_dict_ , _parent =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages antennas.
This class is derived from [`Part`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.html#ansys.aedt.core.modeler.advanced_cad.parts.Part "ansys.aedt.core.modeler.advanced_cad.parts.Part"). 

Parameters: 
     

**root_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Root directory 

**ant_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Antenna dictionary 

**parent**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.parts import Antenna
>>> obj = Antenna()

```
Copy to clipboard
Methods  
| [`Antenna.do_rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate")(app, aedt_object)  | Set the rotation coordinate system relative to the parent coordinate system.  |  
| --- | --- |  
| [`Antenna.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert")(app[, units])  | Insert antenna in HFSS SBR+.  |  
| [`Antenna.set_relative_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs")(app)  | Create a parametric coordinate system.  |  
| [`Antenna.zero_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset")(kw)  | Check if the coordinate system defined by kw is [0, 0, 0].  |  
Attributes  
| [`Antenna.allowed_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys")  | Value for allowed keys.  |  
| --- | --- |  
| [`Antenna.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name")  | Coordinate system name.  |  
| [`Antenna.file_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name")  | Antenna file name.  |  
| [`Antenna.local_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin")  | Local part offset values.  |  
| [`Antenna.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name")  | Part name.  |  
| [`Antenna.params`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params")  | Multi-part component parameters.  |  
| [`Antenna.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch")  | Pitch variable value.  |  
| [`Antenna.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name")  | Pitch variable name.  |  
| [`Antenna.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir")  | Shortcut for dir(self).  |  
| [`Antenna.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll")  | Roll variable value.  |  
| [`Antenna.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name")  | Roll variable name.  |  
| [`Antenna.rot_cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name")  | Rotation coordinate system name.  |  
| [`Antenna.rotate_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin")  | Origin rotation list.  |  
| [`Antenna.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw")  | Yaw variable value.  |  
| [`Antenna.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rst.txt)

# Antenna 

class ansys.aedt.core.modeler.advanced_cad.parts.Antenna(_root_folder_ , _ant_dict_ , _parent =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages antennas.
This class is derived from [`Part`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.html#ansys.aedt.core.modeler.advanced_cad.parts.Part "ansys.aedt.core.modeler.advanced_cad.parts.Part"). 

Parameters: 
     

**root_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Root directory 

**ant_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Antenna dictionary 

**parent**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.parts import Antenna
>>> obj = Antenna()

```
Copy to clipboard
Methods  
| [`Antenna.do_rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.do_rotate")(app, aedt_object)  | Set the rotation coordinate system relative to the parent coordinate system.  |  
| --- | --- |  
| [`Antenna.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.insert")(app[, units])  | Insert antenna in HFSS SBR+.  |  
| [`Antenna.set_relative_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.set_relative_cs")(app)  | Create a parametric coordinate system.  |  
| [`Antenna.zero_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.zero_offset")(kw)  | Check if the coordinate system defined by kw is [0, 0, 0].  |  
Attributes  
| [`Antenna.allowed_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.allowed_keys")  | Value for allowed keys.  |  
| --- | --- |  
| [`Antenna.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.cs_name")  | Coordinate system name.  |  
| [`Antenna.file_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.file_name")  | Antenna file name.  |  
| [`Antenna.local_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.local_origin")  | Local part offset values.  |  
| [`Antenna.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.name")  | Part name.  |  
| [`Antenna.params`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.params")  | Multi-part component parameters.  |  
| [`Antenna.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch")  | Pitch variable value.  |  
| [`Antenna.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.pitch_name")  | Pitch variable name.  |  
| [`Antenna.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.public_dir")  | Shortcut for dir(self).  |  
| [`Antenna.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll")  | Roll variable value.  |  
| [`Antenna.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.roll_name")  | Roll variable name.  |  
| [`Antenna.rot_cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rot_cs_name")  | Rotation coordinate system name.  |  
| [`Antenna.rotate_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.rotate_origin")  | Origin rotation list.  |  
| [`Antenna.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw")  | Yaw variable value.  |  
| [`Antenna.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name "ansys.aedt.core.modeler.advanced_cad.parts.Antenna.yaw_name")  | Yaw variable name.  |