---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# CoordinateSystem 

class ansys.aedt.core.modeler.cad.modeler.CoordinateSystem(_modeler_ , _props =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages the coordinate system data and execution. 

Parameters: 
     

**modeler**
    
Inherited parent object. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of properties. The default is `None`. 

**name**`optional` 
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()

```
Copy to clipboard
Methods  
| [`CoordinateSystem.change_cs_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode")([mode_type])  | Change the mode of the coordinate system.  |  
| --- | --- |  
| [`CoordinateSystem.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create")([origin, ...])  | Create a coordinate system.  |  
| [`CoordinateSystem.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete")()  | Delete the coordinate system.  |  
| [`CoordinateSystem.pointing_to_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis")(...)  | Retrieve the axes from the HFSS X axis and Y pointing axis as per the definition of the AEDT interface coordinate system.  |  
| [`CoordinateSystem.rename`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename")(name)  | Rename the coordinate system.  |  
| [`CoordinateSystem.set_as_working_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs")()  | Set the coordinate system as the working coordinate system.  |  
| [`CoordinateSystem.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update")()  | Update the coordinate system.  |  
Attributes  
| [`CoordinateSystem.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties")  | Available properties.  |  
| --- | --- |  
| [`CoordinateSystem.mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode")  | Coordinate System mode.  |  
| [`CoordinateSystem.origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin")  | Coordinate system origin in model units.  |  
| [`CoordinateSystem.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props")  | Coordinate System Properties.  |  
| [`CoordinateSystem.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir")  | Shortcut for dir(self).  |  
| [`CoordinateSystem.quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion")  | Quaternion computed based on specific axis mode.  |  
| [`CoordinateSystem.ref_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs")  | Reference coordinate system getter and setter.  |  
# CoordinateSystem 

class ansys.aedt.core.modeler.cad.modeler.CoordinateSystem(_modeler_ , _props =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages the coordinate system data and execution. 

Parameters: 
     

**modeler**
    
Inherited parent object. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of properties. The default is `None`. 

**name**`optional` 
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()

```
Copy to clipboard
Methods  
| [`CoordinateSystem.change_cs_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode")([mode_type])  | Change the mode of the coordinate system.  |  
| --- | --- |  
| [`CoordinateSystem.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create")([origin, ...])  | Create a coordinate system.  |  
| [`CoordinateSystem.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete")()  | Delete the coordinate system.  |  
| [`CoordinateSystem.pointing_to_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis")(...)  | Retrieve the axes from the HFSS X axis and Y pointing axis as per the definition of the AEDT interface coordinate system.  |  
| [`CoordinateSystem.rename`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename")(name)  | Rename the coordinate system.  |  
| [`CoordinateSystem.set_as_working_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs")()  | Set the coordinate system as the working coordinate system.  |  
| [`CoordinateSystem.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update")()  | Update the coordinate system.  |  
Attributes  
| [`CoordinateSystem.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties")  | Available properties.  |  
| --- | --- |  
| [`CoordinateSystem.mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode")  | Coordinate System mode.  |  
| [`CoordinateSystem.origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin")  | Coordinate system origin in model units.  |  
| [`CoordinateSystem.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props")  | Coordinate System Properties.  |  
| [`CoordinateSystem.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir")  | Shortcut for dir(self).  |  
| [`CoordinateSystem.quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion")  | Quaternion computed based on specific axis mode.  |  
| [`CoordinateSystem.ref_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs")  | Reference coordinate system getter and setter.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rst.txt)

# CoordinateSystem 

class ansys.aedt.core.modeler.cad.modeler.CoordinateSystem(_modeler_ , _props =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) 
    
Manages the coordinate system data and execution. 

Parameters: 
     

**modeler**
    
Inherited parent object. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of properties. The default is `None`. 

**name**`optional` 
    
The default is `None`.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()

```
Copy to clipboard
Methods  
| [`CoordinateSystem.change_cs_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.change_cs_mode")([mode_type])  | Change the mode of the coordinate system.  |  
| --- | --- |  
| [`CoordinateSystem.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create")([origin, ...])  | Create a coordinate system.  |  
| [`CoordinateSystem.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.delete")()  | Delete the coordinate system.  |  
| [`CoordinateSystem.pointing_to_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.pointing_to_axis")(...)  | Retrieve the axes from the HFSS X axis and Y pointing axis as per the definition of the AEDT interface coordinate system.  |  
| [`CoordinateSystem.rename`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.rename")(name)  | Rename the coordinate system.  |  
| [`CoordinateSystem.set_as_working_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.set_as_working_cs")()  | Set the coordinate system as the working coordinate system.  |  
| [`CoordinateSystem.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.update")()  | Update the coordinate system.  |  
Attributes  
| [`CoordinateSystem.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.available_properties")  | Available properties.  |  
| --- | --- |  
| [`CoordinateSystem.mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.mode")  | Coordinate System mode.  |  
| [`CoordinateSystem.origin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.origin")  | Coordinate system origin in model units.  |  
| [`CoordinateSystem.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.props")  | Coordinate System Properties.  |  
| [`CoordinateSystem.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.public_dir")  | Shortcut for dir(self).  |  
| [`CoordinateSystem.quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.quaternion")  | Quaternion computed based on specific axis mode.  |  
| [`CoordinateSystem.ref_cs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.ref_cs")  | Reference coordinate system getter and setter.  |