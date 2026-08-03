---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# SetupOpti 

class ansys.aedt.core.modules.design_xploration.SetupOpti(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _dictinputs =None_, _optim_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'OptiDesignExplorer'_) 
    
Sets up an optimization in Opimetrics.
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()

```
Copy to clipboard
Methods  
| [`SetupOpti.add_calculation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation "ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation")(calculation[, ...])  | Add a calculation to the setup.  |  
| --- | --- |  
| [`SetupOpti.add_goal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal "ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal")(calculation, ranges[, ...])  | Add a goal to the setup.  |  
| [`SetupOpti.add_variation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation "ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation")(variable_name, ...)  | Add a new variable as input for the optimization and defines its ranges.  |  
| [`SetupOpti.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.analyze.html#ansys.aedt.core.modules.design_xploration.SetupOpti.analyze "ansys.aedt.core.modules.design_xploration.SetupOpti.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupOpti.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.create.html#ansys.aedt.core.modules.design_xploration.SetupOpti.create "ansys.aedt.core.modules.design_xploration.SetupOpti.create")()  | Create a setup.  |  
| [`SetupOpti.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.delete.html#ansys.aedt.core.modules.design_xploration.SetupOpti.delete "ansys.aedt.core.modules.design_xploration.SetupOpti.delete")()  | Delete a defined Optimetrics Setup.  |  
| [`SetupOpti.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.update.html#ansys.aedt.core.modules.design_xploration.SetupOpti.update "ansys.aedt.core.modules.design_xploration.SetupOpti.update")([update_dictionary])  | Update the setup based on stored properties.  |  
Attributes  
| [`SetupOpti.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties.html#ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties "ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupOpti.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir.html#ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir "ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir")  | Shortcut for dir(self).  |  
# SetupOpti 

class ansys.aedt.core.modules.design_xploration.SetupOpti(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _dictinputs =None_, _optim_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'OptiDesignExplorer'_) 
    
Sets up an optimization in Opimetrics.
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()

```
Copy to clipboard
Methods  
| [`SetupOpti.add_calculation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation "ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation")(calculation[, ...])  | Add a calculation to the setup.  |  
| --- | --- |  
| [`SetupOpti.add_goal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal "ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal")(calculation, ranges[, ...])  | Add a goal to the setup.  |  
| [`SetupOpti.add_variation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation "ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation")(variable_name, ...)  | Add a new variable as input for the optimization and defines its ranges.  |  
| [`SetupOpti.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.analyze.html#ansys.aedt.core.modules.design_xploration.SetupOpti.analyze "ansys.aedt.core.modules.design_xploration.SetupOpti.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupOpti.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.create.html#ansys.aedt.core.modules.design_xploration.SetupOpti.create "ansys.aedt.core.modules.design_xploration.SetupOpti.create")()  | Create a setup.  |  
| [`SetupOpti.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.delete.html#ansys.aedt.core.modules.design_xploration.SetupOpti.delete "ansys.aedt.core.modules.design_xploration.SetupOpti.delete")()  | Delete a defined Optimetrics Setup.  |  
| [`SetupOpti.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.update.html#ansys.aedt.core.modules.design_xploration.SetupOpti.update "ansys.aedt.core.modules.design_xploration.SetupOpti.update")([update_dictionary])  | Update the setup based on stored properties.  |  
Attributes  
| [`SetupOpti.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties.html#ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties "ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupOpti.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir.html#ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir "ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.rst.txt)

# SetupOpti 

class ansys.aedt.core.modules.design_xploration.SetupOpti(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _dictinputs =None_, _optim_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'OptiDesignExplorer'_) 
    
Sets up an optimization in Opimetrics.
Examples

```
>>> from ansys.aedt.core.modules.design_xploration import SetupOpti
>>> obj = SetupOpti()

```
Copy to clipboard
Methods  
| [`SetupOpti.add_calculation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation "ansys.aedt.core.modules.design_xploration.SetupOpti.add_calculation")(calculation[, ...])  | Add a calculation to the setup.  |  
| --- | --- |  
| [`SetupOpti.add_goal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal "ansys.aedt.core.modules.design_xploration.SetupOpti.add_goal")(calculation, ranges[, ...])  | Add a goal to the setup.  |  
| [`SetupOpti.add_variation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation.html#ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation "ansys.aedt.core.modules.design_xploration.SetupOpti.add_variation")(variable_name, ...)  | Add a new variable as input for the optimization and defines its ranges.  |  
| [`SetupOpti.analyze`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.analyze.html#ansys.aedt.core.modules.design_xploration.SetupOpti.analyze "ansys.aedt.core.modules.design_xploration.SetupOpti.analyze")([cores, tasks, gpus, ...])  | Solve the active design.  |  
| [`SetupOpti.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.create.html#ansys.aedt.core.modules.design_xploration.SetupOpti.create "ansys.aedt.core.modules.design_xploration.SetupOpti.create")()  | Create a setup.  |  
| [`SetupOpti.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.delete.html#ansys.aedt.core.modules.design_xploration.SetupOpti.delete "ansys.aedt.core.modules.design_xploration.SetupOpti.delete")()  | Delete a defined Optimetrics Setup.  |  
| [`SetupOpti.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.update.html#ansys.aedt.core.modules.design_xploration.SetupOpti.update "ansys.aedt.core.modules.design_xploration.SetupOpti.update")([update_dictionary])  | Update the setup based on stored properties.  |  
Attributes  
| [`SetupOpti.available_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties.html#ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties "ansys.aedt.core.modules.design_xploration.SetupOpti.available_properties")  | Available properties.  |  
| --- | --- |  
| [`SetupOpti.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir.html#ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir "ansys.aedt.core.modules.design_xploration.SetupOpti.public_dir")  | Shortcut for dir(self).  |