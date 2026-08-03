---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# Setup 

class ansys.aedt.core.modules.solve_setup.Setup(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates a 3D setup. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis.Analysis` 
    
Inherited app object. 

**solution_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the setup. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `"MySetupAuto"`. 

**is_new_setup**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the setup from a template. The default is `True`. If `False`, access is to the existing setup.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> setup = app.create_setup()

```
Copy to clipboard
Methods  
| [`Setup.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link "ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link")(design[, solution, ...])  | Import mesh from a source design solution to the target design.  |  
| --- | --- |  
| [`Setup.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.analyze.html#ansys.aedt.core.modules.solve_setup.Setup.analyze "ansys.aedt.core.modules.solve_setup.Setup.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`Setup.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.create.html#ansys.aedt.core.modules.solve_setup.Setup.create "ansys.aedt.core.modules.solve_setup.Setup.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`Setup.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.create_report.html#ansys.aedt.core.modules.solve_setup.Setup.create_report "ansys.aedt.core.modules.solve_setup.Setup.create_report")([expressions, domain, ...])  | Create a report in AEDT.  |  
| [`Setup.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.delete.html#ansys.aedt.core.modules.solve_setup.Setup.delete "ansys.aedt.core.modules.solve_setup.Setup.delete")()  | Delete actual Setup.  |  
| [`Setup.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.disable.html#ansys.aedt.core.modules.solve_setup.Setup.disable "ansys.aedt.core.modules.solve_setup.Setup.disable")()  | Disable a setup.  |  
| [`Setup.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.enable.html#ansys.aedt.core.modules.solve_setup.Setup.enable "ansys.aedt.core.modules.solve_setup.Setup.enable")()  | Enable a setup.  |  
| [`Setup.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache "ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache")(expressions[, ...])  | Enable an expression cache.  |  
| [`Setup.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.get_profile.html#ansys.aedt.core.modules.solve_setup.Setup.get_profile "ansys.aedt.core.modules.solve_setup.Setup.get_profile")()  | Solution profile.  |  
| [`Setup.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.get_solution_data.html#ansys.aedt.core.modules.solve_setup.Setup.get_solution_data "ansys.aedt.core.modules.solve_setup.Setup.get_solution_data")([expressions, ...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`Setup.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree "ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`Setup.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`Setup.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.suppress_all.html#ansys.aedt.core.modules.solve_setup.Setup.suppress_all "ansys.aedt.core.modules.solve_setup.Setup.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`Setup.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all "ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`Setup.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.update.html#ansys.aedt.core.modules.solve_setup.Setup.update "ansys.aedt.core.modules.solve_setup.Setup.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`Setup.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.update_property.html#ansys.aedt.core.modules.solve_setup.Setup.update_property "ansys.aedt.core.modules.solve_setup.Setup.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
Attributes  
| [`Setup.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.available_properties.html#ansys.aedt.core.modules.solve_setup.Setup.available_properties "ansys.aedt.core.modules.solve_setup.Setup.available_properties")  | Available properties.  |  
| --- | --- |  
| [`Setup.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.children.html#ansys.aedt.core.modules.solve_setup.Setup.children "ansys.aedt.core.modules.solve_setup.Setup.children")  | Retrieve children.  |  
| [`Setup.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.command.html#ansys.aedt.core.modules.solve_setup.Setup.command "ansys.aedt.core.modules.solve_setup.Setup.command")  | Command of the modeler hystory if available.  |  
| [`Setup.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics "ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`Setup.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.is_solved.html#ansys.aedt.core.modules.solve_setup.Setup.is_solved "ansys.aedt.core.modules.solve_setup.Setup.is_solved")  | Verify if solutions are available for given setup.  |  
| [`Setup.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.name.html#ansys.aedt.core.modules.solve_setup.Setup.name "ansys.aedt.core.modules.solve_setup.Setup.name")  | Name.  |  
| [`Setup.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.omodule.html#ansys.aedt.core.modules.solve_setup.Setup.omodule "ansys.aedt.core.modules.solve_setup.Setup.omodule")  | Analysis module.  |  
| [`Setup.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.properties.html#ansys.aedt.core.modules.solve_setup.Setup.properties "ansys.aedt.core.modules.solve_setup.Setup.properties")  | Properties data.  |  
| [`Setup.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.props.html#ansys.aedt.core.modules.solve_setup.Setup.props "ansys.aedt.core.modules.solve_setup.Setup.props")  | Properties of the setup.  |  
| [`Setup.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.public_dir.html#ansys.aedt.core.modules.solve_setup.Setup.public_dir "ansys.aedt.core.modules.solve_setup.Setup.public_dir")  | Shortcut for dir(self).  |  
| [`Setup.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.sweeps.html#ansys.aedt.core.modules.solve_setup.Setup.sweeps "ansys.aedt.core.modules.solve_setup.Setup.sweeps")  | Retrieve sweeps.  |  
# Setup 

class ansys.aedt.core.modules.solve_setup.Setup(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates a 3D setup. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis.Analysis` 
    
Inherited app object. 

**solution_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the setup. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `"MySetupAuto"`. 

**is_new_setup**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the setup from a template. The default is `True`. If `False`, access is to the existing setup.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> setup = app.create_setup()

```
Copy to clipboard
Methods  
| [`Setup.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link "ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link")(design[, solution, ...])  | Import mesh from a source design solution to the target design.  |  
| --- | --- |  
| [`Setup.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.analyze.html#ansys.aedt.core.modules.solve_setup.Setup.analyze "ansys.aedt.core.modules.solve_setup.Setup.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`Setup.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.create.html#ansys.aedt.core.modules.solve_setup.Setup.create "ansys.aedt.core.modules.solve_setup.Setup.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`Setup.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.create_report.html#ansys.aedt.core.modules.solve_setup.Setup.create_report "ansys.aedt.core.modules.solve_setup.Setup.create_report")([expressions, domain, ...])  | Create a report in AEDT.  |  
| [`Setup.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.delete.html#ansys.aedt.core.modules.solve_setup.Setup.delete "ansys.aedt.core.modules.solve_setup.Setup.delete")()  | Delete actual Setup.  |  
| [`Setup.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.disable.html#ansys.aedt.core.modules.solve_setup.Setup.disable "ansys.aedt.core.modules.solve_setup.Setup.disable")()  | Disable a setup.  |  
| [`Setup.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.enable.html#ansys.aedt.core.modules.solve_setup.Setup.enable "ansys.aedt.core.modules.solve_setup.Setup.enable")()  | Enable a setup.  |  
| [`Setup.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache "ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache")(expressions[, ...])  | Enable an expression cache.  |  
| [`Setup.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.get_profile.html#ansys.aedt.core.modules.solve_setup.Setup.get_profile "ansys.aedt.core.modules.solve_setup.Setup.get_profile")()  | Solution profile.  |  
| [`Setup.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.get_solution_data.html#ansys.aedt.core.modules.solve_setup.Setup.get_solution_data "ansys.aedt.core.modules.solve_setup.Setup.get_solution_data")([expressions, ...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`Setup.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree "ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`Setup.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`Setup.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.suppress_all.html#ansys.aedt.core.modules.solve_setup.Setup.suppress_all "ansys.aedt.core.modules.solve_setup.Setup.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`Setup.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all "ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`Setup.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.update.html#ansys.aedt.core.modules.solve_setup.Setup.update "ansys.aedt.core.modules.solve_setup.Setup.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`Setup.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.update_property.html#ansys.aedt.core.modules.solve_setup.Setup.update_property "ansys.aedt.core.modules.solve_setup.Setup.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
Attributes  
| [`Setup.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.available_properties.html#ansys.aedt.core.modules.solve_setup.Setup.available_properties "ansys.aedt.core.modules.solve_setup.Setup.available_properties")  | Available properties.  |  
| --- | --- |  
| [`Setup.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.children.html#ansys.aedt.core.modules.solve_setup.Setup.children "ansys.aedt.core.modules.solve_setup.Setup.children")  | Retrieve children.  |  
| [`Setup.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.command.html#ansys.aedt.core.modules.solve_setup.Setup.command "ansys.aedt.core.modules.solve_setup.Setup.command")  | Command of the modeler hystory if available.  |  
| [`Setup.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics "ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`Setup.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.is_solved.html#ansys.aedt.core.modules.solve_setup.Setup.is_solved "ansys.aedt.core.modules.solve_setup.Setup.is_solved")  | Verify if solutions are available for given setup.  |  
| [`Setup.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.name.html#ansys.aedt.core.modules.solve_setup.Setup.name "ansys.aedt.core.modules.solve_setup.Setup.name")  | Name.  |  
| [`Setup.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.omodule.html#ansys.aedt.core.modules.solve_setup.Setup.omodule "ansys.aedt.core.modules.solve_setup.Setup.omodule")  | Analysis module.  |  
| [`Setup.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.properties.html#ansys.aedt.core.modules.solve_setup.Setup.properties "ansys.aedt.core.modules.solve_setup.Setup.properties")  | Properties data.  |  
| [`Setup.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.props.html#ansys.aedt.core.modules.solve_setup.Setup.props "ansys.aedt.core.modules.solve_setup.Setup.props")  | Properties of the setup.  |  
| [`Setup.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.public_dir.html#ansys.aedt.core.modules.solve_setup.Setup.public_dir "ansys.aedt.core.modules.solve_setup.Setup.public_dir")  | Shortcut for dir(self).  |  
| [`Setup.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.sweeps.html#ansys.aedt.core.modules.solve_setup.Setup.sweeps "ansys.aedt.core.modules.solve_setup.Setup.sweeps")  | Retrieve sweeps.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.rst.txt)

# Setup 

class ansys.aedt.core.modules.solve_setup.Setup(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates a 3D setup. 

Parameters: 
     

**app**`ansys.aedt.core.application.analysis.Analysis` 
    
Inherited app object. 

**solution_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the setup. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `"MySetupAuto"`. 

**is_new_setup**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the setup from a template. The default is `True`. If `False`, access is to the existing setup.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> setup = app.create_setup()

```
Copy to clipboard
Methods  
| [`Setup.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link "ansys.aedt.core.modules.solve_setup.Setup.add_mesh_link")(design[, solution, ...])  | Import mesh from a source design solution to the target design.  |  
| --- | --- |  
| [`Setup.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.analyze.html#ansys.aedt.core.modules.solve_setup.Setup.analyze "ansys.aedt.core.modules.solve_setup.Setup.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`Setup.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.create.html#ansys.aedt.core.modules.solve_setup.Setup.create "ansys.aedt.core.modules.solve_setup.Setup.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`Setup.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.create_report.html#ansys.aedt.core.modules.solve_setup.Setup.create_report "ansys.aedt.core.modules.solve_setup.Setup.create_report")([expressions, domain, ...])  | Create a report in AEDT.  |  
| [`Setup.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.delete.html#ansys.aedt.core.modules.solve_setup.Setup.delete "ansys.aedt.core.modules.solve_setup.Setup.delete")()  | Delete actual Setup.  |  
| [`Setup.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.disable.html#ansys.aedt.core.modules.solve_setup.Setup.disable "ansys.aedt.core.modules.solve_setup.Setup.disable")()  | Disable a setup.  |  
| [`Setup.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.enable.html#ansys.aedt.core.modules.solve_setup.Setup.enable "ansys.aedt.core.modules.solve_setup.Setup.enable")()  | Enable a setup.  |  
| [`Setup.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache "ansys.aedt.core.modules.solve_setup.Setup.enable_expression_cache")(expressions[, ...])  | Enable an expression cache.  |  
| [`Setup.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.get_profile.html#ansys.aedt.core.modules.solve_setup.Setup.get_profile "ansys.aedt.core.modules.solve_setup.Setup.get_profile")()  | Solution profile.  |  
| [`Setup.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.get_solution_data.html#ansys.aedt.core.modules.solve_setup.Setup.get_solution_data "ansys.aedt.core.modules.solve_setup.Setup.get_solution_data")([expressions, ...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`Setup.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree "ansys.aedt.core.modules.solve_setup.Setup.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`Setup.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.Setup.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`Setup.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.suppress_all.html#ansys.aedt.core.modules.solve_setup.Setup.suppress_all "ansys.aedt.core.modules.solve_setup.Setup.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`Setup.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all "ansys.aedt.core.modules.solve_setup.Setup.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`Setup.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.update.html#ansys.aedt.core.modules.solve_setup.Setup.update "ansys.aedt.core.modules.solve_setup.Setup.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`Setup.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.update_property.html#ansys.aedt.core.modules.solve_setup.Setup.update_property "ansys.aedt.core.modules.solve_setup.Setup.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
Attributes  
| [`Setup.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.available_properties.html#ansys.aedt.core.modules.solve_setup.Setup.available_properties "ansys.aedt.core.modules.solve_setup.Setup.available_properties")  | Available properties.  |  
| --- | --- |  
| [`Setup.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.children.html#ansys.aedt.core.modules.solve_setup.Setup.children "ansys.aedt.core.modules.solve_setup.Setup.children")  | Retrieve children.  |  
| [`Setup.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.command.html#ansys.aedt.core.modules.solve_setup.Setup.command "ansys.aedt.core.modules.solve_setup.Setup.command")  | Command of the modeler hystory if available.  |  
| [`Setup.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics "ansys.aedt.core.modules.solve_setup.Setup.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`Setup.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.is_solved.html#ansys.aedt.core.modules.solve_setup.Setup.is_solved "ansys.aedt.core.modules.solve_setup.Setup.is_solved")  | Verify if solutions are available for given setup.  |  
| [`Setup.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.name.html#ansys.aedt.core.modules.solve_setup.Setup.name "ansys.aedt.core.modules.solve_setup.Setup.name")  | Name.  |  
| [`Setup.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.omodule.html#ansys.aedt.core.modules.solve_setup.Setup.omodule "ansys.aedt.core.modules.solve_setup.Setup.omodule")  | Analysis module.  |  
| [`Setup.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.properties.html#ansys.aedt.core.modules.solve_setup.Setup.properties "ansys.aedt.core.modules.solve_setup.Setup.properties")  | Properties data.  |  
| [`Setup.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.props.html#ansys.aedt.core.modules.solve_setup.Setup.props "ansys.aedt.core.modules.solve_setup.Setup.props")  | Properties of the setup.  |  
| [`Setup.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.public_dir.html#ansys.aedt.core.modules.solve_setup.Setup.public_dir "ansys.aedt.core.modules.solve_setup.Setup.public_dir")  | Shortcut for dir(self).  |  
| [`Setup.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.sweeps.html#ansys.aedt.core.modules.solve_setup.Setup.sweeps "ansys.aedt.core.modules.solve_setup.Setup.sweeps")  | Retrieve sweeps.  |