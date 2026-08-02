---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# BoundaryObject 

class ansys.aedt.core.modules.boundary.common.BoundaryObject(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _boundarytype =None_, _auto_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages boundary data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the boundary.
Examples
Create a cylinder at the XY working plane and assign a copper coating of 0.2 mm to it. The Coating is a boundary operation and coat will return a `ansys.aedt.core.modules.boundary.common.BoundaryObject`

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Plane
>>> hfss = Hfss()
>>> origin = hfss.modeler.Position(0, 0, 0)
>>> inner = hfss.modeler.create_cylinder(Plane.XY, origin, 3, 200, 0, "inner")
>>> inner_id = hfss.modeler.get_obj_id(
...     "inner",
... )
>>> coat = hfss.assign_finite_conductivity([inner_id], "copper", use_thickness=True, thickness="0.2mm")

```
Copy to clipboard
Methods  
| [`BoundaryObject.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.create.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.create "ansys.aedt.core.modules.boundary.common.BoundaryObject.create")()  | Create a boundary.  |  
| --- | --- |  
| [`BoundaryObject.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.delete.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.delete "ansys.aedt.core.modules.boundary.common.BoundaryObject.delete")()  | Delete the boundary.  |  
| [`BoundaryObject.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree "ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`BoundaryObject.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all "ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all "ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update "ansys.aedt.core.modules.boundary.common.BoundaryObject.update")()  | Update the boundary.  |  
| [`BoundaryObject.update_assignment`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment "ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment")()  | Update the boundary assignment.  |  
| [`BoundaryObject.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property "ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BoundaryObject.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties "ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties")  | Available properties.  |  
| --- | --- |  
| [`BoundaryObject.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.children.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.children "ansys.aedt.core.modules.boundary.common.BoundaryObject.children")  | Retrieve children.  |  
| [`BoundaryObject.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.command.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.command "ansys.aedt.core.modules.boundary.common.BoundaryObject.command")  | Command of the modeler hystory if available.  |  
| [`BoundaryObject.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.name.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.name "ansys.aedt.core.modules.boundary.common.BoundaryObject.name")  | Boundary Name.  |  
| [`BoundaryObject.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.properties.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.properties "ansys.aedt.core.modules.boundary.common.BoundaryObject.properties")  | Properties data.  |  
| [`BoundaryObject.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.props.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.props "ansys.aedt.core.modules.boundary.common.BoundaryObject.props")  | Boundary data.  |  
| [`BoundaryObject.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir "ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir")  | Shortcut for dir(self).  |  
| [`BoundaryObject.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.type.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.type "ansys.aedt.core.modules.boundary.common.BoundaryObject.type")  | Boundary type.  |  
# BoundaryObject 

class ansys.aedt.core.modules.boundary.common.BoundaryObject(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _boundarytype =None_, _auto_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages boundary data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the boundary.
Examples
Create a cylinder at the XY working plane and assign a copper coating of 0.2 mm to it. The Coating is a boundary operation and coat will return a `ansys.aedt.core.modules.boundary.common.BoundaryObject`

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Plane
>>> hfss = Hfss()
>>> origin = hfss.modeler.Position(0, 0, 0)
>>> inner = hfss.modeler.create_cylinder(Plane.XY, origin, 3, 200, 0, "inner")
>>> inner_id = hfss.modeler.get_obj_id(
...     "inner",
... )
>>> coat = hfss.assign_finite_conductivity([inner_id], "copper", use_thickness=True, thickness="0.2mm")

```
Copy to clipboard
Methods  
| [`BoundaryObject.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.create.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.create "ansys.aedt.core.modules.boundary.common.BoundaryObject.create")()  | Create a boundary.  |  
| --- | --- |  
| [`BoundaryObject.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.delete.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.delete "ansys.aedt.core.modules.boundary.common.BoundaryObject.delete")()  | Delete the boundary.  |  
| [`BoundaryObject.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree "ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`BoundaryObject.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all "ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all "ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update "ansys.aedt.core.modules.boundary.common.BoundaryObject.update")()  | Update the boundary.  |  
| [`BoundaryObject.update_assignment`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment "ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment")()  | Update the boundary assignment.  |  
| [`BoundaryObject.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property "ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BoundaryObject.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties "ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties")  | Available properties.  |  
| --- | --- |  
| [`BoundaryObject.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.children.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.children "ansys.aedt.core.modules.boundary.common.BoundaryObject.children")  | Retrieve children.  |  
| [`BoundaryObject.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.command.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.command "ansys.aedt.core.modules.boundary.common.BoundaryObject.command")  | Command of the modeler hystory if available.  |  
| [`BoundaryObject.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.name.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.name "ansys.aedt.core.modules.boundary.common.BoundaryObject.name")  | Boundary Name.  |  
| [`BoundaryObject.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.properties.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.properties "ansys.aedt.core.modules.boundary.common.BoundaryObject.properties")  | Properties data.  |  
| [`BoundaryObject.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.props.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.props "ansys.aedt.core.modules.boundary.common.BoundaryObject.props")  | Boundary data.  |  
| [`BoundaryObject.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir "ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir")  | Shortcut for dir(self).  |  
| [`BoundaryObject.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.type.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.type "ansys.aedt.core.modules.boundary.common.BoundaryObject.type")  | Boundary type.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.rst.txt)

# BoundaryObject 

class ansys.aedt.core.modules.boundary.common.BoundaryObject(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _boundarytype =None_, _auto_update : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Manages boundary data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the boundary.
Examples
Create a cylinder at the XY working plane and assign a copper coating of 0.2 mm to it. The Coating is a boundary operation and coat will return a `ansys.aedt.core.modules.boundary.common.BoundaryObject`

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Plane
>>> hfss = Hfss()
>>> origin = hfss.modeler.Position(0, 0, 0)
>>> inner = hfss.modeler.create_cylinder(Plane.XY, origin, 3, 200, 0, "inner")
>>> inner_id = hfss.modeler.get_obj_id(
...     "inner",
... )
>>> coat = hfss.assign_finite_conductivity([inner_id], "copper", use_thickness=True, thickness="0.2mm")

```
Copy to clipboard
Methods  
| [`BoundaryObject.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.create.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.create "ansys.aedt.core.modules.boundary.common.BoundaryObject.create")()  | Create a boundary.  |  
| --- | --- |  
| [`BoundaryObject.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.delete.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.delete "ansys.aedt.core.modules.boundary.common.BoundaryObject.delete")()  | Delete the boundary.  |  
| [`BoundaryObject.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree "ansys.aedt.core.modules.boundary.common.BoundaryObject.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`BoundaryObject.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all "ansys.aedt.core.modules.boundary.common.BoundaryObject.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all "ansys.aedt.core.modules.boundary.common.BoundaryObject.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update "ansys.aedt.core.modules.boundary.common.BoundaryObject.update")()  | Update the boundary.  |  
| [`BoundaryObject.update_assignment`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment "ansys.aedt.core.modules.boundary.common.BoundaryObject.update_assignment")()  | Update the boundary assignment.  |  
| [`BoundaryObject.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property "ansys.aedt.core.modules.boundary.common.BoundaryObject.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BoundaryObject.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties "ansys.aedt.core.modules.boundary.common.BoundaryObject.available_properties")  | Available properties.  |  
| --- | --- |  
| [`BoundaryObject.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.children.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.children "ansys.aedt.core.modules.boundary.common.BoundaryObject.children")  | Retrieve children.  |  
| [`BoundaryObject.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.command.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.command "ansys.aedt.core.modules.boundary.common.BoundaryObject.command")  | Command of the modeler hystory if available.  |  
| [`BoundaryObject.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.name.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.name "ansys.aedt.core.modules.boundary.common.BoundaryObject.name")  | Boundary Name.  |  
| [`BoundaryObject.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.properties.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.properties "ansys.aedt.core.modules.boundary.common.BoundaryObject.properties")  | Properties data.  |  
| [`BoundaryObject.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.props.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.props "ansys.aedt.core.modules.boundary.common.BoundaryObject.props")  | Boundary data.  |  
| [`BoundaryObject.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir "ansys.aedt.core.modules.boundary.common.BoundaryObject.public_dir")  | Shortcut for dir(self).  |  
| [`BoundaryObject.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.type.html#ansys.aedt.core.modules.boundary.common.BoundaryObject.type "ansys.aedt.core.modules.boundary.common.BoundaryObject.type")  | Boundary type.  |