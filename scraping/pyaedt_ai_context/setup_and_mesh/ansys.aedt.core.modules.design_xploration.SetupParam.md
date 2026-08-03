---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# SetupParam 

class ansys.aedt.core.modules.design_xploration.SetupParam(_p_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _dictinputs =None_, _optim_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'OptiParametric'_) 
    
Sets up a parametric analysis in Optimetrics.
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupParam
>>> obj = SetupParam()

```
Copy to clipboard
Methods  
| [`SetupParam.add_calculation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation.html#ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation "ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation")(calculation[, ...])  | Add a calculation to the setup.  |  
| --- | --- |  
| [`SetupParam.add_variation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_variation.html#ansys.aedt.core.modules.design_xploration.SetupParam.add_variation "ansys.aedt.core.modules.design_xploration.SetupParam.add_variation")(sweep_variable, ...)  | Add a variation to an existing parametric setup.  |  
| [`SetupParam.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.analyze.html#ansys.aedt.core.modules.design_xploration.SetupParam.analyze "ansys.aedt.core.modules.design_xploration.SetupParam.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupParam.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.create.html#ansys.aedt.core.modules.design_xploration.SetupParam.create "ansys.aedt.core.modules.design_xploration.SetupParam.create")()  | Create a setup.  |  
| [`SetupParam.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.delete.html#ansys.aedt.core.modules.design_xploration.SetupParam.delete "ansys.aedt.core.modules.design_xploration.SetupParam.delete")()  | Delete a defined Optimetrics Setup.  |  
| [`SetupParam.export_to_csv`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv.html#ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv "ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv")(output_file)  | Export the current Parametric Setup to csv.  |  
| [`SetupParam.sync_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables.html#ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables "ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables")(variables[, sync_n])  | Sync variable variations in an existing parametric setup.  |  
| [`SetupParam.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.update.html#ansys.aedt.core.modules.design_xploration.SetupParam.update "ansys.aedt.core.modules.design_xploration.SetupParam.update")([update_dictionary])  | Update the setup based on stored properties.  |  
Attributes  
| [`SetupParam.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.available_properties.html#ansys.aedt.core.modules.design_xploration.SetupParam.available_properties "ansys.aedt.core.modules.design_xploration.SetupParam.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupParam.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.public_dir.html#ansys.aedt.core.modules.design_xploration.SetupParam.public_dir "ansys.aedt.core.modules.design_xploration.SetupParam.public_dir")  | Shortcut for dir(self).  |  
# SetupParam 

class ansys.aedt.core.modules.design_xploration.SetupParam(_p_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _dictinputs =None_, _optim_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'OptiParametric'_) 
    
Sets up a parametric analysis in Optimetrics.
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupParam
>>> obj = SetupParam()

```
Copy to clipboard
Methods  
| [`SetupParam.add_calculation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation.html#ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation "ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation")(calculation[, ...])  | Add a calculation to the setup.  |  
| --- | --- |  
| [`SetupParam.add_variation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_variation.html#ansys.aedt.core.modules.design_xploration.SetupParam.add_variation "ansys.aedt.core.modules.design_xploration.SetupParam.add_variation")(sweep_variable, ...)  | Add a variation to an existing parametric setup.  |  
| [`SetupParam.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.analyze.html#ansys.aedt.core.modules.design_xploration.SetupParam.analyze "ansys.aedt.core.modules.design_xploration.SetupParam.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupParam.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.create.html#ansys.aedt.core.modules.design_xploration.SetupParam.create "ansys.aedt.core.modules.design_xploration.SetupParam.create")()  | Create a setup.  |  
| [`SetupParam.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.delete.html#ansys.aedt.core.modules.design_xploration.SetupParam.delete "ansys.aedt.core.modules.design_xploration.SetupParam.delete")()  | Delete a defined Optimetrics Setup.  |  
| [`SetupParam.export_to_csv`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv.html#ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv "ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv")(output_file)  | Export the current Parametric Setup to csv.  |  
| [`SetupParam.sync_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables.html#ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables "ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables")(variables[, sync_n])  | Sync variable variations in an existing parametric setup.  |  
| [`SetupParam.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.update.html#ansys.aedt.core.modules.design_xploration.SetupParam.update "ansys.aedt.core.modules.design_xploration.SetupParam.update")([update_dictionary])  | Update the setup based on stored properties.  |  
Attributes  
| [`SetupParam.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.available_properties.html#ansys.aedt.core.modules.design_xploration.SetupParam.available_properties "ansys.aedt.core.modules.design_xploration.SetupParam.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupParam.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.public_dir.html#ansys.aedt.core.modules.design_xploration.SetupParam.public_dir "ansys.aedt.core.modules.design_xploration.SetupParam.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.rst.txt)

# SetupParam 

class ansys.aedt.core.modules.design_xploration.SetupParam(_p_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _dictinputs =None_, _optim_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'OptiParametric'_) 
    
Sets up a parametric analysis in Optimetrics.
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupParam
>>> obj = SetupParam()

```
Copy to clipboard
Methods  
| [`SetupParam.add_calculation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation.html#ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation "ansys.aedt.core.modules.design_xploration.SetupParam.add_calculation")(calculation[, ...])  | Add a calculation to the setup.  |  
| --- | --- |  
| [`SetupParam.add_variation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.add_variation.html#ansys.aedt.core.modules.design_xploration.SetupParam.add_variation "ansys.aedt.core.modules.design_xploration.SetupParam.add_variation")(sweep_variable, ...)  | Add a variation to an existing parametric setup.  |  
| [`SetupParam.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.analyze.html#ansys.aedt.core.modules.design_xploration.SetupParam.analyze "ansys.aedt.core.modules.design_xploration.SetupParam.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupParam.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.create.html#ansys.aedt.core.modules.design_xploration.SetupParam.create "ansys.aedt.core.modules.design_xploration.SetupParam.create")()  | Create a setup.  |  
| [`SetupParam.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.delete.html#ansys.aedt.core.modules.design_xploration.SetupParam.delete "ansys.aedt.core.modules.design_xploration.SetupParam.delete")()  | Delete a defined Optimetrics Setup.  |  
| [`SetupParam.export_to_csv`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv.html#ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv "ansys.aedt.core.modules.design_xploration.SetupParam.export_to_csv")(output_file)  | Export the current Parametric Setup to csv.  |  
| [`SetupParam.sync_variables`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables.html#ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables "ansys.aedt.core.modules.design_xploration.SetupParam.sync_variables")(variables[, sync_n])  | Sync variable variations in an existing parametric setup.  |  
| [`SetupParam.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.update.html#ansys.aedt.core.modules.design_xploration.SetupParam.update "ansys.aedt.core.modules.design_xploration.SetupParam.update")([update_dictionary])  | Update the setup based on stored properties.  |  
Attributes  
| [`SetupParam.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.available_properties.html#ansys.aedt.core.modules.design_xploration.SetupParam.available_properties "ansys.aedt.core.modules.design_xploration.SetupParam.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupParam.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.public_dir.html#ansys.aedt.core.modules.design_xploration.SetupParam.public_dir "ansys.aedt.core.modules.design_xploration.SetupParam.public_dir")  | Shortcut for dir(self).  |