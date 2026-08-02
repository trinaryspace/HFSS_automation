---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# MaxwellParameters 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters(_app_ , _name_ , _props =None_, _boundarytype =None_) 
    
Manages parameters data and execution. 

Parameters: 
     

**app**[`ansys.aedt.core.maxwell.Maxwell3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell3d.html#ansys.aedt.core.maxwell.Maxwell3d "ansys.aedt.core.maxwell.Maxwell3d"), [`ansys.aedt.core.maxwell.Maxwell2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell2d.html#ansys.aedt.core.maxwell.Maxwell2d "ansys.aedt.core.maxwell.Maxwell2d") 
    
Either `Maxwell3d` or `Maxwell2d` application. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MaxwellParameters
>>> obj = MaxwellParameters()

```
Copy to clipboard
Methods  
| [`MaxwellParameters.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create")()  | Create a boundary.  |  
| --- | --- |  
| [`MaxwellParameters.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete")()  | Delete the boundary.  |  
| [`MaxwellParameters.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MaxwellParameters.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellParameters.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellParameters.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update")()  | Update the boundary.  |  
| [`MaxwellParameters.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`MaxwellParameters.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties")  | Available properties.  |  
| --- | --- |  
| [`MaxwellParameters.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children")  | Retrieve children.  |  
| [`MaxwellParameters.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command")  | Command of the modeler hystory if available.  |  
| [`MaxwellParameters.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name")  | Boundary Name.  |  
| [`MaxwellParameters.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties")  | Properties data.  |  
| [`MaxwellParameters.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props")  | Maxwell parameter data.  |  
| [`MaxwellParameters.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir")  | Shortcut for dir(self).  |  
# MaxwellParameters 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters(_app_ , _name_ , _props =None_, _boundarytype =None_) 
    
Manages parameters data and execution. 

Parameters: 
     

**app**[`ansys.aedt.core.maxwell.Maxwell3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell3d.html#ansys.aedt.core.maxwell.Maxwell3d "ansys.aedt.core.maxwell.Maxwell3d"), [`ansys.aedt.core.maxwell.Maxwell2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell2d.html#ansys.aedt.core.maxwell.Maxwell2d "ansys.aedt.core.maxwell.Maxwell2d") 
    
Either `Maxwell3d` or `Maxwell2d` application. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MaxwellParameters
>>> obj = MaxwellParameters()

```
Copy to clipboard
Methods  
| [`MaxwellParameters.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create")()  | Create a boundary.  |  
| --- | --- |  
| [`MaxwellParameters.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete")()  | Delete the boundary.  |  
| [`MaxwellParameters.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MaxwellParameters.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellParameters.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellParameters.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update")()  | Update the boundary.  |  
| [`MaxwellParameters.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`MaxwellParameters.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties")  | Available properties.  |  
| --- | --- |  
| [`MaxwellParameters.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children")  | Retrieve children.  |  
| [`MaxwellParameters.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command")  | Command of the modeler hystory if available.  |  
| [`MaxwellParameters.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name")  | Boundary Name.  |  
| [`MaxwellParameters.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties")  | Properties data.  |  
| [`MaxwellParameters.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props")  | Maxwell parameter data.  |  
| [`MaxwellParameters.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.rst.txt)

# MaxwellParameters 

class ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters(_app_ , _name_ , _props =None_, _boundarytype =None_) 
    
Manages parameters data and execution. 

Parameters: 
     

**app**[`ansys.aedt.core.maxwell.Maxwell3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell3d.html#ansys.aedt.core.maxwell.Maxwell3d "ansys.aedt.core.maxwell.Maxwell3d"), [`ansys.aedt.core.maxwell.Maxwell2d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.maxwell.Maxwell2d.html#ansys.aedt.core.maxwell.Maxwell2d "ansys.aedt.core.maxwell.Maxwell2d") 
    
Either `Maxwell3d` or `Maxwell2d` application. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the boundary. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the boundary. 

**boundarytype**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the boundary.
Examples

```
>>> from ansys.aedt.core.modules.boundary.maxwell_boundary import MaxwellParameters
>>> obj = MaxwellParameters()

```
Copy to clipboard
Methods  
| [`MaxwellParameters.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.create")()  | Create a boundary.  |  
| --- | --- |  
| [`MaxwellParameters.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.delete")()  | Delete the boundary.  |  
| [`MaxwellParameters.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MaxwellParameters.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellParameters.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MaxwellParameters.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update")()  | Update the boundary.  |  
| [`MaxwellParameters.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`MaxwellParameters.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.available_properties")  | Available properties.  |  
| --- | --- |  
| [`MaxwellParameters.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.children")  | Retrieve children.  |  
| [`MaxwellParameters.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.command")  | Command of the modeler hystory if available.  |  
| [`MaxwellParameters.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.name")  | Boundary Name.  |  
| [`MaxwellParameters.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.properties")  | Properties data.  |  
| [`MaxwellParameters.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.props")  | Maxwell parameter data.  |  
| [`MaxwellParameters.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir.html#ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir "ansys.aedt.core.modules.boundary.maxwell_boundary.MaxwellParameters.public_dir")  | Shortcut for dir(self).  |