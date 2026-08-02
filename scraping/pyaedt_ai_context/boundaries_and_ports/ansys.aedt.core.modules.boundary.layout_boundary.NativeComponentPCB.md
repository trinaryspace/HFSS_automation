---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# NativeComponentPCB 

class ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB(_app_ , _component_type_ , _component_name_ , _props_) 
    
Manages native component PCB data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
AEDT application from the `ansys.aedt.core.application` class. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the component. 

**component_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the component. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Properties of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.layout_boundary import NativeComponentPCB
>>> obj = NativeComponentPCB()

```
Copy to clipboard
Methods  
| [`NativeComponentPCB.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create")()  | Create a Native Component in AEDT.  |  
| --- | --- |  
| [`NativeComponentPCB.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete")()  | Delete the Native Component in AEDT.  |  
| [`NativeComponentPCB.identify_extent_poly`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly")()  | Get polygon that defines board extent.  |  
| [`NativeComponentPCB.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NativeComponentPCB.set_board_extents`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents")(*args, ...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_custom_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_high_side_radiation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_low_side_radiation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution")(*args, ...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentPCB.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentPCB.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update")()  | Update the Native Component in AEDT.  |  
| [`NativeComponentPCB.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NativeComponentPCB.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NativeComponentPCB.board_cutout_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material")  | Material applied to cutout regions.  |  
| [`NativeComponentPCB.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children")  | Retrieve children.  |  
| [`NativeComponentPCB.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command")  | Command of the modeler hystory if available.  |  
| [`NativeComponentPCB.definition_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name")  | Definition name of the native component.  |  
| [`NativeComponentPCB.force_source_solve`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve")  | Force source solution option.  |  
| [`NativeComponentPCB.included_parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts")  | Parts options.  |  
| [`NativeComponentPCB.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name")  | Boundary Name.  |  
| [`NativeComponentPCB.power`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power")  | Power dissipation assigned to the PCB.  |  
| [`NativeComponentPCB.preserve_partner_solution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution")  | Preserve parner solution option.  |  
| [`NativeComponentPCB.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties")  | Properties data.  |  
| [`NativeComponentPCB.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props")  | Retrieve props.  |  
| [`NativeComponentPCB.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir")  | Shortcut for dir(self).  |  
| [`NativeComponentPCB.targetcs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs")  | Native Component Coordinate System.  |  
| [`NativeComponentPCB.via_holes_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material")  | Material applied to via hole regions.  |  
# NativeComponentPCB 

class ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB(_app_ , _component_type_ , _component_name_ , _props_) 
    
Manages native component PCB data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
AEDT application from the `ansys.aedt.core.application` class. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the component. 

**component_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the component. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Properties of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.layout_boundary import NativeComponentPCB
>>> obj = NativeComponentPCB()

```
Copy to clipboard
Methods  
| [`NativeComponentPCB.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create")()  | Create a Native Component in AEDT.  |  
| --- | --- |  
| [`NativeComponentPCB.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete")()  | Delete the Native Component in AEDT.  |  
| [`NativeComponentPCB.identify_extent_poly`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly")()  | Get polygon that defines board extent.  |  
| [`NativeComponentPCB.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NativeComponentPCB.set_board_extents`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents")(*args, ...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_custom_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_high_side_radiation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_low_side_radiation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution")(*args, ...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentPCB.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentPCB.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update")()  | Update the Native Component in AEDT.  |  
| [`NativeComponentPCB.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NativeComponentPCB.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NativeComponentPCB.board_cutout_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material")  | Material applied to cutout regions.  |  
| [`NativeComponentPCB.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children")  | Retrieve children.  |  
| [`NativeComponentPCB.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command")  | Command of the modeler hystory if available.  |  
| [`NativeComponentPCB.definition_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name")  | Definition name of the native component.  |  
| [`NativeComponentPCB.force_source_solve`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve")  | Force source solution option.  |  
| [`NativeComponentPCB.included_parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts")  | Parts options.  |  
| [`NativeComponentPCB.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name")  | Boundary Name.  |  
| [`NativeComponentPCB.power`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power")  | Power dissipation assigned to the PCB.  |  
| [`NativeComponentPCB.preserve_partner_solution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution")  | Preserve parner solution option.  |  
| [`NativeComponentPCB.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties")  | Properties data.  |  
| [`NativeComponentPCB.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props")  | Retrieve props.  |  
| [`NativeComponentPCB.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir")  | Shortcut for dir(self).  |  
| [`NativeComponentPCB.targetcs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs")  | Native Component Coordinate System.  |  
| [`NativeComponentPCB.via_holes_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material")  | Material applied to via hole regions.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.rst.txt)

# NativeComponentPCB 

class ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB(_app_ , _component_type_ , _component_name_ , _props_) 
    
Manages native component PCB data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
AEDT application from the `ansys.aedt.core.application` class. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the component. 

**component_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the component. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Properties of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.layout_boundary import NativeComponentPCB
>>> obj = NativeComponentPCB()

```
Copy to clipboard
Methods  
| [`NativeComponentPCB.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.create")()  | Create a Native Component in AEDT.  |  
| --- | --- |  
| [`NativeComponentPCB.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.delete")()  | Delete the Native Component in AEDT.  |  
| [`NativeComponentPCB.identify_extent_poly`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.identify_extent_poly")()  | Get polygon that defines board extent.  |  
| [`NativeComponentPCB.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NativeComponentPCB.set_board_extents`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_board_extents")(*args, ...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_custom_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_custom_resolution")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_high_side_radiation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_high_side_radiation")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_low_side_radiation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_low_side_radiation")(...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.set_resolution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.set_resolution")(*args, ...)  | Inner wrapper function.  |  
| [`NativeComponentPCB.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentPCB.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentPCB.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update")()  | Update the Native Component in AEDT.  |  
| [`NativeComponentPCB.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NativeComponentPCB.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NativeComponentPCB.board_cutout_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.board_cutout_material")  | Material applied to cutout regions.  |  
| [`NativeComponentPCB.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.children")  | Retrieve children.  |  
| [`NativeComponentPCB.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.command")  | Command of the modeler hystory if available.  |  
| [`NativeComponentPCB.definition_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.definition_name")  | Definition name of the native component.  |  
| [`NativeComponentPCB.force_source_solve`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.force_source_solve")  | Force source solution option.  |  
| [`NativeComponentPCB.included_parts`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.included_parts")  | Parts options.  |  
| [`NativeComponentPCB.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.name")  | Boundary Name.  |  
| [`NativeComponentPCB.power`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.power")  | Power dissipation assigned to the PCB.  |  
| [`NativeComponentPCB.preserve_partner_solution`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.preserve_partner_solution")  | Preserve parner solution option.  |  
| [`NativeComponentPCB.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.properties")  | Properties data.  |  
| [`NativeComponentPCB.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.props")  | Retrieve props.  |  
| [`NativeComponentPCB.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.public_dir")  | Shortcut for dir(self).  |  
| [`NativeComponentPCB.targetcs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.targetcs")  | Native Component Coordinate System.  |  
| [`NativeComponentPCB.via_holes_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentPCB.via_holes_material")  | Material applied to via hole regions.  |