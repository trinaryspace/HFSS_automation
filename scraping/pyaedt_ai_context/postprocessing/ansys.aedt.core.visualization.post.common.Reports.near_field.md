---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.near_field.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# near_field 

Reports.near_field(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") 
    
Create a Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.NearField`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.near_field("GainTotal", "Setup : LastAdaptive", "NF_1")
>>> report.primary_sweep = "Phi"
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard
# near_field 

Reports.near_field(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") 
    
Create a Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.NearField`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.near_field("GainTotal", "Setup : LastAdaptive", "NF_1")
>>> report.primary_sweep = "Phi"
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.near_field.rst.txt)

# near_field 

Reports.near_field(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") 
    
Create a Field Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.NearField`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(my_project)
>>> report = hfss.post.reports_by_category.near_field("GainTotal", "Setup : LastAdaptive", "NF_1")
>>> report.primary_sweep = "Phi"
>>> report.create()
>>> solutions = report.get_solution_data()

```
Copy to clipboard