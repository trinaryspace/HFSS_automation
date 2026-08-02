---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# BoundaryObject3dLayout 

class ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _boundarytype : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Port'_) 
    
Manages boundary data and execution for Hfss3dLayout. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.layout_boundary import BoundaryObject3dLayout
>>> obj = BoundaryObject3dLayout()

```
Copy to clipboard
Methods  
| [`BoundaryObject3dLayout.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete")()  | Delete the boundary.  |  
| --- | --- |  
| [`BoundaryObject3dLayout.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`BoundaryObject3dLayout.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject3dLayout.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject3dLayout.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update")()  | Update the boundary.  |  
| [`BoundaryObject3dLayout.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BoundaryObject3dLayout.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties")  | Available properties.  |  
| --- | --- |  
| [`BoundaryObject3dLayout.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children")  | Retrieve children.  |  
| [`BoundaryObject3dLayout.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command")  | Command of the modeler hystory if available.  |  
| [`BoundaryObject3dLayout.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name")  | Boundary Name.  |  
| [`BoundaryObject3dLayout.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties")  | Properties data.  |  
| [`BoundaryObject3dLayout.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props")  | Excitation data.  |  
| [`BoundaryObject3dLayout.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir")  | Shortcut for dir(self).  |  
# BoundaryObject3dLayout 

class ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _boundarytype : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Port'_) 
    
Manages boundary data and execution for Hfss3dLayout. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.layout_boundary import BoundaryObject3dLayout
>>> obj = BoundaryObject3dLayout()

```
Copy to clipboard
Methods  
| [`BoundaryObject3dLayout.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete")()  | Delete the boundary.  |  
| --- | --- |  
| [`BoundaryObject3dLayout.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`BoundaryObject3dLayout.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject3dLayout.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject3dLayout.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update")()  | Update the boundary.  |  
| [`BoundaryObject3dLayout.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BoundaryObject3dLayout.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties")  | Available properties.  |  
| --- | --- |  
| [`BoundaryObject3dLayout.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children")  | Retrieve children.  |  
| [`BoundaryObject3dLayout.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command")  | Command of the modeler hystory if available.  |  
| [`BoundaryObject3dLayout.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name")  | Boundary Name.  |  
| [`BoundaryObject3dLayout.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties")  | Properties data.  |  
| [`BoundaryObject3dLayout.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props")  | Excitation data.  |  
| [`BoundaryObject3dLayout.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.rst.txt)

# BoundaryObject3dLayout 

class ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _props =None_, _boundarytype : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Port'_) 
    
Manages boundary data and execution for Hfss3dLayout. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.layout_boundary import BoundaryObject3dLayout
>>> obj = BoundaryObject3dLayout()

```
Copy to clipboard
Methods  
| [`BoundaryObject3dLayout.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.delete")()  | Delete the boundary.  |  
| --- | --- |  
| [`BoundaryObject3dLayout.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`BoundaryObject3dLayout.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject3dLayout.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`BoundaryObject3dLayout.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update")()  | Update the boundary.  |  
| [`BoundaryObject3dLayout.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`BoundaryObject3dLayout.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.available_properties")  | Available properties.  |  
| --- | --- |  
| [`BoundaryObject3dLayout.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.children")  | Retrieve children.  |  
| [`BoundaryObject3dLayout.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.command")  | Command of the modeler hystory if available.  |  
| [`BoundaryObject3dLayout.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.name")  | Boundary Name.  |  
| [`BoundaryObject3dLayout.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.properties")  | Properties data.  |  
| [`BoundaryObject3dLayout.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.props")  | Excitation data.  |  
| [`BoundaryObject3dLayout.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.BoundaryObject3dLayout.public_dir")  | Shortcut for dir(self).  |