---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# MeshRegion 

class ansys.aedt.core.modules.mesh_icepak.MeshRegion(_app_ , _objects =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) 
    
Provides Icepak subregions mesh properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import MeshRegion
>>> obj = MeshRegion()

```
Copy to clipboard
Methods  
| [`MeshRegion.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.create.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.create "ansys.aedt.core.modules.mesh_icepak.MeshRegion.create")()  | Create a mesh region.  |  
| --- | --- |  
| [`MeshRegion.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete "ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete")()  | Delete the mesh region.  |  
| [`MeshRegion.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree "ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MeshRegion.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all "ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MeshRegion.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all "ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MeshRegion.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.update.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.update "ansys.aedt.core.modules.mesh_icepak.MeshRegion.update")()  | Update mesh region settings with the settings in the object variable.  |  
| [`MeshRegion.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property "ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
Attributes  
| [`MeshRegion.assignment`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment "ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment")  | List of objects included in mesh region.  |  
| --- | --- |  
| [`MeshRegion.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.children.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.children "ansys.aedt.core.modules.mesh_icepak.MeshRegion.children")  | Retrieve children.  |  
| [`MeshRegion.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.command.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.command "ansys.aedt.core.modules.mesh_icepak.MeshRegion.command")  | Command of the modeler hystory if available.  |  
| [`MeshRegion.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.name.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.name "ansys.aedt.core.modules.mesh_icepak.MeshRegion.name")  | Name of the mesh region.  |  
| [`MeshRegion.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties "ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties")  | Properties data.  |  
| [`MeshRegion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir "ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir")  | Shortcut for dir(self).  |  
# MeshRegion 

class ansys.aedt.core.modules.mesh_icepak.MeshRegion(_app_ , _objects =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) 
    
Provides Icepak subregions mesh properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import MeshRegion
>>> obj = MeshRegion()

```
Copy to clipboard
Methods  
| [`MeshRegion.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.create.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.create "ansys.aedt.core.modules.mesh_icepak.MeshRegion.create")()  | Create a mesh region.  |  
| --- | --- |  
| [`MeshRegion.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete "ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete")()  | Delete the mesh region.  |  
| [`MeshRegion.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree "ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MeshRegion.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all "ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MeshRegion.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all "ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MeshRegion.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.update.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.update "ansys.aedt.core.modules.mesh_icepak.MeshRegion.update")()  | Update mesh region settings with the settings in the object variable.  |  
| [`MeshRegion.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property "ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
Attributes  
| [`MeshRegion.assignment`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment "ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment")  | List of objects included in mesh region.  |  
| --- | --- |  
| [`MeshRegion.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.children.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.children "ansys.aedt.core.modules.mesh_icepak.MeshRegion.children")  | Retrieve children.  |  
| [`MeshRegion.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.command.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.command "ansys.aedt.core.modules.mesh_icepak.MeshRegion.command")  | Command of the modeler hystory if available.  |  
| [`MeshRegion.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.name.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.name "ansys.aedt.core.modules.mesh_icepak.MeshRegion.name")  | Name of the mesh region.  |  
| [`MeshRegion.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties "ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties")  | Properties data.  |  
| [`MeshRegion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir "ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.rst.txt)

# MeshRegion 

class ansys.aedt.core.modules.mesh_icepak.MeshRegion(_app_ , _objects =None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) 
    
Provides Icepak subregions mesh properties and methods.
Examples

```
>>> from ansys.aedt.core.modules.mesh_icepak import MeshRegion
>>> obj = MeshRegion()

```
Copy to clipboard
Methods  
| [`MeshRegion.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.create.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.create "ansys.aedt.core.modules.mesh_icepak.MeshRegion.create")()  | Create a mesh region.  |  
| --- | --- |  
| [`MeshRegion.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete "ansys.aedt.core.modules.mesh_icepak.MeshRegion.delete")()  | Delete the mesh region.  |  
| [`MeshRegion.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree "ansys.aedt.core.modules.mesh_icepak.MeshRegion.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`MeshRegion.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all "ansys.aedt.core.modules.mesh_icepak.MeshRegion.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`MeshRegion.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all "ansys.aedt.core.modules.mesh_icepak.MeshRegion.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`MeshRegion.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.update.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.update "ansys.aedt.core.modules.mesh_icepak.MeshRegion.update")()  | Update mesh region settings with the settings in the object variable.  |  
| [`MeshRegion.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property "ansys.aedt.core.modules.mesh_icepak.MeshRegion.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
Attributes  
| [`MeshRegion.assignment`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment "ansys.aedt.core.modules.mesh_icepak.MeshRegion.assignment")  | List of objects included in mesh region.  |  
| --- | --- |  
| [`MeshRegion.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.children.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.children "ansys.aedt.core.modules.mesh_icepak.MeshRegion.children")  | Retrieve children.  |  
| [`MeshRegion.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.command.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.command "ansys.aedt.core.modules.mesh_icepak.MeshRegion.command")  | Command of the modeler hystory if available.  |  
| [`MeshRegion.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.name.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.name "ansys.aedt.core.modules.mesh_icepak.MeshRegion.name")  | Name of the mesh region.  |  
| [`MeshRegion.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties "ansys.aedt.core.modules.mesh_icepak.MeshRegion.properties")  | Properties data.  |  
| [`MeshRegion.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir.html#ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir "ansys.aedt.core.modules.mesh_icepak.MeshRegion.public_dir")  | Shortcut for dir(self).  |