---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# SetupHFSS 

class ansys.aedt.core.modules.solve_setup.SetupHFSS(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates an HFSS setup. 

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
>>> h3d = Hfss()
>>> setup = h3d.create_setup()

```
Copy to clipboard
Methods  
| [`SetupHFSS.add_derivatives`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives")(derivative_list)  | Add derivatives to the setup.  |  
| --- | --- |  
| [`SetupHFSS.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link")(design[, solution, ...])  | Import mesh from a source design solution to the target design.  |  
| [`SetupHFSS.add_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep")([name, sweep_type])  | Add a sweep to the project.  |  
| [`SetupHFSS.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze "ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupHFSS.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create "ansys.aedt.core.modules.solve_setup.SetupHFSS.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`SetupHFSS.create_frequency_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep")([unit, ...])  | Create a sweep with the specified number of points.  |  
| [`SetupHFSS.create_linear_step_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep")([unit, ...])  | Create a Sweep with a specified frequency step.  |  
| [`SetupHFSS.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report")([expressions, ...])  | Create a report in AEDT.  |  
| [`SetupHFSS.create_single_point_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep")([unit, ...])  | Create a Sweep with a single frequency point.  |  
| [`SetupHFSS.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.delete.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.delete "ansys.aedt.core.modules.solve_setup.SetupHFSS.delete")()  | Delete actual Setup.  |  
| [`SetupHFSS.delete_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep")(name)  | Delete a sweep.  |  
| [`SetupHFSS.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.disable.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.disable "ansys.aedt.core.modules.solve_setup.SetupHFSS.disable")()  | Disable a setup.  |  
| [`SetupHFSS.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable")()  | Enable a setup.  |  
| [`SetupHFSS.enable_adaptive_setup_broadband`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband")(...)  | Enable HFSS broadband setup.  |  
| [`SetupHFSS.enable_adaptive_setup_multifrequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency")(...)  | Enable HFSS multi-frequency setup.  |  
| [`SetupHFSS.enable_adaptive_setup_single`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single")([...])  | Enable HFSS single frequency setup.  |  
| [`SetupHFSS.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache")(expressions)  | Enable an expression cache.  |  
| [`SetupHFSS.get_derivative_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables")()  | Return Derivative Enabled variables.  |  
| [`SetupHFSS.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile")()  | Solution profile.  |  
| [`SetupHFSS.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data")([expressions, ...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`SetupHFSS.get_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep")([name])  | Return frequency sweep object of a given sweep.  |  
| [`SetupHFSS.get_sweep_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names")()  | Get the names of all sweeps in a given analysis setup.  |  
| [`SetupHFSS.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree "ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`SetupHFSS.set_tuning_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset "ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset")(offsets)  | Set derivative variable to a specific offset value.  |  
| [`SetupHFSS.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`SetupHFSS.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSS.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSS.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.update.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.update "ansys.aedt.core.modules.solve_setup.SetupHFSS.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`SetupHFSS.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property "ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
| [`SetupHFSS.use_matrix_convergence`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence "ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence")([...])  | Enable Matrix Convergence criteria.  |  
Attributes  
| [`SetupHFSS.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties "ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupHFSS.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.children.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.children "ansys.aedt.core.modules.solve_setup.SetupHFSS.children")  | Retrieve children.  |  
| [`SetupHFSS.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.command.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.command "ansys.aedt.core.modules.solve_setup.SetupHFSS.command")  | Command of the modeler hystory if available.  |  
| [`SetupHFSS.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics "ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`SetupHFSS.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved "ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved")  | Verify if solutions are available for given setup.  |  
| [`SetupHFSS.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.name.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.name "ansys.aedt.core.modules.solve_setup.SetupHFSS.name")  | Name.  |  
| [`SetupHFSS.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule "ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule")  | Analysis module.  |  
| [`SetupHFSS.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.properties "ansys.aedt.core.modules.solve_setup.SetupHFSS.properties")  | Properties data.  |  
| [`SetupHFSS.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.props.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.props "ansys.aedt.core.modules.solve_setup.SetupHFSS.props")  | Properties of the setup.  |  
| [`SetupHFSS.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir "ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir")  | Shortcut for dir(self).  |  
| [`SetupHFSS.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps "ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps")  | Retrieve sweeps.  |  
# SetupHFSS 

class ansys.aedt.core.modules.solve_setup.SetupHFSS(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates an HFSS setup. 

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
>>> h3d = Hfss()
>>> setup = h3d.create_setup()

```
Copy to clipboard
Methods  
| [`SetupHFSS.add_derivatives`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives")(derivative_list)  | Add derivatives to the setup.  |  
| --- | --- |  
| [`SetupHFSS.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link")(design[, solution, ...])  | Import mesh from a source design solution to the target design.  |  
| [`SetupHFSS.add_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep")([name, sweep_type])  | Add a sweep to the project.  |  
| [`SetupHFSS.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze "ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupHFSS.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create "ansys.aedt.core.modules.solve_setup.SetupHFSS.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`SetupHFSS.create_frequency_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep")([unit, ...])  | Create a sweep with the specified number of points.  |  
| [`SetupHFSS.create_linear_step_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep")([unit, ...])  | Create a Sweep with a specified frequency step.  |  
| [`SetupHFSS.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report")([expressions, ...])  | Create a report in AEDT.  |  
| [`SetupHFSS.create_single_point_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep")([unit, ...])  | Create a Sweep with a single frequency point.  |  
| [`SetupHFSS.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.delete.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.delete "ansys.aedt.core.modules.solve_setup.SetupHFSS.delete")()  | Delete actual Setup.  |  
| [`SetupHFSS.delete_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep")(name)  | Delete a sweep.  |  
| [`SetupHFSS.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.disable.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.disable "ansys.aedt.core.modules.solve_setup.SetupHFSS.disable")()  | Disable a setup.  |  
| [`SetupHFSS.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable")()  | Enable a setup.  |  
| [`SetupHFSS.enable_adaptive_setup_broadband`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband")(...)  | Enable HFSS broadband setup.  |  
| [`SetupHFSS.enable_adaptive_setup_multifrequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency")(...)  | Enable HFSS multi-frequency setup.  |  
| [`SetupHFSS.enable_adaptive_setup_single`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single")([...])  | Enable HFSS single frequency setup.  |  
| [`SetupHFSS.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache")(expressions)  | Enable an expression cache.  |  
| [`SetupHFSS.get_derivative_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables")()  | Return Derivative Enabled variables.  |  
| [`SetupHFSS.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile")()  | Solution profile.  |  
| [`SetupHFSS.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data")([expressions, ...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`SetupHFSS.get_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep")([name])  | Return frequency sweep object of a given sweep.  |  
| [`SetupHFSS.get_sweep_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names")()  | Get the names of all sweeps in a given analysis setup.  |  
| [`SetupHFSS.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree "ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`SetupHFSS.set_tuning_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset "ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset")(offsets)  | Set derivative variable to a specific offset value.  |  
| [`SetupHFSS.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`SetupHFSS.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSS.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSS.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.update.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.update "ansys.aedt.core.modules.solve_setup.SetupHFSS.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`SetupHFSS.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property "ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
| [`SetupHFSS.use_matrix_convergence`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence "ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence")([...])  | Enable Matrix Convergence criteria.  |  
Attributes  
| [`SetupHFSS.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties "ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupHFSS.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.children.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.children "ansys.aedt.core.modules.solve_setup.SetupHFSS.children")  | Retrieve children.  |  
| [`SetupHFSS.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.command.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.command "ansys.aedt.core.modules.solve_setup.SetupHFSS.command")  | Command of the modeler hystory if available.  |  
| [`SetupHFSS.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics "ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`SetupHFSS.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved "ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved")  | Verify if solutions are available for given setup.  |  
| [`SetupHFSS.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.name.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.name "ansys.aedt.core.modules.solve_setup.SetupHFSS.name")  | Name.  |  
| [`SetupHFSS.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule "ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule")  | Analysis module.  |  
| [`SetupHFSS.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.properties "ansys.aedt.core.modules.solve_setup.SetupHFSS.properties")  | Properties data.  |  
| [`SetupHFSS.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.props.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.props "ansys.aedt.core.modules.solve_setup.SetupHFSS.props")  | Properties of the setup.  |  
| [`SetupHFSS.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir "ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir")  | Shortcut for dir(self).  |  
| [`SetupHFSS.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps "ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps")  | Retrieve sweeps.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.rst.txt)

# SetupHFSS 

class ansys.aedt.core.modules.solve_setup.SetupHFSS(_app_ , _solution_type_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'MySetupAuto'_, _is_new_setup : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Initializes, creates, and updates an HFSS setup. 

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
>>> h3d = Hfss()
>>> setup = h3d.create_setup()

```
Copy to clipboard
Methods  
| [`SetupHFSS.add_derivatives`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_derivatives")(derivative_list)  | Add derivatives to the setup.  |  
| --- | --- |  
| [`SetupHFSS.add_mesh_link`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_mesh_link")(design[, solution, ...])  | Import mesh from a source design solution to the target design.  |  
| [`SetupHFSS.add_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.add_sweep")([name, sweep_type])  | Add a sweep to the project.  |  
| [`SetupHFSS.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze "ansys.aedt.core.modules.solve_setup.SetupHFSS.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupHFSS.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create "ansys.aedt.core.modules.solve_setup.SetupHFSS.create")()  | Add a new setup based on class settings in AEDT.  |  
| [`SetupHFSS.create_frequency_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_frequency_sweep")([unit, ...])  | Create a sweep with the specified number of points.  |  
| [`SetupHFSS.create_linear_step_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_linear_step_sweep")([unit, ...])  | Create a Sweep with a specified frequency step.  |  
| [`SetupHFSS.create_report`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report")([expressions, ...])  | Create a report in AEDT.  |  
| [`SetupHFSS.create_single_point_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.create_single_point_sweep")([unit, ...])  | Create a Sweep with a single frequency point.  |  
| [`SetupHFSS.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.delete.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.delete "ansys.aedt.core.modules.solve_setup.SetupHFSS.delete")()  | Delete actual Setup.  |  
| [`SetupHFSS.delete_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.delete_sweep")(name)  | Delete a sweep.  |  
| [`SetupHFSS.disable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.disable.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.disable "ansys.aedt.core.modules.solve_setup.SetupHFSS.disable")()  | Disable a setup.  |  
| [`SetupHFSS.enable`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable")()  | Enable a setup.  |  
| [`SetupHFSS.enable_adaptive_setup_broadband`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_broadband")(...)  | Enable HFSS broadband setup.  |  
| [`SetupHFSS.enable_adaptive_setup_multifrequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_multifrequency")(...)  | Enable HFSS multi-frequency setup.  |  
| [`SetupHFSS.enable_adaptive_setup_single`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_adaptive_setup_single")([...])  | Enable HFSS single frequency setup.  |  
| [`SetupHFSS.enable_expression_cache`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache "ansys.aedt.core.modules.solve_setup.SetupHFSS.enable_expression_cache")(expressions)  | Enable an expression cache.  |  
| [`SetupHFSS.get_derivative_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_derivative_variables")()  | Return Derivative Enabled variables.  |  
| [`SetupHFSS.get_profile`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_profile")()  | Solution profile.  |  
| [`SetupHFSS.get_solution_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_solution_data")([expressions, ...])  | Get a simulation result from a solved setup and cast it in a `SolutionData` object.  |  
| [`SetupHFSS.get_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep")([name])  | Return frequency sweep object of a given sweep.  |  
| [`SetupHFSS.get_sweep_names`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names "ansys.aedt.core.modules.solve_setup.SetupHFSS.get_sweep_names")()  | Get the names of all sweeps in a given analysis setup.  |  
| [`SetupHFSS.jsonalize_tree`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree "ansys.aedt.core.modules.solve_setup.SetupHFSS.jsonalize_tree")()  | Create dictionary from the Binary Tree.  |  
| [`SetupHFSS.set_tuning_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset "ansys.aedt.core.modules.solve_setup.SetupHFSS.set_tuning_offset")(offsets)  | Set derivative variable to a specific offset value.  |  
| [`SetupHFSS.start_continue_from_previous_setup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup "ansys.aedt.core.modules.solve_setup.SetupHFSS.start_continue_from_previous_setup")(...)  | Start or continue from a previously solved setup.  |  
| [`SetupHFSS.suppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSS.suppress_all")(app)  | Activate suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSS.unsuppress_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all "ansys.aedt.core.modules.solve_setup.SetupHFSS.unsuppress_all")(app)  | Disable suppress option for all the operations contained in the binary tree node.  |  
| [`SetupHFSS.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.update.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.update "ansys.aedt.core.modules.solve_setup.SetupHFSS.update")([properties])  | Update the setup based on either the class argument or a dictionary.  |  
| [`SetupHFSS.update_property`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property "ansys.aedt.core.modules.solve_setup.SetupHFSS.update_property")(prop_name, prop_value)  | Update the property of the binary tree node.  |  
| [`SetupHFSS.use_matrix_convergence`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence "ansys.aedt.core.modules.solve_setup.SetupHFSS.use_matrix_convergence")([...])  | Enable Matrix Convergence criteria.  |  
Attributes  
| [`SetupHFSS.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties "ansys.aedt.core.modules.solve_setup.SetupHFSS.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupHFSS.children`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.children.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.children "ansys.aedt.core.modules.solve_setup.SetupHFSS.children")  | Retrieve children.  |  
| [`SetupHFSS.command`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.command.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.command "ansys.aedt.core.modules.solve_setup.SetupHFSS.command")  | Command of the modeler hystory if available.  |  
| [`SetupHFSS.default_intrinsics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics "ansys.aedt.core.modules.solve_setup.SetupHFSS.default_intrinsics")  | Retrieve default intrinsic for actual setup.  |  
| [`SetupHFSS.is_solved`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved "ansys.aedt.core.modules.solve_setup.SetupHFSS.is_solved")  | Verify if solutions are available for given setup.  |  
| [`SetupHFSS.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.name.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.name "ansys.aedt.core.modules.solve_setup.SetupHFSS.name")  | Name.  |  
| [`SetupHFSS.omodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule "ansys.aedt.core.modules.solve_setup.SetupHFSS.omodule")  | Analysis module.  |  
| [`SetupHFSS.properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.properties.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.properties "ansys.aedt.core.modules.solve_setup.SetupHFSS.properties")  | Properties data.  |  
| [`SetupHFSS.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.props.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.props "ansys.aedt.core.modules.solve_setup.SetupHFSS.props")  | Properties of the setup.  |  
| [`SetupHFSS.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir "ansys.aedt.core.modules.solve_setup.SetupHFSS.public_dir")  | Shortcut for dir(self).  |  
| [`SetupHFSS.sweeps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps.html#ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps "ansys.aedt.core.modules.solve_setup.SetupHFSS.sweeps")  | Retrieve sweeps.  |