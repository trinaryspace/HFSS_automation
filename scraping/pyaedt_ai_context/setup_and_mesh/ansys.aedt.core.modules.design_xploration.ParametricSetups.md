---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# ParametricSetups 

class ansys.aedt.core.modules.design_xploration.ParametricSetups(_p_app_) 
    
Sets up Parametrics analyses. It includes Parametrics, Sensitivity and Statistical Analysis.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> sensitivity_setups = app.parametrics

```
Copy to clipboard
Methods  
| [`ParametricSetups.add`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.add.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.add "ansys.aedt.core.modules.design_xploration.ParametricSetups.add")(variable, start_point)  | Add a basic sensitivity analysis.  |  
| --- | --- |  
| [`ParametricSetups.add_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file "ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file")(input_file[, ...])  | Add a Parametric setup from either a csv or txt file.  |  
| [`ParametricSetups.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.delete.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.delete "ansys.aedt.core.modules.design_xploration.ParametricSetups.delete")(name)  | Delete a defined Parametric Setup.  |  
Attributes  
| [`ParametricSetups.design_setups`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups "ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups")  | All design setups ordered by name.  |  
| --- | --- |  
| [`ParametricSetups.optimodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule "ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule")  | Optimetrics module.  |  
| [`ParametricSetups.p_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app "ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app")  | Parent.  |  
| [`ParametricSetups.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir "ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir")  | Shortcut for dir(self).  |  
# ParametricSetups 

class ansys.aedt.core.modules.design_xploration.ParametricSetups(_p_app_) 
    
Sets up Parametrics analyses. It includes Parametrics, Sensitivity and Statistical Analysis.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> sensitivity_setups = app.parametrics

```
Copy to clipboard
Methods  
| [`ParametricSetups.add`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.add.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.add "ansys.aedt.core.modules.design_xploration.ParametricSetups.add")(variable, start_point)  | Add a basic sensitivity analysis.  |  
| --- | --- |  
| [`ParametricSetups.add_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file "ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file")(input_file[, ...])  | Add a Parametric setup from either a csv or txt file.  |  
| [`ParametricSetups.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.delete.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.delete "ansys.aedt.core.modules.design_xploration.ParametricSetups.delete")(name)  | Delete a defined Parametric Setup.  |  
Attributes  
| [`ParametricSetups.design_setups`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups "ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups")  | All design setups ordered by name.  |  
| --- | --- |  
| [`ParametricSetups.optimodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule "ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule")  | Optimetrics module.  |  
| [`ParametricSetups.p_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app "ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app")  | Parent.  |  
| [`ParametricSetups.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir "ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.rst.txt)

# ParametricSetups 

class ansys.aedt.core.modules.design_xploration.ParametricSetups(_p_app_) 
    
Sets up Parametrics analyses. It includes Parametrics, Sensitivity and Statistical Analysis.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> sensitivity_setups = app.parametrics

```
Copy to clipboard
Methods  
| [`ParametricSetups.add`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.add.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.add "ansys.aedt.core.modules.design_xploration.ParametricSetups.add")(variable, start_point)  | Add a basic sensitivity analysis.  |  
| --- | --- |  
| [`ParametricSetups.add_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file "ansys.aedt.core.modules.design_xploration.ParametricSetups.add_from_file")(input_file[, ...])  | Add a Parametric setup from either a csv or txt file.  |  
| [`ParametricSetups.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.delete.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.delete "ansys.aedt.core.modules.design_xploration.ParametricSetups.delete")(name)  | Delete a defined Parametric Setup.  |  
Attributes  
| [`ParametricSetups.design_setups`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups "ansys.aedt.core.modules.design_xploration.ParametricSetups.design_setups")  | All design setups ordered by name.  |  
| --- | --- |  
| [`ParametricSetups.optimodule`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule "ansys.aedt.core.modules.design_xploration.ParametricSetups.optimodule")  | Optimetrics module.  |  
| [`ParametricSetups.p_app`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app "ansys.aedt.core.modules.design_xploration.ParametricSetups.p_app")  | Parent.  |  
| [`ParametricSetups.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir.html#ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir "ansys.aedt.core.modules.design_xploration.ParametricSetups.public_dir")  | Shortcut for dir(self).  |