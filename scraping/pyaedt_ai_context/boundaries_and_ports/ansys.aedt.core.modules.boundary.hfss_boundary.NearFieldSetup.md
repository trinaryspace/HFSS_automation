---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# NearFieldSetup 

class ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup(_app_ , _component_name_ , _props_ , _component_type_) 
    
Manages Near Field Component data and execution.
Examples
In this example the rectangle1 returned object is a `ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup`

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> rectangle1 = hfss.insert_near_field_rectangle()

```
Copy to clipboard
Methods  
| [`NearFieldSetup.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create")()  | Create a Field Setup Component in HFSS.  |  
| --- | --- |  
| [`NearFieldSetup.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete")()  | Delete the Field Setup in AEDT.  |  
| [`NearFieldSetup.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NearFieldSetup.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NearFieldSetup.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NearFieldSetup.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update")()  | Update the Field Setup in AEDT.  |  
| [`NearFieldSetup.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NearFieldSetup.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NearFieldSetup.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children")  | Retrieve children.  |  
| [`NearFieldSetup.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command")  | Command of the modeler hystory if available.  |  
| [`NearFieldSetup.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name")  | Boundary Name.  |  
| [`NearFieldSetup.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties")  | Properties data.  |  
| [`NearFieldSetup.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props")  | Field Properties.  |  
| [`NearFieldSetup.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir")  | Shortcut for dir(self).  |  
# NearFieldSetup 

class ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup(_app_ , _component_name_ , _props_ , _component_type_) 
    
Manages Near Field Component data and execution.
Examples
In this example the rectangle1 returned object is a `ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup`

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> rectangle1 = hfss.insert_near_field_rectangle()

```
Copy to clipboard
Methods  
| [`NearFieldSetup.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create")()  | Create a Field Setup Component in HFSS.  |  
| --- | --- |  
| [`NearFieldSetup.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete")()  | Delete the Field Setup in AEDT.  |  
| [`NearFieldSetup.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NearFieldSetup.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NearFieldSetup.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NearFieldSetup.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update")()  | Update the Field Setup in AEDT.  |  
| [`NearFieldSetup.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NearFieldSetup.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NearFieldSetup.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children")  | Retrieve children.  |  
| [`NearFieldSetup.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command")  | Command of the modeler hystory if available.  |  
| [`NearFieldSetup.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name")  | Boundary Name.  |  
| [`NearFieldSetup.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties")  | Properties data.  |  
| [`NearFieldSetup.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props")  | Field Properties.  |  
| [`NearFieldSetup.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.rst.txt)

# NearFieldSetup 

class ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup(_app_ , _component_name_ , _props_ , _component_type_) 
    
Manages Near Field Component data and execution.
Examples
In this example the rectangle1 returned object is a `ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup`

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> rectangle1 = hfss.insert_near_field_rectangle()

```
Copy to clipboard
Methods  
| [`NearFieldSetup.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.create")()  | Create a Field Setup Component in HFSS.  |  
| --- | --- |  
| [`NearFieldSetup.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.delete")()  | Delete the Field Setup in AEDT.  |  
| [`NearFieldSetup.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NearFieldSetup.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NearFieldSetup.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NearFieldSetup.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update")()  | Update the Field Setup in AEDT.  |  
| [`NearFieldSetup.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NearFieldSetup.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NearFieldSetup.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.children")  | Retrieve children.  |  
| [`NearFieldSetup.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.command")  | Command of the modeler hystory if available.  |  
| [`NearFieldSetup.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.name")  | Boundary Name.  |  
| [`NearFieldSetup.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.properties")  | Properties data.  |  
| [`NearFieldSetup.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.props")  | Field Properties.  |  
| [`NearFieldSetup.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir.html#ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir "ansys.aedt.core.modules.boundary.hfss_boundary.NearFieldSetup.public_dir")  | Shortcut for dir(self).  |