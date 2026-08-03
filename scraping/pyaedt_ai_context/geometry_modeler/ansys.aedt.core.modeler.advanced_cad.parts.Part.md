---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Part 

class ansys.aedt.core.modeler.advanced_cad.parts.Part(_part_folder_ , _part_dict_ , _parent =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages 3D component placement and definition. 

Parameters: 
     

**part_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the folder with the A3DCOMP files. 

**part_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Defines relevant properties of the class with the following keywords: * ‘comp_name’: str, Name of the A3DCOMP file. * ‘offset’: list or str, Offset coordinate system definition relative to the parent. * ‘rotation_cs’: list or str, Rotation coordinate system relative to the parent. * ‘rotation’: str or numeric, Rotation angle. * ‘compensation_angle’: str or numeric, Initial angle. * ‘rotation_axis’: str, Rotation axis (`"X"`, `"Y"`, or `"Z"`). * ‘duplicate_number’: str or int, Number of instances for linear duplication. * ‘duplicate_vector’: list, Vector for duplication relative to the parent coordinate system. 

**parent**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The default is `None`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the A3DCOMP file without the extension. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.parts import Part
>>> obj = Part()

```
Copy to clipboard
Methods  
| [`Part.do_rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate "ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate")(app, aedt_object)  | Set the rotation coordinate system relative to the parent coordinate system.  |  
| --- | --- |  
| [`Part.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.insert.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.insert "ansys.aedt.core.modeler.advanced_cad.parts.Part.insert")(app)  | Insert 3D component in AEDT.  |  
| [`Part.set_relative_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs "ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs")(app)  | Create a parametric coordinate system.  |  
| [`Part.zero_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset "ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset")(kw)  | Check if the coordinate system defined by kw is [0, 0, 0].  |  
Attributes  
| [`Part.allowed_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys "ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys")  | Value for allowed keys.  |  
| --- | --- |  
| [`Part.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name")  | Coordinate system name.  |  
| [`Part.file_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name")  | Antenna file name.  |  
| [`Part.local_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin "ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin")  | Local part offset values.  |  
| [`Part.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.name "ansys.aedt.core.modeler.advanced_cad.parts.Part.name")  | Part name.  |  
| [`Part.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch "ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch")  | Pitch variable value.  |  
| [`Part.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name")  | Pitch variable name.  |  
| [`Part.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir "ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir")  | Shortcut for dir(self).  |  
| [`Part.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.roll.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.roll "ansys.aedt.core.modeler.advanced_cad.parts.Part.roll")  | Roll variable value.  |  
| [`Part.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name")  | Roll variable name.  |  
| [`Part.rot_cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name")  | Rotation coordinate system name.  |  
| [`Part.rotate_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin "ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin")  | Origin rotation list.  |  
| [`Part.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw "ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw")  | Yaw variable value.  |  
| [`Part.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name")  | Yaw variable name.  |  
# Part 

class ansys.aedt.core.modeler.advanced_cad.parts.Part(_part_folder_ , _part_dict_ , _parent =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages 3D component placement and definition. 

Parameters: 
     

**part_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the folder with the A3DCOMP files. 

**part_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Defines relevant properties of the class with the following keywords: * ‘comp_name’: str, Name of the A3DCOMP file. * ‘offset’: list or str, Offset coordinate system definition relative to the parent. * ‘rotation_cs’: list or str, Rotation coordinate system relative to the parent. * ‘rotation’: str or numeric, Rotation angle. * ‘compensation_angle’: str or numeric, Initial angle. * ‘rotation_axis’: str, Rotation axis (`"X"`, `"Y"`, or `"Z"`). * ‘duplicate_number’: str or int, Number of instances for linear duplication. * ‘duplicate_vector’: list, Vector for duplication relative to the parent coordinate system. 

**parent**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The default is `None`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the A3DCOMP file without the extension. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.parts import Part
>>> obj = Part()

```
Copy to clipboard
Methods  
| [`Part.do_rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate "ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate")(app, aedt_object)  | Set the rotation coordinate system relative to the parent coordinate system.  |  
| --- | --- |  
| [`Part.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.insert.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.insert "ansys.aedt.core.modeler.advanced_cad.parts.Part.insert")(app)  | Insert 3D component in AEDT.  |  
| [`Part.set_relative_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs "ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs")(app)  | Create a parametric coordinate system.  |  
| [`Part.zero_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset "ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset")(kw)  | Check if the coordinate system defined by kw is [0, 0, 0].  |  
Attributes  
| [`Part.allowed_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys "ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys")  | Value for allowed keys.  |  
| --- | --- |  
| [`Part.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name")  | Coordinate system name.  |  
| [`Part.file_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name")  | Antenna file name.  |  
| [`Part.local_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin "ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin")  | Local part offset values.  |  
| [`Part.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.name "ansys.aedt.core.modeler.advanced_cad.parts.Part.name")  | Part name.  |  
| [`Part.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch "ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch")  | Pitch variable value.  |  
| [`Part.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name")  | Pitch variable name.  |  
| [`Part.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir "ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir")  | Shortcut for dir(self).  |  
| [`Part.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.roll.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.roll "ansys.aedt.core.modeler.advanced_cad.parts.Part.roll")  | Roll variable value.  |  
| [`Part.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name")  | Roll variable name.  |  
| [`Part.rot_cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name")  | Rotation coordinate system name.  |  
| [`Part.rotate_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin "ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin")  | Origin rotation list.  |  
| [`Part.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw "ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw")  | Yaw variable value.  |  
| [`Part.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name")  | Yaw variable name.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.rst.txt)

# Part 

class ansys.aedt.core.modeler.advanced_cad.parts.Part(_part_folder_ , _part_dict_ , _parent =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages 3D component placement and definition. 

Parameters: 
     

**part_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the folder with the A3DCOMP files. 

**part_dict**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Defines relevant properties of the class with the following keywords: * ‘comp_name’: str, Name of the A3DCOMP file. * ‘offset’: list or str, Offset coordinate system definition relative to the parent. * ‘rotation_cs’: list or str, Rotation coordinate system relative to the parent. * ‘rotation’: str or numeric, Rotation angle. * ‘compensation_angle’: str or numeric, Initial angle. * ‘rotation_axis’: str, Rotation axis (`"X"`, `"Y"`, or `"Z"`). * ‘duplicate_number’: str or int, Number of instances for linear duplication. * ‘duplicate_vector’: list, Vector for duplication relative to the parent coordinate system. 

**parent**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The default is `None`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the A3DCOMP file without the extension. The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.parts import Part
>>> obj = Part()

```
Copy to clipboard
Methods  
| [`Part.do_rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate "ansys.aedt.core.modeler.advanced_cad.parts.Part.do_rotate")(app, aedt_object)  | Set the rotation coordinate system relative to the parent coordinate system.  |  
| --- | --- |  
| [`Part.insert`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.insert.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.insert "ansys.aedt.core.modeler.advanced_cad.parts.Part.insert")(app)  | Insert 3D component in AEDT.  |  
| [`Part.set_relative_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs "ansys.aedt.core.modeler.advanced_cad.parts.Part.set_relative_cs")(app)  | Create a parametric coordinate system.  |  
| [`Part.zero_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset "ansys.aedt.core.modeler.advanced_cad.parts.Part.zero_offset")(kw)  | Check if the coordinate system defined by kw is [0, 0, 0].  |  
Attributes  
| [`Part.allowed_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys "ansys.aedt.core.modeler.advanced_cad.parts.Part.allowed_keys")  | Value for allowed keys.  |  
| --- | --- |  
| [`Part.cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.cs_name")  | Coordinate system name.  |  
| [`Part.file_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.file_name")  | Antenna file name.  |  
| [`Part.local_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin "ansys.aedt.core.modeler.advanced_cad.parts.Part.local_origin")  | Local part offset values.  |  
| [`Part.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.name "ansys.aedt.core.modeler.advanced_cad.parts.Part.name")  | Part name.  |  
| [`Part.pitch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch "ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch")  | Pitch variable value.  |  
| [`Part.pitch_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.pitch_name")  | Pitch variable name.  |  
| [`Part.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir "ansys.aedt.core.modeler.advanced_cad.parts.Part.public_dir")  | Shortcut for dir(self).  |  
| [`Part.roll`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.roll.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.roll "ansys.aedt.core.modeler.advanced_cad.parts.Part.roll")  | Roll variable value.  |  
| [`Part.roll_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.roll_name")  | Roll variable name.  |  
| [`Part.rot_cs_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.rot_cs_name")  | Rotation coordinate system name.  |  
| [`Part.rotate_origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin "ansys.aedt.core.modeler.advanced_cad.parts.Part.rotate_origin")  | Origin rotation list.  |  
| [`Part.yaw`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw "ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw")  | Yaw variable value.  |  
| [`Part.yaw_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name.html#ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name "ansys.aedt.core.modeler.advanced_cad.parts.Part.yaw_name")  | Yaw variable name.  |