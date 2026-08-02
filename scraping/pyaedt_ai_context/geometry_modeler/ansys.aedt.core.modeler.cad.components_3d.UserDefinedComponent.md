---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# UserDefinedComponent 

class ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _props =None_, _component_type =None_) 
    
Manages object attributes for 3DComponent and User Defined Model. 

Parameters: 
     

**primitives**`ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D` 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default value is `None`. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of properties. The default value is `None`. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the component. The default value is `None`.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> prim = aedtapp.modeler.user_defined_components

```
Copy to clipboard
Obtain user defined component names, to return a [`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent").

```
>>> component_names = aedtapp.modeler.user_defined_components
>>> component = aedtapp.modeler[component_names["3DC_Cell_Radome_In1"]]

```
Copy to clipboard
Methods  
| [`UserDefinedComponent.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete")()  | Delete the object.  |  
| --- | --- |  
| [`UserDefinedComponent.duplicate_along_line`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line")(vector)  | Duplicate the object along a line.  |  
| [`UserDefinedComponent.duplicate_and_mirror`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror")(...)  | Duplicate and mirror a selection.  |  
| [`UserDefinedComponent.duplicate_around_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis")(axis)  | Duplicate the component around the axis.  |  
| [`UserDefinedComponent.edit_definition`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition")([password])  | Edit 3d Definition.  |  
| [`UserDefinedComponent.get_component_filepath`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath")()  | Get 3d component file path.  |  
| [`UserDefinedComponent.history`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history")()  | Component history.  |  
| [`UserDefinedComponent.mirror`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror")(origin, vector)  | Mirror a selection.  |  
| [`UserDefinedComponent.move`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move")(vector)  | Move component from a list.  |  
| [`UserDefinedComponent.rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate")(axis[, angle, units])  | Rotate the selection.  |  
| [`UserDefinedComponent.update_definition`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition")([...])  | Update 3d component definition.  |  
| [`UserDefinedComponent.update_native`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native")()  | Update the Native Component in AEDT.  |  
Attributes  
| [`UserDefinedComponent.bounding_box`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box")  | Get bounding dimension of a user defined model.  |  
| --- | --- |  
| [`UserDefinedComponent.center`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center")  | Get center coordinates of a user defined model.  |  
| [`UserDefinedComponent.group_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name")  | Group the component belongs to.  |  
| [`UserDefinedComponent.is_3d_component`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component")  | 3DComponent flag.  |  
| [`UserDefinedComponent.layout_component`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component")  | Layout component object.  |  
| [`UserDefinedComponent.mesh_assembly`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly")  | Mesh assembly flag.  |  
| [`UserDefinedComponent.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name")  | Name of the object.  |  
| [`UserDefinedComponent.parameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters")  | Component parameters.  |  
| [`UserDefinedComponent.parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts")  | Dictionary of objects that belong to the user-defined component.  |  
| [`UserDefinedComponent.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir")  | Shortcut for dir(self).  |  
| [`UserDefinedComponent.target_coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system")  | Target coordinate system.  |  
# UserDefinedComponent 

class ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _props =None_, _component_type =None_) 
    
Manages object attributes for 3DComponent and User Defined Model. 

Parameters: 
     

**primitives**`ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D` 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default value is `None`. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of properties. The default value is `None`. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the component. The default value is `None`.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> prim = aedtapp.modeler.user_defined_components

```
Copy to clipboard
Obtain user defined component names, to return a [`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent").

```
>>> component_names = aedtapp.modeler.user_defined_components
>>> component = aedtapp.modeler[component_names["3DC_Cell_Radome_In1"]]

```
Copy to clipboard
Methods  
| [`UserDefinedComponent.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete")()  | Delete the object.  |  
| --- | --- |  
| [`UserDefinedComponent.duplicate_along_line`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line")(vector)  | Duplicate the object along a line.  |  
| [`UserDefinedComponent.duplicate_and_mirror`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror")(...)  | Duplicate and mirror a selection.  |  
| [`UserDefinedComponent.duplicate_around_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis")(axis)  | Duplicate the component around the axis.  |  
| [`UserDefinedComponent.edit_definition`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition")([password])  | Edit 3d Definition.  |  
| [`UserDefinedComponent.get_component_filepath`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath")()  | Get 3d component file path.  |  
| [`UserDefinedComponent.history`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history")()  | Component history.  |  
| [`UserDefinedComponent.mirror`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror")(origin, vector)  | Mirror a selection.  |  
| [`UserDefinedComponent.move`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move")(vector)  | Move component from a list.  |  
| [`UserDefinedComponent.rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate")(axis[, angle, units])  | Rotate the selection.  |  
| [`UserDefinedComponent.update_definition`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition")([...])  | Update 3d component definition.  |  
| [`UserDefinedComponent.update_native`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native")()  | Update the Native Component in AEDT.  |  
Attributes  
| [`UserDefinedComponent.bounding_box`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box")  | Get bounding dimension of a user defined model.  |  
| --- | --- |  
| [`UserDefinedComponent.center`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center")  | Get center coordinates of a user defined model.  |  
| [`UserDefinedComponent.group_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name")  | Group the component belongs to.  |  
| [`UserDefinedComponent.is_3d_component`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component")  | 3DComponent flag.  |  
| [`UserDefinedComponent.layout_component`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component")  | Layout component object.  |  
| [`UserDefinedComponent.mesh_assembly`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly")  | Mesh assembly flag.  |  
| [`UserDefinedComponent.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name")  | Name of the object.  |  
| [`UserDefinedComponent.parameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters")  | Component parameters.  |  
| [`UserDefinedComponent.parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts")  | Dictionary of objects that belong to the user-defined component.  |  
| [`UserDefinedComponent.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir")  | Shortcut for dir(self).  |  
| [`UserDefinedComponent.target_coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system")  | Target coordinate system.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rst.txt)

# UserDefinedComponent 

class ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _props =None_, _component_type =None_) 
    
Manages object attributes for 3DComponent and User Defined Model. 

Parameters: 
     

**primitives**`ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D` 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default value is `None`. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of properties. The default value is `None`. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the component. The default value is `None`.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> prim = aedtapp.modeler.user_defined_components

```
Copy to clipboard
Obtain user defined component names, to return a [`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent").

```
>>> component_names = aedtapp.modeler.user_defined_components
>>> component = aedtapp.modeler[component_names["3DC_Cell_Radome_In1"]]

```
Copy to clipboard
Methods  
| [`UserDefinedComponent.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete")()  | Delete the object.  |  
| --- | --- |  
| [`UserDefinedComponent.duplicate_along_line`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line")(vector)  | Duplicate the object along a line.  |  
| [`UserDefinedComponent.duplicate_and_mirror`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_and_mirror")(...)  | Duplicate and mirror a selection.  |  
| [`UserDefinedComponent.duplicate_around_axis`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_around_axis")(axis)  | Duplicate the component around the axis.  |  
| [`UserDefinedComponent.edit_definition`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.edit_definition")([password])  | Edit 3d Definition.  |  
| [`UserDefinedComponent.get_component_filepath`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.get_component_filepath")()  | Get 3d component file path.  |  
| [`UserDefinedComponent.history`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.history")()  | Component history.  |  
| [`UserDefinedComponent.mirror`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror")(origin, vector)  | Mirror a selection.  |  
| [`UserDefinedComponent.move`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move")(vector)  | Move component from a list.  |  
| [`UserDefinedComponent.rotate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.rotate")(axis[, angle, units])  | Rotate the selection.  |  
| [`UserDefinedComponent.update_definition`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_definition")([...])  | Update 3d component definition.  |  
| [`UserDefinedComponent.update_native`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.update_native")()  | Update the Native Component in AEDT.  |  
Attributes  
| [`UserDefinedComponent.bounding_box`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.bounding_box")  | Get bounding dimension of a user defined model.  |  
| --- | --- |  
| [`UserDefinedComponent.center`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.center")  | Get center coordinates of a user defined model.  |  
| [`UserDefinedComponent.group_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.group_name")  | Group the component belongs to.  |  
| [`UserDefinedComponent.is_3d_component`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.is_3d_component")  | 3DComponent flag.  |  
| [`UserDefinedComponent.layout_component`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.layout_component")  | Layout component object.  |  
| [`UserDefinedComponent.mesh_assembly`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mesh_assembly")  | Mesh assembly flag.  |  
| [`UserDefinedComponent.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.name")  | Name of the object.  |  
| [`UserDefinedComponent.parameters`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parameters")  | Component parameters.  |  
| [`UserDefinedComponent.parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.parts")  | Dictionary of objects that belong to the user-defined component.  |  
| [`UserDefinedComponent.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.public_dir")  | Shortcut for dir(self).  |  
| [`UserDefinedComponent.target_coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.target_coordinate_system")  | Target coordinate system.  |