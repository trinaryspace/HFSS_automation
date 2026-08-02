---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# NativeComponentObject 

class ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject(_app_ , _component_type_ , _component_name_ , _props_) 
    
Manages Native Component data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the component. 

**component_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the component. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Properties of the boundary.
Examples
This example the par_beam returned object is a [`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject").

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> ffd_file = "path/to/ffdfile.ffd"
>>> par_beam = hfss.create_sbr_file_based_antenna(ffd_file)
>>> par_beam.native_properties["Size"] = "0.1mm"
>>> par_beam.update()
>>> par_beam.delete()

```
Copy to clipboard
Methods  
| [`NativeComponentObject.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create")()  | Create a Native Component in AEDT.  |  
| --- | --- |  
| [`NativeComponentObject.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete")()  | Delete the Native Component in AEDT.  |  
| [`NativeComponentObject.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NativeComponentObject.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentObject.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentObject.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update")()  | Update the Native Component in AEDT.  |  
| [`NativeComponentObject.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NativeComponentObject.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NativeComponentObject.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children")  | Retrieve children.  |  
| [`NativeComponentObject.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command")  | Command of the modeler hystory if available.  |  
| [`NativeComponentObject.definition_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name")  | Definition name of the native component.  |  
| [`NativeComponentObject.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name")  | Boundary Name.  |  
| [`NativeComponentObject.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties")  | Properties data.  |  
| [`NativeComponentObject.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props")  | Retrieve props.  |  
| [`NativeComponentObject.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir")  | Shortcut for dir(self).  |  
| [`NativeComponentObject.targetcs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs")  | Native Component Coordinate System.  |  
# NativeComponentObject 

class ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject(_app_ , _component_type_ , _component_name_ , _props_) 
    
Manages Native Component data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the component. 

**component_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the component. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Properties of the boundary.
Examples
This example the par_beam returned object is a [`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject").

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> ffd_file = "path/to/ffdfile.ffd"
>>> par_beam = hfss.create_sbr_file_based_antenna(ffd_file)
>>> par_beam.native_properties["Size"] = "0.1mm"
>>> par_beam.update()
>>> par_beam.delete()

```
Copy to clipboard
Methods  
| [`NativeComponentObject.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create")()  | Create a Native Component in AEDT.  |  
| --- | --- |  
| [`NativeComponentObject.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete")()  | Delete the Native Component in AEDT.  |  
| [`NativeComponentObject.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NativeComponentObject.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentObject.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentObject.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update")()  | Update the Native Component in AEDT.  |  
| [`NativeComponentObject.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NativeComponentObject.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NativeComponentObject.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children")  | Retrieve children.  |  
| [`NativeComponentObject.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command")  | Command of the modeler hystory if available.  |  
| [`NativeComponentObject.definition_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name")  | Definition name of the native component.  |  
| [`NativeComponentObject.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name")  | Boundary Name.  |  
| [`NativeComponentObject.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties")  | Properties data.  |  
| [`NativeComponentObject.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props")  | Retrieve props.  |  
| [`NativeComponentObject.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir")  | Shortcut for dir(self).  |  
| [`NativeComponentObject.targetcs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs")  | Native Component Coordinate System.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.rst.txt)

# NativeComponentObject 

class ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject(_app_ , _component_type_ , _component_name_ , _props_) 
    
Manages Native Component data and execution. 

Parameters: 
     

**app**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
An AEDT application from `ansys.aedt.core.application`. 

**component_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the component. 

**component_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the component. 

**props**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Properties of the boundary.
Examples
This example the par_beam returned object is a [`ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject").

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> ffd_file = "path/to/ffdfile.ffd"
>>> par_beam = hfss.create_sbr_file_based_antenna(ffd_file)
>>> par_beam.native_properties["Size"] = "0.1mm"
>>> par_beam.update()
>>> par_beam.delete()

```
Copy to clipboard
Methods  
| [`NativeComponentObject.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.create")()  | Create a Native Component in AEDT.  |  
| --- | --- |  
| [`NativeComponentObject.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.delete")()  | Delete the Native Component in AEDT.  |  
| [`NativeComponentObject.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`NativeComponentObject.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentObject.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`NativeComponentObject.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update")()  | Update the Native Component in AEDT.  |  
| [`NativeComponentObject.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.update_property")(...)  | Update the property of the binary tree node.  |  
Attributes  
| [`NativeComponentObject.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.available_properties")  | Available properties.  |  
| --- | --- |  
| [`NativeComponentObject.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.children")  | Retrieve children.  |  
| [`NativeComponentObject.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.command")  | Command of the modeler hystory if available.  |  
| [`NativeComponentObject.definition_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.definition_name")  | Definition name of the native component.  |  
| [`NativeComponentObject.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.name")  | Boundary Name.  |  
| [`NativeComponentObject.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.properties")  | Properties data.  |  
| [`NativeComponentObject.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.props")  | Retrieve props.  |  
| [`NativeComponentObject.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.public_dir")  | Shortcut for dir(self).  |  
| [`NativeComponentObject.targetcs`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs.html#ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs "ansys.aedt.core.modules.boundary.layout_boundary.NativeComponentObject.targetcs")  | Native Component Coordinate System.  |