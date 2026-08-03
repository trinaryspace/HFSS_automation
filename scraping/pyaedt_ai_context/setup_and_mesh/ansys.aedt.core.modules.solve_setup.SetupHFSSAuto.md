---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# SetupHFSSAuto 

class ansys.aedt.core.modules.solve_setup.SetupHFSSAuto(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates an HFSS Auto setup. 

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
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1", setup_type="HFSSDrivenAuto")

```
Copy to clipboard
Methods  
| [`SetupHFSSAuto.add_derivatives`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives")(derivative_list)  | Add derivatives to the setup.  |  
| --- | --- |  
| [`SetupHFSSAuto.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link")(design[, ...])  | Import mesh from a source design solution to the target design.  |  
| [`SetupHFSSAuto.add_subrange`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange")(range_type, start)  | Add a subrange to the sweep.  |  
| [`SetupHFSSAuto.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupHFSSAuto.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`SetupHFSSAuto.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report")([expressions, ...])  | Create a report in AEDT.  |  
| [`SetupHFSSAuto.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete")()  | Delete actual Setup.  |  
| [`SetupHFSSAuto.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable")()  | Disable a setup.  |  
| [`SetupHFSSAuto.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable")()  | Enable a setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_broadband`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband")(...)  | Enable HFSS broadband setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_multifrequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency")(...)  | Enable HFSS multi-frequency setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_single`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single")([...])  | Enable HFSS single frequency setup.  |  
| [`SetupHFSSAuto.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache")(...[, ...])  | Enable an expression cache.  |  
| [`SetupHFSSAuto.get_derivative_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables")()  | Return Derivative Enabled variables.  |  
| [`SetupHFSSAuto.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile")()  | Solution profile.  |  
| [`SetupHFSSAuto.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data")([...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`SetupHFSSAuto.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`SetupHFSSAuto.set_tuning_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset")(offsets)  | Set derivative variable to a specific offset value.  |  
| [`SetupHFSSAuto.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`SetupHFSSAuto.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSSAuto.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSSAuto.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`SetupHFSSAuto.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`SetupHFSSAuto.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupHFSSAuto.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children")  | Retrieve children.  |  
| [`SetupHFSSAuto.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command")  | Command of the modeler hystory if available.  |  
| [`SetupHFSSAuto.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`SetupHFSSAuto.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved")  | Verify if solutions are available for given setup.  |  
| [`SetupHFSSAuto.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name")  | Name.  |  
| [`SetupHFSSAuto.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule")  | Analysis module.  |  
| [`SetupHFSSAuto.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties")  | Properties data.  |  
| [`SetupHFSSAuto.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props")  | Properties of the setup.  |  
| [`SetupHFSSAuto.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir")  | Shortcut for dir(self).  |  
| [`SetupHFSSAuto.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps")  | Retrieve sweeps.  |  
# SetupHFSSAuto 

class ansys.aedt.core.modules.solve_setup.SetupHFSSAuto(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates an HFSS Auto setup. 

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
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1", setup_type="HFSSDrivenAuto")

```
Copy to clipboard
Methods  
| [`SetupHFSSAuto.add_derivatives`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives")(derivative_list)  | Add derivatives to the setup.  |  
| --- | --- |  
| [`SetupHFSSAuto.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link")(design[, ...])  | Import mesh from a source design solution to the target design.  |  
| [`SetupHFSSAuto.add_subrange`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange")(range_type, start)  | Add a subrange to the sweep.  |  
| [`SetupHFSSAuto.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupHFSSAuto.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`SetupHFSSAuto.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report")([expressions, ...])  | Create a report in AEDT.  |  
| [`SetupHFSSAuto.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete")()  | Delete actual Setup.  |  
| [`SetupHFSSAuto.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable")()  | Disable a setup.  |  
| [`SetupHFSSAuto.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable")()  | Enable a setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_broadband`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband")(...)  | Enable HFSS broadband setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_multifrequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency")(...)  | Enable HFSS multi-frequency setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_single`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single")([...])  | Enable HFSS single frequency setup.  |  
| [`SetupHFSSAuto.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache")(...[, ...])  | Enable an expression cache.  |  
| [`SetupHFSSAuto.get_derivative_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables")()  | Return Derivative Enabled variables.  |  
| [`SetupHFSSAuto.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile")()  | Solution profile.  |  
| [`SetupHFSSAuto.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data")([...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`SetupHFSSAuto.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`SetupHFSSAuto.set_tuning_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset")(offsets)  | Set derivative variable to a specific offset value.  |  
| [`SetupHFSSAuto.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`SetupHFSSAuto.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSSAuto.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSSAuto.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`SetupHFSSAuto.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`SetupHFSSAuto.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupHFSSAuto.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children")  | Retrieve children.  |  
| [`SetupHFSSAuto.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command")  | Command of the modeler hystory if available.  |  
| [`SetupHFSSAuto.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`SetupHFSSAuto.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved")  | Verify if solutions are available for given setup.  |  
| [`SetupHFSSAuto.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name")  | Name.  |  
| [`SetupHFSSAuto.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule")  | Analysis module.  |  
| [`SetupHFSSAuto.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties")  | Properties data.  |  
| [`SetupHFSSAuto.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props")  | Properties of the setup.  |  
| [`SetupHFSSAuto.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir")  | Shortcut for dir(self).  |  
| [`SetupHFSSAuto.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps")  | Retrieve sweeps.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.rst.txt)

# SetupHFSSAuto 

class ansys.aedt.core.modules.solve_setup.SetupHFSSAuto(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates an HFSS Auto setup. 

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
>>> import ansys.aedt.core
>>> hfss = ansys.aedt.core.Hfss()
>>> setup1 = hfss.create_setup(name="Setup1", setup_type="HFSSDrivenAuto")

```
Copy to clipboard
Methods  
| [`SetupHFSSAuto.add_derivatives`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_derivatives")(derivative_list)  | Add derivatives to the setup.  |  
| --- | --- |  
| [`SetupHFSSAuto.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_mesh_link")(design[, ...])  | Import mesh from a source design solution to the target design.  |  
| [`SetupHFSSAuto.add_subrange`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.add_subrange")(range_type, start)  | Add a subrange to the sweep.  |  
| [`SetupHFSSAuto.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupHFSSAuto.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`SetupHFSSAuto.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.create_report")([expressions, ...])  | Create a report in AEDT.  |  
| [`SetupHFSSAuto.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.delete")()  | Delete actual Setup.  |  
| [`SetupHFSSAuto.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.disable")()  | Disable a setup.  |  
| [`SetupHFSSAuto.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable")()  | Enable a setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_broadband`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_broadband")(...)  | Enable HFSS broadband setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_multifrequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_multifrequency")(...)  | Enable HFSS multi-frequency setup.  |  
| [`SetupHFSSAuto.enable_adaptive_setup_single`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_adaptive_setup_single")([...])  | Enable HFSS single frequency setup.  |  
| [`SetupHFSSAuto.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.enable_expression_cache")(...[, ...])  | Enable an expression cache.  |  
| [`SetupHFSSAuto.get_derivative_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_derivative_variables")()  | Return Derivative Enabled variables.  |  
| [`SetupHFSSAuto.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_profile")()  | Solution profile.  |  
| [`SetupHFSSAuto.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.get_solution_data")([...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`SetupHFSSAuto.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`SetupHFSSAuto.set_tuning_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.set_tuning_offset")(offsets)  | Set derivative variable to a specific offset value.  |  
| [`SetupHFSSAuto.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`SetupHFSSAuto.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSSAuto.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSSAuto.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`SetupHFSSAuto.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.update_property")(prop_name, ...)  | Update the property of the binary tree node.  |  
Attributes  
| [`SetupHFSSAuto.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupHFSSAuto.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.children")  | Retrieve children.  |  
| [`SetupHFSSAuto.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.command")  | Command of the modeler hystory if available.  |  
| [`SetupHFSSAuto.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`SetupHFSSAuto.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.is_solved")  | Verify if solutions are available for given setup.  |  
| [`SetupHFSSAuto.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.name")  | Name.  |  
| [`SetupHFSSAuto.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.omodule")  | Analysis module.  |  
| [`SetupHFSSAuto.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.properties")  | Properties data.  |  
| [`SetupHFSSAuto.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.props")  | Properties of the setup.  |  
| [`SetupHFSSAuto.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.public_dir")  | Shortcut for dir(self).  |  
| [`SetupHFSSAuto.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.sweeps")  | Retrieve sweeps.  |